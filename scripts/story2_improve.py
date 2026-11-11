# -*- coding: utf-8 -*-
# Story 2: shadcn/improve (설계자-시공자 분업 하네스)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] shadcn/improve : 설계자-시공자 분업 하네스 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_improve.jpg" alt="shadcn improve Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 shadcn 신작 에이전트 스킬</span>
              <span class="aggro-tag">⚡ 토큰 비용 90% 절감 패러다임</span>
              <span class="platform-tag">GitHub Trending (★10.8k)</span>
              <span class="platform-tag">shadcn / improve</span>
            </div>
            
            <h2 class="article-headline">
              "지능이 높은 놈이 설계하고, 싼 놈이 친다": shadcn이 제시한 '설계자-시공자' 분업 하네스
            </h2>

            <div class="article-subheadline">
              모든 코드를 최고가 모델에 맡기던 비효율을 끝내다: Opus의 코드베이스 정밀 감사와 Flash/Haiku의 10분의 1 비용 고속 구현
            </div>
            <p class="article-snippet">
              모던 웹 프론트엔드의 사실상 표준을 정립한 shadcn이 이번에는 코딩 에이전트 생태계의 비효율에 칼을 빼들었습니다. 사소한 변수명 수정이나 보일러플레이트 작성까지 100만 토큰당 수십 달러의 최고가 프론티어 모델을 소비하던 낭비를 멈추고, 지능이 가장 뛰어난 모델은 아키텍처 감사와 정밀 명세(Spec) 작성에만 투입하고 실제 타이핑은 10배 저렴한 경량 모델에 위임하는 오픈소스 하네스 'improve'가 개발자 커뮤니티의 폭발적 반응을 얻고 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "수석 아키텍트에게 벽돌 나르기를 시키고 있는가?"
            </h3>
            <p>
              코딩 에이전트를 도입한 전 세계 수많은 개발팀이 매달 청구되는 엄청난 API 토큰 비용에 충격을 받고 있다. 
              사소한 CSS 마진 수정, 뻔한 CRUD 함수 추가, 오타 수정 작업까지 Claude 3.5 Sonnet이나 Opus, GPT-4o 같은 
              최고가 플래그십 모델을 돌려왔기 때문이다.
            </p>
            <p>
              "우리는 지금 연봉 5억 원짜리 수석 엔지니어에게 커피 타오기와 벽돌 나르기를 시키고 있는 꼴이다." 
              웹 UI 생태계의 절대강자 shadcn은 이 황당한 비효율을 정면으로 꼬집으며, 단 한 줄의 구현 코드도 직접 작성하지 않는 
              역발상 에이전트 스킬 <strong>improve</strong>를 전격 공개했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 지능이 복리로 축적되는 구간에만 최고 지능을 써라
            </h3>
            <p>
              소프트웨어 개발에서 지능이 가장 절실한 순간은 코드를 타이핑할 때가 아니다. 
              코드베이스의 전체 맥락을 꿰뚫어보고, 무엇이 진정으로 고칠 가치가 있는 문제인지 판단하며, 
              부작용(Side-effect) 없는 최소 단위의 변경 계획을 세우는 순간이다.
            </p>

            <div class="editorial-quote">
              <p>
                "가장 유능한 모델은 지능이 복리로 작동하는 곳에만 써야 한다 — 코드베이스를 이해하고, 
                무엇을 해야 할지 판단하고, 명확한 스펙을 작성하는 단계다. <strong>'improve' 스킬은 결코 스스로 코드를 구현하지 않는다. 
                그것이 남기는 산출물은 오직 더 저렴한 하위 모델들이 단 1의 오차도 없이 기계적으로 시공할 수 있는 완벽한 구현 계획서뿐이다.</strong>"
              </p>
              <small>— shadcn, improve 프로젝트 공식 선언문</small>
            </div>

            <p>
              이 전략을 채택한 개발팀들은 에이전트 구동 토큰 비용을 최대 85~92% 절감하면서도, 
              단일 모델이 장시간 코딩할 때 발생하는 '컨텍스트 드리프트(Context Drift)'와 환각 버그를 완벽히 통제하는 데 성공했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 3단계 계층형 라우팅과 원자적 계획(Spec) 합성
            </h3>
            <p>
              `improve` 하네스는 인간 소프트웨어 엔지니어링의 시니어-주니어 협업 구조를 엄격한 알고리즘으로 모델링했다:
            </p>
            <ul>
              <li><strong>Step 1: 심층 아키텍처 감사 (Audit):</strong> 최고 사양 모델(Opus/Sonnet)이 리포지토리의 AST 트리, 타입 시스템, 의존성 관계도를 탐색하여 기술 부채와 리팩토링 포인트를 발굴.</li>
              <li><strong>Step 2: 확정적 명세서(Spec) 발행:</strong> 대상 파일 경로, 함수 시그니처 변경안, 사전 조건, 성공 검증 테스트 명령어를 마크다운 체크리스트로 정밀 합성. 이때 코딩 지침은 기계적으로 실행 가능하도록 극한으로 구체화.</li>
              <li><strong>Step 3: 경량 워커 위임 (Execution):</strong> 토큰 단가가 10분의 1에 불과한 경량 모델(Haiku, Gemini Flash, 로컬 7B SLM)이 명세서의 체크리스트를 하나씩 가져와 파일에 덤프하고 테스트 통과 여부만 확인.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">shadcn improve 설계자-시공자 분업 파이프라인</span>
                <span class="schematic-badge">Tiered Agent Architecture</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Phase 1: The Architect (Opus)</div>
                  <div class="schematic-desc">
                    전체 코드베이스 맥락 파악 및 감사<br>
                    설계 결함 및 리팩토링 목표 선정<br>
                    코드는 짜지 않고 정밀 Spec만 생성
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Phase 2: Atomic Spec Gate</div>
                  <div class="schematic-desc">
                    파일별 변경점(Diff Contract) 정의<br>
                    유닛 테스트 통과 기준 사전 명시<br>
                    환각 여지 제로(0)의 결정론적 지침
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Phase 3: The Builder (Flash/Haiku)</div>
                  <div class="schematic-desc">
                    10배 저렴한 고속 경량 모델<br>
                    스펙대로 기계적 파일 패치 수행<br>
                    테스트 통과 후 즉시 세션 종료
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">shadcn/improve 리포지토리 공식 아키텍처 및 철학</span>
              </div>
              <img src="../assets/images/demo_improve.png" alt="shadcn improve GitHub Repository" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/shadcn/improve 리포지토리 공식 화면: "The skill never implements anything itself. The plan is the product." 코드를 짜지 않고 완벽한 실행 계획서만을 제품으로 정의하는 혁신적 설계 사상.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 빅테크의 토큰 소비 경쟁에 던진 제동
            </h3>
            <p>
              OpenAI와 Anthropic 등 프론티어 파운데이션 모델 제공사들은 자사의 가장 비싸고 거대한 모델을 더 오래, 
              더 많은 토큰을 쓰며 구동하도록 유도해왔다. 하지만 shadcn의 `improve`는 이러한 벤더들의 수익 모델에 정면으로 역행한다.
            </p>
            <p>
              사고와 추론은 단 1회 집중하여 계획을 뽑아내고, 수만 줄의 반복 코딩은 가장 싼 덤핑 모델이나 로컬 모델로 처리해버리기 때문이다. 
              이는 엔터프라이즈 개발 조직이 AI 에이전트 도입 예산을 10분의 1로 압축하면서도 품질을 균일하게 보증할 수 있는 강력한 무기를 쥐어준 셈이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 스마트한 엔지니어링의 본질
            </h3>
            <p>
              인공지능의 시대에도 진짜 실력은 "더 크고 비싼 모델을 마구잡이로 돌리는 것"이 아니라, 
              "각자의 지능 수준에 맞는 자리에 적절한 도구를 배치하는 시스템 설계력"에 있다. 
              shadcn이 제시한 `improve`는 향후 모든 멀티 에이전트 소프트웨어 공학이 따라야 할 실용주의의 모범 답안이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=shadcn+improve+coding+agent+architecture" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/shadcn/improve" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
