# -*- coding: utf-8 -*-
# Story 2: LadybirdBrowser/ladybird

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] LadybirdBrowser/ladybird                         -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ladybird.jpg" alt="Ladybird Independent Browser Engine Alpha Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="globe" style="width:12px;height:12px;fill:#fff;"></i> ALPHA MILESTONE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fee2e2; border-color:#dc2626; color:#991b1b;">🐞 크로미움·웹킷 포크 없는 완전 독립 엔진 첫 알파 출시 · HN 1,179점</span>
              <span class="platform-tag">Hacker News #1 Tech &amp; ladybird.org</span>
              <span class="platform-tag">LadybirdBrowser / ladybird</span>
            </div>

            <h2 class="article-headline">
              "크로미움도 웹킷도 베끼지 않았다" — 제로에서 다시 짠 독립 웹 브라우저 'Ladybird', 마침내 첫 알파(Alpha) 공개
            </h2>

            <div class="article-subheadline">
              2026년 11월 23일 macOS·Linux용 자동 업데이트 알파(2026.47.7) 공식 배포 — LibWeb·LibJS·LibWasm 기반 사이트 격리 멀티프로세스 아키텍처와 Rust 코드 비중 1위 전환, WebDriver 및 Firefox DevTools 프로토콜 지원 (★67,673, BSD-2-Clause)
            </div>
            <p class="article-snippet">
              오늘 웹 생태계의 가장 거대한 이정표 중 하나가 세워졌습니다. 크롬(Blink/V8)과 사파리(WebKit)라는 양대 거대 엔진의 포크에 기대지 않고 웹 표준(W3C/WHATWG) 명세서만 보고 맨바닥부터 엔진을 새로 작성해 온 독립 브라우저 프로젝트 <strong>Ladybird</strong>(누적 <strong>67,673스타</strong>)가 2026년 11월 23일 공식 <strong>첫 알파 릴리스(2026.47.7)</strong>를 발표했습니다. 그동안 소스코드에서 직접 빌드해야만 맛볼 수 있던 이 독립 엔진은 이제 macOS와 Linux용 자동 업데이트 바이너리로 내려받을 수 있으며, 내부 코드베이스에서는 <strong>Rust가 C++를 제치고 최대 비중 언어</strong>로 올라서는 구조적 대전환까지 이뤄냈습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "더 이상 소스에서 컴파일하지 않아도 된다" — 6만 7천 스타의 기다림이 끝난 날
            </h3>
            <p>
              "오랫동안 이 글을 쓰기를 고대해 왔습니다. :^) Ladybird가 이제 알파(Alpha)입니다." 현지 시각 2026년 11월 23일, 안드레아스 클링(Andreas Kling)이 <code>ladybird.org</code>에 짧은 공지를 올리자 해커뉴스에서는 순식간에 <strong>1,179개의 추천과 291개의 댓글</strong>이 폭주했다. 몇 년간 수많은 개발자가 "대체 언제쯤 내 맥북과 리눅스에 설치 파일 하나로 깔아서 써볼 수 있느냐"고 묻던 그 순간이 마침내 릴리스 태그 <code>2026.47.7 Ladybird alpha</code>와 함께 도착한 것이다.
            </p>
            <p>
              시중에 '프라이버시 브라우저', 'AI 브라우저', '차세대 브라우저'라는 간판을 달고 나오는 제품은 넘쳐난다. 하지만 껍데기를 열어보면 99%가 구글의 <strong>Chromium(Blink + V8)</strong>이나 애플의 <strong>WebKit</strong>, 아니면 모질라의 Gecko를 그대로 감싼 변종들이다. 웹 표준을 해석하는 엔진 자체를 포크 없이 백지에서 새로 짓는 일은 수천만 줄의 명세와 수십 년간 쌓인 엣지 케이스 때문에 "현대 소프트웨어 공학에서 불가능에 가까운 영역"으로 치부돼 왔다. Ladybird는 바로 그 불가능에 정면으로 도전해 첫 번째 대중 배포 문턱을 넘었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "보안 해커들이 우리를 뚫어주길 바란다 — 그것이 새 엔진이 단단해지는 유일한 길"
            </h3>
            <p>
              이번 알파 출시가 갖는 결정적 의미는 '완성도 100%' 선언이 아니라 <strong>실제 야생의 웹과 자동 업데이트 롤링 채널로의 진입</strong>이다. 클링은 알파 공지에서 약점을 숨기지 않았다. 일부 웹사이트가 깨지고 충돌이 날 수 있으며, 보안 역시 오늘 당장 완벽을 약속할 수 없다고 솔직히 밝혔다. 대신 브라우저 내부에 원클릭 사이트 깨짐 신고 기능과 열람 가능한 크래시 리포트를 탑재하고, 보안 연구자들을 향해 "제발 우리를 해킹(pwn)해서 어떻게 뚫었는지 알려달라"고 공개 초대장을 보냈다.
            </p>

            <div class="editorial-quote">
              <p>
                "Ladybird는 완전히 새로운 엔진을 탑재한 브라우저이며, 포크(Fork)가 아니라 바닥부터 직접 구축했습니다. <strong>자동 업데이트가 적용되는 롤링 알파 채널을 통해 이제 누구든 소스 빌드 없이 Ladybird의 진화를 매일 직접 체험할 수 있습니다.</strong>"
              </p>
              <small>— Andreas Kling, Ladybird is now in alpha (2026-11-23 공식 발표)</small>
            </div>

            <p>
              특히 주목할 점은 웹 개발자 생태계와의 접점이다. 이번 알파 빌드는 이미 자동화 테스트를 위한 <strong>WebDriver</strong>와 <strong>Firefox DevTools 프로토콜</strong>을 기본 지원해, 프론트엔드 엔지니어들이 크롬과 사파리 외에 제3의 순수 표준 엔진에서 자신의 웹사이트 호환성을 검증할 수 있는 길을 열었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Rust 주도 엔진 재편과 10중 샌드박스 멀티프로세스 해부
            </h3>
            <p>
              Ladybird 저장소의 언어 통계와 프로세스 설계 문서(<code>ProcessArchitecture.md</code>)를 들여다보면, 과거 SerenityOS의 취미 프로젝트에서 현대적 보안 우선 브라우저로 탈바꿈한 아키텍처의 실체가 선명히 드러난다:
            </p>
            <ul>
              <li><strong>Rust가 C++를 추월한 메모리 안전 엔진 전환:</strong> 저장소 언어 분포 기준 <strong>Rust(4,799만 바이트)</strong>가 <strong>C++(3,898만 바이트)</strong>을 앞질러 최대 비중 언어로 자리 잡았다. <code>LibWeb</code>(렌더링), <code>LibJS</code>(자바스크립트), <code>LibWasm</code>(웹어셈블리), <code>LibCrypto/LibTLS</code>, <code>LibGfx</code> 등 핵심 파서와 엔진 계층이 메모리 안전성과 현대적 동시성 중심으로 빠르게 재구성되고 있다.</li>
              <li><strong>철저한 사이트 격리(Site Isolation) 및 헬퍼 프로세스 분리:</strong> 메인 <code>UI</code> 프로세스 아래 <code>Hub</code>가 모든 샌드박스 프로세스를 기동해 직접 연결한다. 서로 다른 사이트 문서는 완전히 분리된 <code>WebContent</code> 렌더러 프로세스에서 돌며, 신뢰할 수 없는 외부 입력을 다루는 <code>RequestServer</code>(네트워크)와 <code>ImageDecoder</code>(이미지 디코딩) 역시 사이트·세션별로 격리된 별도 프로세스로 쪼개져 파서 취약점이 발생해도 피해 반경을 극소화한다.</li>
              <li><strong>미디어·WebRTC 파이프라인 분리:</strong> 각 렌더러마다 <code>MediaServer</code>, <code>AudioServer</code>, <code>VideoDecoderServer</code>, <code>WebRTCClient</code>를 독립 프로세스로 배치해 영상·음성 코덱 버그가 브라우저 전체를 무너뜨리지 못하게 방어한다(macOS에서는 고아 프로세스 방지를 위해 <code>ProcessReaper</code>까지 둔다).</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Ladybird 멀티프로세스 샌드박스 &amp; 독립 웹 엔진(LibWeb/LibJS) 구조</span>
                <span class="schematic-badge">Rust + C++ · BSD-2-Clause · 67.6k★ · Alpha 2026.47.7</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Control &amp; Process Broker</div>
                  <div class="schematic-desc">
                    <strong>UI</strong> 프로세스 (윈도우·롤링 업데이터)<br>
                    <strong>Hub</strong> 브로커 (샌드박스 프로세스 스폰)<br>
                    <strong>Compositor</strong> 독립 화면 합성<br>
                    WebDriver · Firefox DevTools 프로토콜
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Novel Web Engine (No Fork)</div>
                  <div class="schematic-desc">
                    <strong>LibWeb</strong> HTML/CSS 레이아웃·DOM<br>
                    <strong>LibJS</strong> · <strong>LibWasm</strong> 독립 스크립트 실행<br>
                    사이트별 격리 <strong>WebContent</strong> 렌더러<br>
                    Rust 주도 메모리 안전 계층 확장
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Untrusted Parser Isolation</div>
                  <div class="schematic-desc">
                    사이트별 <strong>RequestServer</strong> (LibHTTP/TLS)<br>
                    사이트별 <strong>ImageDecoder</strong> (LibGfx)<br>
                    <strong>MediaServer</strong>·<strong>VideoDecoderServer</strong> 분리<br>
                    파서 크래시 시 단일 탭/헬퍼만 재시작
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">ladybird.org 알파 공식 발표 실화면 — macOS·Linux 롤링 알파 채널 개시</span>
              </div>
              <img src="../assets/images/demo_ladybird.png" alt="Ladybird Browser Alpha Announcement Website" class="showcase-img">
              <p class="showcase-caption">
                ▲ ladybird.org/posts/alpha/ 실화면: 2026년 11월 23일 안드레아스 클링이 공개한 Ladybird Alpha 공식 발표문 및 macOS·Linux 바이너리 다운로드, 자동 업데이트 롤링 채널 안내.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업 패권: 구글 Chromium 독점을 깰 '제3의 엔진'이 필요한 이유
            </h3>
            <p>
              오늘날 지구상 웹 트래픽의 압도적 다수는 구글의 Blink/V8 엔진(Chrome, Edge, Brave, Opera, Arc, Electron)과 애플의 WebKit(Safari, iOS 전체 브라우저) 위에서 돌아간다. 파이어폭스(Gecko)의 점유율이 하락하고 구글 크롬 반독점 소송에서 브라우저 분사·검색 기본값 계약 해제가 거론되는 와중에도, 기술적으로 가장 아픈 지점은 <strong>"구글과 애플을 대체할 완전히 새로운 독립 브라우저 엔진이 시장에 없다"</strong>는 사실이었다.
            </p>
            <ul>
              <li><strong>빅테크 광고·표준 독점 견제:</strong> 단일 엔진(Chromium)이 웹 표준을 독식하면, 광고 차단 API(Manifest V3)나 프라이버시 샌드박스, 신규 웹 API의 방향을 사실상 한 기업이 결정하게 된다. BSD-2-Clause 라이선스의 비영리 재단(Ladybird Browser Initiative)이 후원금과 기부만으로 엔진을 알파까지 밀어 올렸다는 점은 오픈 웹 거버넌스 측면에서 상징성이 크다.</li>
              <li><strong>수익 모델과 지속 가능성 시험대:</strong> 광고 네트워크나 데이터 브로커링을 거부하는 순수 비영리 모델이 향후 수년간 수억 명 규모의 보안 패치와 웹 호환성 유지보수 비용을 어떻게 감당할 것인가가 알파 이후 베타·1.0 여정의 핵심 관전 포인트다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 웹이 다시 '누구의 것도 아닌 공간'이 되려면 엔진부터 자유로워야 한다
            </h3>
            <p>
              알파 버전의 Ladybird는 아직 투박하고, 종종 뻗으며, 수많은 웹사이트가 낯설게 보일 것이다. 하지만 1990년대 넷스케이프와 모질라가 그랬듯, 모든 거대한 브라우저 혁명은 소스 빌드의 벽을 허물고 일반 개발자 노트북에 첫 번째 실행 아이콘이 떨어지는 날 비로소 시작된다.
            </p>
            <p>
              오늘 다운로드 폴더에 떨어진 작은 무당벌레 아이콘 하나는, 웹의 미래를 구글과 애플의 손에만 맡기지 않겠다는 6만 7천 명 개발자들의 조용하지만 단호한 선언이다.
            </p>

            <div class="project-links">
              <a href="https://ladybird.org/posts/alpha/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> Ladybird Alpha 공식 페이지
              </a>
              <a href="https://www.youtube.com/results?search_query=Ladybird+browser+alpha+independent+engine" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/LadybirdBrowser/ladybird" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
