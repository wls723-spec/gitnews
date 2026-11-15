# -*- coding: utf-8 -*-
# Story 5: andrewyng/openworker

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] andrewyng/openworker                             -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openworker.jpg" alt="OpenWorker Local AI Coworker Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="lock" style="width:12px;height:12px;fill:#fff;"></i> LOCAL COWORKER</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#14532d;">🛡️ 4단계 거버넌스 · 로컬 AI 동료</span>
              <span class="platform-tag">GitHub Trending &amp; openworker.com</span>
              <span class="platform-tag">andrewyng / openworker</span>
            </div>
            
            <h2 class="article-headline">
              앤드류 응의 오픈소스 AI 동료 'OpenWorker': "클라우드 종속과 프롬프트 인젝션을 끝내는 4단계 하드 플로어 거버넌스 + Rust 하네스 SDK"
            </h2>

            <div class="article-subheadline">
              Ollama 로컬 모델·25개 이상 커넥터·NVIDIA OpenShell 샌드박스를 결합해 내 PC 안에서 문서·보안·Slack 업무를 대행하고 모든 툴 호출 감사 로그를 남기는 로컬 퍼스트 데스크톱 앱
            </div>
            <p class="article-snippet">
              빅테크들이 앞다퉈 내놓는 클라우드 'AI 코워크' 서비스의 가장 큰 약점은 내 컴퓨터의 파일, Slack, 이메일, API 키를 외부 클라우드 에이전트 서버에 통째로 맡겨야 한다는 불안감입니다. AI 석학 앤드류 응(Andrew Ng) 진영이 MIT 라이선스로 내놓은 `OpenWorker`는 에이전트 루프와 대화·토큰 시크릿 스토어를 100% 사용자 머신에 가두고, NVIDIA OpenShell·macOS 네이티브 샌드박스와 4단계 승인 사다리(Hard Floors)를 결합해 누적 19,342 스타를 기록하며 빠르게 확산되고 있습니다.
            </p>
            <div class="article-action">
              <span>메모 펼치기</span>
              <i data-lucide="chevron-down" class="chevron-icon"></i>
            </div>
          </div>
        </div>

        <div class="article-detail" onclick="event.stopPropagation()">
          <div class="editorial-content">
            
            <h3 class="editorial-section-title">
              <i data-lucide="flame"></i> 1. 리드: "내 로컬 폴더와 API 키를 왜 남의 클라우드에 올려야 하나?"
            </h3>
            <p>
              2026년 들어 AI는 코딩 터미널을 넘어 일반 지식 노동자의 데스크톱으로 진입했다. 회의록 폴더를 요약해 보고서를 쓰고, 보안 취약점을 스캔하며, Slack에서 `@멘션`을 받으면 관련 자료를 찾아 답장하는 'AI 동료(Coworker)' 경쟁이 치열하다. 그러나 기업 보안팀과 프라이버시에 민감한 개발자들은 곧장 제동을 걸었다. 클라우드 기반 AI 동료 앱들은 편리함의 대가로 로컬 파일과 OAuth 토큰, 모델 키를 공급자의 클라우드 세션에 동기화하라고 요구했기 때문이다.
            </p>
            <p>
              오늘 Python 트렌딩 상위권을 지키며 누적 <strong>19,342 스타</strong>를 기록한 <strong>andrewyng/openworker</strong>(MIT 라이선스)는 이 딜레마에 정면으로 반기를 든 오픈소스 프로젝트다. 모든 에이전트 실행과 시크릿을 내 맥북·윈도우 PC 안에 두는 **OpenWorker Desktop App**과, 개발자가 자체 에이전트 앱을 조립할 수 있는 **OpenWorker Harness SDK**를 동시에 내놓았다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 플러그인이 아니라 '아키텍처'로 못 박은 4단계 거버넌스
            </h3>
            <p>
              OpenWorker가 단순한 로컬 챗봇 래퍼와 결정적으로 다른 점은 에이전트의 자율성과 안전성을 조율하는 **Governed by design** 철학이다. 많은 오픈소스 에이전트가 프롬프트에 "위험한 명령은 묻고 실행해"라고 적어두는 수준에 그치지만, OpenWorker는 시스템 레벨에서 에이전트가 스스로 권한을 승격시킬 수 없도록 4개의 물리적 방어층을 깔았다.
            </p>

            <div class="editorial-quote">
              <p>
                "거버넌스는 플러그인이 아니라 아키텍처다. <strong>에이전트는 스스로 새 권한을 부여할 수 없으며, 어떤 프롬프트 인젝션도 승인 게이트를 말로 설득해 통과할 수 없다.</strong> 전체 자동 승인(Auto-approve) 모드에서도 절대 낮출 수 없는 '하드 플로어(Hard Floors)'가 항상 인간에게 에스컬레이션된다."
              </p>
              <small>— andrewyng/openworker 'Governed by design' 보안 아키텍처 명세</small>
            </div>

            <p>
              여기에 로컬 우선(Local-First) 원칙이 결합된다. 대화 기록, 커넥터 토큰, 모델 API 키는 모두 앱 내부 로컬 시크릿 스토어에 저장되며, 원할 경우 OpenAI·Anthropic·Gemini 대신 **Ollama·LM Studio·llama.cpp·vLLM** 같은 완전한 오프라인 로컬 모델로만 구동할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Python·Tauri 데스크톱 + Rust Harness 엔진 + OpenShell 격리벽
            </h3>
            <p>
              OpenWorker는 엔드유저용 데스크톱 앱과 서드파티 개발자용 SDK를 명확히 이원화해 설계했다:
            </p>
            <ul>
              <li><strong>이원화된 런타임(Desktop App vs Harness SDK):</strong> 데스크톱 앱은 React UI와 Tauri 네이티브 쉘이 `aisuite` 기반의 로컬 Python 에이전트 서버(`coworker/`)와 25개 이상의 커넥터·MCP 클라이언트를 감독하는 구조다. 반면 제품 개발자를 위한 `@openworkerai/harness-sdk`는 별도의 고성능 **Rust 에이전트 엔진(`harness/`)**을 제공해 에이전트 루프, 툴 호출, 스트리밍, 영속 세션을 TypeScript나 Rust 앱에 바로 임베드할 수 있다.</li>
              <li><strong>점진적 자율성 사다리 &amp; 서킷 브레이커:</strong> 기본값은 모든 쓰기/실행이 인간 승인 대기 상태이며, 일회성 승인이 상시 규칙(Standing rules)과 설정 허용 목록으로 승격된다. 자동 승인 모드에서는 별도 리뷰어 모델이 일상 작업을 통과시키되, 반복적인 거부(Denial)가 감지되면 즉시 **서킷 브레이커(Circuit Breaker)**가 작동해 리뷰어를 멈추고 인간에게 제어권을 돌려준다. 모든 툴 호출에는 승인 출처(자동·사용자·거부 및 사유) 감사 로그가 영구 첨부된다.</li>
              <li><strong>키와 툴을 가르는 샌드박스 방화벽:</strong> 쉘 명령과 파일 도구는 **NVIDIA OpenShell** 리눅스 컨테이너(macOS는 내장 샌드박스, Windows는 프로필 격리 로컬 계정) 안에서 실행된다. 모델 키와 커넥터 인증 정보, 에이전트 루프는 샌드박스 바깥에 머무르기 때문에, 문서에 숨겨진 프롬프트 인젝션이 명령 실행 단계까지 침투하더라도 컨테이너 내부에는 탈취할 키나 타 폴더 파일이 전혀 존재하지 않는다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">OpenWorker 로컬 퍼스트 4단계 거버넌스 &amp; 샌드박스 격리 아키텍처</span>
                <span class="schematic-badge">Local-First · Rust Harness · OpenShell</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">User Surface &amp; Connectors</div>
                  <div class="schematic-desc">
                    Tauri + React 데스크톱 앱 (or Slack `@` 위임)<br>
                    로컬 시크릿 스토어(API 키·토큰 영구 보관)<br>
                    25+ 커넥터 &amp; MCP · 보안 코워커 기본 탑재<br>
                    클라우드 LLM + Ollama/vLLM 로컬 모델 전환
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">4-Tier Governance Core</div>
                  <div class="schematic-desc">
                    1. Hard Floors: 불가역 작업은 무조건 인간 승인<br>
                    2. Earned Autonomy: 일회성→상시 규칙 승격<br>
                    3. Reviewer + 반복 거부 시 Circuit Breaker<br>
                    4. 전 툴 호출 승인 출처·사유 감사 로그 기록
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Sandboxed Execution Wall</div>
                  <div class="schematic-desc">
                    NVIDIA OpenShell · macOS · Win 계정 격리<br>
                    세션 작업 폴더만 마운트 (키·타 파일 차단)<br>
                    허용된 네트워크 호스트 화이트리스트만 통신<br>
                    인젝션 방어 + Rust Harness SDK 임베딩
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">OpenWorker 공식 웹사이트 (openworker.com) — 데스크톱 앱 및 Harness SDK</span>
              </div>
              <img src="../assets/images/demo_openworker.png" alt="OpenWorker Official Portal & Desktop Coworker Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ openworker.com 공식 화면: 회의 준비(Meeting prep), 일정 조율, 인시던트 트리아지, 보안 코드 리뷰 등 일상 업무를 로컬 데스크톱 앱과 오픈소스 Harness SDK로 통합 수행하는 워크플로우를 제시한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 시장 파급력: '로컬 에이전트 하네스' 표준 경쟁의 신호탄
            </h3>
            <p>
              그동안 일반 사용자용 AI 에이전트 시장은 Anthropic의 Claude Cowork나 빅테크의 유료 데스크톱 앱들이 독점하려던 영역이었다. OpenWorker는 앤드류 응의 명성과 MIT 오픈소스 라이선스, 그리고 `aisuite`·NVIDIA OpenShell 생태계를 업고 "왜 에이전트 런타임까지 빅테크에 종속되어야 하는가?"라는 질문을 던진다.
            </p>
            <ul>
              <li><strong>보안 전문가 동료(Security Coworker) 우선 출격:</strong> OpenWorker는 첫 번째 전문 동료로 코드·의존성 취약점 스캔, 클라우드 설정 점검, 인시던트 조사를 수행하는 보안 코워커를 탑재했다. 제안된 수정 코드는 승인 전 자동 재스캔을 거치도록 설계되어 엔터프라이즈 DevSecOps 팀의 즉각적인 수요를 겨냥한다.</li>
              <li><strong>클라우드 OAuth 브로커 외 100% 로컬 주권:</strong> 커넥터 OAuth 핸드셰이크를 중개하는 경량 서비스 외에는 모든 추론과 파일 처리가 로컬에 머물며, 원할 경우 수동 API 키 입력만으로 클라우드 로그인조차 없이 완전 독립 구동할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 믿을 수 없는 AI에게 필요한 것은 더 큰 모델이 아니라 '단단한 안전울타리'다
            </h3>
            <p>
              에이전트가 파일 시스템을 읽고 Slack 메시지를 보내며 터미널 명령을 내리는 순간, 모델의 지능보다 중요한 것은 "실수하거나 공격당했을 때 얼마나 좁은 상자 안에서 멈출 수 있는가"라는 시스템 공학이다.
            </p>
            <p>
              하드 플로어와 서킷 브레이커, 그리고 OpenShell 샌드박스로 무장한 OpenWorker의 등장은 AI 동료 시대의 진짜 승부가 모델 파라미터 경쟁이 아닌 '신뢰할 수 있는 오픈소스 하네스' 위에서 결정될 것임을 예고하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Andrew+Ng+OpenWorker+open+source" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://openworker.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 방문
              </a>
              <a href="https://github.com/andrewyng/openworker" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
