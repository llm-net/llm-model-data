# 协议面核对结果（2026-09-16）

基线：`a2ab808b3aa1506bf8bef6406892172bce8ee3c4`（`data-2026.09.16.2`）。当前是本地候选，未发布。

## 范围与结果

- 按用户指令整家移除硅基流动（6条模型）与 Together AI（1条模型），排除清单与发布校验阻止重新引入。历史证据保留，不参与当前收录。
- 剩余18家服务商、28个产品、209条模型全部有协议面核对记录：148条 complete、43条 partial、18条 unknown。**逐条填写不等于全部协议已确认**；unknown 不表示不支持。
- 已确认的面均登记规范 ID、独立来源、核对时间和本地证据。没有真实 Key 推理测试；complete 只描述本次官方资料范围。
- 逐字段对比基线：209条保留模型的身份、原核对信息、价格数字、套餐、额度及已有非协议能力均未改。无新增模型，价格基准仍为179条已知、30条未知。
- 晨羽18条文本模型缺匿名逐型号协议矩阵，保留 unknown；deepseek-v4-flash 的 Responses 文档自相矛盾，保留 partial。其他 partial 的具体型号范围与待核对项如下。

## 服务商汇总

| 服务商 | 模型数 | complete | partial | unknown | 已确认面（跨产品并集，不能整家复制） |
| --- | ---: | ---: | ---: | ---: | --- |
| [anthropic](../evidence/anthropic/2026-09-16-protocols.md) | 9 | 9 | 0 | 0 | `anthropic_messages`, `openai_chat` |
| [ark](../evidence/ark/2026-09-16-protocols.md) | 42 | 39 | 3 | 0 | `anthropic_messages`, `ark_image`, `ark_video`, `openai_chat`, `openai_responses` |
| [bailian](../evidence/bailian/2026-09-16-protocols.md) | 35 | 21 | 14 | 0 | `anthropic_messages`, `bailian_text`, `bailian_video`, `openai_chat`, `openai_responses` |
| [chenyu-ai](../evidence/chenyu-ai/2026-09-16-protocols.md) | 29 | 10 | 1 | 18 | `anthropic_messages`, `ark_video`, `bailian_video`, `minimax_speech`, `minimax_video`, `openai_chat`, `openai_image` |
| [cursor](../evidence/cursor/2026-09-16-protocols.md) | 12 | 12 | 0 | 0 | `cursor_agent` |
| [deepseek](../evidence/deepseek/2026-09-16-protocols.md) | 4 | 2 | 2 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |
| [gemini](../evidence/gemini/2026-09-16-protocols.md) | 1 | 1 | 0 | 0 | `gemini_generate_content`, `openai_chat` |
| [groq](../evidence/groq/2026-09-16-protocols.md) | 2 | 2 | 0 | 0 | `openai_chat`, `openai_responses` |
| [hunyuan](../evidence/hunyuan/2026-09-16-protocols.md) | 9 | 8 | 1 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |
| [kling](../evidence/kling/2026-09-16-protocols.md) | 6 | 6 | 0 | 0 | `kling_video` |
| [minimax](../evidence/minimax/2026-09-16-protocols.md) | 14 | 14 | 0 | 0 | `anthropic_messages`, `minimax_image`, `minimax_speech`, `minimax_text`, `minimax_video`, `openai_chat`, `openai_responses` |
| [mistral](../evidence/mistral/2026-09-16-protocols.md) | 2 | 2 | 0 | 0 | `openai_chat` |
| [moonshot](../evidence/moonshot/2026-09-16-protocols.md) | 8 | 1 | 7 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |
| [openai](../evidence/openai/2026-09-16-protocols.md) | 7 | 7 | 0 | 0 | `openai_chat`, `openai_responses` |
| [openrouter](../evidence/openrouter/2026-09-16-protocols.md) | 1 | 1 | 0 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |
| [qianfan](../evidence/qianfan/2026-09-16-protocols.md) | 9 | 9 | 0 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |
| [xai](../evidence/xai/2026-09-16-protocols.md) | 4 | 2 | 2 | 0 | `openai_chat`, `openai_responses`, `xai_grpc` |
| [zhipu](../evidence/zhipu/2026-09-16-protocols.md) | 15 | 2 | 13 | 0 | `anthropic_messages`, `openai_chat`, `openai_responses` |

## 剩余待核对项

这些项目已经保留已确认的面，未确认的面没有猜填。后续更新仍须逐项检查，自动候选报告会继续列出，直到有证据解除缺项。

| 产品 / 模型 | 状态 | 缺口与适用范围 |
| --- | --- | --- |
| `ark/api-cn/doubao-seed-character-260628` | partial | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| `ark/api-cn/doubao-seed-character-251128` | partial | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| `ark/api-cn/doubao-seed-translation-250915` | partial | 该特定翻译 / 角色型号的 Chat 调用已登记；通用平台 Responses / Messages 端点存在不足以证明此型号支持，其他两面待补具体型号证据。 |
| `bailian/api-cn/qwen3-8-max-prime` | partial | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| `bailian/api-cn/minimax-minimax-m3` | partial | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| `bailian/api-cn/xiaomi-mimo-v2-5-pro` | partial | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| `bailian/api-cn/stepfun-step-3-7-flash` | partial | Responses 文档说明列表外百炼直供文本模型也有基础兼容能力，但 Agent 内置工具受限；Messages 仅按明确支持列表登记。DashScope 原生仅登记已核实的千问产品，不据第三方训练方推导。 |
| `bailian/token-plan-cn/qwen3-8-max` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/qwen3-8-flash` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/qwen3-7-plus` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/deepseek-v4-pro` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/deepseek-v4-flash` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/kimi-k2-7-code` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/kimi-k2-6` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/glm-5-2` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/glm-5-1` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `bailian/token-plan-cn/glm-5` | partial | 按本产品独立接入表登记 Chat 与 Messages。Token Plan 接入表未承诺 Responses 或 DashScope 原生调用，不继承按量 API。 |
| `chenyu-ai/api/deepseek-v4-pro` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/deepseek-v4-flash` | partial | 快速上手与 Messages 页按此精确 ID 展示 Chat / Messages 请求。Responses 页一处说 DeepSeek 不支持、另一处示例却用此 ID，存在冲突；不据示例登记 Responses，待公开协议矩阵澄清。 |
| `chenyu-ai/api/deepseek-v4-flash-vision-exp` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/doubao-seed-2-1-pro-260628` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/doubao-seed-2-1-turbo-260628` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/doubao-seed-2-0-lite-260428` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/doubao-seed-2-0-mini-260428` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/doubao-seed-2-0-pro-260215` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen3-8-max` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen3-7-plus` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen3-8-flash` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen3-7-flash` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen3-8-27b` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/minimax-m3` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/glm-5-3` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/glm-5-3-flash` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/kimi-k3` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/qwen-qwen3-8-27b-fp8` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `chenyu-ai/api/nvidia-qwen3-6-35b-a3b-nvfp4` | unknown | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `deepseek/api-cn/deepseek-v4-flash` | partial | 按现有目录和官方 Chat 模型资料登记 Chat；新版 Responses 枚举只列 deepseek-flash / deepseek-v4-pro，Messages 对未知名称会回退，尚未证实此旧 ID 的精确路由，不扩填。 |
| `deepseek/api-cn/deepseek-v4-flash-vision-exp` | partial | 按现有目录和官方 Chat 模型资料登记 Chat；新版 Responses 枚举只列 deepseek-flash / deepseek-v4-pro，Messages 对未知名称会回退，尚未证实此旧 ID 的精确路由，不扩填。 |
| `hunyuan/api-cn/hy-vision-2-0-instruct` | partial | 视觉特定型号只登记 Chat；通用语言型号三协议矩阵未明确覆盖此型号，其他面待核对。 |
| `moonshot/api-cn/kimi-k2-7-code` | partial | Claude Code 接入页另列 K2.7 Code / K2.6；Responses 当前仅明确支持 kimi-k3。与 Messages API 单页只列 K3 的差异留在证据中。 |
| `moonshot/api-cn/kimi-k2-7-code-highspeed` | partial | 高速独立 ID 只登记 Chat；不继承标准速度型号的 Messages，Responses 当前仅明确支持 K3。 |
| `moonshot/api-cn/kimi-k2-6` | partial | Claude Code 接入页另列 K2.7 Code / K2.6；Responses 当前仅明确支持 kimi-k3。与 Messages API 单页只列 K3 的差异留在证据中。 |
| `moonshot/kimi-code/k3` | partial | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| `moonshot/kimi-code/k3-256k` | partial | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| `moonshot/kimi-code/kimi-for-coding` | partial | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| `moonshot/kimi-code/kimi-for-coding-highspeed` | partial | Kimi Code 模型配置逐项列四个 ID，接入表列 OpenAI Chat 与 Anthropic；未承诺订阅 Responses，不从 Kimi 按量 K3 推导。 |
| `xai/grok-build/grok-4-6` | partial | Grok Build 工具订阅承载按官方客户端核对 Responses；不是按量 API 资格，也不继承按量 Chat 或 gRPC。本地官方二进制含 Responses 请求路径，未用订阅真实调用。 |
| `xai/grok-build/grok-4-5` | partial | Grok Build 工具订阅承载按官方客户端核对 Responses；不是按量 API 资格，也不继承按量 Chat 或 gRPC。本地官方二进制含 Responses 请求路径，未用订阅真实调用。 |
| `zhipu/api-cn/glm-5-3` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5-3-flash` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5-2` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5-1` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5-turbo` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-7` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-7-flashx` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-7-flash` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-5-air` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-5v-turbo` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-6v` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |
| `zhipu/api-cn/glm-4-6v-flash` | partial | 官方 Chat 模型接口与 Claude SDK 兼容层；Responses 的明确接入资料只针对 Coding Plan，按量产品不自动继承，待补按量凭证与具体型号证据。 |

## 后续更新约束

维护规则见 [PROTOCOLS.md](PROTOCOLS.md)，已写入 AGENTS.md、采集 / 自动化 / 数据模型 / 审核文档、每家 README 和更新任务 / PR 模板。校验拒绝漏填、旧面名、无证据、模态错配及已排除服务商；候选审阅同时列出协议变化和全部 partial / unknown。

新增字段是 v1 可选元数据扩展；当前发布要求完整核对记录。此数据候选不代表消费者已经接入新增协议字段，也不改变云端或设备的运行期探测结果。
