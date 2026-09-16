# Codex 单次请求思考档位补充核对

检查时间：2026-09-16T14:10:54.972577+00:00。基线 `data-2026.09.16.3` / `dbfe01ff250e30f7f65382e84abf1c89cf6a02c4`。

## 来源与方法

- 官方 CLI 发布：[rust-v0.154.0](https://github.com/openai/codex/releases/tag/rust-v0.154.0)。检查已安装的官方 0.154.0 Linux 程序内嵌模型目录；二进制 SHA-256 `3188814c35471432d4123203e0eb38e5bddc60226e3d7ddf0e59e649ea140022`。读取精确 slug 的 supported_reasoning_levels 与 default_reasoning_level，未根据型号名推导。
- [Codex 模型文档](https://learn.chatgpt.com/docs/models)的 Choose a model：思考强度可选；Ultra 同时启用任务委派，不能表示为单次 HTTP 请求档位。
- [Codex 配置文档](https://learn.chatgpt.com/docs/config-file/config-reference)的 model_reasoning_effort / wire_api：客户端使用 Responses。通用枚举不能替代逐型号目录。
- 官方 CLI 0.154.0，以隔离的空配置、无凭据的回环假服务运行 `gpt-6-astra` + `model_reasoning_effort="high"`。捕获的请求字段是 `model: gpt-6-astra`、`reasoning.effort: high`。无真实模型调用，不涉及账号或私有数据。此验证确认请求构造；并非远端推理成功证明。

## 已确认范围

| Codex 型号 | 单次请求 reasoning.effort | CLI 内嵌默认 |
| --- | --- | --- |
| gpt-6-astra | low, medium, high, xhigh, max | low |
| gpt-5.6-sol | low, medium, high, xhigh, max | low |
| gpt-5.6-terra | low, medium, high, xhigh, max | medium |
| gpt-5.6-luna | low, medium, high, xhigh, max | medium |
| gpt-5.5 | low, medium, high, xhigh | medium |

API profile 的 default 保持 null：CLI 内嵌默认不等于不带 reasoning 的订阅 HTTP 请求默认。是否可关闭保持未知，所以仍是 partial。Spark 不在所检查的内嵌目录中，未补造其档位。

## 修复原因

上一版只登记选择器的 UI 事实，Astra 等型号的 controls 为空；消费者正确地拒绝把界面标签直接当成请求值，结果没有可选项。现在单独登记已核对的 api_request 参数，消费者可展示下拉选择并验证请求，仍保留剩余未知。完整性状态不能作为整个模型的操作禁用条件。
