# -*- coding: utf-8 -*-
# Story 2: NVIDIA/SkillEvaluator

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] NVIDIA/SkillEvaluator                            -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_skill_evaluator.jpg" alt="NVIDIA SkillEvaluator Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> NVIDIA OSS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#14532d;">🧪 에이전트 스킬 품질 감사 표준</span>
              <span class="platform-tag">GitHub Trending &amp; docs.nvidia.com</span>
              <span class="platform-tag">NVIDIA / SkillEvaluator</span>
            </div>

            <h2 class="article-headline">
              "그 스킬, 진짜 에이전트 실력을 높여주나요?" — 엔비디아(NVIDIA)의 3단계 스킬 평가 엔진 'SkillEvaluator'
            </h2>

            <div class="article-subheadline">
              단순 프롬프트 린팅을 넘어 정적 보안 스캔·의미론적 중복 탐지·합성 데이터셋 생성·도커 샌드박스 A/B 실전 벤치마크까지 통합한 Apache-2.0 프레임워크 (2,617스타)
            </div>
            <p class="article-snippet">
              Claude Code, Codex, Antigravity를 겨냥한 <code>SKILL.md</code> 파일이 매일 수만 개씩 쏟아지고 있지만, 정작 그 스킬이 에이전트 성능을 높이는지 오히려 컨텍스트만 오염시키는지 검증할 도구는 전무했습니다. 하루 953스타를 추가한 <strong>NVIDIA/SkillEvaluator</strong>는 논문(arXiv:2608.20614)과 함께 공개된 3단계(Tier 1~3) 자동 감사 파이프라인으로, "스킬 유무에 따른 실제 에이전트 행동 차이"를 도커 샌드박스 안에서 정량 채점합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 마크다운 만능주의와 '스킬 블로트(Skill Bloat)'의 습격
            </h3>
            <p>
              2026년 개발자 생태계의 새로운 유행어는 단연 '에이전트 스킬(Agent Skills)'이다. 팀마다 <code>SKILL.md</code> 폴더를 수십 개씩 사내 저장소에 밀어 넣고, 오픈소스 마켓플레이스에서 남이 쓴 스킬을 무작정 복사해 온다. 하지만 현업 팀들이 곧 마주한 현실은 냉혹했다. 검증되지 않은 스킬이 늘어나자 에이전트가 서로 충돌하는 지침을 동시에 읽어 들여 추론 속도가 느려지고, 심지어 스킬 내부에 숨겨진 프롬프트 인젝션이나 하드코딩된 비밀 키가 CI 파이프라인을 위협하기 시작했다.
            </p>
            <p>
              오늘 GitHub 일간 트렌딩 953스타를 쓸어 담으며 누적 2,617스타를 기록한 <strong>NVIDIA/SkillEvaluator</strong>는 바로 이 '감이 지배하던 스킬 생태계'에 소프트웨어 공학 수준의 테스트 게이트(Quality Gate)와 CI/CD 검증 규율을 이식한 엔비디아의 오픈소스 해답이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 정적 검사부터 Harbor 도커 샌드박스 A/B 대조 실험까지
            </h3>
            <p>
              <code>SkillEvaluator</code>는 단순한 마크다운 문법 검사기가 아니다. 엔비디아가 자사 <code>NVIDIA Verified Skills</code> 파이프라인과 논문(arXiv:2608.20614)에 실제 적용한 3계층 평가 프레임워크를 그대로 PyPI 패키지(<code>skillevaluator</code>)로 풀어냈다.
            </p>

            <div class="editorial-quote">
              <p>
                "스킬 평가의 진짜 질문은 문서가 예쁜가가 아니라 <strong>'스킬을 켰을 때와 껐을 때 실제 에이전트 작업 성공률이 얼마나 달라지는가'</strong>다. SkillEvaluator는 정적 보안 게이트, 임베딩 중복 탐지, 그리고 격리된 샌드박스 A/B 실전 실행을 하나의 CI 명령으로 통합했다."
              </p>
              <small>— NVIDIA SkillEvaluator 3-Tier 아키텍처 문서 &amp; arXiv:2608.20614 백서</small>
            </div>

            <p>
              특히 인상적인 지점은 LLM API 키 없이도 <code>uv run skillevaluator quality-check</code>만으로 즉각 100점 만점의 결정론적 품질 점수(예: <code>88.8/100 (B)</code>)를 뽑아낼 수 있고, 원할 경우 NVIDIA Build(NIM) 무료 프로토타이핑 키나 자체 모델 엔드포인트를 연결해 루브릭 평가와 3단계 라이브 에이전트 평가로 확장할 수 있다는 점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Tier 1(보안·구조) → Tier 2(중복) → Tier 3(실전 A/B)
            </h3>
            <p>
              <code>SkillEvaluator</code>의 <code>validate</code> 파이프라인은 세 개의 독립적이면서도 상호 보완적인 게이트를 순서대로 통과하며 스킬의 실전 투입 가능 여부를 판정한다:
            </p>
            <ul>
              <li><strong>Tier 1 (정적 검증 &amp; 보안 스캐닝):</strong> Agent Skills 공식 스펙(<code>agentskills.io</code>)과 하네스 호환성을 점검한다. 누락된 외부 스캐너(<code>SkillSpector</code>, <code>Gitleaks</code>, 선택적 <code>Semgrep</code>)를 해시 검증된 핀 고정 릴리즈로 자동 확보해 악성 스크립트나 시크릿 유출을 차단한다.</li>
              <li><strong>Tier 2 (의미론적 중복 &amp; 카탈로그 충돌 탐지):</strong> 임베딩과 LLM을 결합해 새 스킬의 지침이 기존 사내 스킬 카탈로그(<code>--catalog ./skill-catalog.json</code>)와 내용이 겹치거나 지시가 상충하는지 자동 탐지한다. 스킬 비대화로 인한 컨텍스트 낭비를 막는 핵심 장치다.</li>
              <li><strong>Tier 3 (합성 데이터셋 &amp; Harbor 라이브 에이전트 평가):</strong> <code>create-eval-dataset</code>으로 스킬 기반 합성 평가 과제와 네거티브 케이스를 자동 생성한 뒤, 오픈소스 에이전트 평가 런타임인 <strong>Harbor</strong>의 Docker 샌드박스 안에서 스킬 적용 전후 에이전트 행동을 직접 비교한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">NVIDIA SkillEvaluator 3-Tier 스킬 품질 게이트 및 CI 파이프라인</span>
                <span class="schematic-badge">Apache-2.0 · arXiv:2608.20614</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Tier 1 · Validation Gate</div>
                  <div class="schematic-desc">
                    결정론적 Quality Score (기본 컷 70점)<br>
                    <code>SkillSpector</code> 스킬 전용 보안 스캔<br>
                    <code>Gitleaks</code> / <code>Semgrep</code> 시크릿·취약점 검사<br>
                    API 키 없이 오프라인 CI 실행 지원
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Tier 2 · Deduplication</div>
                  <div class="schematic-desc">
                    임베딩 기반 의미론적 중복 계산<br>
                    <code>skill-catalog.json</code> 전사 스킬 비교<br>
                    지침 충돌·중복 트리거 사전 차단<br>
                    LLM 루브릭 기반 문서 완성도 채점
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Tier 3 · Live Evaluation</div>
                  <div class="schematic-desc">
                    합성 평가 데이터셋(<code>EVAL.md</code>) 자동 생성<br>
                    <strong>Harbor</strong> + Docker 격리 샌드박스 실행<br>
                    With-Skill vs Without-Skill A/B 대조<br>
                    <code>skillevaluator ci init</code> PR 자동화
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">NVIDIA 공식 SkillEvaluator 문서 및 3-Tier 파이프라인 포털 (docs.nvidia.com)</span>
              </div>
              <img src="../assets/images/demo_skill_evaluator.png" alt="NVIDIA SkillEvaluator Official Documentation and Pipeline" class="showcase-img">
              <p class="showcase-caption">
                ▲ docs.nvidia.com/skills/skillevaluator/ 공식 포털 화면: CLI 단독 실행, <code>skillevaluator ci init</code>을 통한 GitHub/GitLab PR 게이트 연동, 그리고 에이전트 자체 평가 스킬 설치 가이드를 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업적 의미: '프롬프트 감성'에서 '측정 가능한 스킬 엔지니어링'으로
            </h3>
            <p>
              지금까지 AI 에이전트 스킬은 코드가 아니라 일종의 '주술적 텍스트' 취급을 받았다. 작성자가 "내 컴에서는 잘 되던데"라고 말하면 반박할 정량 지표가 없었기 때문이다.
            </p>
            <ul>
              <li><strong>엔비디아의 오픈 거버넌스 포석:</strong> 엔비디아는 GPU 하드웨어와 NIM 추론 엔드포인트 생태계를 넘어, 에이전트 운영 체제 위에서 돌아가는 '스킬의 품질 보증 규격' 자체를 Apache-2.0 오픈소스로 선점하고 있다.</li>
              <li><strong>CI/CD 안으로 들어온 행동 테스트:</strong> <code>skillevaluator ci init</code> 한 줄이면 저장소의 모든 스킬 PR마다 자동으로 품질 점수와 보안 스캔, 중복 리포트가 달리며 조직 차원의 '스킬 부채'를 통제할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 유닛 테스트 없는 코드처럼, 평가 없는 스킬도 살아남지 못한다
            </h3>
            <p>
              소프트웨어 공학이 수십 년에 걸쳐 배운 가장 비싼 교훈은 "측정하지 않는 것은 개선할 수 없다"는 사실이다.
            </p>
            <p>
              앞으로 수천 개의 사내 지침과 도메인 노하우가 <code>SKILL.md</code> 형태로 축적될수록, 좋은 에이전트 팀과 혼란스러운 에이전트 팀을 가르는 기준은 모델 파라미터 크기가 아니라 얼마나 엄격한 '스킬 평가 파이프라인'을 갖추었느냐가 될 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/watch?v=4rI0zATFxYI" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://docs.nvidia.com/skills/skillevaluator/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> NVIDIA 공식 문서 포털
              </a>
              <a href="https://github.com/NVIDIA/SkillEvaluator" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
