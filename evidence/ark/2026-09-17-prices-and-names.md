# 方舟 — Seedance 价格和名称兼容

范围：API 的 Seedance 2.5 / 2.0 / Fast / Mini 日期版与短名、Agent Plan 同系列四条。不改文本、图像或套餐价格；未实调。

## 本次官方来源

- `catalog`：https://www.volcengine.com/docs/82379/1330310；UTC 2026-09-17T10:27:43.962Z；浏览器渲染正文成功。
- `pricing`：https://www.volcengine.com/docs/82379/1544106；UTC 2026-09-17T10:27:45.901Z；浏览器渲染正文成功。
- `protocol-video`：https://www.volcengine.com/docs/82379/1366799；UTC 2026-09-17T10:27:49.851Z；浏览器渲染正文成功。
- `audit-rendered-agent`：https://www.volcengine.com/docs/82379/2366394；UTC 2026-09-17T10:27:42.899Z；浏览器渲染正文成功。
- `protocol-agent`：https://www.volcengine.com/docs/82379/2373738；UTC 2026-09-17T10:27:41.966Z；浏览器渲染正文成功。

来源 ID 的既有等价入口：protocol-models / context-ark-models 对应 catalog，context-ark-agent 对应 Agent Plan 支持表。每条分别维护能力与价格 verification。

## 价格

价格页“视频生成模型 / 按 token 单价”确认标准在线、720p、无参考视频的刊例价：

| 系列 | 目录确认日期版 | CNY / 百万视频 token |
| --- | --- | ---: |
| 2.5 | doubao-seedance-2-5-260628 | 70 |
| 2.0 | doubao-seedance-2-0-260128 | 46 |
| 2.0 Fast | doubao-seedance-2-0-fast-260128 | 37 |
| 2.0 Mini | doubao-seedance-2-0-mini-260615 | 23 |

此次数字未发生降价。Fast / Mini 的企业限时折扣分别为刊例价的 75% / 40%，有资格、日期和用量上限条件，不替代长期基准。Mini 页面“约 0.2 元/秒”是促销和分辨率下的示例，不是 API 每秒固定费率。2.5 的 1080p 促销截至北京时间 9 月 17 日 14:00，抓取时页面仍展示该文字；本次 720p 基准不涉及它，不声称促销仍有效。

无参考视频的 token 单价不能用于含参考视频任务。官方说明用量取 usage.completion_tokens，仅成功任务计费；含参考视频时有不同单价、最低用量，且计费 token 可包含参考视频。保存原视频 token meter，明确成功收费，补充基准适用边界；不增加输入分量重复收费，不按秒反推 token。

## 身份、兼容与缺项

- 官方“视频生成能力”的 Model ID 表确认四个日期版本。此前 Fast 日期版缺条目，现补入。
- 价表与 Agent Plan 用点号系列名（如 doubao-seedance-2.0-mini），本仓库稳定本地 ID 用连字符（doubao-seedance-2-0-mini）。这两个字段不应通过全局字符替换互相推算。
- API Mini 短名此前整条缺失，现新增稳定本地 ID 和参考价；公开 API 示例与 Model ID 表只证实日期版请求 ID，短名 request_id=null / availability=unknown。既有 API 点号短名原值保留，身份改为 needs_review，协议 partial，明确未证明可直接请求。没有将价格参考设置为 alias_of。
- Agent Plan 的四个点号请求名由其独立支持表确认，视频需 Large / Max；协议接入仍按已有 Agent Plan 范围，不能把 API Key 产品能力直接搬入。
- API 日期版确认 ark_video 异步创建与查询；三种文本面不适用。短名保留系列视频面和未核实请求身份限制。生成任务不适用文本对话窗口。全部 Seedance 的逐型号思考控制仍 unknown；未发现参数不能当不支持。
- 每个短名参考同平台同系列最新实际日期版，完整保存数字。reference_origin.catalog_model 绑定 provider / offering / model 和 latest_dated 策略；新增日期版后旧指向将校验失败，必须复核和独立更新，不能运行时悄悄换价。
