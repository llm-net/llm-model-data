# 每模型一个价格基准

## 统一口径

每个 `provider / offering / model` 最多一组价格。输入、缓存读取、输出、输入图片等是这一组里的计费分量，可以相加；循环分时价在同一规则的 `time_pricing` 内表达；分辨率、长上下文、供应端不生成第二套规则。

价格是**公开报价中选定的估算基准**。`selection` 用一句话写清选了哪个标准档；固定价模型按该基准初算；分时模型由消费端按明确的记账时刻选择时段。它不保证每个调用的真实账单都等于估算。

选择顺序：本产品公开标准在线价 → 常规短上下文 / 默认画质 → 非临时促销价。分时模型完整记录峰谷，首档选高峰；永久降价采用降价后的价格。没有证据就保留 unknown，不能采用最低价、训练方价格或同名产品价格来补洞。

## DeepSeek 随时间变价

catalog schema_version=2 在同一 rule 内保存 `time_pricing`，时区为 `Asia/Shanghai`，bands 各带完整 rates；按序首个匹配者胜，末档为无条件兜底。days 使用 ISO 星期（1–7），hours 是当天半开区间（不跨午夜，可拆两段），所有档的 meter 集合相同。rule.rates 必须等于首档，仅作基准投影。每天跨峰谷不更新文件，消费者按本笔时刻选档；跨时段请求的官方 time_basis 未知时保留 unknown，不能猜成官方规定。

官方调整基准时：Agent 重新核对，更新这一组数字，生成价格前后差异交人确认。旧价留在 Git 历史，不在当前模型里并排放多个版本。官方已公告但尚未生效的价格先写证据与提醒，到期复核后替换。

`verification.checked_at` 是资料核对时间；`effective_from / effective_until` 只填证实的生效时刻，不知道就 null。二者不能互相替代。历史账单要使用消费者当时固定的数据版本，不能拿今天的目录重新结算。

## 图像、视频、语音

| 模型类型 | 唯一基准示例 | 计量注意 |
| --- | --- | --- |
| 图像生成 | 标准规格每张 | 使用实际出图张数，不把图片理解写成图片生成 |
| 秒计费视频 | 常规分辨率每秒 | 输入与输出视频若都收费，分别保存分量 |
| token计费视频 | 常规规格每百万视频token | 使用厂商视频usage，不能替换为文本token或按秒猜算 |
| 语音合成 | 每万厂商计费字符 | 汉字、字母的权重按该厂商定义，不等于UTF-8字节 |
| 音频识别 | 每秒 / 每分钟 / 音频token | 保留原计量口径，不硬转成文本输入价 |

数量元数据 `quantity` 保留已确认的字段、免费量和取整；未知项写 null / unknown。账号首次试用额度不能写成每次请求免费量。收费事件不清楚时 `charge_on=unknown`。

例如 MiniMax H3 选择768p：输出0.5元/秒、输入视频0.5元/秒、超过5张的输入图0.2元/张。这是一组基准的三个分量，2K或重生成的其他规格不展开。

## 订阅模型统一使用按量参考价

不核对订阅模型实际扣费、积分折算、额度消耗或超额收费。所有API订阅、开发工具订阅都令usage_prices=not_applicable，仅在reference_prices保存一组价格：

1. 优先取同平台对应型号的按量价格，先查平台完整官方价表，而不是只查本仓库的部分API清单。
2. 该平台没有对应按量价时，再取开发这个模型的源头公司的公开按量价。
3. 两边均无对应型号价格时写unknown；用户明确指定其他参考型号时可记录为近似示意价，必须说明不代表官方同价。

来源型号、URL、同平台/原厂选择理由写进reference_origin；价格数字完整独立保存。这里表示“按量标价等价消耗”，不是订阅实际成本。既有plans套餐资料单独保留，不参与模型单价计算；本流程不追加订阅真实收费调查。

明确映射：Kimi Code的k3、k3-256k按kimi-k3，highspeed按kimi-k2.7-code-highspeed。kimi-for-coding底模仍为K2.8 Preview，用户已明确指定按kimi-k2.7-code公开按量价做示意；不是K2.8官方报价。

用户指定：OpenCode Go 全部型号取模型源头厂商官网公开按量价（中国厂商取国内官网人民币价，不换汇），不采用 Go 文档的用量上限换算价或 Zen 余额价；开发方按量目录已收录时保存 `catalog_model`。Grok Build 的 grok-4.7-build-fast 取 xAI 官网单列的 Grok 4.7 Fast 费率，它不是公开 API 型号，只登记 URL。

Codex统一采用OpenAI API现金标价；GLM Coding Plan采用智谱API现金标价，不能继续保留原CREDIT价格。Cursor Composer采用同平台公开的Standard按量费率。

## API短名对齐日期版

用户指定：方舟doubao-seedance-2.5、2.0、2.0-fast、2.0-mini，以及千帆deepseek-v4-pro、deepseek-v4-flash，价格参考同平台同系列最新日期后缀版本。

当前选取：Seedance分别为260628、260128、fast-260128、mini-260615；千帆Pro为0813、Flash为0731。后续从官方目录确认完整日期再比较，不跨系列选版本。已有短名保留请求ID，新条目请求名未证实则为 null；价格放reference_prices，reference_origin写选定日期版。估价映射不声明实际调用路由等价。

## 聚合平台

OpenRouter使用公开模型目录该行的pricing。硅基流动与 Together AI 已整家排除，不再更新其价格。仅保留模型级估价，不维护路由供应端。具体收录方式见[COLLECTION.md](COLLECTION.md)。

## Seedance 标准价与促销示例

Seedance 四个系列均保存显式 `catalog_model` 来源，按量短名与 Agent Plan 独立存价。标准基准为在线、720p、无参考视频、非限时优惠刊例价；Mini 23 元/百万视频 token 不应被促销的“约 0.2 元/秒”替换。按任务 `usage.completion_tokens` 取量，只在成功生成时收费；含参考视频的单价与最低用量不能套入这一基准。详见[核对记录](../evidence/ark/2026-09-17-prices-and-names.md)。
