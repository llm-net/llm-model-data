# minimax — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| token-plan-cn/`MiniMax-M3` | `MiniMax-M3` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token | 优先同平台按量价。 |
| token-plan-cn/`MiniMax-M2.7` | `MiniMax-M2.7` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token | 优先同平台按量价。 |

## 来源

- `alignment-minimax-pricing`：[官方来源](https://platform.minimaxi.com/docs/guides/pricing-paygo)；抓取 2026-09-16T05:03:42.584149+00:00；提取正文SHA-256 `de745dc4863fe0953b89f567c0201c43b2eae281cb44003f3391dd9b5114310c`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
