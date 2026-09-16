# openai — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| codex/`gpt-6-astra` | `gpt-6-astra` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=1/1000000 token, output_tokens=50/1000000 token | 优先同平台按量价。 |
| codex/`gpt-5.6-sol` | `gpt-5.6-sol` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.4/1000000 token, output_tokens=20/1000000 token | 优先同平台按量价。 |
| codex/`gpt-5.6-terra` | `gpt-5.6-terra` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=12/1000000 token | 优先同平台按量价。 |
| codex/`gpt-5.6-luna` | `gpt-5.6-luna` | USD input_uncached_tokens=0.2/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=1.2/1000000 token | 优先同平台按量价。 |

## 来源

- `alignment-openai-codex-rate`：[官方来源](https://developers.openai.com/api/docs/models/compare)；抓取 2026-09-16T05:05:56.167953+00:00；提取正文SHA-256 `63cc2d7ea7b19beda5004d0f614d812a1170e3450d5a50adb3a1f70f930983fc`。
- `alignment-openai-luna-api`：[官方来源](https://developers.openai.com/api/docs/models/gpt-5.6-luna.md)；抓取 2026-09-16T05:36:38.440582+00:00；提取正文SHA-256 `1f425d8f2a93f8418702ac7acbb62b26850b98fe20680f82205bed5fce38fed0`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
