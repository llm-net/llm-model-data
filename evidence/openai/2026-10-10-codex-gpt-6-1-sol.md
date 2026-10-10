# Codex — GPT-6.1 Sol 与全部型号复核

基线：`b2ce1b7b3a14764d6520e24bf2977033832f8e93`（`data-2026.09.28.2`）。只更新 Codex 产品资料；没有调用私人账号、读取配置 / 会话或发送推理请求。

## 来源与获取时间（UTC）

| source ID | 官方 URL | 获取时间 / 位置 |
| --- | --- | --- |
| r1010-models | https://learn.chatgpt.com/docs/models.md | 2026-10-10T05:39:31Z；GPT-5.5 retirement、Recommended models（ModelDetails 卡片）、GPT-6.1 Sol、Choosing a model、Other models、Deprecated Codex models |
| r1010-pricing | https://developers.openai.com/api/docs/pricing.md | 2026-10-10T05:39:31Z；Flagship models Standard 表短上下文列、Image tokens 表 |
| r1010-api-model | https://developers.openai.com/api/docs/models/gpt-6.1-sol.md | 2026-10-10T05:42:08Z；Model details、Pricing、Endpoints |
| r1010-codex-pricing | https://learn.chatgpt.com/docs/pricing.md | 2026-10-10T05:42:08Z；套餐卡片、本地消息估计表、速度档倍率表 |
| r1010-config | https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-10-10T05:42:08Z；`model_providers.<id>.wire_api`、`model_reasoning_effort` |
| r1010-speed | https://learn.chatgpt.com/docs/agent-configuration/speed.md | 2026-10-10T05:42:08Z；Fast mode、Ultrafast mode |
| r1010-imagegen | https://learn.chatgpt.com/docs/image-generation.md | 2026-10-10T05:43:17Z；第 60 行 |
| r1010-cli | https://registry.npmjs.org/@openai/codex/0.162.1-linux-x64 | 2026-10-10T05:40Z 下载，05:44Z 读取内嵌目录 |

npm `@openai/codex` latest 为 0.162.1。linux-x64 包内 `vendor/x86_64-unknown-linux-musl/bin/codex` 的 SHA-256 为 `628e35487d888a28f0427fc37501da529dd3d81fcbad7a2c3421c1e8670d92e1`。只读静态 JSON 中列表可见型号的 slug、窗口、模态、思考档位、客户端默认与升级目标，摘录见 [client-models.json](2026-10-10-client-models.json)；隐藏型号、程序、提示词与凭据不入库。与 [0.156.1 摘录](2026-09-23-client-models.json) 逐字段比较，唯一差异是新增 `gpt-6.1-sol`，已有 7 个列表型号字段不变。

## 逐型号结论

| Codex 请求名 | 可用性 | 常规 / 最大窗口 tokens | 单模型 effort / 客户端默认 | 参考价 USD（输入 / 缓存读 / 输出） |
| --- | --- | --- | --- | --- |
| gpt-6-astra | active | 272000 / 872000 | low–max / low | 10 / 1 / 50，无变化 |
| gpt-6.1-sol | 新增，推荐 | 272000 / 872000 | low–max / low | 2 / 0.1 / 10 |
| gpt-6-sol | active（不再列为推荐卡片） | 272000 / 872000 | low–max / medium | 2 / 0.2 / 10，无变化 |
| gpt-6-luna | active，推荐 | 272000 / 872000 | low–max / medium | 0.1 / 0.01 / 0.5，无变化 |
| gpt-5.6-sol | active（推出期间保留） | 272000 / 872000 | low–max / low | 4 / 0.4 / 20，无变化 |
| gpt-5.6-terra | active（推出期间保留） | 272000 / 872000 | low–max / medium | 2 / 0.2 / 12，无变化 |
| gpt-5.6-luna | active（推出期间保留） | 272000 / 872000 | low–max / medium | 0.2 / 0.02 / 1.2，无变化 |
| gpt-5.5 | active；2026-10-14 退役 | 272000 / 272000 | low–xhigh / medium | 5 / 0.5 / 30，无变化 |
| gpt-image-2 | active | 不适用 | 不适用 | 文本 5 / 1.25，图像 8 / 输出 30，无变化 |

- 官方 Models 页：推荐型号卡片为 gpt-6-astra、gpt-6.1-sol、gpt-6-luna；「For complex coding and agentic workflows, use GPT-6.1 Sol when available」。GPT-6.1 Sol、GPT-6 Sol、GPT-6 Luna 在 ChatGPT 里只在 Work 与 Codex 提供；GPT-5.6 Sol / Terra / Luna 在推出期间仍可用。GPT-6 Sol 不再有推荐卡片，但正文与 CLI 列表仍列出，Codex 定价页本地消息估计表与积分表仍单列，保持 active。
- GPT-6.1 Sol 推出范围：Plus、Pro、Business、Enterprise、Edu 的桌面应用与 CLI 及 ChatGPT Work 网页 / 移动端；Enterprise / Edu 缺省关闭，需管理员开启；Free 与 Go 推出时不含。Codex 定价页 Plus 卡片写「GPT-6.1 Sol and GPT-6 Luna」。CLI 内嵌 `available_in_plans` 列出更宽的计划代号（含 free、go），与文档推出范围不一致，以文档为准写进备注，`plan_ids` 仍不登记。
- CLI 0.162.1：gpt-6.1-sol 最低客户端 0.153.0，text / image 输入，supported_reasoning_levels low / medium / high / xhigh / max / ultra，default_reasoning_level=low，服务档 priority（Fast），`default_service_tier` 为空（gpt-6-sol / gpt-6-luna 仍为 priority）。Ultra 含自动任务委派，不登记为单次请求档位。文档写「Reasoning effort ranges from Light to Ultra. Max and Ultra depend on your settings」。
- Ultrafast：速度页写 Ultrafast 支持 GPT-6 Astra 与 GPT-6.1 Sol，限 Pro $500 及符合条件的 Enterprise / Edu；CLI 0.162.1 内嵌目录 service_tiers 只有 priority，没有 Ultrafast 档。速度档不改变参考价基准。
- 参考价取 OpenAI API Standard 短上下文列（≤272K 输入）：gpt-6.1-sol 2 / 0.1 / 10（USD / 百万 token），模型页同值，并写「Cached input tokens are priced at 5% of the uncached input token rate」。价表另列 cache writes 2.5、长上下文 4 / 0.2 / 5 / 15、Batch / Flex 半价、Fast 2x、Ultrafast 6x，本条不收录，未收录分量不视为零。本仓库 OpenAI API 目录未单独收录该型号，reference_origin 只登记 URL。
- API 模型页的 1,050,000 窗口、922,000 最大输入、128,000 最大输出与 `reasoning.effort` low–max（缺省 medium）属于按量 API，不继承到 Codex 订阅条目；Codex 窗口只取 CLI 内嵌值。
- 协议：配置参考 `wire_api` 仍写「`responses` is the only supported value」；Models 页写「Current Codex releases don't support `wire_api = "chat"`」。Codex 订阅承载登记 `openai_responses`。`reasoning.effort` 请求字段沿用 [先前请求核对](2026-09-16-codex-request-reasoning.md)，本轮未重跑请求探针；裸订阅请求默认与关闭能力仍 partial。
- 已有型号参考价：Standard 表数字与 2026-09-23 一致。价表脚注「GPT-5.6 Sol’s promotional pricing is available at least through November 21, 2026」，本仓库 gpt-5.6-sol 记录的就是当前标价 4 / 0.4 / 20，到期后复核。
- gpt-5.5：退役公告未变（2026-10-14，不影响 OpenAI API）；CLI 升级目标仍为 gpt-6-sol。今天仍 active，不提前退役。
- gpt-image-2：图像生成页仍写「Built-in image generation uses `gpt-image-2`」，CLI 0.162.1 仍内嵌该型号名；API 图像价不变。media_io 沿用 [图像输入输出核对](2026-09-28-codex-image-media-io.md)，本轮未重查客户端源码与端点行为。
- 隐藏型号（gpt-daybreak-blue-latest、gpt-daybreak-red-latest、codex-auto-review）为 `visibility=hide`，与先前做法一致不收录。

## 未变与缺项

- 未修改套餐价格、额度或实际扣费。Codex 定价页 Pro 卡片现写「Plans at $100, $200, or $500 USD per month」，本仓库 `pro-5x` 仍只登记 $100 档；$200 / $500 档本轮未收录，套餐层面留待单独核对。
- 积分单价（如 GPT-6.1 Sol 50 / 2.5 / 250 credits）按仓库规则不收录。
- 产品 active 不能替代运行期账号可见目录。
