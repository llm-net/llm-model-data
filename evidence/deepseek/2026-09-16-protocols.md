# DeepSeek 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://api-docs.deepseek.com/quick_start/pricing/
- `protocol-responses`：https://api-docs.deepseek.com/api/create-response/
- `protocol-messages`：https://api-docs.deepseek.com/guides/anthropic_api/

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `deepseek-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, responses, messages | Responses model 枚举明确列此 ID；Messages 文档说明 DeepSeek 型号与 Claude 名称映射。不能把不支持型号自动回退的响应当作原型号支持证据。 |
| api-cn | `deepseek-v4-pro` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, responses, messages | Responses model 枚举明确列此 ID；Messages 文档说明 DeepSeek 型号与 Claude 名称映射。不能把不支持型号自动回退的响应当作原型号支持证据。 |
| api-cn | `deepseek-v4-flash` | `openai_chat` | partial | chat, responses, messages | 按现有目录和官方 Chat 模型资料登记 Chat；新版 Responses 枚举只列 deepseek-flash / deepseek-v4-pro，Messages 对未知名称会回退，尚未证实此旧 ID 的精确路由，不扩填。 |
| api-cn | `deepseek-v4-flash-vision-exp` | `openai_chat` | partial | chat, responses, messages | 按现有目录和官方 Chat 模型资料登记 Chat；新版 Responses 枚举只列 deepseek-flash / deepseek-v4-pro，Messages 对未知名称会回退，尚未证实此旧 ID 的精确路由，不扩填。 |
