# Codex — 用户指定删除 gpt-5.3-codex-spark

基线：`99b9f3ee110a1e9ec91ad043bace91be164057e0`（`data-2026.09.23.1`）。本次不抓取官方页面，不刷新其他型号核对结论。

## 结论

- 用户明确指定从 Codex 产品删除 `gpt-5.3-codex-spark`（本地 ID `gpt-5-3-codex-spark`），并在 `providers/openai/provider.json` 的 `excluded_request_ids` 登记，校验器拒绝重新收录。
- 删除前状态：`availability=unknown`、verification `needs_review`、参考价 unknown、思考与上下文 unknown、协议面 partial；依据见 [2026-09-22](2026-09-22-codex-availability.md) 与 [2026-09-23](2026-09-23-codex-gpt-6.md) 记录（英文 Models / Speed 与 CLI 0.155.1、0.156.1 内嵌目录均不列此 slug）。
- 这是收录决定，不是官方退役证明；未找到全球退役公告的事实不变。
