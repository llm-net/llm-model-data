# 可灵 协议面专项核对

核对日期：2026-09-16。访问时段截至 UTC 2026-09-16T12:02:58.787297Z。网页 / 官方文档核对；没有用真实 Key 实调。

## 来源

- `protocol-models`：https://klingai.com/document-api/guides/capability-map/video.md
- `protocol-api`：https://klingai.com/document-api/api-reference/model/text-to-video.md

## 核对边界

按当前产品和模型 ID 核对，表内每一行都是独立结论。complete 仅指本次官方文档范围内的推理协议面清单；partial 的未证实部分不表示不支持。价格、套餐及非协议能力沿用原记录，没有本轮重新背书。

## 逐模型结果

| 产品 | 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- | --- |
| api-cn | `kling-3-0-turbo` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
| api-cn | `kling-3-0` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
| api-cn | `kling-3-0-omni` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
| api-cn | `kling-o1` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
| api-cn | `kling-2-6` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
| api-cn | `kling-2-5-turbo` | `kling_video` | complete | models, api | 可灵视频厂商面；普通文生视频与 Omni / O1 的任务路径按型号区分。协议面共同不代表请求体或操作完全相同。 |
