# -*- coding: utf-8 -*-
# Story 5: Cua Spaces

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] trycua/cua : 컴퓨터 유즈 2.0 오픈소스 멀티플레이어 OS -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_cua.jpg" alt="Cua Spaces Multiplayer Computer Use OS" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 74K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🖥️ 컴퓨터 유즈 2.0 · 멀티플레이어 OS</span>
              <span class="platform-tag">GitHub Trending Rust · Trendshift Top</span>
              <span class="platform-tag">trycua / cua</span>
            </div>
            
            <h2 class="article-headline">
              인간과 AI가 한 데스크톱에서 커서를 마주친다: 컴퓨터 유즈 2.0 오픈소스 멀티플레이어 OS 'Cua Spaces'
            </h2>

            <div class="article-subheadline">
              "Give AI agents computers they can use" — 애플 실리콘 및 리눅스 위에서 독립 가상 데스크톱(VM)을 즉시 생성… 로그인 세션 텔레포트와 크로스 OS Cua Driver로 시간당 수 달러를 요구하는 클라우드 샌드박스 벤더 종속 무력화 (+3만 스타)
            </div>
            <p class="article-snippet">
              AI 에이전트에게 완전한 GUI 컴퓨터를 쥐여주는 오픈소스 인프라. 로그인된 크롬 브라우저와 슬랙 세션을 가상 데스크톱으로 순간 이동(Teleport)시키고, 인간과 에이전트가 각자의 마우스 커서로 하나의 화면에서 실시간 협업하는 멀티플레이어 캔버스 제공.
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
              <i data-lucide="mouse-pointer-click"></i> 1. 원격 브라우저의 덫: 시간당 수 달러의 클라우드 통행세
            </h3>
            <p>
              '컴퓨터 유즈(Computer Use)'가 AI 업계의 최대 화두로 떠오른 이래, 수많은 개발자들은 심각한 현실적 장벽에 부딪혔다. 
              에이전트가 웹사이트를 클릭하고 앱을 조작하도록 만들기 위해, 개발자들은 Browserbase, E2B, Steel 같은 상용 클라우드 브라우저 샌드박스 스타트업들에게 시간당 수 달러에 달하는 가상머신 비용을 지불해야 했다. 
              클라우드 VM은 네트워크 지연(Latency)이 심해 에이전트의 마우스 조작이 버벅거렸고, 매번 번거로운 캡차(CAPTCHA) 인증과 2단계 로그인(2FA) 장벽에 걸려 에이전트가 멈춰 서기 일쑤였다.
            </p>
            <p>
              더 치명적인 문제는 <strong>'격리의 고립감'</strong>이었다. 
              클라우드 저편에서 혼자 돌아가는 에이전트가 폼을 잘못 채우거나 엉뚱한 결제 버튼을 누르려 할 때, 인간 개발자는 실시간으로 개입(Human-in-the-loop)할 수 없었다. 
              이 모든 병목을 단숨에 부수고, <strong>"내 맥북(Apple Silicon)이나 PC 하드웨어 위에서 0원의 비용으로 에이전트 전용 풀 데스크톱을 띄우고, 인간과 AI가 한 화면에서 마우스를 마주치며 일하는"</strong> 오픈소스 컴퓨터 유즈 운영체제 <strong>Cua Spaces(trycua/cua)</strong>가 폭발적인 화제를 모으며 깃허브 3만 스타 고지를 돌파했다.
            </p>

            <div class="editorial-quote">
              "AI에게 원격 브라우저 탭 하나를 던져주고 일하라고 시키는 것은, 신입 사원에게 좁은 열쇠구멍으로 서류를 밀어 넣는 것과 같습니다. 
              에이전트에게 필요한 것은 온전한 파일시스템, 프로세스, 다중 모니터를 갖춘 <strong>'진짜 컴퓨터'</strong>입니다. 
              <strong>Cua Spaces는 인간과 AI가 한 캔버스에서 각자의 커서를 쥐고 어깨를 맞대며 일하는 최초의 멀티플레이어 운영체제입니다.</strong>"
              <span class="quote-author">— 트라이쿠아(trycua) 코어 팀 선언문</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 세션 텔레포트와 멀티플레이어 커서 동기화
            </h3>
            <p>
              Cua가 전 세계 개발자들을 매료시킨 첫 번째 혁신은 <strong>'세션 텔레포트(Session Teleportation)'</strong>다. 
              새로운 VM을 띄울 때마다 구글, 슬랙, 깃허브 계정에 다시 로그인할 필요가 없다. 
              호스트 컴퓨터에서 로그인되어 있는 브라우저나 앱 창을 Cua Space로 드래그하면, 로그인 세션과 인증 쿠키가 암호화된 IPC 파이프를 통해 가상 데스크톱 내부로 즉시 순간 이동한다. 
              2FA 인증을 다시 풀 필요 없이 에이전트가 즉각 업무에 착수할 수 있다.
            </p>
            <p>
              두 번째 혁신은 <strong>'멀티플레이어 데스크톱(Multiplayer Desktop)'</strong>이다. 
              에이전트가 서류 양식을 작성하다가 중요한 법적 동의 체크박스나 최종 결제 승인 단계에 도달하면, 인간은 자신의 파란색 마우스 커서로 화면에 개입해 직접 클릭을 완료해 줄 수 있다. 
              에이전트는 인간의 조작을 인식하고 다음 단계를 이어간다. AI와 인간의 완벽한 탠덤(Tandem) 플레이가 로컬 0ms 지연 시간으로 실현된 것이다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="monitor" style="color:#0ea5e9;"></i> Cua Spaces: 로컬 컴퓨터 유즈 2.0 멀티플레이어 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">LOCAL COMPUTER-USE RUNTIME</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 로그인 세션 텔레포트</div>
                  <div class="step-title">Session Teleport</div>
                  <div class="step-desc">호스트에 로그인된 크롬, 슬랙 세션 쿠키를 격리 가상 데스크톱으로 무중단 이관하여 2FA 재인증 우회.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 초경량 로컬 VM 기동</div>
                  <div class="step-title">Lume (Apple Silicon VM)</div>
                  <div class="step-desc">애플 실리콘 가상화 프레임워크(VZ) 기반의 Lume 엔진으로 1.2초 만에 완전한 로컬 macOS/리눅스 VM 생성.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 크로스 OS 드라이버</div>
                  <div class="step-title">Cua Driver & Telemetry</div>
                  <div class="step-desc">macOS, Windows, Linux 전반에서 UI 트리를 0ms 계측하고 픽셀과 마우스 좌표를 고속 동기화하는 러스트 드라이버.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 멀티플레이어 커서</div>
                  <div class="step-title">Dual Cursor Synchronization</div>
                  <div class="step-desc">인간 커서(블루)와 AI 에이전트 커서(네온)가 동일 캔버스에서 충돌 없이 협동 조작하는 cua-spacesd 프로토콜.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 특화 결정 모델</div>
                  <div class="step-title">CUA-S1 Small Model</div>
                  <div class="step-desc">거대 LLM을 매번 호출하지 않고 초경량 CUA-S1 모델이 클릭·스크롤 결정을 밀리초 단위로 초고속 오프로딩.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘 해부: Lume 가상화 엔진과 초경량 CUA-S1 의사결정 모델
            </h3>
            <p>
              Cua의 기술적 완성도를 뒷받침하는 핵심 무기는 <strong>'Lume 가상화 하이퍼바이저'</strong>와 <strong>'CUA-S1 특화 모델'</strong>의 하이브리드 조합이다:
            </p>
            <p>
              첫째, <strong>애플 실리콘 네이티브 가상화 엔진 Lume</strong>이다. 
              무거운 버추얼박스(VirtualBox)나 QEMU 대신 macOS의 내장 <code>Virtualization.framework</code>를 극한까지 튜닝하여, M1/M2/M3 맥북에서 1GB 미만의 메모리 오버헤드로 독립된 macOS Tahoe 가상 데스크톱을 1.2초 만에 인스턴스화한다. 
              에이전트는 VM 내부의 <code>cua-spacesd</code> 데몬을 통해 파일 시스템, 터미널, GUI 디스플레이 프레임버퍼에 완벽하게 접근한다.
            </p>
            <p>
              둘째, <strong>컴퓨터 조작 전용 경량 모델 CUA-S1</strong>이다. 
              마우스를 어디로 움직이고 어느 좌표를 클릭할지 결정하기 위해 매번 100만 토큰짜리 비싼 거대 모델을 부르면 비용과 지연 시간이 감당되지 않는다. 
              Cua는 컴퓨터 GUI 조작에만 특화된 소형 비전 모델(CUA-S1)을 제공하여, 로컬 GPU에서 30ms 만에 정확한 버튼 바운딩 박스를 찾아내 클릭을 실행한다. 
              고차원 추론은 거대 모델이, 세부 조작은 초경량 모델이 맡는 최적의 2단계 아키텍처다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_cua_desktop.jpg" alt="Cua Spaces 멀티플레이어 가상 데스크톱 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>Cua Spaces 멀티플레이어 데스크톱 캡처:</strong> 맥OS 로컬 머신 위에서 독립 구동되는 가상 데스크톱 화면. 로그인된 앱들이 세션 텔레포트로 즉시 이관되어 있고, 인간과 AI 에이전트가 각자의 커서로 동일한 화면에서 실시간 협업 작업을 수행하는 모습.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="briefcase"></i> 4. 비즈니스 해자: 클라우드 VM 샌드박스 벤더의 종말
            </h3>
            <p>
              Cua의 등장은 클라우드 가상 브라우저 인프라를 독점하려던 수많은 B2B SaaS 스타트업들에게 사형선고나 다름없다. 
              개발자들은 더 이상 에이전트 하나를 돌리기 위해 한 달에 수백만 원의 클라우드 인프라 청구서를 받아 들 필요가 없다. 
              내 책상 위의 맥북 프로 한 대가 10대의 가상 에이전트 워크스테이션으로 변모하기 때문이다. 
              컴퓨터 유즈의 하부 인프라가 오픈소스로 완전히 자립화되면서, 에이전트 서비스 개발의 원가 구조는 10분의 1 수준으로 폭락하게 될 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="terminal"></i> 5. 키커: 한 화면에서 마주 본 인간과 기계의 협주
            </h3>
            <p>
              인공지능과의 협업은 원격 서버의 블랙박스에 질문을 던지고 기다리는 일방통행이 아니다. 
              Cua Spaces가 구현한 멀티플레이어 데스크톱은, <strong>인간의 직관적인 손끝과 인공지능의 지칠 줄 모르는 연산력이 단일한 디지털 공간에서 서로의 커서를 바라보며 호흡하는 가장 아름다운 공존의 풍경</strong>을 열어젖혔다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://cua.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 웹 데모 바로 체험
              </a>
              <a href="https://www.youtube.com/results?search_query=trycua+cua+spaces+computer+use" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/trycua/cua" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 5 ready.")
