# 火山方舟 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-models`：https://www.volcengine.com/docs/82379/1330310
- `protocol-chat`：https://www.volcengine.com/docs/82379/1494384
- `protocol-responses`：https://www.volcengine.com/docs/82379/1569618
- `protocol-messages`：https://www.volcengine.com/docs/82379/2655179
- `protocol-image`：https://www.volcengine.com/docs/82379/1541523
- `protocol-video`：https://www.volcengine.com/docs/82379/1366799
- `protocol-coding`：https://www.volcengine.com/docs/82379/1928261
- `protocol-coding-codex`：https://www.volcengine.com/docs/82379/2556056
- `protocol-agent`：https://www.volcengine.com/docs/82379/2373738
- `protocol-agent-codex`：https://www.volcengine.com/docs/82379/2556054

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| agent-plan-cn | `deepseek-v4-pro` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | agent, agent-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| agent-plan-cn | `deepseek-v4-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | agent, agent-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| agent-plan-cn | `doubao-seedance-2-5` | `ark_video` | complete | models, video, agent | 方舟 Agent Plan 独立订阅入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| agent-plan-cn | `doubao-seedance-2-0` | `ark_video` | complete | models, video, agent | 方舟 Agent Plan 独立订阅入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| agent-plan-cn | `doubao-seedance-2-0-fast` | `ark_video` | complete | models, video, agent | 方舟 Agent Plan 独立订阅入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| agent-plan-cn | `doubao-seedance-2-0-mini` | `ark_video` | complete | models, video, agent | 方舟 Agent Plan 独立订阅入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| agent-plan-cn | `doubao-seedream-5-0-lite` | `ark_image` | complete | models, image, agent | 方舟 Agent Plan 独立订阅入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seed-evolving` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-1-pro-260628` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-1-turbo-260628` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-lite-260428` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-mini-260428` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-pro-260215` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-lite-260215` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-mini-260215` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-2-0-code-preview-260215` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-character-260628` | `openai_chat` | partial | models, chat | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| api-cn | `glm-5-2-260617` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `deepseek-v4-pro-ga-260813` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `deepseek-v4-flash-ga-260731` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `deepseek-v4-pro-260425` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `deepseek-v4-flash-260425` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | models, chat, responses, messages | 按量模型列表与三种文本 API 核对；Model ID / 接入点仍受开通与账号授权限制。Responses 有服务端状态，Messages 兼容参数以官方说明为准。 |
| api-cn | `doubao-seed-character-251128` | `openai_chat` | partial | models, chat | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| api-cn | `doubao-seed-translation-250915` | `openai_chat` | partial | models, chat | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| api-cn | `doubao-seedream-5-0-pro-260628` | `ark_image` | complete | models, image | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedream-5-0-260128` | `ark_image` | complete | models, image | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-5-260628` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-0-260128` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-0-mini-260615` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-5` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-0` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| api-cn | `doubao-seedance-2-0-fast` | `ark_video` | complete | models, video | 方舟 按量入口 的 Seedream / Seedance 厂商协议。按型号选图片生成或视频异步任务，不因 images/generations 同名便标成 OpenAI Image。短名与日期版独立保留。 |
| coding-plan-cn | `doubao-seed-evolving` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `doubao-seed-2-1-turbo` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `doubao-seed-2-0-lite` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `minimax-m3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `glm-5-3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `glm-5-3-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `deepseek-v4-flash` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `deepseek-v4-pro` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `kimi-k2-7-code` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
| coding-plan-cn | `kimi-k3` | `openai_chat`, `openai_responses`, `anthropic_messages` | complete | coding, coding-codex | 此产品官方快速接入与 Codex 配置确认三种文本面；只适用于本套餐支持的 Model Name，不能把套餐 Base URL 或 Key 用到按量产品。 |
