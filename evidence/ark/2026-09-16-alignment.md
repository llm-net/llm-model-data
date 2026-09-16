# ark — 2026-09-16 价格对齐与清理

更新于2026-09-16T05:39:26.808377Z；按用户本轮明确规则执行。参考对象价格来自下列已读取官方资料。

订阅模型不再采集实际扣费；先同平台按量价，平台缺价才回退开发方。对齐不会证明订阅模型可调用，也不会改变原模型身份核对状态。

## 参考价映射

| 产品 / 模型 | 参考对象 | 单价（金额/百万token，其他单位单列） | 原因 |
| --- | --- | --- | --- |
| api-cn/`doubao-seedance-2.5` | `doubao-seedance-2-5-260628` | CNY video_output_tokens=70/1000000 token | 按用户规则，短名估价对齐同系列最新日期版本；这不声明官方路由别名。 |
| api-cn/`doubao-seedance-2.0` | `doubao-seedance-2-0-260128` | CNY video_output_tokens=46/1000000 token | 按用户规则，短名估价对齐同系列最新日期版本；这不声明官方路由别名。 |
| api-cn/`doubao-seedance-2.0-fast` | `doubao-seedance-2-0-fast-260128` | CNY video_output_tokens=37/1000000 token | 按用户规则，短名估价对齐同系列最新日期版本；这不声明官方路由别名。 |
| agent-plan-cn/`deepseek-v4-pro` | `deepseek-v4-pro-ga-260813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=27/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`deepseek-v4-flash` | `deepseek-v4-flash-ga-260731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.10/1000000 token, output_tokens=9/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`doubao-seedance-2.5` | `doubao-seedance-2-5-260628` | CNY video_output_tokens=70/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`doubao-seedance-2.0` | `doubao-seedance-2-0-260128` | CNY video_output_tokens=46/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`doubao-seedance-2.0-fast` | `doubao-seedance-2-0-fast-260128` | CNY video_output_tokens=37/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`doubao-seedance-2.0-mini` | `doubao-seedance-2-0-mini-260615` | CNY video_output_tokens=23/1000000 token | 优先同平台按量价。 |
| agent-plan-cn/`doubao-seedream-5.0-lite` | `doubao-seedream-5-0-260128` | CNY generated_images=0.22/1 image | 优先同平台按量价。 |
| coding-plan-cn/`doubao-seed-evolving` | `doubao-seed-evolving` | CNY input_uncached_tokens=6/1000000 token, input_cached_tokens=1.2/1000000 token, output_tokens=30/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`doubao-seed-2.1-turbo` | `doubao-seed-2-1-turbo-260628` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.6/1000000 token, output_tokens=15/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`doubao-seed-2.0-lite` | `doubao-seed-2-0-lite-260428` | CNY input_uncached_tokens=0.6/1000000 token, input_cached_tokens=0.12/1000000 token, output_tokens=3.6/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`minimax-m3` | `MiniMax-M3` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token | 已检查方舟完整按量价表，未找到该型号公开价；采用模型开发方minimax按量价。 |
| coding-plan-cn/`glm-5.3` | `glm-5.3` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token | 已检查方舟完整按量价表，未找到该型号公开价；采用模型开发方zhipu按量价。 |
| coding-plan-cn/`glm-5.3-flash` | `glm-5.3-flash` | CNY input_uncached_tokens=0.8/1000000 token, input_cached_tokens=0.23/1000000 token, output_tokens=2.8/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`deepseek-v4-flash` | `deepseek-v4-flash-ga-260731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.10/1000000 token, output_tokens=9/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`deepseek-v4-pro` | `deepseek-v4-pro-ga-260813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=27/1000000 token | 优先同平台按量价。 |
| coding-plan-cn/`kimi-k2.7-code` | `kimi-k2.7-code` | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=27/1000000 token | 已检查方舟完整按量价表，未找到该型号公开价；采用模型开发方moonshot按量价。 |
| coding-plan-cn/`kimi-k3` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token | 已检查方舟完整按量价表，未找到该型号公开价；采用模型开发方moonshot按量价。 |

## 来源

- `alignment-ark-rendered-models`：[官方来源](https://www.volcengine.com/docs/82379/1330310)；抓取 2026-09-16T05:06:50.341Z；提取正文SHA-256 `d69c4daa58864d6c56962f1cbe630406018967646f7ed85ea20e2b0c50d5129d`。
- `alignment-ark-rendered-pricing`：[官方来源](https://www.volcengine.com/docs/82379/1544106)；抓取 2026-09-16T05:06:44.570Z；提取正文SHA-256 `ef23eadd6ecebd904461808a1fdd8dc9ad7793ad8d22d7c344365a83f84ca8d0`。
- `alignment-minimax-pricing`：[官方来源](https://platform.minimaxi.com/docs/guides/pricing-paygo)；抓取 2026-09-16T05:03:42.584149+00:00；提取正文SHA-256 `de745dc4863fe0953b89f567c0201c43b2eae281cb44003f3391dd9b5114310c`。
- `alignment-moonshot-pricing-md`：[官方来源](https://platform.kimi.com/docs/pricing/chat.md)；抓取 2026-09-16T05:04:33.824350+00:00；提取正文SHA-256 `34225b80b0ec0ee85738b8c7ba20a98f7cfe110e478b0e6040c22cff5edd865a`。
- `alignment-zhipu-full-prices`：[官方来源](https://docs.bigmodel.cn/cn/guide/start/pricing.md)；抓取 2026-09-16T05:08:49.486617+00:00；提取正文SHA-256 `f77d7a1ade70a90c186bb0b5218900e8807843beaa77a01afe8a3cec484eb1c6`。

方舟/千帆日期选择依据为此前已核对的官方模型目录；记录的是用户指定估价映射，不声明官方路由等价。
