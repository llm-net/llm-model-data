# Anthropic — Claude Code 新增 Sonnet 5.5 / Haiku 5.5 与全部型号复核

基线：`b2ce1b7b3a14764d6520e24bf2977033832f8e93`（`data-2026.09.28.2`）。范围：只更新 Claude Code 产品；API 目录未改。没有真实 Key 实调，没有读取账号、配置或会话。

## 来源与获取时间（UTC）

| source ID | 官方 URL | 获取时间 / 位置 |
| --- | --- | --- |
| r1010-code-models | https://code.claude.com/docs/en/model-config.md | 2026-10-10T08:11:08Z；Model aliases、alias 解析表、版本要求 Note、`default` model setting、Adjust effort level、Extended thinking、Extended context、Haiku 5.5 context window and pricing、Version history |
| r1010-pricing | https://platform.claude.com/docs/en/about-claude/pricing.md | 2026-10-10T08:11:08Z；Model pricing 表、脚注 1/2/3、缓存倍率表 |
| r1010-effort | https://platform.claude.com/docs/en/build-with-claude/effort.md | 2026-10-10T08:11:08Z；Effort levels、Recommended effort levels for Claude Sonnet 5.5 / Haiku 5.5 |
| r1010-code-protocol | https://code.claude.com/docs/en/llm-gateway-protocol.md | 2026-10-10T08:11:08Z；API formats |
| r1010-sonnet-5-5 | https://platform.claude.com/docs/en/models/sonnet-5-5/overview.md | 2026-10-10T08:11:34Z；Model IDs、Pricing、Capabilities、Availability、Good to know |
| r1010-haiku-5-5 | https://platform.claude.com/docs/en/models/haiku-5-5/overview.md | 2026-10-10T08:11:34Z；Model IDs、Pricing、Capabilities、Availability、Good to know |

## Claude Code 模型配置页

- Alias 解析表：Anthropic API 上 `opus` / `sonnet` / `haiku` 分别是 Opus 5.5 / Sonnet 5.5 / Haiku 5.5；Claude Platform on AWS 为 Opus 5.5 / Sonnet 4.6 / Haiku 4.5；Bedrock 与 Google Cloud Agent Platform 为 Opus 5.5 / Sonnet 4.5 / Haiku 4.5。
- Version history：v2.1.284 起 `sonnet` 在 Anthropic API 解析到 Sonnet 5.5；v2.1.293 起 `haiku` 解析到 Haiku 5.5。Note：「Sonnet 5.5 requires Claude Code v2.1.284 or later … Use v2.1.293 or later with Haiku 5.5」。
- `default`：Pro / Max / Team / Enterprise 与 Anthropic API 仍为 Opus 5.5。
- Effort 支持表：Opus 5.5、Sonnet 5.5、Haiku 5.5、Opus 5、Sonnet 5 都是 low / medium / high / xhigh / max。Claude Code 缺省：「Opus 5.5, Sonnet 5.5, and Haiku 5.5 default to `medium`」，其余支持 effort 的型号为 high。用户设置顶层 `effortLevel` 对「Opus 5.5 and models released after it」不生效。
- Extended thinking：「You can't turn thinking off on Opus 5.5, Sonnet 5.5, Haiku 5.5, or the Fable models」，会话开关、`alwaysThinkingEnabled: false`、`MAX_THINKING_TOKENS=0` 对它们无效。
- Extended context：「Fable 5.1, Fable 5, Sonnet 5 and later, Haiku 5.5, and Opus 4.7 and later run with the 1M window by default」。Haiku 5.5 在 Anthropic API 所有套餐以 1M 运行，请求名 `claude-haiku-5-5`；提示超过 100K tokens 时单价更高。
- 自动回退：Sonnet 5.5 的网络安全类拒答在 Sonnet 5 上重跑，生物类没有回退。
- 协议：API formats 表仍只有 Anthropic Messages（`/v1/messages`，可选 count_tokens）与 Bedrock / Agent Platform 格式；订阅承载登记 `anthropic_messages`。

## 新增型号

| 请求名 | API 发布 / 退役承诺 | 窗口 / 最大输出 | Claude Code effort / 缺省 | 参考价 USD（输入 / 缓存读 / 输出 / 5 分钟写入） |
| --- | --- | --- | --- | --- |
| claude-sonnet-5-5 | 2026-09-28 / 不早于 2027-09-28 | 1M / 128K | low–max / medium | 2 / 0.10 / 10 / 2.50 |
| claude-haiku-5-5 | 2026-10-07 / 不早于 2027-10-07 | 1M / 128K | low–max / medium | 0.10 / 0.01 / 0.50 / 0.125 |

- Sonnet 5.5：价表脚注 2「Cache hits and refreshes on Claude Opus 5.5 and Claude Sonnet 5.5 are priced at 0.05x the base input price」，缓存读 0.10 是官方单列值，不按 0.1x 推算。1 小时写入 4、Batch 五折不展开。API 页 Default effort 为 `high`，与 Claude Code 缺省 medium 不同；两者分属不同入口，订阅条目只登记 Claude Code 的值。API 的 `thinking: {"type": "between_tools"}` 未见 Claude Code 暴露，订阅条目仍记思考不可关闭。
- Haiku 5.5：价表分两行，「for prompts up to 100,000 tokens」0.10 / 0.125 / 0.20 / 0.01 / 0.50，「over 100,000 tokens」0.50 / 0.625 / 1 / 0.05 / 2.50。按每型号一组价格的规则取 ≤100K 档为基准，>100K 档、1 小时写入、Batch 不展开。API 页 Default effort 为 `medium`。新分词器下同样文本约比 Haiku 4.5 多 30% token。
- 两者都是文本与图片输入、文本输出。最大输出按 API 页的 128K 标称，精确整数未确认，`max_output_tokens` 保持 null，与已有条目一致。本仓库 Anthropic API 目录未收录这两个型号，reference_origin 只登记 URL。

## 已有型号复核

| 型号 | Claude Code 清单 | 参考价（输入 / 缓存读 / 输出 / 5 分钟写入） | 结论 |
| --- | --- | --- | --- |
| claude-fable-5-1 | `fable` 别名 | 10 / 0.25 / 50 / 12.5 | 无变化 |
| claude-fable-5 | 按 ID 选择 | 10 / 1 / 50 / 12.5 | 无变化 |
| claude-opus-5-5 | `opus` / `default` | 4 / 0.2 / 20 / 5 | 无变化 |
| claude-opus-5 | 按 ID 选择；生物类回退目标 | 5 / 0.5 / 25 / 6.25 | 无变化 |
| claude-sonnet-5 | 按 ID 选择；Sonnet 5.5 网络安全类回退目标 | 2 / 0.2 / 10 / 2.5 | 价格无变化；Anthropic API 上 `sonnet` 别名已改指 Sonnet 5.5，备注更新 |
| claude-haiku-4-5 | 按 ID 选择；第三方云 `haiku` 别名仍指向它 | 1 / 0.1 / 5 / 1.25 | 价格无变化；Anthropic API 上 `haiku` 别名已改指 Haiku 5.5，备注更新；订阅窗口仍 unknown |

## 未收录与缺项

- 套餐（Pro、Max 5x）本轮未重查。
- API 目录（`anthropic/api-global`）未新增 Sonnet 5.5 / Haiku 5.5。
- 继续 partial / unknown：Claude Code 思考的其他入口与组织策略；Haiku 4.5 的订阅窗口；最大输出精确整数。
