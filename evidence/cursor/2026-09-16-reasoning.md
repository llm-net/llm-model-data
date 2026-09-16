# Cursor 思考能力核对

整理时间：UTC 2026-09-16T12:53:46.356875Z。仅核对公开文档，没有真实 Key 推理测试。

## 来源与位置

- `reasoning-completion-claude-fable-5-1`：https://cursor.com/docs/models/claude-fable-5-1；UTC 2026-09-16T12:48:25.452347+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-claude-opus-5`：https://cursor.com/docs/models/claude-opus-5；UTC 2026-09-16T12:48:25.448199+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-claude-sonnet-5`：https://cursor.com/docs/models/claude-sonnet-5；UTC 2026-09-16T12:48:25.432571+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-composer-2-5`：https://cursor.com/docs/models/cursor-composer-2-5；UTC 2026-09-16T12:48:25.447873+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-gemini-3-1-pro`：https://cursor.com/docs/models/gemini-3-1-pro；UTC 2026-09-16T12:48:25.570753+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-gemini-3-8-flash`：https://cursor.com/docs/models/gemini-3-8-flash；UTC 2026-09-16T12:48:25.427306+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-gpt-5-6-luna`：https://cursor.com/docs/models/gpt-5-6-luna；UTC 2026-09-16T12:48:25.922231+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-gpt-5-6-sol`：https://cursor.com/docs/models/gpt-5-6-sol；UTC 2026-09-16T12:48:25.976621+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-gpt-5-6-terra`：https://cursor.com/docs/models/gpt-5-6-terra；UTC 2026-09-16T12:48:25.948809+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-grok-4-5`：https://cursor.com/docs/models/grok-4-5；UTC 2026-09-16T12:48:25.337141+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-grok-4-6`：https://cursor.com/docs/models/grok-4-6；UTC 2026-09-16T12:48:25.479814+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。
- `reasoning-completion-muse-spark-1-3`：https://cursor.com/docs/models/muse-spark-1-3；UTC 2026-09-16T12:48:25.998917+00:00。位置：该型号页 Thinking 能力标记、Strengths；有单列时另核对 Effort levels 与套餐限制。

## 口径

只记录本产品中已确认的控制能力，默认值指未设置时的官方行为；不保存用户本次设置。partial 不表示未列选项一定不支持。parameter=null 表示参数名未确认，禁止自动生成请求；null 预算边界不表示无限预算。详细控制字段见对应 catalog.json。旧价格、型号与协议面的证据不在本次重新核对范围。

## 逐模型结论

| 产品 / 模型 | 支持 | 覆盖 | 已核对控制 | 限制 / 缺项 |
| --- | --- | --- | --- | --- |
| `individual/composer-2-5` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/grok-4-6` | supported | partial | `cursor_agent/client_ui: None` = ["low", "medium", "high", "xhigh"] | Cursor 型号页逐档说明。Grok 的 Start（印度）套餐固定 medium，完整切换能力受套餐限制；Muse 的 extra high 是文档标签，未猜写成 xhigh。没有套用原厂 API。 |
| `individual/grok-4-5` | supported | partial | `cursor_agent/client_ui: None` = ["low", "medium", "high"] | Cursor 型号页逐档说明。Grok 的 Start（印度）套餐固定 medium，完整切换能力受套餐限制；Muse 的 extra high 是文档标签，未猜写成 xhigh。没有套用原厂 API。 |
| `individual/claude-fable-5-1` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/claude-opus-5` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/claude-sonnet-5` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/gemini-3-1-pro` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/gemini-3-8-flash` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/gpt-5-6-luna` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/gpt-5-6-sol` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/gpt-5-6-terra` | supported | partial | 未确认可配置参数 | Cursor 官方该型号页标注 Thinking；具体参数、完整档位、开关与默认值未公布，不能继承模型原厂 API。 |
| `individual/muse-spark-1-3` | supported | partial | `cursor_agent/client_ui: None` = ["minimal", "low", "medium", "high", "extra high", "max"] | Cursor 型号页逐档说明。Grok 的 Start（印度）套餐固定 medium，完整切换能力受套餐限制；Muse 的 extra high 是文档标签，未猜写成 xhigh。没有套用原厂 API。 |
