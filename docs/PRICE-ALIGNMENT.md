# 当前价格对齐结果

更新日期：2026-09-16。用户明确指定的估价规则优先于首轮核对方案。

## 当前结果

- 20家服务商、30个产品、216条模型。
- 71条订阅模型中70条已有参考价；K2.8 Preview按用户指定参考K2.7 Code，新增Codex Spark未查到对应公开按量价，保留unknown。
- 5条方舟/千帆API短名已对齐最新日期版本。
- 共186条有唯一价格基准，剩余30条：晨羽平台29条公开价目未取得、Codex Spark 1条参考价未知。
- 已删除6条模型；排除项写入provider.json，校验器阻止重新导入。SiliconFlow任何retired记录均无法通过校验。

## 固定口径

订阅模型不核对实际扣费、AFP/CREDIT或套餐池消耗；全部保存reference_prices，usage_prices固定not_applicable。

参考顺序：同平台对应型号的按量价 → 开发该模型的源头公司的公开按量价。先查同平台完整官方价表，不以本仓库部分API清单判断有无价格。独立复制数字与来源，不在运行时继承。

Claude日期版Haiku按claude-haiku-4-5；方舟Seedance 2.5/2.0/2.0-fast分别对齐260628/260128/fast-260128，千帆DeepSeek Pro/Flash分别对齐0813/0731。后续发现多个同系列日期版本，选择实际日期最新的一版。映射用于估价，不声明官方路由别名或真实调用可用性。

Codex与GLM Coding Plan原先保存的积分单价已移除，统一改用本平台API现金价格。既有套餐资料独立保留，不参与本流程的模型估价。

## 删除与禁止再收录

| 平台 | 请求ID | 处理 |
| --- | --- | --- |
| OpenRouter | `~openai/gpt-latest` | 用户指定排除，即使再次发现也不自动加入 |
| Together | `openai/gpt-oss-20b` | 同上 |
| Groq | `llama-3.3-70b-versatile` | 同上 |
| SiliconFlow | `Qwen/Qwen3.5-397B-A17B` | 已下线，删除并登记排除 |
| SiliconFlow | `MiniMaxAI/MiniMax-M2.5` | 同上 |
| SiliconFlow | `Pro/zai-org/GLM-4.7` | 同上 |

SiliconFlow今后所有确认下线的模型都剔除，并加入排除清单；不在当前catalog保存历史retired行。

## 用户指定的订阅参考价

kimi-for-coding当前对应K2.8 Preview。同平台就是模型开发方Moonshot；其公开按量表目前只列K3、K2.7 Code、K2.7 Code Highspeed、K2.6。两级来源都没有K2.8报价。用户已明确指定按Kimi K2.7 Code做示意：每百万token未缓存输入6.5元、缓存输入1.3元、输出27元。记录为reference，不改动K2.8 Preview身份，不声明官方同价。

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

各家本轮证据在`evidence/<provider>/2026-09-16-alignment.md`，记录官方URL、抓取时间、参考对象、原厂回退原因和数值。首轮审计文件为历史快照，当前状态以本页与catalog为准。

2026-09-16 订阅补漏：Claude Code新增Fable 5.1；Codex新增GPT-5.5与GPT-5.3-Codex-Spark；Cursor从1项补至12项，按各官方详情页补上请求ID。已有模型的数字价格与所有套餐/额度未改。新增证据为各家 `2026-09-16-subscription-completeness.md`。
