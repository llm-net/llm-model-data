# Claude Code 原厂参考价专项核对

范围仅为 Claude Code 已有 9 个型号；UTC 核对时间 2026-11-11T12:42:14Z。读取官方 [API 价格页](https://platform.claude.com/docs/en/about-claude/pricing) 的 Model pricing 表及 [Claude Code 型号配置](https://code.claude.com/docs/en/model-config) 的 Available models、Work with Fable。来源已分别登记为 `current-code-pricing` 与 `current-code-models`。

全部现有参考价与原厂公开标准 API 价一致，无需修改数字或刷新目录的旧核对日期。统一 USD/百万 token；缓存写入选择 5 分钟 TTL，不把 1 小时缓存、Batch、Fast 或地区溢价并入基准。

| 型号 | 未缓存输入 | 缓存读取 | 输出 | 5 分钟缓存写入 |
| --- | ---: | ---: | ---: | ---: |
| `claude-fable-5-1` | 10 | 0.25 | 50 | 12.5 |
| `claude-fable-5` | 10 | 1 | 50 | 12.5 |
| `claude-opus-5-5` | 4 | 0.2 | 20 | 5 |
| `claude-opus-5` | 5 | 0.5 | 25 | 6.25 |
| `claude-sonnet-5` | 2 | 0.2 | 10 | 2.5 |
| `claude-haiku-4-5` | 1 | 0.1 | 5 | 1.25 |
| `claude-sonnet-5-5` | 2 | 0.1 | 10 | 2.5 |
| `claude-haiku-5-5` | 0.1 | 0.01 | 0.5 | 0.125 |
| `claude-fable-5-2` | 8 | 0.2 | 40 | 10 |

Haiku 5.5 选提示不超过 100,000 token 档；超过后属于另档，现有说明已覆盖。Fable 5.1/5.2 的缓存读取是官网独立数字，不能按通常输入倍率替代。

Claude Code 文档明确当前 Opus/Sonnet/Haiku 别名分别对应 5.5，Fable 5.2 可显式选择，5.1 和 5 仍有独立 ID 说明；本次核对未发现需要新增且已证实的当前订阅型号。公开 API 价格表中的其他型号不自动追加到订阅。未修改 API 产品、订阅真实扣费、模型能力或发布状态。
