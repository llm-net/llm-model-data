# Cursor 编程工具模型核对

来源 URL、UTC 抓取时间、HTTP 状态与逐模型数据见 [核对元数据](tool-model-alignment.json)。范围为 Cursor 个人工具订阅；只读公开资料，未调用模型。

## 模型与价格

每行均核对本产品的 Model ID、Agent / Thinking 标记、上下文、思考控制和价格表。金额单位为 USD / 百万 token；输入、缓存读、输出独立保存。标准档与既有独立 Fast 请求 ID 分开，长上下文档不新增第二套价格规则。

| 本地模型 ID | 请求 ID | 常规 / 最大窗口原文 | 输入 / 缓存读 / 输出 | 核对结论 |
| --- | --- | --- | --- | --- |
| `composer-2-5` | `composer-2.5` | 200k / - | 0.5 / 0.2 / 2.5 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `composer-2-5-fast` | `composer-2.5-fast` | 200k / - | 3 / 0.5 / 15 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `grok-4-7` | `grok-4.7` | 256k / 500k | 2 / 0.5 / 6 | 官方逐型号列出 effort。Plus 固定 medium，不能把 high 默认应用于 Plus。 |
| `grok-4-6` | `grok-4.6` | 256k / - | 2 / 0.5 / 6 | 官方逐型号列出 effort。Plus 固定 medium，不能把 high 默认应用于 Plus。 |
| `grok-4-5` | `grok-4.5` | 256k / - | 2 / 0.5 / 6 | 官方逐型号列出 effort。Plus 固定 medium，不能把 high 默认应用于 Plus。 |
| `claude-fable-5-1` | `claude-fable-5-1` | 300k / 1M | 10 / 0.25 / 50 | 型号页明确支持 thinking 变体并推荐 high；推荐值不作为默认值，完整档位、开关与 RPC 参数未知。 |
| `claude-opus-5-5` | `claude-opus-5-5` | 300k / 1M | 4 / 0.2 / 20 | 型号页明确支持 thinking 变体并推荐 high；推荐值不作为默认值，完整档位、开关与 RPC 参数未知。 |
| `claude-opus-5-5-fast` | `claude-opus-5-5-fast` | 300k / 1M | 8 / 0.4 / 40 | 型号页明确支持 thinking 变体并推荐 high；推荐值不作为默认值，完整档位、开关与 RPC 参数未知。 |
| `claude-opus-5` | `claude-opus-5` | 300k / 1M | 5 / 0.5 / 25 | 型号页明确支持 thinking 变体并推荐 high；推荐值不作为默认值，完整档位、开关与 RPC 参数未知。 |
| `claude-sonnet-5` | `claude-sonnet-5` | 200k / 1M | 2 / 0.2 / 10 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gemini-3-1-pro` | `gemini-3.1-pro` | 200k / 1M | 2 / 0.2 / 12 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gemini-3-8-flash` | `gemini-3.8-flash` | 200k / 1M | 0.75 / 0.075 / 3.75 | 官方型号页列 low / medium / high，默认 high；关闭能力、预算和 RPC 参数未知。 |
| `gpt-5-6-luna` | `gpt-5.6-luna` | 272k / 1M | 0.2 / 0.02 / 1.2 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gpt-5-6-luna-fast` | `gpt-5.6-luna-fast` | 272k / 1M | 0.4 / 0.04 / 2.4 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gpt-5-6-sol` | `gpt-5.6-sol` | 272k / 1M | 4 / 0.4 / 20 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gpt-5-6-sol-fast` | `gpt-5.6-sol-fast` | 272k / 1M | 8 / 0.8 / 40 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gpt-5-6-terra` | `gpt-5.6-terra` | 272k / 1M | 2 / 0.2 / 12 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `gpt-5-6-terra-fast` | `gpt-5.6-terra-fast` | 272k / 1M | 4 / 0.4 / 24 | 型号卡标记 Thinking；未公布完整档位、参数、开关与默认行为，不能继承原厂 API。 |
| `muse-spark-1-3` | `muse-spark-1.3` | 300k / 1M | 1.25 / 0.15 / 4.25 | 官方列六档，保留 extra high 的界面原文，默认 high；关闭能力、预算和 RPC 参数未知。 |
| `claude-sonnet-5-5` | `claude-sonnet-5-5` | 200k / 1M | 2 / 0.1 / 10 | 型号页确认 thinking 变体与 effort；只列有证据的 low / high / max，默认 high；完整枚举、关闭能力与 RPC 参数未知。 |
| `claude-haiku-5-5` | `claude-haiku-5-5` | 300k / 1M | 0.1 / 0.01 / 0.5 | 官方明确 low / medium / high 可关闭 thinking，并展示 thinking 开启时的 max；默认、完整档位与 RPC 字段未知。 |
| `gemini-4-argon` | `gemini-4-argon` | 200k / 1M | 2 / 0.1 / 10 | 官方型号页列 minimal / low / medium / high，默认 medium；关闭能力、预算和 RPC 参数未知。 |
| `muse-wonder-1-0` | `muse-wonder-1.0` | 300k / 1M | 4 / 0.2 / 20 | 官方列六档，保留 extra high 的界面原文，默认 high；关闭能力、预算和 RPC 参数未知。 |
| `claude-opus-5-fast` | `claude-opus-5-fast` | 300k / 1M | 10 / 1 / 50 | 型号页明确支持 thinking 变体并推荐 high；推荐值不作为默认值，完整档位、开关与 RPC 参数未知。 |

## 协议与可用性

- 所有条目的官方型号卡都明确标记 Agent；官方 CLI 的认证页与参数页确认工具订阅认证和 `--model` 入口。协议仍为 `cursor_agent`，不从模型原厂继承 Chat、Responses 或 Messages。当前官方 CLI 静态声明 `agent.v1.AgentService.Run` 为 `BiDiStreaming`，另有 `RunSSE` / `RunPoll`。版本与 SHA-256 在核对元数据；未运行客户端、未读取会话或进行真实 Key 探测。
- Claude Sonnet 5.5、Claude Haiku 5.5、Gemini 4 Argon、Muse Wonder 的 ID 均来自当前型号卡；Muse Wonder 的请求名为 `muse-wonder-1.0`。Opus 5 的 Fast 请求名来自其 Pricing 小节。
- Opus 5、Sonnet 5 与 Muse Spark 1.3 的型号卡和价格仍有效，推荐后继型号不构成下线依据。当前官方 CLI 也明确将 `composer-2-fast` 映射为 `composer-2.5-fast`。Grok 的 Fast 与 500k 是文档中的设置组合，未找到独立请求 ID，不猜型号名。
- 官网当前主表未列 GPT-6 系列，不能从 Codex 清单向 Cursor 继承。

## 条件与缺项

- 全部上下文仅提供 k / M 标称规格，均保持 partial、整数值 null。1M / Max Mode 的套餐与入口在型号页和总价页之间没有完整对齐，记录条件，不把扩展窗口当成默认窗口。
- 全部思考能力保持 partial。官方界面 effort 标签已经记录，私有 RPC 参数名、完整预算与部分关闭 / 默认行为没有公开；Haiku 5.5 仅在 low / medium / high 明确允许关闭 thinking。
- Gemini 3.8 Flash 当前输出参考价为 3.75；其余既有输入 / 缓存读 / 输出价在本次公开表内一致。
- 官方 Cache Write 原值保存在元数据。除已有 Opus 5.5 映射外，型号页未确认对应 5m / 1h 时长，不把未分时长的写入价强填到现有时长 meter，也不把缺项当成免费。
- Haiku 5.5 的标准参考档以输入不超过 100k 为限；超过后五倍。GPT-5.6 的标准参考档以输入不超过 272k 为限；Grok 4.7 以输入不超过 256k 为限。
- 本目录既有 Pro / Pro+ / Ultra 套餐仍是 legacy Cursor 合同。当前 X Subscription 的 Plus 固定自有模型 medium effort、关闭 Fast；第三方模型需要 Premium 或更高档。不同购买口径不混入同一份 plans，套餐未做新的价格核对。
