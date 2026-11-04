# -*- coding: utf-8 -*-
# Story 5: jub0t/Concat

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [CARD 5] jub0t/Concat : 캡컷(CapCut)을 대체하는 오픈소스 Rust 비디오 에디터 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_concat.jpg" alt="Concat Open-Source Video Editor" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="video" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #5</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 262 스타 폭발 · 바이트댄스 캡컷 유료화 대항마</span>
              <span class="platform-tag">GitHub Trending Rust</span>
              <span class="platform-tag">jub0t / Concat</span>
            </div>
            
            <h2 class="article-headline">
              바이트댄스 캡컷의 독점과 구독료 장사에 던진 일격: Rust로 깎아낸 100% 무료 로컬 비디오 에디터 'Concat'
            </h2>

            <div class="article-subheadline">
              "무료로 사용자를 모은 뒤 기본 기능마저 프로 구독으로 잠가버리는 인질극에 마침표를 찍다" — 전 세계 숏폼 크리에이터와 오픈소스 진영, 바이트댄스 캡컷(CapCut)을 완벽 대체하는 로컬 퍼스트 비디오 편집기 'Concat' 공개… Rust + Tauri 기반의 초경량 네이티브 엔진, 제로 클라우드 프라이버시, 그리고 AI 에이전트가 직접 영상 컷편집을 조작하는 MCP 서버 내장으로 크리에이터 혁명을 촉발하다
            </div>
            <p class="article-snippet">
              워터마크 제로, 월 구독료 제로, 데이터 수집 제로. FFmpeg 하드웨어 가속 타임라인과 JSON-RPC API를 탑재하여 Claude Code나 커스텀 AI 에이전트가 직접 자막 생성, 컷편집, 키프레임 이펙트를 프로그래밍 방식으로 일괄 렌더링하는 차세대 영상 워크벤치.
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
              <i data-lucide="flame"></i> 1. 리드: 전 세계 유튜버·틱톡커들의 뒤통수를 친 캡컷(CapCut)의 변심
            </h3>
            <p>
              지난 수년간 틱톡의 모회사 바이트댄스(ByteDance)가 배포한 <strong>캡컷(CapCut)</strong>은 전 세계 수억 명의 영상 크리에이터를 사로잡았다. 
              간편한 타임라인, 매력적인 트랜지션, 원클릭 자동 자막(Auto Captions) 기능은 프리미어 프로나 파이널 컷의 복잡한 진입 장벽을 완전히 허물며 숏폼 콘텐츠의 표준 편집기로 군림했다.
            </p>
            <p>
              하지만 독점의 달콤함이 정점에 달하자, 바이트댄스는 본색을 드러냈다. 
              기존에 무료로 제공되던 기본 기능들을 하나둘씩 <strong>'CapCut Pro' 유료 구독(연간 수십만 원) 뒤로 감추기 시작</strong>했고, 
              심지어 텍스트 자동 자막 생성이나 단순 노이즈 제거 기능마저 결제 없이는 워터마크를 찍어 내보내기를 차단했다. 
              여기에 민감한 개인 영상과 프로젝트 데이터가 중국 클라우드 서버로 실시간 전송된다는 보안·프라이버시 불안까지 겹치며 크리에이터 커뮤니티의 분노는 임계점을 넘어섰다.
            </p>
            <p>
              이 탐욕의 구독 모델에 통쾌한 일격을 가하기 위해 오픈소스 엔지니어들이 뭉쳤다. 
              개발자 <strong>jub0t</strong>가 주도하는 100% 무료 로컬 퍼스트 비디오 에디터 <strong>Concat(jub0t/Concat)</strong>이 공개되며 깃허브 Rust 및 Trendshift 트렌딩 1위에 등극했다.
            </p>

            <div class="editorial-quote danger">
              "캡컷은 훌륭한 도구였지만, 이제는 사용자를 인질로 잡고 매달 결제를 강요하는 전형적인 빅테크 독점 소프트웨어로 변질되었습니다. 
              <strong>Concat의 약속은 명확합니다. 영원히 완전 무료이며(AGPL-3.0), 내 컴퓨터에서만 로컬로 돌며, 단 1바이트의 개인 영상도 외부 서버로 전송하지 않습니다. 크리에이티브 도구는 인질이 되어서는 안 됩니다.</strong>"
              <span class="quote-author">— Concat 창시자 jub0t 릴리즈 선언문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: Rust + Tauri 네이티브 엔진과 AI 에이전트 전용 MCP 서버
            </h3>
            <p>
              <code>Concat</code>은 무거운 일렉트론(Electron) 래퍼가 아니다. 
              운영체제의 네이티브 웹뷰와 초저지연 시스템 언어인 <strong>Rust(러스트)</strong>를 결합한 <code>Tauri</code> 프레임워크로 제작되어, 
              앱 실행 파일 용량이 30MB 안팎에 불과하며 메모리 점유율은 상용 툴의 1/5 수준이다.
            </p>
            <p>
              더욱 혁명적인 점은 <strong>인공지능 에이전트와의 공생 설계</strong>다. 
              Concat은 앱 내부에 자체 <strong>MCP(Model Context Protocol) 서버</strong>를 내장하고 있어, 
              인간이 마우스로 타임라인을 편집할 수 있을 뿐만 아니라 <strong>Claude Code나 AI 에이전트가 명령줄(`concat --mcp`)을 통해 프로젝트 생성, 클립 자르기, 음성 파형 분석, 자막 배치, 색보정 키프레임을 직접 제어</strong>할 수 있다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> Concat: Rust 기반 로컬 영상 엔진과 듀얼 컨트롤(인간 GUI + AI MCP) 아키텍처
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">코어 엔진</span>
                  <strong>Rust + FFmpeg GPU 가속</strong>
                  <div class="schematic-desc">
                    NVIDIA NVDEC/NVENC, 인텔 QuickSync, 애플 VideoToolbox 하드웨어 디코더를 직접 호출하여 4K 60fps 무지연 스크러빙
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">프라이버시</span>
                  <strong>100% Local-First</strong>
                  <div class="schematic-desc">
                    인터넷 연결이 끊겨도 모든 기능 온전 구동. 프로젝트 파일, 캐시, 렌더링 결과물이 사용자 로컬 SSD에만 보존
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">AI 연동 인터페이스</span>
                  <strong>내장 MCP 서버</strong>
                  <div class="schematic-desc">
                    Claude Code 등에서 `concat --mcp`로 호출. 음성 대화 기반 자동 컷편집 및 타임라인 자동 완성 스크립팅 지원
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">크로스 플랫폼</span>
                  <strong>Tauri 경량 바이너리</strong>
                  <div class="schematic-desc">
                    Windows(MSI/EXE), macOS(Apple Silicon/Intel), Linux(AppImage/deb) 단일 코드베이스로 동일한 성능과 단축키 보장
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: JSON-RPC 자동화와 무손실 타임라인 파이프라인
            </h3>
            <p>
              기존 영상 편집 프로그램들이 플러그인 생태계를 독점 API로 걸어 잠근 것과 달리, 
              Concat은 모든 타임라인 조작을 <strong>JSON-RPC 2.0 프로토콜</strong>로 완전히 투명하게 개방했다.
            </p>
            <p>
              개발자나 크리에이터는 파이썬 스크립트나 AI 하네스를 통해 <em>"1분 20초부터 2분 10초 사이의 묵음 구간을 모두 잘라내고, 중요한 단어 5개에 팝업 텍스트 이펙트를 추가한 뒤 9:16 세로 릴스로 렌더링해 줘"</em>라는 자연어 명령을 내릴 수 있다. 
              Concat의 헤드리스 엔진이 백그라운드에서 프로젝트 AST를 실시간 수정하고 무손실 하드웨어 가속 렌더러로 5초 만에 쇼츠 영상을 굽는다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_concat_editor.jpg" alt="Concat Native Rust Video Editor UI" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="video"></i> <strong>[실구동 캡처 검증]</strong> Concat 다크 모드 타임라인 인터페이스. 다중 비디오·오디오 트랙, 실시간 파형(Waveform) 시각화, 키프레임 제어 패널 및 미디어 라이브러리가 깔끔한 다크 테마로 구성되어 있으며, 상용 캡컷과 동일한 반응형 UX를 구독료와 계정 로그인 없이 완전 무료로 제공하고 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="dollar-sign"></i> 4. 비즈니스 대격변: 구독 피로(Subscription Fatigue)와 오픈소스의 반격
            </h3>
            <p>
              어도비(Adobe)의 크리에이티브 클라우드 월 6만 원, 캡컷 프로 월 1만 5천 원... 
              전 세계 디지털 크리에이터들이 겪고 있는 <strong>'구독 피로(Subscription Fatigue)'</strong>는 이미 포화 상태다. 
              내가 만든 콘텐츠의 소유권을 주장하기도 전에, 도구 사용료로 수입의 상당 부분을 빅테크 플랫폼에 바쳐야 하는 구조적 착취가 지속되어 왔다.
            </p>
            <p>
              Concat은 이 기형적인 비즈니스 모델에 대한 오픈소스 진영의 단호한 거부권(Veto)이다. 
              블렌더(Blender)가 수십조 원의 3D CG 소프트웨어 시장을 무료화했듯이, 
              Concat은 숏폼과 영상 편집 시장에서 독점 기업들의 마진을 0으로 수렴시키는 파괴적 균열을 만들어내고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="scissors"></i> 5. 키커: 창작의 도구는 만인의 것이어야 한다
            </h3>
            <p>
              영상 편집은 21세기 인류의 가장 보편적인 언어가 되었다. 
              자신의 생각을 비디오로 표현하는 행위가 거대 테크 기업의 월 결제일과 신용카드 잔고에 저당 잡혀서는 안 된다. 
              가장 현대적인 언어 Rust로 벼려낸 Concat의 가위는, 
              빅테크가 묶어둔 구독의 사슬을 끊고 전 세계 모든 창작자에게 온전한 자유를 돌려주고 있다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=Concat+Free+Open+Source+CapCut+Replacement+Rust" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/jub0t/Concat" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
            <a href="https://concatenate.pages.dev" target="_blank" rel="noopener noreferrer" class="project-link demo">
              <i data-lucide="external-link" style="width:16px;height:16px;"></i> Concat 공식 웹사이트
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
