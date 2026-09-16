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
