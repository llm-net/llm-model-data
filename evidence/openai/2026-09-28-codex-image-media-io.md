# Codex 订阅：gpt-image-2 图像生成输入输出

基线：`e49d95e9063acab5a06d6afe60d80ed2bf328d8e`。在 codex 产品新增图像型号 `gpt-image-2`。

## 来源

| source ID | URL | UTC 时间 / 位置 | 用途 |
| --- | --- | --- | --- |
| codex-imagegen | https://learn.chatgpt.com/docs/image-generation.md | 2026-09-28T06:36:13Z；第 36–38、60–61 行 | 功能与型号 |
| codex-image-inputs | https://learn.chatgpt.com/docs/image-inputs.md | 2026-09-28T06:36:13Z；第 35–36 行 | 输入格式 |
| audit-codex-pricing | https://learn.chatgpt.com/docs/pricing | 2026-09-28T06:36:14Z；第 424 行 | Free 档不可用 |
| codex-imagegen-release | https://github.com/openai/codex/blob/rust-v0.158.0/codex-rs/ext/image-generation/src/tool.rs | 2026-09-28T06:23–06:34Z；tag rust-v0.158.0 → commit 064c6b8c737f5b41d171fdda80bd9ef10ad06eb3 | 官方客户端请求构造 |
| codex-images-backend | https://chatgpt.com/backend-api/codex/images/generations | 同上（`model-provider-info/src/lib.rs:77` 的 CHATGPT_CODEX_BASE_URL） | 端点 |
| codex-responses-backend | https://chatgpt.com/backend-api/codex/responses | 消费者板测记录，最后更新 2026-09-17T18:06:37Z | Responses 工具路径 |
| image-model-gpt-image-2、image-tool-reference | https://developers.openai.com/api/docs/models/gpt-image-2.md、…/api/reference/resources/responses/methods/create.md | 2026-09-28T06:37:57Z、06:38:43Z | API 对照，不继承 |
| image-pricing | https://developers.openai.com/api/docs/pricing.md | 2026-09-28T06:37:58Z；Image tokens Standard | 参考价 |

本次没有用任何账号实调；源码只读公开仓库，不提交程序或凭据。

## 官方客户端的出图路径

- 文档：CLI 在提示里写 `$imagegen` 调起图像生成，`-i` / `--image` 附参考图；「Built-in image generation uses `gpt-image-2` and counts toward your general Codex usage limits.」价格页：「Image generation isn't available on the Free plan.」输入「accepts common image formats, including PNG and JPEG」。文档没写可选型号、比例、尺寸、张数或输出格式。
- rust-v0.158.0（与 main@44fe510、rust-v0.159.0-alpha.12 的 tool.rs 相同）给对话模型暴露函数工具 `image_gen.imagegen`，参数 `prompt`、`transparent_background`（缺省 false）、`referenced_image_paths`（≤ 5 个绝对路径）、`num_last_images_to_include`（1–5），两种取参考图方式互斥。客户端本地执行它：
  - 无参考图 POST `{CHATGPT_CODEX_BASE_URL}/images/generations`，有参考图 POST `/images/edits`（`codex-api/src/endpoint/images.rs:62-83`），JSON 体。
  - 请求体只有 `prompt`、`background`（`transparent` / `opaque`）、`model: "gpt-image-2"`、`quality: "auto"`、`size: "auto"`；`n` 不发送（tool.rs:432-452、488-496；集成测试 `app-server/tests/suite/v2/imagegen_extension.rs:166-175` 断言同一请求体）。
  - 编辑的参考图放在 `images[]`，每项 `{"image_url": "data:<mime>;base64,…"}` 或 `{"file_id": …}`；PNG / JPEG / WebP 原字节透传，其他可解码格式先转 PNG（`utils/image/src/lib.rs`）。`MAX_EDIT_IMAGES = 5` 是客户端上限。
  - 只取响应 `data[0].b64_json`，存为 `.png`。
- commit 634ebc1（2026-09-09）的差异：没有 `transparent_background`，`background` 固定 `auto`；编辑只支持 `image_url`。
- rust-v0.143.0 为止客户端还向 Responses 请求挂托管工具 `{"type":"image_generation","output_format":"png"}`；自 rust-v0.144.0 起移除，官方客户端不再用 Responses 出图。

## 订阅端点行为（消费者板测）

以下摘自 LLM Gate 在开发板上的板测记录（最后更新 2026-09-17T18:06:37Z），使用一个 Codex 订阅账号，只在内存里检查状态、白名单元数据、图像容器与像素，不保存提示词、图片或响应正文；本次没有重跑。

Images 端点：`model` 写 `gpt-image-2.5-sunburst`、`gpt-image-2.5-flare` 或无效名称，都返回 200 与 PNG 1254×1254，响应没有服务端实际型号字段。

Responses 端点（`tools: [{"type": "image_generation", …}]`，`tool_choice` 钉死该工具，顶层 `model` 是承载的文本模型）：

| 工具对象写入 | 结果 |
| --- | --- |
| `output_format` = png / jpeg / webp | 采用 |
| `output_format=jpeg` + `output_compression=20` | 采用，体积约为缺省压缩的 2/3 |
| `size` = 1536x1024、1024x1536、1280x720、999x333、auto | 全部忽略，恒为 1254×1254 |
| `quality` = low / medium / high / xhigh / ultra | 不报错；条目回报的 quality 由后端自选，与请求无稳定对应 |
| `background=transparent` | 400 `invalid_value`：「Transparent background is not supported for this model.」 |
| 提示词后跟 `input_image` 参考图 | 可用 |
| 提示词尾部写比例（如 `Aspect ratio: 16:9.`） | 像素随之变化，总量约 157 万：1:1=1254×1254、16:9=1672×941、9:16=941×1672、4:3=1448×1086、3:4=1086×1448、3:2=1536×1024、2:3=1024×1536、2:1=1774×887、21:9=1916×821 |
| 提示词写透明背景 | PNG 真正透明（条目回报 transparent），WebP 仍不透明 |

返回的工具标识为 `gpt-image-2-codex`，`model` 写 2.5 型号名也不变；推理等级也不改变工具标识。因此本产品只收录 `gpt-image-2`，2.5 型号名只作说明。

## Images 2.5 的冲突

OpenAI 官方 X 帖（2026-09-08）称 Images 2.5「rolling out today to all ChatGPT, ChatGPT Work, and Codex users」；但 Codex 文档与 rust-v0.158.0 / main 源码仍写死 `gpt-image-2`，官方资料没有 Codex 内选择 Flare / Sunburst 的方法。发布文原页返回 403，未逐字核对。

## 上下文、思考与参考价

- Images 端点没有文本对话窗口，上下文记 not_applicable。
- 图像型号没有思考控制资料；承载文本模型的推理等级不改变图像型号，思考记 unknown。
- 参考价取同平台 OpenAI API `gpt-image-2` Standard（每百万 token）：文本输入 5、文本缓存 1.25、图像输入 8、图像缓存 2、图像输出 30 USD。计量词汇没有缓存图像输入，图像缓存价只写在说明里；官方注明缓存价只适用于 Responses 出图。
