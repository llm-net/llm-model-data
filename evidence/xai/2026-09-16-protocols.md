# xAI 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-api`：https://docs.x.ai/developers/quickstart
- `protocol-grok45`：https://docs.x.ai/developers/models/grok-4.5
- `protocol-grok46`：https://docs.x.ai/developers/models/grok-4.6
- `protocol-grpc`：https://docs.x.ai/developers/grpc-api-reference/chat
- `protocol-build`：https://docs.x.ai/build/overview

- `protocol-chat`：https://docs.x.ai/developers/model-capabilities/legacy/chat-completions （Legacy Chat Completions 说明及模型请求示例）

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

已安装官方 Grok CLI 二进制 SHA-256：`504dd6546ab991b75d36698242875ce461489cd1f8cd84285873cb55bd5c7d54`；只读静态产物确认 `/responses` 与官方 API 根字符串，结合 Build 接入资料记录承载推断为 partial；不据此声称所有版本或订阅功能完全等价。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `grok-4-6` | `openai_chat`, `openai_responses`, `xai_grpc` | complete | api, grok45, grok46, grpc, chat | xAI 按量 Chat Completions（legacy）、Responses 与官方原生 gRPC Chat。模型名字相同不代表 Grok Build 订阅可复用这些入口。 |
| api-global | `grok-4-5` | `openai_chat`, `openai_responses`, `xai_grpc` | complete | api, grok45, grok46, grpc, chat | xAI 按量 Chat Completions（legacy）、Responses 与官方原生 gRPC Chat。模型名字相同不代表 Grok Build 订阅可复用这些入口。 |
| grok-build | `grok-4-6` | `openai_responses` | partial | build | Grok Build 工具订阅承载按官方客户端核对 Responses；不是按量 API 资格，也不继承按量 Chat 或 gRPC。本地官方二进制含 Responses 请求路径，未用订阅真实调用。 |
| grok-build | `grok-4-5` | `openai_responses` | partial | build | Grok Build 工具订阅承载按官方客户端核对 Responses；不是按量 API 资格，也不继承按量 Chat 或 gRPC。本地官方二进制含 Responses 请求路径，未用订阅真实调用。 |
