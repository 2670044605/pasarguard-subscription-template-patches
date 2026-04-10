# Deploying the custom PasarGuard subscription template

## Goal
Deploy a custom-built English-first subscription page artifact while keeping PasarGuard core behavior unchanged.

## Baseline
- Upstream repo: `PasarGuard/subscription-template`
- Upstream source ref: `1fe452c96308fbd434f6a30ee24c989c0e90716f`
- Pinned release asset: `v1.3.6 / en.html`
- Production host: `digitalocean-sg`
- Production artifact path: `/var/lib/pasarguard/templates/subscription/index.html`

## Requirements
- `python3`, `curl`, `scp`, `ssh` available on the build host
- SSH access to target host
- Docker Compose v2 available on target host

## Correct deployment order
1. Build English artifact with `sh scripts/build-en-html.sh`
2. The script downloads upstream `en.html`
3. The local static patch hides the footer support/credit block
4. Copy artifact to target host
5. Ensure PasarGuard `.env` points to custom template directory and `subscription/index.html`
6. Restart only `pasarguard` service with `docker compose up -d pasarguard`
7. Verify dashboard returns `200`
8. Verify subscription short link opens the English page

## Rollback
1. Restore `/opt/pasarguard/.env.bak-subscription-template-patches-*`
2. Replace `/var/lib/pasarguard/templates/subscription/index.html` with previous version if needed
3. Run `cd /opt/pasarguard && docker compose up -d pasarguard`

## Validation
- `curl -I https://pasarguard.jerrylabs.dev/dashboard/` returns `200`
- `https://sub.jerrylabs.dev/<username>` opens subscription page successfully
- English is the default rendered language on a clean browser state
- Footer support/credit block is not visible
