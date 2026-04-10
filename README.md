# pasarguard-subscription-template-patches

A tracked patch repository for long-term maintenance of the PasarGuard subscription page template.

## Purpose
This repository keeps a small, reviewable patch set and reproducible build/deploy workflow for the PasarGuard `subscription-template`, without republishing the upstream source tree.

## Current customization scope
- Default production artifact uses the official English release asset (`en.html`)
- Footer block is hidden via a minimal static patch
- Footer credit `Made with ❤️ by PasarGuard Team` is stripped/hidden

## Upstream baseline
- Upstream repo: `https://github.com/PasarGuard/subscription-template`
- Baseline source commit reference: `1fe452c96308fbd434f6a30ee24c989c0e90716f`
- Pinned release asset: `v1.3.6 / en.html`
- Upstream license status at time of setup: `NONE` (no license detected)

## Repository layout
- `patches/` — source-level reference patch against the pinned upstream baseline
- `docs/` — patch notes and deployment records
- `scripts/` — build and deployment helpers
- `CHANGELOG.md` — human-readable change log

## Build English artifact
```bash
sh scripts/build-en-html.sh
```

Expected output:
- `build/output/index.html`

Build strategy:
- download official upstream release asset `en.html`
- apply a minimal local static patch
- produce deployable `index.html`

## Deploy to production
```bash
TARGET_HOST=digitalocean-sg sh scripts/deploy-on-server.sh
```

This copies `build/output/index.html` to:
- `/var/lib/pasarguard/templates/subscription/index.html`

and ensures:
- `CUSTOM_TEMPLATES_DIRECTORY="/var/lib/pasarguard/templates/"`
- `SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"`

## Maintenance workflow
1. Check upstream changes/releases
2. If needed, re-derive source patch against a new pinned upstream commit
3. Update static patch logic if upstream release HTML shape changes
4. Update docs and changelog
5. Commit
6. Push to GitHub
7. Rebuild English artifact
8. Redeploy and verify

## Notes
- This repository intentionally does **not** republish the full upstream source tree.
- Production uses a patched English release asset, which is significantly faster and more reliable to reproduce in constrained environments like iSH.
