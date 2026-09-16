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
