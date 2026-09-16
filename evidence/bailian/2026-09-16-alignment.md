# bailian — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| coding-plan-cn/`qwen3.7-plus` | `qwen3.7-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=8/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`qwen3.6-plus` | `qwen3.6-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=12/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`kimi-k2.5` | `kimi-k2.5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=21/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`glm-5` | `glm-5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=18/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`MiniMax-M2.5` | `MiniMax-M2.5` | CNY input_uncached_tokens=2.1/1000000 token, output_tokens=8.4/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`qwen3.5-plus` | `qwen3.5-plus` | CNY input_uncached_tokens=0.8/1000000 token, output_tokens=4.8/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`qwen3-max-2026-01-23` | `qwen3-max-2026-01-23` | CNY input_uncached_tokens=2.5/1000000 token, output_tokens=10/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`qwen3-coder-next` | `qwen3-coder-next` | CNY input_uncached_tokens=1/1000000 token, output_tokens=4/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`qwen3-coder-plus` | `qwen3-coder-plus` | CNY input_uncached_tokens=4/1000000 token, output_tokens=16/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| coding-plan-cn/`glm-4.7` | `glm-4.7` | CNY input_uncached_tokens=3/1000000 token, output_tokens=14/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`qwen3.8-max` | `qwen3.8-max` | CNY input_uncached_tokens=12/1000000 token, output_tokens=36/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`qwen3.8-flash` | `qwen3.8-flash` | CNY input_uncached_tokens=0.8/1000000 token, output_tokens=2.7/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`qwen3.7-plus` | `qwen3.7-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=8/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`deepseek-v4-pro` | `deepseek-v4-pro` | CNY input_uncached_tokens=12/1000000 token, output_tokens=24/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`deepseek-v4-flash` | `deepseek-v4-flash` | CNY input_uncached_tokens=1/1000000 token, output_tokens=2/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`kimi-k2.7-code` | `kimi-k2.7-code` | CNY input_uncached_tokens=6.5/1000000 token, output_tokens=27/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`kimi-k2.6` | `kimi-k2.6` | CNY input_uncached_tokens=6.5/1000000 token, output_tokens=27/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`glm-5.2` | `glm-5.2` | CNY input_uncached_tokens=8/1000000 token, output_tokens=28/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`glm-5.1` | `glm-5.1` | CNY input_uncached_tokens=6/1000000 token, output_tokens=24/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |
| token-plan-cn/`glm-5` | `glm-5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=18/1000000 token | 优先同平台百炼北京按量价；目录部分收录不意味着该平台无价。 |

## 来源

- `alignment-bailian-pricing`：[官方来源](https://help.aliyun.com/zh/model-studio/model-pricing)；抓取 2026-09-16T05:03:41.055245+00:00；提取正文SHA-256 `b41943ec0bdefedeb7fb43e936b2387ab96f8587a3ee1d73ab9adaa23a0bba98`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
