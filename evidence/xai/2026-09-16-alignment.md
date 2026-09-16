# xai — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| grok-build/`grok-4.6` | `grok-4.6` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token | 优先同平台按量价。 |
| grok-build/`grok-4.5` | `grok-4.5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=6/1000000 token | 优先同平台按量价。 |

## 来源

- `alignment-xai-grok45`：[官方来源](https://docs.x.ai/developers/models/grok-4.5)；抓取 2026-09-16T05:05:55.704809+00:00；提取正文SHA-256 `3ae3001022ce66ee69ed8d06c11070e9b0501d01c46127b2790609adc126dfab`。
- `alignment-xai-grok46`：[官方来源](https://docs.x.ai/developers/models/grok-4.6)；抓取 2026-09-16T05:05:55.630800+00:00；提取正文SHA-256 `662b46bbfc1b535f2b2c89f51911d8eec62a030965fd625ce7d780ed73fcfec0`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
