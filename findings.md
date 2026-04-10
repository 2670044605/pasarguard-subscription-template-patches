# findings

## 初始结论
- `subscription-template` 是 PasarGuard 官方支持的订阅页模板层，不是核心源码改造。
- 当前生产已临时启用官方 `zh.html` 静态产物。
- 本次目标是沉淀为独立长期维护仓库，并切换默认英文版上线。

## 维护策略
- 上游仓库当前 `license=NONE`，因此不直接公开镜像上游源码副本。
- 采用“补丁仓库”模式：仓库仅保存上游 pinned commit、补丁脚本、构建脚本、部署脚本、文档与 changelog。
- 生产产物在本地/CI 按 pinned upstream 构建后部署，不把上游源码整仓再发布到补丁仓库中。
