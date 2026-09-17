# Anthropic — Fable 按量目录补漏

核对完成时间（UTC）：2026-09-17T10:30:47.945348+00:00。范围仅 Fable 5.1、Fable 5 的 API 与 Claude Code；其他型号和套餐本轮未更新。没有真实 Key 实调。

## 官方来源与位置

- `pricing`：https://platform.claude.com/docs/en/about-claude/pricing ，Model pricing 表；本次核对输入、输出、缓存读、5 分钟 / 1 小时缓存写入。
- `repair-claude-fable-5-1`：https://platform.claude.com/docs/en/models/fable-5-1/overview ，Model IDs / Pricing / Capabilities / Availability。
- `repair-claude-fable-5`：https://platform.claude.com/docs/en/models/fable-5/overview ，同上。
- `reasoning-claude-effort`：https://platform.claude.com/docs/en/build-with-claude/effort ，Supported models / Effort levels / API 示例。
- `protocol-chat`：https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk ，Getting started / model 字段 / Thinking support / compatibility limitations。
- `repair-context`：https://platform.claude.com/docs/en/build-with-claude/context-windows ，Context window sizes by model。
- `completion-code-models` / `reasoning-claude-code` / `context-claude-code`：https://code.claude.com/docs/en/model-config ，Work with Fable / Effort / Extended thinking / Extended context。
- `protocol-code`：https://code.claude.com/docs/en/llm-gateway ，Subscriptions and gateways（订阅 OAuth 与按量网关凭据分开）；继续核对其链接的 compatibility 文档。

上述页面在本次会话 2026-09-17 UTC 读取；时间记核对完成时刻，官方调价生效时刻未知，保持 null。

## 价格结论

| API / Claude Code 参考型号 | 输入 | 缓存读 | 输出 | 5 分钟缓存写入 |
| --- | ---: | ---: | ---: | ---: |
| claude-fable-5-1 | 10 | 0.25 | 50 | 12.5 |
| claude-fable-5 | 10 | 1 | 50 | 12.5 |

单位均 USD / 百万 token。API 两条此前漏收录；Claude Code Fable 5 此前缺 5 分钟缓存写入，现补齐。5.1 的缓存读不能按通用 0.1 倍输入推算。官方还列出两者 1 小时写入 20，但本仓库唯一基准继续选择 5 分钟 TTL，不增加第二套规格。缓存写入、缓存命中和未缓存输入互斥计量，不能重复加总。

订阅独立保存相同数字与明确 `catalog_model` 来源；API 缺项不能因为订阅有参考价就被统计为已覆盖。不调整 Cursor 等其他平台自己的价格。

## 能力和身份

- 两个精确 API ID 均确认；5.1 是当前版，5 是 active legacy，不能当作同一个别名。原生 Messages 的逐型号示例及官方 Chat 兼容层已查；Responses 未发现支持证据。Chat 不支持缓存、忽略 reasoning_effort；保留其限制。
- 两者 API 自适应思考不可关闭，顶层 output_config.effort 支持 low / medium / high / xhigh / max，默认 high。Chat 具体控制和 5.1 逐消息 beta 控制未完整登记，reasoning 保持 partial。
- API 规格列 1M 窗口、128K 最大输出；Code 的 Extended context 还明确两型号直连 Anthropic API 默认 1 million 窗口，因此 API 窗口记 1000000。最大输出的精确整数未另核实，保留 null。
- Claude Code 独立确认两个型号、Messages 承载、五档 --effort 与不可关闭思考；持久化 effortLevel 不接受 max。原生窗口为 1 million，客户端关闭 1M 会施加 200K 上限，套餐及网关资格另有约束；不继承 API 的工具能力。思考的其他设置入口仍 partial。

协议补充来源 `repair-code-protocol`：https://code.claude.com/docs/en/llm-gateway-protocol ，本次 UTC 2026-09-17 读取 API formats 与 Request headers。明确 /v1/messages 和订阅 OAuth beta 头，支持上述 Code 协议结论。
