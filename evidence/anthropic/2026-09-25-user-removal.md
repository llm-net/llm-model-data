# Claude Code — 用户指定删除 claude-haiku-4-5-20251001

基线：`99b9f3ee110a1e9ec91ad043bace91be164057e0`（`data-2026.09.23.1`）。本次不抓取官方页面，不刷新其他型号核对结论。

## 结论

- 用户明确指定从 Claude Code 产品删除日期版 `claude-haiku-4-5-20251001`，并在 `providers/anthropic/provider.json` 的 `excluded_request_ids` 登记，校验器拒绝重新收录；排除按服务商生效，API 产品当前未收录此请求 ID。
- 删除前状态：`availability=unknown`、verification `needs_review`；Claude Code 模型配置页不列此固定 ID（见 [2026-09-23](2026-09-23-claude-opus-5-5.md)），参考价按用户指定对齐 `claude-haiku-4-5`。该估价映射随条目一并删除。
- 短名 `claude-haiku-4-5` 保留，状态与价格不变。
