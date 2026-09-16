# Google Gemini 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-gemini`：https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash；UTC 2026-09-16T12:46:09.049549+00:00。位置：Capabilities → Thinking，3.7 Flash 的 minimal 不支持说明。
- `reasoning-gemini-openai`：https://ai.google.dev/gemini-api/docs/openai；UTC 2026-09-16T12:48:26.703014+00:00。位置：Thinking 的 reasoning_effort 映射表、默认模型档位与 Gemini 3 不能关闭思考的说明。
- `reasoning-gemini-thinking`：https://ai.google.dev/gemini-api/docs/thinking；UTC 2026-09-16T12:46:09.208396+00:00。位置：Controlling thinking 的逐模型默认值 / Levels Supported 表。

- `reasoning-gemini-generate-content`：https://ai.google.dev/api/generate-content；UTC 2026-09-16T13:00:50.495099Z。位置：GenerationConfig.thinkingConfig、ThinkingConfig.thinkingLevel、ThinkingLevel 枚举。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-global/gemini-3-7-flash` | supported | partial | `gemini_generate_content/api_request: generationConfig.thinkingConfig.thinkingLevel` = ["LOW", "MEDIUM", "HIGH"]; `openai_chat/api_request: reasoning_effort` = ["low", "medium", "high"] | 3.7 Flash 专页明确 low/medium/high，minimal 报错；思考指南默认 medium，兼容文档明确 Gemini 3 不能关闭思考。GenerateContent 原生字段与大写枚举已核对；其他预算参数的型号适用范围未全部核对，保留 partial。 |
