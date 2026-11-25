# -*- coding: utf-8 -*-
# Story 3: erkamyaman/rea-games (Clean-room Game Reverse Engineering & Frame-by-Frame Verification)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] erkamyaman/rea-games : Clean-Room Game Rebuilder -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_reagames.jpg" alt="rea-games Clean-Room Game Reverse Engineering and Frame-by-Frame Verification Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="gamepad-2" style="width:12px;height:12px;"></i> CLEAN-ROOM REBUILD</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🕹️ 667,561 입력 프레임 일치 검증 · GAME.md 공개 스펙 · Web/Rust/Godot 이식</span>
              <span class="platform-tag">GitHub New Rocket &amp; Game Dev</span>
              <span class="platform-tag">erkamyaman / rea-games</span>
            </div>

            <h2 class="article-headline">
              "원본 게임은 건드리지 않고, 프레임 단위 동작만 100% 똑같이 재건한다" — 'rea-games'
            </h2>

            <div class="article-subheadline">
              원본 실행 환경의 시계와 난수(Math.random)를 가로채 66만 7천 번의 입력·상태 테이프를 녹화하고, 개방형 행위 명세서 GAME.md를 추출해 Web·Rust(Bevy)·Godot으로 클린룸 재구현한 뒤 첫 불일치 프레임까지 검출 (★181 · MIT)
            </div>
            <p class="article-snippet">
              기존 소프트웨어를 AI 에이전트로 역공학해 <code>Rust</code> 등으로 다시 짜는 <code>rea</code>·<code>rust-anything</code> 계열 계보가 이번에는 게임 엔진을 정조준했습니다. 오늘 공개 16시간 만에 ★181을 돌파한 <strong>erkamyaman/rea-games</strong>는 크롬 공룡 게임(Dino, <strong>63,000프레임</strong>), 2048(24,044입력), Canvas Bird(드ロー콜 1,140스텝 일치), 테트리스 등 6종의 게임을 가짜 시계·시드 난수 하네스 위에서 <strong>총 667,561개 입력 테이프</strong>로 녹화한 뒤, 오픈 포맷 <code>GAME.md</code> 행위 명세만으로 Web·Rust(Bevy)·Godot 버전을 새로 빌드해 원본과 프레임 단위로 100% 똑같이 움직임을 입증합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 1,800프레임, 23개의 선인장, 그리고 정확히 같은 프레임의 추락
            </h3>
            <p>
              게임을 다른 엔진이나 언어로 이식해 본 개발자라면 누구나 아는 사실이 있다. 겉보기에 똑같이 흉내 내기는 쉬워도, 막상 플레이해 보면 점프가 반 프레임 늦거나 충돌 판정(Hitbox)이 1픽셀 어긋나서 "원작의 손맛"이 완전히 죽어버린다는 것이다. 특히 난수가 개입하고 <code>requestAnimationFrame</code>과 DOM/Canvas 타이밍이 뒤엉킨 게임은 재구현이 원작과 똑같이 작동하는지 증명할 방법조차 마땅치 않았다.
            </p>
            <p>
              터키 개발자 에르캄 야만(erKam Yaman)이 공개한 <code>rea-games</code>의 데모 GIF를 보면 등골이 서늘해진다. 왼쪽 창에는 크롬 오프라인 공룡 게임(Dino) 원본이, 오른쪽 창에는 새로 짠 리빌드가 나란히 달린다. 1,800스텝, 23개의 장애물, 익룡 한 마리까지 지나간 뒤 마지막 충돌 순간에 이르기까지, 양쪽의 점수·공룡 높이·선인장 좌표는 소수점 한 자리 차이도 없이 완벽하게 겹쳐 떨어진다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "소스코드를 베끼지 않고, 행위 명세(`GAME.md`)로 동등성을 증명하다"
            </h3>
            <p>
              <code>rea-games</code>는 어도비 포토샵 역공학으로 화제를 모았던 <code>morluto/rea</code>와 <code>rust-anything</code> 패밀리의 최신 진화형이다. 핵심 발상은 <strong>소스코드 변환(Transpiling)이 아니라 결정론적 행위 기록(Tape Recording)과 개방형 명세(<code>GAME.md</code>)</strong>다. 원본 코드는 단 한 줄도 수정하지 않은 채 외부 하네스에서 시간과 난수만 주입해 입출력 궤적(Trace)을 뽑고, AI 에이전트(Claude Code·Codex)가 이를 해독해 <code>GAME.md</code>를 작성하면, 이후 어떤 언어·어떤 아트 애셋으로 새로 짜더라도 검증기(<code>rea-games verify</code>)가 첫 번째로 틀어진 프레임과 원인을 정확히 짚어낸다.
            </p>

            <div class="editorial-quote">
              <p>
                "원본의 시계(performance.now, Date.now)와 Math.random을 바깥에서 교체해 모든 난수 소비 내역을 테이프(Tape)로 저장한다. <strong>이후 GAME.md 명세만으로 Web, Rust(Bevy), Godot 등 어떤 엔진으로 다시 짜든, 667,561개 입력 전 구간에서 동일하게 동작하거나 첫 불일치 지점을 즉시 폭로한다.</strong>"
              </p>
              <small>— erkamyaman/rea-games 아키텍처 및 Chrome Dino GAME.md 명세서</small>
            </div>

            <p>
              이미 2048(19개 케이스·24,044입력), Dino(29개 케이스·63,000프레임), Canvas Bird(30개 케이스·68,409프레임), Blocks/테트리스(36개 케이스·104,208프레임)는 웹뿐만 아니라 <strong>Godot과 Rust(Bevy) 네이티브 포트까지 전 케이스 검증을 통과</strong>했으며, Bricks(209,600스텝)와 Paddles(198,300스텝) 역시 GitHub Pages 웹 데모에서 직접 플레이할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 가짜 시계·난수 테이프·드로우콜 스냅샷의 3단 검증
            </h3>
            <p>
              비공개 상태를 숨긴 게임까지 프레임 단위로 뜯어내어 엔진을 갈아 끼우는 <code>rea-games</code>의 공학적 메커니즘은 다음 세 단계로 동작한다:
            </p>
            <ul>
              <li><strong>결정론적 하네스 &amp; 테이프 녹화 (<code>driver.mjs</code>):</strong> Playwright Chromium에서 원본 페이지를 열되, 페이지 스크립트가 실행되기 직전에 <code>performance.now</code>·<code>Date.now</code>·<code>requestAnimationFrame</code>·<code>Math.random</code>·<code>AudioContext</code>를 가로챈다. 가짜 시계는 오직 테스트 러너가 <code>step({dt, jump, duck...})</code>을 호출할 때만 전진하며, 게임이 소비한 모든 난수 시퀀스(<code>tape</code>)와 프레임 후 상태를 <code>cases/*.json</code>에 기록한다.</li>
              <li><strong>행위 명세 포맷 <code>GAME.md</code> 추출:</strong> 녹화된 궤적과 프레임 순서를 분석해 한 프레임 안의 연산 순서(예: 시계 전진 → keydown/keyup 순서 → rAF 콜백 실행), 물리 상수, 심지어 원작에 숨어 있는 기벽(Quirk)과 버그까지 명시한 <code>GAME.md</code>를 생성한다.</li>
              <li><strong>크로스 엔진 <code>stdin/stdout</code> 검증기와 드로우콜 감시:</strong> 새로 만든 Web·Rust(Bevy)·Godot 포트는 <code>cases/*.json</code>을 표준 입력(<code>stdin</code>)으로 받아 <code>{trace, tapeUsed}</code> JSON을 출력한다. 만약 <code>Canvas Bird</code>처럼 원작 게임 내부 변수가 클로저로 완전히 은닉돼 상태 읽기조차 불가능한 경우, <code>CanvasRenderingContext2D</code>의 드로우콜(<code>draw calls</code>) 전체를 가로채 1,140스텝의 렌더링 명령 자체가 일치하는지 비교한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">rea-games 클린룸 역공학 &amp; 크로스 엔진 검증 파이프라인</span>
                <span class="schematic-badge">667,561 Recorded Inputs · GAME.md Spec · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Deterministic Harness</div>
                  <div class="schematic-desc">
                    원본 무수정 실행 + Playwright 후킹<br>
                    가짜 시계(<code>now += dt</code>) &amp; rAF 큐 제어<br>
                    <code>Math.random</code> 시드 테이프(<code>tape</code>) 녹화<br>
                    상태 또는 Canvas 드로우콜 <code>cases/*.json</code> 저장
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. GAME.md Behavior Spec</div>
                  <div class="schematic-desc">
                    프레임 내 연산 순서·물리 상수 명문화<br>
                    원작의 미세한 버그·예외 규칙까지 기술<br>
                    구현 코드와 분리된 순수 행위 명세 포맷<br>
                    AI 에이전트(Claude/Codex)로 타 엔진 이식
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Cross-Engine Verifier</div>
                  <div class="schematic-desc">
                    Web(JS) / Rust(Bevy) / Godot 포트 빌드<br>
                    <code>stdin</code> 케이스 재생 → <code>{trace, tapeUsed}</code><br>
                    독창적 자체 아트로 100% 클린룸 렌더링<br>
                    1프레임·1난수라도 틀리면 즉시 차이점 보고
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">rea-games 라이브 웹 데모 실화면 — 클린룸 재구현 6종 아케이드 게임 및 검증 현황</span>
              </div>
              <img src="../assets/images/demo_reagames.png" alt="rea-games Live Web Demo Playable Clean-Room Rebuilds" class="showcase-img">
              <p class="showcase-caption">
                ▲ erkamyaman.github.io/rea-games/ 실화면: 자체 아트로 새로 그려냈지만 667,561회 입력 검증을 100% 통과한 2048·Dino·Canvas Bird·Blocks·Bricks·Paddles 플레이어블 웹 포트.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적 분기점: 게임 보존과 '행위 명세 기반 클린룸 재구현'의 합법적 방패
            </h3>
            <p>
              게임 산업에서 에뮬레이션과 리마스터는 늘 저작권 분쟁의 화약고였다. 원본 바이너리나 스프라이트 아트를 한 픽셀이라도 뜯어 쓰면 저작권 침해로 즉각 철퇴를 맞지만, <code>rea-games</code>가 보여주는 방법론은 전통적인 <strong>'클린룸(Clean-room) 설계'를 AI 시대의 자동화 검증 도구로 격상</strong>시켰다.
            </p>
            <ul>
              <li><strong>저작물 비복제 원칙과 <em>Sega v. Accolade</em> 전통:</strong> 재구현된 포트는 원본 소스코드, 이미지, 사운드를 전혀 포함하지 않으며(오히려 새로운 자체 아트로 그린다), 오직 블랙박스 입출력 관찰과 행위 규칙 명세(<code>GAME.md</code>)로부터 작성된다. 게임 규칙과 수학적 메커니즘 자체는 저작권 보호 대상인 '표현'이 아니라 '아이디어/시스템'에 속하므로, 레거시 웹·모바일 게임을 현대 엔진(Rust/Godot)으로 보존하거나 이식하는 데 강력한 법적 안전지대를 형성한다.</li>
              <li><strong>AI 코딩 시대의 '테스트 오라클' 혁명:</strong> 그동안 AI에게 "고전 게임을 Rust로 다시 짜줘"라고 시키면 겉만 그럴듯한 버그투성이 코드를 내놓기 일쑤였다. <code>rea-games</code>는 6만 프레임짜리 결정론적 테이프를 AI의 채점기(Oracle)로 물려, 인간의 감에 의존하던 게임 이식을 엄격한 회귀 테스트 공학으로 바꿔놓았다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 코드가 썩어 사라져도, 게임의 '영혼'은 명세서로 남는다
            </h3>
            <p>
              플래시(Flash)가 죽고 수많은 오래된 웹·모바일 게임이 런타임과 함께 증발해 버렸을 때, 우리가 잃어버린 것은 특정 언어의 문법이 아니라 그 게임만의 미묘한 물리 감각과 타이밍이었다.
            </p>
            <p>
              <code>GAME.md</code>와 66만 번의 입력 테이프는 그 무형의 감각을 시대를 초월해 복제 가능한 청사진으로 박제한다. 오늘 작은 아케이드 게임 6종에서 시작된 이 실험이 내일 어느 거대한 레거시 소프트웨어의 세대교체를 열게 될지, 개발자들의 시선이 모이고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=rea-games+reverse+engineer+game+GAME+md" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://erkamyaman.github.io/rea-games/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 웹 데모 바로 플레이
              </a>
              <a href="https://github.com/erkamyaman/rea-games" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
