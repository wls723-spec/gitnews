# -*- coding: utf-8 -*-
# Story 4: kajisho5/ffmpeg-skill

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] kajisho5/ffmpeg-skill                            -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ffmpeg_skill.jpg" alt="ffmpeg-skill Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="film" style="width:12px;height:12px;fill:#fff;"></i> LOCAL VIDEO AI</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">🎬 에이전트 전용 로컬 영상 편집기</span>
              <span class="platform-tag">GitHub Trending &amp; MCP</span>
              <span class="platform-tag">kajisho5 / ffmpeg-skill</span>
            </div>

            <h2 class="article-headline">
              "더 이상 엉터리 FFmpeg 명령어를 추측하지 않는다" — 코딩 에이전트에게 결정론적 영상 편집 손을 달아준 'ffmpeg-skill'
            </h2>

            <div class="article-subheadline">
              API 키·클라우드 업로드 없이 Python 표준 라이브러리만으로 42종 FFmpeg 도구·자동 검증 루프·기계 판독 가능 계약(SPEC) MCP 서버를 제공하는 MIT 오픈소스 (6,619스타)
            </div>
            <p class="article-snippet">
              LLM에게 영상 컷 편집이나 세로형 릴스 크롭을 시켜본 개발자라면 누구나 AI가 존재하지 않는 <code>ffmpeg</code> 필터 플래그를 지어내거나 오디오 싱크가 어긋난 결과물을 "완료했습니다"라고 우기는 현상을 겪어봤을 것입니다. 하루 475스타를 보태며 6,619스타에 올라선 <strong>kajisho5/ffmpeg-skill</strong>은 에이전트가 임의의 셸 문자열을 뱉지 못하게 막고, <code>probe → edit → check → verify</code>의 엄격한 42개 타입드 도구와 MCP 계약을 통해 100% 로컬에서 무오류 영상 편집을 수행합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 30년 된 만능 도구 FFmpeg 앞에서 쩔쩔매던 AI 에이전트
            </h3>
            <p>
              FFmpeg은 현대 인터넷 비디오의 숨은 엔진이지만, 그 문법은 인간에게도 악명 높다. <code>-filter_complex</code> 한 줄에 수십 개의 스트림 라벨과 픽셀 포맷, 타임스탬프 보정이 얽혀 있기 때문이다. AI 코딩 에이전트에게 영상 편집을 맡기면 십중팔구 프레임레이트를 제멋대로 가정하거나, 컨테이너가 지원하지 않는 코덱을 우겨 넣거나, 단순 스트림 복사(Stream Copy)로 1초 만에 끝날 일을 불필요하게 재인코딩해 화질을 깎아먹는다. 더 큰 문제는 에이전트가 결과 파일의 길이·해상도·음량을 확인조차 하지 않고 작업을 끝낸다는 점이다.
            </p>
            <p>
              이 고질적 문제를 정교한 계약 기반 도구 설계로 해결하며 <strong>6,619스타</strong>를 모은 프로젝트가 <strong>kajisho5/ffmpeg-skill</strong>이다. 클라우드 SaaS 영상 편집기 구독료도, 외부 API 키도, 심지어 외부 파이썬 패키지 의존성조차 없이 오직 로컬 <code>ffmpeg</code>와 Python 표준 라이브러리만으로 돌아간다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '두뇌(LLM)'와 '손(결정론적 실행 엔진)'의 완벽한 분리
            </h3>
            <p>
              <code>ffmpeg-skill</code>의 설계 철학은 명쾌하다. LLM은 무엇을 자르고 어떤 자막을 넣을지 결정하는 '두뇌' 역할만 하고, 실제 프레임을 자르고 음량을 맞추며 규격을 재측정하는 '손'의 영역에서는 단 1픽셀·0.01초의 추측도 허용하지 않는 것이다.
            </p>

            <div class="editorial-quote">
              <p>
                "아무것도 셸(Shell)을 거치지 않고, 호출자로부터 임의의 필터 그래프 문자열도 받지 않는다. 모든 작업은 <code>probe.py</code> 실측으로 시작해 <strong>타입이 지정된 42개 스크립트를 거쳐, 최종 파일의 길이·해상도·음량·시각적 밀착 시트까지 사후 검증</strong>한 뒤 구조화된 JSON으로 보고한다."
              </p>
              <small>— ffmpeg-skill v3 아키텍처 원칙 및 SPEC (Self-Producing Execution Contract) 문서</small>
            </div>

            <p>
              실제로 <code>npx ffmpeg-skill</code> 한 줄이면 Claude Code, Cursor, Codex 등 모든 <code>SKILL.md</code> 및 MCP 호환 클라이언트에 즉시 장착된다. 촬영 원본이 기밀이거나 용량이 수십 GB에 달해 클라우드에 올릴 수 없는 프로덕션 팀에게도 완벽한 오프라인 대안이 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: SPEC 자가 생성 계약과 42종 Probe-Edit-Verify 파이프라인
            </h3>
            <p>
              에이전트가 도구의 인자를 착각하지 않고, 도구가 늘어나도 컨텍스트 창이 터지지 않게 만드는 세 가지 내부 메커니즘이 돋보인다:
            </p>
            <ul>
              <li><strong>SPEC (Self-Producing Execution Contract):</strong> 42개 도구의 JSON 입력 스키마와 MCP 도구 정의를 별도 파일에 손으로 복붙하지 않는다. 실제 CLI를 정의하는 파이썬 <code>argparse</code> 파서에서 런타임에 계약을 직접 추출하며, 문서와 코드가 조금이라도 어긋나면 CI 빌드가 즉시 실패한다.</li>
              <li><strong>컨텍스트 최적화 MCP 노출 + 전체 호출 호환:</strong> <code>tools/list</code> 응답은 클라이언트 컨텍스트 절약을 위해 핵심 12개 도구만 기본 노출하지만(<code>FFMPEG_SKILL_MCP_FULL=1</code> 시 42개 전체 노출), 42개 모든 도구는 <code>tools/call</code>로 즉시 호출할 수 있다.</li>
              <li><strong>무손실 우선 편집 &amp; 물리량 사후 검증(<code>check.py</code> · <code>look.py</code>):</strong> 컷·병합·무음 제거(<code>silence.py</code>)·카라오케 팝업 자막(<code>caption.py</code>)·16:9→9:16 스마트 크롭(<code>fit.py</code>)·EBU R128 라우드니스 정규화(<code>loudness.py</code>)는 물론, 멀티캠 싱크와 드리프트 보정까지 수행한 뒤 최종 산출물을 <code>ffprobe</code>와 컨택트 시트로 재검증한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">ffmpeg-skill v3 결정론적 영상 편집 &amp; SPEC 계약 아키텍처</span>
                <span class="schematic-badge">42 Tools · Zero Deps · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Probe &amp; SPEC Contract</div>
                  <div class="schematic-desc">
                    <code>probe.py</code>로 실측 메타데이터 확보<br>
                    <code>argparse</code> 파서에서 JSON 스키마 자동 도출<br>
                    Core 12개 기본 노출 / 42종 MCP 풀 호출<br>
                    셸 인젝션·임의 필터 그래프 차단
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. 42 Typed Editing Tools</div>
                  <div class="schematic-desc">
                    컷/병합(무손실 우선) · 무음 제거(<code>silence.py</code>)<br>
                    9:16 리프레임(<code>fit.py</code>) · 팝업 자막(<code>caption.py</code>)<br>
                    HDR→SDR LUT · 오디오 다이나믹스 · <code>loudness.py</code><br>
                    멀티캠 드리프트 보정 &amp; 배치 렌더링
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Post-Export Verification</div>
                  <div class="schematic-desc">
                    <code>check.py</code>: 목적지 규격(길이·FPS·음량) 대조<br>
                    <code>look.py</code>: 화면 변화 구간 컨택트 시트 생성<br>
                    구조화된 JSON 측정치 반환(예: 59.98s, 1080×1920)<br>
                    FFmpeg 6.1 · 7.1 · 8 · 9 CI 전수 검증
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">ffmpeg-skill 공식 데모 및 42종 파이프라인 포털 (kajisho5.github.io/ffmpeg-skill)</span>
              </div>
              <img src="../assets/images/demo_ffmpeg_skill.png" alt="ffmpeg-skill Official Portal and Before/After Video Demos" class="showcase-img">
              <p class="showcase-caption">
                ▲ kajisho5.github.io/ffmpeg-skill/ 실구동 화면: 카라오케 팝 자막, 16:9→9:16 세로 리프레이밍, 무음 컷 편집, 라우드니스 파형 정규화 등 모든 데모가 재현 가능한 CLI 명령어와 함께 제공된다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업적 파급력: 클라우드 영상 편집 SaaS를 위협하는 로컬 '하네스 생태계'
            </h3>
            <p>
              OpusClip, Descript 같은 클라우드 AI 영상 편집 서비스는 월 구독료를 받고 영상을 서버에 업로드한 뒤 자막을 입히고 숏폼을 잘라낸다. 그러나 개인정보가 담긴 회의 녹화본, 미공개 제품 영상, 고화질 4K 프로레스(ProRes) 원본을 매번 클라우드로 올리는 것은 비용과 보안 양면에서 거대한 마찰이었다.
            </p>
            <ul>
              <li><strong>단방향 의존 생태계의 표준 블록:</strong> <code>ffmpeg-skill</code>은 <code>remotion-ffmpeg-skill</code>, <code>transcription-skill</code>, <code>qc-skill</code> 등 상위 AI 영상 프로덕션 에이전트들이 믿고 호출할 수 있는 순수 '물리 엔진' 역할을 수행한다.</li>
              <li><strong>프라이버시와 속도의 동시 확보:</strong> 로컬 Whisper/Parakeet과 결합할 경우 단 1바이트의 영상 데이터도 외부 서버로 나가지 않은 채 숏폼 편집부터 방송 규격 라우드니스 검사까지 자동화할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 에이전트에게 필요한 건 더 똑똑한 프롬프트가 아니라 '거짓말 못 하는 자와 캘리퍼스'다
            </h3>
            <p>
              AI가 전문 도구를 다루지 못했던 이유는 지능이 부족해서가 아니라, 자기가 만든 결과물을 스스로 측정할 계측기가 없었기 때문이다.
            </p>
            <p>
              <code>ffmpeg-skill</code>이 증명한 해법은 단순하고도 강력하다. 에이전트에게 셸 권한을 통째로 던져주며 기적을 바라지 말고, 타입이 엄격한 도구와 사후 계측기를 쥐여주라. 그 순간 오래된 C 기반 오픈소스 도구조차 가장 믿음직한 AI 멀티미디어 스튜디오로 다시 태어난다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=ffmpeg-skill+MCP+AI+video+editor" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://kajisho5.github.io/ffmpeg-skill/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 &amp; 데모
              </a>
              <a href="https://github.com/kajisho5/ffmpeg-skill" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
