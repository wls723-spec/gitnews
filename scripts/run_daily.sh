#!/usr/bin/env bash
# run_daily.sh - GitNews 데일리 오픈소스 & AI 트렌드 자동 발행 스크립트
set -eo pipefail

export LANG=ko_KR.UTF-8
export LC_ALL=ko_KR.UTF-8
export PATH="/home/jini/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

WORKSPACE="/home/jini/workspace/gitnews"
LOG_FILE="$WORKSPACE/cron.log"

echo "============================================================" >> "$LOG_FILE"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting GitNews Daily Generation..." >> "$LOG_FILE"
echo "============================================================" >> "$LOG_FILE"

cd "$WORKSPACE"

# Run agy non-interactively with auto-approved permissions
/home/jini/.local/bin/agy --dangerously-skip-permissions -p "$WORKSPACE 오늘거 만들어줘" >> "$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] GitNews Daily Generation Finished!" >> "$LOG_FILE"
