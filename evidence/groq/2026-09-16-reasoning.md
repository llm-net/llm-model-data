# Groq 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-groq`：https://console.groq.com/docs/reasoning；UTC 2026-09-16T12:46:08.547881+00:00。位置：Supported Models、Options for Reasoning Effort (GPT-OSS)。
- `reasoning-groq-responses`：https://console.groq.com/docs/responses-api；UTC 2026-09-16T12:48:26.133567+00:00。位置：Reasoning 小节，reasoning.effort 请求示例。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-global/openai-gpt-oss-120b` | supported | partial | `openai_chat/api_request: reasoning_effort` = ["low", "medium", "high"]; `openai_responses/api_request: reasoning.effort` = ["low", "medium", "high"] | Groq 明确 GPT-OSS 20B / 120B 的三档与两个协议参数。缺省档位、是否有关闭方法仍未知；reasoning_format / include_reasoning 只控制展示，不是深度。 |
| `api-global/openai-gpt-oss-20b` | supported | partial | `openai_chat/api_request: reasoning_effort` = ["low", "medium", "high"]; `openai_responses/api_request: reasoning.effort` = ["low", "medium", "high"] | Groq 明确 GPT-OSS 20B / 120B 的三档与两个协议参数。缺省档位、是否有关闭方法仍未知；reasoning_format / include_reasoning 只控制展示，不是深度。 |
