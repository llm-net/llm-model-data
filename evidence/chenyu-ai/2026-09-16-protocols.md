# 晨羽AI 协议面专项核对

核对日期：2026-09-16，UTC 2026-09-16T12:14:31.226871Z。读取匿名公开文档与发布目录，无真实 Key 推理调用。

## 来源

- `protocol-models`：https://chenyu.pro/api-docs/docs/models/
- `protocol-images`：https://chenyu.pro/api-docs/docs/images/
- `protocol-quickstart`：https://chenyu.pro/api-docs/docs/quickstart/
- `protocol-messages`：https://chenyu.pro/api-docs/docs/anthropic-messages/
- `protocol-responses`：https://chenyu.pro/api-docs/docs/openai-responses/
- `protocol-catalog`：https://chenyu.pro/catalog/platform-models.json

## 页面位置、冲突与边界

- 模型目录「图片模型」「视频模型」「语音模型」按精确 ID 给出面与入口；「文本模型」只列模型，明确实际面以登录控制台徽标为准，未提供匿名逐型号矩阵。
- 图片生成页「已登记模型」明确两款 Seedream 使用 OpenAI Images Generations，且当前未开放图片厂商协议面。匿名发布目录 v25 仍标 ark_image；新 API 专文优先，不把旧标记传播回新数据。
- 快速上手的 Chat / Messages 请求与 Messages 专文都示例 deepseek-v4-flash。Responses 专文「哪些模型在这一面上」说 DeepSeek 没有此端点，但请求示例使用同一 ID；记录冲突，不用单个示例证明支持。
- 匿名目录只提取 chenyu_ai 模型公开字段，未复制完整目录、消费者配置或其他平台数据。目录正文 SHA-256：`ebbc1f787e937f6644ded7eeeea612d8cfc340d3f2f5d23a38e1cb0299ee3543`。
- 原审计留下的模型身份 / 价格 verification 保持原时间与结论；本轮仅补协议面的独立核对，不将文档清单等同于实时调用成功。

## 逐模型结果

| 模型 ID | 协议面 | 覆盖 | 来源 ID 后缀 | 限制 / 结论 |
| --- | --- | --- | --- | --- |
| `deepseek-v4-pro` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `deepseek-v4-flash` | `openai_chat`, `anthropic_messages` | partial | models, quickstart, messages, responses | 快速上手与 Messages 页按此精确 ID 展示 Chat / Messages 请求。Responses 页一处说 DeepSeek 不支持、另一处示例却用此 ID，存在冲突；不据示例登记 Responses，待公开协议矩阵澄清。 |
| `deepseek-v4-flash-vision-exp` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seed-2-1-pro-260628` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seed-2-1-turbo-260628` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seed-2-0-lite-260428` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seed-2-0-mini-260428` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seed-2-0-pro-260215` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `doubao-seedream-5-0-pro-260628` | `openai_image` | complete | models, images, catalog | 当前公开模型目录「图片模型」与「图片生成」明确两款 Seedream 走 OpenAI Image。匿名目录 v25 的 ark_image 为旧标记，按当前具体 API 文档取值；不新增方舟原生图片面。 |
| `doubao-seedream-5-0-260128` | `openai_image` | complete | models, images, catalog | 当前公开模型目录「图片模型」与「图片生成」明确两款 Seedream 走 OpenAI Image。匿名目录 v25 的 ark_image 为旧标记，按当前具体 API 文档取值；不新增方舟原生图片面。 |
| `doubao-seedance-2-5-260628` | `ark_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `doubao-seedance-2-0-260128` | `ark_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `doubao-seedance-2-0-mini-260615` | `ark_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `qwen3-8-max` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `qwen3-7-plus` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `qwen3-8-flash` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `qwen3-7-flash` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `qwen3-8-27b` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `wan3-0-video` | `bailian_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `wan3-0-video-prime` | `bailian_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `minimax-m3` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `minimax-h3` | `minimax_video` | complete | models, quickstart, catalog | 公开模型目录「视频模型」逐项列此 ID 及厂商任务入口，与匿名发布目录对应；不是 OpenAI Chat。 |
| `speech-2-8-hd` | `minimax_speech` | complete | models, quickstart, catalog | 公开模型目录「语音模型」明确 speech-2.8-hd / turbo 走 MiniMax T2A；匿名旧目录 minimax_audio 按规范名归一为 minimax_speech。 |
| `speech-2-8-turbo` | `minimax_speech` | complete | models, quickstart, catalog | 公开模型目录「语音模型」明确 speech-2.8-hd / turbo 走 MiniMax T2A；匿名旧目录 minimax_audio 按规范名归一为 minimax_speech。 |
| `glm-5-3` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `glm-5-3-flash` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `kimi-k3` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `qwen-qwen3-8-27b-fp8` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
| `nvidia-qwen3-6-35b-a3b-nvfp4` |  | unknown | models | 公开「模型目录」列出此 ID，但明确文本模型各面以控制台运行态徽标为准，未公布逐模型协议矩阵。平台有通用入口不证明本型号开放；保留未知，不能从采购厂商或其他部署推导。 |
