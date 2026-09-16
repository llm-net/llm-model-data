# 模型思考能力维护

思考能力与协议面、模型身份和价格一起核对。数据属于 **Provider → 产品 → 模型 → 协议面 / 设置入口**，不是全局的“低、中、高”。同一模型在按量 API、API 订阅和编程工具中的档位、开关与默认值独立维护。

## 字段

每个模型保存 `capabilities.reasoning`：

| 字段 | 含义 |
| --- | --- |
| `support` | `supported` 已确认支持思考；`unsupported` 有证据明确不支持；`unknown` 未确认。未提供深度参数不等于不支持思考。 |
| `coverage` | `complete` 当前协议和设置范围已核对；`partial` 仍有具体缺口；`unknown` 没有足以确认支持与否的证据。 |
| `profiles` | 按 `interface` 和 `surface` 分别保存的控制方式；未知或明确不支持时为空。 |
| `verification` | 思考能力自己的状态、UTC 时间、已登记 source ID 与本地证据，不借用价格或协议面核对。 |
| `notes` | 当前型号适用范围、兼容映射、条件限制、未核对项。 |

每个 profile：

| 字段 | 含义 |
| --- | --- |
| `interface` | 当前模型已确认的协议面 ID；不能因发现通用思考参数就给模型新增协议面。 |
| `surface` | `api_request` 是请求体；`client_setting` 是工具配置、环境变量或 CLI 参数；`client_ui` 是工具界面或交互命令。 |
| `can_disable` | true / false / null；null 是未知。思考摘要隐藏、低档位、忽略关闭参数都不能当作关闭成功。 |
| `default_behavior` | `enabled` / `disabled` / `adaptive` / `unknown`，描述不设置时的行为；组织策略、套餐或条件例外写 notes。 |
| `controls` | 已确认的控制参数，未确认参数可以为空；空列表不表示没有思考能力。 |
| `notes` | 本协议或工具入口的限制及生效条件。 |

每个 control：

- `kind`：`effort` 是深度 / 努力档位；`mode` 是模式；`toggle` 是布尔开关；`budget_tokens` 是独立的思考 token 预算。参数名叫 effort 也可能实际只切模式，按语义分类。
- `parameter`：官方名称。请求体嵌套字段用点分路径，例如 `reasoning.effort`；客户端写实际设置键、环境变量、CLI 参数或交互命令。**参数名未公布时写 null，只能 partial，不能猜一个 SDK 字段。** 以最终请求 JSON 为准，区分 SDK 的额外参数容器与供应商在线协议中的同名字段。
- `values`：已确认的官方值，保留原类型、大小写与拼写。UI 标签不是 wire 枚举；例如界面 `Extra high` 不能自动改成 `xhigh`。partial 时清单可能不完整，notes 必须交代缺口。
- `minimum` / `maximum`：预算的已知闭区间边界，仅 `budget_tokens` 使用。null 表示未核对，**不是无限制**。依本次 max_tokens 而变的上限写 notes，不能抄成模型固定预算。
- `default`：该参数省略时的官方值，未知为 null；不能填用户当前设置或自行推荐值。预算的负数 / 零哨兵值只有来源明确支持时才列入 values，并在 notes 解释。
- `notes`：档位别名映射、开关与 effort 的组合限制、预算条件、工具版本 / 套餐限制和未知范围。

保存能力清单，不保存请求配置、用户偏好、组织的实际策略、某次选择或私有会话。消费者负责让用户选取选项；发送前必须认得协议和 surface、核实 parameter 不为 null，并处理对应限制。不能把全部 controls 无条件拼进每次请求。

## 每次更新的步骤

1. 检查服务商及型号排除清单，读取本产品资料，不从同名原厂或同家其他产品继承。
2. 对每个型号检查：是否思考、能否关闭、有哪些档位 / 模式 / 预算、缺省行为、协议差异、组合限制及套餐 / 工具版本限制。非文本模型也显式留结论，不能仅按模态标 unsupported。
3. 以官方精确型号支持表、接口参数和订阅配置说明为依据。通用 schema 的所有枚举不是每个型号的支持清单；示例只证明其覆盖范围。只有搜索摘要、猜测或访问失败时保留 unknown。
4. 保存简短证据：官方 URL、UTC 获取时间、具体小节、型号范围和冲突。已知字段与未知字段分开，只有思考能力的 verification 刷新，其他字段不连带背书。
5. 更新 profiles 和独立 verification。unsupported 也必须有官方依据；known 记录必须 verified；unknown 必须 needs_review、checked_at=null、profiles=[]。已确认支持但只有一部分面或参数时用 partial。
6. 运行 validate 与单元测试。review 必须展示思考能力前后值，持续列出全部 partial / unknown，包括本次没改的缺项。仅价格不变不能跳过更新。

## 本轮容易混淆的事实

- GPT-5.2 API 的五档不能复制成 Codex 各型号的支持集。Codex Ultra 包含任务委派，不只是一档模型推理深度。
- Claude Code Fable 无法关闭思考；`--effort` 和持久化 `effortLevel` 接受的值并不完全一致。Haiku 不支持 effort 档位，但可使用扩展思考。
- MiniMax M3 的 Responses `reasoning.effort` 实际是模式开关，几个非 none 值不区分推理深度；其 Chat 与 Messages 的默认思考行为不同。M2.x 关闭参数无效。
- Kimi Code 的 K3 默认 high，按量 K3 默认 max。订阅关闭思考会改由 K2.8 Preview 承载，不能描述成同一个 K3 模型只换开关。
- Cursor 的档位属于 Cursor 自己的型号与套餐；私有 RPC 参数未公布的 UI 档位保留 parameter=null。
- thinking summary、reasoning_format、include_reasoning 是展示控制；max_output_tokens / max_completion_tokens 是总输出限制，都不是独立的思考深度预算。

逐模型数据和来源在 `evidence/<provider>/2026-09-16-reasoning.md`，本轮范围见 [REASONING-AUDIT-2026-09-16.md](REASONING-AUDIT-2026-09-16.md)。

## 格式兼容

`reasoning` 是 v1 中的可选元数据扩展：新 schema 能读取未带此字段的历史版本，旧字段语义不变；**当前仓库发布校验要求每个模型显式填写**。完整覆盖必须没有协议缺口，并覆盖每个已登记面；默认行为、关闭能力或参数名未知时只能 partial。

新增数据不代表云端或固件已接入该字段。消费者适配、展示和实际参数发送需要各自实现与验证。
