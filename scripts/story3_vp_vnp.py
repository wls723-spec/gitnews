# -*- coding: utf-8 -*-
# Story 3: anthropics/formal-math (vp-vnp)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] anthropics/formal-math (vp-vnp)                  -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_vp_vnp.jpg" alt="Anthropic Formal Math VP != VNP Lean 4 Proof Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sigma" style="width:12px;height:12px;fill:#fff;"></i> AI FORMAL MATH</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ede9fe; border-color:#7c3aed; color:#5b21b6;">🧮 클로드가 직접 증명하고 Lean 4가 기계 검증한 대수적 P≠NP(VP≠VNP) · HN 72.5점/h</span>
              <span class="platform-tag">Hacker News Rising &amp; Lean 4</span>
              <span class="platform-tag">anthropics / formal-math (vp-vnp)</span>
            </div>

            <h2 class="article-headline">
              "AI가 발견한 미해결 복잡도 분리를 인간 대신 Lean 4 커널이 심판하다" — 앤스로픽이 공개한 '모든 체 위에서의 VP ≠ VNP' 형식 증명
            </h2>

            <div class="article-subheadline">
              내부 연구용 Claude 모델이 발리언트의 대수적 P vs NP 문제(VP ≠ VNP 및 VP-closure 분리)의 초다항식 회로 하한을 도출·논문화하고, sorry 없는 Lean 4 + Mathlib + Palomar 독립 커널(nanoda) 검증까지 완수 (Apache-2.0, ★527)
            </div>
            <p class="article-snippet">
              AI가 수학 경시대회 문제를 푸는 단계를 넘어, 50년 난제인 P vs NP의 대수적 대응물 <strong>VP ≠ VNP(모든 체 F 위에서 성립)</strong>에 대한 새로운 초다항식 하한 증명과 Lean 4 형식화 코드가 오늘 <code>anthropics/formal-math/vp-vnp</code> 저장소에 공개되며 해커뉴스에서 <strong>시간당 72.5점(45점/0.6h)</strong>의 폭발적 반응을 일으키고 있습니다. 해밀턴 사이클 다항식과 표수 2 이외의 퍼머넌트(Permanent)가 <code>m^(c·(log m)^(1/3))</code>개 이상의 산술 회로 게이트를 필요로 함을 보인 이 결과는 논문과 형식 증명 모두 AI가 작성했으며, 인간 수학자의 검토 대신 <strong>독립 Lean 커널 <code>nanoda</code></strong>가 공리 위반 없이 기계 검증을 통과했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 인간 수학자가 아직 읽지 못한 증명을 '두 개의 독립 커널'이 먼저 승인했다
            </h3>
            <p>
              오늘 해커뉴스 개발자들과 이론 컴퓨터 과학자들이 일제히 클릭한 저장소 <code>anthropics/formal-math/vp-vnp</code>의 README 상단에는 이례적이면서도 섬뜩한 문장이 박혀 있다. <em>"이 결과는 내부 연구용 Claude 모델이 발견했다. 이 폴더에는 논문과 Lean 4 형식화가 들어 있다. 둘 다 AI 모델이 작성했으며, 인간 수학자는 아직 이 증명을 검증하지 않았다."</em>
            </p>
            <p>
              과거 LLM이 수학 정리를 "풀었다"고 주장할 때마다 학계는 환각(Hallucination)과 미묘한 논리적 비약, 은근슬쩍 숨긴 <code>sorry</code> 플레이스홀더를 의심해야 했다. 그러나 앤스로픽의 <code>formal-math</code> 저장소는 전혀 다른 규칙으로 작동한다. 앞선 리만 제타 영점(<code>zeta23</code>), 3SUM/APSP(<code>3sum-apsp</code>), 지수시간 가설 반증 시도(<code>eth</code>)에 이어 오늘 추가된 <code>vp-vnp/</code>는 <strong>"인간이 설득될 필요 없이, 수학의 최소 공리 3개만 허용한 형식 검증 샌드박스를 통과하라"</strong>는 냉혹한 기계 심판대 위에 올려졌다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "왜 VP ≠ VNP 형식화가 P vs NP 시대의 과학적 패러다임을 바꾸는가"
            </h3>
            <p>
              1979년 레슬리 발리언트(Leslie Valiant)가 정의한 <strong>VP vs VNP</strong>는 불리언 회로 기반의 P vs NP를 다항식과 산술 회로(덧셈·곱셈 게이트)의 세계로 옮긴 '대수적 P vs NP' 문제다. (주의: VP ≠ VNP가 곧바로 튜링 머신의 P ≠ NP를 해결하는 것은 아니며, 저장소 역시 이를 명확히 선 긋는다.) 핵심은 <strong>'해밀턴 사이클 다항식(<code>hc</code>)'과 '행렬의 퍼머넌트(<code>perm</code>)'가 다항식 크기(심지어 근사 회로 포함)의 산술 회로로 계산될 수 있는가</strong>다.
            </p>

            <div class="editorial-quote">
              <p>
                "모든 체(Field) 위에서 해밀턴 사이클 다항식과(표수 2를 제외한) 퍼머넌트는 충분히 큰 m에 대해 m^(c·(log m)^(1/3))개 이상의 게이트를 필요로 한다. <strong>근사 회로에 대해서도 동일하게 성립하므로 VP는 VNP의 진부분집합이며, VNP는 VP의 폐포(Closure)에도 포함되지 않는다.</strong>"
              </p>
              <small>— anthropics/formal-math/vp-vnp 공식 명세 (Apache-2.0 · Lean 4 + Palomar)</small>
            </div>

            <p>
              이 놀라운 주장이 학술지 동료 심사(Peer Review) 이전에 GitHub 커밋으로 던져졌을 때 가장 중요한 질문은 단 하나다: <em>"사기나 편법 없이 진짜 증명됐는가?"</em> 바로 이 지점에서 Lean 4 + Mathlib과 Palomar 레지스트리의 이중 검증 파이프라인이 인간 심사위원의 빈자리를 메운다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: <code>Statement.lean</code> → <code>Solution.lean</code> → <code>nanoda</code> 독립 커널 검증
            </h3>
            <p>
              <code>vp-vnp/</code> 디렉터리 구조를 열어보면, AI가 정의 자체를 유리하게 조작해 속이는 '스펙 해킹(Spec Hacking)'을 원천 봉쇄하는 영리한 3단계 검증 아키텍처가 드러난다:
            </p>
            <ul>
              <li><strong>Mathlib 단독 의존 명제 파일(<code>Statement.lean</code> &amp; <code>Challenge.lean</code>):</strong> <code>Computes</code>(산술 회로 게이트 정의), <code>perm</code>(m×m 행렬의 퍼머넌트), <code>hc</code>(단일 사이클 순열의 해밀턴 다항식), <code>VP</code>, <code>VPBar</code>(근사 폐포), <code>VNP</code>, <code>Separation</code> 정의는 오직 표준 Mathlib만 임포트해 기술된다. 증명 코드(<code>Solution.lean</code>)가 명제 정의에 끼어들 여지를 없앴다.</li>
              <li><strong>무(無)<code>sorry</code> 증명 및 공리 감사(<code>PrintAxioms.lean</code>):</strong> <code>lake build</code> 실행 시 <code>Challenge.lean</code>의 스텁 외에는 어떠한 <code>sorry</code>도 허용되지 않으며, <code>lake env lean scripts/PrintAxioms.lean</code>은 증명 전체가 오직 표준 수학 공리 3종(<code>propext</code>, <code>Classical.choice</code>, <code>Quot.sound</code>)만 사용했음을 감사한다.</li>
              <li><strong>이중 커널 + 샌드박스 비교(<code>comparator.json</code> + <code>nanoda</code>):</strong> Palomar 레지스트리의 <code>comparator-check.sh</code>는 <code>Challenge</code> 모듈과 <code>Solution.lean</code>의 5개 핵심 정리(<code>mainTheorem</code>, <code>mainTheoremApprox</code>, <code>separation</code>, <code>separationClosure</code>, <code>permanent_over_real</code>)의 타입 시그니처 일치를 대조한 뒤, Lean 기본 커널과 별개로 독립 작성된 타입 체커 <strong><code>nanoda</code></strong>와 <code>landrun</code> 샌드박스에서 <code>"Your solution is okay!"</code>를 받아야만 CI를 통과시킨다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Anthropic formal-math (vp-vnp) AI 정리 발견 → 이중 커널 형식 검증 파이프라인</span>
                <span class="schematic-badge">Lean 4 + Mathlib · Apache-2.0 · Zero sorry · nanoda Verified</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Trusted Spec (Mathlib Only)</div>
                  <div class="schematic-desc">
                    <code>Statement.lean</code>: <code>Computes</code>·<code>perm</code>·<code>hc</code><br>
                    발리언트 클래스 <code>VP</code> · <code>VPBar</code> · <code>VNP</code> 정의<br>
                    <code>Challenge.lean</code> 불변 목표 시그니처<br>
                    스펙 해킹 방지를 위해 Mathlib만 임포트
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. AI-Authored Proof &amp; Paper</div>
                  <div class="schematic-desc">
                    Claude 연구 모델이 정리 발견 및 <code>paper.pdf</code> 집필<br>
                    <code>Solution.lean</code> + <code>NS1</code>·<code>Nc</code>·<code>Ov</code> 모듈<br>
                    <code>m^(c·(log m)^(1/3))</code> 게이트 하한 &amp; 폐포 분리 증명<br>
                    <code>PrintAxioms</code>: 3대 표준 공리 외 사용 0건
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Palomar Independent Kernel</div>
                  <div class="schematic-desc">
                    <code>lean4export</code>로 증명 텀 직렬화<br>
                    독립 커널 <strong><code>nanoda</code></strong>로 교차 타입 체킹<br>
                    <code>landrun</code> 샌드박스 내 <code>comparator</code> 실행<br>
                    결과: <code>"Your solution is okay!"</code>
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">anthropics/formal-math/vp-vnp 저장소 실화면 — 논문 PDF·Lean 4 형식화 및 Palomar 검증 명세</span>
              </div>
              <img src="../assets/images/demo_vp_vnp.png" alt="Anthropic Formal Math VP != VNP Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/anthropics/formal-math/tree/main/vp-vnp 실화면: Claude 모델이 작성한 paper.pdf, Statement.lean, Solution.lean 모듈과 PrintAxioms·nanoda 커널 검증 절차가 담긴 연구 아티팩트.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 인식론적 전환점: "증명 검증은 기계가, 명제 해석은 인간이"
            </h3>
            <p>
              <code>vp-vnp</code> 저장소가 던지는 진짜 질문은 AI 연구실 간의 벤치마크 점수 경쟁을 훨씬 뛰어넘는다. README 자체가 정확히 짚어낸 마지막 구멍—<em>"Lean이 증명은 확인해 주지만, <code>Statement.lean</code>이 정말로 논문에서 주장하는 수학적 의미를 정확히 반영했는지는 기계가 검사해 주지 못한다"</em>—가 바로 미래 수학자의 역할이 될 것이기 때문이다.
            </p>
            <ul>
              <li><strong>형식화와 의미론적 틈(Semantic Gap):</strong> 만약 산술 회로(<code>Computes</code>)나 근사(<code>Approximates</code>) 정의에 미세한 버그가 있다면, 기계 커널은 그 잘못된 정의에 대해 100% 완벽한 증명을 통과시켜 버린다. 결국 인간 전문가는 수백 페이지의 증명 과정을 따라가는 대신 <code>Statement.lean</code>의 100줄짜리 정의가 표준 수학 직관과 일치하는지만 정밀 감사하면 되는 시대가 열렸다.</li>
              <li><strong>논문 출판 속도의 붕괴:</strong> 수년이 걸리던 난제 검증이 <code>git push</code>와 함께 <code>comparator-check.sh</code> CI 워크플로로 떨어지는 순간, 수학계와 AI 연구소의 권력 균형은 '가장 큰 연산 클러스터 + 형식 검증 루프'를 쥔 쪽으로 급격히 기울고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 인간이 아직 읽지 않은 정리가 이미 진실의 성적표를 받아 들었다
            </h3>
            <p>
              이제 학계 수학자들이 <code>paper.pdf</code>와 Appendix Q(정리-Lean 매핑 표)를 한 줄씩 검토하며 이 증명의 우아함과 정의의 정확성을 판가름할 것이다. 오류가 정의 속에 숨어 있을 수도 있고, 반대로 역사에 남을 돌파구일 수도 있다.
            </p>
            <p>
              확실한 것은 단 하나다. 인류가 수천 년간 '인간의 머리로 이해하고 고개를 끄덕이는 과정'으로만 정의해 왔던 수학적 발견의 최전선에, 이제는 차가운 샌드박스 커널의 <code>"Your solution is okay!"</code>라는 한 줄이 새로운 관문으로 들어섰다는 사실이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Anthropic+formal+math+Lean+4+VP+VNP" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/anthropics/formal-math/tree/main/vp-vnp" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
