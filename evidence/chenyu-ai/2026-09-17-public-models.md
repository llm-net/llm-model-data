# 晨羽AI 公开模型、价格与能力核对（2026-09-17）

核对基线：`45e47b537766404df24e1ba7868e73efff4aed6e`。

模型 API 获取时间（UTC）：`2026-09-17T02:22:31.938451Z`，HTTP 200。页面均经公网 HTTPS 匿名获取；未读取账号、渠道、内部配置或账本，未进行付费推理。

## 来源与保存范围

- `public-models` / `public-pricing`：https://chenyu.pro/api/v1/public/models，响应原文保存为 [公开响应](2026-09-17-public-models.json)，SHA-256 `c3b7f829cfcaa36ece0b88bcd634de44523172803b41031c9a0a83172c68c6eb`。
- 响应含 30 个模型，币种 CNY、价格簿 `22`、`effectiveAt=2026-09-16T17:39:52Z`。effectiveAt 作为价簿元数据保留，不冒充各型号首次生效时间；规则的 effective_from / effective_until 仍为 null。
- 只保存本次必要的公开模型响应与核对结论；不保存整站 HTML、设备目录的其他平台或消费者配置。

| source ID | 官方 URL / 位置 | UTC 获取时间 | 页面 SHA-256 |
| --- | --- | --- | --- |
| catalog / pricing / protocol-models / context-chenyu-models | https://chenyu.pro/api-docs/docs/models/ | 2026-09-17T02:20:53.588990+00:00 | `ddd9dd474f8768b5a04652577b513bcfbbdd78aab73d88784ce15c6cf6e13d94` |
| billing | https://chenyu.pro/api-docs/docs/billing/ | 2026-09-17T02:20:53.566696+00:00 | `c2db92643540c8ac63313dd246beb98a6e6a5152b3a7a9c02547030753aabf6a` |
| protocol-quickstart | https://chenyu.pro/api-docs/docs/quickstart/ | 2026-09-17T02:20:53.626723+00:00 | `91f13bef23433b4adc6cf0e2db4a5e4c84c71e30668eee154f79d9e41e54f7dd` |
| protocol-responses | https://chenyu.pro/api-docs/docs/openai-responses/ | 2026-09-17T02:20:53.646106+00:00 | `971f692bfef6251c588578b8b465b85c5a40778dab43a2d091b13ed8ee614677` |
| protocol-messages | https://chenyu.pro/api-docs/docs/anthropic-messages/ | 2026-09-17T02:20:53.839379+00:00 | `cb3d4025033396ce7b2a67a92a2afbafc4aa10465e8a8e4638e5d6ae1782d4ef` |
| protocol-images | https://chenyu.pro/api-docs/docs/images/ | 2026-09-17T02:20:53.851673+00:00 | `f3167b5dbb6e7d10ba4af7ebb05a01600f176613cd50fa580fe230746aad875c` |
| protocol-videos | https://chenyu.pro/api-docs/docs/videos/ | 2026-09-17T02:20:53.926839+00:00 | `00f08192eef573c96903d2146c686611724c009a23dbc9e1634d38bbfc523fdd` |
| protocol-speech | https://chenyu.pro/api-docs/docs/speech/ | 2026-09-17T02:20:53.974891+00:00 | `82097f280dea45bd1fac434fdbf00269589f13d5e8d2e4bbdea3a267dba6a48a` |
| protocol-catalog / context-chenyu-catalog | https://chenyu.pro/catalog/platform-models.json | 2026-09-17T02:20:54.086113+00:00 | `d6da4ccfa75749ea5cb348e097294fc09a4032ff9b68dceea7e59bf1066a8fa0` |

## 结论与冲突处理

- 原有 29 项都仍在公开清单中，身份与价格从 needs_review / unknown 更新为已核对；无删除。仅新增明确发布的 `deepseek-flash`（DeepSeek-V4.1-Flash），不改既有请求 ID，不猜 alias_of。
- 30 项协议面都有逐型号实时矩阵。DeepSeek 4 项现列 Chat / Responses / Messages；5 项 Doubao Seed 只列 Responses / Messages，不能照原厂加 Chat；GLM 2 项只列 Chat / Messages。两款 Seedream 新增 Ark Image，与 OpenAI Image 并列。
- Responses 静态页「哪些模型在这一面上」仍举 DeepSeek 没有 Responses 的例子，与当前实时矩阵冲突。本轮以实时逐型号清单为准并保留冲突，不声称已经用 Key 验通。图片页现在将厂商面的可用性明确交给实时目录，不再沿用昨日的单面结论。
- 公开 `/catalog/platform-models.json` 本轮为 v26，`chenyu_ai.models=[]`。这是另一份发布目录，不能据其空列表宣布 30 个实时在列模型下线；不用它替代模型页公开接口。
- 20 个文本型号的 contextLength 都是明确整数 token，不作 K/M 换算。其余 10 个结合图片生成、异步视频或 T2A 专文判为无适用文本对话窗口；API 的 0 保存为 null。两个自部署型号的 maxOutput=0 保留未知。
- 当前响应没有 reasoning 数据。Messages 页「这是一条直通面」只说 thinking 原样透传；Responses 页只说 reasoning item 由上游决定。两者都不是本产品逐型号开关、档位、预算或默认行为的证明。30 项均继续 unknown / needs_review，checked_at=null；本次查询时间由本记录给出。
- 模型页与 billing 页宣称以当前生效价簿结算。当前 DeepSeek 每个计价行都是 conditions={}，没有 timeBand、timeClass 或峰谷数字；本次保留统一价，不从原厂或另一条未发布的 DeepSeek 改动复制空闲价。billing 的分时段介绍只能证明结算机制，不能证明本价簿已经配齐档位。

## 金额与计量

- 精确换算：`amount = Decimal(unitPriceNanos) × per / Decimal(unitSize) / 1000000000`。文本 / 视频 token 统一展示每百万 token；语音为每万计费字符；图片为每张，视频时长为每秒。不使用二进制浮点，不换汇。
- Seedream Pro：成功图片 0.3 元/张，输入图片 0.02 元/张，每笔前 1 张免费；Lite 成功图片 0.22 元/张，未列输入价不等于输入免费。MiniMax H3 输入 / 输出视频各 0.5 元/秒，输入图片 0.2 元/张，每笔前 5 张免费。
- billing「每笔请求如何计费」：缓存、未缓存输入和输出分量分别计量，推理 token 不重复相加；视频小数秒不作数量进位；所有计费项的费用各自向上取整到纳元。这与 quantity.rounding 区别记录。
- 成功图片数量来自实际输出（images 页给出 usage.generated_images）；输入图片数量的逐型号字段未公开，只记录有证据的免费张数。视频 token 的确切字段与 MiniMax 视频时长字段未逐项公开，保留未知；百炼输出时长在 videos 页列为 usage.output_video_duration。
- 语音页「计费」明确同步读取 extra_info.usage_characters，异步读取受理应答 usage_characters；不能与 word_count 混用。同步成功结算、异步受理即结算，同价但事件不同，因此 rule.charge_on=unknown 并注明差异，不能以一个 success 覆盖异步。
- billing 的终态规则优先于视频页旧概述：明确失败 / 取消不收成功生成费；未知或查询过期不证明失败，不自动归零。任务需通过平台查询终态；不将回调本身当已结算。
- 本轮没有套餐、额度或税费变更；含税与否、逐型号首次生效时间、未列费率分量及精确计量字段缺项均不补猜。

## 每个已有及新增模型的结果

下表价格均为 CNY。旧 29 项用量价全部为 unknown，本轮右列为当前价；新增项原先不存在。每行思考能力均 unknown，逐项列出以供审阅。

| 请求 ID | 变更 | 当前价格（meter=amount/per unit） | 协议面 | 上下文 token / 最大输出 | 思考 |
| --- | --- | --- | --- | --- | --- |
| `deepseek-flash` | 新增 | input_uncached_tokens=2/1000000 token; input_cached_tokens=0.04/1000000 token; output_tokens=8/1000000 token | openai_chat, openai_responses, anthropic_messages | 1048576 / 393216 | unknown |
| `deepseek-v4-pro` | unknown → published | input_uncached_tokens=9/1000000 token; input_cached_tokens=0.3/1000000 token; output_tokens=27/1000000 token | openai_chat, openai_responses, anthropic_messages | 1048576 / 393216 | unknown |
| `deepseek-v4-flash` | unknown → published | input_uncached_tokens=2/1000000 token; input_cached_tokens=0.04/1000000 token; output_tokens=8/1000000 token | openai_chat, openai_responses, anthropic_messages | 1048576 / 393216 | unknown |
| `deepseek-v4-flash-vision-exp` | unknown → published | input_uncached_tokens=2/1000000 token; input_cached_tokens=0.04/1000000 token; output_tokens=8/1000000 token | openai_chat, openai_responses, anthropic_messages | 1048576 / 393216 | unknown |
| `doubao-seed-2-1-pro-260628` | unknown → published | input_uncached_tokens=6/1000000 token; input_cached_tokens=1.2/1000000 token; output_tokens=30/1000000 token | openai_responses, anthropic_messages | 262144 / 262144 | unknown |
| `doubao-seed-2-1-turbo-260628` | unknown → published | input_uncached_tokens=3/1000000 token; input_cached_tokens=0.6/1000000 token; output_tokens=15/1000000 token | openai_responses, anthropic_messages | 262144 / 262144 | unknown |
| `doubao-seed-2-0-lite-260428` | unknown → published | input_uncached_tokens=0.6/1000000 token; input_cached_tokens=0.12/1000000 token; output_tokens=3.6/1000000 token | openai_responses, anthropic_messages | 262144 / 131072 | unknown |
| `doubao-seed-2-0-mini-260428` | unknown → published | input_uncached_tokens=0.2/1000000 token; input_cached_tokens=0.04/1000000 token; output_tokens=2/1000000 token | openai_responses, anthropic_messages | 262144 / 131072 | unknown |
| `doubao-seed-2-0-pro-260215` | unknown → published | input_uncached_tokens=3.2/1000000 token; input_cached_tokens=0.64/1000000 token; output_tokens=16/1000000 token | openai_responses, anthropic_messages | 262144 / 131072 | unknown |
| `doubao-seedream-5-0-pro-260628` | unknown → published | generated_images=0.3/1 image; input_images=0.02/1 image（免费 1 张） | openai_image, ark_image | not_applicable / — | unknown |
| `doubao-seedream-5-0-260128` | unknown → published | generated_images=0.22/1 image | openai_image, ark_image | not_applicable / — | unknown |
| `doubao-seedance-2-5-260628` | unknown → published | video_output_tokens=70/1000000 token | ark_video | not_applicable / — | unknown |
| `doubao-seedance-2-0-260128` | unknown → published | video_output_tokens=46/1000000 token | ark_video | not_applicable / — | unknown |
| `doubao-seedance-2-0-mini-260615` | unknown → published | video_output_tokens=23/1000000 token | ark_video | not_applicable / — | unknown |
| `qwen3.8-max` | unknown → published | input_uncached_tokens=12/1000000 token; output_tokens=36/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 131072 | unknown |
| `qwen3.7-plus` | unknown → published | input_uncached_tokens=2/1000000 token; output_tokens=8/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 131072 | unknown |
| `qwen3.8-flash` | unknown → published | input_uncached_tokens=0.8/1000000 token; output_tokens=2.7/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 131072 | unknown |
| `qwen3.7-flash` | unknown → published | input_uncached_tokens=0.2/1000000 token; output_tokens=0.8/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 131072 | unknown |
| `qwen3.8-27b` | unknown → published | input_uncached_tokens=3/1000000 token; output_tokens=12/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 131072 | unknown |
| `wan3.0-video` | unknown → published | video_input_seconds=0.3/1 second; video_output_seconds=0.3/1 second | bailian_video | not_applicable / — | unknown |
| `wan3.0-video-prime` | unknown → published | video_input_seconds=0.45/1 second; video_output_seconds=0.45/1 second | bailian_video | not_applicable / — | unknown |
| `MiniMax-M3` | unknown → published | input_uncached_tokens=2.1/1000000 token; input_cached_tokens=0.42/1000000 token; output_tokens=8.4/1000000 token | openai_chat, openai_responses, anthropic_messages | 1000000 / 524288 | unknown |
| `MiniMax-H3` | unknown → published | input_images=0.2/1 image（免费 5 张）; video_input_seconds=0.5/1 second; video_output_seconds=0.5/1 second | minimax_video | not_applicable / — | unknown |
| `speech-2.8-hd` | unknown → published | billable_characters=3.5/10000 character | minimax_speech | not_applicable / — | unknown |
| `speech-2.8-turbo` | unknown → published | billable_characters=2/10000 character | minimax_speech | not_applicable / — | unknown |
| `glm-5.3` | unknown → published | input_uncached_tokens=8/1000000 token; input_cached_tokens=2/1000000 token; output_tokens=28/1000000 token | openai_chat, anthropic_messages | 1048576 / 131072 | unknown |
| `glm-5.3-flash` | unknown → published | input_uncached_tokens=0.8/1000000 token; input_cached_tokens=0.23/1000000 token; output_tokens=2.8/1000000 token | openai_chat, anthropic_messages | 1048576 / 131072 | unknown |
| `kimi-k3` | unknown → published | input_uncached_tokens=20/1000000 token; input_cached_tokens=2/1000000 token; output_tokens=100/1000000 token | openai_chat, openai_responses, anthropic_messages | 1048576 / 1048576 | unknown |
| `Qwen/Qwen3.8-27B-FP8` | unknown → published | input_uncached_tokens=3/1000000 token; input_cached_tokens=0.6/1000000 token; output_tokens=12/1000000 token | openai_chat, openai_responses, anthropic_messages | 262144 / 未知 | unknown |
| `nvidia/Qwen3.6-35B-A3B-NVFP4` | unknown → published | input_uncached_tokens=1.8/1000000 token; output_tokens=10.8/1000000 token | openai_chat, openai_responses, anthropic_messages | 262144 / 未知 | unknown |

## 候选边界与检查

- `scripts/catalog.py validate` 通过；`python -m unittest discover -s tests -v` 的 70 个测试全部通过。另用 Fraction 独立反算 69 条费率，与公开接口的纳元金额和单位全部一致；30 个请求 ID、协议面、窗口 / 输出上限和两处免费张数逐项对上。
- 更新前已有的 9 个修改 / 未跟踪文件按 SHA-256 检查均逐字节未变；29 个既有模型的本地主键、请求 ID、别名关系及无新增证据的其他能力字段保留原值。
- 本批只更新晨羽AI资料、来源与当前价格对齐摘要；工作树原有 DeepSeek 分时价格及 schema / 脚本改动按原样保留。全仓 review 会包含这些既有改动，不能把它们误认为本次新增。
- 当前仅为本地候选；未提交、未推送、未打正式 tag、未更新消费者。完整差异、全仓 partial / unknown 和内容哈希见 `.review/REVIEW.md`、`.review/diff.patch`、`.review/manifest.json`。
