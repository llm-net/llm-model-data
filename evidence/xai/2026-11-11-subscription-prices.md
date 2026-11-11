# Grok Build 原厂参考价专项核对

范围仅为 `grok-build` 已有 7 个型号，保留非促销标准价。UTC 读取窗口：2026-11-11T12:42:14Z 至 2026-11-11T12:47:02Z。通过官网 HTML、官方 Markdown 与 OpenAPI 读取；没有使用真实 Key 调用模型。只更新 3 个媒体型号的参考价及其来源，不更改 API 产品、型号身份或能力核对日期。

## 官方来源

| source ID | URL | 页面位置及结论 |
| --- | --- | --- |
| `imagine-pricing` | https://docs.x.ai/developers/pricing | Text API、Imagine API、Grok 4.7 Fast pricing；币种 USD，HTML 媒体表包含输入分量和分辨率档 |
| `refresh-pricing` | https://docs.x.ai/developers/pricing.md | Text API 与 Fast 分节；媒体 Markdown 简表仅列输出起价，不能代替 HTML 完整表 |
| `imagine-model-image2` | https://docs.x.ai/developers/models/grok-imagine-image-2.0 | Pricing、Input pricing、按 resolution/quality 的输出表 |
| `imagine-model-video15` | https://docs.x.ai/developers/models/grok-imagine-video-1.5 | Pricing、Input pricing、按 resolution 的输出表；预设音色输入免费 |
| `imagine-model-video` | https://docs.x.ai/developers/models/grok-imagine-video | Pricing、Input pricing、按 resolution 的输出表；Video Extension 明示促销 |
| `imagine-image-generation` | https://docs.x.ai/developers/model-capabilities/images/generation | Resolution 缺省 1k；Quality 的 auto 在生成取 low、编辑取 medium |
| `subscription-image-quality-retirement` | https://docs.x.ai/developers/migration/imagine-image-quality-nov-2 | How the redirect works、Pricing impact；退役的是旧 quality 型号，2.0 的 low 仍在售 |
| `imagine-video-generation` | https://docs.x.ai/developers/model-capabilities/video/generation | Resolution 缺省 480p；完成响应 video.duration；编辑保持输入分辨率 |
| `imagine-video-i2v` | https://docs.x.ai/developers/model-capabilities/video/image-to-video | image 首帧；与尾帧、参考图或关键帧组合时切换到参考图生视频 |
| `imagine-video-r2v` | https://docs.x.ai/developers/model-capabilities/video/reference-to-video | 1.5 的 reference_images、last_frame 与 keyframes[].image；各图按实际提交数量统计 |
| `imagine-video-editing` | https://docs.x.ai/developers/model-capabilities/video/editing | 通过 video 提交输入媒体，编辑保留原时长 |
| `imagine-rest-images` | https://docs.x.ai/developers/rest-api-reference/inference/images | 实际出图在返回 data 中 |
| `imagine-rest-videos` | https://docs.x.ai/developers/rest-api-reference/inference/videos | 完成响应 video.duration，不把 cost_in_usd_ticks 当作输入视频秒数 |
| `imagine-openapi` | https://docs.x.ai/openapi.json | EditImageRequest 的 image/images 互斥；GenerateVideoRequest、EditVideoRequest 的图片和视频输入字段；读取完成 UTC 2026-11-11T12:44:56Z |

图生视频与参考图生视频页面于 UTC 2026-11-11T12:47:02Z 直接读取。字段只按对应型号及操作范围计量；1.5 的关键帧示例明确请求字段 `keyframes[].image`，该输入计入图片张数，但本次不改能力清单。精确计费输入秒数没有独立 usage 字段，不能从账单金额反算时长。

## 文本结果

单位为 USD/百万 token，依次为未缓存输入、缓存读取、输出。四条现有数字均相符，不刷新不变条目的核对日期。

| 型号 | 现有值 = 官网值 | 标准档 |
| --- | --- | --- |
| `grok-4.7` | 2 / 0.5 / 6 | 提示严格小于 200k |
| `grok-4.7-build-fast` | 4 / 1 / 12 | 官网独立 Fast 档，非公开 API 型号；超过 200k 另价 |
| `grok-4.6` | 2 / 0.5 / 6 | 提示严格小于 200k |
| `grok-4.5` | 2 / 0.30 / 6 | 提示严格小于 200k |

Fast 正文规定超过 200k 才用长上下文价；其表头使用 Below/Above，未把普通 API 的 ≥200k 阈值强套到 Fast。Fast 与 Priority、美国区域溢价分别维护，不把两种溢价叠算为本基准。

## 媒体修正

| 型号 | 原参考价 | 本次标准基准 |
| --- | --- | --- |
| `grok-imagine-image-2.0` | 仅输出 0.04 USD/图；输入图写未查到 | 明确 1K、low，输出仍为 0.04 USD/图，补输入 0.01 USD/图 |
| `grok-imagine-video-1.5` | 仅输出 0.080 USD/秒，未注明分辨率 | 明确默认 480p，输出不变，补输入图片 0.01 USD/图 |
| `grok-imagine-video` | 仅输出 0.050 USD/秒，未注明分辨率 | 明确 480p 普通生成或编辑，输出不变，补输入图片 0.002 USD/图、输入视频 0.01 USD/秒 |

图像 low 没有退役：2026-11-02 退役的是 `grok-imagine-image-quality` 旧请求名，其生成和编辑都转向 2.0 low。本目录原条目直接使用 2.0，默认 auto 的编辑则使用 medium，1K 输出为 0.06 USD/图；要采用本条 low 估价，编辑需明确选择 low。其他质量和分辨率只记条件，不增加第二组规则。

视频标准输出费率依分辨率变化：1.5 的 720p/1080p 为 0.14/0.25 USD/秒，Classic 的 720p 为 0.07 USD/秒。普通编辑沿用输入分辨率，只有 480p 输出属于所选基准。Classic 视频延长的促销价格不写入标准价。1.5 预设音色输入有明确免费说明，但未公布适合本条的数量单位，不造一个音频按秒零价。

图片按实际输入张数；视频输入按源媒体实际秒数，与输出 `video.duration` 分开。免费量、最低量及视频秒数取整未见明确规定，保留 null/unknown。图像输出用实际 `data` 张数，不使用请求期望的 `n`。所有订阅 `usage_prices` 仍为 not_applicable，参考价不证明订阅扣费或通道授权。

## 型号完整性与限制

公开 API 价表另有 `grok-build-0.1`、`grok-imagine-video-1.5-lite`，不据 API 价表推断 Grok Build 订阅可用。`https://cli-chat-proxy.grok.com/v1/models` 本次匿名访问返回 401（UTC 2026-11-11T12:42:25Z），无法据此补充订阅型号，未新增型号。
