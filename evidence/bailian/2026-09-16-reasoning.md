# 阿里云百炼 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-bailian`：https://help.aliyun.com/zh/model-studio/deep-thinking；UTC 2026-09-16T12:46:09.025673+00:00。位置：支持的模型（逐型号默认值及混合 / 仅思考）、限制思考长度。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-cn/qwen3-8-max` | supported | partial | `openai_chat/api_request: enable_thinking` = [true, false]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true, false]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/qwen3-8-max-prime` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/qwen3-7-plus` | supported | partial | `openai_chat/api_request: enable_thinking` = [true, false]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true, false]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/qwen3-8-flash` | supported | partial | `openai_chat/api_request: enable_thinking` = [true, false]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true, false]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/qwen3-7-flash` | supported | partial | `openai_chat/api_request: enable_thinking` = [true, false]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true, false]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/qwen3-coder-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/qwen3-vl-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/qwen3-vl-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/qwen3-8-2-4t-a95b` | supported | partial | `openai_chat/api_request: enable_thinking` = [true]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/qwen3-8-27b` | supported | partial | `openai_chat/api_request: enable_thinking` = [true, false]; `openai_chat/api_request: thinking_budget` = []; `bailian_text/api_request: enable_thinking` = [true, false]; `bailian_text/api_request: thinking_budget` = [] | 百炼深度思考页逐型号区分混合 / 仅思考与默认值。Responses / Messages 的具体控制方式以及 budget 数值仍待核对；不复制到 Coding Plan 或 Token Plan。 |
| `api-cn/minimax-minimax-m3` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/xiaomi-mimo-v2-5-pro` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/stepfun-step-3-7-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/wan3-0-video` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `api-cn/wan3-0-video-prime` | unknown | unknown | 未确认可配置参数 | 当前是图片、视频或语音型号；本轮未取得其思考控制能力的型号证据。不能按模态推断“不支持”，也不把质量、速度或生成预算当成思考深度。 |
| `coding-plan-cn/qwen3-7-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/qwen3-6-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/kimi-k2-5` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/glm-5` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/minimax-m2-5` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/qwen3-5-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/qwen3-max-2026-01-23` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/qwen3-coder-next` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/qwen3-coder-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/glm-4-7` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/qwen3-8-max` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/qwen3-8-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/qwen3-7-plus` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/deepseek-v4-pro` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/deepseek-v4-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/kimi-k2-7-code` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/kimi-k2-6` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/glm-5-2` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/glm-5-1` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `token-plan-cn/glm-5` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
