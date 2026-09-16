# 思考能力核对结果（2026-09-16）

本轮在尚未发布的协议面候选上增加思考能力；此前整家移除硅基流动与 Together AI 的决定保持有效。

## 范围与结果

- 剩余18家服务商、28个产品、209条模型全部显式填写 capabilities.reasoning。3 条 complete、62 条 partial、144 条 unknown。
- 65条已有公开文档证明思考能力；其中部分产品只确认能力或 UI 档位，具体参数、缺省行为、范围或某些协议面仍待核对。其余144条明确保留未知，未按模态猜成不支持。
- 没有真实 Key 推理测试；verified 仅表示已核对所引用的公开资料。型号、协议面、价格、套餐及既有能力没有连带改动。
- 本轮重点覆盖 OpenAI / Codex、Claude / Claude Code、Cursor、DeepSeek、Kimi / Kimi Code、MiniMax API、百炼与智谱部分型号、Groq、Gemini、xAI 及 Hy 两个型号；未用 API 资料自动填充同名订阅。

## 服务商汇总

| 服务商 | 模型数 | complete | partial | unknown |
| --- | ---: | ---: | ---: | ---: |
| [anthropic](../evidence/anthropic/2026-09-16-reasoning.md) | 9 | 0 | 9 | 0 |
| [ark](../evidence/ark/2026-09-16-reasoning.md) | 42 | 0 | 0 | 42 |
| [bailian](../evidence/bailian/2026-09-16-reasoning.md) | 35 | 0 | 6 | 29 |
| [chenyu-ai](../evidence/chenyu-ai/2026-09-16-reasoning.md) | 29 | 0 | 0 | 29 |
| [cursor](../evidence/cursor/2026-09-16-reasoning.md) | 12 | 0 | 12 | 0 |
| [deepseek](../evidence/deepseek/2026-09-16-reasoning.md) | 4 | 2 | 0 | 2 |
| [gemini](../evidence/gemini/2026-09-16-reasoning.md) | 1 | 0 | 1 | 0 |
| [groq](../evidence/groq/2026-09-16-reasoning.md) | 2 | 0 | 2 | 0 |
| [hunyuan](../evidence/hunyuan/2026-09-16-reasoning.md) | 9 | 0 | 2 | 7 |
| [kling](../evidence/kling/2026-09-16-reasoning.md) | 6 | 0 | 0 | 6 |
| [minimax](../evidence/minimax/2026-09-16-reasoning.md) | 14 | 0 | 3 | 11 |
| [mistral](../evidence/mistral/2026-09-16-reasoning.md) | 2 | 0 | 0 | 2 |
| [moonshot](../evidence/moonshot/2026-09-16-reasoning.md) | 8 | 0 | 8 | 0 |
| [openai](../evidence/openai/2026-09-16-reasoning.md) | 7 | 1 | 6 | 0 |
| [openrouter](../evidence/openrouter/2026-09-16-reasoning.md) | 1 | 0 | 0 | 1 |
| [qianfan](../evidence/qianfan/2026-09-16-reasoning.md) | 9 | 0 | 0 | 9 |
| [xai](../evidence/xai/2026-09-16-reasoning.md) | 4 | 0 | 2 | 2 |
| [zhipu](../evidence/zhipu/2026-09-16-reasoning.md) | 15 | 0 | 11 | 4 |

## 后续核对

逐模型缺项在各家的证据文件及 catalog.json 的 reasoning.notes 中；catalog.py review 每次都会列出所有思考能力 partial / unknown，包括没有发生变化的记录。后续优先补：

- 各协议面的参数、预算与默认值，避免把已核对的一个面当成该模型的全部控制方式。
- Codex 每个型号的完整档位与默认值；通用配置表、某一型号的选择器示例不能证明其他型号的可选集。
- Cursor 私有 RPC 参数及套餐限制；官方 UI 标签可展示，parameter=null 时不能生成请求。
- 尚无型号级思考证据的方舟、晨羽、千帆、聚合别名、多模态型号及其余订阅产品。
- 来源冲突：xAI Grok 4.5 模型页与思考专文对 xhigh 的表述不同，保留专文说明和双方一致的独立档位，不将其静默当第四档。

## 验证与维护

结构 / 语义校验、默认值与类型、预算边界 / 哨兵值、来源隔离、协议范围、历史可读性与候选报告均有测试。对比本轮编辑前的209条模型记录，移除新 reasoning 字段后全部相等；旧协议核对与价格没有刷新时间或改值。

规范见 [REASONING.md](REASONING.md)。维护入口已同步至 AGENTS.md、数据模型、自动化、协议维护、审核文档、各服务商 README 与更新 / PR 模板。此候选未发布，消费者尚需独立适配该字段。
