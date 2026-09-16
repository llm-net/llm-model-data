# 火山方舟

## 核对重点

按量、Agent Plan、Coding Plan 分开；文本与图片视频的计量项不同，不能只抓文本价表。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api-cn](offerings/api-cn/catalog.json)
- [agent-plan-cn](offerings/agent-plan-cn/catalog.json)
- [coding-plan-cn](offerings/coding-plan-cn/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。

短名估价按同系列最新日期版本对齐，具体范围与选择规则见[PRICING.md](../../docs/PRICING.md)。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`，包括本家的所有订阅产品。不能从模型原厂、价格或同家其他产品继承协议；partial / unknown 必须进入候选报告。本轮证据见 [协议核对记录](../../evidence/ark/2026-09-16-protocols.md)。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`；官方参数、档位、开关、预算、默认值按产品及协议 / 工具入口独立核对，未证实的部分保留 unknown / partial，不能继承原厂 API。本轮记录见 [思考能力证据](../../evidence/ark/2026-09-16-reasoning.md)。
