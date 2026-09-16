# DeepSeek 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-deepseek`：https://api-docs.deepseek.com/guides/thinking_mode/；UTC 2026-09-16T12:46:08.453826+00:00。位置：Thinking Mode Toggle and Effort Control 三协议表、Requested effort / Actual mapped effort 表。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-cn/deepseek-flash` | supported | complete | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"]; `openai_chat/api_request: reasoning_effort` = ["minimal", "low", "medium", "high", "xhigh", "max", "ultra"]; `openai_responses/api_request: reasoning.effort` = ["none", "low", "high", "max"]; `anthropic_messages/api_request: thinking.type` = ["enabled", "disabled"]; `anthropic_messages/api_request: output_config.effort` = ["minimal", "low", "medium", "high", "xhigh", "max", "ultra"] | 按当前 Thinking Mode 的三协议对照表记录；默认 high。旧 deepseek-v4-flash 与实验 ID 不继承此结论。 |
| `api-cn/deepseek-v4-pro` | supported | complete | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"]; `openai_chat/api_request: reasoning_effort` = ["minimal", "low", "medium", "high", "xhigh", "max", "ultra"]; `openai_responses/api_request: reasoning.effort` = ["none", "low", "high", "max"]; `anthropic_messages/api_request: thinking.type` = ["enabled", "disabled"]; `anthropic_messages/api_request: output_config.effort` = ["minimal", "low", "medium", "high", "xhigh", "max", "ultra"] | 按当前 Thinking Mode 的三协议对照表记录；默认 high。旧 deepseek-v4-flash 与实验 ID 不继承此结论。 |
| `api-cn/deepseek-v4-flash` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `api-cn/deepseek-v4-flash-vision-exp` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
