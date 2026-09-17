# DeepSeek

## 核对重点

缓存命中与未命中分别定价；核对峰谷作息、币种以及旧模型名的实际映射。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api-cn](offerings/api-cn/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。

## 当前核价口径

使用 catalog v2 的规则内 time_pricing，完整保存高峰与空闲价格及北京时间作息；历史调价仍留 Git。 最新分时结论见[核对证据](../../evidence/deepseek/2026-09-17-time-pricing.md)。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`，包括本家的所有订阅产品。不能从模型原厂、价格或同家其他产品继承协议；partial / unknown 必须进入候选报告。本轮证据见 [协议核对记录](../../evidence/deepseek/2026-09-16-protocols.md)。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`；官方参数、档位、开关、预算、默认值按产品及协议 / 工具入口独立核对，未证实的部分保留 unknown / partial，不能继承原厂 API。本轮记录见 [思考能力证据](../../evidence/deepseek/2026-09-16-reasoning.md)。

## 上下文长度核对

新增及每次更新模型必须按 [CONTEXT.md](../../docs/CONTEXT.md) 查询本产品官方窗口，包含全部订阅型号。填写 `context_window_tokens` 与独立 `context_assessment`，记录单位及套餐 / 扩展模式条件；未知写原因并进入审阅报告，不从同名原厂或其他产品继承。
