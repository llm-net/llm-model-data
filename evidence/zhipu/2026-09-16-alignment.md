# zhipu — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| coding-plan-cn/`glm-5.3` | `glm-5.3` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`glm-5.3-flash` | `glm-5.3-flash` | CNY input_uncached_tokens=0.8/1000000 token, input_cached_tokens=0.23/1000000 token, output_tokens=2.8/1000000 token | 优先同平台按量价。 |

## 来源

- `alignment-zhipu-full-prices`：[官方来源](https://docs.bigmodel.cn/cn/guide/start/pricing.md)；抓取 2026-09-16T05:08:49.486617+00:00；提取正文SHA-256 `f77d7a1ade70a90c186bb0b5218900e8807843beaa77a01afe8a3cec484eb1c6`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
