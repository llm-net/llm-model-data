# Cursor 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-auth`：https://cursor.com/docs/cli/reference/authentication
- `protocol-install`：https://cursor.com/install
- `protocol-models`：https://cursor.com/docs/models-and-pricing

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

官方已安装 CLI 2026.08.11-e8db854 的 index.js SHA-256：`f6fd4e6bf3d6ecbf66cc2dcabcf708b8a7c37b400d10c82a58658b5e331c36d0`。独立读取该官方产物的服务声明，`agent.v1.AgentService` 下 `Run` 的 kind 为 `BiDiStreaming`，另有 RunSSE / RunPoll；只摘录协议标识，不保存客户端程序、会话或凭证。用户 API Key 文档与模型配置页分别核对认证和型号范围。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| individual | `composer-2-5` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `grok-4-6` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `grok-4-5` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `claude-fable-5-1` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `claude-opus-5` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `claude-sonnet-5` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `gemini-3-1-pro` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `gemini-3-8-flash` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `gpt-5-6-luna` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `gpt-5-6-sol` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `gpt-5-6-terra` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
| individual | `muse-spark-1-3` | `cursor_agent` | complete | auth, install, models | Cursor 个人订阅通过官方客户端私有 Agent ConnectRPC / protobuf 使用；本地官方 CLI 2026.08.11-e8db854 代码确认 AgentService.Run 双向流。不是按模型原厂分配的 Chat / Responses / Messages 面，也不代表公开通用推理 API。 |
