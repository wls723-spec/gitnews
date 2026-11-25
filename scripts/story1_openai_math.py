# -*- coding: utf-8 -*-
# Story 1: openai/math (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] openai/math : COVER STORY                         -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openai_math.jpg" alt="OpenAI Math Matrix Multiplication Exponent 9/4 and Lean 4 Formal Proofs Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER STORY #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">📐 HN 1,007점·554댓글 · ω = 9/4 증명 &amp; Lean 4 수학 대폭발</span>
              <span class="platform-tag">Hacker News #1 &amp; Formal Math</span>
              <span class="platform-tag">openai / math</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"60년 난제 '행렬 곱셈 지수 ω = 9/4'가 GitHub PR 한 건으로 풀렸다" — AI 형식 증명의 밤</span>
            </h2>

            <div class="article-subheadline">
              보도자료도, 학회 엠바고도 없이 GitHub PR(#6)로 올라온 OpenAI 내부 모델의 수학 논문 730편 — ω = 9/4 일치 하한과 VP ≠ VNP·FFT 하한에 더해, Anthropic의 리만 가설 Lean 4 압축(7.6만 줄)과 Google Cogentic까지 같은 날 쏟아진 컴퓨터과학 대격변 (★18,316 · Apache-2.0)
            </div>
            <p class="article-snippet">
              간밤 전 세계 수학자와 컴퓨터과학자들은 언론 보도자료가 아니라 <strong>GitHub PR 알림</strong>을 보고 잠에서 깼습니다. <strong>openai/math</strong>(★18,316 · 375개 패밀리 · 730편 원고)가 업데이트되면서 1969년 슈트라센 이후 반세기를 끌어온 행렬 곱셈 지수가 모든 체(Field) 위에서 정확히 <strong>ω = 9/4 (2.25)</strong>임을 보이는 일치 하한과 Lean 4 형식 증명이 공개됐고(HN <strong>1,007점·댓글 554개</strong>), <code>VP ≠ VNP</code>, 다항식 히르슈 반례, FFT 회로 하한까지 연달아 투하됐습니다. 같은 날 저명 복잡도 이론가 스콧 애런슨의 <em>"Holy shit"</em> 탄성(HN <strong>703점</strong>), Anthropic의 일반화 리만 가설 Lean 4 압축(<code>grh-lean</code>, 1,700만 줄 → <strong>7.6만 줄</strong>), 구글 리서치의 <code>Cogentic</code> 논문 공개(<strong>416점</strong>)까지 겹치며 오픈소스 저장소가 인류 수학의 최전선으로 변모했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 보도자료가 사라진 자리, GitHub 커밋으로 쏟아진 난제들
            </h3>
            <p>
              2026년 11월 24일 밤에서 25일 새벽 사이, 학계와 오픈소스 커뮤니티의 타임라인을 뒤흔든 건 화려한 키노트 무대가 아니었다. <code>openai/math</code> 저장소에 조용히 머지된 풀 리퀘스트 <code>#5</code>(<code>VP != VNP</code>)와 <code>#6</code>(11월 24일 논문·Lean 형식화 묶음), 그리고 <code>lsernau/grh-lean</code>과 <code>google-research/cogentic_research_papers</code>의 연속 커밋이었다. 텍사스 대학교 오스틴 캠퍼스의 양자컴퓨팅·복잡도 이론가 스콧 애런슨(Scott Aaronson)은 동료들과 저녁 식사를 하던 중 쏟아지는 저장소 업데이트를 보고 결국 자신의 블로그 <em>Shtetl-Optimized</em>에 <em>"내가 지금 무슨 일이 벌어지고 있는지 제대로 설명할 제목을 못 찾겠다"</em>며 연신 감탄사를 내뱉는 글을 올렸다.
            </p>
            <p>
              그가 저녁 디저트를 먹기도 전에 타임라인에 뜬 결과는 반세기 넘게 알고리즘 이론의 성배로 불리던 문제였다. 1969년 폴커 슈트라센(Volker Strassen)이 <i>O</i>(<i>n</i><sup>3</sup>) 벽을 깨고 <strong>ω ≤ log<sub>2</sub> 7 ≈ 2.807</strong>을 보인 이래 수많은 수학자들이 ω = 2일 것이라 믿어 왔던 정사각 행렬 곱셈의 지수 ω가, <strong>모든 체(Field) 위에서 정확히 9/4 = 2.25</strong>라는 논문(<em>The matrix multiplication exponent is nine fourths</em>)과 Lean 4 형식화 코드가 <code>openai/math</code>에 올라온 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '상한(Upper Bound)'을 넘어 '하한(Lower Bound)'과 '기계 검증'으로
            </h3>
            <p>
              이번 사건이 단순한 AI 벤치마크 기록 경신이 아니라 인류 지식 생산 방식의 패러다임 전환인 이유는 두 가지다. 첫째, 알고리즘을 하나 더 깎아 상한을 낮추는 것이 아니라 <strong>"어떠한 회로로도 이보다 빠르게 계산할 수 없다"는 비선형 하한(ω ≥ 9/4 및 FFT Ω(<i>N</i> (log <i>N</i>)<sup>1/2</sup>))을 증명</strong>했다는 점이다. 둘째, 인간 수학자가 수만 페이지를 일일이 검산할 수 없는 초고밀도 증명을 <strong>Lean 4 형식 검증기(Type Checker)</strong>와 함께 GitHub에 오픈소스 데이터로 방출하는 경쟁이 시작됐다는 점이다.
            </p>

            <div class="editorial-quote">
              <p>
                "마치 레벤후크가 연못물에 현미경을 처음 들이대거나 갈릴레오가 별을 향해 망원경을 겨눈 순간 같다. OpenAI와 Anthropic이 이제는 보도자료조차 내지 않고 밤새 GitHub 저장소에 파일들을 올리고 있다. <strong>고대부터 이어져 온 복잡도 이론의 질문들이 실마리를 조금씩 흘리는 수준을 넘어, 이제는 곧장 답을 얻고 있다.</strong>"
              </p>
              <small>— 스콧 애런슨(Scott Aaronson), <em>Shtetl-Optimized</em> 포스트 (HN 703점·532댓글)</small>
            </div>

            <p>
              같은 시각 <code>google-research/google-research</code>는 <code>cogentic_research_papers</code> 디렉터리를 통해 기존 LLM들이 중앙 오케스트레이터와 중간 증명 데이터베이스를 공유하며 정수 인수분해(<code>integer_factorization</code>), 이산 로그(<code>discrete_logarithm</code>), 로그-랭크 추측(<code>logrank_conjecture</code>)을 공략한 논문군을 공개했고(HN <strong>416점·317댓글</strong>), Anthropic 측 연구자(<code>lsernau/grh-lean</code>)는 앞서 공개됐던 약 1,700만 줄 규모의 일반화 리만 가설(GRH) Lean 4 증명을 Claude와 협업해 <strong>가독성 에디션 30만 줄, 압축 에디션 7.6만 줄(99.56% 축소)</strong>로 정제한 저장소를 <code>Apache-2.0</code>으로 배포했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 텐서 기하학 하한에서 Lean 4 공리 검증(`PrintAxioms`)까지
            </h3>
            <p>
              <code>openai/math</code> 저장소가 375개 패밀리, 730개 원고를 다루며 신뢰성을 확보하는 구조는 전통적 논문 출판과 달리 <strong>라텍스(LaTeX) 원고—동반 기하 프레임워크—Lean 4 커널 검증</strong>의 3단 파이프라인으로 맞물려 있다:
            </p>
            <ul>
              <li><strong>기하 경계 랭크와 비스칼라 게이트 하한:</strong> 행렬 곱셈 원고는 모든 변 길이 <i>n</i> ≥ 2에서 형식 다항식 항등식을 계산하는 나눗셈 없는 산술 회로가 최소 ⌈<i>n</i><sup>9/4</sup> / 2⌉개의 비스칼라 곱셈·나눗셈 게이트를 요구함을 보인다. 동반 논문(<em>Euclidean geometry in the asymptotic spectrum of tensors</em>)이 텐서의 점근 스펙트럼 기하 구조를 제공하고, 이를 바탕으로 ω(<i>F</i>; 1, 1, 1) = 9/4 및 쌍대 지수 α(<i>F</i>) = 1/2를 도출한다.</li>
              <li><strong>Lean 4 형식화와 <code>ExactExponent.lean</code>:</strong> <code>lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean</code>의 정리 <code>square_exponent</code>와 <code>dual_exponent</code>는 임의의 체 <code>[Field F]</code>에 대해 <code>formalOmega F 1 1 1 = 9 / 4</code>를 타입 시스템 수준에서 컴파일한다. 대용량 메모리 매핑(<code>vm.max_map_count</code>) 한계를 피하기 위해 모듈 단위 부분 컴파일과 <code>ComparatorChallenges</code> 인터페이스로 명제 정의(Spec)와 증명(Proof)의 동일성을 외부에서 감사하게 만든다.</li>
              <li><strong>최소 공리 기반 99.5% 증명 압축 (<code>grh-lean</code>):</strong> <code>lsernau/grh-lean</code>은 Lean v4.35.0과 Mathlib 위에서 오직 표준 3대 공리(<code>propext</code>, <code>Classical.choice</code>, <code>Quot.sound</code>)만 사용했음을 <code>scripts/PrintAxioms.lean</code>으로 검증하며 1,700만 줄의 AI 기계 생성 증명을 76,000줄까지 압축해 인간 수학자의 감사 가능성을 높였다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">AI 자율 수학 연구 &amp; Lean 4 오픈소스 검증 아키텍처</span>
                <span class="schematic-badge">730 Manuscripts · Lean 4 Type Checker · Apache-2.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Open Research Synthesis</div>
                  <div class="schematic-desc">
                    내부 추론 모델 / <code>Cogentic</code> 하네스<br>
                    중간 증명 DB + 텐서 스펙트럼 프레임워크<br>
                    730편 원고(LaTeX + BibTeX) 자동 생성<br>
                    <code>ω = 9/4</code>, <code>VP ≠ VNP</code>, Hirsch 반례 도출
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Lean 4 Kernel &amp; Comparator</div>
                  <div class="schematic-desc">
                    <code>ExactExponent.lean</code> · <code>grh-compact</code><br>
                    표준 3대 공리(<code>propext</code> 등) 외 <code>sorry</code> 차단<br>
                    <code>ComparatorChallenges</code>로 명제 왜곡 감사<br>
                    1,700만 줄 → 7.6만 줄 증명 압축
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. GitHub Raw Data Release</div>
                  <div class="schematic-desc">
                    동료 심사 전 GitHub PR로 원시 데이터 공개<br>
                    누구나 <code>lake build</code>로 독립 재검증<br>
                    비형식 원고 오류는 커뮤니티 PR/이슈로 수정<br>
                    학계 우선권·크레딧은 커뮤니티에 전권 위임
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">openai/math 저장소 실화면 — ω = 9/4 원고 빌드 구조 및 Lean 4 형식화 연결 링크</span>
              </div>
              <img src="../assets/images/demo_openai_math.png" alt="OpenAI Math Matrix Multiplication Exponent 9/4 Preprint Repository" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/openai/math 실화면: 11월 24일 에디션 'The matrix multiplication exponent is nine fourths'의 LaTeX 소스(main.tex), PDF, 그리고 ExactExponent.lean 형식 증명 링크가 공개되어 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 학계 권위와 저널리즘의 분기점: "동료 심사는 누가, 어떻게 감당할 것인가"
            </h3>
            <p>
              수백 년 동안 수학계의 게이트키퍼는 저널과 소수 석학의 6개월~3년짜리 동료 심사(Peer Review)였다. 그러나 한 프론티어 연구소가 하룻밤에 375개 분야의 원고 730편을 GitHub에 올리고, 아직 Lean 형식화가 끝나지 않은 비검증 원고와 기계 검증만 통과한 수십만 줄의 Lean 파일이 동시에 쏟아지는 순간 기존의 저널 제도는 사실상 기능 정지에 빠진다.
            </p>
            <ul>
              <li><strong>'정의의 정확성(Spec Audit)'이라는 새로운 병목:</strong> 해커뉴스 554개 댓글에서도 가장 치열했던 쟁점은 <em>"Lean 컴파일러가 증명의 논리적 무결성을 보장하더라도, 애초에 Lean으로 번역된 정리의 정의(<code>formalOmega</code>, <code>VP</code>, <code>GRH</code>)가 수학계가 뜻하는 진짜 명제와 일치하는가?"</em>였다. 컴파일은 통과했지만 정의가 미묘하게 다르다면 헛수고이기 때문이다. 바로 이 때문에 OpenAI는 <code>ComparatorChallenges</code>를 두고, Anthropic은 <code>grh-compact</code>(7.6만 줄)와 <code>GUIDE.md</code>를 따로 내놓아 인간 수학자의 '명제 정의 감사' 비용을 낮추는 데 사활을 걸고 있다.</li>
              <li><strong>Apache-2.0 오픈소스 라이선스와 공개 경쟁:</strong> 주요 AI 랩들이 특허나 비공개 논문 대신 Apache-2.0 코드와 LaTeX 소스를 통째로 GitHub에 푸시하는 현상은 연구 우선권(Priority) 선점 전쟁이 곧 '누가 더 빠르게 형식 검증 가능한 공개 아티팩트를 내놓는가'로 이동했음을 뜻한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 수학의 언어가 종이에서 타입 체커로 옮겨간 밤
            </h3>
            <p>
              물론 <code>openai/math</code>의 모든 원고가 당장 완벽한 것은 아니다. OpenAI 스스로도 README에 <em>"비형식화된 일부 결과에는 오류가 있을 수 있으며 이는 정제된 학술 논문이 아니라 원시 연구 데이터(raw research data)로 보아야 한다"</em>고 적었고, <code>lsernau/grh-lean</code> 역시 <em>"아직 어떤 인간 수학자도 끝까지 읽어보지 않았고 기계 검사만 통과했다"</em>고 명시했다.
            </p>
            <p>
              그럼에도 돌이킬 수 없는 문턱은 이미 넘어섰다. 반세기 동안 'ω = 2일 것'이라 막연히 믿어온 교과서가 단 하나의 커밋으로 흔들리고, 1,700만 줄의 기계 증명이 하루 만에 7.6만 줄로 정제되는 시대—이제 수학적 진실을 가리는 최전선은 학회 강당이 아니라 <code>git pull</code>과 <code>lake build</code>가 돌아가는 개발자의 터미널 위에 놓여 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=openai+math+matrix+multiplication+9+4+lean+4" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/openai/math" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
