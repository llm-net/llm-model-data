# 人工确认

Agent 完成采集、编辑、比较和检查，人集中确认一份具体结果。

“提交推送”只更新Git分支；“发布数据版本”是在明确授权后推送`data-YYYY.MM.DD.N`正式tag。只有这类tag参与最新发布判定，完整规则见[RELEASE.md](RELEASE.md)。无需额外搭发布服务；当前工具不自动打tag。

## A. 本地对话（现在可用）

1. 保存更新前 commit，完成编辑和检查。
2. `python scripts/catalog.py review --base <更新前commit>` 生成摘要、完整 diff 和哈希清单。人工看到价格前后值、单位、基准选择、模型增删、协议面增删与独立核对状态、套餐 / 额度、思考能力的参数 / 档位 / 预算 / 默认值前后变化、全部协议及思考能力 partial / unknown 项、来源、生效时间，以及数量口径 / 取整、收费事件、模型状态和估算基准变化。
3. Agent 提供报告和完整 candidate SHA-256，明确确认动作是保存候选、提交还是正式发布。
4. 人回复例如：`确认候选 <完整SHA256>，允许提交；不发布`。真实对话是授权来源，不由 agent 自造 approved.json。
5. 动作前运行 `python scripts/catalog.py check-candidate <完整SHA256>`。内容或审阅基线变化则重出报告；已有明确授权且没变化则不重复询问。

本地哈希只绑定内容，不认证人的身份。当前工具没有 approve / 发布命令，不能传一个 --approved 就绕过人。数据确认不自动授权消费者部署。

## B. 受保护 PR（配置后作为常用方式）

- Agent 准备分支、PR 和摘要；有远端写入授权才提交。
- 管理员设置 main 必须经 PR、至少 1 位真人批准、CI validate 通过、新提交撤销旧批准、最新推送由他人批准，限制绕过 / 直接推送。
- Agent 仅有工作分支权限，无批准、合并或发布权限。发布从已审核的精确 commit 构建；workflow / 工具改动也要审核。
- 如需独立发布确认，用受保护 GitHub Environment。CODEOWNERS 填实际维护者，不能编造账号。
- **当前只提供 PR 模板和校验 CI，尚未配置远端分支保护、审核人或发布 Environment。** Markdown 规范不等于强制门禁。

[GitHub 分支保护官方说明](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。

## 候选与确认失效

哈希覆盖 providers、schemas、evidence、docs、scripts、tests、templates、AGENTS.md、README.md、依赖、CI 和 .gitignore 的路径及字节哈希；排除虚拟环境、.git 和生成目录。新增、删除、证据和规则改动均失效。

报告还绑定 base commit 和 diff SHA-256，防止审阅包陈旧；生成目录不纳入自己。脚本只证明未变，不证明人批准。

初期每批真实数据变更都人工确认；以后可另行批准有来源范围、阈值和异常条件的自动发布策略，当前没有这份授权。无人值守 agent 留“待审核”结果后结束，不把超时当同意。
