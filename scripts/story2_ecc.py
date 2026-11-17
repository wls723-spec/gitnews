# -*- coding: utf-8 -*-
# Story 2: affaan-m/ECC

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] affaan-m/ECC                                     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ecc.jpg" alt="ECC Agent Harness OS Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> 305K STARS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#14532d;">⚙️ 에이전트 하네스 운영체제</span>
              <span class="platform-tag">GitHub Trending &amp; ecc.tools</span>
              <span class="platform-tag">affaan-m / ECC</span>
            </div>

            <h2 class="article-headline">
              30만 스타를 돌파한 코딩 에이전트의 '운영체제': 72개 에이전트·327개 스킬·보안 방패를 하나로 묶은 'ECC'
            </h2>

            <div class="article-subheadline">
              매 세션 프롬프트를 새로 짜는 비효율을 끝내고, 계획·테스트·구현·리뷰·학습·보안 감사(AgentShield)를 에이전트 하네스에 영구 각인하는 MIT 오픈소스 시스템 (305,454스타)
            </div>
            <p class="article-snippet">
              Claude Code, Codex, Cursor 같은 코딩 에이전트가 코드를 짜는 능력은 이미 상향 평준화됐지만, 실무에서는 세션이 바뀔 때마다 규칙을 잊고 테스트 없이 코드를 밀어 넣는 '기억 상실증'이 최대 약점이었습니다. 오늘 하루 902스타를 보태며 누적 305,454스타라는 경이로운 기록을 세운 <strong>affaan-m/ECC</strong>는 72종의 전문 에이전트, 327개 스킬, 지속 학습(Instincts) 메모리, 그리고 내장 보안 스캐너까지 단 한 줄의 설치 명령(<code>npx ecc-universal@2.2.3 setup</code>)으로 이식합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 모델 전쟁이 끝나고 시작된 '하네스(Harness) 패권' 경쟁
            </h3>
            <p>
              2026년 개발 현장에서는 더 이상 "어떤 LLM 모델이 1% 더 똑똑한가"만이 승패를 가르지 않는다. 같은 모델을 써도 어떤 팀은 PR 한 번에 프로덕션 수준의 코드를 뽑아내고, 어떤 팀은 에이전트가 컨텍스트 창을 낭비하며 엉뚱한 파일을 부수는 일이 비일비재하다. 차이를 만드는 것은 모델 바깥의 <strong>하네스(Harness)</strong>, 즉 계획·검증·기억·보안 규율의 총체다.
            </p>
            <p>
              오늘 GitHub 트렌딩에서 902스타를 추가하며 305,454스타 고지를 밟은 <strong>affaan-m/ECC</strong>(v2.2.3)는 개인의 프롬프트 팁 모음집 수준을 완전히 벗어나, 코딩 에이전트를 위한 사실상의 표준 '엔지니어링 운영체제'로 자리매김했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "컨텍스트 창을 최적화하라, 나머지는 전부 영속화하라"
            </h3>
            <p>
              ECC의 설계 철학은 단 한 문장으로 요약된다. 에이전트의 한정된 작업 기억(컨텍스트 창)에 잡다한 지침을 몰아넣는 대신, 필요한 순간에만 적재적소의 전문 스킬과 규율을 호출하고 세션에서 얻은 성공 패턴은 <strong>'본능(Instincts)'</strong>으로 저장해 다음 작업에 자동 재사용하는 구조다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신의 에이전트는 코드를 짤 수 있다. 하지만 ECC는 에이전트에게 <strong>조율된 엔지니어링 시스템</strong>을 부여한다. <strong>컨텍스트 창을 최적화하고, 그 외 모든 것은 영속화하라.</strong>"
              </p>
              <small>— affaan-m/ECC 공식 아키텍처 매니페스토 (MIT 라이선스 · v2.2.3)</small>
            </div>

            <p>
              초기 Claude Code 중심에서 출발한 ECC는 최신 2.2 버전에서 <code>ecc-universal</code> 패키지로 진화했다. Claude Code와 Codex·Kimi Code의 네이티브 플러그인 경로는 물론 Cursor, OpenCode, Gemini CLI, Zed, GitHub Copilot, Antigravity까지 크로스 하네스 어댑터를 제공하며 단일 팀 내 이기종 AI 툴 공존 문제를 풀어냈다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 7단계 엔지니어링 루프와 AgentShield 보안 게이트
            </h3>
            <p>
              ECC가 327개 스킬과 72개 에이전트를 충돌 없이 굴리는 비결은 엄격한 생명주기 제어와 내장 감사 계층에 있다:
            </p>
            <ul>
              <li><strong>7단계 강제 개발 루프 (<code>plan → test → implement → review → verify → remember → improve</code>):</strong> 훅(Hooks)과 선택적 규칙(Rules)을 통해 에이전트가 계획 수립과 TDD 테스트 작성 없이 성급히 구현으로 넘어가지 못하도록 런타임에서 통제하며, 구현 뒤에는 새로운 컨텍스트에서 교차 리뷰를 수행한다.</li>
              <li><strong>세션 요약 &amp; 지속 학습(Continuous Learning &amp; Instincts):</strong> 반복적으로 성공한 문제 해결 패턴과 프로젝트 고유 규약을 휘발시키지 않고 구조화된 메모리와 재사용 가능한 스킬·본능으로 축적해, 매 세션 프롬프트 재설계 비용을 제거한다.</li>
              <li><strong>내장 보안 스캐너 <code>ecc-agentshield</code>:</strong> 에이전트 설정 자체가 공격 표면이 되는 시대에 맞춰 프롬프트, 훅 스크립트, MCP 설정, 권한 정책, 하드코딩된 시크릿까지 자동 감사하는 방어 레이어를 기본 통합했다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">ECC v2.2 에이전트 하네스 운영체제 아키텍처</span>
                <span class="schematic-badge">MIT · 72 Agents · 327 Skills</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Surface &amp; Adapters</div>
                  <div class="schematic-desc">
                    <code>npx ecc-universal@2.2.3 setup</code><br>
                    Claude Code · Codex · Kimi 네이티브<br>
                    Cursor · Gemini · Zed · Antigravity 어댑터<br>
                    327개 도메인별 <code>Skills</code> &amp; 98개 커맨드
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Runtime Enforcement Loop</div>
                  <div class="schematic-desc">
                    Plan → TDD Test → Implement → Review<br>
                    Hooks 기반 컨텍스트 예산 제어<br>
                    72개 전문 서브에이전트 (아키텍처·빌드 수리)<br>
                    <code>ecc-agentshield</code> 프롬프트·MCP 보안 스캔
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Persistence &amp; Memory</div>
                  <div class="schematic-desc">
                    Session Summaries 자동 기록<br>
                    Continuous Learning 경험 증류<br>
                    <code>Instincts</code> 반복 승리 패턴 영속화<br>
                    언어·프로젝트별 선택적 Rules 로딩
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">ECC 공식 플랫폼 및 스킬 카탈로그 포털 (ecc.tools)</span>
              </div>
              <img src="../assets/images/demo_ecc.png" alt="ECC Official Tools Portal" class="showcase-img">
              <p class="showcase-caption">
                ▲ ecc.tools 공식 포털 실구동 화면: 72개 전문 에이전트, 327개 스킬, AgentShield 보안 스캐너 및 크로스 플랫폼 하네스 지원 매트릭스를 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 생태계 판도 변화: '벤더 종속 IDE'를 무력화하는 오픈 표준 하네스
            </h3>
            <p>
              30만 개가 넘는 스타와 수많은 기업 스폰서가 ECC에 몰리는 이유는, AI 코딩 도구의 가치가 IDE UI가 아니라 '팀에 축적된 엔지니어링 규율과 스킬 자산'으로 이동했기 때문이다.
            </p>
            <ul>
              <li><strong>스위칭 비용의 역전:</strong> Claude Code에서 Codex나 Cursor로 갈아타더라도 ECC에 담아둔 테스트 규율, 아키텍처 규칙, 보안 감사 훅은 그대로 따라온다. 에이전트 런타임이 교체 가능한 부품(Commodity)이 되는 순간이다.</li>
              <li><strong>공급망 보안의 표준화:</strong> 외부 스킬 마켓플레이스에서 가져온 훅이나 MCP 설정이 개발자 PC의 비밀 키를 탈취할 수 있다는 우려 속에서, <code>ecc-agentshield</code>의 통합은 오픈소스 에이전트 팩의 신뢰 기준선을 끌어올렸다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 리눅스 배포판처럼 진화하는 에이전트 하네스
            </h3>
            <p>
              초기 리눅스 커널 주변에 수많은 유틸리티와 패키지 매니저가 모여 완전한 운영체제 배포판이 되었듯, 오늘날 AI 코딩 에이전트 주변에서도 '무엇이 기본 표준 번들이 될 것인가'를 둘러싼 거대한 수렴이 일어나고 있다.
            </p>
            <p>
              305,454스타를 기록한 ECC의 폭발적 성장은 한 가지를 분명히 말해준다. 개발자들은 이제 에이전트에게 "코드를 짜달라"고 빌지 않는다. 검증되고 기억하며 스스로 보안을 지키는 엔지니어링 체제 전체를 설치하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=affaan-m+ECC+agent+harness+Claude+Code" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://ecc.tools" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 ECC.tools 포털
              </a>
              <a href="https://github.com/affaan-m/ECC" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
