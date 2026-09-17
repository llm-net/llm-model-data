# 晨羽AI 思考能力补充核对（2026-09-17）

核对时间（UTC）：`2026-09-17T03:00:52.551850Z`。更新前 Git 基线：`45e47b537766404df24e1ba7868e73efff4aed6e`；前一批晨羽AI更新仍在工作树，本次以其 30 个模型为直接比较对象。

仅使用晨羽AI公开 HTTPS 模型页和匿名接口，没有 Key 推理或实际扣费测试。旧的同日模型 / 价格证据保留原文，本文件记录随后新增的思考声明。

## 来源与位置

- `public-reasoning`：https://chenyu.pro/api/v1/public/models，读取 `data.models[].modelId / reasoning`，HTTP 200。完整公开响应见 [机读快照](2026-09-17-reasoning-public-models.json)，SHA-256 `5c6e8476ec8245aa02cca2d44903166c30c67aeb55b52de4923ed99cc22705f9`。
- `reasoning-models`：模型页正文新增思考能力说明，明确逐协议面列出开关、默认行为、强度原始值与 token 预算，并将缺资料项标为未确认。页面本身仍在浏览器读取上述接口，不能仅以 HTML 的加载占位判无资料。

| source ID | URL | UTC 获取时间 | SHA-256 |
| --- | --- | --- | --- |
| reasoning-models | https://chenyu.pro/api-docs/docs/models/ | 2026-09-17T03:00:52.467823Z | `7d1629b69524d669171dcd014891ba209c5b264cb193ae9fb43d64155b2ffc69` |
| protocol-messages | https://chenyu.pro/api-docs/docs/anthropic-messages/ | 2026-09-17T03:00:52.578302Z | `afce56b4fa77de430783e2f910530485abf5ee824c9626e910199754acc2c1bb` |
| protocol-responses | https://chenyu.pro/api-docs/docs/openai-responses/ | 2026-09-17T03:00:52.518902Z | `47cae2e2316855cb6c88e3c5a19e13fdb265bf4aa607c2768e02e0b34db8fe78` |
| billing | https://chenyu.pro/api-docs/docs/billing/ | 2026-09-17T03:00:52.715287Z | `dc1f50d4487603bae630aec92d2162d4eb2171a33116956cb1dbf1a70d331175` |
| protocol-images | https://chenyu.pro/api-docs/docs/images/ | 2026-09-17T03:00:52.861534Z | `2758f625acb833dd31251a4af58f68b0e90e801e740f7b21b47e71dde57296f6` |
| protocol-videos | https://chenyu.pro/api-docs/docs/videos/ | 2026-09-17T03:00:53.291392Z | `ff9c613a7c8b3cf34a474da474d89122192deb88b71013b84ef3c024ec73079b` |
| protocol-speech | https://chenyu.pro/api-docs/docs/speech/ | 2026-09-17T03:00:52.878539Z | `e29b8111b6a90e507feb741855745ea39650496d5dec51c5993ccbbaa630a097` |

## 更新范围与依据

- 思考支持由全部 unknown 变为 10 项 supported：DeepSeek V4 Pro 为 complete；2 项 GLM、Kimi K3、MiniMax M3、5 项 Qwen 为 partial；其余 20 项仍 unknown。无模型增删，没有 unsupported 结论。
- 每条已确认参数来自晨羽AI接口中该精确 modelId 的 reasoning，并与该行 protocols 对照。原始响应附带的是供应商资料的旧 verification；这里重新登记晨羽AI来源、查询时间与本地证据，不能复制原厂 source_ids、核对日期或 evidence 路径来验证晨羽AI。原始元数据只在快照中保留供追溯。
- 公开模型页已把这些字段作为本平台逐型号说明。本次记录的是晨羽AI公开声明，不是从本仓库同名原厂条目自行推导，也不表示真实 Key 参数实调通过。
- DeepSeek V4 Pro 的 Chat / Messages 默认思考开启，effort 默认 high；Chat 原始兼容值 minimal→low、medium/xhigh→high、ultra→max。Messages 接受同一组原始 effort 值，说明为兼容别名。Responses 只列 none/low/high/max，不扩展其他面的别名。
- GLM 5.3 / Flash 的 Chat 默认开启且不可关闭，effort=low/high/max、默认 max；原响应备注夹带其他产品与 GLM 5.2 的说明，本条限定到当前型号，不登记订阅映射。Messages 参数未公布。
- Kimi K3 的 Chat 默认开启且不可关闭，effort=low/high/max、默认 max。原备注提及其他 K2.x 型号，此处不继承；Responses / Messages 控制未公布。
- MiniMax M3 的三个协议面默认不同：Chat 是 adaptive；Messages 是 disabled；Responses 是 none。Responses 的 minimal/low/medium/high 都只是开启自适应思考，保留 kind=mode，不能当作四档深度。公开 coverage 仍为 partial，本次保持该声明。
- 五个 Qwen 型号只登记 Chat 的 enable_thinking 与 thinking_budget。前者为布尔值、默认 true；后者已知参数名，但 minimum / maximum / default 都是 null。未知预算不表示无限制，不能用其他型号或 maxOutput 补数。
- 新 deepseek-flash、两条旧 Flash / 实验 ID、5 项 Doubao Seed、两项自部署 Qwen 与 10 项多模态模型没有已确认思考控制。API 显式 unknown 或未返回 reasoning 都保持 needs_review / checked_at=null；不能按模型模态直接写不支持。

## 同时复核模型、价格、协议与上下文

- 本次响应去掉 reasoning 后与前一份公开响应逐字段一致：30 个模型、69 条费率、CNY、价格簿 v22、effectiveAt=2026-09-16T17:39:52Z；模型 ID、展示名、模态、协议面、contextLength、maxOutput、金额、单位和免费张数条件都未变化。
- 本次是思考专项补充，价格、型号及上下文 / 协议的已有独立 verification 保持原文和日期；新证据记录复核结果，不用思考资料的旧日期刷新其他字段。
- Responses 静态页仍有 DeepSeek 无 Responses 端点的旧例子；实时逐型号 protocols 和本轮 DeepSeek V4 Pro reasoning 均明确列 Responses，沿用实时矩阵并保留该冲突。
- 20 个文本上下文维持已确认整数；10 个生成 / 合成接口仍无适用对话窗口。两款自部署型号的最大输出依然未确认。

## 逐型号结论（含全部 partial / unknown）

| 请求 ID | 原状态 → 当前状态 | 已公开控制与默认值 | 缺项 / 说明 |
| --- | --- | --- | --- |
| `deepseek-flash` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `deepseek-v4-pro` | unknown → supported / complete | openai_chat: 可关, 默认 enabled; thinking.type="enabled"/"disabled"（default="enabled"）; reasoning_effort="minimal"/"low"/"medium"/"high"/"xhigh"/"max"/"ultra"（default="high"）<br>openai_responses: 可关, 默认 enabled; reasoning.effort="none"/"low"/"high"/"max"（default="high"）<br>anthropic_messages: 可关, 默认 enabled; thinking.type="enabled"/"disabled"（default="enabled"）; output_config.effort="minimal"/"low"/"medium"/"high"/"xhigh"/"max"/"ultra"（default="high"） | 晨羽AI逐型号公开三面思考控制，均默认开启且可关闭。Chat / Messages 的兼容值映射需按各控制说明解释，不视作七个独立深度；Responses 只登记 none/low/high/max。其他 DeepSeek 请求 ID 不继承本条。 |
| `deepseek-v4-flash` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `deepseek-v4-flash-vision-exp` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seed-2-1-pro-260628` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seed-2-1-turbo-260628` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seed-2-0-lite-260428` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seed-2-0-mini-260428` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seed-2-0-pro-260215` | unknown → unknown / unknown | — | 公开接口明确返回 support=unknown、coverage=unknown、profiles=[]，未提供此型号的思考参数或默认行为。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seedream-5-0-pro-260628` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seedream-5-0-260128` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seedance-2-5-260628` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seedance-2-0-260128` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `doubao-seedance-2-0-mini-260615` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `qwen3.8-max` | unknown → supported / partial | openai_chat: 可关, 默认 enabled; enable_thinking=true/false（default=true）; thinking_budget=上下界未确认（default=null） | 晨羽AI公开本型号 Chat 面 enable_thinking=true/false，默认 true；支持 thinking_budget，但数值上下界和默认预算未公布。已登记的 Responses / Messages 面控制仍未知，coverage 保持 partial；不能用最大输出或其他型号预算代填。 |
| `qwen3.7-plus` | unknown → supported / partial | openai_chat: 可关, 默认 enabled; enable_thinking=true/false（default=true）; thinking_budget=上下界未确认（default=null） | 晨羽AI公开本型号 Chat 面 enable_thinking=true/false，默认 true；支持 thinking_budget，但数值上下界和默认预算未公布。已登记的 Responses / Messages 面控制仍未知，coverage 保持 partial；不能用最大输出或其他型号预算代填。 |
| `qwen3.8-flash` | unknown → supported / partial | openai_chat: 可关, 默认 enabled; enable_thinking=true/false（default=true）; thinking_budget=上下界未确认（default=null） | 晨羽AI公开本型号 Chat 面 enable_thinking=true/false，默认 true；支持 thinking_budget，但数值上下界和默认预算未公布。已登记的 Responses / Messages 面控制仍未知，coverage 保持 partial；不能用最大输出或其他型号预算代填。 |
| `qwen3.7-flash` | unknown → supported / partial | openai_chat: 可关, 默认 enabled; enable_thinking=true/false（default=true）; thinking_budget=上下界未确认（default=null） | 晨羽AI公开本型号 Chat 面 enable_thinking=true/false，默认 true；支持 thinking_budget，但数值上下界和默认预算未公布。已登记的 Responses / Messages 面控制仍未知，coverage 保持 partial；不能用最大输出或其他型号预算代填。 |
| `qwen3.8-27b` | unknown → supported / partial | openai_chat: 可关, 默认 enabled; enable_thinking=true/false（default=true）; thinking_budget=上下界未确认（default=null） | 晨羽AI公开本型号 Chat 面 enable_thinking=true/false，默认 true；支持 thinking_budget，但数值上下界和默认预算未公布。已登记的 Responses / Messages 面控制仍未知，coverage 保持 partial；不能用最大输出或其他型号预算代填。 |
| `wan3.0-video` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `wan3.0-video-prime` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `MiniMax-M3` | unknown → supported / partial | openai_chat: 可关, 默认 adaptive; thinking.type="adaptive"/"disabled"（default="adaptive"）<br>anthropic_messages: 可关, 默认 disabled; thinking.type="adaptive"/"disabled"（default="disabled"）<br>openai_responses: 可关, 默认 disabled; reasoning.effort="none"/"minimal"/"low"/"medium"/"high"（default="none"） | 晨羽AI公开 Chat 默认 adaptive，Messages 默认 disabled，Responses 默认 none；三面均可关闭。Responses 的非 none 取值只开启自适应思考，不区分深度，故 kind=mode。公开声明仍为 partial，本次保留该覆盖状态，不补额外档位或预算。 |
| `MiniMax-H3` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `speech-2.8-hd` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `speech-2.8-turbo` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `glm-5.3` | unknown → supported / partial | openai_chat: 不可关, 默认 enabled; thinking.type="enabled"（default="enabled"）; reasoning_effort="low"/"high"/"max"（default="max"） | 晨羽AI仅公开本型号 Chat 面控制：默认开启、不可关闭，reasoning_effort 为 low/high/max，默认 max。已登记的 Messages 面参数仍未知，coverage 保持 partial。 |
| `glm-5.3-flash` | unknown → supported / partial | openai_chat: 不可关, 默认 enabled; thinking.type="enabled"（default="enabled"）; reasoning_effort="low"/"high"/"max"（default="max"） | 晨羽AI仅公开本型号 Chat 面控制：默认开启、不可关闭，reasoning_effort 为 low/high/max，默认 max。已登记的 Messages 面参数仍未知，coverage 保持 partial。 |
| `kimi-k3` | unknown → supported / partial | openai_chat: 不可关, 默认 enabled; reasoning_effort="low"/"high"/"max"（default="max"） | 晨羽AI公开本型号 Chat 面 reasoning_effort=low/high/max，默认 max，思考默认开启且不可关闭。已登记的 Responses / Messages 面控制仍未知，不引用 K2.x 或订阅产品的行为。 |
| `Qwen/Qwen3.8-27B-FP8` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |
| `nvidia/Qwen3.6-35B-A3B-NVFP4` | unknown → unknown / unknown | — | 公开接口未返回此型号的 reasoning 对象；模型说明和适用接口专文也未提供逐型号控制。 继续保留未知；不从同名原厂、其他请求 ID 或模型模态推断支持 / 不支持。 |

## 候选说明

- 校验通过，70 个单元测试全部通过。14 个协议面配置、23 个控制项的参数、原始值、默认值、预算边界与开关逐项和公开声明对齐；全部非思考模型字段及其他服务商文件保持原值。
- 更新本产品的 reasoning、来源登记和当前摘要；前次模型 / 价格采集文件保持原文，其他服务商与工作树已有 DeepSeek 分时价格改动保持原样。全仓审阅包仍包含前次未提交内容，不能把全部差异视作本次新改动。
- 完成校验后生成 `.review/REVIEW.md`、`diff.patch` 和候选 SHA-256；本次仅更新本地资料，没有提交、推送、正式 tag 或消费者激活。
