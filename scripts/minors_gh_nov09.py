# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-11-09

GH_MINORS = """
      <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
      <!-- [GH 0~10h] Item 1: trafficinc/tokenshield -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 1개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 0.7시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI 코딩 세션의 토큰 낭비를 80% 줄이는 저장소 압축 맵 CLI&quot; : tokenshield</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">trafficinc/tokenshield — 로컬 Git 리포지토리의 핵심 심볼과 트리 구조만을 컴팩트하게 추출하여 LLM 프롬프트에 주입하는 경량 Go CLI</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">전체 코드베이스를 무지성으로 프롬프트에 밀어 넣는 토큰 낭비를 원천 차단</h3>
          <div class="minor-detail-subheadline">AST 심볼 맵과 시맨틱 파일 계층 구조를 1/10 크기로 압축하여 세션 비용 절감</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 코딩 에이전트가 리포지토리를 이해하기 위해 수만 줄의 파일을 그대로 읽어 들이면서 1회 질의당 수천 원의 토큰 비용이 증발하는 현상을 해결하기 위해 등장했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Git Worktree &rarr; Go Tree-Sitter AST Parse &rarr; TokenShield Compressed Map &rarr; LLM Agent Context
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Go 언어로 작성되어 0.05초 만에 프로젝트 전체의 함수 시그니처, 인터페이스, 모듈 참조 관계를 미니멀한 마크다운 맵으로 요약하여 컨텍스트 윈도우 한계를 대폭 늘려줍니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/trafficinc/tokenshield" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: xdisform/Spider -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 12개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.5시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.3 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;Claude Code를 자율 레드팀 침투 테스터로 전환하는 멀티 에이전트 하네스&quot; : Spider</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">xdisform/Spider — 취약점 자동 정찰, 모의 침투 익스플로잇 체이닝, 패치 검증을 자율 수행하는 사이버 보안 에이전트 시스템</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">수동 모의해킹의 병목을 없애고 24시간 가동되는 보안 감사 편대 구축</h3>
          <div class="minor-detail-subheadline">정찰 에이전트와 공격 체인 분석 에이전트의 분업을 통한 제로데이 보안 취약점 사전 차단</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                지능화된 웹 공격과 복잡해진 마이크로서비스 환경에서 인간 보안 엔지니어의 정기 점검만으로는 매일 배포되는 코드의 취약점을 제때 적발하기 어려운 한계를 타개했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Target Surface Discovery &rarr; Spider Recon Swarm &rarr; Autonomous Exploit Verifier &rarr; Fix Suggestion Report
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Claude Code의 도구 실행 능력을 정밀 보안 프레임워크로 감싸 오탐(False Positive)을 90% 이상 걸러내고 실제 재현 가능한 공격 PoC 코드와 권고 패치를 동시에 작성해 줍니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/xdisform/Spider" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: mitschud/Relay -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 4개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.0시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;로컬 AI 코딩 에이전트를 위한 초경량 Rust 네이티브 데스크톱 하네스&quot; : Relay</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">mitschud/Relay — 시스템 리소스를 15MB 이하로 최소화하고 로컬 LLM 에이전트 워크스페이스를 실시간 제어하는 Rust GUI</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">무거운 Electron 에디터 대신 가볍게 백그라운드에서 돌아가는 전용 하네스</h3>
          <div class="minor-detail-subheadline">시스템 트레이에 상주하며 로컬 Ollama 모델 및 코딩 에이전트의 파일 I/O를 실시간 중계</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                로컬 모델을 돌리기에도 벅찬 데스크톱 환경에서 수백 메가바이트를 점유하는 무거운 AI IDE GUI에 피로감을 느낀 개발자들을 위해 제작되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> System Tray &rarr; Native Rust GUI (egui) &rarr; Local LLM IPC Relay &rarr; Sandboxed Workspace
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Rust로 작성되어 메모리 누수 없이 0.1초 만에 켜지며, 에이전트의 변경 사항을 즉시 깃 디프(Diff)로 렌더링하여 안전한 머지를 지원합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/mitschud/Relay" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
      <!-- [GH 10~20h] Item 4: wanshuiyin/SuperARIS -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 33개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.6시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.9 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;개발자가 잠든 밤새 자율적으로 논문과 코드를 탐색하는 리서치 에이전트&quot; : SuperARIS</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">wanshuiyin/SuperARIS — Auto Research In Sleep (ARIS) 아키텍처로 방대한 기술 문헌을 밤새 수집·비교·합성하는 파이썬 에이전트</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">밤에 잠들기 전 키워드 한 줄만 던져두면 아침에 완성된 심층 연구 리포트 수령</h3>
          <div class="minor-detail-subheadline">ArXiv 논문, 깃허브 코드, 해커뉴스 토론을 교차 검증하여 지식 그래프로 축적</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                매일 수백 편씩 쏟아지는 AI 논문과 오픈소스 릴리즈를 일일이 모니터링하기 불가능한 연구자들을 위해, 수면 시간 동안 에이전트가 백그라운드 탐색을 완료하도록 고안되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> User Research Seed &rarr; Night-Loop Crawler &rarr; Cross-Ref Synthesis &rarr; Morning Intelligence Report
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                DeepSeek-V2.5와 Claude API를 효율적으로 결합하여 저비용으로 고품질 학술 리뷰를 작성하고 코드 실행 검증까지 자율적으로 마칩니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/wanshuiyin/SuperARIS" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: DarkBytee/DuckAi -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 12개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;API 키 없이 6대 상용 LLM을 스트리밍하는 덕덕고 무료 터미널 CLI&quot; : DuckAi</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">DarkBytee/DuckAi — DuckDuckGo AI Chat 엔드포인트를 역공학하여 Claude 3 Haiku, GPT-4o mini 등을 무과금 터미널 챗으로 실행</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">회원가입도 유료 결제도 필요 없는 가장 직관적인 제로 비용 LLM 터미널 클라이언트</h3>
          <div class="minor-detail-subheadline">덕덕고의 프라이버시 퍼스트 AI 인프라를 활용한 실시간 마크다운 스트리밍 파이프라인</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                간단한 코드 스니펫 확인이나 번역을 위해 매번 브라우저를 열거나 유료 API 키를 발급받아야 하는 번거로움을 덜기 위해 탄생했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Terminal Input &rarr; DuckDuckGo Ephemeral Session &rarr; Multi-Model Streaming &rarr; Rich TUI Markdown
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                VFS 세션 암호화와 익명 프록시를 통해 사용자의 프롬프트가 빅테크의 모델 학습 데이터로 재사용되지 않는 강력한 프라이버시를 보장합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/DarkBytee/DuckAi" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: tailucanh/offload-mcp-server -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 13개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;메인 코딩 에이전트의 문서 독해를 보조 에이전트에 위임하는 MCP 오프로더&quot; : offload-mcp-server</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">tailucanh/offload-mcp-server — 컨텍스트 윈도우 오염을 막기 위해 대형 파일 분석 작업을 서브 에이전트로 분기하고 핵심만 회신받는 MCP 서버</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">메인 모델의 고비용 토큰 윈도우를 순수 코딩 작업에만 온전히 집중시키는 지능적 오프로딩</h3>
          <div class="minor-detail-subheadline">수천 줄의 설정 파일이나 로그 분석을 저렴한 보조 LLM으로 격리 처리</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Claude 3.5 Sonnet 같은 비싼 프론티어 모델이 수십 메가바이트짜리 로그 파일이나 장문 문서를 읽다가 컨텍스트가 가득 차 조기 종료되는 문제를 방지합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Main Coding Agent &rarr; Offload MCP &rarr; Sub-Agent (Flash/Local) Deep Read &rarr; Condensed 3-Line Summary
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Model Context Protocol(MCP) 표준을 채택하여 Cursor, Claude Code, Cline 등 모든 에이전트 도구에 무설정 플러그인으로 즉시 연동됩니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/tailucanh/offload-mcp-server" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
      <!-- [GH 20~30h] Item 7: ensignalp/kota -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 53개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;리눅스 데스크톱 상단 패널에서 실시간 AI 사용량과 쿼터를 감시하는 도구&quot; : kota</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ensignalp/kota — Claude, Codex, Gemini, Copilot의 API 호출 한도와 잔여 토큰을 GNOME 상단 바에 실시간 표기하는 Rust 위젯</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">코딩 도중 갑자기 발생하는 Rate Limit 폭탄을 사전에 방지하는 데스크톱 게이지</h3>
          <div class="minor-detail-subheadline">다중 공급자의 잔여 토큰 쿼터와 리셋 잔여 시간을 1초 간격으로 폴링 모니터링</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                개발자가 열정적으로 코딩 에이전트를 돌리다가 갑자기 일일 한도 초과(429 Too Many Requests)로 작업이 중단되는 불편을 미연에 방지합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Provider API Endpoints &rarr; Rust Async Quota Scraper &rarr; GNOME Shell D-Bus &rarr; Top-Panel Gauge
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                안전한 키링(Keyring) 저장소를 사용해 API 토큰을 암호화 보관하며, 한도 80% 도달 시 사전에 데스크톱 네이티브 알림을 전송합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/ensignalp/kota" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: flockcap/cantrip -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 19개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.8시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;평상어를 즉시 안전한 쉘 명령어로 변환하는 키리스 터미널 비서&quot; : cantrip</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">flockcap/cantrip — API 키 등록 없이도 로컬 및 무료 엔드포인트를 통해 복잡한 터미널 파이프라인 명령어를 원터치 생성하는 Rust CLI</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">기억나지 않는 tar, ffmpeg, awk 정규식 옵션을 말하듯 타이핑하면 즉시 해결</h3>
          <div class="minor-detail-subheadline">명령어 실행 전 파괴적 변경(rm -rf, dd 등) 위험을 자체 분석해 경고하는 안전 가드레일</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                복잡한 리눅스 명령어를 검색하느라 브라우저를 뒤지는 수고를 덜고, 터미널 안에서 자연어로 직관적인 파이프라인을 구축하고자 하는 요구를 충족합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Plain English Query &rarr; Lightweight Model Synthesis &rarr; Safety Rule Engine &rarr; Copy-to-Clipboard
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                순수 Rust 바이너리로 단 5MB 미만의 크기를 자랑하며, 단축키 하나로 현재 쉘 히스토리를 오염시키지 않고 명령어를 생성·검증합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/flockcap/cantrip" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: avivgerz-hue/vibe-shield -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 18개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI 생성 코드의 악성 스킬 주입과 취약점을 60가지 규칙으로 차단하는 정적 감사기&quot; : vibe-shield</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">avivgerz-hue/vibe-shield — 코딩 에이전트가 무심코 받아들이는 환각 패키지, 프롬프트 주입 공격을 실시간 차단하는 MCP 보안 서버</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">바이브 코딩(Vibe Coding) 시대의 가장 큰 구멍인 공급망 오염과 슬롭 코드 박멸</h3>
          <div class="minor-detail-subheadline">AST 정적 분석과 알려진 악성 의존성 시그니처 60종을 통한 컴파일 이전 선제 감사</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 코딩 도구가 제안한 존재하지 않는 가짜 라이브러리(패키지 환각)를 해커가 선점 등록하여 개발 환경을 감염시키는 공급망 공격이 급증함에 따라 개발되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Agent Output Code &rarr; AST & Dependency Scanner &rarr; 60 Rules Vibe Audit &rarr; Safe Clean Diff
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                TypeScript로 구현된 MCP 서버 형태로, 에이전트가 코드를 파일 시스템에 쓰기 직전 가로채어 취약한 패턴을 즉각 경고하고 안전한 대안 코드를 강제합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/avivgerz-hue/vibe-shield" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>
"""
