# OpenAI 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-codex-config`：https://learn.chatgpt.com/docs/config-file/config-reference；UTC 2026-09-16T12:46:08.429559+00:00。位置：model_reasoning_effort / model_reasoning_summary 配置项；通用枚举不是逐模型支持矩阵。
- `reasoning-codex-models`：https://learn.chatgpt.com/docs/models；UTC 2026-09-16T12:46:08.205192+00:00。位置：Choose a model → Codex CLI 的 Sol 思考选择器及 Recommended models。
- `reasoning-openai-guide`：https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2；UTC 2026-09-16T12:46:09.234458+00:00。位置：Reasoning effort 与 Chat / Responses 请求配置示例。
- `reasoning-openai-model`：https://developers.openai.com/api/docs/models/gpt-5.2.md；UTC 2026-09-16T12:46:08.512485+00:00。位置：GPT-5.2 介绍段 Reasoning.effort、Model details 与 Endpoints 表。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-global/gpt-5-2` | supported | complete | `openai_chat/api_request: reasoning_effort` = ["none", "low", "medium", "high", "xhigh"]; `openai_responses/api_request: reasoning.effort` = ["none", "low", "medium", "high", "xhigh"] | GPT-5.2 按量模型的官方五档；none 关闭思考。不是 Codex 订阅设置。 |
| `codex/gpt-6-astra` | supported | partial | 未确认可配置参数 | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
| `codex/gpt-5-6-sol` | supported | partial | `openai_responses/client_ui: /model` = ["Low", "Medium", "High", "Extra high", "Max"] | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
| `codex/gpt-5-6-terra` | supported | partial | 未确认可配置参数 | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
| `codex/gpt-5-6-luna` | supported | partial | 未确认可配置参数 | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
| `codex/gpt-5-5` | supported | partial | 未确认可配置参数 | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
| `codex/gpt-5-3-codex-spark` | supported | partial | 未确认可配置参数 | 官方 Codex 文档列出此型号并提供思考选择器；仅 Sol 有明确逐档示例。其他型号的档位、是否可关闭及默认值尚未逐项证实。配置键 model_reasoning_effort 的通用枚举不代表每个模型都支持。 |
