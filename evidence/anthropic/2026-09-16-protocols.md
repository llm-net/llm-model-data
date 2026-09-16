# Anthropic 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-messages`：https://platform.claude.com/docs/en/api/overview
- `protocol-chat`：https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk
- `protocol-code`：https://code.claude.com/docs/en/llm-gateway

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-global | `claude-opus-5` | `openai_chat`, `anthropic_messages` | complete | messages, chat | Messages 为原生接口；Chat 是官方用于评估的兼容层，功能不完整，官方不将它视为多数生产场景的长期方案。未登记 Responses。 |
| api-global | `claude-sonnet-5` | `openai_chat`, `anthropic_messages` | complete | messages, chat | Messages 为原生接口；Chat 是官方用于评估的兼容层，功能不完整，官方不将它视为多数生产场景的长期方案。未登记 Responses。 |
| api-global | `claude-haiku-4-5` | `openai_chat`, `anthropic_messages` | complete | messages, chat | Messages 为原生接口；Chat 是官方用于评估的兼容层，功能不完整，官方不将它视为多数生产场景的长期方案。未登记 Responses。 |
| claude-code | `claude-fable-5-1` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
| claude-code | `claude-fable-5` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
| claude-code | `claude-opus-5` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
| claude-code | `claude-sonnet-5` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
| claude-code | `claude-haiku-4-5` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
| claude-code | `claude-haiku-4-5-20251001` | `anthropic_messages` | complete | code | Claude Code 的 Anthropic Messages 订阅承载；OAuth / beta 头及订阅限制与按量 Key 不同。按量 API 的 Chat 兼容层不能自动用于此订阅。 |
