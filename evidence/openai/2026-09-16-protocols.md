# OpenAI 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-api`：https://developers.openai.com/api/docs/models/gpt-5.2
- `protocol-codex`：https://learn.chatgpt.com/docs/config-file/config-reference
- `protocol-models`：https://learn.chatgpt.com/docs/models

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `gpt-5-2` | `openai_chat`, `openai_responses` | complete | api | GPT-5.2 模型详情列出的 Chat Completions 与 Responses 推理接口；图像输入不表示图像生成协议。 |
| codex | `gpt-6-astra` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
| codex | `gpt-5-6-sol` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
| codex | `gpt-5-6-terra` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
| codex | `gpt-5-6-luna` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
| codex | `gpt-5-5` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
| codex | `gpt-5-3-codex-spark` | `openai_responses` | complete | codex, models | Codex 配置只支持 Responses wire API；此处表示 Codex 订阅承载，不能凭此调用公开按量 API 或复用 API Key。不同模型套餐准入仍看 plan_ids。 |
