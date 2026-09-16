# 智谱 BigModel 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://docs.bigmodel.cn/api-reference/模型-api/对话补全
- `protocol-messages`：https://docs.bigmodel.cn/cn/guide/develop/claude/introduction
- `protocol-coding`：https://docs.bigmodel.cn/cn/guide/develop/others
- `protocol-codex`：https://docs.bigmodel.cn/cn/coding-plan/tool/codex

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `glm-5-3` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5-3-flash` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5-2` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5-1` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5-turbo` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-7` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-7-flashx` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-7-flash` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-5-air` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-5v-turbo` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-6v` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| api-cn | `glm-4-6v-flash` | `openai_chat`, `anthropic_messages` | partial | chat, messages | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| coding-plan-cn | `glm-5-3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, codex, messages | GLM Coding Plan 的 Chat 专用根、Codex Responses 根及 Anthropic 根分别核对，不能把 /api/v1 的支持推给按量产品。 |
| coding-plan-cn | `glm-5-3-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, codex, messages | GLM Coding Plan 的 Chat 专用根、Codex Responses 根及 Anthropic 根分别核对，不能把 /api/v1 的支持推给按量产品。 |
