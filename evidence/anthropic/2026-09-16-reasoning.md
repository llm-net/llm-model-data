# Anthropic 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-claude-code`：https://code.claude.com/docs/en/model-config；UTC 2026-09-16T12:46:08.102668+00:00。位置：Adjust effort level 的逐型号表、Set the effort level、Adaptive reasoning and fixed thinking budgets、Extended thinking。
- `reasoning-claude-effort`：https://platform.claude.com/docs/en/build-with-claude/effort；UTC 2026-09-16T12:46:08.299961+00:00。位置：Effort levels 支持表、Recommended effort levels for Claude Opus 5 / Sonnet 5。
- `reasoning-claude-overview`：https://platform.claude.com/docs/en/build-with-claude/thinking；UTC 2026-09-16T12:48:26.247993+00:00。位置：默认思考说明、Sonnet 5 / Opus 5 关闭思考及高 effort 组合限制、Haiku interleaved thinking 限制。
- `reasoning-claude-thinking`：https://platform.claude.com/docs/en/build-with-claude/extended-thinking；UTC 2026-09-16T12:46:08.300128+00:00。位置：Supported models、How to use extended thinking、Budget rules and tuning、Interleaved thinking in manual mode。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-global/claude-opus-5` | supported | partial | `anthropic_messages/api_request: thinking.type` = ["adaptive", "disabled"]; `anthropic_messages/api_request: output_config.effort` = ["low", "medium", "high", "xhigh", "max"] | Opus 5 / Sonnet 5 默认自适应思考，不接受旧手动 budget_tokens。Messages 已核对，Chat 兼容层的控制方式仍未知。 |
| `api-global/claude-sonnet-5` | supported | partial | `anthropic_messages/api_request: thinking.type` = ["adaptive", "disabled"]; `anthropic_messages/api_request: output_config.effort` = ["low", "medium", "high", "xhigh", "max"] | Opus 5 / Sonnet 5 默认自适应思考，不接受旧手动 budget_tokens。Messages 已核对，Chat 兼容层的控制方式仍未知。 |
| `api-global/claude-haiku-4-5` | supported | partial | `anthropic_messages/api_request: thinking.type` = ["enabled", "disabled"]; `anthropic_messages/api_request: thinking.budget_tokens` = [] | Haiku 4.5 支持手动思考预算，不支持 interleaved thinking；不能用 effort 代替预算。默认模式和 Chat 兼容层参数未完整核对。 |
| `claude-code/claude-fable-5-1` | supported | partial | `anthropic_messages/client_setting: --effort` = ["low", "medium", "high", "xhigh", "max"] | 按 Claude Code 的型号支持表、effort 解析顺序与 Extended thinking 核对。Fable 无法关闭思考；Opus / Sonnet 可以。持久化与会话设置限制不同，未展开全部入口和组织策略。 |
| `claude-code/claude-fable-5` | supported | partial | `anthropic_messages/client_setting: --effort` = ["low", "medium", "high", "xhigh", "max"] | 按 Claude Code 的型号支持表、effort 解析顺序与 Extended thinking 核对。Fable 无法关闭思考；Opus / Sonnet 可以。持久化与会话设置限制不同，未展开全部入口和组织策略。 |
| `claude-code/claude-opus-5` | supported | partial | `anthropic_messages/client_setting: --effort` = ["low", "medium", "high", "xhigh", "max"]; `anthropic_messages/client_setting: alwaysThinkingEnabled` = [true, false] | 按 Claude Code 的型号支持表、effort 解析顺序与 Extended thinking 核对。Fable 无法关闭思考；Opus / Sonnet 可以。持久化与会话设置限制不同，未展开全部入口和组织策略。 |
| `claude-code/claude-sonnet-5` | supported | partial | `anthropic_messages/client_setting: --effort` = ["low", "medium", "high", "xhigh", "max"]; `anthropic_messages/client_setting: alwaysThinkingEnabled` = [true, false] | 按 Claude Code 的型号支持表、effort 解析顺序与 Extended thinking 核对。Fable 无法关闭思考；Opus / Sonnet 可以。持久化与会话设置限制不同，未展开全部入口和组织策略。 |
| `claude-code/claude-haiku-4-5` | supported | partial | `anthropic_messages/client_setting: alwaysThinkingEnabled` = [true, false] | Haiku 可用扩展思考开关，但默认值和此客户端的固定预算范围未核实。日期版仅沿用官方 Haiku 4.5 产品身份，不借价格近似推导参数。 |
| `claude-code/claude-haiku-4-5-20251001` | supported | partial | `anthropic_messages/client_setting: alwaysThinkingEnabled` = [true, false] | Haiku 可用扩展思考开关，但默认值和此客户端的固定预算范围未核实。日期版仅沿用官方 Haiku 4.5 产品身份，不借价格近似推导参数。 |
