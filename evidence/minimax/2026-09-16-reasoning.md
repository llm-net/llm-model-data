# MiniMax 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-minimax`：https://platform.minimax.cn/docs/api-reference/responses-create；UTC 2026-09-16T12:46:08.918757+00:00。位置：reasoning 参数、M3 的 none / 非 none 语义与 M2.x 关闭无效说明。
- `reasoning-minimax-chat`：https://platform.minimax.cn/docs/api-reference/text-openai-api；UTC 2026-09-16T12:48:26.809093+00:00。位置：MiniMax-M3 请求参数、Thinking 控制。
- `reasoning-minimax-messages`：https://platform.minimax.cn/docs/api-reference/text-anthropic-api；UTC 2026-09-16T12:48:26.098715+00:00。位置：Thinking 控制、Messages 字段支持。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-cn/minimax-m3` | supported | partial | `openai_chat/api_request: thinking.type` = ["adaptive", "disabled"]; `anthropic_messages/api_request: thinking.type` = ["adaptive", "disabled"]; `openai_responses/api_request: reasoning.effort` = ["none", "minimal", "low", "medium", "high"] | M3 的 Chat 默认开启，Messages / Responses 默认关闭；M2.x 不能关闭。废弃原生文本面的控制参数未核对，整体 partial。 |
| `api-cn/minimax-m2-7` | supported | partial | 未确认可配置参数 | M3 的 Chat 默认开启，Messages / Responses 默认关闭；M2.x 不能关闭。废弃原生文本面的控制参数未核对，整体 partial。 |
| `api-cn/minimax-m2-7-highspeed` | supported | partial | 未确认可配置参数 | M3 的 Chat 默认开启，Messages / Responses 默认关闭；M2.x 不能关闭。废弃原生文本面的控制参数未核对，整体 partial。 |
| `api-cn/image-01` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/image-01-live` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/minimax-h3` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-2-8-hd` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-2-8-turbo` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-2-6-hd` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-2-6-turbo` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-02-hd` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/speech-02-turbo` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `token-plan-cn/minimax-m3` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/minimax-m2-7` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
