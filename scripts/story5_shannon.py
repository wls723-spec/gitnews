# -*- coding: utf-8 -*-
# Story 5: KeygraphHQ/shannon

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] KeygraphHQ/shannon : 자율 AI 웹 침투 테스트 에이전트 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_shannon.jpg" alt="Shannon AI Pentester" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #5</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 증명되지 않은 취약점은 소음이다: 100% 실증 기반 자율 해킹</span>
              <span class="platform-tag">Weekly Highlight</span>
              <span class="platform-tag">KeygraphHQ / shannon</span>
            </div>
            
            <h2 class="article-headline">
              코드를 읽고 실제 제로데이 익스플로잇까지 입증한다: 자율 침투 테스트 AI 'Shannon'
            </h2>

            <div class="article-subheadline">
              "No exploit, no report" — 정적 코드 분석(SAST)과 격리된 샌드박스 런타임 타격을 직결… 소스코드 취약점 후보 중 실제 쉘(Shell)을 탈취하고 공격에 성공한 치명적 버그만을 입증해 보고하는 5.1만 스타의 파괴적 보안 에이전트
            </div>
            <p class="article-snippet">
              수천 건의 오탐(False Positive)으로 보안 엔지니어를 지치게 하던 기존 정적 분석 도구의 한계를 근본적으로 돌파. 최신 php2shell RCE 공격 체인까지 단숨에 검증하며, 배포 전 소프트웨어의 실제 해킹 가능성을 실증적으로 규명하는 자율 화이트햇 에이전트 Shannon의 내부 메커니즘을 파헤칩니다.
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
              <i data-lucide="flame"></i> 1. 리드: 수천 장의 가짜 경보 보고서에 질린 화이트햇 해커들
            </h3>
            <p>
              기업의 보안 담당자와 개발자들에게 기존 정적 코드 분석기(SonarQube, Checkmarx 등)가 내놓는 보안 감사 리포트는 일종의 '재앙'이었다. 
              수백 페이지에 달하는 PDF 문서에는 수천 개의 "심각한 잠재적 취약점"이 적혀 있지만, 실제로 공격자가 접근해 익스플로잇(Exploit)을 성공시킬 수 있는 유효 취약점은 1% 미만이었다. 
              이 가짜 경보(False Positive)의 홍수 속에서 엔지니어들은 번아웃에 빠졌고, 정작 진짜 치명적인 제로데이 버그는 무시당한 채 프로덕션으로 배포되었다.
            </p>
            <p>
              정보 이론의 아버지 클로드 섀넌(Claude Shannon)의 이름을 따 명명된 <strong>KeygraphHQ/shannon</strong>은 이 오랜 보안 업계의 병폐를 가장 과격하고 대담한 철학으로 격파했다. 
              그들의 철학은 단 한 문장으로 요약된다: 
              <strong>"No exploit, no report (실제 익스플로잇 증명이 없으면, 한 줄의 보고서도 쓰지 않는다)."</strong>
            </p>
            <p>
              단 한 번의 CLI 명령어(<code>npx @keygraph/shannon@latest</code>)로 실행되는 Shannon은, 소스코드를 읽는 데서 멈추지 않는다. 
              격리된 도커 환경에서 타깃 웹 애플리케이션을 직접 기동하고, 고도로 훈련된 에이전트 편대를 출격시켜 실제 해커처럼 페이로드를 날려 공격 성공을 두 눈으로 확인했을 때만 보고서를 발행한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 화이트박스 정적 분석과 블랙박스 런타임 침투의 융합
            </h3>
            <p>
              지금까지 보안 감사는 두 개의 고립된 섬으로 나뉘어 있었다. 
              내부 코드를 들여다보는 정적 분석(SAST)은 실행 맥락을 몰라 오탐이 극심했고, 외부에서 침투를 시도하는 펜테스터(DAST)는 내부 코드를 보지 못해 복잡한 비즈니스 로직 취약점을 놓쳤다.
            </p>

            <div class="editorial-quote">
              <p>
                "인간 펜테스터가 가장 강력한 이유는 코드를 읽으면서 동시에 브라우저를 두드려 공격하기 때문이다. 
                Shannon은 이 두 가지 감각을 단일 AI 아키텍처로 융합했다. 
                <strong>공격 성공이 로그로 입증되지 않은 취약점은 보안 엔지니어의 시간을 뺏을 자격이 없다.</strong>"
              </p>
              <small>— Keygraph 보안 연구소 수석 아키텍트</small>
            </div>

            <p>
              Shannon은 최근 글로벌 인터넷을 강타한 치명적인 <strong>'php2shell' 원격 코드 실행(RCE)</strong> 공격 체인 검증 프로브(<code>--exp-php2shell</code>)를 즉시 오픈소스로 탑재하며, 
              이론상의 취약점이 실제 서버 탈취로 이어지는지 3분 만에 실증하는 독보적인 실전성을 입증했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 6단계 자율 정찰-타격-화해(Reconciliation) 파이프라인
            </h3>
            <p>
              Shannon의 내부는 다단계 에이전트 오케스트레이션 파이프라인으로 설계되어 있다.
            </p>

            <!-- 순수 HTML+CSS 다이어그램: Shannon 자율 침투 테스트 아키텍처 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">ARCHITECTURE SCHEMATIC</span>
                <span class="schematic-title">Shannon 자율 침투 테스트(Pentest) 6단계 검증 루프</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #ef4444;">
                  <div class="schematic-card-title" style="color: #b91c1c;">1~3단계: 정찰 & 가설 수립</div>
                  <div class="schematic-step">1. 런타임 정찰: Injection, XSS, SSRF, Auth 전문 에이전트</div>
                  <div class="schematic-step">2. 코드 분석(SAST): 신뢰 경계 및 위험 데이터 흐름 매핑</div>
                  <div class="schematic-step">3. Finding Reconciliation: 중복 제거 및 단일 공격 큐 생성</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">4~6단계: 실제 타격 & 증명</div>
                  <div class="schematic-step">4. Exploitation Agents: 실제 PoC 공격 페이로드 실행</div>
                  <div class="schematic-step">5. Validation Gate: 공격 미입증 후보 전량 자동 폐기 (Drop)</div>
                  <div class="schematic-step">6. Reporting: 증거 스크린샷·패킷 포함 SARIF/PDF 발행 &rarr; CI/CD 차단</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ Shannon은 소스코드 의심점과 런타임 공격 가능성을 크로스체크하여, 샌드박스 내부에서 실제 권한 탈취가 일어났을 때만 빌드를 차단한다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_shannon.png" alt="Shannon AI Pentester in action" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ Shannon 공식 웹 애플리케이션 & API 자율 침투 테스트 콘솔:</strong> 
                로컬 CLI에서 단일 명령어로 실행되며, 에이전트가 소스코드 구조를 파악하고 브라우저/API 엔드포인트를 향해 실제 익스플로잇을 감행한 실시간 터미널 타임라인 및 입증된 취약점 리포트를 출력한다.
              </div>
            </div>

            <p>
              각각의 스캔은 격리된 <strong>단발성(Ephemeral) 도커 컨테이너</strong>에서 안전하게 실행되므로, 에이전트가 격렬한 침투 공격을 수행하더라도 개발자의 로컬 머신이나 실제 프로덕션 서버에는 어떤 부수적 피해도 주지 않는다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 수천만 원대 침투 테스트 컨설팅 시장의 해체
            </h3>
            <p>
              전통적인 화이트햇 해킹 및 모의 침투 테스트(Pentest)는 고도로 전문화된 소수 보안 컨설팅 펌의 전유물이었다. 
              기업들은 분기마다 한 번 웹사이트 점검을 위해 수천만 원에서 수억 원의 용역비를 지불해야 했다. 
              하지만 3개월마다 한 번 받는 보고서는 매일 수십 번 배포되는 현대의 애자일 CI/CD 환경에서 아무런 방패가 되지 못했다.
            </p>
            <p>
              Shannon은 이 비싼 인간 전문가의 모의 해킹 프로세스를 <strong>'깃허브 액션(GitHub Actions) CI/CD 파이프라인의 1단계 체크'</strong>로 끌어내렸다. 
              모든 Pull Request가 열릴 때마다 자율 에이전트가 백그라운드에서 실시간 해킹 테스트를 수행하고 익스플로잇 가능 여부를 판정함으로써, 고비용 보안 외주 시장의 패러다임을 뿌리부터 뒤흔들고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 완벽한 방패는 가장 날카로운 창을 품는다
            </h3>
            <p>
              취약점을 찾았다고 주장하는 수많은 도구가 있었다. 
              그러나 실제로 칼을 쥐고 벽을 뚫어 증명해 보인 도구는 없었다. 
              Keygraph의 Shannon은 인공지능이 인간 보안 연구원의 '직관적인 공격성'을 마침내 코드 레벨에서 완벽하게 모사할 수 있음을 증명했다.
            </p>
            <p>
              내 코드가 세상에 공개되기 전, 나보다 먼저 내 코드를 해킹해 줄 자율 에이전트가 존재한다는 것. 
              그것이야말로 악의적인 블랙햇 해커들의 공격이 난무하는 현대 웹에서 엔지니어가 가질 수 있는 가장 든든하고 강력한 디지털 갑옷이다.
            </p>

            <div class="project-links-bar">
              <a href="https://keygraph.io/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>Keygraph 공식 사이트 둘러보기</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=shannon+ai+pentester+keygraph" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/KeygraphHQ/shannon" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+51.0k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
