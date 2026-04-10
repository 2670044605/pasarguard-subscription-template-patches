#!/bin/sh
set -eu

TARGET_HOST=${TARGET_HOST:-digitalocean-sg}
BASE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
ARTIFACT="$BASE_DIR/build/output/index.html"
REMOTE_ENV_UPDATER=/tmp/update_pasarguard_env.py

if [ ! -f "$ARTIFACT" ]; then
  echo "Artifact not found: $ARTIFACT" >&2
  echo "Run: sh scripts/build-en-html.sh" >&2
  exit 1
fi

scp -q /var/minis/shared/projects/pasarguard-sg/update_pasarguard_env.py "$TARGET_HOST:$REMOTE_ENV_UPDATER"
scp -q "$ARTIFACT" "$TARGET_HOST:/tmp/pasarguard-subscription-index.html"

ssh -o BatchMode=yes "$TARGET_HOST" '
set -eu
cd /opt/pasarguard
cp .env .env.bak-subscription-template-patches-$(date +%Y%m%d-%H%M%S)
mkdir -p /var/lib/pasarguard/templates/subscription
cp /tmp/pasarguard-subscription-index.html /var/lib/pasarguard/templates/subscription/index.html
python3 /tmp/update_pasarguard_env.py /opt/pasarguard/.env --set CUSTOM_TEMPLATES_DIRECTORY="\"/var/lib/pasarguard/templates/\"" --set SUBSCRIPTION_PAGE_TEMPLATE="\"subscription/index.html\""
docker compose up -d pasarguard
'

echo "Deployed artifact to $TARGET_HOST"
