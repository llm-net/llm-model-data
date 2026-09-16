# 2026-09-16 上下文长度核对结果

基线：`884ae02873a04ef09dad43d386221e966556f8fe`。覆盖 18 家服务商、28 个产品、209 条记录，其中 169 条文本模型。按平台 / 产品 / 精确请求 ID 核对，未新增或删除模型。

## 结果

- 原有整数窗口 18 条，当前 55 条：新增 38 条精确整数，另清除 1 条把输入上限混当总窗口的旧值。
- 47 条已确认整数窗口；84 条已有官方标称规格，尚缺精确整数换算依据（其中 8 条保留历史整数，但显式标为 partial，未冒充本轮确认）。
- 48 条仍为 unknown，其中 38 条文本、10 条晨羽生成模型；30 条生成接口的文本对话窗口不适用。
- 对原先 151 条缺少整数窗口的文本模型，补入 38 条精确整数和 76 条官方标称规格；余下 37 条仍未取得本产品窗口。另有 Gemini 旧值纠正后归入 unknown。
- 每条模型现在都有独立 context_assessment、来源和本地证据；上下文专项没有改价格、身份、协议面、思考能力、最大输出或它们的核对日期。

## 已确认的重要差异

- 百炼公开模型中心支持无凭据匿名查询，按量 API 的 12 条精确型号取得 contextWindow 整数。qwen3.8-max-prime 没有返回，不把相近 ID 当作同一型号。参考 [机读字段摘录](../evidence/bailian/2026-09-16-context-api.json)。
- 百炼 Coding Plan FAQ 的 GLM-5 为 202752、MiniMax-M2.5 为 196608；MiniMax 原厂 API 的 M2.7 为 204800，不能跨产品或型号照搬。
- Kimi Code 的 kimi-for-coding（K2.8 Preview）为 1048576；其价格参考 K2.7 Code 不意味着上下文也采用 K2.7 Code。K3 的 1048576 需要 Allegretto 及以上，Moderato 只有 262144。
- Codex CLI 0.154.0 静态目录的 5 个已收录型号常规窗口为 272000，部分可扩展到 872000；没有使用 API 页的窗口。Spark 不在该内嵌目录中，继续待核。
- Gemini 3.7 Flash 页面只明确输入 1048576、输出 65536；总窗口未确认，旧 context_window_tokens=1048576 已清空，保留输入上限事实在 notes。
- Cursor 文档同时列常规窗口与 Max context；本轮保留这两种规格的区别，没有把最大模式写成常规窗口。

## 产品覆盖

| 服务商 / 产品 | 记录 | 已确认整数 | 仅标称 / 待补证 | 未知 | 不适用 |
| --- | ---: | ---: | ---: | ---: | ---: |
| [anthropic/api-global](../providers/anthropic/offerings/api-global/catalog.json) | 3 | 3 | 0 | 0 | 0 |
| [anthropic/claude-code](../providers/anthropic/offerings/claude-code/catalog.json) | 6 | 4 | 0 | 2 | 0 |
| [ark/agent-plan-cn](../providers/ark/offerings/agent-plan-cn/catalog.json) | 7 | 0 | 2 | 0 | 5 |
| [ark/api-cn](../providers/ark/offerings/api-cn/catalog.json) | 25 | 0 | 17 | 0 | 8 |
| [ark/coding-plan-cn](../providers/ark/offerings/coding-plan-cn/catalog.json) | 10 | 0 | 9 | 1 | 0 |
| [bailian/api-cn](../providers/bailian/offerings/api-cn/catalog.json) | 15 | 12 | 0 | 1 | 2 |
| [bailian/coding-plan-cn](../providers/bailian/offerings/coding-plan-cn/catalog.json) | 10 | 10 | 0 | 0 | 0 |
| [bailian/token-plan-cn](../providers/bailian/offerings/token-plan-cn/catalog.json) | 10 | 0 | 0 | 10 | 0 |
| [chenyu-ai/api](../providers/chenyu-ai/offerings/api/catalog.json) | 29 | 0 | 0 | 29 | 0 |
| [cursor/individual](../providers/cursor/offerings/individual/catalog.json) | 12 | 0 | 12 | 0 | 0 |
| [deepseek/api-cn](../providers/deepseek/offerings/api-cn/catalog.json) | 4 | 0 | 4 | 0 | 0 |
| [gemini/api-global](../providers/gemini/offerings/api-global/catalog.json) | 1 | 0 | 0 | 1 | 0 |
| [groq/api-global](../providers/groq/offerings/api-global/catalog.json) | 2 | 2 | 0 | 0 | 0 |
| [hunyuan/api-cn](../providers/hunyuan/offerings/api-cn/catalog.json) | 9 | 0 | 9 | 0 | 0 |
| [kling/api-cn](../providers/kling/offerings/api-cn/catalog.json) | 6 | 0 | 0 | 0 | 6 |
| [minimax/api-cn](../providers/minimax/offerings/api-cn/catalog.json) | 12 | 3 | 0 | 0 | 9 |
| [minimax/token-plan-cn](../providers/minimax/offerings/token-plan-cn/catalog.json) | 2 | 0 | 1 | 1 | 0 |
| [mistral/api-global](../providers/mistral/offerings/api-global/catalog.json) | 2 | 0 | 2 | 0 | 0 |
| [moonshot/api-cn](../providers/moonshot/offerings/api-cn/catalog.json) | 4 | 0 | 4 | 0 | 0 |
| [moonshot/kimi-code](../providers/moonshot/offerings/kimi-code/catalog.json) | 4 | 4 | 0 | 0 | 0 |
| [openai/api-global](../providers/openai/offerings/api-global/catalog.json) | 1 | 1 | 0 | 0 | 0 |
| [openai/codex](../providers/openai/offerings/codex/catalog.json) | 6 | 5 | 0 | 1 | 0 |
| [openrouter/api-global](../providers/openrouter/offerings/api-global/catalog.json) | 1 | 1 | 0 | 0 | 0 |
| [qianfan/api-cn](../providers/qianfan/offerings/api-cn/catalog.json) | 9 | 0 | 9 | 0 | 0 |
| [xai/api-global](../providers/xai/offerings/api-global/catalog.json) | 2 | 2 | 0 | 0 | 0 |
| [xai/grok-build](../providers/xai/offerings/grok-build/catalog.json) | 2 | 0 | 0 | 2 | 0 |
| [zhipu/api-cn](../providers/zhipu/offerings/api-cn/catalog.json) | 13 | 0 | 13 | 0 | 0 |
| [zhipu/coding-plan-cn](../providers/zhipu/offerings/coding-plan-cn/catalog.json) | 2 | 0 | 2 | 0 | 0 |

## 整数值变化

| 服务商 / 产品 / 模型 | 原值 | 新值 |
| --- | ---: | ---: |
| `anthropic/claude-code/claude-fable-5-1` | null | 1000000 |
| `anthropic/claude-code/claude-fable-5` | null | 1000000 |
| `anthropic/claude-code/claude-opus-5` | null | 1000000 |
| `anthropic/claude-code/claude-sonnet-5` | null | 1000000 |
| `bailian/api-cn/qwen3-8-max` | null | 1000000 |
| `bailian/api-cn/qwen3-7-plus` | null | 1000000 |
| `bailian/api-cn/qwen3-8-flash` | null | 1000000 |
| `bailian/api-cn/qwen3-7-flash` | null | 1000000 |
| `bailian/api-cn/qwen3-coder-plus` | null | 1000000 |
| `bailian/api-cn/qwen3-vl-plus` | null | 262144 |
| `bailian/api-cn/qwen3-vl-flash` | null | 262144 |
| `bailian/api-cn/qwen3-8-2-4t-a95b` | null | 1000000 |
| `bailian/api-cn/qwen3-8-27b` | null | 1000000 |
| `bailian/api-cn/minimax-minimax-m3` | null | 1000000 |
| `bailian/api-cn/xiaomi-mimo-v2-5-pro` | null | 1000000 |
| `bailian/api-cn/stepfun-step-3-7-flash` | null | 262144 |
| `bailian/coding-plan-cn/qwen3-7-plus` | null | 1000000 |
| `bailian/coding-plan-cn/qwen3-6-plus` | null | 1000000 |
| `bailian/coding-plan-cn/kimi-k2-5` | null | 262144 |
| `bailian/coding-plan-cn/glm-5` | null | 202752 |
| `bailian/coding-plan-cn/minimax-m2-5` | null | 196608 |
| `bailian/coding-plan-cn/qwen3-5-plus` | null | 1000000 |
| `bailian/coding-plan-cn/qwen3-max-2026-01-23` | null | 262144 |
| `bailian/coding-plan-cn/qwen3-coder-next` | null | 262144 |
| `bailian/coding-plan-cn/qwen3-coder-plus` | null | 1000000 |
| `bailian/coding-plan-cn/glm-4-7` | null | 202752 |
| `gemini/api-global/gemini-3-7-flash` | 1048576 | null |
| `minimax/api-cn/minimax-m3` | null | 1000000 |
| `minimax/api-cn/minimax-m2-7` | null | 204800 |
| `minimax/api-cn/minimax-m2-7-highspeed` | null | 204800 |
| `moonshot/kimi-code/k3` | null | 1048576 |
| `moonshot/kimi-code/k3-256k` | null | 262144 |
| `moonshot/kimi-code/kimi-for-coding` | null | 1048576 |
| `moonshot/kimi-code/kimi-for-coding-highspeed` | null | 262144 |
| `openai/codex/gpt-6-astra` | null | 272000 |
| `openai/codex/gpt-5-6-sol` | null | 272000 |
| `openai/codex/gpt-5-6-terra` | null | 272000 |
| `openai/codex/gpt-5-6-luna` | null | 272000 |
| `openai/codex/gpt-5-5` | null | 272000 |

## 全部待补证 / 未知项

partial 表示已查到官方窗口规格；只有缺精确整数口径时，不自行统一乘 1000 / 1024。网络失败、订阅产品未列窗口与规格缩写缺口分开记录。以下包括本轮未改动的历史缺项。

| 服务商 / 产品 / 模型 | 状态 | 官方规格 | 缺项与条件 |
| --- | --- | --- | --- |
| `anthropic/claude-code/claude-haiku-4-5` | unknown | — | 本次 Claude Code 型号配置页未明确这两个精确订阅型号的上下文窗口；API 的 200K 不能自动作为订阅限制。 |
| `anthropic/claude-code/claude-haiku-4-5-20251001` | unknown | — | 本次 Claude Code 型号配置页未明确这两个精确订阅型号的上下文窗口；API 的 200K 不能自动作为订阅限制。 |
| `ark/agent-plan-cn/deepseek-v4-pro` | partial | 1024k | Agent Plan 自身型号表，与 Coding Plan 分别核对。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/agent-plan-cn/deepseek-v4-flash` | partial | 1024k | Agent Plan 自身型号表，与 Coding Plan 分别核对。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-evolving` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-1-pro-260628` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-1-turbo-260628` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-lite-260428` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-mini-260428` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-pro-260215` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-lite-260215` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-mini-260215` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-2-0-code-preview-260215` | partial | 256k | 按量目录精确日期版行。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-character-260628` | partial | 128k | 按量目录精确日期版行。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/glm-5-2-260617` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/deepseek-v4-pro-ga-260813` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/deepseek-v4-flash-ga-260731` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/deepseek-v4-pro-260425` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/deepseek-v4-flash-260425` | partial | 1024k | 按量目录精确日期版行。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-character-251128` | partial | 128k | 按量目录精确日期版行。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/api-cn/doubao-seed-translation-250915` | partial | 4k | 按量目录精确日期版行。 官方窗口原文为 4k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/doubao-seed-evolving` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/doubao-seed-2-1-turbo` | partial | 256k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/doubao-seed-2-0-lite` | unknown | — | Coding Plan 概述列出该模型，但没有其窗口整数或标称值；不能继承 API 日期版。 |
| `ark/coding-plan-cn/minimax-m3` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/glm-5-3` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/glm-5-3-flash` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/deepseek-v4-flash` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/deepseek-v4-pro` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/kimi-k2-7-code` | partial | 256k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `ark/coding-plan-cn/kimi-k3` | partial | 1024k | Coding Plan 自身规格；工具使用长窗口可能需 [1m] 设置，客户端压缩阈值不能替代服务窗口。 官方窗口原文为 1024k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `bailian/api-cn/qwen3-8-max-prime` | unknown | — | 公开模型中心按精确请求 ID 查询未返回本型号；不是模型下线证明，也不套 qwen3.8-max 的窗口。 |
| `bailian/token-plan-cn/qwen3-8-max` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/qwen3-8-flash` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/qwen3-7-plus` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/deepseek-v4-pro` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/deepseek-v4-flash` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/kimi-k2-7-code` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/kimi-k2-6` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/glm-5-2` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/glm-5-1` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `bailian/token-plan-cn/glm-5` | unknown | — | Token Plan 团队版型号表及 FAQ 未列逐型号上下文长度；未从百炼 API、Coding Plan 或原厂继承。 |
| `chenyu-ai/api/deepseek-v4-pro` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/deepseek-v4-flash` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/deepseek-v4-flash-vision-exp` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seed-2-1-pro-260628` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seed-2-1-turbo-260628` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seed-2-0-lite-260428` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seed-2-0-mini-260428` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seed-2-0-pro-260215` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seedream-5-0-pro-260628` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seedream-5-0-260128` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seedance-2-5-260628` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seedance-2-0-260128` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/doubao-seedance-2-0-mini-260615` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen3-8-max` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen3-7-plus` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen3-8-flash` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen3-7-flash` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen3-8-27b` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/wan3-0-video` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/wan3-0-video-prime` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/minimax-m3` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/minimax-h3` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/speech-2-8-hd` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/speech-2-8-turbo` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/glm-5-3` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/glm-5-3-flash` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/kimi-k3` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/qwen-qwen3-8-27b-fp8` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `chenyu-ai/api/nvidia-qwen3-6-35b-a3b-nvfp4` | unknown | — | 公开模型文档和公开目录均连接超时，未取得本平台逐型号窗口。未读内部渠道、数据库或部署配置，不以采购方或开源权重规格补值。 |
| `cursor/individual/composer-2-5` | partial | 200k | 记录本产品常规 Context window；Max context 原文为 -，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 200k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/grok-4-6` | partial | 256k | 记录本产品常规 Context window；Max context 原文为 -，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/grok-4-5` | partial | 256k | 记录本产品常规 Context window；Max context 原文为 -，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/claude-fable-5-1` | partial | 300k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 300k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/claude-opus-5` | partial | 300k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 300k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/claude-sonnet-5` | partial | 200k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 200k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/gemini-3-1-pro` | partial | 200k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 200k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/gemini-3-8-flash` | partial | 200k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 200k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/gpt-5-6-luna` | partial | 272k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 272k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/gpt-5-6-sol` | partial | 272k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 272k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/gpt-5-6-terra` | partial | 272k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 272k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `cursor/individual/muse-spark-1-3` | partial | 300k | 记录本产品常规 Context window；Max context 原文为 1M，不能拿最大模式替换常规窗口，也不能抄原厂 API。 官方窗口原文为 300k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `deepseek/api-cn/deepseek-flash` | partial | 1M | 原厂 API 型号表；旧 Flash 请求名由脚注明确接受并转到当前 Flash，不是猜测别名。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 1048576 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `deepseek/api-cn/deepseek-v4-pro` | partial | 1M | 原厂 API 型号表；旧 Flash 请求名由脚注明确接受并转到当前 Flash，不是猜测别名。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 1048576 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `deepseek/api-cn/deepseek-v4-flash` | partial | 1M | 原厂 API 型号表；旧 Flash 请求名由脚注明确接受并转到当前 Flash，不是猜测别名。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 1048576 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `deepseek/api-cn/deepseek-v4-flash-vision-exp` | partial | 1M | 原厂 API 型号表；旧 Flash 请求名由脚注明确接受并转到当前 Flash，不是猜测别名。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 1048576 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `gemini/api-global/gemini-3-7-flash` | unknown | — | 官方只列 Input token limit=1048576、Output token limit=65536，未明确二者合计的总上下文窗口；旧 context_window_tokens=1048576 混用了输入上限，本轮清空；最大输出保留。 |
| `hunyuan/api-cn/hy4-preview` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/hy3` | partial | 256k | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/hy-mt2-pro` | partial | 8k | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 8k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/hy-vision-2-0-instruct` | partial | 44k | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 44k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/deepseek-v4-pro-0813` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/deepseek-v4-flash-0731` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/glm-5-3` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/kimi-k3` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `hunyuan/api-cn/minimax-m3` | partial | 1M | 腾讯 TokenHub 对应型号行，不能把最大输入或第三方原厂参数作为窗口。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `minimax/token-plan-cn/minimax-m3` | partial | 1M | Token Plan 套餐页确认 M3 1M 长上下文；与 API 的整数窗口分别核对。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `minimax/token-plan-cn/minimax-m2-7` | unknown | — | 订阅资料确认支持 M2.7，但未列该型号订阅窗口；套餐页泛称 1M 不能覆盖 M2.7，也不能直接继承 API 的 204800。 |
| `mistral/api-global/mistral-large-latest` | partial | 256k | 官方配置页 latest 别名分别指向 Large 3 / Small 4；托管型号页公布 256k，不使用开源权重配置补整数。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `mistral/api-global/mistral-small-latest` | partial | 256k | 官方配置页 latest 别名分别指向 Large 3 / Small 4；托管型号页公布 256k，不使用开源权重配置补整数。 官方窗口原文为 256k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `moonshot/api-cn/kimi-k3` | partial | 1M | API 文档标称 1M；max_completion_tokens=1048576 是输出参数上限，不能作为总窗口的整数证明。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 1048576 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `moonshot/api-cn/kimi-k2-7-code` | partial | 256K | API 文档明确列出这三个型号各有 256K；订阅 Kimi Code 的整数不能自动证明本产品整数边界。 官方窗口原文为 256K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 262144 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `moonshot/api-cn/kimi-k2-7-code-highspeed` | partial | 256K | API 文档明确列出这三个型号各有 256K；订阅 Kimi Code 的整数不能自动证明本产品整数边界。 官方窗口原文为 256K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 262144 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `moonshot/api-cn/kimi-k2-6` | partial | 256K | API 文档明确列出这三个型号各有 256K；订阅 Kimi Code 的整数不能自动证明本产品整数边界。 官方窗口原文为 256K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 历史整数 262144 保留供追溯，当前来源未能独立复核其精确值，不能视为本轮已确认。 |
| `openai/codex/gpt-5-3-codex-spark` | unknown | — | Codex 文档有 Spark 型号，但未列窗口；本次 CLI 0.154.0 内嵌目录没有该精确 slug，不能用其他 Codex 型号或 API 规格补齐。 |
| `qianfan/api-cn/ernie-5-1` | partial | 128k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/ernie-5-0` | partial | 128k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/ernie-4-5-turbo-128k` | partial | 128k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/ernie-4-5-turbo-vl-32k` | partial | 32k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 32k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/deepseek-v4-pro` | partial | 1M | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/deepseek-v4-flash` | partial | 1M | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/glm-5-3` | partial | 1M | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/ernie-4-5-turbo-20260402` | partial | 128k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 128k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `qianfan/api-cn/glm-5-1` | partial | 198k | 千帆精确 model 参数所在行，最大输入与最大输出另列；不从价格短名映射推导。 官方窗口原文为 198k；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `xai/grok-build/grok-4-6` | unknown | — | Grok Build 配置文档只解释 context_window 可配置并用于压缩，没有给出精确型号的内置窗口；API 500000 不能自动继承。 |
| `xai/grok-build/grok-4-5` | unknown | — | Grok Build 配置文档只解释 context_window 可配置并用于压缩，没有给出精确型号的内置窗口；API 500000 不能自动继承。 |
| `zhipu/api-cn/glm-5-3` | partial | 1M | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5-3-flash` | partial | 1M | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5-2` | partial | 1M | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5-1` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5-turbo` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-7` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-7-flashx` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-7-flash` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-5-air` | partial | 128K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 128K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-5v-turbo` | partial | 200K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 200K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-6v` | partial | 128K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 128K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/api-cn/glm-4-6v-flash` | partial | 128K | 智谱国内 API 型号表；不把百炼 Coding Plan 的 202752 或原厂权重配置当作本产品值。 官方窗口原文为 128K；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/coding-plan-cn/glm-5-3` | partial | 1M | Coding Plan 文档针对 GLM-5.3 / GLM-5.3-Flash 要求 [1m] 后缀；配置示例 1000000 是 CLAUDE_CODE_AUTO_COMPACT_WINDOW 压缩阈值，不能据此确认服务窗口整数。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |
| `zhipu/coding-plan-cn/glm-5-3-flash` | partial | 1M | Coding Plan 文档针对 GLM-5.3 / GLM-5.3-Flash 要求 [1m] 后缀；配置示例 1000000 是 CLAUDE_CODE_AUTO_COMPACT_WINDOW 压缩阈值，不能据此确认服务窗口整数。 官方窗口原文为 1M；本次未找到精确整数及缩写换算依据，不自行把 K/M 乘以 1000 或 1024。 |

## 检查与交付

validate 通过，66 项单元测试通过，git diff --check 通过；已逐模型比较并确认除上下文字段之外的数据与基线一致。相对基线的候选审阅包由本轮工作生成；完整变更与候选哈希在 `.review/`。本文件不是正式数据发布。每家 `evidence/<provider>/2026-09-16-context.md` 记录 URL、UTC 获取时间、位置和逐模型结论。
