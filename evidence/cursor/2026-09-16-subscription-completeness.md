# Cursor 模型补漏

UTC 核对时间：2026-09-16T10:27:21.232069Z；公开资料核对，未实调。
## 身份来源

以下各官方详情页顶部 Model ID 字段直接确认请求 ID；不是从展示名或开发方 API 名猜测。
- completion-composer-2-5：https://cursor.com/docs/models/cursor-composer-2-5 → `composer-2.5`。
- completion-grok-4-6：https://cursor.com/docs/models/grok-4-6 → `grok-4.6`。
- completion-grok-4-5：https://cursor.com/docs/models/grok-4-5 → `grok-4.5`。
- completion-claude-fable-5-1：https://cursor.com/docs/models/claude-fable-5-1 → `claude-fable-5-1`。
- completion-claude-opus-5：https://cursor.com/docs/models/claude-opus-5 → `claude-opus-5`。
- completion-claude-sonnet-5：https://cursor.com/docs/models/claude-sonnet-5 → `claude-sonnet-5`。
- completion-gemini-3-1-pro：https://cursor.com/docs/models/gemini-3-1-pro → `gemini-3.1-pro`。
- completion-gemini-3-8-flash：https://cursor.com/docs/models/gemini-3-8-flash → `gemini-3.8-flash`。
- completion-gpt-5-6-luna：https://cursor.com/docs/models/gpt-5-6-luna → `gpt-5.6-luna`。
- completion-gpt-5-6-sol：https://cursor.com/docs/models/gpt-5-6-sol → `gpt-5.6-sol`。
- completion-gpt-5-6-terra：https://cursor.com/docs/models/gpt-5-6-terra → `gpt-5.6-terra`。
- completion-muse-spark-1-3：https://cursor.com/docs/models/muse-spark-1-3 → `muse-spark-1.3`。

## 同平台参考价

completion-pricing：https://cursor.com/docs/models-and-pricing ，Cursor Models / Other Models 标准行；单位 USD/百万 token。仅用于参考价，不调查订阅实际扣费。

| request_id | 输入 | 缓存读 | 输出 | 官网缓存写（TTL 未明确） |
| --- | --- | --- | --- | --- |
| composer-2.5 | 0.5 | 0.2 | 2.5 | — |
| grok-4.6 | 2 | 0.5 | 6 | — |
| grok-4.5 | 2 | 0.5 | 6 | — |
| claude-fable-5-1 | 10 | 0.25 | 50 | 12.5 |
| claude-opus-5 | 5 | 0.5 | 25 | 6.25 |
| claude-sonnet-5 | 2 | 0.2 | 10 | 2.5 |
| gemini-3.1-pro | 2 | 0.2 | 12 | — |
| gemini-3.8-flash | 0.75 | 0.075 | 3.5 | — |
| gpt-5.6-luna | 0.2 | 0.02 | 1.2 | 0.25 |
| gpt-5.6-sol | 4 | 0.4 | 20 | 5 |
| gpt-5.6-terra | 2 | 0.2 | 12 | 2.5 |
| muse-spark-1.3 | 1.25 | 0.15 | 4.25 | — |

本轮从 1 项补至 12 项。Composer 原价格不变，request_id 从 null 修为官网明确的 composer-2.5。缓存写入未明确 TTL，不能塞入 cache_write_5m_tokens/1h，先保留数值于备注；横杠不是 0。只收页面当前标准行，仍 coverage=partial；Fast、Thinking、长上下文是变体，不拆多套价。Pro/Pro Plus/Ultra 页内明确覆盖两类模型池，关联三档；未增加地区套餐，原套餐与额度不改。所有生效时间保持 null。
