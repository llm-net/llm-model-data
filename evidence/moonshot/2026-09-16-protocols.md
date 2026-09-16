# Moonshot / Kimi 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://platform.kimi.com/docs/api/chat
- `protocol-responses`：https://platform.kimi.com/docs/api/responses
- `protocol-messages`：https://platform.kimi.com/docs/api/messages
- `protocol-claude`：https://platform.kimi.com/docs/guide/claude-code-kimi
- `protocol-coding`：https://www.kimi.com/code/docs/en/kimi-code/models

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `kimi-k3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, responses, messages | K3 在 Responses / Messages model 说明中明确支持；Responses 无服务端历史，与 Chat 多轮请求不同。 |
| api-cn | `kimi-k2-7-code` | `openai_chat`, `anthropic_messages` | partial | chat, claude | Claude Code 接入页另列 K2.7 Code / K2.6；Responses 当前仅明确支持 kimi-k3。与 Messages API 单页只列 K3 的差异留在证据中。 |
| api-cn | `kimi-k2-7-code-highspeed` | `openai_chat` | partial | chat | 高速独立 ID 只登记 Chat；不继承标准速度型号的 Messages，Responses 当前仅明确支持 K3。 |
| api-cn | `kimi-k2-6` | `openai_chat`, `anthropic_messages` | partial | chat, claude | Claude Code 接入页另列 K2.7 Code / K2.6；Responses 当前仅明确支持 kimi-k3。与 Messages API 单页只列 K3 的差异留在证据中。 |
| kimi-code | `k3` | `openai_chat`, `anthropic_messages` | partial | coding | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| kimi-code | `k3-256k` | `openai_chat`, `anthropic_messages` | partial | coding | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| kimi-code | `kimi-for-coding` | `openai_chat`, `anthropic_messages` | partial | coding | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| kimi-code | `kimi-for-coding-highspeed` | `openai_chat`, `anthropic_messages` | partial | coding | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
