# 本轮工作区前后对照

> 首轮核对的历史快照。后续已按用户决定改为订阅按量参考价并删除排除项；当前数量和剩余缺项见[PRICE-ALIGNMENT.md](PRICE-ALIGNMENT.md)。

基线：本轮开始时保存的未提交工作区快照；不是已发布版本。金额均为原币种。

| 产品 / 模型 | 原模型状态 → 当前 | 原价格 → 当前唯一基准 |
| --- | --- | --- |
| anthropic/api-global/`claude-opus-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 5/1000000token, input_cached_tokens 0.5/1000000token, output_tokens 25/1000000token, cache_write_5m_tokens 6.25/1000000token |
| anthropic/api-global/`claude-sonnet-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 2/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 10/1000000token, cache_write_5m_tokens 2.5/1000000token |
| anthropic/api-global/`claude-haiku-4-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 1/1000000token, input_cached_tokens 0.1/1000000token, output_tokens 5/1000000token, cache_write_5m_tokens 1.25/1000000token |
| anthropic/claude-code/`claude-fable-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 10/1000000token, input_cached_tokens 1/1000000token, output_tokens 50/1000000token |
| anthropic/claude-code/`claude-opus-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 5/1000000token, input_cached_tokens 0.5/1000000token, output_tokens 25/1000000token |
| anthropic/claude-code/`claude-sonnet-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 2/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 10/1000000token |
| anthropic/claude-code/`claude-haiku-4-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 1/1000000token, input_cached_tokens 0.1/1000000token, output_tokens 5/1000000token |
| ark/agent-plan-cn/`deepseek-v4-pro` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`deepseek-v4-flash` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`doubao-seedance-2-5` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`doubao-seedance-2-0` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`doubao-seedance-2-0-fast` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`doubao-seedance-2-0-mini` | unknown → active | unknown → unknown |
| ark/agent-plan-cn/`doubao-seedream-5-0-lite` | unknown → active | unknown → unknown |
| ark/api-cn/`doubao-seed-evolving` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 1.2/1000000token, output_tokens 30/1000000token |
| ark/api-cn/`doubao-seed-2-1-pro-260628` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 1.2/1000000token, output_tokens 30/1000000token |
| ark/api-cn/`doubao-seed-2-1-turbo-260628` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.6/1000000token, output_tokens 15/1000000token |
| ark/api-cn/`doubao-seed-2-0-lite-260428` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.6/1000000token, input_cached_tokens 0.12/1000000token, output_tokens 3.6/1000000token |
| ark/api-cn/`doubao-seed-2-0-mini-260428` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 2/1000000token |
| ark/api-cn/`doubao-seed-2-0-pro-260215` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3.2/1000000token, input_cached_tokens 0.64/1000000token, output_tokens 16/1000000token |
| ark/api-cn/`doubao-seed-2-0-lite-260215` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.6/1000000token, input_cached_tokens 0.12/1000000token, output_tokens 3.6/1000000token |
| ark/api-cn/`doubao-seed-2-0-mini-260215` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 2/1000000token |
| ark/api-cn/`doubao-seed-2-0-code-preview-260215` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3.2/1000000token, input_cached_tokens 0.64/1000000token, output_tokens 16/1000000token |
| ark/api-cn/`doubao-seed-character-260628` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.16/1000000token, output_tokens 2/1000000token |
| ark/api-cn/`glm-5-2-260617` | unknown → active | unknown → baseline: CNY input_uncached_tokens 8/1000000token, input_cached_tokens 2/1000000token, output_tokens 28/1000000token |
| ark/api-cn/`deepseek-v4-pro-ga-260813` | unknown → active | unknown → baseline: CNY input_uncached_tokens 9/1000000token, input_cached_tokens 0.30/1000000token, output_tokens 27/1000000token |
| ark/api-cn/`deepseek-v4-flash-ga-260731` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.10/1000000token, output_tokens 9/1000000token |
| ark/api-cn/`deepseek-v4-pro-260425` | unknown → active | unknown → baseline: CNY input_uncached_tokens 9/1000000token, input_cached_tokens 0.30/1000000token, output_tokens 27/1000000token |
| ark/api-cn/`deepseek-v4-flash-260425` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.10/1000000token, output_tokens 9/1000000token |
| ark/api-cn/`doubao-seed-character-251128` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.16/1000000token, output_tokens 2/1000000token |
| ark/api-cn/`doubao-seed-translation-250915` | unknown → active | unknown → baseline: CNY input_uncached_tokens 1.2/1000000token, output_tokens 3.6/1000000token |
| ark/api-cn/`doubao-seedream-5-0-pro-260628` | unknown → active | unknown → baseline: CNY generated_images 0.30/1image, input_images 0.02/1image |
| ark/api-cn/`doubao-seedream-5-0-260128` | unknown → active | unknown → baseline: CNY generated_images 0.22/1image |
| ark/api-cn/`doubao-seedance-2-5-260628` | unknown → active | unknown → baseline: CNY video_output_tokens 70/1000000token |
| ark/api-cn/`doubao-seedance-2-0-260128` | unknown → active | unknown → baseline: CNY video_output_tokens 46/1000000token |
| ark/api-cn/`doubao-seedance-2-0-mini-260615` | unknown → active | unknown → baseline: CNY video_output_tokens 23/1000000token |
| ark/coding-plan-cn/`doubao-seed-evolving` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`doubao-seed-2-1-turbo` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`doubao-seed-2-0-lite` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`minimax-m3` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`glm-5-3` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`glm-5-3-flash` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`deepseek-v4-flash` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`deepseek-v4-pro` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`kimi-k2-7-code` | 未收录 → active | 未收录 → unknown |
| ark/coding-plan-cn/`kimi-k3` | 未收录 → active | 未收录 → unknown |
| bailian/api-cn/`qwen3-8-max` | unknown → active | unknown → baseline: CNY input_uncached_tokens 12/1000000token, output_tokens 36/1000000token |
| bailian/api-cn/`qwen3-8-max-prime` | unknown → active | unknown → baseline: CNY input_uncached_tokens 24/1000000token, output_tokens 72/1000000token |
| bailian/api-cn/`qwen3-7-plus` | unknown → active | unknown → baseline: CNY input_uncached_tokens 2/1000000token, output_tokens 8/1000000token |
| bailian/api-cn/`qwen3-8-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, output_tokens 2.7/1000000token |
| bailian/api-cn/`qwen3-7-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.2/1000000token, output_tokens 0.8/1000000token |
| bailian/api-cn/`qwen3-coder-plus` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4/1000000token, output_tokens 16/1000000token |
| bailian/api-cn/`qwen3-vl-plus` | unknown → active | unknown → baseline: CNY input_uncached_tokens 1/1000000token, output_tokens 10/1000000token |
| bailian/api-cn/`qwen3-vl-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.15/1000000token, output_tokens 1.5/1000000token |
| bailian/api-cn/`qwen3-8-2-4t-a95b` | unknown → active | unknown → baseline: CNY input_uncached_tokens 12/1000000token, output_tokens 36/1000000token |
| bailian/api-cn/`qwen3-8-27b` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, output_tokens 12/1000000token |
| bailian/api-cn/`minimax-minimax-m3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4.2/1000000token, output_tokens 16.8/1000000token |
| bailian/api-cn/`xiaomi-mimo-v2-5-pro` | unknown → active | unknown → baseline: CNY input_uncached_tokens 7/1000000token, output_tokens 21/1000000token |
| bailian/api-cn/`stepfun-step-3-7-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 1.35/1000000token, output_tokens 8.1/1000000token |
| bailian/api-cn/`wan3-0-video` | unknown → active | unknown → baseline: CNY video_input_seconds 0.3/1second, video_output_seconds 0.3/1second |
| bailian/api-cn/`wan3-0-video-prime` | unknown → active | unknown → baseline: CNY video_input_seconds 0.45/1second, video_output_seconds 0.45/1second |
| bailian/coding-plan-cn/`qwen3-7-plus` | active → active | short: CNY input_uncached_tokens 2/1000000token, output_tokens 8/1000000token; long: CNY input_uncached_tokens 6/1000000token, output_tokens 24/1000000token → baseline: CNY input_uncached_tokens 2/1000000token, output_tokens 8/1000000token |
| bailian/token-plan-cn/`qwen3-8-max` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`qwen3-8-flash` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`qwen3-7-plus` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`deepseek-v4-pro` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`deepseek-v4-flash` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`kimi-k2-7-code` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`kimi-k2-6` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`glm-5-2` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`glm-5-1` | unknown → active | unknown → unknown |
| bailian/token-plan-cn/`glm-5` | unknown → active | unknown → unknown |
| cursor/individual/`composer-2-5` | active → active | standard: USD input_uncached_tokens 0.5/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 2.5/1000000token; on-demand: USD input_uncached_tokens 0.5/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 2.5/1000000token → baseline: USD input_uncached_tokens 0.5/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 2.5/1000000token |
| deepseek/api-cn/`deepseek-flash` | active → active | peak: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token; off-peak: CNY input_uncached_tokens 1/1000000token, input_cached_tokens 0.02/1000000token, output_tokens 4/1000000token → baseline: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token |
| deepseek/api-cn/`deepseek-v4-pro` | active → active | peak: CNY input_uncached_tokens 9/1000000token, input_cached_tokens 0.30/1000000token, output_tokens 27/1000000token; off-peak: CNY input_uncached_tokens 4.5/1000000token, input_cached_tokens 0.15/1000000token, output_tokens 13.5/1000000token → baseline: CNY input_uncached_tokens 9/1000000token, input_cached_tokens 0.30/1000000token, output_tokens 27/1000000token |
| deepseek/api-cn/`deepseek-v4-flash` | active → active | peak: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token; off-peak: CNY input_uncached_tokens 1/1000000token, input_cached_tokens 0.02/1000000token, output_tokens 4/1000000token → baseline: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token |
| deepseek/api-cn/`deepseek-v4-flash-vision-exp` | active → active | peak: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token; off-peak: CNY input_uncached_tokens 1/1000000token, input_cached_tokens 0.02/1000000token, output_tokens 4/1000000token → baseline: CNY input_uncached_tokens 2/1000000token, input_cached_tokens 0.04/1000000token, output_tokens 8/1000000token |
| gemini/api-global/`gemini-3-7-flash` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.75/1000000token, input_cached_tokens 0.075/1000000token, output_tokens 3.75/1000000token |
| groq/api-global/`openai-gpt-oss-120b` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.15/1000000token, output_tokens 0.60/1000000token |
| groq/api-global/`openai-gpt-oss-20b` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.075/1000000token, output_tokens 0.30/1000000token |
| groq/api-global/`llama-3-3-70b-versatile` | unknown → active | unknown → unknown |
| hunyuan/api-cn/`hy4-preview` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 0.3/1000000token, output_tokens 18/1000000token |
| hunyuan/api-cn/`hy3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 1/1000000token, input_cached_tokens 0.25/1000000token, output_tokens 4/1000000token |
| hunyuan/api-cn/`hy-mt2-pro` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.5/1000000token, output_tokens 2/1000000token |
| hunyuan/api-cn/`hy-vision-2-0-instruct` | unknown → active | unknown → baseline: CNY input_uncached_tokens 7.5/1000000token, output_tokens 17.5/1000000token |
| hunyuan/api-cn/`deepseek-v4-pro-0813` | unknown → active | unknown → baseline: CNY input_uncached_tokens 9/1000000token, input_cached_tokens 0.3/1000000token, output_tokens 27/1000000token |
| hunyuan/api-cn/`deepseek-v4-flash-0731` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.1/1000000token, output_tokens 9/1000000token |
| hunyuan/api-cn/`glm-5-3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 8/1000000token, input_cached_tokens 2/1000000token, output_tokens 28/1000000token |
| hunyuan/api-cn/`kimi-k3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 20/1000000token, input_cached_tokens 2/1000000token, output_tokens 100/1000000token |
| hunyuan/api-cn/`minimax-m3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 2.1/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 8.4/1000000token |
| kling/api-cn/`kling-3-0-turbo` | unknown → active | unknown → baseline: CNY video_output_seconds 0.8/1second |
| kling/api-cn/`kling-3-0` | unknown → active | unknown → baseline: CNY video_output_seconds 0.6/1second |
| kling/api-cn/`kling-3-0-omni` | unknown → active | unknown → baseline: CNY video_output_seconds 0.6/1second |
| kling/api-cn/`kling-o1` | unknown → active | unknown → baseline: CNY video_output_seconds 0.6/1second |
| kling/api-cn/`kling-2-6` | unknown → active | unknown → baseline: CNY video_output_seconds 0.3/1second |
| kling/api-cn/`kling-2-5-turbo` | unknown → active | unknown → baseline: CNY video_output_seconds 0.3/1second |
| minimax/api-cn/`minimax-m3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 2.1/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 8.4/1000000token |
| minimax/api-cn/`minimax-m2-7` | unknown → active | unknown → baseline: CNY input_uncached_tokens 2.1/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 8.4/1000000token |
| minimax/api-cn/`minimax-m2-7-highspeed` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4.2/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 16.8/1000000token |
| minimax/api-cn/`image-01` | active → active | per-image: CNY generated_images 0.025/1image → baseline: CNY generated_images 0.025/1image |
| minimax/api-cn/`image-01-live` | active → active | per-image: CNY generated_images 0.025/1image → baseline: CNY generated_images 0.025/1image |
| minimax/api-cn/`minimax-h3` | active → active | generation-768p: CNY video_output_seconds 0.50/1second, video_input_seconds 0.50/1second, input_images 0.20/1image; generation-2k: CNY video_output_seconds 0.80/1second, video_input_seconds 0.80/1second, input_images 0.20/1image; regeneration-2k: CNY video_output_seconds 0.30/1second, video_input_seconds 0.30/1second, input_images 0.15/1image → baseline: CNY video_output_seconds 0.50/1second, video_input_seconds 0.50/1second, input_images 0.20/1image |
| minimax/api-cn/`speech-2-8-hd` | active → active | sync-tts: CNY billable_characters 3.50/10000character → baseline: CNY billable_characters 3.5/10000character |
| minimax/api-cn/`speech-2-8-turbo` | active → active | sync-tts: CNY billable_characters 2.00/10000character → baseline: CNY billable_characters 2/10000character |
| minimax/api-cn/`speech-2-6-hd` | unknown → active | unknown → baseline: CNY billable_characters 3.5/10000character |
| minimax/api-cn/`speech-2-6-turbo` | unknown → active | unknown → baseline: CNY billable_characters 2/10000character |
| minimax/api-cn/`speech-02-hd` | unknown → active | unknown → baseline: CNY billable_characters 3.5/10000character |
| minimax/api-cn/`speech-02-turbo` | unknown → active | unknown → baseline: CNY billable_characters 2/10000character |
| minimax/token-plan-cn/`minimax-m3` | 未收录 → active | 未收录 → baseline: CNY input_uncached_tokens 2.1/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 8.4/1000000token |
| minimax/token-plan-cn/`minimax-m2-7` | 未收录 → active | 未收录 → baseline: CNY input_uncached_tokens 2.1/1000000token, input_cached_tokens 0.42/1000000token, output_tokens 8.4/1000000token |
| mistral/api-global/`mistral-large-latest` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.5/1000000token, input_cached_tokens 0.05/1000000token, output_tokens 1.5/1000000token |
| mistral/api-global/`mistral-small-latest` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.15/1000000token, input_cached_tokens 0.015/1000000token, output_tokens 0.6/1000000token |
| moonshot/api-cn/`kimi-k3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 20/1000000token, input_cached_tokens 2/1000000token, output_tokens 100/1000000token |
| moonshot/api-cn/`kimi-k2-7-code` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6.5/1000000token, input_cached_tokens 1.3/1000000token, output_tokens 27/1000000token |
| moonshot/api-cn/`kimi-k2-7-code-highspeed` | unknown → active | unknown → baseline: CNY input_uncached_tokens 13/1000000token, input_cached_tokens 2.6/1000000token, output_tokens 54/1000000token |
| moonshot/api-cn/`kimi-k2-6` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6.5/1000000token, input_cached_tokens 1.1/1000000token, output_tokens 27/1000000token |
| moonshot/kimi-code/`k3` | 未收录 → active | 未收录 → unknown |
| moonshot/kimi-code/`k3-256k` | 未收录 → active | 未收录 → unknown |
| moonshot/kimi-code/`kimi-for-coding` | 未收录 → active | 未收录 → unknown |
| moonshot/kimi-code/`kimi-for-coding-highspeed` | 未收录 → active | 未收录 → unknown |
| openai/api-global/`gpt-5-2` | unknown → active | unknown → baseline: USD input_uncached_tokens 1.75/1000000token, input_cached_tokens 0.175/1000000token, output_tokens 14/1000000token |
| openai/codex/`gpt-6-astra` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 250/1000000token, input_cached_tokens 25/1000000token, output_tokens 1250/1000000token |
| openai/codex/`gpt-5-6-sol` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 100/1000000token, input_cached_tokens 10/1000000token, output_tokens 500/1000000token |
| openai/codex/`gpt-5-6-terra` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 50/1000000token, input_cached_tokens 5/1000000token, output_tokens 300/1000000token |
| openai/codex/`gpt-5-6-luna` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 5/1000000token, input_cached_tokens 0.5/1000000token, output_tokens 30/1000000token |
| openrouter/api-global/`anthropic-claude-sonnet-latest` | unknown → active | unknown → baseline: USD input_uncached_tokens 2.000000/1000000token, output_tokens 10.00000/1000000token, input_cached_tokens 0.2000000/1000000token |
| qianfan/api-cn/`ernie-5-1` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4/1000000token, output_tokens 18/1000000token |
| qianfan/api-cn/`ernie-5-0` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, output_tokens 24/1000000token |
| qianfan/api-cn/`ernie-4-5-turbo-128k` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 3.2/1000000token |
| qianfan/api-cn/`ernie-4-5-turbo-vl-32k` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.75/1000000token, output_tokens 9/1000000token |
| qianfan/api-cn/`deepseek-v4-pro` | unknown → active | unknown → unknown |
| qianfan/api-cn/`deepseek-v4-flash` | unknown → active | unknown → unknown |
| qianfan/api-cn/`glm-5-3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 8/1000000token, input_cached_tokens 2/1000000token, output_tokens 28/1000000token |
| qianfan/api-cn/`ernie-4-5-turbo-20260402` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 3.2/1000000token |
| qianfan/api-cn/`glm-5-1` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 1.3/1000000token, output_tokens 24/1000000token |
| siliconflow/api-cn/`deepseek-ai-deepseek-v4-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.3/1000000token, output_tokens 9/1000000token |
| siliconflow/api-cn/`deepseek-ai-deepseek-v4-pro` | unknown → active | unknown → baseline: CNY input_uncached_tokens 12/1000000token, input_cached_tokens 1/1000000token, output_tokens 24/1000000token |
| siliconflow/api-cn/`deepseek-ai-deepseek-v3-2` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4/1000000token, input_cached_tokens 0.4/1000000token, output_tokens 6/1000000token |
| siliconflow/api-cn/`pro-zai-org-glm-5-1` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 1.3/1000000token, output_tokens 24/1000000token |
| siliconflow/api-cn/`qwen-qwen3-5-397b-a17b` | unknown → retired | unknown → not_applicable |
| siliconflow/api-cn/`pro-moonshotai-kimi-k2-6` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6.5/1000000token, input_cached_tokens 1.1/1000000token, output_tokens 27/1000000token |
| siliconflow/api-cn/`moonshotai-kimi-k2-7-code` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6.5/1000000token, input_cached_tokens 1.3/1000000token, output_tokens 27/1000000token |
| siliconflow/api-cn/`minimaxai-minimax-m2-5` | unknown → retired | unknown → not_applicable |
| siliconflow/api-cn/`pro-zai-org-glm-4-7` | unknown → retired | unknown → not_applicable |
| together/api-global/`openai-gpt-oss-120b` | unknown → active | unknown → baseline: USD input_uncached_tokens 0.15/1000000token, output_tokens 0.60/1000000token |
| xai/api-global/`grok-4-6` | unknown → active | unknown → baseline: USD input_uncached_tokens 2/1000000token, input_cached_tokens 0.5/1000000token, output_tokens 6/1000000token |
| xai/api-global/`grok-4-5` | unknown → active | unknown → baseline: USD input_uncached_tokens 2/1000000token, input_cached_tokens 0.30/1000000token, output_tokens 6/1000000token |
| xai/grok-build/`grok-4-6` | unknown → active | unknown → baseline: USD input_uncached_tokens 2/1000000token, input_cached_tokens 0.5/1000000token, output_tokens 6/1000000token |
| zhipu/api-cn/`glm-5-3` | unknown → active | unknown → baseline: CNY input_uncached_tokens 8/1000000token, input_cached_tokens 2/1000000token, output_tokens 28/1000000token |
| zhipu/api-cn/`glm-5-3-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.23/1000000token, output_tokens 2.8/1000000token |
| zhipu/api-cn/`glm-5-2` | unknown → active | unknown → baseline: CNY input_uncached_tokens 8/1000000token, input_cached_tokens 2/1000000token, output_tokens 28/1000000token |
| zhipu/api-cn/`glm-5-1` | unknown → active | unknown → baseline: CNY input_uncached_tokens 6/1000000token, input_cached_tokens 1.3/1000000token, output_tokens 24/1000000token |
| zhipu/api-cn/`glm-5` | unknown → active | unknown → baseline: CNY input_uncached_tokens 4/1000000token, input_cached_tokens 1/1000000token, output_tokens 18/1000000token |
| zhipu/api-cn/`glm-5-turbo` | unknown → active | unknown → baseline: CNY input_uncached_tokens 5/1000000token, input_cached_tokens 1.2/1000000token, output_tokens 22/1000000token |
| zhipu/api-cn/`glm-4-7` | unknown → active | unknown → baseline: CNY input_uncached_tokens 3/1000000token, input_cached_tokens 0.6/1000000token, output_tokens 14/1000000token |
| zhipu/api-cn/`glm-4-7-flashx` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.5/1000000token, input_cached_tokens 0.1/1000000token, output_tokens 3/1000000token |
| zhipu/api-cn/`glm-4-7-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0/1000000token, input_cached_tokens 0/1000000token, output_tokens 0/1000000token |
| zhipu/api-cn/`glm-4-5-air` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0.8/1000000token, input_cached_tokens 0.16/1000000token, output_tokens 6/1000000token |
| zhipu/api-cn/`glm-5v-turbo` | unknown → active | unknown → baseline: CNY input_uncached_tokens 5/1000000token, input_cached_tokens 1.2/1000000token, output_tokens 22/1000000token |
| zhipu/api-cn/`glm-4-6v` | unknown → active | unknown → baseline: CNY input_uncached_tokens 1/1000000token, input_cached_tokens 0.2/1000000token, output_tokens 3/1000000token |
| zhipu/api-cn/`glm-4-6v-flash` | unknown → active | unknown → baseline: CNY input_uncached_tokens 0/1000000token, input_cached_tokens 0/1000000token, output_tokens 0/1000000token |
| zhipu/coding-plan-cn/`glm-5-3` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 6.9/10000token, input_cached_tokens 1.7/10000token, output_tokens 24/10000token |
| zhipu/coding-plan-cn/`glm-5-3-flash` | unknown → active | unknown → baseline: CREDIT input_uncached_tokens 2.3/10000token, input_cached_tokens 0.56/10000token, output_tokens 8/10000token |
