# -*- coding: utf-8 -*-
# Story 5: bendlang/bend

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] bendlang/bend                                    -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_bend.jpg" alt="Bend 2 Proof-Verified AI Programming Language Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;fill:#fff;"></i> PROOF-BLOCKED AI</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#e0e7ff; border-color:#4338ca; color:#312e81;">📐 수학적 증명으로 AI 버그를 막는 언어</span>
              <span class="platform-tag">GitHub Trending &amp; bend-lang.com</span>
              <span class="platform-tag">bendlang / bend</span>
            </div>

            <h2 class="article-headline">
              인간이 AI 코드를 일일이 읽지 않고도 신뢰하는 법: 컴파일러가 수학 증명으로 실수를 봉쇄하는 'Bend 2'
            </h2>

            <div class="article-subheadline">
              핵심 불변 규칙을 선언한 <code>LAWS.bend</code>와 Lean 검증 커널(<code>--verdict</code>)로 AI의 버그 병합을 원천 차단하고, 단일 코드가 CPU부터 1만 개 GPU 코어까지 자동 병렬 실행되는 Apache-2.0 언어 (+127스타/일, 누적 25,609스타)
            </div>
            <p class="article-snippet">
              "클로드, 보드 가장자리를 통과해 반대편으로 워프하도록 고쳐줘." AI가 기분 좋게 코드를 고쳐 놓았지만, 몰래 '승리 불가'라는 핵심 게임 규칙을 깨뜨렸다면 어떨까요? 오늘 127스타를 보태며 누적 25,609스타를 기록한 빅토르 타엘린(Victor Taelin) 팀의 <strong>bendlang/bend</strong>(Bend 2)는 인간이 수천 줄의 AI 코드를 리뷰하는 대신, <code>LAWS.bend</code>에 절대 깨지면 안 되는 법칙을 적어두고 컴파일러가 수학적 증명(<code>PROOF.bend</code>) 없이는 빌드를 거부하게 만드는 대담한 포스트-AGI 프로그래밍 언어입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 벽을 통과하려던 AI 에이전트, 컴파일러 앞에서 멈춰 서다
            </h3>
            <p>
              Bend 2의 데모 시연에는 섬뜩할 만큼 직관적인 게임 화면이 등장한다. 규칙은 단 하나, <em>"이 게임에서 승리(깃발 도달)는 수학적으로 불가능하다(<code>you_cant_win</code>)."</em> 이제 AI 에이전트에게 새 기능을 주문한다. <em>"맵의 좌우 가장자리를 감싸서 반대편으로 이동하게 만들어줘."</em>
            </p>
            <p>
              기존 언어(Python이나 TypeScript)였다면 AI는 순식간에 좌표 래핑(Wrap-around) 코드를 짰을 것이고, 미처 막지 못한 구석 틈새로 캐릭터가 빠져나가 깃발을 밟는 치명적 버그가 그대로 머지(Merge)됐을 것이다. 하지만 <strong>bendlang/bend</strong> 위에서 <code>LAWS.bend</code>가 작동하자 AI는 빌드를 통과하지 못한다. 어떤 이동 시퀀스(<code>moves: List&lt;Game.Move&gt;</code>)를 넣어도 <code>Game.is_won(board) == False</code>가 성립한다는 수학적 증명을 <code>PROOF.bend</code>에 제출할 수 없었기 때문이다. 결국 AI는 스스로 코드를 고쳐 반대쪽 가장자리에 벽을 세우고, 증명을 완성한 뒤에야 컴파일러의 문을 통과했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "<code>LAWS.bend</code>는 수학적 증명이 강제하는 <code>AGENTS.md</code>다"
            </h3>
            <p>
              바이브코딩이 확산되면서 개발 업계의 최대 난제는 '작성 속도'가 아니라 '검증 비용'으로 옮겨갔다. 린트와 단위 테스트는 개발자가 미처 상상하지 못한 엣지 케이스를 막아주지 못한다. 반면 Isabelle, Agda, Lean, Rocq 같은 기존 정형 검증(Formal Verification) 증명 보조기들은 체커가 수 분씩 걸리고 문법이 지나치게 난해해 실무 웹·백엔드 앱에 쓰기 어려웠다. Bend 2는 바로 이 간극을 겨냥해 <strong>"파이썬처럼 쓰되 의존 타입으로 증명하고, C와 CUDA 속도로 달리는 언어"</strong>를 선언했다.
            </p>

            <div class="editorial-quote">
              <p>
                "포스트-AGI 경제에서 인간은 결국 코드를 직접 쓰고 읽는 일을 멈출 것이다. 하지만 AI에게 우리의 의도를 모호함 없이 전달할 언어는 여전히 필요하다. <strong><code>LAWS.bend</code>는 수학적 증명이 뒷받침하는 <code>AGENTS.md</code>다.</strong>"
              </p>
              <small>— Victor Taelin / bendlang/bend 공식 선언문 (Apache-2.0)</small>
            </div>

            <p>
              "모든 잔액의 합은 항상 0이어야 한다", "배열은 절대 경계 밖을 참조하지 않는다" 같은 비즈니스 불변식(Invariant)을 <code>LAWS.bend</code>에 선언하고 <code>AGENTS.md</code>에 <code>bend PROOF.bend</code> 실행을 지시하면, AI가 아무리 교묘하게 코드를 뜯어고쳐도 법칙을 깨뜨리는 순간 컴파일 자체가 수학적으로 불가능해진다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 아핀 의존 타입 이론(BendTT)과 1만 코어 자동 GPU 병렬화
            </h3>
            <p>
              Bend 2는 구버전(HVM 기반 Bend 1)을 완전히 새로 갈아엎고 두 개의 논문(<em>BendTT</em>와 <em>BendRT</em>)에 기반한 새로운 컴파일러 스택을 구축했다:
            </p>
            <ul>
              <li><strong>아핀 의존 타입 &amp; 초고속 증명 체커 (<code>BendTT</code> + <code>bendtt.lean</code>):</strong> 모든 타입을 명시하고 클로저·배열 공유를 차단하는 아핀(Affine) 선형성과 순수성을 채택해, Isabelle·Agda·Lean·Rocq 대비 몇 자릿수(OOM) 빠른 1초 미만의 증명 검증을 목표로 한다. 또한 컴파일러 본체의 버그 가능성을 차단하기 위해 <code>--verdict</code> 옵션은 Lean으로 정형 검증된 신뢰 커널(<code>bendtt.lean</code>)을 통해 최종 증명을 교차 검증한다.</li>
              <li><strong>스레드·락 없는 GPU 자동 병렬화 (<code>!</code> 연산자):</strong> 개발자가 CUDA 커널이나 뮤텍스를 한 줄도 짤 필요 없이, 분할 정복 재귀 호출에 <code>pow2!(20n)</code>처럼 느낌표(<code>!</code>) 하나만 붙이면 작업 트리를 수만 개의 GPU 코어로 쪼개어 실행한 뒤 합친다.</li>
              <li><strong>멀티 타깃 네이티브 컴파일 &amp; 샌드박스:</strong> C(단일 코어 수작업 C와 맞먹는 속도), Metal(Apple Silicon), CUDA, JavaScript 타깃으로 컴파일되며, 공식 CLI 바이너리 <code>bend</code>는 신뢰할 수 없는 프로젝트의 <code>bunfig.toml</code>과 <code>.env</code> 로딩을 차단해 보안성까지 챙겼다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Bend 2 정형 증명 게이트 및 CPU/GPU 자동 병렬 실행 파이프라인</span>
                <span class="schematic-badge">Apache-2.0 · BendTT + Lean Kernel + BendRT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Intent &amp; Invariant Laws</div>
                  <div class="schematic-desc">
                    <code>LAWS.bend</code> 불변 법칙 선언<br>
                    AI 에이전트가 코드 + <code>PROOF.bend</code> 작성<br>
                    아핀 의존 타입(Python 유사 문법)<br>
                    종료성 검사(Termination Check) 강제
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Fast Proof &amp; Lean Verdict</div>
                  <div class="schematic-desc">
                    <code>bend PROOF.bend</code> 초고속 체커 실행<br>
                    <code>--verdict</code>: Lean 증명 커널 검증<br>
                    법칙 위배 시 컴파일 물리적 차단<br>
                    <strong>AI 환각·회귀 버그 원천 봉쇄</strong>
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. BendRT Parallel Compile</div>
                  <div class="schematic-desc">
                    분할 정복(<code>pow2!(20n)</code>) 무락 병렬화<br>
                    CPU: C-속도 네이티브(Clang 19+)<br>
                    GPU: CUDA 12 / Apple Metal 통합 메모리<br>
                    빠른 프로토타이핑용 JS 타깃 병행 지원
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Bend 2 공식 웹사이트 &amp; 인터랙티브 PROOF.bend 랩</span>
              </div>
              <img src="../assets/images/demo_bend.png" alt="Bend 2 Official Website Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ bend-lang.com 공식 사이트 실화면: 벤치마크 비교(CPU/GPU 런타임·증명 체커 속도)와 브라우저에서 직접 <code>LAWS.bend</code> 법칙을 깨뜨려 볼 수 있는 인터랙티브 데모(#lab)를 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업적 파장: "인간 친화적 문법"의 종말과 "검증 기계 친화적 언어"의 부상
            </h3>
            <p>
              지난 50년간 프로그래밍 언어는 인간이 타이핑을 덜 치고 편하게 읽을 수 있도록 추론(Inference)과 동적 타이핑, 암묵적 편의성을 늘리는 방향으로 발전해 왔다. Bend 2는 이 역사를 정면으로 거스른다. 타입 추론도 없고, <code>if-then-else</code> 문법 설탕도 없으며, 타입 어노테이션이 장황하다.
            </p>
            <ul>
              <li><strong>솔직한 한계와 실용적 타협:</strong> 현재 U64/F64 미지원, F32 부동소수점 증명 불가, 문자열 연결 리스트 성능 한계, TLS/HTTP 기본 라이브러리 부재, 컴파일러 본체의 99% AI 작성 등 초기 단계의 제약을 가감 없이 공개하면서도, 핵심 안전성만큼은 Lean 정형 커널(<code>--verdict</code>)로 분리해 신뢰성을 확보했다.</li>
              <li><strong>AI 시대의 새 패러다임:</strong> 코드를 치는 주체가 인간에서 AI로 넘어간다면, 언어는 인간이 덜 타이핑하게 해주는 도구가 아니라 <strong>"AI가 거짓말을 못 하게 가두는 수학적 우리(Cage)"</strong>가 되어야 한다는 선언이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 리뷰하지 마라, 증명하게 하라
            </h3>
            <p>
              AI가 하루에 10만 줄의 코드를 생산하는 시대에, 인간 엔지니어가 눈을 부릅뜨고 PR을 한 줄씩 읽는 시대는 이미 한계를 맞았다.
            </p>
            <p>
              Bend 2는 아직 거칠고 젊은 실험 언어다. 그러나 "프롬프트로 지시하고 테스트로 기도하는" 오늘의 AI 코딩을 넘어, 수학적 법칙을 통과하지 못한 코드는 세상에 태어날 수조차 없는 내일의 소프트웨어 공학을 가장 선명하게 앞당겨 보여주고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Bend+programming+language+Victor+Taelin+proofs" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://bend-lang.com/#lab" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> Bend 2 인터랙티브 랩
              </a>
              <a href="https://github.com/bendlang/bend" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
