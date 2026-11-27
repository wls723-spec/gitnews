# -*- coding: utf-8 -*-
# Story 3: SWE-agent/mini-swe-agent

STORY_3_HTML = r"""
      <!-- ========================================================== -->
      <!-- [HERO 3] SWE-agent/mini-swe-agent                          -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_mini_swe_agent.jpg" alt="Minimalist 100-Line Bash AI Coding Agent Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> AGENT ARCHITECTURE #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">⚡ ★10,142 · 단 100줄의 파이썬으로 SWE-bench Verified 74% 돌파</span>
              <span class="platform-tag">GitHub Trending &amp; Princeton/Stanford</span>
              <span class="platform-tag">SWE-agent / mini-swe-agent</span>
            </div>

            <h2 class="article-headline">
              "복잡한 툴 스캐폴딩은 모델의 발목을 잡을 뿐이었다" — 단 100줄의 Bash-Only 파이썬으로 Claude Code와 맞붙는 'mini-swe-agent'
            </h2>

            <div class="article-subheadline">
              SWE-bench와 SWE-agent의 원조 연구진이 직접 거대한 에이전트 스캐폴드를 도려내고, Tool-Calling API·상태 유지 셸 없이 순수 선형 메시지 이력과 subprocess.run 루프만으로 SWE-bench Verified 74%+를 달성한 초경량 코딩 에이전트 (v2.4.6 · MIT)
            </div>
            <p class="article-snippet">
              코딩 에이전트를 만들려면 파일 편집기, 검색기, AST 파서, 상태 유지 PTY 셸, 복잡한 컨텍스트 압축기 등 수만 줄의 스캐폴드가 필요하다는 업계 통념이 정면으로 부정당했습니다. <strong>SWE-agent/mini-swe-agent</strong>는 에이전트 코어 클래스가 <strong>단 약 100줄의 파이썬</strong>뿐이며, 심지어 LLM의 함수 호출(Tool-Calling) API조차 쓰지 않고 오직 독립적인 <code>bash</code> 실행(<code>subprocess.run</code>)과 선형 대화 기록만 유지합니다. 그런데도 <strong>SWE-bench Verified에서 74% 이상</strong>을 기록하며 Ramp SWE-Bench 공식 백엔드로 채택되었고 DeepSWE 평가에서 거대 상용 에이전트를 제쳤습니다(★<strong>10,142</strong>).
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
              <i data-lucide="flame"></i> 1. 리드: 창시자가 스스로의 유산을 100분의 1로 깎아낸 날
            </h3>
            <p>
              2024년 코딩 에이전트 혁명의 방아쇠를 당긴 장본인은 프린스턴과 스탠퍼드 연구진이 내놓은 <code>SWE-bench</code>와 <code>SWE-agent</code>였다. 당시 연구진은 모델이 파일 줄 번호를 틀리지 않도록 전용 에디터 인터페이스(ACI, Agent-Computer Interface)와 수십 종의 커스텀 도구를 정교하게 깎아 붙여야만 GitHub 이슈를 풀 수 있다고 믿었다. 그 결과 업계 전체가 거대한 에이전트 하네스와 복잡한 상태 머신을 쌓아 올리는 군비 경쟁에 돌입했다.
            </p>
            <p>
              하지만 2년 뒤, 같은 연구진이 던진 질문은 통렬한 자기반성이었다: <em>"만약 우리의 에이전트를 100배 단순하게 만들고도 거의 똑같이—혹은 더 잘—작동한다면?"</em> 그 답으로 내놓은 <strong><code>mini-swe-agent</code>(v2.4.6)</strong>는 Meta·NVIDIA·IBM·Anyscale·프린스턴·스탠퍼드 연구실은 물론, Ramp의 실시간 코딩 에이전트 벤치마크 표준으로 자리 잡았다. Claude Code보다 훨씬 빠르게 기동하며, 코드 전체를 개발자 한 명이 10분 만에 읽고 개조할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "왜 상태 유지 셸도, 커스텀 도구도 다 버렸는가"
            </h3>
            <p>
              프런티어 언어모델의 추론 능력이 급상승하면서, 과거 에이전트 성능을 끌어올리던 복잡한 툴 스캐폴딩은 오히려 모델의 추론 자유도를 가두고 학습/평가 간 괴리(overfitting)를 낳는 족쇄로 변했다. <code>mini-swe-agent</code>는 <strong>"모델을 중심에 두고 하네스는 투명한 유리판처럼 사라져야 한다"</strong>는 철학을 끝까지 밀어붙였다.
            </p>

            <div class="editorial-quote">
              <p>
                "<strong>Bash 외에는 어떠한 도구도 없다.</strong> 심지어 LM의 Tool-Calling 인터페이스조차 필요 없다. 모든 행동은 상태가 없는 <code>subprocess.run</code>으로 독립 실행되고, 기록은 완전히 선형(Linear)이다. 궤적(trajectory)과 모델에 넘기는 메시지 배열 사이에 어떠한 왜곡도 없다."
              </p>
              <small>— SWE-agent / mini-swe-agent 설계 선언문 &amp; v2 아키텍처 문서 (★10,142 · MIT)</small>
            </div>

            <p>
              실제로 데이터커브(Datacurve)의 DeepSWE 평가 하네스에서 <code>mini-swe-agent</code> 기반 구성은 무거운 상용 하네스를 갖춘 Claude Code와 Codex보다 높은 점수를 기록했고, SWE-bench Verified에서도 <strong>74%를 상회</strong>하는 성적을 냈다. 개발자가 "PR을 올려줘" 같은 새 기능을 원할 때도 에이전트 코드를 고치는 대신 그냥 셸에서 <code>gh</code>를 쓰라고 말로 지시하면 그만이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 100줄 코어·Stateless Subprocess·다중 샌드박스 추상화
            </h3>
            <p>
              <code>src/minisweagent/agents/default.py</code>를 열어보면 상용 에이전트에서 흔히 보이는 겹겹의 플래너·메모리 매니저·툴 라우터가 단 하나도 없다. 대신 세 가지 극도로 단순한 원칙이 맞물려 작동한다:
            </p>
            <ul>
              <li><strong>Tool-Calling API 비의존 &amp; 순수 선형 히스토리:</strong> 모델이 정해진 포맷으로 bash 명령을 출력하면 <code>DefaultAgent</code>가 이를 실행해 출력을 다음 user 메시지로 그대로 이어 붙인다. Tool-Calling JSON 스키마를 지원하지 않는 오픈웨이트 모델이나 실험용 로컬 모델도 아무런 어댑터 없이 즉시 투입할 수 있으며, <code>trajectory == messages</code> 구조 덕분에 SFT·강화학습(RL) 데이터로 1:1 직결된다.</li>
              <li><strong>상태 없는(Stateless) 독립 <code>subprocess.run</code> 실행:</strong> 수많은 에이전트가 대화형 PTY 세션을 열어두고 <code>cd</code> 상태나 백그라운드 프로세스 꼬임으로 멈춰 버리는 반면, <code>mini</code>는 매 명령을 완전히 독립된 단발 프로세스로 실행한다. 그 덕분에 <code>subprocess.run</code> 한 줄만 <code>docker exec</code>로 갈아 끼우면 <strong>Local, Docker/Podman, Singularity/Apptainer, Bubblewrap, Contree, Modal</strong> 등 어떤 샌드박스로도 1초 만에 이식된다.</li>
              <li><strong>비용·스텝·월클록 하드 가드레일과 ProgramBench:</strong> <code>AgentConfig</code>(Pydantic)는 <code>step_limit</code>, <code>cost_limit</code>(기본 $3.0), <code>wall_time_limit_seconds</code>, 연속 포맷 에러 상한을 내장해 무한 폭주를 막으며, <code>litellm</code>·OpenRouter·Portkey 및 <code>/responses</code> 엔드포인트·interleaved thinking까지 모두 호환한다. 최근에는 초고난도 신규 벤치마크 <code>ProgramBench</code> 실행기까지 통합했다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">mini-swe-agent v2 초경량 무상태(Stateless) 코딩 에이전트 루프</span>
                <span class="schematic-badge">~100 Lines Python · Bash-Only · Linear Trajectory</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Linear Message Loop</div>
                  <div class="schematic-desc">
                    Jinja2 <code>StrictUndefined</code> 프롬프트 렌더링<br>
                    Tool-Calling JSON 스키마 <strong>불필요</strong><br>
                    <code>trajectory == messages</code> 1:1 일치<br>
                    LiteLLM / OpenRouter / 로컬 모델 전수 지원
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Stateless Bash Execution</div>
                  <div class="schematic-desc">
                    오직 1개 도구: <strong>Bash</strong> (<code>subprocess.run</code>)<br>
                    상태 유지 셸(PTY) 행(Hang)·꼬임 원천 차단<br>
                    명령 단위 독립 실행 &rarr; <code>docker exec</code> 즉시 치환<br>
                    SWE-bench Verified <strong>&gt;74%</strong> 달성
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Pluggable Sandboxes &amp; RL</div>
                  <div class="schematic-desc">
                    Local / Docker / Podman / Bubblewrap<br>
                    Singularity / Apptainer / Contree / Modal<br>
                    <code>cost_limit</code> · <code>step_limit</code> 안전 차단기<br>
                    SFT·RL 훈련 및 ProgramBench 표준 하네스
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">mini-swe-agent.com 공식 문서 실화면 — v2.4.6 아키텍처·7대 샌드박스·벤치마크 스펙</span>
              </div>
              <img src="../assets/images/demo_mini_swe_agent.png" alt="mini-swe-agent Official v2 Documentation and Architecture Overview" class="showcase-img">
              <p class="showcase-caption">
                ▲ mini-swe-agent.com/latest/ 실화면: 100줄 파이썬 코어, Meta·NVIDIA·Stanford 등 채택 현황, SWE-bench Verified 74%+ 성과 및 다중 샌드박스 환경 구성.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 &amp; 연구 분기점: '더 똑똑한 프롬프트'보다 '더 얇은 하네스'가 이기는 이유
            </h3>
            <p>
              수많은 AI 스타트업들이 독자적인 에이전트 오케스트레이션 프레임워크와 화려한 툴 체인을 자사의 '기술 해자(Moat)'라고 주장해 왔다. 그러나 <code>mini-swe-agent</code>의 성공은 불편한 진실을 증명한다—기반 모델이 강해질수록 개발자가 덧붙인 복잡한 툴 추상화는 오히려 모델이 리눅스 셸을 자유롭게 부리는 능력을 방해하거나 특정 하네스에 과적합된 취약한 결과물만 양산한다는 것이다.
            </p>
            <ul>
              <li><strong>RL·파인튜닝 표준 베이스라인의 통일:</strong> AI 연구실들이 모델을 훈련할 때 거대한 모노레포 하네스에 종속되면 다음 세대 모델에 결과를 재사용할 수 없다. <code>mini-swe-agent</code>는 스캐폴드 편향을 '제로'에 가깝게 낮춤으로써 순수 모델 지능과 RL 정책의 효과를 측정하는 표준 자로 자리매김했다.</li>
              <li><strong>해킹 가능한(Hackable) 일상 CLI로의 복귀:</strong> 블랙박스 상용 코딩 에이전트의 불투명한 시스템 프롬프트와 요금 체계에 지친 엔지니어에게, 단 100줄짜리 코어를 통째로 이해하고 자신만의 가드레일과 로컬 모델 라우팅을 심을 수 있는 해방구를 제공한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 강력한 도구는 이미 50년 전부터 <code>/bin/bash</code>에 있었다
            </h3>
            <p>
              AI 에이전트를 위해 수십 개의 새로운 JSON 파일 편집 API를 발명할 필요가 있었을까? <code>mini-swe-agent</code>는 유닉스 파이프와 <code>grep</code>, <code>sed</code>, <code>git</code>이라는 50년 묵은 도구가 최신 언어모델의 손에 쥐어졌을 때 얼마나 파괴적인지를 보여준다.
            </p>
            <p>
              프레임워크가 복잡해질수록 버그는 프레임워크에서 나오고, 프레임워크가 100줄로 줄어들면 남는 것은 순수한 모델의 실력뿐이다. 오늘날 AI 엔지니어링의 진짜 경쟁력은 코드를 더하는 것이 아니라, 어디까지 과감히 지울 수 있는가에 달려 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=mini-swe-agent+swe-bench+bash+only+ai+agent" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://mini-swe-agent.com/latest/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 공식 문서 &amp; 리더보드
              </a>
              <a href="https://github.com/SWE-agent/mini-swe-agent" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
