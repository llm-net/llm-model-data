# 阿里云百炼 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-chat`：https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope
- `protocol-responses`：https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-responses
- `protocol-messages`：https://help.aliyun.com/zh/model-studio/anthropic-api-messages
- `protocol-native`：https://help.aliyun.com/zh/model-studio/text-generation
- `protocol-tools`：https://help.aliyun.com/zh/model-studio/more-tools
- `protocol-coding`：https://help.aliyun.com/zh/model-studio/coding-plan-faq
- `protocol-video`：https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `qwen3-8-max` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-8-max-prime` | `openai_chat`, `openai_responses` | partial | chat, responses | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-7-plus` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-8-flash` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-7-flash` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-coder-plus` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-vl-plus` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-vl-flash` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-8-2-4t-a95b` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `qwen3-8-27b` | `openai_chat`, `openai_responses`, `anthropic_messages`, `bailian_text` | complete | chat, responses, messages, native | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `minimax-minimax-m3` | `openai_chat`, `openai_responses` | partial | chat, responses | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `xiaomi-mimo-v2-5-pro` | `openai_chat`, `openai_responses` | partial | chat, responses | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `stepfun-step-3-7-flash` | `openai_chat`, `openai_responses` | partial | chat, responses | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| api-cn | `wan3-0-video` | `bailian_video` | complete | video | 万相 3.0 / prime 通过百炼视频异步任务协议调用；不是 Chat 视频输入，也不是 OpenAI 图像协议。 |
| api-cn | `wan3-0-video-prime` | `bailian_video` | complete | video | 万相 3.0 / prime 通过百炼视频异步任务协议调用；不是 Chat 视频输入，也不是 OpenAI 图像协议。 |
| coding-plan-cn | `qwen3-7-plus` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `qwen3-6-plus` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `kimi-k2-5` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `glm-5` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `minimax-m2-5` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `qwen3-5-plus` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `qwen3-max-2026-01-23` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `qwen3-coder-next` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `qwen3-coder-plus` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| coding-plan-cn | `glm-4-7` | `openai_chat`, `anthropic_messages` | complete | tools, coding | 按本产品独立接入表登记 Chat 与 Messages。官方 FAQ 明确不支持 Responses。 |
| token-plan-cn | `qwen3-8-max` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `qwen3-8-flash` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `qwen3-7-plus` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `deepseek-v4-pro` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `deepseek-v4-flash` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `kimi-k2-7-code` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `kimi-k2-6` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `glm-5-2` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `glm-5-1` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| token-plan-cn | `glm-5` | `openai_chat`, `anthropic_messages` | partial | tools | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
