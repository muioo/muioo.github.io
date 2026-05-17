#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"

cd "${ROOT_DIR}"

git pull --rebase origin main

export AI_DAILY_TIMEZONE="${AI_DAILY_TIMEZONE:-Asia/Shanghai}"

python scripts/ai-daily/fetch.py

git add content/ai-daily data/ai-daily

if git diff --cached --quiet; then
  echo "No AI Daily changes."
  exit 0
fi

git config user.name "${AI_DAILY_GIT_NAME:-ai-daily-bot}"
git config user.email "${AI_DAILY_GIT_EMAIL:-ai-daily-bot@example.com}"

git commit -m "chore: update ai daily"
git push origin main
