# OpenRouter 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://openrouter.ai/docs/quickstart
- `protocol-responses`：https://openrouter.ai/docs/api_reference/responses/overview
- `protocol-messages`：https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-a-message.md

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `anthropic-claude-sonnet-latest` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, responses, messages | OpenRouter 自身提供三种入口，模型使用本平台精确 ID；协议转换发生在 OpenRouter 服务端，不等于底层训练方原生支持全部三面。 |
