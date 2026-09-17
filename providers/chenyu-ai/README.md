# 晨羽 AI

## 核对重点

作为独立服务商记录公开模型和价格；不能抄采购厂商价格或某个开发环境模型列表。

模型与价格的当前入口是 [模型页](https://chenyu.pro/api-docs/docs/models/)，页面从匿名 [公开模型接口](https://chenyu.pro/api/v1/public/models) 实时读取。常规更新先查这个接口中的精确请求 ID、协议面、上下文和价格行，不能只抓 HTML 的加载占位，也不能用设备发布目录代替当前可用清单。

2026-09-17 已更新 30 个模型（已有 29 个，新增 `deepseek-flash`），30 项人民币按量价与协议面已核对，20 项文本上下文为已知整数，10 项生成 / 合成接口不适用文本对话窗口。随后按新公开说明补入 10 项思考支持（1 项 complete / 9 项 partial），20 项仍未知，两款自部署模型的最大输出仍未知。模型与价格见 [首轮证据](../../evidence/chenyu-ai/2026-09-17-public-models.md)，新增的思考参数、默认值和缺项见 [思考补充核对](../../evidence/chenyu-ai/2026-09-17-reasoning.md)。这些是本地数据核对结果，正式发布仍以远端数据 tag 为准。

当前公开价簿 v22 的 DeepSeek 价格行没有峰谷条件；不能因计费说明介绍了分时机制，或原厂已有峰谷价，就给晨羽AI补造空闲档。图片输入免费张数来自 `conditions.freeUnits`；视频 token、视频秒和语音计费字符保持独立单位。金额按纳元用 Decimal 精确换算，不使用浮点。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api](offerings/api/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`，包括本家的所有订阅产品。不能从模型原厂、价格或同家其他产品继承协议；partial / unknown 必须进入候选报告。当前证据见 [2026-09-17 核对记录](../../evidence/chenyu-ai/2026-09-17-public-models.md)，此前 [2026-09-16 记录](../../evidence/chenyu-ai/2026-09-16-protocols.md) 仅作历史。实时逐型号矩阵优先于静态页面的旧举例，冲突仍需显式记录。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`；官方参数、档位、开关、预算、默认值按产品及协议 / 工具入口独立核对，未证实的部分保留 unknown / partial，不能继承原厂 API。本轮来源是晨羽AI自己公开的 `data.models[].reasoning`，查询范围与缺项见 [2026-09-17 思考证据](../../evidence/chenyu-ai/2026-09-17-reasoning.md)。接口附带的原厂核对元数据只供追溯，本产品须重新登记晨羽AI来源与证据；通用字段透传说明仍不证明逐型号接受哪些参数。

DeepSeek V4 Pro 已公开三面控制；GLM 5.3 / Flash 和 Kimi K3 当前只确认 Chat 的 low/high/max；五项 Qwen 的 Chat 开关已知、预算范围仍未知。MiniMax M3 的 Chat / Messages / Responses 默认行为不同，Responses 的 `reasoning.effort` 只切模式；按量原厂字段、其他型号与其他协议的兼容值都不能自动补入缺项。

## 上下文长度核对

新增及每次更新模型必须按 [CONTEXT.md](../../docs/CONTEXT.md) 查询本产品官方窗口，包含全部订阅型号。填写 `context_window_tokens` 与独立 `context_assessment`，记录单位及套餐 / 扩展模式条件；未知写原因并进入审阅报告，不从同名原厂或其他产品继承。
