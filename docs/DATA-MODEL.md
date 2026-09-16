# 数据模型 v1

## 身份

provider 是售卖 / 提供模型服务的平台，不要求是训练方。offering 是可独立购买或接入的产品，kind 为 pay_as_you_go / api_subscription / tool_subscription。API 订阅可能只准编程工具使用，分类不推断使用许可。

国内外站分别建 offering；档内只选一个标准价格基准，其余差异写selection与notes。market=unconfirmed 表示尚未核清，不代表全球通用。

模型唯一键是 provider_id / offering.id / model.id。本地 id 可读、稳定；request_id 是实际请求名，未知为 null。不同产品可以有不同模型、名称和能力。alias_of 只指本产品的模型，别名也完整保存自己的价格，不隐式继承。

modalities 记录输出 / 服务类型，不把图片理解误当作图片生成。可选 capabilities 保存输入模态、上下文 / 输出上限、工具调用、结构化输出、流式和接口类型；null / 空列表表示尚未核对，不表示不支持。这些能力只属于当前产品，同名模型不继承。

## 三种价格

| 字段 | 含义 |
| --- | --- |
| models[].usage_prices | 按量产品公开用量价中选定的估算基准；订阅固定not_applicable |
| models[].reference_prices | 订阅模型和指定短名的按量参考价，独立保存完整数字 |
| plans[].prices | 独立套餐的标准月付售价 |

每个 price set 有 status、rules、verification、notes。published 表示来源发布了数字，**不是人工已批准**。unknown / not_applicable 时 rules 必须为空；未知和不适用要写原因。零价必须有来源。

usage 的 basis 只允许 public_list / provider_credit_rate；reference 只允许 reference；套餐只允许 subscription_fee。provider_credit_rate是保留的价格基础词汇；当前订阅策略禁止在模型记录中保存这种实际额度费率。订阅模型只允许reference_prices，不允许CREDIT币种。

参考 rule 必须有 reference_origin：URL、对象文字、选择理由。数值完整保存在本条中，来源仅作证据，没有引用继承。上游参考对象改价，生成本产品自己的变更提案。订阅固定优先同平台按量价，缺价再选模型开发方；具体映射见[PRICING.md](PRICING.md)。

## 规则

- currency：原币种三字母代码；CREDIT 是该产品私有额度单位，不能跨产品相加。
- rates：meter、十进制字符串 amount、整数 per、unit。例如 input_uncached_tokens / "2" / 1000000 / token。
- meter / unit 词汇真源是 schemas/meters.json；多模态数量口径、免费量和数量舍入放在 rate.quantity。
- selection：唯一基准的选择口径，例如常规高峰或720p无声；是供人理解的说明，不是运行时条件。
- effective_from / effective_until：带时区的官方半开有效区间，未知为 null。不能用 checked_at 替代。
- time_basis / charge_on：用哪个事件时刻选价、何种事件收费；两者未知时显式 unknown。
- tax：included / excluded / unknown，不按币种猜税。
- verification：规则自己的来源、核对时间和证据。

每个模型 usage_prices 与 reference_prices 合计最多一条 rule，且没有 conditions、schedules、routes。保留 rules 数组是格式容器，maxItems=1，不允许借此恢复多档。每个套餐也只存一组标准月付价；不同档位分别建plan。

一条rule里的rates是可相加的不同计费分量。缓存读取、未命中输入和缓存写入不得重复统计同一批token。未记录的费率分量是未知，不能当作0。

金额不存浮点，不统一换人民币。缓存计量是否包含在输入总量、缓存 TTL、阶梯判据等在 meter / notes / 证据里明确，不能根据模型名猜测。

## 套餐

plan 独立记录 prices、quotas、overage、verification。套餐价格 rule 的 billing_period 是实际购买周期（P1M / P1Y 等），charge_unit 是 account / seat；年付存全年应付金额，不存“每月折合”。

quota：metric、limit 十进制字符串、unit、window（rolling / calendar / billing_cycle / unknown，duration、timezone、anchor）。5 小时、周、月约束独立，不能相加。绝对量未知为 null；不限量附公平使用说明，不能编巨大数字。

overage：blocked / pay_as_you_go / add_on / unknown，是否默认开启和细节记 notes。模型 plan_ids 为空表示档位尚未核对，不代表所有套餐可用。

## 证据与版本

verification.status=verified 必须有 checked_at、source_ids 和存在的本地 evidence；needs_review 的 checked_at 为 null。模型能力、用量价、参考价、套餐逐项核对，不能因网页可打开就验证整家。coverage=partial 表示部分收录，不意味着列表外不可用。

schema_version 是格式版本，Git commit / tag 是资料版本，SHA-256 是确认对象。消费者拥有自己的激活状态和账本；本仓库不存渠道、利润率、余额和环境开关。

## 当前草案

v1尚未正式发布，本次按用户确定的单一基准简化；首次正式发布后的破坏性变化需提升格式版本。详细口径见[PRICING.md](PRICING.md)，聚合平台收录见[COLLECTION.md](COLLECTION.md)。

## 排除项

provider.json可有excluded_request_ids字符串数组；用户明确排除的请求ID不得重新收录。SiliconFlow额外禁止retired模型留在catalog。排除项变更随数据审阅。
