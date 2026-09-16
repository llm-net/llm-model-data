# Moonshot / Kimi 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-kimi-code`：https://www.kimi.com/code/docs/en/kimi-code/models；UTC 2026-09-16T12:46:08.609263+00:00。位置：模型及思考默认值、Thinking off routes to K2.8 Preview、Effort mapping in third-party tools。
- `reasoning-moonshot`：https://platform.kimi.com/docs/api/chat.md；UTC 2026-09-16T12:46:08.646437+00:00。位置：思考模式与 Preserved Thinking、OpenAPI 的 KimiK3ChatRequest / KimiK27CodeChatRequest / KimiK26ChatRequest。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-cn/kimi-k3` | supported | partial | `openai_chat/api_request: reasoning_effort` = ["low", "high", "max"] | Chat 文档按精确 ID 分 schema；K2.7 Code 高速版明确与标准版参数一致且不可关思考。K3 使用 low/high/max，K2.6 可关闭；其他已登记协议面的参数还未补证。 |
| `api-cn/kimi-k2-7-code` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"] | Chat 文档按精确 ID 分 schema；K2.7 Code 高速版明确与标准版参数一致且不可关思考。K3 使用 low/high/max，K2.6 可关闭；其他已登记协议面的参数还未补证。 |
| `api-cn/kimi-k2-7-code-highspeed` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled"] | Chat 文档按精确 ID 分 schema；K2.7 Code 高速版明确与标准版参数一致且不可关思考。K3 使用 low/high/max，K2.6 可关闭；其他已登记协议面的参数还未补证。 |
| `api-cn/kimi-k2-6` | supported | partial | `openai_chat/api_request: thinking.type` = ["enabled", "disabled"] | Chat 文档按精确 ID 分 schema；K2.7 Code 高速版明确与标准版参数一致且不可关思考。K3 使用 low/high/max，K2.6 可关闭；其他已登记协议面的参数还未补证。 |
| `kimi-code/k3` | supported | partial | `openai_chat/api_request: None` = ["low", "high", "max"]; `anthropic_messages/api_request: None` = ["low", "high", "max"] | K3 与 K2.8 Preview 的订阅档位独立核对。none 会关闭思考并改由 K2.8 Preview（非思考）承载，不能当成原 K3 无思考版本；具体 wire 字段仍待核对。 |
| `kimi-code/k3-256k` | supported | partial | `openai_chat/api_request: None` = ["low", "high", "max"]; `anthropic_messages/api_request: None` = ["low", "high", "max"] | K3 与 K2.8 Preview 的订阅档位独立核对。none 会关闭思考并改由 K2.8 Preview（非思考）承载，不能当成原 K3 无思考版本；具体 wire 字段仍待核对。 |
| `kimi-code/kimi-for-coding` | supported | partial | `openai_chat/api_request: None` = ["low", "high", "max"]; `anthropic_messages/api_request: None` = ["low", "high", "max"] | K3 与 K2.8 Preview 的订阅档位独立核对。none 会关闭思考并改由 K2.8 Preview（非思考）承载，不能当成原 K3 无思考版本；具体 wire 字段仍待核对。 |
| `kimi-code/kimi-for-coding-highspeed` | supported | partial | `openai_chat/api_request: None` = ["low", "high", "max"]; `anthropic_messages/api_request: None` = ["low", "high", "max"] | K3 与 K2.8 Preview 的订阅档位独立核对。none 会关闭思考并改由 K2.8 Preview（非思考）承载，不能当成原 K3 无思考版本；具体 wire 字段仍待核对。 |
