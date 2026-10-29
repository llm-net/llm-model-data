# 晨羽 AI

## 核对重点

作为独立服务商记录公开模型和价格；不能抄采购厂商价格或某个开发环境模型列表。

模型与价格的当前入口是 [模型页](https://chenyu.pro/api-docs/docs/models/)，页面从匿名 [公开模型接口](https://chenyu.pro/api/v1/public/models) 实时读取。常规更新先查这个接口中的精确请求 ID、协议面、上下文和价格行，不能只抓 HTML 的加载占位，也不能用设备发布目录代替当前可用清单。

本轮逐模型核对见 [2026-10-29 证据](../../evidence/chenyu-ai/2026-10-29-audit.md)，逐项核验日期以 catalog.json 中各独立 assessment 为准。当前公开接口的 DeepSeek 价格行已经包含 `conditions.timeBand`，按本平台发布的时段与每档金额保存；不能从计费说明或原厂价格推造本平台未公开的档位。图片输入免费张数来自 `conditions.freeUnits`；视频 token、视频秒和语音计费字符保持独立单位。金额按纳元用 Decimal 精确换算，不使用浮点。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api](offerings/api/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`，包括本家的所有订阅产品。不能从模型原厂、价格或同家其他产品继承协议；partial / unknown 必须进入候选报告。当前证据见 [2026-10-29 核对记录](../../evidence/chenyu-ai/2026-10-29-audit.md)，此前记录仅作历史。实时逐型号矩阵优先于静态页面的旧举例，冲突仍需显式记录。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`；官方参数、档位、开关、预算、默认值按产品及协议 / 工具入口独立核对，未证实的部分保留 unknown / partial，不能继承原厂 API。本轮来源是晨羽AI自己公开的 `data.models[].reasoning`，查询范围与缺项见 [2026-10-29 证据](../../evidence/chenyu-ai/2026-10-29-audit.md)。接口附带的原厂核对元数据只供追溯，本产品须重新登记晨羽AI来源与证据；通用字段透传说明仍不证明逐型号接受哪些参数。

DeepSeek Flash、V4 Pro 与 Kimi K3 已公开三面控制；五项 Seed 文本已公开 Responses / Messages 控制。GLM 5.3 / Flash 仍仅确认 Chat，五项 Qwen 的公开配置有所扩展但预算边界或部分协议仍不完整。MiniMax M3 的 Chat / Messages / Responses 默认行为不同，Responses 的 `reasoning.effort` 只切模式；按量原厂字段、其他型号与其他协议的兼容值都不能自动补入缺项。

非文本媒体要独立核对本平台专页及其明确指定的原厂资料；仅查阅入口不能刷新全部 `media_io` 或枚举集核验日期。本轮 10 项媒体契约保留历史核验，详细限制未逐字段重新确认的缺口已列入本次证据。

## 上下文长度核对

新增及每次更新模型必须按 [CONTEXT.md](../../docs/CONTEXT.md) 查询本产品官方窗口，包含全部订阅型号。填写 `context_window_tokens` 与独立 `context_assessment`，记录单位及套餐 / 扩展模式条件；未知写原因并进入审阅报告，不从同名原厂或其他产品继承。

2026-09-19 思考专项修正：`deepseek-flash` 已从晨羽AI公开接口独立核实三协议面控制，Responses 为 `none / low / high / max`、默认 `high`；见[本次证据](../../evidence/chenyu-ai/2026-09-19-deepseek-flash-reasoning.md)。此前记录的该型号 unknown 已被替换；其余型号与价格未修改。
