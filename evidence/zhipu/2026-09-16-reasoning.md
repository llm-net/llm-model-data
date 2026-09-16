# 智谱 BigModel 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-zhipu`：https://docs.bigmodel.cn/cn/guide/capabilities/thinking；UTC 2026-09-16T12:46:09.129063+00:00。位置：核心参数说明中 thinking.type 与 reasoning_effort 的逐型号说明，特别是 API / Coding Plan 两组映射。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-cn/glm-5-3` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"]; `openai_chat/api_request: reasoning_effort` = ["low", "high", "max"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-5-3-flash` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"]; `openai_chat/api_request: reasoning_effort` = ["low", "high", "max"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-5-2` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"]; `openai_chat/api_request: reasoning_effort` = ["none", "minimal", "low", "medium", "high", "xhigh", "max"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-5-1` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-5` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-5-turbo` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-4-7` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-4-7-flashx` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/glm-4-7-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/glm-4-5-air` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/glm-5v-turbo` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-4-6v` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `api-cn/glm-4-6v-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `coding-plan-cn/glm-5-3` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"]; `openai_chat/api_request: reasoning_effort` = ["none", "minimal", "low", "medium", "high", "xhigh", "max"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
| `coding-plan-cn/glm-5-3-flash` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"]; `openai_chat/api_request: reasoning_effort` = ["none", "minimal", "low", "medium", "high", "xhigh", "max"] | 以深度思考页的精确型号与 API / Coding Plan 差异为准；5.3 系列思考不可关闭。Messages / Responses 的控制字段待独立核对。 |
