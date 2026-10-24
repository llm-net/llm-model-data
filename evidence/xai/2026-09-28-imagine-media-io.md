# Grok Build：Grok Imagine 图像 / 视频型号输入输出

基线：`e49d95e9063acab5a06d6afe60d80ed2bf328d8e`。在 grok-build 产品新增 `grok-imagine-image-2.0`、`grok-imagine-video-1.5`、`grok-imagine-video` 三个型号的资料；本次没有实调。

## 来源

全部为 2026-09-28 UTC 获取的 xAI 官方文档（.md 版本；.md 省略的警示框另查渲染页）。

| source ID | URL | UTC 时间 | 用途 |
| --- | --- | --- | --- |
| imagine-models | https://docs.x.ai/developers/models | 06:22:38Z | 型号表 |
| imagine-pricing | https://docs.x.ai/developers/pricing | 06:22:38Z | Imagine Pricing |
| imagine-model-image2 / -video15 / -video | https://docs.x.ai/developers/models/grok-imagine-{image-2.0,video-1.5,video} | 06:25:32–34Z | 型号页、模态、别名 |
| imagine-image-generation | https://docs.x.ai/developers/model-capabilities/images/generation | 06:22:39Z（渲染页 06:26:57Z） | 比例、分辨率、quality、n |
| imagine-image-editing / -multi | …/images/editing、…/images/multi-image-editing | 06:22:40Z（渲染页 06:26:56Z） | 编辑、最多 5 张图 |
| imagine-video-generation | …/video/generation | 06:22:40Z（渲染页 06:26:54Z） | 时长、比例、分辨率、音轨、音色 |
| imagine-video-i2v / -r2v | …/video/image-to-video、…/video/reference-to-video | 06:22:41Z（渲染页 06:26:34–55Z） | 首帧、首尾帧、关键帧、参考图 ≤ 7、参考音色 |
| imagine-video-editing / -extension | …/video/editing、…/video/extension | 06:22:42Z、06:24:58Z（渲染页 06:26:32–33Z） | 编辑 ≤ 8.7 s；延长输入 2–15 s、新增 2–10 s |
| imagine-openapi | https://docs.x.ai/openapi.json | 06:25:05Z | 请求 / 响应 schema 与枚举 |
| imagine-rest-images / -videos | https://docs.x.ai/developers/rest-api-reference/inference/{images,videos} | 06:25:04Z | REST 字段 |
| imagine-tts-voices | https://docs.x.ai/developers/model-capabilities/audio/text-to-speech | 渲染页 06:28:43Z | 预设音色 |
| build-commands | https://docs.x.ai/build/modes-and-commands | 06:25:04Z | /imagine、/imagine-video |
| build-zdr-video | https://docs.x.ai/build/settings/zdr-video-storage | 06:25:05Z | Build 视频工具 |
| audit-faq | https://docs.x.ai/grok/faq | 06:25:05Z | SuperGrok 用量池 |

## 订阅通道

- Build 文档有 `/imagine <prompt>`（「Generate an image from a text description」）与 `/imagine-video <prompt>`，并写「A few commands appear only when their feature is available (for example /imagine and /loop)」。ZDR 页写视频工具「Grok Build presigns an upload URL for each generation and passes it to the API」，对应 Imagine 请求的 `output.upload_url`。
- Grok FAQ：SuperGrok 付费计划是「one shared weekly usage pool」，覆盖「Chat, Imagine, Voice, or Build」。
- 未找到：Build 用哪个 Imagine 型号、订阅令牌能否直接调用 `https://api.x.ai/v1` 的 Imagine 端点、Build 内 Imagine 的用量限制。消费者（LLM Gate 固件）按官方客户端的 user token 约定（`Authorization: Bearer` + `X-XAI-Token-Auth: xai-grok-cli`）把订阅令牌发往 `api.x.ai/v1/images/*`、`/videos/*`，这是实现依据，不是公开文档；本次没有实调。
- 因此三个型号的 `availability=unknown`、型号身份 `needs_review`；`media_io` 按 xAI 公开 API 文档记录，标 partial，并在说明里写明订阅通道这一环未经公开文档证实。

## 型号

| 型号 | 价格（原文） | 操作 |
| --- | --- | --- |
| grok-imagine-image-2.0 | $0.04 / image | 文生图；单图编辑或最多 5 张图的多图编辑；`quality` 只有本型号支持 |
| grok-imagine-video-1.5 | $0.080 / sec | 文生、图生（首帧）、首尾帧（`last_frame`）、关键帧（`keyframes` ≤ 4）、参考图生视频（≤ 7 张，可带 ≤ 3 个预设音色）；型号页输入为 text、image，编辑 / 延长示例均用 Classic |
| grok-imagine-video | $0.050 / sec | 文生、图生、参考图生视频、视频编辑、视频延长；「Classic grok-imagine-video rejects last_frame and keyframes and rejects combining image with reference inputs.」 |

## 字段要点与文档冲突

- 图像 `aspect_ratio` 枚举（OpenAPI）：`1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, 21:9, 5:2, auto`。单图编辑「do not set this」，自动跟随输入图。
- 图像 `resolution`：指南只列 `1k`（缺省）、`2k`；OpenAPI 枚举多一个 `1.5k`。记录取指南两值，`1.5k` 写进说明。
- `quality`：指南、release notes、迁移指南写 `low | medium | auto`，缺省 `auto`（生成取 low、编辑取 medium），只对 2.0 生效；REST 参考与 OpenAPI 请求 schema 没有此字段；`/v1/image-generation-models` 的计价层写 low / medium / high。记录取指南三值。
- `n`：生成 1–10，缺省 1；编辑未写上限。
- 图像输入 `{url | file_id}`，url 可为公网地址或 base64 data URL，格式 JPEG / PNG / WebP；多图用 `<IMAGE_0>` 等在提示词里指代；大小上限未查到。
- 输出 `data[].url` 或 `data[].b64_json`（`response_format` 缺省 url），`mime_type` 示例为 image/png、image/jpeg、image/webp；URL「temporary」，有效期未查到。
- 视频 `duration` 1–15，缺省 8（兼容 `seconds`）；`aspect_ratio` `1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3`，缺省 16:9；`resolution` `480p`（缺省）/ `720p` / `1080p`，1080p 只在 1.5 的文生 / 图生，参考图生视频上限 720p。
- 图生视频的 `aspect_ratio`：指南写会覆盖并拉伸输入图，OpenAPI 写对图生视频忽略。
- `generate_audio`：指南写缺省带音轨、传 false 得无声视频；OpenAPI 无此字段。`last_frame` 只在指南，不在 OpenAPI。
- 组合（reference-to-video 页 First & Last frame 小节、REST 参考）：1.5 的 `image` 可与 `reference_images`、`reference_audios`、`last_frame` 组合；可以只给 `last_frame`；首尾帧请求的 prompt 都可省；`reference_audios` 可不带 `reference_images` 单独使用（「audio-only reference-to-video」），带任一参考即参考生视频模式。Classic「rejects last_frame and rejects combining image with reference inputs」。
- 参考音色 `reference_audios[]`：每项 `{voice_id}` 或 `{url}`，最多 3 个；url 为 ≤ 15 s 的自带音频，「available to trusted partners, on request」。预设音色 28 个（与 TTS 共用、大小写不敏感）：carina, zagan, helix, orion, luna, iris, altair, zenith, perseus, helios, lux, kepler, rigel, cosmo, celeste, ursa, sirius, lumen, castor, naksh, atlas, aurora, liora, ara, eve, leo, rex, sal。
- 视频编辑：必填 `prompt`、`video`（`{url | file_id}`，.mp4，H.265 / H.264 / AV1），输入最长 8.7 s；不收 duration / aspect_ratio / resolution，输出沿用输入、上限 720p。
- 视频延长：必填 `prompt`、`video`，输入 2–15 s；`duration` 2–10，缺省 6，只指新增段；输出沿用输入比例与分辨率、上限 720p。
- 查询 `GET /v1/videos/{request_id}`：`status` `pending | done | expired | failed`，`video{url, duration, …}`，产物 mp4，URL 有效期未查到；返回没有按秒计量字段，秒数取 `video.duration`。
- 未查到：提示词长度上限（仅 models 接口示例有 `max_prompt_length: 1024`，型号为 grok-imagine-image）、视频输入大小上限、`seed`。

## 上下文、思考与参考价

- 三个型号都是 Imagine 生成接口，没有文本对话窗口，上下文记 not_applicable。
- 未找到思考控制资料，思考记 unknown。
- 参考价取同平台 xAI API Imagine Pricing：2.0 为 0.04 USD / 张，video-1.5 为 0.080 USD / 秒，video 为 0.050 USD / 秒。imagine 总览写视频「both duration and resolution affect the total cost」，价格表每型号只有一个单价，按表中单价记录。
