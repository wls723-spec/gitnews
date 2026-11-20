# -*- coding: utf-8 -*-
# Story 4: FlashML-org/FreeVideo

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] FlashML-org/FreeVideo                            -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_freevideo.jpg" alt="FreeVideo 8GB VRAM Local Video Generation Engine Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="film" style="width:12px;height:12px;fill:#fff;"></i> LOCAL VIDEO AI</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e40af;">🎬 8GB VRAM 내 PC에서 MiniMax H3 로컬 영상 생성</span>
              <span class="platform-tag">GitHub Trending &amp; freevideo-community</span>
              <span class="platform-tag">FlashML-org / FreeVideo</span>
            </div>

            <h2 class="article-headline">
              "H100 클라우드 구독료는 필요 없다" — 단 8GB VRAM 소비자용 GPU에서 1분짜리 MiniMax H3 영상과 16MP 이미지를 굽는 'FreeVideo'
            </h2>

            <div class="article-subheadline">
              8-step Video DeltaNet(VDN) 하이브리드 어텐션 + 비동기 가중치 스트리밍 + RTX 30시리즈 int8 2.3배 가속으로 GeForce 노트북·Apple Silicon Mac까지 뚫고 ComfyUI 타임라인·코딩 에이전트 제어까지 결합한 Apache-2.0 엔진 (+304스타/일, 누적 3,770스타)
            </div>
            <p class="article-snippet">
              5초짜리 AI 영상을 몇 번 생성하고 나면 수십 달러의 크레딧이 순식간에 증발하던 클라우드 생성형 비디오 시장에 정면 균열이 가고 있습니다. 오늘 하루 304스타를 보태며 누적 3,770스타로 급부상한 <strong>FlashML-org/FreeVideo</strong>는 OpenVDN의 8스텝 VDN-H3 모델과 하드웨어 적응형 가중치 스트리밍을 결합해, 일반 게이밍 PC의 8GB VRAM·16GB RAM만으로도 멀티모달(텍스트·초/말 프레임·이미지·오디오) 영상과 16MP 고해상도 이미지를 100% 로컬에서 생성합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 8GB VRAM 보급형 그래픽카드에서 MiniMax H3 영상이 돌아가는 순간
            </h3>
            <p>
              불과 얼마 전까지만 해도 최상위 비디오 파운데이션 모델을 돌린다는 것은 월 수백 달러를 태우는 클라우드 API를 쓰거나 80GB H100 서버를 빌리는 일이었다. 8GB VRAM짜리 노트북 GPU에 수십 기가바이트 비디오 디퓨전 가중치를 올리는 순간 즉시 <code>CUDA Out Of Memory</code> 에러를 뱉으며 프로세스가 죽었기 때문이다.
            </p>
            <p>
              그러나 <strong>FlashML-org/FreeVideo</strong>의 원클릭 런처(<code>FreeVideo.exe</code> / Apple Silicon <code>.dmg</code> / Linux <code>AppImage</code>)를 실행하면 풍경이 바뀐다. 브라우저에 ComfyUI 기반 전용 크리에이티브 워크스페이스가 열리고, 사용자는 단돈 1원도 클라우드에 내지 않은 채 내 책상 위 8GB VRAM GPU에서 MiniMax H3 기반 영상과 v0.5.0에 추가된 <strong>최대 16메가픽셀(16 MP) 로컬 이미지</strong>를 뽑아낸다. 오늘 하루 <strong>+304스타(누적 3,770스타)</strong>가 몰린 이유는 명확하다. "이미 당신이 소유한 컴퓨터에서 영상을 만들어라"는 약속이 실제 코드로 증명됐기 때문이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 선형 시간 Video DeltaNet과 소비자용 하드웨어의 해방
            </h3>
            <p>
              긴 영상을 로컬에서 만들지 못했던 근본 원인은 프레임 수가 늘어날수록 연산량과 메모리 점유율이 제곱($O(N^2)$)으로 폭증하는 기존 시공간 풀 어텐션(Full Attention) 구조에 있었다. FreeVideo는 <strong>OpenVDN의 8-step Video DeltaNet(VDN-H3)</strong> 하이브리드 어텐션 모델을 토대로 삼고, 그 위에 GPU VRAM·시스템 RAM·디스크를 정교하게 지휘하는 자체 저메모리 추론 엔진을 얹어 1분 이상의 장편 영상 생성과 4단계 화질 프리뷰 워크플로우를 일반 PC로 끌어내렸다.
            </p>

            <div class="editorial-quote">
              <p>
                "하드웨어에 맞춰 가중치 배치와 정밀도, 어텐션 커널을 스스로 조율한다. <strong>GeForce·RTX 30 시리즈에서는 자동으로 int8로 전환해 5초 영상 생성을 약 2.3배 가속</strong>하고, 단 8GB VRAM·16GB RAM 한계 안에서 16MP 이미지와 1분 이상 비디오를 완주한다."
              </p>
              <small>— FlashML-org/FreeVideo 아키텍처 &amp; v0.3~v0.5 릴리즈 노트 (Apache-2.0)</small>
            </div>

            <p>
              더 놀라운 점은 v0.4.0부터 <strong>Claude Code나 Codex 같은 AI 코딩 에이전트</strong>가 FreeVideo를 직접 조종해 1분 이상 영상을 생성하고 타임라인 뷰에서 편집까지 수행할 수 있도록 문을 열어두었다는 사실이다. 로컬 비디오 엔진이 에이전트의 '시각 제작 도구'로 합류한 셈이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 8-Step VDN 하이브리드 어텐션 · 비동기 가중치 스트리밍 · 하드웨어 적응 실행
            </h3>
            <p>
              FreeVideo가 OOM(메모리 초과) 없이 8GB VRAM 벽을 돌파하는 핵심 기술은 세 가지 계층의 치밀한 시스템 엔지니어링에 있다:
            </p>
            <ul>
              <li><strong>하드웨어 적응형 정밀도 &amp; 커널 프로빙:</strong> 실행 시점에 장착된 GPU 세대를 자동 판별한다. GeForce 및 RTX 30 시리즈에는 <code>int8</code> 양자화 가중치를 배치해 2.3배 속도 향상을 끌어내고, 워크스테이션/데이터센터 GPU에서는 <code>FP8</code> 경로를 택하며 가용한 최적 어텐션 커널을 자동 탐색한다. Apple Silicon Mac 네이티브 실행도 공식 지원한다.</li>
              <li><strong>가중치 스트리밍 · 비동기 프리페치 · 청크 연산:</strong> 모델 전체를 VRAM에 상주시키는 대신, 지금 연산할 레이어의 가중치만 비동기 DMA 프리페치로 시스템 RAM/디스크에서 스트리밍하고 중간 활성화 텐서를 청크 단위로 쪼개 처리해 피크 VRAM을 8GB 이하로 묶는다.</li>
              <li><strong>절반 해상도 선프리뷰 &amp; 워크플로우 임베딩(ComfyUI):</strong> v0.3.2의 'Preview First' 기능으로 저해상도 초안을 먼저 확인해 마음에 드는 시드만 풀 해상도로 마감할 수 있어 전기세와 시간을 아낀다. 생성된 영상 파일 자체에 프롬프트·시드·LoRA 설정 메타데이터가 박혀 있어 ComfyUI 캔버스에 드래그 앤 드롭하면 즉시 작업 상태가 복원된다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">FreeVideo 8GB VRAM 로컬 비디오·16MP 이미지 추론 아키텍처</span>
                <span class="schematic-badge">Apache-2.0 · OpenVDN H3 (8-Step) · ComfyUI Native</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Multimodal &amp; Agent Input</div>
                  <div class="schematic-desc">
                    텍스트 · 시작/끝 프레임 · 오디오 레퍼런스<br>
                    커뮤니티 MiniMax H3 LoRA 플러그인<br>
                    Claude Code / Codex 에이전트 제어<br>
                    Half-Res 프리뷰로 시드 사전 선별
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Adaptive VDN-H3 Engine</div>
                  <div class="schematic-desc">
                    8-Step Video DeltaNet 하이브리드 어텐션<br>
                    <strong>RTX 30xx int8 (2.3x↑)</strong> / 워크스테이션 FP8<br>
                    가중치 스트리밍 + 비동기 프리페치<br>
                    청크 연산으로 <strong>8GB VRAM · 16GB RAM</strong> 유지
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Timeline &amp; Reproducible Out</div>
                  <div class="schematic-desc">
                    1분+ 장편 타임라인 편집 뷰 내장<br>
                    v0.5.0 최대 16MP 고화질 이미지 생성<br>
                    생성 영상 내 ComfyUI 워크플로우 자동 각인<br>
                    Win/Mac/Linux 원클릭 오프라인 설치 지원
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">FreeVideo 커뮤니티 갤러리 &amp; 4단계 화질 비교 실구동 쇼케이스</span>
              </div>
              <img src="../assets/images/demo_freevideo.png" alt="FreeVideo Community Gallery Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ freevideo-community.pages.dev 공식 갤러리 실화면: Light·Medium·High·Max 4단계 화질 레벨별 결과물, GPU 사양 및 실제 로컬 생성 소요 시간을 투명하게 비교 전시하고 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업 패권: 클라우드 비디오 API의 크레딧 과금 모델과 검열 장벽 돌파
            </h3>
            <p>
              Runway, Kling, Sora 등 상용 클라우드 비디오 플랫폼의 비즈니스 모델은 거대한 H100 GPU 클러스터 임대료와 불투명한 크레딧 차감 구조에 기대고 있다. 사용자는 프롬프트를 조금만 고쳐도 다시 과금되며, 사내 미공개 제품 시안이나 영화 콘티를 외부 서버에 올려야 하는 보안 리스크까지 떠안는다.
            </p>
            <ul>
              <li><strong>Apache-2.0 개방과 오프라인 주권:</strong> FreeVideo는 4대 모델 팩(비디오·텍스트 인코더·비디오/오디오 디코더·샘플링 캐시)을 오프라인 ZIP으로도 가져올 수 있게 설계해 인터넷이 끊긴 스튜디오나 사내 망에서도 동일한 품질의 영상을 뽑아낸다.</li>
              <li><strong>생태계 승수 효과:</strong> 독자 폐쇄 포맷을 고집하는 대신 이미 수십만 명의 크리에이터가 쓰는 <strong>ComfyUI</strong>를 전면 채택해 기존 노드·커뮤니티 LoRA 생태계를 그대로 흡수했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 크리에이티브의 제약은 '구독 한도'가 아니라 당신의 상상력뿐이다
            </h3>
            <p>
              불과 2년 전 LLM에서 벌어졌던 '데이터센터에서 내 노트북 VRAM으로의 대이동'이 이제 생성형 비디오와 멀티모달 영역에서 똑같이 재현되고 있다.
            </p>
            <p>
              클라우드의 과금 타이머를 끄고 8GB 노트북 GPU 팬이 돌아가는 소리 속에서 1분짜리 영상을 직접 빚어내는 순간, AI 영상 제작의 주도권은 빅테크 플랫폼에서 다시 개인 창작자의 책상으로 돌아온다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=FreeVideo+MiniMax+H3+8GB+VRAM+ComfyUI" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://freevideo-community.pages.dev/#gallery" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 갤러리 / 화질 비교
              </a>
              <a href="https://github.com/FlashML-org/FreeVideo" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
