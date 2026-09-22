# Codex 可用性与退役范围复核

基线：`747a09c0831c7f4213e6f68df48e49456947e7b6`。仅更新 Codex 产品资料；没有调用私人账号、读取配置/会话或发送推理请求。

## 来源与获取时间

| source ID | 官方 URL | UTC 获取时间 / 位置 |
| --- | --- | --- |
| refresh-models | https://learn.chatgpt.com/docs/models.md | 2026-09-22T05:37:10Z；推荐模型、Other models、Deprecated Codex models |
| refresh-speed | https://learn.chatgpt.com/docs/agent-configuration/speed.md | 2026-09-22T05:37:10Z；完整正文 |
| refresh-config | https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-09-22T05:37:10Z；wire_api、model_reasoning_effort |
| refresh-pricing | https://developers.openai.com/api/docs/pricing.md | 2026-09-22T05:38:11Z；Standard pricing data |
| refresh-cli | https://learn.chatgpt.com/docs/config-file/config-reference | 2026-09-22T05:42:30Z；结合本机官方 CLI 0.155.1 的内嵌逐型号目录 |

官方 CLI Linux x86_64 0.155.1 的 SHA-256 为 `0753dfe1d8b87a52436deb13eb1c549661ef4c84fee2c5aa688385eebeccb761`。只读静态 JSON 中的精确 slug、窗口、模态、思考档位与客户端默认；必要字段摘录见 [client-models.json](2026-09-22-client-models.json)。程序、提示词、账号目录与凭据不入库。

## 逐型号结论

| Codex 请求名 | 可用性 | 常规 / 最大窗口 tokens | 单模型 effort / 客户端默认 |
| --- | --- | --- | --- |
| gpt-6-astra | active，受套餐和灰度约束 | 272000 / 872000 | low, medium, high, xhigh, max / low |
| gpt-5.6-sol | active | 272000 / 872000 | low, medium, high, xhigh, max / low |
| gpt-5.6-terra | active | 272000 / 872000 | low, medium, high, xhigh, max / medium |
| gpt-5.6-luna | active | 272000 / 872000 | low, medium, high, xhigh, max / medium |
| gpt-5.5 | active；2026-10-14 退役 | 272000 / 272000 | low, medium, high, xhigh / medium |
| gpt-5.3-codex-spark | unknown；不判全局 retired | unknown | unknown |

前五项当前英文官方模型页仍收录，0.155.1 内嵌目录逐项确认窗口和档位，均含 text/image 输入。窗口是客户端目录默认，不是账号授权或服务端极限保证；最大窗口只保存在说明中。Ultra 包含任务委派，不作为单次模型深度。Responses 的 `reasoning.effort` 字段沿用 [先前请求核对](2026-09-16-codex-request-reasoning.md)，本次未重跑请求探针；各型号裸订阅请求默认、关闭能力仍 partial。

已核对 Chat、Responses、Messages：当前 Codex 配置的 wire_api 仅支持 Responses；自定义 API provider 与 ChatGPT 订阅不能混同。Spark 只保留历史 Responses 承载证据及旧核对日期，覆盖降为 partial，不能作为当前可调用证明。

Spark 已不在本轮英文 Models/Speed 正文或 0.155.1 内嵌目录中；检索到的旧本地化页面仍描述 Pro 研究预览。这种差异没有明确的全局退役日期，故 `availability=unknown`、模型 verification 为 needs_review，移除未经当前核实的 Pro 套餐关联。原思考 supported 只来自通用选择器，缺逐型号依据，降为 unknown。其上下文与按量参考价仍 unknown。没有以任何私人账号读数建立全局事实。

官方已明确 GPT-5.4/5.4-mini 在 2026-08-31 退出 ChatGPT 登录的 Codex，GPT-5.2/5.3-codex 已 deprecated；这些原本不在本产品目录内，不重新加入。GPT-5.5 的未来退役不影响 OpenAI API，本次也不修改 API 产品。

## 价格及剩余缺项

前五项原有输入/缓存读/输出三个参考价分量与当前 Standard 短上下文表一致，没有改数字。GPT-5.5 的 selection 从“不超过 272K”修正为表中的“严格少于 272K”。Astra/5.6 新表还列 cache writes，当前条目未表达其数量口径；不能解释为免费。本轮保留这些参考价原核对时间和来源，不声称已完整复核现金结算。Spark 无对应公开 API 价，不用其他 Codex 型号近似。

未修改套餐价格、额度或实际扣费。全部 Codex 思考 partial/unknown、Spark 上下文 unknown、Spark 协议 partial 与参考价 unknown 必须进入候选报告。产品 active 始终不能替代运行期账号可见目录。
