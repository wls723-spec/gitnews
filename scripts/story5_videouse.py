# -*- coding: utf-8 -*-
# Story 5: browser-use/video-use

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] browser-use/video-use : 코딩 에이전트 비디오 편집 스튜디오 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_video_use.jpg" alt="video-use Coding Agent Automated Video Editor" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 112K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🎬 3만 스타 browser-use 팀의 신작</span>
              <span class="aggro-tag">✂️ 타임라인 GUI 없는 터미널 영상 편집기</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">browser-use / video-use</span>
            </div>
            
            <h2 class="article-lead-headline">
              프리미어와 캡컷의 타임라인을 터미널로 치환하다: 3만 스타 browser-use 팀의 100% 오픈소스 에이전트 영상 제작소 'video-use'
            </h2>

            <div class="article-subheadline">
              "Edit videos with Claude Code. 100% open source" — browser-use, 원본 촬영 영상 폴더만 지정하고 터미널에서 대화하면 불필요한 추임새·무음 자동 컷편집, 30ms 오디오 페이드, 자막 버닝, Remotion·Manim 애니메이션 서브에이전트 병렬 합성까지 원스톱으로 final.mp4를 렌더링하는 AI 영상 제작 혁명
            </div>
            <p class="article-snippet">
              마우스로 수백 번 자르고 이어 붙이던 지루한 NLE 타임라인 편집의 종말. 코딩 에이전트가 영상의 모든 컷 경계면을 스스로 시청하고 자가 평가(Self-evaluating)하여 무결점 영상을 뽑아내는 차세대 오픈소스 비디오 파이프라인.
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
              <i data-lucide="scissors"></i> 1. 리드: 새벽 3시, 타임라인의 파도 속에서 허우적대던 영상 편집자들
            </h3>
            <p>
              유튜브 크리에이터나 영상 콘텐츠 제작자에게 가장 고통스럽고 지루한 노동은 무엇인가? 
              바로 원본 촬영본에서 <em>"어...", "음...", "그게 아니라..."</em> 같은 말실수와 헛기침, 말문이 막힌 무음 구간을 수백 번 가위질하며 잘라내는 <strong>'기본 컷편집(Rough Cut)'</strong>이다.
            </p>
            <p>
              어도비 프리미어 프로(Adobe Premiere Pro)나 다빈치 리졸브(DaVinci Resolve), 캡컷(CapCut) 같은 현대 비선형 영상 편집기(NLE)는 지난 30년 동안 화려한 이펙트와 색보정 도구를 추가해 왔지만, 본질적으로는 여전히 <strong>인간이 마우스로 타임라인의 클립을 일일이 쪼개고 당겨 붙여야 하는 가내수공업</strong>의 틀을 벗어나지 못했다. 
              10분짜리 브이로그나 튜토리얼 영상을 하나 만들기 위해 편집자는 3~4시간 동안 모니터를 뚫어져라 쳐다보며 같은 단축키를 수천 번 연타해야 했다.
            </p>
            <p>
              2026년 10월 26일, 깃허브 스타 3만 개를 돌파하며 브라우저 자율 조작 혁명을 이끌었던 <strong>'browser-use' 핵심 개발팀</strong>이 영상 편집 소프트웨어 시장에 강력한 폭탄을 투하했다. 
              100% 완전 무료 오픈소스 프로젝트 <strong>'video-use(browser-use/video-use)'</strong>를 공개하며, <strong>"타임라인도, 마우스도, 복잡한 메뉴도 필요 없다. 폴더에 영상만 던지고 터미널에서 에이전트와 대화하면 완성된 고화질 MP4가 나온다"</strong>는 선언을 던진 것이다.
            </p>

            <div class="editorial-quote danger">
              "소프트웨어 엔지니어링이 프롬프트와 에이전트로 이동했듯이, 영상 편집 역시 타임라인 인터페이스를 졸업해야 한다. 
              <strong>크리에이터의 머릿속에 있는 것은 스토리와 메시지이지, 프레임 단위의 레이저 툴 좌표가 아니다.</strong> 
              video-use는 에이전트가 귀로 듣고, 눈으로 검토하며, 스스로 렌더링하는 진정한 포스트 프로덕션의 자동화다."
              <span class="quote-author">— browser-use 코어 엔지니어링 팀</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: '말만 하는 AI'가 아닌 'ffmpeg을 지휘하는 오케스트라'
            </h3>
            <p>
              소라(Sora)나 런웨이(Runway) 같은 생성형 비디오 AI가 가상의 영상을 만들어내는 도구라면, <code>video-use</code>는 <strong>실제 인간이 촬영한 실사 영상을 전문가 수준으로 다듬어내는 실전 포스트 프로덕션 도구</strong>다.
            </p>
            <p>
              사용자가 할 일은 터미널에서 <code>cd /path/to/videos</code>를 친 뒤 <code>claude</code>를 실행하는 것뿐이다. 
              에이전트는 폴더 내의 다중 테이크(Takes)를 읽어 들여 음성 트랙을 전사(Whisper)하고, 발화 사이의 침묵과 추임새를 감지하여 밀리초 단위로 컷을 쳐낸다. 
              그리고 각 컷의 이음매마다 음향이 튀는 '퍽' 소리(Pop Noise)를 방지하기 위해 <strong>정밀한 30ms 오디오 마이크로 크로스페이드</strong>를 자동으로 삽입한다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="film" style="color:#ec4899;"></i> video-use: 5단계 자율 영상 합성 & 서브에이전트 렌더링 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">PROMPT-DRIVEN NLE PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 원본 분석 & 음성 전사</div>
                  <div class="step-title">Multi-Take Ingestion</div>
                  <div class="step-desc">다중 카메라 영상의 타임코드와 음성 파형을 Whisper로 분석하여 발화 구간과 무음 감지.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 추임새 제거 & 30ms 페이드</div>
                  <div class="step-title">Filler & Pop-Noise Strip</div>
                  <div class="step-desc">'음', '어' 등 불필요 어휘를 1프레임 단위로 잘라내고, 절단면마다 30ms 오디오 페이드를 걸어 무결음 처리.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 색보정 & 2단어 자막</div>
                  <div class="step-title">Auto Color & Subtitle Burn</div>
                  <div class="step-desc">ffmpeg 필터 체인으로 시네마틱 톤 자동 보정 및 모바일 쇼츠 규격의 2단어 대문자 하이라이트 자막 버닝.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 모션 그래픽 병렬 생성</div>
                  <div class="step-title">Sub-agent Motion Engine</div>
                  <div class="step-desc">Remotion, Manim, HyperFrames 서브에이전트들이 배경 설명 인포그래픽과 애니메이션을 병렬 렌더링.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 컷 경계면 자가 감사</div>
                  <div class="step-title">Self-evaluating Final Render</div>
                  <div class="step-desc">모든 컷 연결부의 영상 싱크와 오디오 밸런스를 에이전트가 직접 시청 검수 후 최종 final.mp4 출력.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 다중 애니메이션 엔진과 세션 기억 계승
            </h3>
            <p>
              <code>video-use</code>의 구조에서 가장 감탄을 자아내는 공학적 설계는 <strong>'이종 모션 그래픽 엔진들의 서브에이전트 병렬 지휘'</strong>다.
            </p>
            <p>
              단순한 텍스트 자막을 넘어 영상 중간에 수식이나 코드 실행 애니메이션, 통계 차트가 필요할 경우, <code>video-use</code>는 작업 목적에 따라 최적의 외부 렌더러를 선택하여 백그라운드 서브에이전트를 동시 스폰(Spawn)한다:
            </p>
            <ul style="margin: 1rem 0 1.5rem 1.5rem; line-height: 1.8; color: var(--text-dark);">
              <li><strong>Remotion:</strong> React 기반 컴포넌트로 60fps 인터랙티브 웹 UI 애니메이션 렌더링</li>
              <li><strong>Manim:</strong> 3Blue1Brown 스타일의 정밀한 수학·물리 수식 및 기하학 그래프 렌더링</li>
              <li><strong>HyperFrames:</strong> 초경량 HTML/CSS 기반의 60fps 결정론적 에이전트 비디오 렌더링</li>
              <li><strong>ElevenLabs 연동:</strong> 부족한 내레이션이나 다국어 더빙이 필요할 경우 고품질 음성 실시간 합성</li>
            </ul>
            <p>
              또한 <code>project.md</code> 파일에 크리에이터의 선호 자막 폰트, 컬러 팔레트, 컷 호흡 템포를 지속적으로 기록하여, 다음 주에 새로운 푸티지를 들고 와도 지난번 편집 스타일을 100% 동일하게 유지한다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_video_use_timeline.jpg" alt="video-use 터미널 기반 영상 편집 워크플로우 실구동 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>실제 video-use 비디오 편집 파이프라인 구동 화면:</strong> 터미널 환경에서 raw 푸티지를 입력받아 무음 구간을 30ms 오디오 페이드로 매끄럽게 연결하고, Remotion 및 Manim 서브에이전트와 협업하여 완성된 4K 비디오 트랙과 오디오 트랙을 단일 명령어로 결합·출력하는 차세대 NLE 아키텍처.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 어도비의 크리에이티브 클라우드 제국을 겨눈 칼끝
            </h3>
            <p>
              어도비(Adobe)가 연간 수조 원의 구독 매출을 올릴 수 있었던 본질적인 방어벽은 <strong>"프로페셔널 영상 편집자가 되려면 프리미어 프로의 복잡한 패널과 타임라인 인터페이스를 수년간 학습해야 한다"는 높은 진입 장벽</strong>이었다.
            </p>
            <p>
              그러나 <code>video-use</code>는 그 수년간의 소프트웨어 조작 숙련도를 <strong>'자연어 대화' 하나로 완전히 무력화</strong>했다. 
              이제 중고등학생이나 1인 기획자도 터미널 창에 <em>"튜토리얼 영상 만들어줘. 지루한 부분은 다 쳐내고 핵심 개념 나올 때 Manim 그래프 띄워줘"</em>라고 타이핑하는 것만으로, 월 수십만 원의 외주 편집자를 고용한 것 이상의 완성도를 10분 만에 얻을 수 있다. 
              상용 NLE 소프트웨어의 거대한 인터페이스 해자가 허물어지고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 마우스가 사라진 자리에 남는 창작자의 영혼
            </h3>
            <p>
              영상 편집의 본질은 언제나 '이야기를 전달하는 것'이었다. 
              그러나 도구의 복잡성 때문에 창작자들은 스토리의 깊이를 고민하는 시간보다, 타임라인 위에서 클립의 앞뒤를 맞추고 볼륨 게인을 조절하는 기계적인 노동에 90%의 에너지를 빼앗겨 왔다.
            </p>
            <p>
              <code>video-use</code>가 우리에게 돌려준 것은 단순히 절약된 시간만이 아니다. 
              잡다한 마우스 클릭의 굴레에서 해방된 크리에이터는 이제 다시 <strong>"무엇을 말할 것인가", "어떤 감동을 전할 것인가"라는 창작의 순수한 본질</strong>로 돌아갈 수 있게 되었다. 
              스크린의 타임라인은 사라졌지만, 스토리텔링의 새로운 황금기가 열리고 있다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=video-use+browser-use+claude+code+edit+videos" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/browser-use/video-use" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 5 (video-use) module loaded successfully.")
