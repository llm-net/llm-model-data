# OpenCode

## 核对重点

OpenCode Go 是面向国际用户的包月开源编码模型套餐，与 Zen 按量余额分开。Go 文档的“token 价格”是用量上限换算表，不是参考价；模型参考价按用户指定取各模型源头厂商官网公开按量价，中国厂商取其国内官网人民币价，不换汇。

当前产品包含 Go 和 Go Plus 两档。原厂停止某个型号不证明 Go 同名入口停止；Go 仍列出而原厂已无现行标准报价时保留本产品模型，并把原厂参考价标为 unknown。官方入口为 `/inference/go/`，逐型号原生入口取当前 Endpoints 表；兼容面还须核对 Go 与 Harnesses 的明确声明，不从旧路径或同域名推断兼容。

先读取 provider.json 的官方来源入口；入口本身不代表当前事实已经核实。具体核对状态以 catalog.json 各条 verification 为准。

## 独立产品

- [go](offerings/go/catalog.json)

## 更新纪律

型号与原生协议以 Go 文档 Endpoints 表为准；Go 与 Harnesses 当前明确所有在列文本模型还支持 Chat、Responses、Messages 和 Gemini GenerateContent，非原生面由 Console 转换。记录转换事实及限制，不据此推断思考参数等价；未在当前清单出现的历史型号不自动扩面。请求使用裸型号名。开发方按量目录已收录的型号保存 `catalog_model` 来源并完整复制数字；未收录的只登记开发方 URL。促销价、长上下文档、缓存写入限免不进基准。更新前检查provider.json排除清单。

## 协议面核对

每次更新必须按 [PROTOCOLS.md](../../docs/PROTOCOLS.md) 逐模型核对 `capabilities.interfaces` 与独立 `interface_assessment`。不能从模型原厂、价格或其他平台继承协议；partial / unknown 必须进入候选报告。本轮证据见 [Go 核对记录](../../evidence/opencode/2026-09-23-go.md)。

## 思考能力核对

每次更新同时按 [REASONING.md](../../docs/REASONING.md) 逐模型维护 `capabilities.reasoning`。Go 文档未公布逐型号思考控制，当前全部 unknown；不从开发方 API 或 models.dev 布尔标记继承。

## 上下文长度核对

新增及每次更新模型必须按 [CONTEXT.md](../../docs/CONTEXT.md) 查询本产品窗口。Go 文档不列窗口；OpenCode 文档指明客户端从 models.dev 读取型号限额，当前取其 opencode-go 条目的 `limit.context`，不从开发方 API 继承。
