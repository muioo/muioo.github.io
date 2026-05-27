#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"

cd "${ROOT_DIR}"

GIT_REMOTE="${AI_DAILY_GIT_REMOTE:-origin}"
GIT_BRANCH="${AI_DAILY_GIT_BRANCH:-main}"
PYTHON_BIN="${AI_DAILY_PYTHON:-/root/miniconda3/bin/python}"

# 清理 Hugo 构建产物和运行缓存，让服务器可以拉取本地推送的最新笔记。
cleanup_generated_files() {
  git restore -- public resources content/ai-daily data/ai-daily .hugo_build.lock ai-daily.log 2>/dev/null || true
  git clean -fd -- public resources content/ai-daily data/ai-daily .hugo_cache scripts/ai-daily/__pycache__ 2>/dev/null || true
}

# 拉取前确认没有普通源码或笔记的未提交改动。
ensure_clean_source_tree() {
  local dirty_paths

  cleanup_generated_files
  dirty_paths="$(git status --porcelain --untracked-files=all)"

  if [[ -n "${dirty_paths}" ]]; then
    echo "Refuse to pull because the server has uncommitted source or note changes:" >&2
    echo "${dirty_paths}" >&2
    echo "Commit or remove these changes on the server, then rerun this script." >&2
    exit 1
  fi
}

ensure_clean_source_tree
git pull --rebase "${GIT_REMOTE}" "${GIT_BRANCH}"

export AI_DAILY_TIMEZONE="${AI_DAILY_TIMEZONE:-Asia/Shanghai}"

"${PYTHON_BIN}" scripts/ai-daily/fetch.py

git add content/ai-daily data/ai-daily

if git diff --cached --quiet; then
  echo "No AI Daily changes."
  exit 0
fi

git config user.name "${AI_DAILY_GIT_NAME:-ai-daily-bot}"
git config user.email "${AI_DAILY_GIT_EMAIL:-ai-daily-bot@example.com}"

git commit -m "chore: update ai daily"
git push "${GIT_REMOTE}" "${GIT_BRANCH}" || {
  git pull --rebase "${GIT_REMOTE}" "${GIT_BRANCH}"
  git push "${GIT_REMOTE}" "${GIT_BRANCH}"
}
