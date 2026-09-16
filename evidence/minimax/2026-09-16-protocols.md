# MiniMax 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://platform.minimax.cn/docs/api-reference/text-openai-api
- `protocol-messages`：https://platform.minimax.cn/docs/api-reference/text-anthropic-api
- `protocol-responses`：https://platform.minimax.cn/docs/api-reference/responses-create
- `protocol-native`：https://platform.minimax.cn/docs/api-reference/text-post
- `protocol-image`：https://platform.minimax.cn/docs/api-reference/image-generation-t2i
- `protocol-video`：https://platform.minimax.cn/docs/api-reference/video-generation-v2-create
- `protocol-speech`：https://platform.minimax.cn/docs/api-reference/speech-t2a-http
- `protocol-plan`：https://platform.minimax.cn/docs/token-plan/quickstart
- `protocol-codex`：https://platform.minimax.cn/docs/token-plan/codex
- `protocol-cursor`：https://platform.minimax.cn/docs/token-plan/cursor

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `minimax-m3` | `openai_chat`, `openai_responses`, `anthropic_messages`, `minimax_text` | complete | chat, responses, messages, native | M3 / M2.7 系列三种兼容文本面；原生 text/chatcompletion_v2 仍有型号文档，但已标 deprecated。Responses 的 M2.x 思考不可关闭，与 M3 不同。 |
| api-cn | `minimax-m2-7` | `openai_chat`, `openai_responses`, `anthropic_messages`, `minimax_text` | complete | chat, responses, messages, native | M3 / M2.7 系列三种兼容文本面；原生 text/chatcompletion_v2 仍有型号文档，但已标 deprecated。Responses 的 M2.x 思考不可关闭，与 M3 不同。 |
| api-cn | `minimax-m2-7-highspeed` | `openai_chat`, `openai_responses`, `anthropic_messages`, `minimax_text` | complete | chat, responses, messages, native | M3 / M2.7 系列三种兼容文本面；原生 text/chatcompletion_v2 仍有型号文档，但已标 deprecated。Responses 的 M2.x 思考不可关闭，与 M3 不同。 |
| api-cn | `image-01` | `minimax_image` | complete | image | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `image-01-live` | `minimax_image` | complete | image | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `minimax-h3` | `minimax_video` | complete | video | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-2-8-hd` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-2-8-turbo` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-2-6-hd` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-2-6-turbo` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-02-hd` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| api-cn | `speech-02-turbo` | `minimax_speech` | complete | speech | 按当前型号 API 登记厂商面：图片 image-01 系列、H3 v2 视频任务或 speech TTS；TTS HTTP / WebSocket 与异步方式归同一面，具体操作并非所有型号均支持。 |
| token-plan-cn | `minimax-m3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | plan, codex, cursor | Token Plan 的 Anthropic 快速开始及 Codex / Cursor 接入说明确认三种文本面；用订阅凭证，未把按量原生废弃接口扩给订阅。 |
| token-plan-cn | `minimax-m2-7` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | plan, codex, cursor | Token Plan 的 Anthropic 快速开始及 Codex / Cursor 接入说明确认三种文本面；用订阅凭证，未把按量原生废弃接口扩给订阅。 |
