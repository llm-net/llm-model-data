#!/usr/bin/env python3
"""Validate local facts and prepare a reviewable candidate; never publish or approve."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {"providers", "schemas", "evidence", "docs", "scripts", "tests", "templates", ".github"}
ROOT_FILES = {"AGENTS.md", "README.md", "requirements.txt", ".gitignore"}
class CatalogError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CatalogError(message)


def json_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=json_pairs)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def unique(items, field, label):
    values = [x[field] for x in items]
    require(len(values) == len(set(values)), f"{label}: duplicate {field}")
    return set(values)


def local_evidence(root, value):
    require(isinstance(value, str), "verified record needs evidence")
    path = Path(value)
    require(not path.is_absolute() and ".." not in path.parts and path.parts[0] == "evidence",
            f"evidence must be repository-relative under evidence/: {value}")
    target = root / path
    require(target.is_file() and not target.is_symlink(), f"missing evidence: {value}")
    require(target.resolve().is_relative_to((root / "evidence").resolve()), "evidence escapes repository")


def walk_verifications(root, node, source_ids):
    if isinstance(node, dict):
        if "verification" in node:
            v = node["verification"]
            require(set(v["source_ids"]) <= source_ids, "unknown source_id")
            require(len(v["source_ids"]) == len(set(v["source_ids"])), "duplicate source_id")
            if v["status"] == "verified":
                require(v["checked_at"] is not None and v["source_ids"], "verified record needs date and sources")
                require(date(v["checked_at"]) <= datetime.now(timezone.utc), "checked_at is in the future")
                local_evidence(root, v["evidence"])
            else:
                require(v["checked_at"] is None, "needs_review must not claim a successful checked_at")
                if v["evidence"] is not None:
                    local_evidence(root, v["evidence"])
        for value in node.values():
            walk_verifications(root, value, source_ids)
    elif isinstance(node, list):
        for value in node:
            walk_verifications(root, value, source_ids)


def check_prices(value, purpose, meters=None):
    meters = meters or read_json(ROOT / "schemas/meters.json")
    rules = value["rules"]
    require(bool(rules) == (value["status"] == "published"), "unknown/not_applicable cannot contain rates; published needs rules")
    unique(rules, "id", "price rules")
    allowed = {"usage": {"public_list", "provider_credit_rate"}, "reference": {"reference"}, "plan": {"subscription_fee"}}[purpose]
    require(len(rules) <= 1, "one price baseline per model/plan")
    for rule in rules:
        require(rule["basis"] in allowed, f"{purpose}: wrong price basis")
        if value["verification"]["status"] == "verified":
            require(rule["verification"]["status"] == "verified", "verified price set contains unverified rule")
        require((rule["reference_origin"] is not None) == (purpose == "reference"), "reference_origin is required only for reference rates")
        require((rule["billing_period"] is not None) == (purpose == "plan"), "billing_period is required only for plan price")
        require((rule["charge_unit"] is not None) == (purpose == "plan"), "charge_unit is required only for plan price")
        if rule["effective_from"] and rule["effective_until"]:
            require(date(rule["effective_from"]) < date(rule["effective_until"]), "invalid effective interval")
        unique(rule["rates"], "meter", "rates")
        for rate in rule["rates"]:
            require(rate["meter"] in meters and meters[rate["meter"]]["unit"] == rate["unit"], "meter/unit mismatch")
            require(Decimal(rate["amount"]) >= 0, "negative price")
            if Decimal(rate["amount"]) == 0:
                require(rule["verification"]["status"] == "verified", "zero price requires verified evidence")
            require((rate["unit"] == "subscription") == (purpose == "plan"), "subscription unit only belongs to plan price")
            if rate["unit"] not in {"token", "subscription", "credit", "request"}:
                require("quantity" in rate, "multimodal rate requires explicit quantity metadata")
            if "quantity" in rate:
                q = rate["quantity"]
                if q["source"] in {"provider_usage", "request"}:
                    require(q["fields"], "quantity source requires fields")
                if q["source"] == "unknown":
                    require(not q["fields"], "unknown quantity source cannot claim fields")
                if q["rounding"] in {"ceil", "floor"}:
                    require(q["increment"] is not None and Decimal(q["increment"]) > 0, "rounding needs positive increment")
                else:
                    require(q["increment"] is None, "no increment for none/unknown rounding")


def check_offering(root, data, provider):
    require(data["provider_id"] == provider["id"], "provider_id mismatch")
    source_ids = {s["id"] for s in provider["sources"]}
    walk_verifications(root, data, source_ids)
    plan_ids = unique(data["plans"], "id", "plans")
    model_ids = unique(data["models"], "id", "models")
    requests = [m["request_id"] for m in data["models"] if m["request_id"] is not None]
    require(len(requests) == len(set(requests)), "duplicate request_id within offering")
    aliases = {}
    meters = read_json(root / "schemas/meters.json")
    excluded = set(provider.get("excluded_request_ids", []))
    excluded_local_ids = {re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") for value in excluded}
    for m in data["models"]:
        require(m["request_id"] not in excluded and m["id"] not in excluded_local_ids,
                "model is explicitly excluded from collection")
        if provider["id"] == "siliconflow":
            require(m["availability"] != "retired", "SiliconFlow retired models must be removed")
        if data["kind"] in {"api_subscription", "tool_subscription"}:
            require(m["usage_prices"]["status"] == "not_applicable" and not m["usage_prices"]["rules"],
                    "subscription models use reference prices only")
            require(all(r["currency"] != "CREDIT" for r in m["reference_prices"]["rules"]),
                    "subscription reference must use pay-as-you-go currency, not credits")
        require(set(m["plan_ids"]) <= plan_ids, "model references unknown plan")
        if m["alias_of"] is not None:
            require(m["alias_of"] in model_ids and m["alias_of"] != m["id"], "unknown/self model alias")
            aliases[m["id"]] = m["alias_of"]
        check_prices(m["usage_prices"], "usage", meters)
        check_prices(m["reference_prices"], "reference", meters)
        require(sum(len(m[key]["rules"]) for key in ("usage_prices", "reference_prices")) <= 1,
                "one price baseline per model across usage/reference")
    for start in aliases:
        seen = set()
        while start in aliases:
            require(start not in seen, "model alias cycle")
            seen.add(start)
            start = aliases[start]
    for plan in data["plans"]:
        check_prices(plan["prices"], "plan", meters)
        for q in plan["quotas"]:
            w = q["window"]
            if w["timezone"]:
                try:
                    ZoneInfo(w["timezone"])
                except ZoneInfoNotFoundError as exc:
                    raise CatalogError("invalid quota timezone") from exc
            if w["duration"]:
                    require(re.fullmatch(r"P(?:[1-9][0-9]*[DWMY]|T[1-9][0-9]*[HMS])", w["duration"]), "unsupported quota duration")


def validate(root=ROOT):
    validators = {}
    for kind in ("provider", "catalog"):
        schema = read_json(root / f"schemas/{kind}.schema.json")
        Draft202012Validator.check_schema(schema)
        validators[kind] = Draft202012Validator(schema, format_checker=FormatChecker())
    meters = read_json(root / "schemas/meters.json")
    catalog_schema = read_json(root / "schemas/catalog.schema.json")
    require(set(meters) == set(catalog_schema["$defs"]["rate"]["properties"]["meter"]["enum"]),
            "meter registry/schema drift")
    stats = Counter()
    provider_files = sorted((root / "providers").glob("*/provider.json"))
    require(provider_files, "no providers")
    allowed_json = set(provider_files)
    for p in provider_files:
        provider = read_json(p)
        validators["provider"].validate(provider)
        require(provider["id"] == p.parent.name, f"provider directory mismatch: {p}")
        unique(provider["sources"], "id", "sources")
        require((p.parent / "README.md").is_file(), "provider README missing")
        stats["providers"] += 1
        files = sorted((p.parent / "offerings").glob("*/catalog.json"))
        require(files, f"provider has no offerings: {p}")
        for f in files:
            allowed_json.add(f)
            data = read_json(f)
            try:
                validators["catalog"].validate(data)
                require(data["id"] == f.parent.name, "offering directory mismatch")
                check_offering(root, data, provider)
            except Exception as exc:
                raise CatalogError(f"{f.relative_to(root)}: {exc}") from exc
            stats["offerings"] += 1
            stats["models"] += len(data["models"])
            stats["plans"] += len(data["plans"])
            for m in data["models"]:
                stats["models_" + m["verification"]["status"]] += 1
                for purpose in ("usage_prices", "reference_prices"):
                    stats[purpose + "_" + m[purpose]["status"]] += 1
    require(set((root / "providers").rglob("*.json")) == allowed_json, "unrecognized/orphan JSON under providers")
    imp = read_json(root / "evidence/imports/manifest.json")
    for item in imp["inputs"].values():
        local_evidence(root, item["snapshot"])
        require(sha((root / item["snapshot"]).read_bytes()) == item["sha256"], "migration snapshot hash mismatch")
    return dict(sorted(stats.items()))


def included(name):
    p = Path(name)
    return (name in ROOT_FILES or p.parts[0] in DIRECTORIES) and "__pycache__" not in p.parts and p.suffix != ".pyc"


def current_files(root):
    files = {}
    for prefix in sorted(DIRECTORIES | ROOT_FILES):
        path = root / prefix
        require(not path.is_symlink(), f"symlinks not supported in review input: {path}")
        paths = [path] if path.is_file() else sorted(path.rglob("*")) if path.is_dir() else []
        for p in paths:
            require(not p.is_symlink(), f"symlinks not supported in review input: {p}")
            if p.is_file() and included(p.relative_to(root).as_posix()):
                files[p.relative_to(root).as_posix()] = p.read_bytes()
    return dict(sorted(files.items()))


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root)


def base_files(root, ref):
    commit = git(root, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()
    paths = git(root, "ls-tree", "-r", "--name-only", "-z", commit).decode().split("\0")
    return commit, {p: git(root, "show", f"{commit}:{p}") for p in paths if p and included(p)}


def make_diff(old, new):
    chunks = []
    for p in sorted(old.keys() | new.keys()):
        if old.get(p) == new.get(p):
            continue
        lines = difflib.unified_diff(
            old.get(p, b"").decode().splitlines(keepends=True),
            new.get(p, b"").decode().splitlines(keepends=True),
            fromfile="a/" + p if p in old else "/dev/null",
            tofile="b/" + p if p in new else "/dev/null")
        for line in lines:
            chunks.append(line)
            if not line.endswith("\n"):
                chunks.append("\n\\ No newline at end of file\n")
    return "".join(chunks)


def summarize_changes(old, new):
    lines = []
    for path in sorted(old.keys() | new.keys()):
        if not path.endswith("/catalog.json") or old.get(path) == new.get(path):
            continue
        before = json.loads(old[path]) if path in old else {}
        after = json.loads(new[path]) if path in new else {}
        lines += [f"### {path}", ""]
        for field in ("coverage",):
            if before.get(field) != after.get(field):
                lines.append(f"- {field}: {json.dumps(before.get(field), ensure_ascii=False)} → {json.dumps(after.get(field), ensure_ascii=False)}")
        for group in ("models", "plans"):
            left = {m["id"]: m for m in before.get(group, [])}
            right = {m["id"]: m for m in after.get(group, [])}
            for mid in sorted(left.keys() | right.keys()):
                a, b = left.get(mid), right.get(mid)
                if a == b:
                    continue
                action = "新增" if a is None else "删除" if b is None else "修改"
                lines.append(f"- {group} / {mid}: {action}")
                fields = ("request_id", "alias_of", "availability", "plan_ids", "capabilities", "usage_prices", "reference_prices") if group == "models" else ("prices", "quotas", "overage")
                for field in fields:
                    av, bv = (a or {}).get(field), (b or {}).get(field)
                    if av != bv:
                        # Keep the human summary concise; full evidence/metadata stays in diff.patch.
                        if field in {"prices", "usage_prices", "reference_prices"}:
                            def describe(value):
                                if value is None:
                                    return "未记录"
                                if not value["rules"]:
                                    return value["status"]
                                return "; ".join(
                                    r["id"] + " [" + r["basis"] + "] " + ", ".join(
                                        f"{x['meter']}={x['amount']} {r['currency']}/{x['per']} {x['unit']}"
                                        + (" 数量=" + json.dumps(x["quantity"], ensure_ascii=False) if "quantity" in x else "")
                                        for x in r["rates"]
                                    ) + f" 周期={r['billing_period']} 税={r['tax']} 基准=" + r.get("selection", json.dumps(r.get("conditions", []), ensure_ascii=False))
                                    + f" 有效期=[{r['effective_from']}, {r['effective_until']})"
                                    + f" 选价时刻={r['time_basis']} 收费事件={r['charge_on']}"
                                    for r in value["rules"]
                                )
                            lines.append(f"  - {field}: {describe(av)} → {describe(bv)}")
                        else:
                            lines.append(f"  - {field}: {json.dumps(av, ensure_ascii=False)} → {json.dumps(bv, ensure_ascii=False)}")
        lines.append("")
    return "\n".join(lines)


def candidate(root, base):
    commit, old = base_files(root, base)
    new = current_files(root)
    inventory = {p: sha(raw) for p, raw in new.items()}
    payload = {"base_commit": commit, "files": inventory}
    diff = make_diff(old, new)
    return {**payload, "candidate_sha256": sha(canonical(payload)), "diff_sha256": sha(diff.encode())}, diff, old, new


def review(root, base):
    stats = validate(root)
    manifest, diff, old, new = candidate(root, base)
    changed = [p for p in sorted(old.keys() | new.keys()) if old.get(p) != new.get(p)]
    report = "\n".join([
        "# 数据候选审阅包", "", "状态：待人工确认。不是正式发布物。", "",
        f"基线：`{manifest['base_commit']}`", "",
        f"候选 SHA-256：`{manifest['candidate_sha256']}`", "",
        "## 检查与范围", "", "结构和语义校验通过。单元测试结果需另附，不能用这句话代替测试。", "",
        "```json", json.dumps(stats, ensure_ascii=False, indent=2), "```", "",
        "## 文件变化", "", *[f"- {p}" for p in changed], "",
        "## 模型与套餐变化", "", summarize_changes(old, new),
        "## 人工确认", "", "请同时阅读 diff.patch 中的说明、来源和校验器变化；核对未知项。",
        "确认时指定完整候选 SHA-256 与动作（保存 / 提交 / 发布），不是泛泛地说继续。",
        "数据确认不授权消费者部署。", "",
    ])
    manifest["report_sha256"] = sha(report.encode())
    output = root / ".review"
    output.mkdir(exist_ok=True)
    (output / "diff.patch").write_text(diff, encoding="utf-8")
    (output / "REVIEW.md").write_text(report, encoding="utf-8")
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest["candidate_sha256"]


def check_candidate(root, expected):
    require(re.fullmatch(r"[0-9a-f]{64}", expected), "provide full SHA-256")
    saved = read_json(root / ".review/manifest.json")
    require(saved["candidate_sha256"] == expected, "provided hash does not match review package")
    current, diff, old, new = candidate(root, saved["base_commit"])
    require(current["candidate_sha256"] == expected, "candidate changed; generate a fresh review")
    require(current["diff_sha256"] == saved["diff_sha256"], "base/diff changed")
    require(sha((root / ".review/diff.patch").read_bytes()) == sha(diff.encode()), "review diff modified")
    require(sha((root / ".review/REVIEW.md").read_bytes()) == saved["report_sha256"], "review report modified")
    validate(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    r = commands.add_parser("review")
    r.add_argument("--base", required=True, help="commit from before the update")
    c = commands.add_parser("check-candidate")
    c.add_argument("sha256")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            print(json.dumps(validate(), ensure_ascii=False, indent=2))
        elif args.command == "review":
            print("Draft candidate:", review(ROOT, args.base))
            print("Review .review/REVIEW.md and .review/diff.patch; no publication performed.")
        else:
            check_candidate(ROOT, args.sha256)
            print("Candidate unchanged. This check does not attest human approval.")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
