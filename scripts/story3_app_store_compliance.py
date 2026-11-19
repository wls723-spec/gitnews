# -*- coding: utf-8 -*-
# Story 3: mjmirza/app-store-compliance

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] mjmirza/app-store-compliance                     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_app_store_compliance.jpg" alt="App Store Compliance Guard Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield-check" style="width:12px;height:12px;fill:#fff;"></i> PRE-SUBMIT GUARD</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fee2e2; border-color:#dc2626; color:#991b1b;">🛡️ 앱 스토어 25% 리젝트를 터미널에서 원천 차단</span>
              <span class="platform-tag">GitHub Trending &amp; Playbook</span>
              <span class="platform-tag">mjmirza / app-store-compliance</span>
            </div>

            <h2 class="article-headline">
              오후 한 나절 만에 앱을 짰는데, 심사에 일주일을 버린다? 바이브코딩 시대의 필수 가드 'App Store Compliance'
            </h2>

            <div class="article-subheadline">
              117개 애플·구글 심사 거부 패턴과 프라이버시 매니페스트, EU AI Act·DSA·COPPA 등 95개 글로벌 법규 시한을 코딩 에이전트 제출 훅으로 자동 차단하는 오픈 플레이북 (+542스타/일, 누적 1,782스타)
            </div>
            <p class="article-snippet">
              AI 코딩 도구의 확산으로 2026년 앱 출시 시도가 전년 대비 60~80% 폭증하자, 애플과 구글은 심사를 완화하기는커녕 4건 중 1건을 거절하며 빗장을 걸어 잠갔습니다. 오늘 하루 542스타를 쓸어 담으며 급부상한 <strong>mjmirza/app-store-compliance</strong>는 심사 거절 메일을 받고 일주일을 허비하는 대신, <code>fastlane</code>이나 <code>eas submit</code>을 치는 순간 에이전트가 먼저 코드를 스캔해 치명적 결함을 <code>BLOCKED.</code>로 막아세우는 자동 컴플라이언스 방어막입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 오후에 앱을 완성하고, 그날 밤 계정이 정지되는 시대
            </h3>
            <p>
              2026년 1분기, 양대 앱 마켓의 신규 제출 건수는 1년 전보다 60% 이상(iOS 단독 80%) 폭증했다. Claude Code나 Cursor를 켠 비전공자·1인 개발자도 오후 한 나절이면 번듯한 모바일 앱을 빌드해 낸다. 하지만 App Store Connect에 바이너리를 올리는 순간, 전혀 다른 현실이 기다린다. 애플은 연간 약 777만 건의 심사 중 약 193만 건(약 25%)을 거절하고 있고, 구글 역시 2025년 한 해에만 175만 건 이상의 플레이 스토어 제출을 정책 위반으로 차단했다.
            </p>
            <p>
              단 한 줄짜리 불친절한 거절 사유를 받고 추측으로 고쳐 재심사를 넣는 사이 일주일이 증발한다. 오늘 하루에만 542스타(누적 1,782스타)를 끌어올린 <strong>mjmirza/app-store-compliance</strong>는 이 불투명한 관문 앞에 엔지니어링의 빛을 비춘다. 117개의 실전 거부 패턴과 95개의 글로벌 규제 마감일(EU AI Act, DSA, COPPA, 연령 인증법)을 코드화해, 제출 커맨드가 실행되기 직전 터미널에서 먼저 심사관을 대신해 <strong>"통과 불가(BLOCKED)"</strong> 판정을 내려주는 오픈소스 가드다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: AI 생성 앱이 가장 많이 밟는 2개의 지뢰와 '가짜 인용'의 제거
            </h3>
            <p>
              바이브코딩으로 빠르게 만든 앱들이 거절당하는 이유는 놀라울 만큼 반복적이다. 첫째는 외부 AI API로 개인정보를 보내면서 제공자 이름을 명시한 동의 모달(Consent Modal)을 빠뜨리거나 프라이버시 매니페스트(Privacy Manifest)와 실제 서드파티 SDK 동작이 불일치하는 경우다. 둘째는 심사관용 라이브 백엔드 데모 계정 미비와 계정 삭제 기능 누락이다.
            </p>

            <div class="editorial-quote">
              <p>
                "확인할 수 없는 항목은 깨끗하다고 가정하지 않고 반드시 표면에 드러낸다. <strong>놓친 경고 하나는 일주일의 심사 거절 비용을 치르게 하지만, 미리 드러낸 경고는 단 1분이면 확인하고 고칠 수 있다.</strong>"
              </p>
              <small>— mjmirza/app-store-compliance 설계 원칙 (실제 Reddit 첫 심사 통과 후기 검증)</small>
            </div>

            <p>
              특히 이 프로젝트가 돋보이는 지점은 철저한 <strong>인용 무결성 검증(<code>verify-citations.py</code>)</strong>이다. 애플 개발자 페이지는 존재하지 않는 가짜 문서 ID를 넣어도 HTTP 200을 반환하기 때문에, 단순 상태 코드만 믿으면 AI가 지어낸 환각 가이드라인을 걸러내지 못한다. 저자는 호스트별 가짜 대조군 지문을 비교하는 검증 스크립트까지 내장해 모든 조항이 실제 애플·구글 원문과 연결되도록 강제했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: PreToolUse 훅 차단과 8종 연속 규제 모니터
            </h3>
            <p>
              저장소는 코딩 에이전트 사용자의 환경과 일반 개발자 환경을 모두 아우르는 정교한 다층 감사 파이프라인으로 구성된다:
            </p>
            <ul>
              <li><strong>13대 코딩 에이전트 자동 가드 (<code>scripts/install.sh --tool all</code>):</strong> Claude Code, Codex CLI, Gemini CLI, OpenCode, Cursor, Copilot, Grok, Qwen, Kimi, Factory Droid, Windsurf 등에 <code>PreToolUse</code> 훅으로 <code>app-store-compliance-guard.sh</code>를 설치한다. 에이전트가 <code>fastlane</code>, <code>eas submit</code>, <code>gradle bundleRelease</code>, <code>xcrun altool</code>을 실행하려 하면 즉시 가로채 <code>rejection-patterns.json</code>과 대조한다.</li>
              <li><strong>실전 판정 프로토콜 (<code>BLOCKED.</code> / <code>CLEAR.</code>):</strong> Xcode, Android, 혹은 Expo(<code>app.json</code>/<code>app.config</code>) 프로젝트를 스캔해 치명적 위험이 발견되면 파일·라인 번호와 정확한 수정안(<code>fix.</code>)을 출력하며 업로드를 중단시킨다.</li>
              <li><strong>8종 연속 규제 &amp; RSS 모니터:</strong> 애플 개발자 RSS 피드를 실시간 추적하는 <code>monitor.py</code>부터 <code>monitor-regulatory.py</code>(EU/UK/US 등 지역별 법규), <code>monitor-ai-policy.py</code>(생성형 AI 정책), <code>release-audit.py</code>, <code>accessibility-audit.py</code>, <code>deadline-checker.py</code>까지 완비했다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">App Store Compliance 사전 제출 차단 &amp; 규제 감사 파이프라인</span>
                <span class="schematic-badge">117 Rejection Patterns · 95 Legal Deadlines</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Agent Hook Intercept</div>
                  <div class="schematic-desc">
                    Claude · Codex · Cursor · Gemini 훅<br>
                    <code>fastlane</code> · <code>eas submit</code> 실행 감지<br>
                    <code>xcrun altool</code> · <code>gradle bundleRelease</code><br>
                    제출 명령 직전 자동 스캔 트리거
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Pattern &amp; Policy Scan</div>
                  <div class="schematic-desc">
                    117개 거절 패턴(<code>rejection-patterns.json</code>)<br>
                    Privacy Manifest + SDK 런타임 대조<br>
                    외부 AI 동의 모달 · 인앱결제 · 계정 삭제<br>
                    <strong>CRITICAL 발견 시 즉시 <code>BLOCKED.</code></strong>
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Regulatory &amp; Citation Gate</div>
                  <div class="schematic-desc">
                    95개 규제 타임라인(EU AI Act·DSA·COPPA)<br>
                    <code>verify-citations.py</code> 허위 HTTP 200 탐지<br>
                    <code>PRE-SUBMISSION-CHECKLIST.md</code> 점검<br>
                    <code>CLEAR.</code> 판정 후 안전한 1회성 심사 통과
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">App Store Compliance 공식 플레이북 웹 대시보드</span>
              </div>
              <img src="../assets/images/demo_app_store_compliance.png" alt="App Store Compliance Official Website Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ mjmirza.github.io/app-store-compliance 공식 사이트 실화면: iOS/Android 117대 리젝트 패턴, 95개 글로벌 법규 시한, 그리고 코딩 에이전트용 사전 차단 가드 사용법을 한눈에 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 플랫폼 권력 역학: '깜깜이 심사 게이트키핑'에 맞서는 집단 지성 방어선
            </h3>
            <p>
              애플과 구글의 앱 심사는 수십조 원 규모 모바일 경제의 절대적 문지기다. AI 시대에 플랫폼들이 불량 앱 차단을 명분으로 심사 기준과 EU DSA·AI Act 등 지역 규제를 촘촘하게 조이면서, 거대 법무팀과 컴플라이언스 전담 인력이 없는 인디 개발자와 소형 스타트업은 잦은 거절과 계정 정지 공포에 내몰리고 있다.
            </p>
            <ul>
              <li><strong>대기업 법무·QA팀의 민주화:</strong> 한 명의 개인 개발자가 구축하고 기계적 인용 검증으로 신뢰도를 담보한 오픈 플레이북이, 대기업 내부 컴플라이언스 체크리스트에 준하는 방어력을 무료로 제공한다.</li>
              <li><strong>소프트웨어 공학의 시프트-레프트(Shift-Left):</strong> 앱 스토어 심사를 "제출 후 기다리는 운의 영역"에서 "커밋·빌드 단계의 결정론적 정적 검증 영역"으로 끌어내린 것이 가장 큰 전환점이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 이제 당신의 AI 에이전트가 거절당할 앱의 업로드를 거부한다
            </h3>
            <p>
              코드를 빠르게 짜는 시대는 이미 왔다. 이제 진짜 경쟁력은 '얼마나 빨리 짜느냐'가 아니라 '한 번에 프로덕션 문턱을 넘을 수 있느냐'로 이동하고 있다.
            </p>
            <p>
              리젝트 메일을 받고 일주일을 날릴 것인가, 아니면 제출 버튼을 누르기 1분 전에 터미널에서 스스로를 차단할 것인가. <code>app-store-compliance</code>는 AI 코딩 에이전트에게 처음으로 '규제 감각과 자기 절제'를 가르치고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=App+Store+review+rejection+compliance+checklist+AI" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://mjmirza.github.io/app-store-compliance/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 플레이북 사이트
              </a>
              <a href="https://github.com/mjmirza/app-store-compliance" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
