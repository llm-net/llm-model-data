# 百度千帆 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://cloud.baidu.com/doc/qianfan/s/xmh4sttmy
- `protocol-messages`：https://cloud.baidu.com/doc/qianfan-docs/s/6mh3e6gjp
- `protocol-responses`：https://cloud.baidu.com/doc/qianfan-docs/s/4mi400l1m

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `ernie-5-1` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `ernie-5-0` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `ernie-4-5-turbo-128k` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `ernie-4-5-turbo-vl-32k` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `deepseek-v4-pro` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `deepseek-v4-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `glm-5-3` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `ernie-4-5-turbo-20260402` | `openai_chat`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
| api-cn | `glm-5-1` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | chat, messages, responses | 千帆声明全量 Chat 模型兼容 Messages；Responses 支持表仅列指定 DeepSeek / GLM / Qwen，当前 ERNIE 与 GLM-5.3 未列，不能整家加 Responses。 |
