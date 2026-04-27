# task_plan

## 目标
- 将 PasarGuard `subscription-template` 整理为可长期维护的独立补丁仓库。
- 默认产出并上线英文版订阅页模板到生产 `digitalocean-sg`。
- 保留文档、变更记录、构建与部署说明，便于后续持续维护。

## 阶段
- [complete] 1. 盘点现状：检查上游模板结构、当前生产状态、GitHub 推送条件
- [complete] 2. 建立本地长期维护仓库骨架与文档
- [complete] 3. 生成英文版模板产物并准备部署脚本
- [complete] 4. 初始化 Git、提交变更并尝试推送 GitHub
- [complete] 5. 上线到生产并完成验收
- [complete] 6. 更新项目记录与记忆

## 约束
- 优先最小风险；不直接改 PasarGuard 核心。
- 生产只替换订阅模板文件与对应 `.env` 选择。
- 需要 fresh verification 后再声称完成。
