# Google Gemini 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-compatibility`：https://ai.google.dev/gemini-api/docs/openai
- `protocol-model`：https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `gemini-3-7-flash` | `openai_chat`, `gemini_generate_content` | complete | compatibility, model | Gemini 3.7 Flash 的原生 GenerateContent 与 OpenAI Chat 兼容层。云端或设备是否实现原生面是消费者能力，不改变供应商事实。 |
