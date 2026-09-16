# anthropic — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| claude-code/`claude-fable-5` | `claude-fable-5` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=1/1000000 token, output_tokens=50/1000000 token | 优先同平台Anthropic API标准价。 |
| claude-code/`claude-opus-5` | `claude-opus-5` | USD input_uncached_tokens=5/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=25/1000000 token, cache_write_5m_tokens=6.25/1000000 token | 优先同平台Anthropic API标准价。 |
| claude-code/`claude-sonnet-5` | `claude-sonnet-5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=10/1000000 token, cache_write_5m_tokens=2.5/1000000 token | 优先同平台Anthropic API标准价。 |
| claude-code/`claude-haiku-4-5` | `claude-haiku-4-5` | USD input_uncached_tokens=1/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=5/1000000 token, cache_write_5m_tokens=1.25/1000000 token | 优先同平台Anthropic API标准价。 |
| claude-code/`claude-haiku-4-5-20251001` | `claude-haiku-4-5` | USD input_uncached_tokens=1/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=5/1000000 token, cache_write_5m_tokens=1.25/1000000 token | 用户明确指定日期版Haiku按claude-haiku-4-5对齐。 |

## 来源

- `alignment-anthropic-pricing`：[官方来源](https://platform.claude.com/docs/en/about-claude/pricing)；抓取 2026-09-16T05:03:39.486090+00:00；提取正文SHA-256 `1a1bdfeffd74c32141a50f47a6a6e04302fa2374c2f50c01409b6832dcba09ba`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
