# Claude Code 模型补漏

UTC 核对时间：2026-09-16T10:27:21.232069Z；公开资料核对，未实调。

- completion-code-models：https://code.claude.com/docs/en/model-config ，Work with Fable 明确区分 Fable 5.1 与 Fable 5，固定 ID 为 claude-fable-5-1。新增前者，不改写后者。
- completion-api-pricing：https://platform.claude.com/docs/en/about-claude/pricing ，模型价表 Fable 5.1 行：每百万 token USD 输入 10、缓存读取 0.25、输出 50、5m 缓存写入 12.5。作为同平台参考价完整保存；官方生效时间未确认，保持 null。
- 已有 Fable 5、Opus 5、Sonnet 5、Haiku 4.5 仍在模型配置页；仅复核身份，本轮不刷新既有价格核对时间。日期版 Haiku 的订阅可选性仍未核清，保持 unknown。
- 套餐与额度未改；Fable 资格依账号，plan_ids 保持空。旧审计未覆盖新增型号，不代表它不可用。
