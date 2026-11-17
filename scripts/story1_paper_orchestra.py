# -*- coding: utf-8 -*-
# Story 1: google-research/paper-orchestra (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] google-research/paper-orchestra : COVER STORY     -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_paper_orchestra.jpg" alt="Google Research PaperOrchestra Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🎻 구글 리서치 논문 자동 집필 오케스트라</span>
              <span class="platform-tag">GitHub Trending &amp; Google Cloud AI Research</span>
              <span class="platform-tag">google-research / paper-orchestra</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">아이디어 노트와 실험 로그만 던지면 학회 투고용 LaTeX 논문이 쏟아진다: 구글 리서치 'PaperOrchestra'</span>
            </h2>

            <div class="article-subheadline">
              아웃라인·문헌 조사·섹션 집필·플로팅 비평가 루프·내용 정제까지 5개 전문 에이전트를 지휘해 투고 직전 PDF까지 완성하는 Apache-2.0 오픈소스 프레임워크 (+1,175스타/일)
            </div>
            <p class="article-snippet">
              AI 연구자들이 실험을 끝내고도 CVPR이나 ICLR 마감에 맞춰 수십 페이지의 관련 연구 조사, 실험 그래프 플로팅, LaTeX 조판을 맞추느라 밤을 새우던 풍경이 뿌리부터 흔들리고 있습니다. 하루 만에 1,175스타를 끌어모으며 오늘 GitHub 전체 1위에 오른 <strong>google-research/paper-orchestra</strong>는 단편적인 아이디어 메모(<code>idea_sparse.md</code>)와 실험 로그(<code>experimental_log.md</code>)를 입력받아 다섯 개의 전문 에이전트가 교향악단처럼 협업하며 학회 템플릿 맞춤형 원고와 시각 자료를 생성합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 실험은 끝났는데 논문이 나오지 않는 '라스트 마일'의 병목
            </h3>
            <p>
              머신러닝 연구실에서 가장 값비싼 시간은 GPU 클러스터가 돌아가는 시간이 아니라, 수백 개의 실험 로그 표와 마크다운 메모를 꺼내 놓고 수십 편의 선행 논문을 인용하며 LaTeX 컴파일 에러와 씨름하는 마감 전 일주일이다. 그동안 범용 LLM에 "논문 초안을 써달라"고 부탁하면 그럴듯한 문장은 만들어주었지만, 존재하지 않는 참고문헌을 지어내거나 실험 수치와 본문 서술이 어긋나고, 학회 2단 레이아웃에서 표와 그림이 찢어지는 문제가 반복됐다.
            </p>
            <p>
              구글 클라우드 AI 리서치(Google Cloud AI Research) 팀이 Apache-2.0 라이선스로 전격 공개하며 하루 1,175스타(누적 2,917스타)를 돌파한 <strong>google-research/paper-orchestra</strong>는 이 '연구의 마지막 1마일'을 단일 프롬프트가 아닌 분업화된 멀티 에이전트 파이프라인으로 정면 돌파한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 단일 LLM 초안 생성기를 넘어선 '자기 비평 연구 집필 오케스트라'
            </h3>
            <p>
              PaperOrchestra가 주목받는 이유는 단순히 글쓰기를 자동화해서가 아니다. 구글 리서치 내부의 연구 워크플로우를 <strong>아웃라인·문헌 조사·섹션 집필·시각화·내용 정제</strong>라는 5단계 엔지니어링 파이프라인으로 해체하고, 각 단계에 특화된 작성 에이전트와 반성(Reflection)·비평(Critic) 에이전트를 분리 배치했기 때문이다.
            </p>

            <div class="editorial-quote">
              <p>
                "PaperOrchestra는 정형화되지 않은 사전 집필 자료(아이디어와 실험 로그)를 포괄적인 문헌 종합, 자동 생성된 플롯 및 개념 다이어그램을 포함한 <strong>투고 준비 완료 상태의 LaTeX 원고(<code>final_paper.pdf</code>)</strong>로 유연하게 변환한다."
              </p>
              <small>— Google Cloud AI Research PaperOrchestra 공식 저장소 아키텍처 개요 (Apache-2.0)</small>
            </div>

            <p>
              더욱 흥미로운 점은 시간 기준선 통제 장치다. CLI 옵션에 <code>--research_cutoff</code>(예: <code>2024-11</code>)을 두어 특정 시점 이후의 문헌을 배제한 공정한 연구 재현 벤치마크가 가능하며, <code>autoraters/</code> 디렉토리와 인터랙티브 프론트엔드 데모까지 함께 공개해 연구 커뮤니티가 직접 에이전트 작문 품질을 검증할 수 있게 열었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 5대 전문 에이전트와 3회 반복 플로팅 비평 루프
            </h3>
            <p>
              <code>methods/paper_writer_with_plotting.py</code>에 구현된 PaperOrchestra의 내부 파이프라인은 원시 실험 자료를 구조화된 학술 원고로 제련하는 세 가지 핵심 엔진으로 작동한다:
            </p>
            <ul>
              <li><strong>하이브리드 문헌 종합 &amp; 컷오프 필터링 (<code>HybridLiteratureAgent</code>):</strong> Semantic Scholar API와 연동해 핵심 선행 연구를 실시간 검색하고 우선순위를 매겨 BibTeX 인용과 관련 연구 맥락을 원고에 통합한다. 지정된 <code>research_cutoff</code> 이전 논문만 걸러내는 시계열 가드도 내장했다.</li>
              <li><strong>아웃라인·섹션 병렬 분업 (<code>OutlineAgent</code> &amp; <code>SectionWritingAgent</code>):</strong> 타겟 학회 템플릿(<code>templates/cvpr2025</code>, <code>iclr2025</code> 등)의 분량과 구조를 읽어 전체 논문 뼈대를 설계한 뒤, 각 섹션을 독립적으로 집필하면서 실험 로그의 정확한 수치를 본문에 결속시킨다.</li>
              <li><strong>코드 기반 플로팅 &amp; 최대 3라운드 비평 루프 (<code>PlottingAgent</code> &amp; <code>ContentRefinementAgent</code>):</strong> <code>--use_plotting true</code> 활성화 시 실험 데이터를 바탕으로 파이썬 시각화 코드를 작성해 차트를 렌더링하고, 이미지 모델(<code>gemini-3-pro-image-preview</code>)로 개념 다이어그램을 생성한 뒤 최대 3라운드의 Critic 검증과 반성 모델(<code>reflection_model_name</code>)의 교정을 거쳐 최종 LaTeX PDF를 빌드한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Google Research PaperOrchestra 5-Agent 논문 집필 오케스트레이션</span>
                <span class="schematic-badge">Apache-2.0 · CVPR/ICLR Templates</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Raw Materials &amp; Literature</div>
                  <div class="schematic-desc">
                    <code>idea_sparse.md</code> + <code>experimental_log.md</code><br>
                    <code>OutlineAgent</code> 학회 템플릿 구조 설계<br>
                    <code>HybridLiteratureAgent</code> (Semantic Scholar)<br>
                    <code>--research_cutoff</code> 시점 기반 문헌 필터
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Writing &amp; Plotting Loop</div>
                  <div class="schematic-desc">
                    <code>SectionWritingAgent</code> 섹션별 병렬 집필<br>
                    <code>PlottingAgent</code> 코드 기반 차트·개념도 생성<br>
                    최대 3회 <code>Critic</code> 시각 품질 자가 검증<br>
                    Writer(<code>gemini-3.1-pro</code>) + Image 모델 협업
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Refinement &amp; LaTeX PDF</div>
                  <div class="schematic-desc">
                    <code>ContentRefinementAgent</code> 논리·일관성 교정<br>
                    Reflection 모델 교차 리뷰 및 분량 튜닝<br>
                    <code>latex_writeup/</code> 조판 및 컴파일<br>
                    최종 투고용 <code>final_paper.pdf</code> 산출
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">PaperOrchestra 공식 프로젝트 포털 (yiwen-song.github.io/paper_orchestra)</span>
              </div>
              <img src="../assets/images/demo_paper_orchestra.png" alt="PaperOrchestra Official Project Page" class="showcase-img">
              <p class="showcase-caption">
                ▲ PaperOrchestra 공식 프로젝트 페이지 실구동 화면: Google Cloud AI Research 저자진과 5단계 멀티 에이전트 파이프라인 개요, 실험 아키텍처 및 자동 평가(Autoraters) 결과를 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 학계·산업 파급력: '논문 생산비 0원' 시대가 부를 피어리뷰의 시험대
            </h3>
            <p>
              구글 리서치가 자체 논문 자동 생성 파이프라인의 코드와 프롬프트, 평가자(Autoraters)까지 오픈소스로 푼 것은 학술 생태계에 거대한 양날의 검을 들이민 셈이다.
            </p>
            <ul>
              <li><strong>연구 속도의 극대화 vs 리뷰 붕괴 우려:</strong> 실험 결과를 수일 만에 깔끔한 ICLR/CVPR 포맷 원고로 바꿔주는 도구는 비영어권 연구자와 소규모 랩의 장벽을 극적으로 낮추지만, 동시에 AI가 대량 생성한 그럴듯한 논문이 학회 피어리뷰 시스템을 마비시킬 수 있다는 논쟁도 재점화하고 있다.</li>
              <li><strong>데이터셋 분리 공개와 투명성:</strong> 구글 팀은 코드 저장소에 벤치마크 데이터셋은 별도 공개로 남겨두면서도, 모든 프롬프트(<code>methods/prompts/</code>)와 자동 평가 스크립트(<code>autoraters/</code>)를 열어 과학적 검증 가능성을 확보했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 연구자의 손에서 LaTeX를 해방시킨 뒤 남는 질문
            </h3>
            <p>
              워드프로세서와 LaTeX가 연구자의 물리적 조판 노동을 줄여주었듯, PaperOrchestra는 문헌 조사와 초안 조립이라는 인지적·기계적 노동을 에이전트 오케스트라에게 위임했다.
            </p>
            <p>
              이제 학계에 남는 진짜 질문은 "이 논문의 문장이 유려한가"가 아니다. 서론과 그래프를 에이전트가 수 분 만에 빚어내는 시대에, 인간 연구자가 마지막까지 책임져야 할 독창적 가설과 실험의 진실성을 어떻게 증명할 것인가다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=PaperOrchestra+Google+Research+AI+paper+writing" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://yiwen-song.github.io/paper_orchestra/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 프로젝트 페이지
              </a>
              <a href="https://github.com/google-research/paper-orchestra" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
