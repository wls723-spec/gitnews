# -*- coding: utf-8 -*-
# Story 4: google-labs-code/stitch-skills

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] google-labs-code/stitch-skills                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_stitch_skills.jpg" alt="Google Stitch Design Skills Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="layers" style="width:12px;height:12px;fill:#fff;"></i> AGENT SKILLS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e3a8a;">🎨 구글 랩스 공식 UI 디자인-투-코드 스킬</span>
              <span class="platform-tag">GitHub Trending &amp; Google Stitch MCP</span>
              <span class="platform-tag">google-labs-code / stitch-skills</span>
            </div>

            <h2 class="article-headline">
              피그마 핸드오프의 시대는 끝났다? 구글 랩스가 푼 오픈 표준 에이전트 스킬 'Stitch Skills'
            </h2>

            <div class="article-subheadline">
              Stitch MCP 서버와 Agent Skills 오픈 표준을 결합해 디자인 시스템(DESIGN.md)·멀티페이지 웹사이트·React/Native 컴포넌트·Remotion 데모 영상까지 코딩 에이전트로 직결 (+369스타/일, 누적 10,383스타)
            </div>
            <p class="article-snippet">
              그동안 AI 코딩 에이전트에게 UI를 맡기면 "전형적인 보라색 그라데이션 AI 슬롭(AI Slop)"을 뱉어내기 일쑤였고, 반대로 기존 프로덕션 프론트엔드 코드의 디자인 시스템을 AI 디자인 도구와 양방향 동기화하는 것도 쉽지 않았습니다. 오늘 369스타를 보태며 누적 10,383스타를 돌파한 구글 랩스의 <strong>google-labs-code/stitch-skills</strong>는 <code>DESIGN.md</code>와 <code>SITE.md</code> 헌법 파일, 그리고 16종의 모듈형 스킬을 통해 Antigravity·Gemini CLI·Claude Code·Cursor·Codex를 디자인 엔지니어링 파이프라인으로 통합합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 디자인 캔버스와 프로덕션 코드베이스 사이의 '잃어버린 다리'
            </h3>
            <p>
              프론트엔드 개발팀의 가장 지루한 마찰은 언제나 디자인 툴과 IDE 사이의 번역 비용에서 발생한다. 디자이너가 캔버스에서 시안을 고치면 개발자가 CSS 토큰과 컴포넌트를 손으로 다시 깎아야 하고, 반대로 코드가 먼저 진화하면 디자인 시안은 며칠 만에 낡은 유물이 된다. 기존 AI 코드 생성기는 첫 화면은 그럴듯하게 뽑아내지만, 다섯 페이지짜리 일관된 웹 앱이나 기존 React 프로젝트의 <code>shadcn/ui</code>·디자인 토큰과 어긋나기 일쑤였다.
            </p>
            <p>
              구글 랩스(Google Labs)가 Apache-2.0 라이선스와 <code>agentskills.io</code> 오픈 표준에 맞춰 공개한 <strong>google-labs-code/stitch-skills</strong>는 이 단절을 원격 Stitch MCP 서버와 3개 플러그인 번들(<code>stitch-design</code>, <code>stitch-build</code>, <code>stitch-utilities</code>)로 꿰매 버렸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 특정 IDE에 가두지 않는 '오픈 표준 에이전트 스킬' 전략
            </h3>
            <p>
              이번 저장소가 주목받는 결정적 이유는 구글이 자사의 Gemini CLI나 Antigravity만을 위한 폐쇄형 플러그인이 아니라, 경쟁 에이전트인 <strong>Claude Code, Cursor, Codex, OpenCode</strong>까지 모두 지원하는 개방형 패키지로 설계했다는 점이다.
            </p>

            <div class="editorial-quote">
              <p>
                "Google Stitch용 에이전트 스킬과 플러그인 모음은 <strong>Agent Skills 오픈 표준</strong>을 따르며, Codex·Antigravity·Gemini CLI·Claude Code·Cursor·OpenCode 등 어떤 코딩 에이전트에서도 즉시 호환된다."
              </p>
              <small>— google-labs-code/stitch-skills 공식 문서 (Apache-2.0)</small>
            </div>

            <p>
              특히 최근(11월 17~18일) 머지된 <code>site-md</code> 스킬은 프로젝트 브리프에서 사이트 전체의 아키텍처 헌법(<code>SITE.md</code>)을 먼저 도출한 뒤 <code>stitch-loop</code>로 멀티페이지 웹사이트를 자동 빌드·검증하게 만들며, 프롬프트 한 줄짜리 장난감 데모를 엔지니어링 워크플로우로 격상시켰다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Design ↔ Build ↔ Utilities 3단 양방향 파이프라인
            </h3>
            <p>
              <code>plugins/</code> 디렉토리 아래 3개의 플러그인으로 모듈화된 Stitch Skills는 코드에서 디자인을 역추출하고 다시 프로덕션 코드로 내보내는 완전한 왕복(Round-trip) 파이프라인을 제공한다:
            </p>
            <ul>
              <li><strong><code>stitch-design</code> (양방향 동기화 &amp; 정적 스냅샷):</strong> <code>code-to-design</code>과 <code>extract-design-md</code>로 기존 React/Vue 코드나 <code>localhost:3000</code> 실행 화면(<code>extract-static-html</code>)에서 <code>DESIGN.md</code> 토큰을 추출해 Stitch 프로젝트에 업로드하고, <code>generate-design</code>으로 다크모드·고밀도 변형을 즉시 생성한다.</li>
              <li><strong><code>stitch-build</code> (프레임워크 변환 &amp; 영상 워크스루):</strong> 확정된 Stitch 화면을 <code>react-components</code>, <code>react-native</code>, <code>react-vite-dashboard</code>(TanStack Query 연동), <code>shadcn-ui</code> 규격의 검증된 코드로 변환하고, 심지어 <code>remotion</code> 스킬로 부드러운 줌·전환이 들어간 제품 소개 영상까지 자동 렌더링한다.</li>
              <li><strong><code>stitch-utilities</code> (<code>taste-design</code> &amp; <code>SITE.md</code> 헌법):</strong> 모호한 프롬프트를 정제하는 <code>enhance-prompt</code>, 뻔한 AI 스타일을 배제하고 정밀 타이포그래피와 색채를 강제하는 <code>taste-design</code>, 그리고 멀티페이지 일관성을 지키는 <code>site-md</code> + <code>stitch-loop</code> 자동 검증 루프를 묶어 제공한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Google Stitch Skills × Stitch MCP 양방향 디자인 엔지니어링 파이프라인</span>
                <span class="schematic-badge">Apache-2.0 · Agent Skills Open Standard</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Utilities &amp; Constitution</div>
                  <div class="schematic-desc">
                    <code>enhance-prompt</code> UI 명세 구체화<br>
                    <code>taste-design</code> 안티-AI-슬롭 규칙<br>
                    <code>extract-design-md</code> → <code>DESIGN.md</code><br>
                    <code>site-md</code> 사이트 구조 헌법 생성
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Stitch MCP &amp; Design</div>
                  <div class="schematic-desc">
                    원격 Stitch MCP 서버 실시간 통신<br>
                    <code>code-to-design</code> 기존 코드 업로드<br>
                    <code>generate-design</code> 변형·편집 생성<br>
                    <code>stitch-loop</code> 멀티페이지 자동 빌드
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Production Build Outputs</div>
                  <div class="schematic-desc">
                    <code>react-components</code> · <code>shadcn-ui</code><br>
                    <code>react-native</code> 모바일 네이티브 코드<br>
                    <code>react-vite-dashboard</code> 대시보드<br>
                    <code>remotion</code> 자동 시연 영상 렌더링
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Google Stitch MCP 공식 설정 가이드 및 플랫폼 포털</span>
              </div>
              <img src="../assets/images/demo_stitch_skills.png" alt="Google Stitch MCP Setup Documentation" class="showcase-img">
              <p class="showcase-caption">
                ▲ stitch.withgoogle.com 공식 MCP 설정 문서 실화면: Antigravity, Gemini CLI, Claude Code, Cursor 등 다양한 AI 코딩 에이전트에 Stitch MCP 서버와 오픈 스탠다드 스킬을 연결하는 절차를 안내한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 디자인 툴 시장의 지각 변동: '파일(Figma)' 중심에서 '마크다운 헌법(DESIGN.md)' 중심으로
            </h3>
            <p>
              Stitch Skills가 던지는 가장 묵직한 신호는 디자인 시스템의 진실의 원천(Source of Truth)이 바이너리 캔버스 파일에서 버전 관리가 가능한 시맨틱 텍스트(<code>DESIGN.md</code>, <code>SITE.md</code>)로 이동하고 있다는 점이다.
            </p>
            <ul>
              <li><strong>크로스 에이전트 생태계 선점:</strong> 구글이 <code>npx skills add google-labs-code/stitch-skills</code>와 <code>npx plugins add</code>를 통해 자사 MCP 서버를 타사 코딩 에이전트의 기본 디자인 엔진으로 심으면서, 프론트엔드 UI 생성의 표준 허브 자리를 노리고 있다.</li>
              <li><strong>디자이너와 엔지니어의 역할 재편:</strong> 정적 목업 화면 수십 장을 수동으로 정렬하는 대신, 브랜드 미학을 <code>DESIGN.md</code>와 <code>taste-design</code> 규칙으로 명문화해 에이전트 루프를 지휘하는 '디자인 아키텍트'로 역할이 진화하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 스킬 파일 몇 개가 바꾼 프론트엔드 팀의 월요일 아침
            </h3>
            <p>
              불과 1년 전만 해도 에이전트 스킬은 개발자가 개인 블로그에 올리던 프롬프트 요령에 불과했다. 하지만 이제 구글 랩스가 직접 16개의 정교한 워크플로우 스킬을 오픈 표준으로 패키징해 배포하는 시대가 열렸다.
            </p>
            <p>
              디자인과 코드가 하나의 MCP 루프 안에서 서로를 실시간으로 번역하기 시작할 때, 우리에게 남는 것은 툴을 옮겨 다니는 반복 노동이 아니라 "무엇을 만들 가치가 있는가"라는 순수한 제품 감각뿐이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Google+Stitch+MCP+Agent+Skills+design+to+code" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://stitch.withgoogle.com/docs/mcp/setup/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 Stitch MCP 가이드
              </a>
              <a href="https://github.com/google-labs-code/stitch-skills" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
