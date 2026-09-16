# 模型与价格更新任务

范围：填写服务商/产品；默认核对其catalog内全部模型与套餐。开始前记录Git commit。

读取AGENTS.md、目标服务商README与provider.json。逐项核对官方模型ID、当前状态、已记录能力、单一价格基准；订阅模型不调查实际扣费，先同平台按量价再开发方公开价。抓取失败、冲突、缺项都留下明确结论；不能跳过后标整家verified。

每模型最多一组价格，遵循docs/PRICING.md。聚合平台按docs/COLLECTION.md处理，不展开端点、不全量导入。保存URL、抓取时间和简短事实证据。金额用Decimal，未知不填0。

按provider.json排除清单跳过已排除型号；SiliconFlow确认下线即删除并登记排除。对指定API短名核对同系列最新日期版本。

完成校验和必要测试，运行catalog.py review生成完整候选报告，给出本次修改、未知清单与候选SHA-256。待审核结果不得自动发布；已有明确授权且内容未变时不重复索取。
