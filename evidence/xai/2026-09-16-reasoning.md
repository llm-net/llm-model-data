# xAI 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-xai`：https://docs.x.ai/developers/models/grok-4.6；UTC 2026-09-16T12:46:09.860854+00:00。位置：Capabilities → Reasoning efforts。
- `reasoning-xai-reasoning`：https://docs.x.ai/developers/model-capabilities/text/reasoning；UTC 2026-09-16T12:48:26.452852+00:00。位置：The reasoning_effort parameter、Effort levels、Summary table；4.5 的 xhigh 实际按 high 处理。
- `reasoning-xai45`：https://docs.x.ai/developers/models/grok-4.5；UTC 2026-09-16T12:46:09.823320+00:00。位置：Capabilities → Reasoning efforts；与推理专文有冲突。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `api-global/grok-4-6` | supported | partial | `openai_chat/api_request: reasoning_effort` = ["low", "medium", "high", "xhigh"]; `openai_responses/api_request: reasoning.effort` = ["low", "medium", "high", "xhigh"] | 推理专页明确不能关闭；4.5 专页的 xhigh 标记与推理专页支持表冲突，只登记双方一致的三档。原生 gRPC 控制字段仍待证实。 |
| `api-global/grok-4-5` | supported | partial | `openai_chat/api_request: reasoning_effort` = ["low", "medium", "high"]; `openai_responses/api_request: reasoning.effort` = ["low", "medium", "high"] | 推理专页明确不能关闭；4.5 专页的 xhigh 标记与推理专页支持表冲突，只登记双方一致的三档。原生 gRPC 控制字段仍待证实。 |
| `grok-build/grok-4-6` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
| `grok-build/grok-4-5` | unknown | unknown | 未确认可配置参数 | 未取得本产品、本精确模型 ID 的完整思考控制依据；通用接口或同名原厂模型不作为支持证据。参数、档位、默认值及开关保持未知。 |
