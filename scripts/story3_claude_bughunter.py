# -*- coding: utf-8 -*-
# Story 3: elementalsouls/Claude-BugHunter

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] elementalsouls/Claude-BugHunter                  -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_claude_bughunter.jpg" alt="Claude-BugHunter Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield" style="width:12px;height:12px;fill:#fff;"></i> RED TEAM AI</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fee2e2; border-color:#dc2626; color:#991b1b;">🎯 실전 버그바운티 83종 스킬</span>
              <span class="platform-tag">GitHub Trending &amp; Security</span>
              <span class="platform-tag">elementalsouls / Claude-BugHunter</span>
            </div>

            <h2 class="article-headline">
              "챗봇을 시니어 레드팀 해커로 변신시키다" — HackerOne 681건 실전 패턴을 이식한 'Claude-BugHunter'
            </h2>

            <div class="article-subheadline">
              83개 공격 보안 스킬, 15개 슬래시 명령어, 24개 취약점 클래스, 엔터프라이즈 CVE 체인 및 Burp MCP 연동까지 통합한 MIT 오픈소스 공격 보안 에이전트 스위트 (7,386스타)
            </div>
            <p class="article-snippet">
              일반 코딩 에이전트에게 웹 보안 점검을 시키면 교과서적인 "입력값을 검증하세요" 수준의 피상적 조언만 내놓다 멈춥니다. 하루 1,057스타를 폭발적으로 끌어모으며 누적 7,386스타를 달성한 <strong>elementalsouls/Claude-BugHunter</strong>는 681건의 실제 공개된 HackerOne 버그바운티 리포트와 엔터프라이즈 ID·인프라 공격 매트릭스를 83개 <code>SKILL.md</code>로 구조화해, Claude Code·Codex·Antigravity가 실제 인가된 모의해킹 수순 그대로 타깃을 분석하게 만듭니다.
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
              <i data-lucide="flame"></i> 1. 리드: 교과서 보안과 실전 버그바운티 사이의 거대한 간극
            </h3>
            <p>
              모의해킹과 버그바운티 현장은 단순한 취약점 스캐너(DAST) 버튼을 누르는 작업이 아니다. 시니어 헌터는 서브도메인 열거와 기술 스택 핑거프린팅으로 공격 표면을 좁힌 뒤, OAuth 리다이렉트 우회, GraphQL 인트로스펙션 노출, IDOR와 권한 상승을 엮어 실제 비즈니스 영향력을 입증하는 '체인(Chain)'을 설계한다.
            </p>
            <p>
              하지만 기존 AI 에이전트는 이런 비선형적 공격 사고(Red-Team Mindset)와 최신 CVE 익스플로잇 맥락이 텅 비어 있었다. 바로 이 공백을 정면 돌파하며 오늘 GitHub 일간 트렌딩 최상위권(1,057스타/일, 총 7,386스타)을 점령한 프로젝트가 보안 연구자 사친 샤르마(Sachin Sharma)가 공개한 <strong>Claude-BugHunter</strong>다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 681건 HackerOne 실전 리포트를 'Topic-Triggered' 스킬로 증류
            </h3>
            <p>
              <code>Claude-BugHunter</code>가 단순한 프롬프트 모음집이 아닌 이유는 방대한 실전 데이터를 4계층 스택(Think → Hunt → Perimeter → Ship)으로 정교하게 모듈화했기 때문이다. 사용자는 복잡한 명령어를 외울 필요조차 없다.
            </p>

            <div class="editorial-quote">
              <p>
                "테스트할 대상을 평범한 영어로 설명하기만 하면 해당 주제의 <code>hunt-*</code> 스킬이 <strong>이름을 부르지 않아도 자동으로 로드된다.</strong> 681건의 공개 HackerOne 패턴 중 433건이 개별 인용·감사 가능하며, 범위 이탈(OOS) 반박과 7문항 트리아지 게이트까지 내장되어 있다."
              </p>
              <small>— Claude-BugHunter 공식 아키텍처 및 4-Layer 스택 명세 (MIT 라이선스)</small>
            </div>

            <p>
              게다가 이 스킬들은 <code>SKILL.md</code> 오픈 표준을 따르기 때문에 Claude Code뿐만 아니라 OpenCode, OpenAI Codex CLI, Hermes Agent, Google Antigravity 등 주요 멀티 에이전트 하네스에서 <code>bash scripts/install.sh --all --burp-mcp</code> 명령 한 줄로 동일하게 구동된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 4계층 공격 매트릭스와 Burp MCP · 7-Question Gate
            </h3>
            <p>
              에이전트가 범위 밖(Out-of-Scope) 자산을 건드리거나 오탐(False Positive) 리포트를 양산하는 사고를 막으면서도 치명적 취약점을 파고들게 만드는 내부 구조는 다음과 같다:
            </p>
            <ul>
              <li><strong>Think &amp; Hunt (비선형 정찰 + 58종 <code>hunt-*</code> 스킬):</strong> <code>bb-methodology</code>가 정찰 결과를 바탕으로 공격 표면을 순위화하고, 24개 핵심 취약점 클래스별 탐지 패턴·페이로드·우회 테이블(Bypass Table)·체인 템플릿을 동적 로딩한다.</li>
              <li><strong>Hit the Perimeter (엔터프라이즈 인프라 매트릭스):</strong> M365/Entra, Okta, vCenter, SSL-VPN 어플라이언스, SharePoint, 클라우드 IAM 등 기업 경계망을 노리는 2024~2026년 최신 CVE 체인과 자격증명 탈취 후 권한 상승(Post-Credential Escalation) 경로를 체계화했다.</li>
              <li><strong>Burp MCP 연동 &amp; Ship It (7-Question Gate):</strong> 터미널 네이티브 <code>cbh</code> CLI와 Burp Suite MCP 서버가 실제 HTTP 트래픽을 주고받으며 검증하고, 보고 단계에서는 <code>triage-validation</code>의 7단계 검증 게이트, VRT 기반 심각도 산정, PII 마스킹(<code>evidence-hygiene</code>)을 거쳐 제출 가능한 리포트를 생성한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Claude-BugHunter 4-Layer 공격 보안 스택 &amp; 멀티 하네스 아키텍처</span>
                <span class="schematic-badge">83 Skills · 681 Patterns · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Think &amp; Hunt Webapps</div>
                  <div class="schematic-desc">
                    5단계 비선형 정찰(<code>web2-recon</code>)<br>
                    HackerOne 681건 기반 58개 <code>hunt-*</code> 스킬<br>
                    24개 취약점 클래스 우회 페이로드 테이블<br>
                    OAuth · GraphQL · Race Condition 체이닝
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Perimeter &amp; Burp MCP</div>
                  <div class="schematic-desc">
                    Entra · Okta · vCenter · SSL-VPN CVE 체인<br>
                    Burp Suite MCP 실시간 트래픽 인터셉트<br>
                    <code>cbh</code> 터미널 러너 &amp; <code>hunt</code> 작업 폴더 스캐폴더<br>
                    Claude · Codex · Antigravity 동시 지원
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Ship &amp; Evidence Hygiene</div>
                  <div class="schematic-desc">
                    오탐 차단용 7-Question Validation Gate<br>
                    VRT 심각도 매핑 &amp; OOS(범위외) 반박 논리<br>
                    증적 내 개인정보(PII) 자동 비식별화<br>
                    DVWA · OWASP Juice Shop 실전 훈련 대응
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Claude-BugHunter 공식 프로젝트 포털 &amp; 스킬 카탈로그 (elementalsouls.github.io)</span>
              </div>
              <img src="../assets/images/demo_claude_bughunter.png" alt="Claude-BugHunter Official Portal and Skill Catalog" class="showcase-img">
              <p class="showcase-caption">
                ▲ elementalsouls.github.io/Claude-BugHunter 실구동 포털: 83개 보안 스킬, 15개 슬래시 커맨드, 681개 공개 버그바운티 패턴 및 다중 에이전트 하네스 설치 매트릭스를 한눈에 탐색할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 보안 산업의 분기점: 공격과 방어의 AI 비대칭 해소와 윤리적 경계
            </h3>
            <p>
              그동안 버그바운티 프로그램 운영사들은 "AI가 생성한 저품질 스팸 리포트(AI Slop)" 때문에 심각한 트리아지 피로감을 호소해 왔다. LLM이 그럴듯한 문장으로 사실 확인도 안 된 취약점을 무작위 제보했기 때문이다.
            </p>
            <ul>
              <li><strong>방어자·인가된 레드팀을 위한 '재현 가능한 증거' 규율:</strong> <code>Claude-BugHunter</code>는 7문항 자가 검증 게이트와 <code>evidence-hygiene</code>를 강제해 허위 제보를 걸러내고, 기업 보안팀이 자사 배포 전 DVWA·스테이징 환경에서 선제 레드팀 감사를 자동화하도록 돕는다.</li>
              <li><strong>표준 <code>SKILL.md</code>가 만든 지식 자산화:</strong> 10년 차 보안 연구자의 암묵지와 681건의 취약점 체인 노하우가 깃허브의 버전 관리 가능한 오픈소스 텍스트 스킬로 코드화되면서 보안 역량의 민주화가 가속화되고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 방패보다 먼저 움직이는 창, 코드로 공개된 해커의 두뇌
            </h3>
            <p>
              공격자와 방어자의 싸움은 늘 '누가 더 빠르게 틈을 찾아내느냐'의 속도전이었다.
            </p>
            <p>
              681개의 실전 취약점 패턴이 에이전트의 기본 스킬셋으로 오픈소스화된 지금, 보안 팀에게 주어진 선택지는 명확하다. 공격자가 이 스킬 번들을 돌리기 전에, 우리 개발 파이프라인이 먼저 <code>Claude-BugHunter</code>를 돌려 스스로의 성벽을 두드려 보는 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Claude-BugHunter+AI+bug+bounty+skills" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://elementalsouls.github.io/Claude-BugHunter" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 문서 &amp; 스킬 카탈로그
              </a>
              <a href="https://github.com/elementalsouls/Claude-BugHunter" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
