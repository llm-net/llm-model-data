# 模型与价格更新任务

范围：填写服务商/产品；默认核对其catalog内全部模型与套餐。开始前记录Git commit。

必读 docs/CONTEXT.md：每个新增及已有模型都要查询本平台、本产品的官方上下文长度，填写 context_window_tokens 与独立 context_assessment；核实单位、常规 / 扩展窗口、套餐限制，不从原厂同名型号继承，不用输入上限或压缩阈值代替。查不到也写来源与原因，审阅报告持续列出全部 partial / unknown。

读取AGENTS.md、docs/PROTOCOLS.md、docs/REASONING.md、目标服务商README与provider.json。逐项核对官方模型ID、当前状态、已记录能力、每个模型的所有适用协议面及独立 interface_assessment、独立 reasoning（按协议与工具入口的思考参数、档位 / 预算、能否关闭、默认值及限制）、单一价格基准；订阅模型不调查实际扣费，先同平台按量价再开发方公开价。抓取失败、冲突、缺项都留下明确结论；不能跳过后标整家verified。

每模型最多一组价格，遵循docs/PRICING.md。聚合平台按docs/COLLECTION.md处理，不展开端点、不全量导入。保存URL、抓取时间和简短事实证据。金额用Decimal，未知不填0。

先查 schemas/excluded-providers.json：硅基流动与 Together AI 整家排除，不得从旧证据自动恢复；再按 provider.json 排除清单跳过已排除型号。对指定API短名核对同系列最新日期版本。

完成校验和必要测试，运行catalog.py review生成完整候选报告，给出本次修改、协议面与思考能力前后值和全部 partial / unknown 清单与候选SHA-256。待审核结果不得自动发布；已有明确授权且内容未变时不重复索取。

收到发布授权后按docs/RELEASE.md执行：确认后的提交推送至main，再创建并推送data-YYYY.MM.DD.N正式tag。只要求提交推送时不打发布tag；最新发布只从符合规则的远端tag中按日期和整数序号选取。
