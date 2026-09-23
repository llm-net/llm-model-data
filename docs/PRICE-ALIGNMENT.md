# 当前价格对齐结果

更新日期：2026-09-23。用户明确指定的估价规则优先于首轮核对方案。

## 当前结果

- 19家服务商、29个产品、259条模型。
- 114条订阅模型中113条已有参考价；K2.8 Preview按用户指定参考K2.7 Code；Codex Spark 在同平台与开发方 OpenAI 均无公开按量价，保留unknown。
- 6条方舟/千帆API短名已对齐最新日期版本。
- 共258条有唯一价格基准，剩余 Codex Spark 1条参考价未知。
- 2026-09-23：新增 OpenCode Go（31条，全部按源头厂商官网价）、Claude Opus 5.5（API 与 Claude Code）、Codex GPT-6 Sol / Luna、Cursor 7个请求 ID（Grok 4.7、Composer 2.5 Fast、Opus 5.5 及 Fast、GPT-5.6 三个 Fast），Grok Build 的 Grok 4.7 Fast 由 unknown 改为 xAI 官网 Fast 费率。已有型号数字价格与套餐 / 额度未改，见 [Anthropic](../evidence/anthropic/2026-09-23-claude-opus-5-5.md)、[Codex](../evidence/openai/2026-09-23-codex-gpt-6.md)、[Cursor](../evidence/cursor/2026-09-23-models.md)、[Grok Build](../evidence/xai/2026-09-23-grok-47-fast.md)、[OpenCode Go](../evidence/opencode/2026-09-23-go.md)。
- 本轮整家删除硅基流动（6条模型）和 Together AI（1条模型）；schemas/excluded-providers.json 阻止重新导入。此前逐型号排除的历史仍见下表。
- 晨羽AI 30条按本平台匿名公开接口的人民币价格独立保存，见 [2026-09-17 核对记录](../evidence/chenyu-ai/2026-09-17-public-models.md) 与 [思考补充核对](../evidence/chenyu-ai/2026-09-17-reasoning.md)。其余服务商专项历史结果见 [PROTOCOL-AUDIT-2026-09-16.md](PROTOCOL-AUDIT-2026-09-16.md)。

## 固定口径

订阅模型不核对实际扣费、AFP/CREDIT或套餐池消耗；全部保存reference_prices，usage_prices固定not_applicable。

参考顺序：同平台对应型号的按量价 → 开发该模型的源头公司的公开按量价。先查同平台完整官方价表，不以本仓库部分API清单判断有无价格。独立复制数字与来源，不在运行时继承。

Claude日期版Haiku按claude-haiku-4-5；方舟Seedance 2.5/2.0/2.0-fast分别对齐260628/260128/fast-260128，千帆DeepSeek Pro/Flash分别对齐0813/0731。后续发现多个同系列日期版本，选择实际日期最新的一版。映射用于估价，不声明官方路由别名或真实调用可用性。

Codex与GLM Coding Plan原先保存的积分单价已移除，统一改用本平台API现金价格。既有套餐资料独立保留，不参与本流程的模型估价。

## 删除与禁止再收录

| 平台 | 请求ID | 处理 |
| --- | --- | --- |
| OpenRouter | `~openai/gpt-latest` | 用户指定排除，即使再次发现也不自动加入 |
| Together | 全部 | 整家排除，包含此前单独排除的 openai/gpt-oss-20b |
| Groq | `llama-3.3-70b-versatile` | 同上 |
| SiliconFlow | 全部 | 整家排除，历史下线条目不再逐条恢复 |

硅基流动与 Together AI 整家排除，包括仍在服务的模型；旧下线记录只保留在 Git 历史与证据中。

## 用户指定的订阅参考价

kimi-for-coding当前对应K2.8 Preview。同平台就是模型开发方Moonshot；其公开按量表目前只列K3、K2.7 Code、K2.7 Code Highspeed、K2.6。两级来源都没有K2.8报价。用户已明确指定按Kimi K2.7 Code做示意：每百万token未缓存输入6.5元、缓存输入1.3元、输出27元。记录为reference，不改动K2.8 Preview身份，不声明官方同价。

## 用户指定：订阅缺价按源头厂商官网对齐

用户明确要求订阅里缺价的型号去模型源头厂商官网对齐价格：

- OpenCode Go 全部型号取开发方官网公开按量价：中国厂商取其国内官网人民币价，Grok / GPT / Muse 取开发方美元价，不换汇。Go 文档的 token 价是用量上限扣减换算表，Zen 是另一套按量余额，均不作为参考价。开发方按量目录已收录的型号保存 `catalog_model`；DeepSeek V4.1 Flash 参考 `deepseek-flash`。促销价、长上下文档与缓存写入限免不进基准。
- Grok Build 的 `grok-4.7-build-fast` 取 xAI 官网单列的 Grok 4.7 Fast 费率（同一模型的更快服务档，只在 Cursor 与 Grok Build 提供，公开 API 无此型号）。
- Cursor 新增条目仍按同平台 Cursor 公开价；Composer 由 Cursor 开发，同平台价即开发方价。

## 完整对齐表

表内金额均保存原币种和计费单位；未列缓存等分量不等于免费。每行只是一组按量参考价，不是订阅真实扣款。

| 平台 / 产品 | 当前型号 | 按量参考对象 | 唯一基准 |
| --- | --- | --- | --- |
| anthropic/claude-code | `claude-fable-5` | `claude-fable-5` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=1/1000000 token, output_tokens=50/1000000 token |
| anthropic/claude-code | `claude-opus-5` | `claude-opus-5` | USD input_uncached_tokens=5/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=25/1000000 token, cache_write_5m_tokens=6.25/1000000 token |
| anthropic/claude-code | `claude-sonnet-5` | `claude-sonnet-5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=10/1000000 token, cache_write_5m_tokens=2.5/1000000 token |
| anthropic/claude-code | `claude-haiku-4-5` | `claude-haiku-4-5` | USD input_uncached_tokens=1/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=5/1000000 token, cache_write_5m_tokens=1.25/1000000 token |
| anthropic/claude-code | `claude-haiku-4-5-20251001` | `claude-haiku-4-5` | USD input_uncached_tokens=1/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=5/1000000 token, cache_write_5m_tokens=1.25/1000000 token |
| ark/agent-plan-cn | `deepseek-v4-pro` | `deepseek-v4-pro-ga-260813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=27/1000000 token |
| ark/agent-plan-cn | `deepseek-v4-flash` | `deepseek-v4-flash-ga-260731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.10/1000000 token, output_tokens=9/1000000 token |
| ark/agent-plan-cn | `doubao-seedance-2.5` | `doubao-seedance-2-5-260628` | CNY video_output_tokens=70/1000000 token |
| ark/agent-plan-cn | `doubao-seedance-2.0` | `doubao-seedance-2-0-260128` | CNY video_output_tokens=46/1000000 token |
| ark/agent-plan-cn | `doubao-seedance-2.0-fast` | `doubao-seedance-2-0-fast-260128` | CNY video_output_tokens=37/1000000 token |
| ark/agent-plan-cn | `doubao-seedance-2.0-mini` | `doubao-seedance-2-0-mini-260615` | CNY video_output_tokens=23/1000000 token |
| ark/agent-plan-cn | `doubao-seedream-5.0-lite` | `doubao-seedream-5-0-260128` | CNY generated_images=0.22/1 image |
| ark/api-cn | `doubao-seedance-2.5` | `doubao-seedance-2-5-260628` | CNY video_output_tokens=70/1000000 token |
| ark/api-cn | `doubao-seedance-2.0` | `doubao-seedance-2-0-260128` | CNY video_output_tokens=46/1000000 token |
| ark/api-cn | `doubao-seedance-2.0-fast` | `doubao-seedance-2-0-fast-260128` | CNY video_output_tokens=37/1000000 token |
| ark/coding-plan-cn | `doubao-seed-evolving` | `doubao-seed-evolving` | CNY input_uncached_tokens=6/1000000 token, input_cached_tokens=1.2/1000000 token, output_tokens=30/1000000 token |
| ark/coding-plan-cn | `doubao-seed-2.1-turbo` | `doubao-seed-2-1-turbo-260628` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.6/1000000 token, output_tokens=15/1000000 token |
| ark/coding-plan-cn | `doubao-seed-2.0-lite` | `doubao-seed-2-0-lite-260428` | CNY input_uncached_tokens=0.6/1000000 token, input_cached_tokens=0.12/1000000 token, output_tokens=3.6/1000000 token |
| ark/coding-plan-cn | `minimax-m3` | `MiniMax-M3` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token |
| ark/coding-plan-cn | `glm-5.3` | `glm-5.3` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token |
| ark/coding-plan-cn | `glm-5.3-flash` | `glm-5.3-flash` | CNY input_uncached_tokens=0.8/1000000 token, input_cached_tokens=0.23/1000000 token, output_tokens=2.8/1000000 token |
| ark/coding-plan-cn | `deepseek-v4-flash` | `deepseek-v4-flash-ga-260731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.10/1000000 token, output_tokens=9/1000000 token |
| ark/coding-plan-cn | `deepseek-v4-pro` | `deepseek-v4-pro-ga-260813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=27/1000000 token |
| ark/coding-plan-cn | `kimi-k2.7-code` | `kimi-k2.7-code` | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=27/1000000 token |
| ark/coding-plan-cn | `kimi-k3` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token |
| bailian/coding-plan-cn | `qwen3.7-plus` | `qwen3.7-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=8/1000000 token |
| bailian/coding-plan-cn | `qwen3.6-plus` | `qwen3.6-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=12/1000000 token |
| bailian/coding-plan-cn | `kimi-k2.5` | `kimi-k2.5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=21/1000000 token |
| bailian/coding-plan-cn | `glm-5` | `glm-5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=18/1000000 token |
| bailian/coding-plan-cn | `MiniMax-M2.5` | `MiniMax-M2.5` | CNY input_uncached_tokens=2.1/1000000 token, output_tokens=8.4/1000000 token |
| bailian/coding-plan-cn | `qwen3.5-plus` | `qwen3.5-plus` | CNY input_uncached_tokens=0.8/1000000 token, output_tokens=4.8/1000000 token |
| bailian/coding-plan-cn | `qwen3-max-2026-01-23` | `qwen3-max-2026-01-23` | CNY input_uncached_tokens=2.5/1000000 token, output_tokens=10/1000000 token |
| bailian/coding-plan-cn | `qwen3-coder-next` | `qwen3-coder-next` | CNY input_uncached_tokens=1/1000000 token, output_tokens=4/1000000 token |
| bailian/coding-plan-cn | `qwen3-coder-plus` | `qwen3-coder-plus` | CNY input_uncached_tokens=4/1000000 token, output_tokens=16/1000000 token |
| bailian/coding-plan-cn | `glm-4.7` | `glm-4.7` | CNY input_uncached_tokens=3/1000000 token, output_tokens=14/1000000 token |
| bailian/token-plan-cn | `qwen3.8-max` | `qwen3.8-max` | CNY input_uncached_tokens=12/1000000 token, output_tokens=36/1000000 token |
| bailian/token-plan-cn | `qwen3.8-flash` | `qwen3.8-flash` | CNY input_uncached_tokens=0.8/1000000 token, output_tokens=2.7/1000000 token |
| bailian/token-plan-cn | `qwen3.7-plus` | `qwen3.7-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=8/1000000 token |
| bailian/token-plan-cn | `deepseek-v4-pro` | `deepseek-v4-pro` | CNY input_uncached_tokens=12/1000000 token, output_tokens=24/1000000 token |
| bailian/token-plan-cn | `deepseek-v4-flash` | `deepseek-v4-flash` | CNY input_uncached_tokens=1/1000000 token, output_tokens=2/1000000 token |
| bailian/token-plan-cn | `kimi-k2.7-code` | `kimi-k2.7-code` | CNY input_uncached_tokens=6.5/1000000 token, output_tokens=27/1000000 token |
| bailian/token-plan-cn | `kimi-k2.6` | `kimi-k2.6` | CNY input_uncached_tokens=6.5/1000000 token, output_tokens=27/1000000 token |
| bailian/token-plan-cn | `glm-5.2` | `glm-5.2` | CNY input_uncached_tokens=8/1000000 token, output_tokens=28/1000000 token |
| bailian/token-plan-cn | `glm-5.1` | `glm-5.1` | CNY input_uncached_tokens=6/1000000 token, output_tokens=24/1000000 token |
| bailian/token-plan-cn | `glm-5` | `glm-5` | CNY input_uncached_tokens=4/1000000 token, output_tokens=18/1000000 token |
| cursor/individual | `composer-2.5` | `composer-2.5` | USD input_uncached_tokens=0.5/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=2.5/1000000 token |
| minimax/token-plan-cn | `MiniMax-M3` | `MiniMax-M3` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token |
| minimax/token-plan-cn | `MiniMax-M2.7` | `MiniMax-M2.7` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token |
| moonshot/kimi-code | `k3` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token |
| moonshot/kimi-code | `k3-256k` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token |
| moonshot/kimi-code | `kimi-for-coding` | `kimi-k2.7-code`（用户指定近似参考） | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=27/1000000 token |
| moonshot/kimi-code | `kimi-for-coding-highspeed` | `kimi-k2.7-code-highspeed` | CNY input_uncached_tokens=13/1000000 token, input_cached_tokens=2.6/1000000 token, output_tokens=54/1000000 token |
| openai/codex | `gpt-6-astra` | `gpt-6-astra` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=1/1000000 token, output_tokens=50/1000000 token |
| openai/codex | `gpt-5.6-sol` | `gpt-5.6-sol` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.4/1000000 token, output_tokens=20/1000000 token |
| openai/codex | `gpt-5.6-terra` | `gpt-5.6-terra` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=12/1000000 token |
| openai/codex | `gpt-5.6-luna` | `gpt-5.6-luna` | USD input_uncached_tokens=0.2/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=1.2/1000000 token |
| qianfan/api-cn | `deepseek-v4-pro` | `deepseek-v4-pro-0813` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.3/1000000 token, output_tokens=27/1000000 token |
| qianfan/api-cn | `deepseek-v4-flash` | `deepseek-v4-flash-0731` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=9/1000000 token |
| xai/grok-build | `grok-4.6` | `grok-4.6` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| xai/grok-build | `grok-4.5` | `grok-4.5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=6/1000000 token |
| zhipu/coding-plan-cn | `glm-5.3` | `glm-5.3` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token |
| zhipu/coding-plan-cn | `glm-5.3-flash` | `glm-5.3-flash` | CNY input_uncached_tokens=0.8/1000000 token, input_cached_tokens=0.23/1000000 token, output_tokens=2.8/1000000 token |

| anthropic/claude-code | `claude-fable-5-1` | `claude-fable-5-1` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=0.25/1000000 token, output_tokens=50/1000000 token, cache_write_5m_tokens=12.5/1000000 token |
| openai/codex | `gpt-5.5` | `gpt-5.5` | USD input_uncached_tokens=5/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=30/1000000 token |
| openai/codex | `gpt-5.3-codex-spark` | `未知` | unknown：未查到对应型号公开按量价 |
| cursor/individual | `grok-4.6` | `grok-4.6` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| cursor/individual | `grok-4.5` | `grok-4.5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| cursor/individual | `claude-fable-5-1` | `claude-fable-5-1` | USD input_uncached_tokens=10/1000000 token, input_cached_tokens=0.25/1000000 token, output_tokens=50/1000000 token |
| cursor/individual | `claude-opus-5` | `claude-opus-5` | USD input_uncached_tokens=5/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=25/1000000 token |
| cursor/individual | `claude-sonnet-5` | `claude-sonnet-5` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=10/1000000 token |
| cursor/individual | `gemini-3.1-pro` | `gemini-3.1-pro` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=12/1000000 token |
| cursor/individual | `gemini-3.8-flash` | `gemini-3.8-flash` | USD input_uncached_tokens=0.75/1000000 token, input_cached_tokens=0.075/1000000 token, output_tokens=3.5/1000000 token |
| cursor/individual | `gpt-5.6-luna` | `gpt-5.6-luna` | USD input_uncached_tokens=0.2/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=1.2/1000000 token |
| cursor/individual | `gpt-5.6-sol` | `gpt-5.6-sol` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.4/1000000 token, output_tokens=20/1000000 token |
| cursor/individual | `gpt-5.6-terra` | `gpt-5.6-terra` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=12/1000000 token |
| cursor/individual | `muse-spark-1.3` | `muse-spark-1.3` | USD input_uncached_tokens=1.25/1000000 token, input_cached_tokens=0.15/1000000 token, output_tokens=4.25/1000000 token |
| anthropic/claude-code | `claude-opus-5-5` | `claude-opus-5-5` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=20/1000000 token, cache_write_5m_tokens=5/1000000 token |
| openai/codex | `gpt-6-sol` | `gpt-6-sol` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=10/1000000 token |
| openai/codex | `gpt-6-luna` | `gpt-6-luna` | USD input_uncached_tokens=0.1/1000000 token, input_cached_tokens=0.01/1000000 token, output_tokens=0.5/1000000 token |
| cursor/individual | `grok-4.7` | `grok-4.7` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| cursor/individual | `composer-2.5-fast` | `Composer 2.5 (Fast)` | USD input_uncached_tokens=3/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=15/1000000 token |
| cursor/individual | `claude-opus-5-5` | `Claude Opus 5.5` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.2/1000000 token, output_tokens=20/1000000 token, cache_write_5m_tokens=5/1000000 token |
| cursor/individual | `claude-opus-5-5-fast` | `Claude Opus 5.5 (Fast Mode)` | USD input_uncached_tokens=8/1000000 token, input_cached_tokens=0.4/1000000 token, output_tokens=40/1000000 token, cache_write_5m_tokens=10/1000000 token |
| cursor/individual | `gpt-5.6-sol-fast` | `gpt-5.6-sol-fast` | USD input_uncached_tokens=8/1000000 token, input_cached_tokens=0.8/1000000 token, output_tokens=40/1000000 token |
| cursor/individual | `gpt-5.6-terra-fast` | `gpt-5.6-terra-fast` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=0.4/1000000 token, output_tokens=24/1000000 token |
| cursor/individual | `gpt-5.6-luna-fast` | `gpt-5.6-luna-fast` | USD input_uncached_tokens=0.4/1000000 token, input_cached_tokens=0.04/1000000 token, output_tokens=2.4/1000000 token |
| xai/grok-build | `grok-4.7-build-fast` | `Grok 4.7 Fast` | USD input_uncached_tokens=4/1000000 token, input_cached_tokens=1/1000000 token, output_tokens=12/1000000 token |
| opencode/go | `kimi-k3` | `kimi-k3` | CNY input_uncached_tokens=20/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=100/1000000 token |
| opencode/go | `kimi-k2.7-code` | `kimi-k2-7-code` | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=27/1000000 token |
| opencode/go | `kimi-k2.6` | `kimi-k2-6` | CNY input_uncached_tokens=6.5/1000000 token, input_cached_tokens=1.1/1000000 token, output_tokens=27/1000000 token |
| opencode/go | `glm-5.3` | `glm-5-3` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token |
| opencode/go | `glm-5.3-flash` | `glm-5-3-flash` | CNY input_uncached_tokens=0.8/1000000 token, input_cached_tokens=0.23/1000000 token, output_tokens=2.8/1000000 token |
| opencode/go | `glm-5.2` | `glm-5-2` | CNY input_uncached_tokens=8/1000000 token, input_cached_tokens=2/1000000 token, output_tokens=28/1000000 token |
| opencode/go | `glm-5.1` | `glm-5-1` | CNY input_uncached_tokens=6/1000000 token, input_cached_tokens=1.3/1000000 token, output_tokens=24/1000000 token |
| opencode/go | `deepseek-v4.1-flash` | `deepseek-flash` | CNY input_uncached_tokens=2/1000000 token, input_cached_tokens=0.04/1000000 token, output_tokens=8/1000000 token（峰时首档，另有谷时） |
| opencode/go | `deepseek-v4-pro` | `deepseek-v4-pro` | CNY input_uncached_tokens=9/1000000 token, input_cached_tokens=0.30/1000000 token, output_tokens=27/1000000 token（峰时首档，另有谷时） |
| opencode/go | `deepseek-v4-flash` | `deepseek-v4-flash` | CNY input_uncached_tokens=2/1000000 token, input_cached_tokens=0.04/1000000 token, output_tokens=8/1000000 token（峰时首档，另有谷时） |
| opencode/go | `deepseek-v4-flash-vision-exp` | `deepseek-v4-flash-vision-exp` | CNY input_uncached_tokens=2/1000000 token, input_cached_tokens=0.04/1000000 token, output_tokens=8/1000000 token（峰时首档，另有谷时） |
| opencode/go | `qwen3.8-max` | `qwen3-8-max` | CNY input_uncached_tokens=12/1000000 token, output_tokens=36/1000000 token |
| opencode/go | `qwen3.8-flash` | `qwen3-8-flash` | CNY input_uncached_tokens=0.8/1000000 token, output_tokens=2.7/1000000 token |
| opencode/go | `qwen3.7-max` | `qwen3.7-max` | CNY input_uncached_tokens=12/1000000 token, output_tokens=36/1000000 token |
| opencode/go | `qwen3.7-plus` | `qwen3-7-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=8/1000000 token |
| opencode/go | `qwen3.6-plus` | `qwen3.6-plus` | CNY input_uncached_tokens=2/1000000 token, output_tokens=12/1000000 token |
| opencode/go | `minimax-m3` | `minimax-m3` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token |
| opencode/go | `minimax-m2.7` | `minimax-m2-7` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.42/1000000 token, output_tokens=8.4/1000000 token |
| opencode/go | `minimax-m2.5` | `MiniMax-M2.5` | CNY input_uncached_tokens=2.1/1000000 token, input_cached_tokens=0.21/1000000 token, output_tokens=8.4/1000000 token, cache_write_5m_tokens=2.625/1000000 token |
| opencode/go | `mimo-v2.6-pro` | `mimo-v2.6-pro` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.025/1000000 token, output_tokens=6/1000000 token |
| opencode/go | `mimo-v2.6-flash` | `mimo-v2.6-flash` | CNY input_uncached_tokens=1/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=2/1000000 token |
| opencode/go | `mimo-v2.5-pro` | `mimo-v2.5-pro` | CNY input_uncached_tokens=3/1000000 token, input_cached_tokens=0.025/1000000 token, output_tokens=6/1000000 token |
| opencode/go | `mimo-v2.5` | `mimo-v2.5` | CNY input_uncached_tokens=1/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=2/1000000 token |
| opencode/go | `longcat-2.0` | `LongCat-2.0` | CNY input_uncached_tokens=5/1000000 token, input_cached_tokens=0.1/1000000 token, output_tokens=20/1000000 token |
| opencode/go | `hy4-preview` | `hy4-preview` | CNY input_uncached_tokens=6/1000000 token, input_cached_tokens=0.3/1000000 token, output_tokens=18/1000000 token |
| opencode/go | `hy3` | `hy3` | CNY input_uncached_tokens=1/1000000 token, input_cached_tokens=0.25/1000000 token, output_tokens=4/1000000 token |
| opencode/go | `gpt-5.6-luna` | `gpt-5.6-luna` | USD input_uncached_tokens=0.2/1000000 token, input_cached_tokens=0.02/1000000 token, output_tokens=1.2/1000000 token |
| opencode/go | `grok-4.7` | `grok-4-7` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| opencode/go | `grok-4.6` | `grok-4-6` | USD input_uncached_tokens=2/1000000 token, input_cached_tokens=0.5/1000000 token, output_tokens=6/1000000 token |
| opencode/go | `muse-spark-1.3-contributor` | `muse-spark-1.3-contributor` | USD input_uncached_tokens=0.10/1000000 token, input_cached_tokens=0.002/1000000 token, output_tokens=0.20/1000000 token |
| opencode/go | `muse-spark-1.2-contributor` | `muse-spark-1.2-contributor` | USD input_uncached_tokens=0.10/1000000 token, input_cached_tokens=0.002/1000000 token, output_tokens=0.20/1000000 token |

各家本轮证据在`evidence/<provider>/2026-09-16-alignment.md`，记录官方URL、抓取时间、参考对象、原厂回退原因和数值。首轮审计文件为历史快照，当前状态以本页与catalog为准。

2026-09-16 订阅补漏：Claude Code新增Fable 5.1；Codex新增GPT-5.5与GPT-5.3-Codex-Spark；Cursor从1项补至12项，按各官方详情页补上请求ID。已有模型的数字价格与所有套餐/额度未改。新增证据为各家 `2026-09-16-subscription-completeness.md`。

## Fable / Seedance 补漏与名称兼容

新增 Anthropic API 的 Fable 5.1、Fable 5，补 Claude Code Fable 5 的 5 分钟缓存写入 12.5 USD/百万 token；其余已有金额不变。新增方舟 Fast 日期版与 Mini API 短名参考记录。Seedance 的 70/46/37/23 CNY 每百万视频 token 标准基准不变，明确在线 720p 无参考视频、非促销与成功计费。

新增结构化来源身份与精确查找，阻止同名跨平台/产品匹配、短名漏同步、跨 Fast/Mini 系列套价。Mini API 短名 request_id 未证实，保留 null；已有三个 API 短名改为身份 needs_review / 协议 partial，历史请求名保留，不声称可调用。Fable API 思考控制保留 partial；Seedance 思考均 unknown。其余全部缺项持续列入生成的审阅包。

来源：[Anthropic](../evidence/anthropic/2026-09-17-prices-and-names.md)、[方舟](../evidence/ark/2026-09-17-prices-and-names.md)。套餐与额度本次无变化；候选尚未正式发布，也未更新消费者。
