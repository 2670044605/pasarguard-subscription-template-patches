# progress

## 2026-04-10
- 初始化订阅模板长期维护项目规划。
- 确认本地具备 `git` / `gh` / `node` / `npm`，且 GitHub 已登录可推送。
- 确认上游 `subscription-template` 具备源码构建路径，适合做成“补丁覆盖 + 构建脚本”型仓库。
- 已生成正式补丁文件 `patches/0001-english-default-and-minimal-debranding.patch`。
- 已补齐 README / CHANGELOG / patch note / build script / deploy script / deployment doc。
- 构建阶段曾因用户中途取消导致依赖未装全，当前改为显式安装 devDependencies 并绕过 `.bin`，直接调用 `typescript` / `vite` 包入口继续验证。
- 从断点恢复后，优先走现成脚本的快速构建验证路径。
- 发现 Alpine aarch64/musl 下 `rollup` optional native dependency 缺失；已把 `@rollup/rollup-linux-arm64-musl` 安装补丁直接写进构建脚本，作为快速稳定兜底。
- 二次修正：补装 Rollup 原生包时同样加上 `--legacy-peer-deps`，避免触发上游 React/qrcode peer dependency 冲突。
- 最终切换到更快更稳的方案：使用上游 pinned release asset `v1.3.6/en.html`，再做本地静态补丁后部署，避免 iSH 环境下的前端全量构建不稳定。
- 已将补丁仓库推送到 GitHub，并将英文版订阅模板部署到生产。

## 2026-05-08
- 生产模板已针对上游 `v2.2.0` 的底部支持入口做二次修正：在保留 CSS 隐藏兜底的同时，直接移除已知 v2.x bundle 中的 footer/support 组件，避免 `support-url` 响应头在页面底部渲染“支持/پشتیبانی”按钮。
- 生产备份：`digitalocean-sg:/root/minis-maint/pasarguard-sub-footer-remove-20260507T232533Z/index.html.before`；验证公开 HTML 页面已含 `const EU=()=>null` 且正文不再显示支持入口。
