# Moonshot / Kimi

## 核对重点

开放平台和 Kimi Code 分开；短请求名、日期版本、订阅可用型号分别验证。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api-cn](offerings/api-cn/catalog.json)
- [kimi-code](offerings/kimi-code/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。

## 用户指定的示意价

`kimi-for-coding`底模仍为K2.8 Preview，参考`kimi-k2.7-code`的按量价：每百万token输入6.5元、缓存输入1.3元、输出27元。后续更新沿此参考对象核价，不改写成K2.8的官方收费。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`，包括本家的所有订阅产品。不能从模型原厂、价格或同家其他产品继承协议；partial / unknown 必须进入候选报告。本轮证据见 [协议核对记录](../../evidence/moonshot/2026-09-16-protocols.md)。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`；官方参数、档位、开关、预算、默认值按产品及协议 / 工具入口独立核对，未证实的部分保留 unknown / partial，不能继承原厂 API。本轮记录见 [思考能力证据](../../evidence/moonshot/2026-09-16-reasoning.md)。

## 上下文长度核对

新增及每次更新模型必须按 [CONTEXT.md](../../docs/CONTEXT.md) 查询本产品官方窗口，包含全部订阅型号。填写 `context_window_tokens` 与独立 `context_assessment`，记录单位及套餐 / 扩展模式条件；未知写原因并进入审阅报告，不从同名原厂或其他产品继承。
