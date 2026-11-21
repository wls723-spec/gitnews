# -*- coding: utf-8 -*-
# Story 4: rtk-ai/rtk

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] rtk-ai/rtk                                       -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_rtk.jpg" alt="RTK Rust Token Killer CLI Proxy Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> -90% TOKEN TAX</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#d1fae5; border-color:#059669; color:#065f46;">✂️ 에이전트가 읽는 터미널 쓰레기 출력 90%를 25ms 만에 증발</span>
              <span class="platform-tag">GitHub Trending &amp; rtk-ai.app</span>
              <span class="platform-tag">rtk-ai / rtk</span>
            </div>

            <h2 class="article-headline">
              "당신의 AI 에이전트는 로그 소음 속에 익사하고 있다" — CLI 출력을 60~90% 압축해 토큰 과금과 컨텍스트 낭비를 끝낸 'RTK'
            </h2>

            <div class="article-subheadline">
              의존성 0개 단일 Rust 바이너리·명령당 25ms 미만 초저지연 프록시로 100종 이상 개발 명령(git·cargo·pytest·ls) 출력 실시간 정제, 프롬프트 캐시 무손실 Pipelines 및 엔터프라이즈 제어 게이트웨이 RTK Pro 제공 (+129스타/일, 누적 87,414스타)
            </div>
            <p class="article-snippet">
              AI 코딩 에이전트가 프로젝트의 테스트 스위트(<code>cargo test</code>·<code>pytest</code>)를 한 번 돌릴 때마다 수천 줄의 성공 로그와 ANSI 색상 코드가 컨텍스트 창을 가득 메우고, 사용자는 그 '읽을 필요 없는 잡음'을 LLM에 먹이기 위해 고스란히 API 비용과 쿼터를 태우고 있습니다. 누적 <strong>87,414스타</strong>를 기록하며 다시금 트렌딩 상단을 지킨 <strong>rtk-ai/rtk(Rust Token Killer)</strong>는 <code>rtk init -g</code> 한 줄로 에이전트 훅 뒤에 숨어, 에이전트가 실행하는 100여 종의 개발 명령 출력을 25ms 만에 핵심 3줄로 압축해 전달합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 281개 테스트 중 3개가 실패했는데, 에이전트는 왜 3,400토큰을 삼켰는가
            </h3>
            <p>
              터미널에서 코딩 에이전트에게 "테스트 돌리고 실패한 원인 고쳐줘"라고 지시할 때 벌어지는 낭비는 상상을 초월한다. 281개 테스트 중 통과한 278개의 <code>ok</code> 로그와 컴파일러 워닝, 장황한 <code>git status</code>·<code>ls</code> 출력이 수천 토큰 분량의 텍스트 덩어리로 LLM 입력창에 쏟아진다. 컨텍스트 창은 금세 오염되어 모델의 추론 정확도는 떨어지고(Lost in the Middle), 토큰 과금 게이지는 맹렬히 돌아간다.
            </p>
            <p>
              누적 <strong>87,414스타(오늘 +129스타)</strong>라는 경이로운 지지를 얻은 Rust 프로젝트 <strong>rtk-ai/rtk</strong>의 시연 데모는 이 문제를 한눈에 증명한다. <code>rtk init -g</code>로 글로벌 훅을 등록한 뒤 에이전트에게 테스트를 시키면, RTK가 <code>cargo test</code> 출력을 <strong>94.2%</strong>, <code>ls</code> 출력을 <strong>82.3%</strong> 압축해 두 명령어 합산 <strong>3.4K 토큰(93.3%)</strong>을 절약해 준다. 그러면서도 에이전트는 "281개 중 3개 테스트가 실패했으며 각각의 실패 어설션(Assertion)은 무엇"인지 한 치의 정보 손실 없이 정확히 짚어낸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "설치하고 잊어버려라 — 에이전트와 배시 사이의 투명한 다이어트 필터"
            </h3>
            <p>
              기존의 토큰 절약 기법들이 모델 프롬프트를 고치거나 별도의 요약 LLM을 한 번 더 호출해 지연시간을 늘리는 방식이었다면, RTK는 <strong>결정론적 Rust CLI 프록시</strong>라는 완전히 다른 접근법을 택했다. 의존성 없는 단일 Rust 바이너리로 작동하며 명령어당 오버헤드가 <strong>25ms 미만</strong>이라 사람이 체감할 수 없는 속도로 실행된다.
            </p>

            <div class="editorial-quote">
              <p>
                "에이전트가 <code>git status</code>를 실행하면 RTK가 가로채 <code>rtk git status</code>를 돌리고, 에이전트에게는 40줄짜리 로그 대신 <strong>3줄짜리 핵심 요약</strong>만 보여준다. 배울 것도, 호출 방식을 바꿀 것도 없다."
              </p>
              <small>— rtk-ai/rtk "Install &amp; Forget" 아키텍처 원칙 (Apache-2.0)</small>
            </div>

            <p>
              게다가 최신 v1.2.1 세대의 RTK는 단순한 배시 출력 압축기를 넘어 <strong>에이전트 무관(Agent-agnostic) Pipelines</strong>로 진화했다. 무거운 파일 읽기는 저렴한 보조 모델로 넘기고, 프롬프트 캐시(Prompt Cache)를 깨뜨리지 않는 범위 내에서 API 트래픽 자체를 정제해, 커뮤니티 벤치마크 기준 전체 에이전트 작업 비용을 추가로 20.2% 더 절감하는 파이프라인 생태계까지 열어젖혔다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 25ms 결정론적 파서 · 캐시 보존 Pipelines · <code>rtk gain</code> 텔레메트리
            </h3>
            <p>
              RTK가 에이전트의 추론 능력을 훼손하지 않으면서도 출력을 최대 90%까지 압축하는 3단계 메커니즘은 다음과 같다:
            </p>
            <ul>
              <li><strong>무설정 글로벌 훅 &amp; 100+ 명령어 전용 압축기:</strong> <code>rtk init -g</code>가 Claude Code 등 에이전트 훅을 자동 등록하면 <code>git</code>, <code>cargo</code>, <code>pytest</code>, <code>npm</code>, <code>docker</code>, <code>ls</code> 등 100여 종 명령의 구조를 이해하는 Rust 전용 파서가 ANSI 코드·중복 스택트레이스·성공 로그를 걷어내고 실패/변경 지점만 남긴다.</li>
              <li><strong>프롬프트 캐시 무결성 보장 Pipelines:</strong> LLM API의 비용 효율 핵심인 프리픽스 캐시(Prompt Cache)를 무효화하지 않으면서도 배시 밖의 대용량 파일 읽기나 API 페이로드를 저렴한 모델/필터로 라우팅하는 선언형 파이프라인을 지원한다.</li>
              <li><strong>실시간 절감 대시보드 (<code>rtk gain</code>) &amp; 엔터프라이즈 게이트웨이:</strong> 로컬에서 얼마나 많은 토큰을 아꼈는지 명령어별 절감률로 즉시 추적하며, 조직 전체의 에이전트 호출 비용·시크릿·개인정보(PII) 마스킹·감사 로그를 통제하는 <code>RTK Pro</code> 게이트웨이로 확장된다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">RTK (Rust Token Killer) 25ms CLI 프록시 &amp; 캐시 보존 파이프라인 구조</span>
                <span class="schematic-badge">Apache-2.0 Core + BUSL-1.1 Pro · Single Rust Binary · &lt;25ms Overhead</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Transparent Hook Intercept</div>
                  <div class="schematic-desc">
                    <code>rtk init -g</code> 에이전트 훅 자동 등록<br>
                    에이전트 명령 투명 가로채기 (설정 0)<br>
                    100+ 개발 CLI(git·cargo·test·ls) 지원<br>
                    의존성 0 단일 Rust 바이너리 실행
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. &lt;25ms Semantic Compression</div>
                  <div class="schematic-desc">
                    ANSI·중복 로그·성공 스팸 60~90% 제거<br>
                    실패 어설션·핵심 Diff만 3줄 정제<br>
                    <code>rtk gain</code> 실시간 토큰 절감률 계측<br>
                    (예: <code>cargo test</code> 94.2% 절감)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Pipelines &amp; RTK Pro</div>
                  <div class="schematic-desc">
                    무거운 파일 읽기 저비용 모델 오프로드<br>
                    LLM 프롬프트 캐시 무손실 트래픽 정제<br>
                    사내 단일 게이트웨이(비용·PII·감사)<br>
                    팀 단위 파이프라인 공유 카탈로그
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">rtk-ai.app 공식 웹사이트 실화면 — "Your AI agent drowns in noise. RTK cleans it up."</span>
              </div>
              <img src="../assets/images/demo_rtk.png" alt="RTK Official Website Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ www.rtk-ai.app 공식 사이트 실화면: 87.4K 스타를 기록한 Rust Token Killer의 핵심 철학("Raw Context vs Clean Context")과 오픈소스 Pipelines, 엔터프라이즈 게이트웨이 RTK Pro 아키텍처를 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 토큰 인플레이션 시대의 필수 '엔진룸 배플'과 오픈코어 전략
            </h3>
            <p>
              에이전트 코딩이 보편화되면서 기업과 개인 개발자 모두 API 토큰 비용과 모델 레이트 리밋(Rate Limit)을 가장 큰 운영 병목으로 마주하고 있다. 흥미롭게도 모델 공급사들은 토큰 소비가 늘수록 매출이 오르는 구조이기에 '컨텍스트 다이어트'에 소극적인 반면, RTK는 철저히 사용자와 기업의 편에서 불필요한 토큰 세금을 깎아주는 포지션을 점유했다.
            </p>
            <ul>
              <li><strong>Apache-2.0 코어 + BUSL-1.1 거버넌스 이중 구조:</strong> 개발자 개인이 쓰는 CLI 압축기 코어는 Apache-2.0으로 개방해 8만 7천여 스타의 거대한 저변을 확보하고, 전사적 시크릿 차단·비용 한도·감사 로그를 제공하는 엔터프라이즈 제어 계층(RTK Pro)은 BUSL-1.1 기반으로 수익화하는 영리한 오픈코어 전략을 구사한다.</li>
              <li><strong>에이전트 모델 종속성 제로:</strong> Claude Code, OpenCode, Codex, Cursor 등 어떤 에이전트나 모델을 쓰든 배시 레이어에서 동일하게 작동하기 때문에 LLM 세대교체 리스크로부터 자유로운 인프라 해자를 구축했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 더 큰 모델이 아니라 더 깨끗한 신호가 에이전트를 똑똑하게 만든다
            </h3>
            <p>
              우리는 종종 모델의 컨텍스트 창이 100만, 200만 토큰으로 커지면 모든 문제가 해결될 것이라 착각한다. 하지만 쓰레기를 넣으면 비싼 쓰레기가 나올 뿐, 에이전트의 주의력은 불필요한 로그 사이에서 빠르게 분산된다.
            </p>
            <p>
              단 25밀리초 만에 잡음을 걷어내고 핵심 신호만 남겨주는 RTK는 보여준다. AI 시대의 진짜 최적화는 모델 가중치 안에만 있는 것이 아니라, 모델에게 말을 거는 터미널 파이프 입구에도 있다는 사실을.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=RTK+Rust+Token+Killer+CLI+AI+agent" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://www.rtk-ai.app" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 / 파이프라인
              </a>
              <a href="https://github.com/rtk-ai/rtk" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
