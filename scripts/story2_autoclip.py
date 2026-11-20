# -*- coding: utf-8 -*-
# Story 2: zhouxiaoka/autoclip

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] zhouxiaoka/autoclip                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_autoclip.jpg" alt="AutoClip Local AI Video Clipping Studio Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="scissors" style="width:12px;height:12px;fill:#fff;"></i> AI VIDEO STUDIO</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">🔥 단돈 18원으로 숏폼 10편·커버·발행 패키지 완성</span>
              <span class="platform-tag">GitHub Trending &amp; autoclip_intro</span>
              <span class="platform-tag">zhouxiaoka / autoclip</span>
            </div>

            <h2 class="article-headline">
              "링크 하나 던지면 7.5분 만에 숏폼 10편 출고" — 월 10만 원대 AI 숏폼 구독 SaaS를 파괴하는 로컬 스튜디오 'AutoClip'
            </h2>

            <div class="article-subheadline">
              1시간 43분짜리 젠슨 황 인터뷰를 텍스트 모델 비용 0.09위안(약 18원)으로 YouTube Shorts·TikTok·Reels·샤오홍슈 맞춤 세로형 클립·자막·커버·ZIP 패키지로 로컬 자동 렌더링하고 MCP 서버로 에이전트에 직결 (+983스타/일, 누적 12,138스타)
            </div>
            <p class="article-snippet">
              1~3시간짜리 팟캐스트와 컨퍼런스 대담을 세로형 숏폼으로 잘라내고, 화자를 추적해 크롭하며, 플랫폼별 썸네일과 카피까지 뽑아내는 작업에 월 수십 달러씩 OpusClip 같은 클라우드 SaaS를 결제하던 크리에이터 생태계가 뒤집히고 있습니다. 오늘 하루에만 983스타를 추가하며 GitHub 트렌딩 최상위권에 오른 <strong>zhouxiaoka/autoclip</strong>은 편집·화자 프레이밍·FFmpeg 렌더링을 전량 내 컴퓨터에서 돌리며 데스크톱 앱과 CLI, MCP 서버까지 단일 파이프라인으로 묶어냈습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 1시간 43분짜리 인터뷰가 7.5분 만에 10개의 숏폼 패키지로 쏟아졌다
            </h3>
            <p>
              영어로 된 1시간 43분 분량의 젠슨 황(Jensen Huang) 인터뷰 URL을 붙여넣고 목표 플랫폼으로 'Shorts'와 '샤오홍슈'를 고른다. 커피 한 잔을 내리고 돌아온 7.5분 뒤, 로컬 디스크에는 이미 10편의 완결된 세로형 하이라이트 영상과 커버 이미지, 제목, 해시태그, 심지어 바로 업로드할 수 있는 ZIP 발행 패키지까지 생성돼 있다. 그동안 나간 AI API 비용은 텍스트 모델 기준 고작 <strong>0.09위안(한화 약 18원)</strong>. 자막이 없는 2시간 52분짜리 중국어 대담조차 로컬 Whisper로 전사하고 10편을 뽑아내는 데 29.5분과 0.20위안(약 40원)밖에 들지 않았다.
            </p>
            <p>
              오늘 하루에만 <strong>+983스타(누적 12,138스타)</strong>를 모으며 폭발적인 반향을 일으킨 MIT 오픈소스 프로젝트 <strong>zhouxiaoka/autoclip</strong>이 증명한 현실이다. 과거 웹 SaaS로 몇 시간의 크레딧 제한을 걸어두고 월 29~99달러를 받던 상용 숏폼 재가공(Content Repurposing) 도구들의 수익 모델이 오픈소스 로컬 데스크톱 + 바이브 에이전트 MCP 조합 앞에서 무력화되고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 클라우드 렌더링 대기열과 자릿세의 종말
            </h3>
            <p>
              기존 AI 클리핑 SaaS의 가장 큰 병목은 무거운 영상 파일의 클라우드 업로드 대기 시간, 워터마크 인질극, 그리고 분당 과금되는 렌더링 크레딧이었다. AutoClip은 무거운 연산인 디코딩·화자 추적 프레이밍·자막 번인(Burn-in)·인코딩을 전부 <strong>사용자의 Apple Silicon Mac이나 Windows x64·Docker 환경의 로컬 FFmpeg</strong>로 끌어내리고, 클라우드나 로컬 LLM(Ollama/LM Studio)에는 가벼운 텍스트 분석과 필요 최소한의 샘플링 프레임만 넘기는 역발상으로 비용을 100분의 1 수준으로 압축했다.
            </p>

            <div class="editorial-quote">
              <p>
                "편집, 화자 프레이밍, 최종 렌더링은 온전히 당신의 컴퓨터에서 끝난다. <strong>더우인·샤오홍슈는 인터뷰 2분할 구도로, TikTok·Reels·Shorts는 풀스크린 팟캐스트 구도로</strong> 플랫폼 문법까지 스스로 맞춰 출고한다."
              </p>
              <small>— zhouxiaoka/autoclip 로컬-퍼스트 아키텍처 &amp; 플랫폼 어댑터 설계 (MIT)</small>
            </div>

            <p>
              더욱이 <code>npx skills add zhouxiaoka/autoclip</code>과 <code>uvx autoclip-mcp</code>를 통해 최신 데스크톱 앱과 완벽히 동일한 일괄 제작 파이프라인을 MCP(Model Context Protocol)로 개방함으로써, 이제는 AI 코딩 에이전트가 영상 수집부터 숏폼 10편 추출·자막 페이지네이션·ZIP 패킹까지 무인으로 지휘한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 원클릭 로컬 클리핑 · 화자 추적 · MCP 통합 파이프라인
            </h3>
            <p>
              AutoClip은 단일 Python/FFmpeg 코어를 Desktop(Tauri/React), Docker Web UI(Next.js + FastAPI), CLI, 그리고 <code>autoclip-mcp</code>가 공유하는 일관된 3단 파이프라인을 구축했다:
            </p>
            <ul>
              <li><strong>하이브리드 자막·멀티모달 스코어링:</strong> 원작자 자막(<code>--srt</code>)이 있으면 음성을 재전사하지 않고 즉시 분석에 돌입하며, 자막이 없을 경우 내장 로컬 Whisper / SenseVoice(또는 Qwen-Audio 등 클라우드 전사)로 타임스탬프를 추출한다. 이후 플랫폼별 바이럴 점수 모델이 상위 10개 하이라이트 구간을 선별하고 나머지는 예비 후보로 대기시킨다.</li>
              <li><strong>동적 화자 프레이밍 &amp; 자막 페이지네이션:</strong> 세로형 영상 변환 시 단순히 화면 중앙을 자르지 않고 말하는 인물을 추적해 구도를 잡으며, 슬라이드나 무인 샷이 나오면 자동으로 전체 화면(Full-frame)으로 복귀해 정보 손실을 막는다.</li>
              <li><strong>에이전트 네이티브 CLI &amp; MCPB 브리지:</strong> <code>autoclip produce talk.mp4 --platform douyin --json</code> CLI와 <code>start_quick_output</code> / <code>get_quick_output_status</code> MCP 툴을 제공해 OpenCode·Claude Code 등 에이전트가 영상 제작 워크플로우에 직접 개입하고 결과물을 타임라인 에디터로 넘길 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">AutoClip 로컬 영상 재가공 &amp; MCP 자동 출고 파이프라인</span>
                <span class="schematic-badge">MIT License · Desktop + CLI + autoclip-mcp</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Ingest &amp; Local ASR</div>
                  <div class="schematic-desc">
                    영상 URL / 로컬 MP4 입력<br>
                    기존 자막 우선 재사용 (<code>--srt</code>)<br>
                    로컬 Whisper / SenseVoice 전사<br>
                    타임스탬프·청크 인덱싱
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Highlight &amp; Framing</div>
                  <div class="schematic-desc">
                    LLM 기반 서사 스코어링 (Top 10 선정)<br>
                    (Ollama 로컬 또는 저비용 API 선택)<br>
                    인터뷰형 / 풀스크린 팟캐스트 자동 구도<br>
                    화자 추적 크롭 &amp; 무인샷 전체 보존
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Local Render &amp; MCP</div>
                  <div class="schematic-desc">
                    로컬 FFmpeg 60fps 고속 렌더링<br>
                    커버·제목·소개·해시태그·ZIP 패키징<br>
                    <code>autoclip mcp</code> (에이전트 원격 제어)<br>
                    수동 타임라인 에디터 미세 조정 지원
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">AutoClip 공식 소개 페이지 &amp; 실제 AI 숏폼 렌더링 쇼케이스</span>
              </div>
              <img src="../assets/images/demo_autoclip.png" alt="AutoClip Official Showcase Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ zhouxiaoka.github.io/autoclip_intro 공식 페이지 실화면: 빌 게이츠·샘 알트만·젠슨 황 등 실제 장편 대담에서 자동 추출한 세로형/가로형 숏폼 성편과 플랫폼별 자막·프레이밍 결과를 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: OpusClip의 월정액 벽과 어도비 타임라인의 무게를 동시에 무너뜨리다
            </h3>
            <p>
              OpusClip, Munch, Vizard 등 실리콘밸리에서 수천만 달러의 투자를 유치했던 AI 숏폼 SaaS 스타트업들의 해자는 '자막-하이라이트-크롭'을 한 번에 묶어주는 워크플로우 편의성뿐이었다. 이들은 분 단위 업로드 제한과 워터마크, 월정액 구독으로 크리에이터의 마진을 잠식해 왔다.
            </p>
            <ul>
              <li><strong>MIT 완전 개방과 프라이버시 투명성:</strong> AutoClip은 미공개 원고나 사내 강연 영상이 외부 렌더링 서버에 올라가는 것을 극도로 꺼리는 기업 마케팅팀에게 완벽한 대안을 제시한다. Ollama와 로컬 Whisper를 묶으면 1바이트의 영상도 사내망 밖으로 나가지 않는다.</li>
              <li><strong>무서명(Attribution-Free) 카피 출력:</strong> 복사하는 발행 문구에 'AutoClip으로 제작됨' 같은 강제 꼬리표를 붙이지 않는 철저한 크리에이터 중심 철학은 상업 채널의 즉각적인 실전 채택을 이끌고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 영상 편집의 '클라우드 렌더링 세금'은 끝났다
            </h3>
            <p>
              텍스트와 코드에서 시작된 AI의 로컬 민주화가 이제 가장 무거운 미디어 영역인 비디오 프로덕션의 자릿세까지 지우고 있다.
            </p>
            <p>
              링크 하나에 18원. 1만2천 개의 별표가 증명하듯, 앞으로 1인 미디어와 에이전트 파이프라인의 표준 편집실은 클라우드 구독 결제창이 아니라 내 책상 위 CPU와 로컬 터미널 안에서 돌아갈 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=AutoClip+open+source+AI+video+clipping" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://zhouxiaoka.github.io/autoclip_intro/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 / 사례집
              </a>
              <a href="https://github.com/zhouxiaoka/autoclip" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
