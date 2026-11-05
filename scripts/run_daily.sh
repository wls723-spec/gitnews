#!/usr/bin/env bash
# run_daily.sh - GitNews 데일리 오픈소스 & AI 트렌드 자동 발행 스크립트
# - 무한 행 방지 및 실행 타임아웃
# - 실패 시 재시도 (최대 3회 백오프)
# - 수차례 실패 시 agy를 호출하여 로그 분석 및 자율 문제해결 유도
set -eo pipefail

export LANG=ko_KR.UTF-8
export LC_ALL=ko_KR.UTF-8
export PATH="/home/jini/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

WORKSPACE="/home/jini/workspace/gitnews"
LOG_FILE="$WORKSPACE/cron.log"
TODAY=$(date '+%Y-%m-%d')
TARGET_HTML="$WORKSPACE/news/${TODAY}.html"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

echo "============================================================" >> "$LOG_FILE"
log "Starting GitNews Daily Generation for ${TODAY}..."
echo "============================================================" >> "$LOG_FILE"

cd "$WORKSPACE"

MAX_RETRIES=3
SUCCESS=false

for attempt in $(seq 1 $MAX_RETRIES); do
  log "[Attempt $attempt/$MAX_RETRIES] Running daily generation pipeline via agy..."
  
  # Run agy with a 20-minute safety timeout to prevent permanent hanging
  if timeout 1200 /home/jini/.local/bin/agy --dangerously-skip-permissions -p "$WORKSPACE 오늘거(${TODAY}) 지침서대로 완성해서 배포까지 해줘" >> "$LOG_FILE" 2>&1; then
    # Verify if target file exists and is not empty
    if [ -s "$TARGET_HTML" ]; then
      log "✓ Verification passed: ${TARGET_HTML} exists and is populated."
      SUCCESS=true
      break
    else
      log "✗ Attempt $attempt failed: ${TARGET_HTML} does not exist or is empty."
    fi
  else
    log "✗ Attempt $attempt exited with non-zero status or timed out."
  fi

  if [ $attempt -lt $MAX_RETRIES ]; then
    log "Waiting 30 seconds before retry..."
    sleep 30
  fi
done

# If all normal attempts failed, trigger emergency self-healing call with error logs
if [ "$SUCCESS" = false ]; then
  log "⚠️ All $MAX_RETRIES standard attempts failed! Triggering emergency self-healing agy run..."
  /home/jini/.local/bin/agy --dangerously-skip-permissions -p "긴급: $WORKSPACE 오늘자(${TODAY}) 기사 자동 생성이 3회 연속 실패했습니다. 최근 cron.log 오류를 분석하여 원인을 즉시 해결하고 오늘자 뉴스를 반드시 생성 및 배포해주세요." >> "$LOG_FILE" 2>&1
fi

log "GitNews Daily Generation Script Finished."
