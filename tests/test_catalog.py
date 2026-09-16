"""Guard price identity, provenance and approval freshness using isolated repositories."""
from copy import deepcopy
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/catalog.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class DataContracts(unittest.TestCase):
    def setUp(self):
        self.provider = c.read_json(ROOT / "providers/deepseek/provider.json")
        self.data = c.read_json(ROOT / "providers/deepseek/offerings/api-cn/catalog.json")

    def check(self):
        c.check_offering(ROOT, self.data, self.provider)

    def test_complete_repository_validates(self):
        stats = c.validate(ROOT)
        self.assertGreater(stats["models_verified"], 0)

    def test_duplicate_id_rejected_within_product(self):
        self.data["models"].append(deepcopy(self.data["models"][0]))
        with self.assertRaisesRegex(c.CatalogError, "duplicate id"):
            self.check()

    def test_same_model_can_have_different_prices_in_another_product(self):
        other = deepcopy(self.data)
        other["id"] = "different-product"
        other["models"][0]["usage_prices"]["rules"][0]["rates"][0]["amount"] = "999"
        self.check()
        c.check_offering(ROOT, other, self.provider)
        self.assertNotEqual(other["models"][0]["usage_prices"], self.data["models"][0]["usage_prices"])

    def test_unknown_cannot_silently_be_free(self):
        self.data["models"][0]["usage_prices"]["status"] = "unknown"
        with self.assertRaisesRegex(c.CatalogError, "unknown/not_applicable"):
            self.check()

    def test_reference_cannot_be_actual_usage_price(self):
        self.data["models"][0]["usage_prices"]["rules"][0]["basis"] = "reference"
        with self.assertRaisesRegex(c.CatalogError, "wrong price basis"):
            self.check()

    def test_reference_requires_explicit_origin(self):
        p = self.data["models"][0]["reference_prices"]
        p.update(deepcopy(self.data["models"][0]["usage_prices"]))
        for rule in p["rules"]:
            rule["basis"] = "reference"
        with self.assertRaisesRegex(c.CatalogError, "reference_origin"):
            self.check()

    def test_verified_requires_evidence(self):
        self.data["models"][0]["verification"]["evidence"] = "evidence/missing.md"
        with self.assertRaisesRegex(c.CatalogError, "missing evidence"):
            self.check()

    def test_cross_provider_source_reference_rejected(self):
        self.data["verification"]["source_ids"] = ["other-provider-source"]
        with self.assertRaisesRegex(c.CatalogError, "unknown source"):
            self.check()

    def test_alias_cycles_rejected(self):
        a, b = self.data["models"][:2]
        a["alias_of"], b["alias_of"] = b["id"], a["id"]
        with self.assertRaisesRegex(c.CatalogError, "alias cycle"):
            self.check()

    def test_plan_mapping_stays_local(self):
        self.data["models"][0]["plan_ids"] = ["pro"]
        with self.assertRaisesRegex(c.CatalogError, "unknown plan"):
            self.check()

    def test_multiple_price_baselines_rejected(self):
        rules = self.data["models"][0]["usage_prices"]["rules"]
        extra = deepcopy(rules[0]); extra["id"] = "off-peak"
        rules.append(extra)
        with self.assertRaisesRegex(c.CatalogError, "one price baseline"):
            self.check()

    def test_usage_and_reference_cannot_both_supply_a_price(self):
        model = self.data["models"][0]
        model["reference_prices"] = deepcopy(model["usage_prices"])
        rule = model["reference_prices"]["rules"][0]
        rule["basis"] = "reference"
        rule["reference_origin"] = {"url": "https://example.com/price", "subject": "example", "reason": "example"}
        with self.assertRaisesRegex(c.CatalogError, "one price baseline"):
            self.check()

    def test_removed_subdivision_fields_rejected_by_schema(self):
        schema = c.Draft202012Validator(c.read_json(ROOT / "schemas/catalog.schema.json"))
        for key, value in [("routes", []), ("routing_mode", "dynamic")]:
            with self.subTest(field=key):
                data = deepcopy(self.data)
                data["models"][0][key] = value
                self.assertFalse(schema.is_valid(data))
        self.data["models"][0]["usage_prices"]["rules"][0]["conditions"] = []
        self.assertFalse(schema.is_valid(self.data))

    def test_effective_time_interval_order(self):
        rule = self.data["models"][0]["usage_prices"]["rules"][0]
        rule["effective_from"] = "2026-09-16T00:00:00Z"
        rule["effective_until"] = "2026-09-15T00:00:00Z"
        with self.assertRaisesRegex(c.CatalogError, "effective interval"):
            self.check()

    def test_float_money_is_invalid_schema(self):
        self.data["models"][0]["usage_prices"]["rules"][0]["rates"][0]["amount"] = 0.5
        schema = c.read_json(ROOT / "schemas/catalog.schema.json")
        self.assertFalse(c.Draft202012Validator(schema).is_valid(self.data))

    def test_unknown_fields_rejected(self):
        self.data["cloud"] = {"enabled": True}
        schema = c.read_json(ROOT / "schemas/catalog.schema.json")
        self.assertFalse(c.Draft202012Validator(schema).is_valid(self.data))

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaisesRegex(c.CatalogError, "duplicate JSON"):
            json.loads('{"price": "1", "price": "2"}', object_pairs_hook=c.json_pairs)

    def test_review_patch_handles_original_file_without_final_newline(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "README.md").write_bytes(b"before")
            patch = c.make_diff({"README.md": b"before"}, {"README.md": b"after\n"})
            result = subprocess.run(["git", "apply", "--check", "-"], input=patch,
                                    text=True, cwd=folder, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)


class MultimodalAndAudit(unittest.TestCase):
    def setUp(self):
        self.data = c.read_json(ROOT / "providers/minimax/offerings/api-cn/catalog.json")
        self.provider = c.read_json(ROOT / "providers/minimax/provider.json")

    def model(self, request_id):
        return next(m for m in self.data["models"] if m["request_id"] == request_id)

    def test_h3_estimate_includes_video_inputs_and_extra_images(self):
        rates = self.model("MiniMax-H3")["usage_prices"]["rules"][0]["rates"]
        quantities = {"video_output_seconds": 10, "video_input_seconds": 5, "input_images": 7}
        # Arithmetic illustration only: quantity rounding remains explicitly unknown.
        total = sum(max(Decimal(quantities[r["meter"]]) - Decimal(r["quantity"]["included_units"] or "0"), 0)
                    * Decimal(r["amount"]) / r["per"] for r in rates)
        self.assertEqual(total, Decimal("7.90"))

    def test_tts_character_usage_is_not_utf8_bytes(self):
        rate = self.model("speech-2.8-hd")["usage_prices"]["rules"][0]["rates"][0]
        self.assertEqual(rate["quantity"]["fields"], ["$.extra_info.usage_characters"])
        self.assertEqual(rate["per"], 10000)
        rate["unit"] = "byte"
        with self.assertRaisesRegex(c.CatalogError, "meter/unit mismatch"):
            c.check_offering(ROOT, self.data, self.provider)

    def test_multimodal_requires_quantity(self):
        self.model("MiniMax-H3")["usage_prices"]["rules"][0]["rates"][0].pop("quantity")
        with self.assertRaisesRegex(c.CatalogError, "explicit quantity"):
            c.check_offering(ROOT, self.data, self.provider)

    def test_known_quantity_source_requires_fields(self):
        q = self.model("MiniMax-H3")["usage_prices"]["rules"][0]["rates"][0]["quantity"]
        q["source"] = "provider_usage"
        with self.assertRaisesRegex(c.CatalogError, "requires fields"):
            c.check_offering(ROOT, self.data, self.provider)

    def test_rounding_requires_positive_step(self):
        q = self.model("MiniMax-H3")["usage_prices"]["rules"][0]["rates"][0]["quantity"]
        q["rounding"] = "ceil"
        with self.assertRaisesRegex(c.CatalogError, "positive increment"):
            c.check_offering(ROOT, self.data, self.provider)

    def test_review_exposes_baseline_and_quantity(self):
        path = "providers/minimax/offerings/api-cn/catalog.json"
        report = c.summarize_changes({}, {path: c.canonical(self.data)})
        self.assertIn("768p", report)
        self.assertIn("included_units", report)
        self.assertIn("收费事件", report)

    def test_openrouter_model_price_needs_no_endpoint(self):
        data = c.read_json(ROOT / "providers/openrouter/offerings/api-global/catalog.json")
        provider = c.read_json(ROOT / "providers/openrouter/provider.json")
        c.check_offering(ROOT, data, provider)
        priced = next(m for m in data["models"] if m["usage_prices"]["status"] == "published")
        self.assertNotIn("routes", priced)
        self.assertEqual(len(priced["usage_prices"]["rules"]), 1)


class SubscriptionAndCollectionPolicy(unittest.TestCase):
    def test_subscription_cannot_keep_actual_usage_or_credit_rates(self):
        data = c.read_json(ROOT / "providers/openai/offerings/codex/catalog.json")
        provider = c.read_json(ROOT / "providers/openai/provider.json")
        data["models"][0]["usage_prices"] = deepcopy(data["models"][0]["reference_prices"])
        with self.assertRaisesRegex(c.CatalogError, "reference prices only"):
            c.check_offering(ROOT, data, provider)
        data = c.read_json(ROOT / "providers/openai/offerings/codex/catalog.json")
        data["models"][0]["reference_prices"]["rules"][0]["currency"] = "CREDIT"
        with self.assertRaisesRegex(c.CatalogError, "not credits"):
            c.check_offering(ROOT, data, provider)

    def test_explicitly_excluded_model_cannot_be_reimported(self):
        for vendor, offering in [("openrouter", "api-global"), ("groq", "api-global")]:
            with self.subTest(vendor=vendor):
                data = c.read_json(ROOT / f"providers/{vendor}/offerings/{offering}/catalog.json")
                provider = c.read_json(ROOT / f"providers/{vendor}/provider.json")
                data["models"][0]["request_id"] = provider["excluded_request_ids"][0]
                with self.assertRaisesRegex(c.CatalogError, "explicitly excluded"):
                    c.check_offering(ROOT, data, provider)

    def test_excluded_local_id_cannot_hide_behind_null_request_id(self):
        data = c.read_json(ROOT / "providers/openrouter/offerings/api-global/catalog.json")
        provider = c.read_json(ROOT / "providers/openrouter/provider.json")
        data["models"][0].update(id="openai-gpt-latest", request_id=None)
        with self.assertRaisesRegex(c.CatalogError, "explicitly excluded"):
            c.check_offering(ROOT, data, provider)

    def test_removed_providers_cannot_be_reintroduced_even_with_active_models(self):
        for vendor in ("siliconflow", "together"):
            with self.subTest(vendor=vendor):
                data = c.read_json(ROOT / "providers/deepseek/offerings/api-cn/catalog.json")
                provider = c.read_json(ROOT / "providers/deepseek/provider.json")
                data["provider_id"] = provider["id"] = vendor
                with self.assertRaisesRegex(c.CatalogError, "provider is explicitly excluded"):
                    c.check_offering(ROOT, data, provider)


class ProtocolContracts(unittest.TestCase):
    setUp = DataContracts.setUp
    check = DataContracts.check

    def test_new_model_cannot_omit_protocol_assessment(self):
        for field in ("interfaces", "interface_assessment"):
            with self.subTest(field=field):
                data = deepcopy(self.data)
                del data["models"][0]["capabilities"][field]
                with self.assertRaisesRegex(c.CatalogError, "protocol interfaces and assessment"):
                    c.check_offering(ROOT, data, self.provider)

    def test_legacy_names_and_vendor_slugs_are_not_current_faces(self):
        for face in ("openai", "responses", "anthropic", "images", "minimax_audio", "gemini", "vendor_native", "ark"):
            with self.subTest(face=face):
                self.data["models"][0]["capabilities"]["interfaces"] = [face]
                with self.assertRaisesRegex(c.CatalogError, "unknown or legacy protocol face"):
                    self.check()

    def test_price_verification_cannot_substitute_protocol_evidence(self):
        v = self.data["models"][0]["capabilities"]["interface_assessment"]["verification"]
        v.update(status="needs_review", checked_at=None)
        with self.assertRaisesRegex(c.CatalogError, "own verified evidence"):
            self.check()

    def test_protocol_provenance_is_checked_independently(self):
        v = self.data["models"][0]["capabilities"]["interface_assessment"]["verification"]
        v["source_ids"] = ["unregistered-protocol-source"]
        with self.assertRaisesRegex(c.CatalogError, "unknown source_id"):
            self.check()
        v["source_ids"] = ["protocol-chat"]
        v["evidence"] = "evidence/missing-protocol-proof.md"
        with self.assertRaisesRegex(c.CatalogError, "missing evidence"):
            self.check()

    def test_unknown_does_not_assert_support_or_a_successful_check(self):
        cap = self.data["models"][0]["capabilities"]
        cap["interface_assessment"]["coverage"] = "unknown"
        with self.assertRaisesRegex(c.CatalogError, "unknown needs an empty list"):
            self.check()
        cap["interfaces"] = []
        with self.assertRaisesRegex(c.CatalogError, "must not claim successful verification"):
            self.check()
        cap["interface_assessment"]["verification"].update(status="needs_review", checked_at=None)
        cap["reasoning"].update(support="unknown", coverage="unknown", profiles=[])
        cap["reasoning"]["verification"].update(status="needs_review", checked_at=None)
        self.check()

    def test_protocol_must_match_output_not_input_modality(self):
        cap = self.data["models"][0]["capabilities"]
        cap["input_modalities"] = ["text", "image"]
        cap["interfaces"] = ["ark_image"]
        with self.assertRaisesRegex(c.CatalogError, "does not match output modality"):
            self.check()

    def test_tool_subscription_is_not_provider_api(self):
        def interfaces(provider, offering):
            data = c.read_json(ROOT / f"providers/{provider}/offerings/{offering}/catalog.json")
            return [m["capabilities"]["interfaces"] for m in data["models"]]
        self.assertTrue(all(x == ["cursor_agent"] for x in interfaces("cursor", "individual")))
        self.assertTrue(all(x == ["openai_responses"] for x in interfaces("openai", "codex")))
        self.assertTrue(all(x == ["anthropic_messages"] for x in interfaces("anthropic", "claude-code")))
        self.assertTrue(all("openai_responses" not in x for x in interfaces("bailian", "coding-plan-cn")))

    def test_protocol_change_is_visible_even_if_price_does_not_change(self):
        before = deepcopy(self.data)
        after = deepcopy(before)
        after["models"][0]["capabilities"]["interfaces"].remove("openai_responses")
        path = "providers/deepseek/offerings/api-cn/catalog.json"
        report = c.summarize_changes({path: c.canonical(before)}, {path: c.canonical(after)})
        self.assertIn("openai_responses", report)
        self.assertIn("capabilities", report)
        self.assertNotIn("usage_prices:", report)

    def test_v1_schema_can_read_history_but_publish_requires_review(self):
        historical = deepcopy(self.data)
        del historical["models"][0]["capabilities"]
        schema = c.Draft202012Validator(c.read_json(ROOT / "schemas/catalog.schema.json"))
        self.assertTrue(schema.is_valid(historical))
        with self.assertRaisesRegex(c.CatalogError, "protocol interfaces and assessment"):
            c.check_offering(ROOT, historical, self.provider)


class ReasoningContracts(unittest.TestCase):
    def setUp(self):
        self.provider = c.read_json(ROOT / "providers/openai/provider.json")
        self.data = c.read_json(ROOT / "providers/openai/offerings/api-global/catalog.json")
        self.cap = self.data["models"][0]["capabilities"]
        self.reasoning = self.cap["reasoning"]

    def check(self):
        c.check_offering(ROOT, self.data, self.provider)

    def test_history_is_readable_but_current_data_cannot_omit_reasoning(self):
        del self.cap["reasoning"]
        validator = c.Draft202012Validator(c.read_json(ROOT / "schemas/catalog.schema.json"))
        self.assertTrue(validator.is_valid(self.data))
        with self.assertRaisesRegex(c.CatalogError, "reasoning assessment is required"):
            self.check()

    def test_unknown_is_not_unsupported_or_a_supported_control(self):
        self.reasoning.update(support="unknown", coverage="unknown")
        with self.assertRaisesRegex(c.CatalogError, "cannot assert profiles"):
            self.check()
        self.reasoning["profiles"] = []
        with self.assertRaisesRegex(c.CatalogError, "cannot claim successful verification"):
            self.check()
        self.reasoning["verification"].update(status="needs_review", checked_at=None)
        self.check()
        self.reasoning.update(support="unsupported", coverage="complete")
        with self.assertRaisesRegex(c.CatalogError, "own verified evidence"):
            self.check()

    def test_reasoning_needs_independent_registered_provenance(self):
        v = self.reasoning["verification"]
        v["source_ids"] = ["unregistered-reasoning-source"]
        with self.assertRaisesRegex(c.CatalogError, "unknown source_id"):
            self.check()
        v["source_ids"] = ["reasoning-openai-model"]
        v["evidence"] = "evidence/missing-reasoning.md"
        with self.assertRaisesRegex(c.CatalogError, "missing evidence"):
            self.check()

    def test_reasoning_cannot_invent_a_protocol_or_hide_missing_faces(self):
        self.reasoning["profiles"].pop()
        with self.assertRaisesRegex(c.CatalogError, "cover every confirmed interface"):
            self.check()
        self.reasoning["coverage"] = "partial"
        self.reasoning["profiles"][0]["interface"] = "anthropic_messages"
        with self.assertRaisesRegex(c.CatalogError, "confirmed model interface"):
            self.check()

    def test_client_settings_cannot_become_an_api_contract(self):
        self.reasoning["profiles"][0]["surface"] = "client_setting"
        with self.assertRaisesRegex(c.CatalogError, "cannot be copied"):
            self.check()

    def test_default_must_be_supported_and_typed(self):
        control = self.reasoning["profiles"][0]["controls"][0]
        control["default"] = "invented-tier"
        with self.assertRaisesRegex(c.CatalogError, "outside supported values"):
            self.check()
        control["default"] = True
        with self.assertRaisesRegex(c.CatalogError, "default has wrong type"):
            self.check()

    def test_budget_bounds_special_values_and_unknowns(self):
        self.reasoning["coverage"] = "partial"
        control = self.reasoning["profiles"][0]["controls"][0]
        control.update(kind="budget_tokens", parameter="thinking.budget_tokens",
                       values=[-1], minimum=1024, maximum=4096, default=-1)
        self.check()
        control["minimum"] = 5000
        with self.assertRaisesRegex(c.CatalogError, "invalid reasoning budget range"):
            self.check()
        control["minimum"] = 1024
        control["default"] = 8192
        with self.assertRaisesRegex(c.CatalogError, "outside supported values"):
            self.check()
        control.update(default=True, values=[True])
        with self.assertRaisesRegex(c.CatalogError, "values have wrong type"):
            self.check()
        control.update(default=None, values=[], minimum=None, maximum=None)
        self.check()

    def test_unpublished_parameter_or_default_stays_partial(self):
        control = self.reasoning["profiles"][0]["controls"][0]
        control["parameter"] = None
        with self.assertRaisesRegex(c.CatalogError, "parameter must remain partial"):
            self.check()
        control["parameter"] = "reasoning_effort"
        control["default"] = None
        with self.assertRaisesRegex(c.CatalogError, "default must remain partial"):
            self.check()
        self.reasoning["coverage"] = "partial"
        self.check()

    def test_duplicate_profiles_and_controls_are_rejected(self):
        self.reasoning["profiles"].append(deepcopy(self.reasoning["profiles"][0]))
        with self.assertRaisesRegex(c.CatalogError, "duplicate reasoning profile"):
            self.check()
        self.reasoning["profiles"].pop()
        controls = self.reasoning["profiles"][0]["controls"]
        controls.append(deepcopy(controls[0]))
        with self.assertRaisesRegex(c.CatalogError, "duplicate parameter"):
            self.check()

    def test_vendor_defaults_and_control_semantics_are_not_flattened(self):
        doc = c.read_json(ROOT / "providers/minimax/offerings/api-cn/catalog.json")
        m3 = next(m for m in doc["models"] if m["request_id"] == "MiniMax-M3")
        profiles = {p["interface"]: p for p in m3["capabilities"]["reasoning"]["profiles"]}
        self.assertEqual(profiles["openai_chat"]["default_behavior"], "adaptive")
        self.assertEqual(profiles["openai_responses"]["default_behavior"], "disabled")
        self.assertEqual(profiles["openai_responses"]["controls"][0]["kind"], "mode")
        cursor = c.read_json(ROOT / "providers/cursor/offerings/individual/catalog.json")
        by_id = {m["request_id"]: m["capabilities"]["reasoning"] for m in cursor["models"]}
        self.assertNotIn("xhigh", by_id["grok-4.5"]["profiles"][0]["controls"][0]["values"])
        self.assertIn("xhigh", by_id["grok-4.6"]["profiles"][0]["controls"][0]["values"])
        self.assertIsNone(by_id["grok-4.6"]["profiles"][0]["controls"][0]["parameter"])
        gemini = c.read_json(ROOT / "providers/gemini/offerings/api-global/catalog.json")
        profiles = {p["interface"]: p for p in gemini["models"][0]["capabilities"]["reasoning"]["profiles"]}
        self.assertEqual(profiles["gemini_generate_content"]["controls"][0]["values"], ["LOW", "MEDIUM", "HIGH"])
        self.assertEqual(profiles["openai_chat"]["controls"][0]["values"], ["low", "medium", "high"])

    def test_reasoning_only_change_is_in_candidate_summary(self):
        before = deepcopy(self.data)
        self.reasoning["profiles"][0]["controls"][0]["default"] = "high"
        path = "providers/openai/offerings/api-global/catalog.json"
        report = c.summarize_changes({path: c.canonical(before)}, {path: c.canonical(self.data)})
        self.assertIn("reasoning", report)
        self.assertIn("high", report)
        self.assertNotIn("usage_prices:", report)


class ApprovalFreshness(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in c.DIRECTORIES | c.ROOT_FILES:
            src, dst = ROOT / name, self.root / name
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
            elif src.is_file():
                shutil.copyfile(src, dst)
        def run(*args):
            subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)
        run("init")
        run("config", "user.name", "Test")
        run("config", "user.email", "test@example.invalid")
        run("add", ".")
        run("commit", "-m", "test baseline")

    def test_review_is_deterministic_and_not_approval(self):
        first = c.review(self.root, "HEAD")
        second = c.review(self.root, "HEAD")
        self.assertEqual(first, second)
        c.check_candidate(self.root, first)
        self.assertNotIn("approved", c.read_json(self.root / ".review/manifest.json"))

    def test_review_keeps_protocol_gaps_visible_without_data_changes(self):
        c.review(self.root, "HEAD")
        report = (self.root / ".review/REVIEW.md").read_text()
        self.assertIn("## 协议面待核对清单", report)
        for path in (self.root / "providers").glob("*/offerings/*/catalog.json"):
            doc = c.read_json(path)
            for model in doc["models"]:
                assessment = model["capabilities"]["interface_assessment"]
                if assessment["coverage"] != "complete":
                    self.assertIn(f"{doc['provider_id']}/{doc['id']}/{model['id']}: "
                                  f"{assessment['coverage']}", report)

    def test_review_keeps_reasoning_gaps_visible_without_data_changes(self):
        c.review(self.root, "HEAD")
        report = (self.root / ".review/REVIEW.md").read_text().split("## 思考能力待核对清单")[1]
        for path in (self.root / "providers").glob("*/offerings/*/catalog.json"):
            doc = c.read_json(path)
            for model in doc["models"]:
                reasoning = model["capabilities"]["reasoning"]
                if reasoning["coverage"] != "complete":
                    self.assertIn(f"{doc['provider_id']}/{doc['id']}/{model['id']}: "
                                  f"{reasoning['coverage']}", report)

    def test_new_untracked_data_invalidates_confirmation(self):
        expected = c.review(self.root, "HEAD")
        (self.root / "evidence/new.md").write_text("new evidence")
        with self.assertRaisesRegex(c.CatalogError, "candidate changed"):
            c.check_candidate(self.root, expected)

    def test_deleted_file_invalidates_confirmation(self):
        expected = c.review(self.root, "HEAD")
        (self.root / "docs/AUTOMATION.md").unlink()
        with self.assertRaisesRegex(c.CatalogError, "candidate changed"):
            c.check_candidate(self.root, expected)

    def test_changed_rule_invalidates_confirmation(self):
        expected = c.review(self.root, "HEAD")
        path = self.root / "providers/deepseek/offerings/api-cn/catalog.json"
        data = c.read_json(path)
        data["models"][0]["usage_prices"]["rules"][0]["rates"][0]["amount"] = "123"
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(c.CatalogError, "candidate changed"):
            c.check_candidate(self.root, expected)

    def test_modified_report_rejected(self):
        expected = c.review(self.root, "HEAD")
        (self.root / ".review/REVIEW.md").write_text("looks good, approve everything")
        with self.assertRaisesRegex(c.CatalogError, "report modified"):
            c.check_candidate(self.root, expected)

    def test_symlinks_cannot_hide_unreviewed_content(self):
        (self.root / "providers/link").symlink_to(self.root / "evidence", target_is_directory=True)
        with self.assertRaisesRegex(c.CatalogError, "symlinks"):
            c.current_files(self.root)


if __name__ == "__main__":
    unittest.main()
