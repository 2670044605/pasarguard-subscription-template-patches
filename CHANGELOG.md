# Changelog

All notable changes to this patch repository will be documented in this file.

## [0.1.2] - 2026-05-08
### Changed
- Updated the pinned upstream release asset to `v2.2.0/en.html`.
- Removed the known v2.x rendered footer/support component in addition to the CSS footer-hide guard, so `support-url` response headers no longer produce a visible support link/button.
- Preserved the local Chinese apps heading normalization (`应用领域` → `客户端应用`).

## [0.1.1] - 2026-04-10
### Changed
- Switched the reproducible build workflow to a pinned upstream release asset (`v1.3.6/en.html`) plus a local static patch.
- Avoided fragile local full frontend builds in constrained iSH/Alpine environments.

## [0.1.0] - 2026-04-10
### Added
- Initial patch repository for PasarGuard subscription template customization.
- Patch `0001-english-default-and-minimal-debranding.patch`.
- Reproducible build helper for English single-file HTML artifact.
- Production deployment helper and deployment documentation.

### Changed
- Default production artifact switched to English.
- Footer support/credit block hidden.
