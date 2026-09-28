# 媒体输入输出契约

非文本模型（图像、视频、语音、音乐）的生成接口各不相同：能收哪些输入、能调哪些参数、会产出什么，逐厂商、逐型号都有差别。`capabilities.media_io` 按本产品、本型号记录这份**厂商事实**，供消费者据以构造请求与界面。它与价格、协议面、上下文一样有独立证据和核对结论。

## 边界

- 只记厂商原样的接口事实：字段路径、取值、缺省、上限与产物形态。**不跨厂商归一**：不发明统一的 `voice`、`duration`、`size`，参数名就是厂商请求体里的字段路径。
- 不记消费者策略（界面开放哪些参数、只收浏览器能播放的格式等），不记请求拼装算法、轮询或错误解析逻辑。这些属于消费者的适配代码。
- 只记本产品文档写明的内容。同名型号在另一个产品（按量 / 订阅 / 聚合平台）的契约不继承；聚合平台必须按它自己的文档核对，即便它声称原样转发厂商接口。
- 纯文本模型（`modalities` 只有 `text`）不带本字段；其余模型必须带，未核对时写 `status: unknown`。

## 结构

```text
media_io
├─ status        known | partial | unknown
├─ operations[]  每种生成操作一项（文生视频、图生视频、图像编辑、语音合成……）
│  ├─ id         小写蛇形，本模型内唯一，如 text_to_video、image_to_video、image_generation、speech_synthesis
│  ├─ interface  所用协议面，必须在 capabilities.interfaces 里
│  ├─ endpoint   "METHOD /路径"，厂商站点根之后的官方路径；WebSocket 写 WSS
│  ├─ mode       sync（一次返回）| async_task（先受理后查询）| stream（分块 / 流式返回）
│  ├─ inputs[]   模型消费的内容（文本、图像、视频、音频）
│  ├─ outputs[]  产物
│  └─ params[]   控制项
├─ verification  本字段独立的来源、核对时间与证据
└─ notes         覆盖范围与缺项
```

- `known`：本产品文档对该型号在所列协议面上公开的操作、输入、输出与参数都已记录。不承诺厂商以后不加参数。
- `partial`：已核对部分内容，缺口（没找到的参数、型号适用范围不明、文档冲突）必须写进 `notes`，操作或参数自己的 `notes` 也要说明。
- `unknown`：尚未核对或找不到可用文档；`operations` 为空，`verification.status` 为 `needs_review`。不能解释为「没有输入输出限制」。

### 字段路径

`field` 用请求体根开始的点路径：

- `a.b.c` 是嵌套对象字段；`a[]` 是数组元素；`a[k=v]`、`a[k1=v1,k2=v2]` 是数组里对应键取给定值的元素，例如方舟视频的 `content[type=image_url,role=first_frame].image_url.url`。
- 请求头写 `header:<名称>`，查询参数写 `query:<名称>`，multipart 表单字段写 `form:<名称>`。
- 选模型的字段（`model`，或豆包语音的 `header:X-Api-Resource-Id`）不记为输入或参数。
- 同一个字段只能是输入或参数之一。

### 输入 `inputs[]`

| 字段 | 含义 |
| --- | --- |
| `role` | 内容角色，见下表 |
| `field` | 字段路径 |
| `required` | 该操作是否必填 |
| `min_items` / `max_items` | 可重复内容（多张参考图）的数量范围；单值写 `null` / `1` |
| `formats` | 文件格式，小写扩展名或编码名（`png`、`jpeg`、`mp4`、`mp3`、`wav`）；文本输入为空列表 |
| `transports` | 传入方式：`inline`（文本直接写在请求体里）、`url`、`base64`（裸 base64）、`data_uri`、`file_id`（厂商上传接口返回的 id）、`asset_id` |
| `limits` | 上限 / 下限，见「限制」 |

| role | 用途 |
| --- | --- |
| `prompt` | 生成提示词 |
| `negative_prompt` | 反向提示词 |
| `text` | 要朗读 / 合成的正文（语音合成） |
| `lyrics` | 歌词（音乐） |
| `first_frame` / `last_frame` | 视频首帧 / 尾帧图 |
| `reference_image` / `reference_video` / `reference_audio` | 参考素材（风格、主体、音色、配乐） |
| `source_image` / `source_video` / `source_audio` | 被编辑、延长或续写的原素材 |
| `mask` | 局部编辑遮罩 |
| `source_task` | 引用本平台先前任务（如方舟 Seedance 的样片任务 ID），产物由厂商侧取用 |

### 输出 `outputs[]`

| 字段 | 含义 |
| --- | --- |
| `media` | `image` / `video` / `audio` / `text`（字幕、时间戳等附带产物） |
| `formats` | 产物格式 |
| `delivery` | 取回方式：`url`（厂商临时地址）、`base64`、`hex`（十六进制编码，放在 JSON 响应里）、`stream`（分块流）、`file_id` |
| `max_items` | 单次请求最多产出几份；未知写 `null` |
| `url_ttl_seconds` | 产物地址有效期（秒）；无地址或未写明写 `null` |
| `limits` | 产物规格范围，如时长、宽高、采样率 |

### 参数 `params[]`

| 字段 | 含义 |
| --- | --- |
| `field` | 字段路径 |
| `type` | `enum`（字符串取值集合）、`integer`、`number`、`boolean`、`string`、`string_list` |
| `values` | `enum` 的全部取值；`integer` 的离散取值（如采样率）；`string_list` 的可选项。其余为 `null` |
| `values_ref` | 可省略。引用本文件 `media_value_sets` 里的共享取值集，代替 `values`（两者只能填一个） |
| `min` / `max` | `integer` 用整数；`number` 用十进制字符串；`string` 为长度、`string_list` 为项数（整数）。与 `values` 二选一 |
| `unit` | 数值单位：`second`、`millisecond`、`pixel`、`hertz`、`fps`、`percent`、`byte`、`character`、`item`、`ratio`、`bit_per_second`；非数值参数为 `null` |
| `default` | 厂商文档写明的缺省（不传时的行为）；文档没写为 `null` 并在 `notes` 说明 |
| `required` | 是否必填 |

音色、风格等取值列表记该型号可用的全部官方系统取值；账号私有取值（复刻音色）不列举，只在 `notes` 说明取值方式。

### 共享取值集 `media_value_sets`

长列表（系统音色、语种）和多个操作、多个型号共用的列表，放在 `catalog.json` 顶层的 `media_value_sets`，参数用 `values_ref` 引用，不在每个参数里重复：

```json
"media_value_sets": {
  "seed-tts-2-0-voices": {
    "values": ["zh_female_vv_uranus_bigtts", "zh_male_m191_uranus_bigtts"],
    "labels": {"zh_female_vv_uranus_bigtts": "Vivi 2.0", "zh_male_m191_uranus_bigtts": "云舟"},
    "verification": {"status": "verified", "checked_at": "…", "source_ids": ["…"], "evidence": "evidence/…", "notes": "…"},
    "notes": "豆包语音合成模型 2.0 可用的官方系统音色。"
  }
}
```

- 键名小写、连字符或下划线，本文件内唯一；每个集合必须被至少一个参数引用。
- `values` 全为字符串或全为整数；`labels` 是厂商官方展示名（取值 → 名称），没有写 `null`，只能标注集合内的取值。
- 集合有自己的 verification；同一集合被多个型号引用，表示这些型号的文档给出的是同一份列表，型号间有差别就分开建集合。
- 小的枚举（几个取值）直接写在参数的 `values` 里，展示名可写进参数 `notes`。

### 限制

`limits[]` 每项 `measure`、`min`、`max`（十进制字符串，至少一端非空）、`unit`、`notes`：

| measure | unit |
| --- | --- |
| `file_size` | `byte` |
| `width` / `height` / `pixels` | `pixel` |
| `aspect_ratio` | `ratio`（宽 / 高的十进制值） |
| `duration` | `second` / `millisecond` |
| `length` | `character`（文本） |
| `count` | `item` |
| `fps` | `fps` |
| `sample_rate` | `hertz` |
| `bitrate` | `bit_per_second` |

同一对象内 `measure` 不重复。字符上限按厂商口径（字符、字节或 token）写明在 `notes`，不能换算。

文件大小等以 KB / MB 写出的上限，与 [CONTEXT.md](CONTEXT.md) 的 K / M 规则同一口径：只有厂商写明换算关系（给出字节数，或写明 1MB=1024KB 之类）时才换成 `byte` 记进 `limits`，并在该限制的 `notes` 写依据；否则不记 `file_size`，把原文（如「不超过 10MB」）写进该输入的 `notes`。不得自行约定十进制或二进制。

## 示例

```json
"media_io": {
  "status": "partial",
  "operations": [{
    "id": "speech_synthesis",
    "interface": "ark_tts",
    "endpoint": "POST /api/v3/plan/tts/unidirectional",
    "mode": "stream",
    "inputs": [{"role": "text", "field": "req_params.text", "required": true, "min_items": null, "max_items": 1,
                "formats": [], "transports": ["inline"], "limits": [], "notes": "官方未写数值上限，超限报 40402003。"}],
    "outputs": [{"media": "audio", "formats": ["mp3", "ogg_opus", "pcm"], "delivery": ["stream"], "max_items": 1,
                 "url_ttl_seconds": null, "limits": [], "notes": "逐行 JSON，data 为 base64 音频块。"}],
    "params": [
      {"field": "req_params.speaker", "type": "enum", "values": ["zh_female_vv_uranus_bigtts"], "min": null, "max": null,
       "unit": null, "default": null, "required": true, "notes": "zh_female_vv_uranus_bigtts：Vivi 2.0。"},
      {"field": "req_params.audio_params.sample_rate", "type": "integer", "values": [8000, 16000, 24000, 48000],
       "min": null, "max": null, "unit": "hertz", "default": 24000, "required": false, "notes": null}
    ],
    "notes": null
  }],
  "verification": {"status": "verified", "checked_at": "2026-09-28T03:00:00Z", "source_ids": ["agent-plan-voice"],
                   "evidence": "evidence/ark/2026-09-28-media-io.md", "notes": "仅核对 HTTP 单向流式。"},
  "notes": "WebSocket 接口未记录。"
}
```

## 更新步骤

1. 列出所更新产品的每个非文本模型，包括日期版、短名与聚合平台条目。
2. 查该产品官方 API 参考与型号支持表：每个型号支持哪些操作（文生、图生、首尾帧、参考、编辑、延长），每个操作的字段、取值、缺省、上限与产物形态。型号差异（某分辨率只有某型号支持）必须按型号分开记，不能把整族的最大集合复制给每个型号。
3. 在 `evidence/<provider>/` 记录 URL、UTC 抓取时间、页面小节、结论、冲突与缺项；来源 ID 须在 provider.json 登记。
4. 填写 `media_io` 与独立 `verification`；查不到的写 `partial` / `unknown` 并说明。
5. 运行 `python scripts/catalog.py validate`、单元测试与 `review`；审阅报告的「媒体输入输出待核对清单」列出全部 partial / unknown。
