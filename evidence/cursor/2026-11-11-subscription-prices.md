# Cursor 编程工具订阅参考价复核

范围：`cursor / individual` 已有模型的参考价。对缺价型号同时查询本产品官方型号页和模型开发方 Google 的 API 价格，不改套餐或模型身份。

## 官方来源

| source ID | URL | UTC 抓取时间 | 页面位置 |
| --- | --- | --- | --- |
| `r1111-gemini-4-carbon` | https://cursor.com/docs/models/gemini-4-carbon | 2026-11-11T12:37:33.423496+00:00 | Pricing 及表后推出优惠说明；Context window、Max context、Effort levels |
| `subscription-google-api-pricing` | https://aistudio.google.com/docs/pricing | 2026-11-11T12:37:33.905375+00:00 | Gemini 4 Carbon → Standard |
| `subscription-google-carbon-intro` | https://aistudio.google.com/docs/whats-new-gemini-4-carbon | 2026-11-11T12:37:33.630722+00:00 | New model、Pricing |

各页均成功取得官方正文。Cursor 与 Google 均明确当前为 introductory 费率；不能因为所选服务档叫 Standard 就将其视为非促销标准价。

## 查到的价格与缺项

单位为 **USD / 1,000,000 token**。本产品和 Google API 当前输入 `2`、缓存读取 `0.10`、输出（包括思考 token）`10`，持续至 2026-11-30。官网另列 2026-12-01 起输入 `4`、缓存读取 `0.20`、输出 `20`，尚未生效。

Google 仅支持隐式缓存，不支持显式缓存；Cursor 缓存写入列为横线，未据此填写零价或猜测 TTL。官方没有给出上述切换日期的时区与精确时刻，不自行填入带时区有效期。

本产品与原厂均无当前非促销标准基准，按 [价格规则](../../docs/PRICING.md) 保留 `reference_prices.status=unknown`、`rules=[]`、`verification.status=needs_review`、`checked_at=null`。优惠数字和未来数字只留证据，不能提前采用未来价，也不能拿其他 Gemini 型号或 Contributor 数据许可档补价。这里的缺项不是“未查原厂”或“官网未公布 API 价格”。

## 产品与能力边界

Cursor 型号页明确旧版套餐使用 Other Models pool；新售 The X Subscription 的预付费规则不覆盖旧版 `individual` 套餐资料。

该页仍标常规窗口 `200k`、Max context `1M`；effort 为 `low / medium / high`，默认 `medium`。没有新的精确整数单位说明、私有 RPC 参数或关闭思考说明，维持已有能力与 partial 结论及原核对日期，不借原厂 API 的 1,048,576 窗口补本产品窗口。

## 已有正常报价复核

2026-11-11 12:42:41–12:42:42 UTC 成功逐页取得下列官方型号页的 Pricing 表，覆盖其余 25 条 `published` 型号（同页 Standard / Fast 分开比对）。当前已保存的价格数字及分量均一致：

| 官方页面 | 对应型号或档位 |
| --- | --- |
| https://cursor.com/docs/models/cursor-composer-2-5 | Composer 2.5、Fast |
| https://cursor.com/docs/models/grok-4-5 | Grok 4.5 |
| https://cursor.com/docs/models/grok-4-6 | Grok 4.6 |
| https://cursor.com/docs/models/grok-4-7 | Grok 4.7 |
| https://cursor.com/docs/models/claude-fable-5-1 | Claude Fable 5.1 |
| https://cursor.com/docs/models/claude-fable-5-2 | Claude Fable 5.2 |
| https://cursor.com/docs/models/claude-opus-5 | Claude Opus 5、Fast |
| https://cursor.com/docs/models/claude-opus-5-5 | Claude Opus 5.5、Fast |
| https://cursor.com/docs/models/claude-sonnet-5 | Claude Sonnet 5 |
| https://cursor.com/docs/models/claude-sonnet-5-5 | Claude Sonnet 5.5 |
| https://cursor.com/docs/models/claude-haiku-5-5 | Claude Haiku 5.5 |
| https://cursor.com/docs/models/gemini-3-1-pro | Gemini 3.1 Pro |
| https://cursor.com/docs/models/gemini-3-8-flash | Gemini 3.8 Flash |
| https://cursor.com/docs/models/gemini-4-argon | Gemini 4 Argon |
| https://cursor.com/docs/models/gpt-5-6-luna | GPT-5.6 Luna、Fast |
| https://cursor.com/docs/models/gpt-5-6-sol | GPT-5.6 Sol、Fast |
| https://cursor.com/docs/models/gpt-5-6-terra | GPT-5.6 Terra、Fast |
| https://cursor.com/docs/models/muse-spark-1-3 | Muse Spark 1.3 |
| https://cursor.com/docs/models/muse-wonder | Muse Wonder 1.0 |

Muse Wonder 于 2026-11-11T12:43:54.676540+00:00、Muse Spark 1.3 于 2026-11-11T12:43:55.080464+00:00 再次核对：虽表格 Cache Write 是横线，两页表后正文均明确不收缓存写入费，所以保留既有零价；并非把横线当零。

Cursor 的 Gemini 4 Argon、Gemini 3.8 Flash、GPT-5.6 Sol / Fast 当前本产品型号页没有限期优惠条件。按同平台优先的既有顺序保留 Cursor 明确公布的本产品价，不将原厂 API 的促销期限或其他条件自动移植到 Cursor。Carbon 的本产品页则明确推出优惠，按前述规则继续保留缺项。

2026-11-11T12:44:42.287640+00:00 核对 https://cursor.com/docs/models-and-pricing，当前列出的基础型号在目录已有对应项，未发现明确漏收的基础型号。Grok 型号页另有 Fast 与 500k 价格档；不能把价格表中的速度或上下文档名直接猜成新增请求型号。本轮不新增档位模型或改已有请求名。
