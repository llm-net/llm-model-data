# Anthropic

## 核对重点

API 与 Claude Code 订阅分开；缓存读和缓存写不同，写入 TTL 也可能改变计费。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [api-global](offerings/api-global/catalog.json)
- [claude-code](offerings/claude-code/catalog.json)

## 更新纪律

模型身份独立核对；按量产品核价，订阅模型只维护按量参考价：优先本平台，缺价才取开发方。完整重复保存价格，不做运行时继承。只选一个标准基准，其他规格和促销写备注。更新前检查provider.json排除清单。
