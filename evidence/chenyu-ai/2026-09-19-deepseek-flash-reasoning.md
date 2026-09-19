# 晨羽AI DeepSeek Flash 思考档位修正

官方来源：https://chenyu.pro/api/v1/public/models；UTC 获取时间：`2026-09-19T06:56:25.208094+00:00`。经公开 HTTPS 匿名读取，HTTP 200，无 Key、Cookie 或付费调用。

基线提交：`bf577ad968a15cadb63d439c93bb7899c74776a0`。本次仅修正 `deepseek-flash` 的思考事实，不改价格、可用性、窗口值或模型清单。

证据位置：`data.models[modelId=deepseek-flash].reasoning`。已保存公开模型能力字段的[机读摘录](2026-09-19-reasoning-public-models.json)（非完整原始响应），包含全部 30 个已有模型以核对协议、窗口和思考缺项。

## 修正

- 旧资料记 unknown；当前晨羽AI已明确公开 supported / complete。
- Responses：`reasoning.effort` = `none / low / high / max`，默认 `high`；`none` 关闭。
- Chat：`thinking.type` = enabled / disabled，默认 enabled；`reasoning_effort` = minimal / low / medium / high / xhigh / max / ultra，默认 high。
- Messages：`thinking.type` = enabled / disabled，默认 enabled；`output_config.effort` 与 Chat 枚举相同、默认 high。
- Chat 与 Messages 的兼容映射按公开 control.notes 保留；未推导 Responses 的其他枚举。原响应的原厂 verification 留在摘录中用于追溯，条目改为本平台独立来源和本次时间。

## 范围与缺项

- 逐项核对现有 30 个请求 ID，全部仍在公开清单；协议 ID、窗口与输出字段对照结果如下。此次不重新背书价格；公开价格已有分时差异，须由独立核价更新处理。
- 其余型号的未确认思考能力继续未知，partial 继续保留原有缺口；无 reasoning 字段不是不支持。GLM 公开说明含其他产品的泛化兼容文字，继续保留原先仅登记自身 low/high/max 的限定，不据此扩充取值。

| 请求 ID | 思考支持 / 覆盖 | 协议对照 | 窗口对照 |
| --- | --- | --- | --- |
| `deepseek-flash` | supported / complete | 相同 | 相同 |
| `deepseek-v4-pro` | supported / complete | 相同 | 相同 |
| `deepseek-v4-flash` | unknown / unknown | 相同 | 相同 |
| `deepseek-v4-flash-vision-exp` | unknown / unknown | 相同 | 相同 |
| `doubao-seed-2-1-pro-260628` | unknown / unknown | 相同 | 相同 |
| `doubao-seed-2-1-turbo-260628` | unknown / unknown | 相同 | 相同 |
| `doubao-seed-2-0-lite-260428` | unknown / unknown | 相同 | 相同 |
| `doubao-seed-2-0-mini-260428` | unknown / unknown | 相同 | 相同 |
| `doubao-seed-2-0-pro-260215` | unknown / unknown | 相同 | 相同 |
| `doubao-seedream-5-0-pro-260628` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `doubao-seedream-5-0-260128` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `doubao-seedance-2-5-260628` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `doubao-seedance-2-0-260128` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `doubao-seedance-2-0-mini-260615` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `qwen3.8-max` | supported / partial | 相同 | 相同 |
| `qwen3.7-plus` | supported / partial | 相同 | 相同 |
| `qwen3.8-flash` | supported / partial | 相同 | 相同 |
| `qwen3.7-flash` | supported / partial | 相同 | 相同 |
| `qwen3.8-27b` | supported / partial | 相同 | 相同 |
| `wan3.0-video` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `wan3.0-video-prime` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `MiniMax-M3` | supported / partial | 相同 | 相同 |
| `MiniMax-H3` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `speech-2.8-hd` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `speech-2.8-turbo` | unknown / unknown | 相同 | 不适用或口径不同，未修改 |
| `glm-5.3` | supported / partial | 相同 | 相同 |
| `glm-5.3-flash` | supported / partial | 相同 | 相同 |
| `kimi-k3` | supported / partial | 相同 | 相同 |
| `Qwen/Qwen3.8-27B-FP8` | unknown / unknown | 相同 | 相同 |
| `nvidia/Qwen3.6-35B-A3B-NVFP4` | unknown / unknown | 相同 | 相同 |
