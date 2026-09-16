# cursor — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| individual/`composer-2-5` | `Composer 2.5 Standard on-demand` | USD input_uncached_tokens=0.5/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=2.5/1000000 token | 采用Cursor本平台公布的Standard额外按量费率，不取套餐池折算。 |

## 来源

- `alignment-cursor-pricing`：[官方来源](https://cursor.com/docs/models-and-pricing)；抓取 2026-09-16T05:03:37.367367+00:00；提取正文SHA-256 `c1a946566e0c2d05609b7f98fb9679609198d280790ebb2f87770af5379e2f67`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
