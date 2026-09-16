# Groq 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://console.groq.com/docs/openai
- `protocol-responses`：https://console.groq.com/docs/responses-api

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `openai-gpt-oss-120b` | `openai_chat`, `openai_responses` | complete | chat, responses | Groq 平台的 GPT-OSS 120B / 20B；Responses 与 Chat 各有参数限制，不继承 OpenAI 自家托管服务的其他 API。 |
| api-global | `openai-gpt-oss-20b` | `openai_chat`, `openai_responses` | complete | chat, responses | Groq 平台的 GPT-OSS 120B / 20B；Responses 与 Chat 各有参数限制，不继承 OpenAI 自家托管服务的其他 API。 |
