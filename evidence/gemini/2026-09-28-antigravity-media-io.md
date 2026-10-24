# Antigravity 工具订阅：gemini-3.1-flash-image 输入输出实测

基线：`e49d95e9063acab5a06d6afe60d80ed2bf328d8e`。新增 `antigravity` 产品，只收录图像型号 `gemini-3.1-flash-image`；本产品的文本型号、套餐与额度未收录。

## 来源与方法

| source ID | URL | UTC 时间 / 位置 | 用途 |
| --- | --- | --- | --- |
| antigravity-code-assist | https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent | 2026-09-27T15:23Z–2026-09-28T05:41:16Z，分五批 | 订阅通道逐参数实测 |
| gemini-image-guide | https://ai.google.dev/gemini-api/docs/generate-content/image-generation | 2026-09-28T06:25:51Z；Aspect ratios and image size、Thinking、Image Search、reference images | Gemini API 文档，仅作对照，不继承 |
| gemini-image-model | https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image | 2026-09-28T06:25:51Z | 同上 |
| pricing | https://ai.google.dev/gemini-api/docs/pricing | 2026-09-28T06:25:51Z；Gemini 3.1 Flash Image (Nano Banana 2) Standard | 参考价 |
| antigravity-models | https://antigravity.google/docs/models | 2026-09-28T06:24:09Z；Additional Models | Antigravity 官方对生图型号的说明 |
| antigravity-plans | https://antigravity.google/docs/plans | 2026-09-28T06:24:10Z；Baseline Quota、Overages | 额度窗口 |
| antigravity-terms | https://antigravity.google/terms | 2026-09-28T06:24:24Z | 第三方访问条款 |
| code-assist-cli | https://github.com/google-gemini/gemini-cli/blob/v0.61.0/packages/core/src/code_assist/server.ts | 2026-09-28T06:28Z；tag v0.61.0（commit bb523741c7429a44d03e964bc124c7c92df59d5f），server.ts:73-74、converter.ts:33-39 | Code Assist 端点与信封 |

- 实测用一个 Antigravity 工具订阅账号（套餐档位未记录）。凭据只在持有它的设备进程内使用，没有输出或归档；本文件不记账号身份、设备地址、凭据或原始响应。
- 请求形态是 Code Assist 信封：`{"project", "model": "gemini-3.1-flash-image", "userAgent": "antigravity", "requestType": "agent", "requestId", "request": <Gemini GenerateContentRequest>}`，发往上表端点的 `v1internal:generateContent`（非流式）。信封由消费者实现，与官方 agy 客户端同形；本次没有另取官方客户端产物核对。
- 提示词是无害的合成句子（灯塔插画等），参考图是本地生成的纯色几何图（384×384 JPEG / PNG / GIF、1×1 WebP、768×432 JPEG、2200×2200 噪点 PNG）。只记录 HTTP 状态、上游错误原文、finishReason、各 part 的类型 / 长度、解码后的图像 MIME 与像素、thoughtSignature 长度与 usageMetadata。模型生成的文本只记长度。
- 共发 41 个用例，成功出图 30 张。

## 官方资料

- Antigravity 模型页 Additional Models：「Nano Banana 2: Used by the generative image tool when the Agent wants to produce a UI mockup …」，并写这些模型「not customizable」；没给型号 ID，条目链接却指向 Nano Banana Pro 的博客。Google 博客（2026-02-26）写 Nano Banana 2「available for use in Google Antigravity」；型号 ID 只在 Gemini API 文档里对应为 `gemini-3.1-flash-image`。
- 套餐页：Pro「refreshed every five hours until weekly limit reached」，Ultra 同为 5 小时刷新；没写图像生成是否单独计额。实测的 5 小时重置与此一致。
- gemini-cli v0.61.0：`CODE_ASSIST_ENDPOINT = 'https://cloudcode-pa.googleapis.com'`、`CODE_ASSIST_API_VERSION = 'v1internal'`；信封 `CAGenerateContentRequest{model, project?, user_prompt_id?, request, enabled_credit_types?}`。gemini-cli 的信封里没有 `requestType` / `userAgent`，实测用的这两个字段来自消费者对 agy 请求的抓包，不是公开源码。Antigravity 官方资料没有提到 cloudcode-pa 或 v1internal。
- 条款：「Using third party software, tools, or services to access the Service (e.g. using OpenClaw with Antigravity OAuth) is a breach of this Agreement. Such actions may be grounds for suspension or termination of your Antigravity and/or Gemini CLI accounts.」本记录只陈述事实，不代表获授权。

## 型号身份

`model=gemini-3.1-flash-image` 返回 200，响应 `modelVersion` 同名。同一通道对 `gemini-3.1-flash-image-preview`、`gemini-3.1-flash-lite-image`、`gemini-3-pro-image` 均返回 404 `Requested entity was not found.`，本产品不收录它们。

## 字段位置

Gemini API 文档推荐的 `generationConfig.responseFormat.image`（`aspectRatio`、`imageSize`、`mimeType`、`delivery`）在本通道全部返回 400：`Unknown name "aspectRatio" at 'request.generation_config.response_format.image': Cannot find field.`。图像参数只能写在 `generationConfig.imageConfig`。

## 参数

| 请求 | 结果 |
| --- | --- |
| `imageConfig.aspectRatio=9:21`、`2:1` | 400：`aspect_ratio must be one of '1:1', '1:4', '1:8', '2:3', '3:2', '3:4', '4:1', '4:3', '4:5', '5:4', '8:1', '9:16', '16:9', or '21:9'.` |
| `imageConfig.imageSize=0.5K` | 400：`Unsupported image_size '0.5K'. Supported values are: 1K, 2K, 4K, 512, 512P, 512PX.` |
| `imageConfig.imageSize=1k`（小写） | 200，出 1152×928（5:4 的 1K 档）；Gemini API 文档称小写会被拒，本通道受理 |
| `thinkingConfig.thinkingLevel=LOW` | 400：`Thinking level LOW is not supported for this model. Please retry with other thinking level.` |
| `thinkingLevel=MINIMAL`、`HIGH` | 200 |
| `thinkingLevel=HIGH` + `includeThoughts=true` | 200；parts 依次为思考文本、一张 `thought:true` 的草稿图、思考文本、带 `thoughtSignature` 的最终图；usage 另列 `thoughtsTokenCount` |
| `candidateCount=2` | 400：`Multiple candidates is not enabled for this model` |
| `responseModalities` 省略、`["IMAGE"]`、`["TEXT","IMAGE"]` | 均只返回一张图，没有文本 part |
| `responseModalities=["TEXT"]` | 只返回一段文本（带短 thoughtSignature），不出图 |
| `imageConfig.imageOutputOptions.mimeType=image/png`（Vertex 字段） | 200，仍输出 JPEG |
| `imageConfig.personGeneration=ALLOW_ALL`（Vertex 字段） | 200，效果未验证（提示词无人物） |
| `seed=42`、`temperature=0.4`、`topP=0.9` | 200，效果未验证 |
| `tools=[{"googleSearch":{}}]` | 200，候选带 `groundingMetadata`（`webSearchQueries`、`groundingChunks`、`searchEntryPoint`） |
| `tools=[{"googleSearch":{"searchTypes":{"webSearch":{},"imageSearch":{}}}}]` | 200，同上；未返回 `imageSearchQueries`，Image Search 是否生效未确认 |
| 多轮：历史里的 model 图像 part 不带 `thoughtSignature` | 200；未出现 Gemini 3 文档所说的严格 400 |

## 参考图

| 请求 | 结果 |
| --- | --- |
| 14 张 384×384 JPEG（inlineData） | 200；promptTokenCount 3633 |
| 15 张 | 200；promptTokenCount 3891，未见 14 张上限被强制执行 |
| 3 张 PNG + 2 张 JPEG | 200 |
| 1×1 WebP + JPEG | 200 |
| GIF | 200（Gemini API 文档的格式清单未列 GIF） |
| `fileData.fileUri` = google.com 上的一张 https PNG | 200；由上游自行抓取，只测了这一个地址 |
| 单张 14.5 MB PNG（整个请求 19.4 MB） | 200；该图只计约 258 token |
| 768×432（16:9）参考图、不带 aspectRatio、`imageSize=512` | 出 683×384，比例跟随参考图 |

HEIC / HEIF 与视频、PDF 输入未测。

## 输出

- 全部为 `candidates[0].content.parts[].inlineData`，`mimeType=image/jpeg`，base64；同一 part 带 `thoughtSignature`。响应外层是 `{"response": {…}, "traceId": …}`。
- 不带 `imageConfig`、无参考图时出 1408×768，不是 Gemini API 文档所说的 1:1。

| 比例 @ 尺寸 | 实测像素 | Gemini API 像素表 |
| --- | --- | --- |
| 1:1 @512 | 512×512 | 512×512 |
| 1:4 / 4:1 @512 | 256×1024 / 1024×256 | 一致 |
| 1:8 / 8:1 @512 | 176×1456 / 1456×176 | 192×1536 / 1536×192 |
| 21:9 @512 | 784×336 | 792×168（疑似笔误） |
| 3:4 @512 | 448×592 | 448×600 |
| 2:3 @512 | 416×624 | 424×632 |
| 9:16 / 16:9 @512 | 384×688 / 688×384 | 一致 |
| 5:4 @1K、4:3 @1K | 1152×928、1200×896 | 一致 |
| 3:2 @2K | 2528×1696 | 一致 |
| 1:1 @4K | 4096×4096 | 一致 |

- 耗时与体积：512 档 6–13 s，整份响应 0.4–1 MB；1K 约 9 s、约 2 MB；2K 15.6 s、7.8 MB；4K 26.6 s、17.3 MB（JPEG 7.3 MB，thoughtSignature 约 7.5 MB）。thoughtSignature 随参考图增多而变大。
- usageMetadata 的 `candidatesTokenCount`：512 档 955–1278，1K 约 1510，2K 2073，4K 2894；Gemini API 文档每张为 747 / 1120 / 1680 / 2520。不开 `includeThoughts` 时 usage 没有单列思考 token。

## 额度

三次出现 429 `RESOURCE_EXHAUSTED`（reason `QUOTA_EXHAUSTED`，metadata.model 为本型号），`quotaResetTimeStamp` 依次为 19:39:50Z、00:39:50Z、05:39:50Z，按 5 小时窗口重置。完整观察的两个窗口分别出图 9 张、12 张后耗尽，两次累计输出 token 都在约 1.2–1.3 万时耗尽；只是两个窗口的观察，不能据此确定额度口径。配额检查早于参数语义校验：额度耗尽时非法比例也返回 429，而 JSON 未知字段仍返回 400。

## 上下文与参考价

- 未找到 Antigravity 对本型号公布的上下文窗口；Gemini API 模型页的 131,072 输入 / 32,768 输出属于另一产品，不继承。上下文记 unknown。
- 参考价取同平台 Gemini API Standard 付费档：输入 0.50 USD / 百万 token（文本与图片），文本与思考输出 3 USD，图像输出 60 USD。只作消耗示意，不是订阅扣费。
