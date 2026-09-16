# 聚合平台收录与排除

当前保留的 OpenRouter 数据用于初步估算；硅基流动与 Together AI 已由用户整家删除。维持现有平台 → 产品 → 模型结构，每模型一个价格基准。

- `catalog.json` 中的模型就是维护清单，`coverage=partial`。
- 只收录确实需要的模型；常规更新核对清单内全部条目。发现新模型可在报告列建议，不能因抓到了全量API而全量灌入。
- 不设60/40条、系列数、端点数或单批新增数的额外限制；不再维护collection-policy.json。
- OpenRouter取 `/api/v1/models` 中精确ID的 `pricing`。按token报价用Decimal乘一百万，统一保存每百万token价。没有对应ID就未知，不根据名字猜路由目标。
- 只保留一个标准基准；原厂价、端点价、最低可选路由价均不混入第二套价格。
- 公开目录缺项不等于下线。更新前检查 schemas/excluded-providers.json 及 provider.json 的 excluded_request_ids，历史只留 Git 与证据。
- 协议面也按本平台的模型入口逐条核对，不能照抄原厂，见 [PROTOCOLS.md](PROTOCOLS.md)。

新增、删除和改价随同一份候选报告人工确认，不另设复杂审批流程。未知值不能用0替代。模型级估价与实际路由账单可能不同。

## 固定排除（用户明确指定）

| 平台 | 不再收录的请求ID |
| --- | --- |
| OpenRouter | `~openai/gpt-latest` |
| Groq | `llama-3.3-70b-versatile` |

这些是用户收录决定，不都表示厂商下线。自动更新即使再发现价格或模型名也不能重新加入；用户明确变更决定后才能改排除清单。

## 整家排除

`siliconflow`（硅基流动）与 `together`（Together AI）于 2026-09-16 由用户明确删除，包含全部产品和模型。机器清单在 [schemas/excluded-providers.json](../schemas/excluded-providers.json)，validate 拒绝重新导入。保留的 evidence / imports 是历史，不是恢复依据；只有用户明确变更决定才能恢复。
