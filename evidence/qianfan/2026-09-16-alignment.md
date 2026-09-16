# qianfan — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| api-cn/`deepseek-v4-pro` | `deepseek-v4-pro-0813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.3/1000000 token, output_tokens=27/1000000 token | 按用户规则，对齐当前官方目录中同系列最新日期版本。 |
| api-cn/`deepseek-v4-flash` | `deepseek-v4-flash-0731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=9/1000000 token | 按用户规则，对齐当前官方目录中同系列最新日期版本。 |

## 来源

- `alignment-qianfan-current-prices`：[官方来源](https://cloud.baidu.com/doc/qianfan/s/wmh4sv6ya)；抓取 2026-09-16T05:13:57.720753+00:00；提取正文SHA-256 `14c8a02a3f9e32591a02bed6df3ad719551971e461049b1765e50c659db9cb73`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
