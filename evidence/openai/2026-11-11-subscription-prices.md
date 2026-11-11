# Codex 原厂 API 参考价复核

范围：`openai / codex` 已有模型的 API 参考价。更新价格缺项与图像估价基准，不改变套餐、模型身份或能力核对日期。

## 官方来源

| source ID | URL | UTC 抓取时间 | 页面位置 |
| --- | --- | --- | --- |
| `r1024-openai-pricing` | https://developers.openai.com/api/docs/pricing.md | 2026-11-11T12:37:33.378835+00:00 | Standard pricing data 的 `gpt-5.6-sol` 行、上下文阈值及表后促销说明 |
| `subscription-sol-api-model` | https://developers.openai.com/api/docs/models/gpt-5.6-sol | 2026-11-11T12:37:33.551597+00:00 | Pricing、长上下文与缓存写入说明 |

两页均成功取得官方正文，明确当前 GPT-5.6 Sol 费率属于促销，持续至 2026-11-30。只记录官方给出的日期，没有时区及精确结束时刻，不自行转换为带时区有效期。

## 查到的价格与缺项

单位均为 **USD / 1,000,000 token**。Standard 常规短上下文（输入不超过 272K token）当前输入 `4`、缓存读取 `0.40`、30 分钟缓存写入 `5`、输出 `20`；12 小时缓存写入 `10` 是另一 TTL 档，不能与 30 分钟写入累加。

超过 272K 输入 token 时，完整请求的长上下文档为输入 `8`、缓存读取 `0.80`、30 分钟缓存写入 `10`、输出 `30`；12 小时缓存写入为 `20`。Fast、Batch、Flex、地区处理附加费不混入标准短上下文基准。

当前未取得该精确型号现行非促销标准价，也未取得促销结束后确定执行的价格。不能由折扣百分比倒推原价，不能采用其他 GPT 型号或订阅 CREDIT 费率补缺。

按当前 [价格规则](../../docs/PRICING.md)，`reference_prices` 继续为 `unknown`、`rules=[]`、`verification.status=needs_review`、`checked_at=null`；上面的公开优惠数字仅留作证据。本次未知表示非促销标准基准未确认，不表示官网没有公布 API 调用价格。

## 能力边界

本轮另读 https://learn.chatgpt.com/docs/models.md（2026-11-11 12:34–12:35 UTC），当前页面未给出 GPT-5.6 Sol 在 Codex 订阅中的精确窗口或逐型号思考档位。因此保留既有 CLI 证据及其原成功日期，不从 API 型号页继承 Codex 的窗口、接口或思考参数。

## 已有正常报价与图像基准

2026-11-11T12:44:42.100184+00:00 再取 OpenAI 完整 API 价表。Codex 的七个已有正常报价文本型号 `gpt-6.1-sol`、`gpt-6.1-terra`、`gpt-6-astra`、`gpt-6-sol`、`gpt-6-luna`、`gpt-5.6-terra`、`gpt-5.6-luna` 的输入、缓存读、30 分钟缓存写与输出分量均与 Standard 短上下文表一致，不制造价格变更。

图像核对追加来源：

| source ID | URL | UTC 抓取时间 | 页面位置 |
| --- | --- | --- | --- |
| `subscription-image-api-caching` | https://developers.openai.com/api/docs/guides/image-generation.md | 2026-11-11T12:44:42.111508+00:00 | Cached input pricing |
| `codex-imagegen` | https://learn.chatgpt.com/docs/image-generation.md | 2026-11-11T12:44:42.171109+00:00 | 内置出图型号与用量说明 |

Codex 图像文档仍明确内置型号为 `gpt-image-2`。现有协议证据已确认官方客户端走 Codex Images 路径，同时保留 Responses 出图承载；本轮不把 API 新列的 Image 2.5 / 2.6 系列直接当成可选择的 Codex 请求型号。

API 完整价表给出 `gpt-image-2` Standard 的文本输入 `5`、图像输入 `8`、图像输出 `30` USD / 百万对应 token，三项不变。图像指南明确：文本缓存输入 `1.25` 与图像缓存输入 `2` 的优惠只适用于 Responses API 的图像工具，直接 Images 请求（包括编辑接口）不适用。

为遵守每模型仅一组估价基准，明确选择与当前官方客户端路径对应的 **API Images Standard** 作为参考，移除先前混入的 `input_cached_tokens=1.25`；不新增图像缓存分量，也不将任何缓存价改成零。Responses 缓存费率仍作为基准外官方事实保留在本证据与规则备注中。这里是所选 API 参考基准的收敛，不代表订阅真实扣费或否定另一已确认协议。

## 型号清单边界

2026-11-11T12:44:42.205956+00:00 查询 https://learn.chatgpt.com/docs/pricing.md，其常规模型表与当前目录一致。共享价格表另列 Daybreak Blue、Daybreak Red、GPT-Rosalind-Research；https://learn.chatgpt.com/docs/cyber-safety.md（本轮 12:44 UTC）明确 Daybreak 依赖独立准入及具体产品面。共享费率表不能单独证明这些型号是普通 Codex 订阅可选模型，不据此新增或猜测请求名。
