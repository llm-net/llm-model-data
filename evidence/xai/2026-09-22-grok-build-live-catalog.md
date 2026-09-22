# Grok Build 在线目录补核

基线：`f181c2ed405c57c9fc15df35081cb8a00d73b23d`（`data-2026.09.22.1`）。前轮仅核对公开文档与客户端内嵌目录，未取得新订阅型号 request_id。本轮查询官方订阅在线目录补齐，不修改不可变旧 tag。

## 来源与边界

- `grok-build-models`：https://cli-chat-proxy.grok.com/v1/models ，UTC `2026-09-22T05:59:06Z`，GET 200。
- 两份现有订阅凭据分别查询，返回的下列型号及能力完全相同。只查询型号元数据，没有推理、刷新令牌或修改数据库；凭据只在持有设备的进程内使用，未输出或归档。
- 仅保存公开型号字段的[最小摘录](2026-09-22-grok-build-models.json)。不保存账号身份、设备信息、凭据、端点密钥、额外请求头、系统提示词或原始响应。
- `refresh-settings`：https://docs.x.ai/build/settings/reference.md ，前轮 UTC `2026-09-22T05:37:10Z` 已获取；`models.default_reasoning_effort` 是官方客户端设置键。

## 逐型号结果

| 本地模型 ID | 官方 model / 请求 ID | api_backend | context_window | reasoning_efforts 原值 | 客户端 reasoning_effort |
| --- | --- | --- | ---: | --- | --- |
| grok-4-7 | grok-4.7 | responses | 500000 | low, medium, high, xhigh | high |
| grok-4-7-fast | grok-4.7-build-fast | responses | 500000 | low, medium, high, xhigh | high |
| grok-4-6 | grok-4.6 | responses | 500000 | low, medium, high, xhigh | high |
| grok-4-5 | grok-4.5 | responses | 500000 | low, medium, high | high |

四项均声明 supports_reasoning_effort=true，均未标 hidden。前两项 request_id 从 null 补为官方 model 值；Fast 本地身份保持不变，不把展示名猜成 `grok-4.7-fast`。4.5 从 unknown 改为 active，因为在线订阅目录明确仍列出它；active 不保证每份账号都有资格。

两项新型号的窗口由 unknown 变 known；协议从 unknown 变 Responses/partial；思考从 unknown 变 supported/partial。既有 4.5/4.6 用在线精确型号重新核对相同字段。Chat、Messages、gRPC 未获本产品逐型号依据，不从按量 API 继承。裸订阅请求参数、后端默认、关闭能力与其他客户端版本仍未确认，故保留 partial。客户端 high 默认不等于后端裸请求默认。

## 价格与消费边界

没有更改任何模型价格数字、参考对象或套餐；标准 4.7/4.6/4.5 沿用上轮对应公开 API 参考价和原核对日期。Fast 在公开 API 上没有对应按量产品，reference_prices 仍 unknown，不能解释为免费或自动倍乘标准版。

资料消费者通常只把 active 且 request_id 非空的条目投影为可选模型。前一版两项新型号虽有资料记录，但无法进入这种列表；本次修正该缺项，并使用消费者真实 DeviceCatalog 转换验证请求名被保留。此验证不代表推理实调或消费者已经同步新版本。
