# OpenRouter / SiliconFlow 简化收录

这两个平台的数据用于初步估算。维持现有平台 → 产品 → 模型结构，每模型一个价格基准。

- `catalog.json` 中的模型就是维护清单，`coverage=partial`。
- 只收录确实需要的模型；常规更新核对清单内全部条目。发现新模型可在报告列建议，不能因抓到了全量API而全量灌入。
- 不设60/40条、系列数、端点数或单批新增数的额外限制；不再维护collection-policy.json。
- OpenRouter取 `/api/v1/models` 中精确ID的 `pricing`。按token报价用Decimal乘一百万，统一保存每百万token价。没有对应ID就未知，不根据名字猜路由目标。
- SiliconFlow按精确请求ID核对本平台价格页，并查看服务调整公告。Pro前缀、国内外站不是可以隐式合并的身份。
- 只保留一个标准基准；原厂价、端点价、最低可选路由价均不混入第二套价格。
- 公开目录缺项不等于下线。SiliconFlow一经确认下线就删除当前条目，并加入excluded_request_ids防止旧资料重新导入；历史只留Git与证据。

新增、删除和改价随同一份候选报告人工确认，不另设复杂审批流程。未知值不能用0替代。模型级估价与实际路由账单可能不同。

## 固定排除（用户明确指定）

| 平台 | 不再收录的请求ID |
| --- | --- |
| OpenRouter | `~openai/gpt-latest` |
| Together | `openai/gpt-oss-20b` |
| Groq | `llama-3.3-70b-versatile` |
| SiliconFlow | `Qwen/Qwen3.5-397B-A17B`、`MiniMaxAI/MiniMax-M2.5`、`Pro/zai-org/GLM-4.7`，以及今后确认已下线的其他型号 |

这些是用户收录决定，不都表示厂商下线。自动更新即使再发现价格或模型名也不能重新加入；用户明确变更决定后才能改排除清单。
