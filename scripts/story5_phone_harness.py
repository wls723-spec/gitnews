# -*- coding: utf-8 -*-
# Story 5: phone-harness/phone-harness

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] phone-harness/phone-harness                      -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_phone_harness.jpg" alt="Phone Harness Zero-Jailbreak Agent Mobile Control Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="smartphone" style="width:12px;height:12px;fill:#fff;"></i> MOBILE AGENT</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#15803d; color:#166534;">📱 탈옥·Xcode 없이 내 아이폰·안드로이드를 AI가 직접 조작</span>
              <span class="platform-tag">GitHub Trending &amp; phone-harness.com</span>
              <span class="platform-tag">phone-harness / phone-harness</span>
            </div>

            <h2 class="article-headline">
              "탈옥도 앱 설치도 필요 없다" — 맥북 iPhone Mirroring과 Apple Vision OCR로 애플의 담장을 우아하게 넘은 모바일 에이전트 하네스 'phone-harness'
            </h2>

            <div class="article-subheadline">
              Claude Code·Codex·Hermes Agent·MCP 클라이언트가 동일한 Python 헬퍼(<code>find_text</code>·<code>tap</code>·<code>screen</code>)로 실물 iPhone(Mirroring+Vision OCR)·Android(adb 접근성 트리)·클라우드 폰까지 통합 제어하는 MIT 프레임워크 (+206스타/일, 누적 5,362스타)
            </div>
            <p class="article-snippet">
              웹 브라우저는 Playwright가 점령했지만, 정작 현대인의 핵심 금융·배달·모빌리티·메신저 서비스가 몰려 있는 스마트폰 앱은 여전히 AI 에이전트의 손이 닿지 않는 고립된 섬이었습니다. 오늘 하루 206스타를 추가하며 누적 5,362스타를 돌파한 <strong>phone-harness/phone-harness</strong>는 탈옥(Jailbreak)도, Xcode 빌드 서명도, 폰에 별도 에이전트 앱을 까는 수고도 없이 macOS의 기본 iPhone Mirroring 창과 Apple Vision OCR, Android adb를 단일 Python·MCP 규격으로 묶어 에이전트에게 실제 스마트폰 손가락을 달아주었습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "지금 내 위치에서 커피숍까지 Waymo 호출해 줘" — 아이폰을 직접 두드리는 터미널
            </h3>
            <p>
              터미널 창에서 코딩 에이전트에게 <code>phone-harness</code> 스킬을 쥐여주고 던진다. <em>"날씨 앱 열어서 예보 읽어주고, 노트 앱에 새 메모 남겨줘."</em> 잠시 후 맥북 한쪽에 떠 있던 <strong>iPhone Mirroring</strong> 창 위로 보이지 않는 손가락이 움직인다. 폰을 탈옥하지도, 개발자 계정을 묶어 WebDriverAgent를 서명 컴파일하지도 않았다. 폰에는 아무 앱도 새로 깔리지 않았다. 그저 에이전트가 화면의 <code>find_text("Weather") → (400, 468)</code> 좌표를 읽어 <code>tap(400, 468)</code>을 쏘고 화면 텍스트를 되읽었을 뿐이다.
            </p>
            <p>
              오늘 하루에만 <strong>+206스타(누적 5,362스타)</strong>를 모으며 GitHub 트렌딩에 오른 MIT 오픈소스 <strong>phone-harness/phone-harness</strong>는 데스크톱과 웹에 갇혀 있던 AI 에이전트의 활동 반경을 마침내 주머니 속 스마트폰 생태계로 확장했다. Claude Code, Codex, Grok Bot은 물론 <code>hermes plugins install</code>을 통한 Hermes Agent, OpenClaw, 그리고 원격 MCP(<code>https://mcp.phone-harness.com/mcp</code>)까지 한 번에 연결된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 애플의 폐쇄형 iOS API 장벽을 '정식 OS 기능 조합'으로 우회하다
            </h3>
            <p>
              그동안 iOS 기기를 외부에서 자동화하려면 Appium + Xcode + 유료 애플 개발자 인증서라는 악명 높은 지옥문을 통과하거나 기기를 탈옥해야 했다. <code>phone-harness</code>는 이 모든 마찰을 기발한 발상의 전환으로 삭제했다. 애플이 macOS 15+와 iOS 18+에 공식 탑재한 <strong>iPhone Mirroring</strong> 기능과 macOS 내장 <strong>Apple Vision OCR</strong> 프레임워크를 결합해, 폰 내부 OS를 건드리지 않고도 맥북 화면 레벨에서 완전한 시지각-입력 폐루프(Closed-loop)를 완성한 것이다.
            </p>

            <div class="editorial-quote">
              <p>
                "탈옥도, Xcode도, 폰에 설치할 앱도 제로(Zero). <strong>모든 기기가 동일한 Python 헬퍼(<code>open_app</code>·<code>tap_text</code>·<code>screen</code>) 뒤에 숨어 있어</strong>, 로컬 iPhone용으로 짠 스크립트가 Android와 클라우드 기기에서도 그대로 작동한다."
              </p>
              <small>— phone-harness/phone-harness 크로스 플랫폼 추상화 설계 (MIT)</small>
            </div>

            <p>
              심지어 에이전트가 작업 도중 스스로 반복적인 모바일 UI 조작 루틴을 <code>~/.phone-harness/agent-workspace</code>에 재사용 가능한 Python 헬퍼 함수로 축적하게 만들어, 실행할수록 점점 빠르고 정확해지는 '모바일 스킬 자가 진화'까지 구현했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 4대 백엔드 추상화와 Vision OCR / Accessibility Tree 이중 인식
            </h3>
            <p>
              <code>phone-harness</code>는 서로 전혀 다른 OS 제약을 가진 모바일 타깃을 단일 Python heredoc 실행기(<code>phone-harness &lt;&lt;'PY'</code>)로 평준화한다:
            </p>
            <ul>
              <li><strong>실물 iPhone (macOS 15+ iPhone Mirroring + Vision OCR):</strong> macOS Screen Recording 권한으로 iPhone Mirroring 윈도우 프레임을 캡처한 뒤, 클라우드 비전 API에 매번 고비용 이미지를 보내는 대신 <strong>로컬 Apple Vision OCR</strong>로 UI 텍스트와 바운딩 박스를 초고속 추출한다. 이후 Accessibility 권한을 통해 클릭·스와이프·타이핑 입력 이벤트를 직접 주입한다. (아이콘 등 레이블 없는 UI는 스크린샷+비전 모델 폴백).</li>
              <li><strong>실물 Android (USB / Wi-Fi adb + Accessibility Tree):</strong> macOS·Linux·Windows 어디서나 <code>adb</code>와 USB 디버깅만 켜면 안드로이드 접근성 트리(Accessibility Tree)에서 정밀한 UI 텍스트 노드를 긁어와 지연 없이 조작한다.</li>
              <li><strong>Phone Harness Cloud &amp; 원격 MCP:</strong> 책상 위에 실물 기기가 없거나 다중 기기(실물 SIM/2FA 포함 전용 iPhone 또는 온디맨드 Android)가 필요할 때는 동일한 헬퍼 코드가 각각 HTTPS와 원격 adb 터널을 타고 클라우드 기기를 제어한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">phone-harness 무탈옥 통합 모바일 에이전트 제어 아키텍처</span>
                <span class="schematic-badge">MIT License · iOS Mirroring + Android adb + MCP</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Unified Agent Interface</div>
                  <div class="schematic-desc">
                    Claude Code · Codex · Hermes · OpenClaw<br>
                    표준 헬퍼: <code>open_app / tap_text / screen</code><br>
                    <code>~/.phone-harness/agent-workspace</code> 자가 축적<br>
                    <code>https://mcp.phone-harness.com/mcp</code>
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. OS-Native Perception</div>
                  <div class="schematic-desc">
                    <strong>iOS:</strong> iPhone Mirroring 창 캡처 +<br>
                    로컬 <strong>Apple Vision OCR</strong> 텍스트 좌표화<br>
                    <strong>Android:</strong> adb + Accessibility Tree<br>
                    (비텍스트 아이콘만 비전 LLM 폴백)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Zero-Mod Execution</div>
                  <div class="schematic-desc">
                    macOS 입력 이벤트 / adb 셸 인젝션<br>
                    실물 iPhone · Android · Cloud 기기<br>
                    동일 코드 100% 호환 실행<br>
                    탈옥·Xcode 서명·앱 설치 완전 불필요
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">phone-harness 공식 웹사이트 &amp; 모바일 에이전트 셋업 인터페이스</span>
              </div>
              <img src="../assets/images/demo_phone_harness.png" alt="Phone Harness Official Website Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ phone-harness.com 공식 사이트 실화면: 실물 iPhone/Android 연결부터 클라우드 호스팅 폰, 코딩 에이전트 원클릭 온보딩 프롬프트까지 통합 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 &amp; 법적 분기점: Apple의 '폐쇄형 앱 정원'과 QA 디바이스 팜 시장의 재편
            </h3>
            <p>
              모바일 앱은 의도적으로 공개 웹 API나 DOM을 노출하지 않아 BrowserStack·Sauce Labs 같은 고가의 클라우드 QA 디바이스 팜과 비싼 RPA(로봇 프로세스 자동화) 업체들의 거대한 수익원이 되어왔다. 동시에 애플은 iOS 앱 내부 자동화와 서드파티 접근성 후킹을 OS 정책으로 철저히 봉쇄해 왔다.
            </p>
            <ul>
              <li><strong>OS 정식 기능의 합법적 조합 (Clean Orchestration):</strong> <code>phone-harness</code>는 iOS 커널 익스플로잇이나 사설 API 리버스 엔지니어링 없이, 오직 애플이 공식 배포한 macOS의 iPhone Mirroring·Vision OCR·Accessibility 권한만을 정공법으로 엮어냈기 때문에 탈옥으로 인한 보안 취약점이나 앱스토어 약관 리스크에서 자유롭다.</li>
              <li><strong>실물 기기 한계선의 투명한 명시:</strong> DRM 영상 블랙아웃, 잠금 해제/PIN 입력의 사용자 개입 필요성, Face ID·멀티터치 미지원 등 물리적 보안 경계를 명확히 존중하면서도 QA 테스트·앱 워크플로우 자동화의 90%를 즉시 해방시켰다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 에이전트가 브라우저를 넘어 '모바일 앱'의 문을 열었다
            </h3>
            <p>
              웹페이지가 없는 서비스는 존재해도, 모바일 앱만 존재하는 서비스는 넘쳐난다. 에이전트가 스마트폰 화면을 직접 읽고 두드릴 수 있게 된 순간, API가 없는 수백만 개의 레거시·모바일 전용 서비스가 전부 자동화 대상이 된다.
            </p>
            <p>
              탈옥도 Xcode도 없이 맥북 미러링 창 하나를 통해 애플의 가장 견고한 성벽을 걸어 들어간 phone-harness의 아이디어는, 가장 단순한 인터페이스 결합이 가장 거대한 플랫폼 해자를 무력화한다는 사실을 다시 한번 일깨워 준다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=phone-harness+AI+agent+control+iPhone+Android" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://phone-harness.com/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 / Cloud
              </a>
              <a href="https://github.com/phone-harness/phone-harness" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
