# moonshot — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| kimi-code/`k3` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token | 按已确认底模映射到同平台API；k3-256k仅上下文差别，统一采用K3按量价。 |
| kimi-code/`k3-256k` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token | 按已确认底模映射到同平台API；k3-256k仅上下文差别，统一采用K3按量价。 |
| kimi-code/`kimi-for-coding` | `kimi-k2.7-code` | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=27/1000000 token | 用户指定近似示意，底模仍为K2.8 Preview。 |
| kimi-code/`kimi-for-coding-highspeed` | `kimi-k2.7-code-highspeed` | CNY input_uncached_tokens=13/1000000 token, input_cached_tokens=2.6/1000000 token, output_tokens=54/1000000 token | 按已确认底模映射到同平台API；k3-256k仅上下文差别，统一采用K3按量价。 |

用户后续明确回复：“指定按 Kimi K2.7 Code 价格做示意”。因此kimi-for-coding保留K2.8 Preview身份，参考kimi-k2.7-code按量价。此次只确定参考映射，沿用下列已核对价格证据，不声称K2.8官方报价已发布。

## 来源

- `alignment-moonshot-pricing-policy`：[官方来源](https://platform.kimi.com/docs/pricing/chat.md)；抓取 2026-09-16T05:36:38.441446+00:00；提取正文SHA-256 `34225b80b0ec0ee85738b8c7ba20a98f7cfe110e478b0e6040c22cff5edd865a`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
