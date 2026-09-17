# DeepSeek 分时段价格复核

核对时间（UTC）：2026-09-16T18:11:35.617731Z。只使用官方公开资料，未进行付费 API 调用。

来源：https://api-docs.deepseek.com/zh-cn/quick_start/pricing/ ，模型表、价格行与脚注 (1)–(3)。

- deepseek-flash（DeepSeek-V4.1-Flash）及仍可调用的 deepseek-v4-flash、deepseek-v4-flash-vision-exp：每百万 token 高峰输入 2 元、缓存命中 0.04 元、输出 8 元；空闲依次 1 / 0.02 / 4 元。
- deepseek-v4-pro 当前仍为 DeepSeek-V4-Pro-0813，官方脚注已明确继续提供服务、计费不变；高峰输入 9 元、缓存命中 0.30 元、输出 27 元；空闲 4.5 / 0.15 / 13.5 元。没有按早先新闻中的改路由预告覆盖现行表格。
- 作息按北京时间周一至周五 09:00–12:00、14:00–18:00 为高峰，其余（包括周末）为空闲。实现使用半开区间，跨午夜需拆分；不推导法定节假日调休。
- 官方本页没有明确跨时段请求按开始、结束或逐 token 计时；保留 time_basis=unknown，消费者自己的时刻口径必须明确，不声称复刻官方跨边界账单。
- 本轮同时复核上下文原始标称仍为 1M、输出 384K；未证实上下文整数单位，沿用原 partial assessment 与历史值，不刷新成 known。
- 价格表仍列 Chat、Responses、Anthropic 三面及思考/非思考。核查 Chat 参数页面 https://api-docs.deepseek.com/api/create-chat-completion/ 的 thinking 与 reasoning_effort 段；其他能力保留独立证据，不以价格核对刷新成功日期。Responses / Anthropic 英文 guides URL 本次读取失败，不将失败当作下线或覆盖既有结论。

schema_version=2 增加规则内 time_pricing；规则 rates 与首档相同，仅作固定价兼容投影。高峰金额未变，新增完整空闲档及作息。候选需按仓库 review 流程审核，尚未发布。
