# ============================================================
# Local daily scheduler: generate AI daily + GitHub trending and push.
# Only stages/commits generated outputs (.ai-daily, github-trending, data).
# Hand-written notes under content/post are NEVER touched.
# Invoked by Windows Task Scheduler on a daily schedule.
# Keep this file ASCII-only to avoid PS 5.1 encoding issues.
# ============================================================
$ErrorActionPreference = "Stop"

# Repo root is parent of scripts/
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Output ("[{0}] start daily generate" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))

# 1) Generate content (throw on failure so Task Scheduler logs the error)
python scripts/ai-daily/fetch.py
python scripts/github-trending/fetch.py

# 2) Stage only generated outputs (including deletions)
git add -A -- content/ai-daily data/ai-daily content/github-trending data/github-trending

# 3) Exit early if nothing changed
if (git diff --cached --quiet) {
    Write-Output ("[{0}] no daily changes, exit" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))
    exit 0
}

# 4) Commit and push; rebase first to avoid non-fast-forward rejection
git config user.name "local-daily-bot"
git config user.email "local-daily-bot@example.com"
git commit -m "chore: update ai daily and github trending"
git pull --rebase origin main
git push origin main

Write-Output ("[{0}] daily generate done" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))