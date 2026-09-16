# 腾讯 TokenHub / 混元 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-language`：https://cloud.tencent.com/document/product/1823/130079
- `protocol-hy`：https://cloud.tencent.com/document/product/1823/132252
- `protocol-api`：https://cloud.tencent.com/document/product/1823/130078

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `hy4-preview` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `hy3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `hy-mt2-pro` | `openai_chat` | complete | language, hy | TokenHub 协议矩阵明确把 Hy-MT2-Pro 的 Responses / Messages 标为不支持，仅 Chat。 |
| api-cn | `hy-vision-2-0-instruct` | `openai_chat` | partial | language, hy | 视觉特定型号只登记 Chat；通用语言型号三协议矩阵未明确覆盖此型号，其他面待核对。 |
| api-cn | `deepseek-v4-pro-0813` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `deepseek-v4-flash-0731` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `glm-5-3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `kimi-k3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
| api-cn | `minimax-m3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | language, hy, api | TokenHub 逐模型协议矩阵登记三面；DeepSeek / GLM 等部分型号的 Responses 是平台服务端兼容转换，存在参数和内置工具限制。此 offering 不混入旧混元平台接口。 |
