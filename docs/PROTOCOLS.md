# 模型协议面维护

协议面与模型身份、可用性、价格同属每次更新的必查项。**不能只补模型名和价格，也不能把同一服务商的所有模型复制成同一组协议面。**

## 数据字段

每个模型的 `capabilities.interfaces` 是该产品下已经有证据的协议面 ID 列表。`capabilities.interface_assessment` 保存本次协议核对的独立结论：

- `coverage: complete`：本次来源范围内，已核对当前模型的推理接口与兼容接口；不承诺未来无新增接口，也不等于真实 Key 实调通过。
- `coverage: partial`：已确认列表内的面，但仍有具体缺口或型号适用范围待证实，必须写进 `notes`。
- `coverage: unknown`：尚未取得可支持该型号的协议证据，`interfaces=[]`、`verification.status=needs_review`、`checked_at=null`。未知不能被解释为不支持，更不能默认补 Chat。
- `verification`：协议面独立的来源 ID、本地证据和核对时间，不沿用价格核对结果。非空协议面列表必须有已核对来源及本地证据。

能力字段中的 `input_modalities` / token 上限等没有核对时仍为空 / null。补协议面不意味着重新验证这些能力，也不刷新原模型和价格的 verification。

协议面注册表为 [schemas/protocol-faces.json](../schemas/protocol-faces.json)。已有云端共同协议面沿用相同 ID 和展示名：

| 类型 | ID |
| --- | --- |
| 文本兼容面 | `openai_chat`、`openai_responses`、`anthropic_messages` |
| 图像 | `openai_image`、`minimax_image`、`ark_image`、`bailian_image` |
| 视频 | `minimax_video`、`ark_video`、`bailian_video`、`kling_video` |
| 语音 | `minimax_speech` |
| 其他已核对的供应商协议 | `gemini_generate_content`、`bailian_text`、`minimax_text`、`xai_grpc` |
| 私有工具订阅承载 | `cursor_agent` |

同一协议面的同步 / SSE / WebSocket 传输和异步任务查询不重复建面。厂商 body 与操作不同，即使路径都叫 `images/generations`，也不能直接判定为 `openai_image`。厂商 slug（如 `ark`）不是协议面。新发现无法表达的协议时，先增注册表、schema、证据和测试，不能使用 `native` / `vendor_native` 占位，也不把 Gemini 原生面称作 OpenAI Chat。

本字段的范围是**当前 catalog 所收录模型的直接推理协议，以及订阅工具实际使用的模型承载协议**。另行购买的托管 Agent / Conversations 产品、管理 API、计费查询、模型发现、文件上传、批任务外包装不因同平台存在就附加到本模型。尚未收录的 embedding / rerank 等模型不在本轮新增范围。

## 每次更新步骤

1. 先查 [服务商排除清单](../schemas/excluded-providers.json) 和 provider.json 的模型排除清单。硅基流动与 Together AI 已由用户整家排除，旧证据与导入快照不得用来恢复它们。
2. 列出所更新产品的每一个模型，包括订阅模型、日期版、短名、别名与未知请求 ID。逐模型检查已有协议面是否仍有有效依据。
3. 检查官方推理 API、兼容层文档、型号支持矩阵及套餐接入说明。按量 API、API 订阅、编程工具订阅的来源独立；同名原厂模型不能证明聚合平台支持该协议。
4. 对文本逐项检查 Chat、Responses、Messages 以及该厂商公开的原生协议；对图像、视频、语音核对实际生成 / 任务 API。型号支持表优先于平台概述。HTTP 401 / 403 只说明鉴权行为，不能证明某型号可用。
5. 记录 source ID、官方 URL、UTC 时间、页面具体小节和型号适用范围；私有订阅协议若依据官方客户端产物，记版本和 SHA-256，只摘录必要协议标识，不提交程序、凭据、会话或私有流量。
6. 更新 interfaces 与独立 assessment。部分支持、已废弃但仍有文档的面、兼容转换、参数限制、未知范围写清。不能为通过检查而复制整家的面、把 unknown 改 complete 或把未知列表补成默认面。
7. 同时按 [REASONING.md](REASONING.md) 核对每个面上的思考控制；协议支持不等于接受其他面相同的 reasoning 参数。
8. 运行 `python scripts/catalog.py validate` 和单元测试；生成 review 时核对**协议面增删、覆盖状态、来源变动、全部 partial / unknown 清单**。模型名与价格不变但协议面变化，也必须出候选报告。

## 本轮已发现的差异

- Anthropic API 提供 Messages 和用于评估的 Chat 兼容层；Claude Code 订阅不能继承该 Chat 层。
- Codex 使用 Responses 承载；Cursor 使用私有 Agent RPC，不能因模型由 OpenAI / Anthropic 提供而标记为它们的 API。
- 百炼 Coding Plan 明确不支持 Responses；Token Plan 和按量产品独立核对。百炼 Responses 的部分型号只有基础兼容能力，内置 Agent 工具受限。
- Kimi 按量 Responses 明确列 K3，其他型号不能照抄；Kimi Code 的四个模型 ID 另有独立接入表。
- 千帆 Responses 支持表没有覆盖全部 ERNIE / GLM；TokenHub Hy-MT2-Pro 的 Responses 和 Messages 被明确标为不支持。
- MiniMax 原生 `text/chatcompletion_v2` 已标 deprecated，不能把“仍有文档”写成推荐的新接口。

完整逐模型结论和来源在 `evidence/<provider>/2026-09-16-protocols.md`；总体缺口见 [PROTOCOL-AUDIT-2026-09-16.md](PROTOCOL-AUDIT-2026-09-16.md)。

## 兼容与消费者

这是 v1 的可选元数据扩展：已有 `interfaces` 保持“协议 ID 列表”语义，新增 `interface_assessment`；JSON Schema 保留读取旧 v1 记录的能力。**当前仓库的发布校验**要求所有模型都有 interfaces 和 assessment，旧版本内容不能不经核对直接重发。旧 `gemini` / `vendor_native` 值仅在 schema 中保留历史兼容，当前发布校验拒绝它们。

供应商协议面存在不表示云端 / 设备已实现，也不自动创建部署地址或开启渠道。消费者应识别自己支持的规范 ID，展示不支持 / 未核对状态；不能静默把原生面降成 Chat，也不能从协议清单猜 Key、endpoint 或模型重命名。模型协议事实与运行期探测结果须分开。

本轮修改的是资料仓库。既有消费者中的协议映射和界面是否接入这些新增字段，要在消费者自身的变更与验证中说明，不能因数据已填写就宣称激活后协议路由已同步。
