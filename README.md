# llm-model-data

各大模型服务商的模型、协议面、思考能力、按量价格、订阅套餐与参考价格资料。**一份服务商数据，多种消费者；不按云平台 / 盒子分区。** 每个平台、产品、模型只有一组估算价格。已完成一轮公开资料核对，仍有明确缺项，正式版本以远端数据 tag 为准。

## 目录选择

**每个服务商一个目录，每个独立产品一个子目录、一个 catalog.json。** 单个服务商文件容易把按量和订阅混在一起；当前每个模型一个文件又太零碎。模型和自己的价格放在一起，阅读和 diff 都有上下文。

```text
providers/
  bailian/
    provider.json                  # 身份与官方资料入口
    README.md                      # 这家核价时需注意的差异
    offerings/
      api-cn/catalog.json          # 按量 API
      token-plan-cn/catalog.json   # API 订阅
      coding-plan-cn/catalog.json  # 另一个 API 订阅产品
  openai/
    offerings/api-global/catalog.json
    offerings/codex/catalog.json
  cursor/offerings/individual/catalog.json
schemas/                           # 严格 JSON Schema
evidence/                          # 核对记录与迁移证据
docs/                              # 数据语义、确认与自动更新设计
scripts/catalog.py                 # 校验、审阅包、确认内容检查
tests/                             # 数据边界回归测试
.github/                           # PR 模板与只读校验 CI
```

- [当前价格对齐结果与剩余缺项](docs/PRICE-ALIGNMENT.md)
- [首轮核对历史报告](docs/AUDIT-2026-09-16.md)
- [服务商索引](providers/README.md)
- [数据模型](docs/DATA-MODEL.md)
- [上下文长度维护（新增及更新必查）](docs/CONTEXT.md)
- [当前上下文长度核对结果](docs/CONTEXT-AUDIT-2026-09-16.md)
- [思考能力维护（每次更新必读）](docs/REASONING.md)
- [当前思考能力核对结果](docs/REASONING-AUDIT-2026-09-16.md)
- [协议面维护（每次更新必读）](docs/PROTOCOLS.md)
- [当前协议面核对结果](docs/PROTOCOL-AUDIT-2026-09-16.md)
- [统一估价与多模态计费](docs/PRICING.md)
- [聚合平台简化收录](docs/COLLECTION.md)
- [人工确认](docs/REVIEW.md)
- [数据版本发布与最新版本判定](docs/RELEASE.md)
- [Agent 自动更新](docs/AUTOMATION.md)
- [初始化范围](docs/BOOTSTRAP.md)
- [Agent 工作规则](AGENTS.md)

## 本地检查

Python 3.11+：

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/catalog.py validate
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/catalog.py review --base HEAD
```

本机若未安装 Python ensurepip，可用现成 uv 创建环境：`uv venv .venv --python /usr/bin/python3`，再 `uv pip install --python .venv/bin/python -r requirements.txt`。

审阅 .review/REVIEW.md、diff.patch、manifest.json。HEAD 应替换成**开始更新前**的 commit，不能拿更新后的 HEAD 当基线。工具不发布、不写远端、不调用消费者接口；review 仅生成草稿审阅包。

## 三条底线

1. 跨平台 / 产品即使同名同价，也完整重复记录，不做价格继承。
2. 未知不是免费；订阅统一按同平台按量价、其次开发方价格作参考，参考消耗不是额外应付金额；套餐费不除以额度冒充 token 单价。
3. 允许部分收录，但未知、缺失、未核对必须明示；消费者不能把 needs_review 当现行收费依据。
