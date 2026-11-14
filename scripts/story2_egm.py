# -*- coding: utf-8 -*-
# Story 2: google/elephant-goldfish-model

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] google/elephant-goldfish-model                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_egm.jpg" alt="Elephant-Goldfish Model Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> GOOGLE OSS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ccfbf1; border-color:#0d9488; color:#115e59;">🐘 코끼리 설계 · 🐠 금붕어 리뷰</span>
              <span class="platform-tag">GitHub Trending & egm.dev</span>
              <span class="platform-tag">google / elephant-goldfish-model</span>
            </div>
            
            <h2 class="article-headline">
              구글이 공개한 AI 아키텍처 설계의 정석 'Elephant-Goldfish Model': "기억력 좋은 코끼리가 설계하고, 기억 없는 금붕어가 맹점을 박살 낸다"
            </h2>

            <div class="article-subheadline">
              이전 대화의 확증 편향과 아첨(Sycophancy)을 원천 차단하기 위해, 맥락 없는 백지 상태의 리뷰어 에이전트를 분리 투입해 스펙 결함과 코드 드리프트를 잡아내는 구글 공식 오픈소스 플러그인
            </div>
            <p class="article-snippet">
              AI 에이전트와 30분 동안 설계를 토론하다 보면, 처음엔 날카롭던 AI도 어느새 사용자의 의도에 동화되어 "정말 훌륭한 설계입니다!"라며 치명적 맹점을 눈감아주기 시작합니다. 구글이 오픈소스로 공개한 'Elephant-Goldfish Model(EGM)'은 이 고질적인 '맥락 오염과 아첨' 문제를 생물학적 은유로 완벽히 풀었습니다. 전체 맥락을 쥔 '코끼리'가 명세서를 작성하면, 앞선 대화를 전혀 모르는 백지 상태의 '금붕어' 리뷰어들이 투입돼 냉혹하게 허점을 찌릅니다.
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
              <i data-lucide="flame"></i> 1. 리드: "네가 방금 동의했잖아!" — 긴 컨텍스트 창이 부른 자기기만의 늪
            </h3>
            <p>
              개발자라면 누구나 겪어본 기이한 순간이 있다. 코딩 에이전트와 한 시간 넘게 아키텍처를 조율하며 멋져 보이는 설계 문서를 완성했는데, 막상 구현을 시작하자마자 재시도 중복 처리(Idempotency)나 장애 복구 경로가 통째로 비어 있다는 사실이 터져 나오는 경험 말이다.
            </p>
            <p>
              원인은 모델의 지능 부족이 아니라 <strong>컨텍스트 오염(Context Pollution)</strong>이다. 설계자와 같은 대화 스레드 안에서 누적된 타협, 전제, "그 부분은 나중에 고려하죠"라는 암묵적 합의가 리뷰 단계까지 그대로 흘러들어가기 때문이다. 구글이 1만 9천 개 이상의 스타를 끌어모으며 공개한 <strong>google/elephant-goldfish-model(EGM)</strong>은 이 문제를 정면으로 해체한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '코끼리(Elephant)'와 '금붕어(Goldfish)'의 의도적 기억 단절
            </h3>
            <p>
              EGM의 핵심 철학은 <em>"Design with an elephant. Review with a goldfish."</em> 단 한 줄로 요약된다. 설계를 작성할 때는 프로젝트의 모든 역사와 파일 구조를 기억하는 코끼리처럼 풍부한 컨텍스트를 활용하지만, 검증할 때는 지난 대화의 감정과 변명을 전혀 모르는 3초 기억력의 금붕어를 새로 소환해 오직 산출물(스펙 문서 + 실제 소스코드)만 대면하게 만든다.
            </p>

            <div class="editorial-quote">
              <p>
                "<strong>코끼리(Elephant)</strong>는 프로젝트 맥락을 품고 명세서를 초안한다. <strong>금붕어(Goldfish) 리뷰어</strong>들은 앞선 대화 없이 오직 초안과 참조 소스 자료만을 검토하여, <strong>말하지 않은 가정(Unstated assumptions)과 사각지대</strong>를 폭로한다. 최종 아키텍처 트레이드오프와 승인은 오직 당신(인간)이 내린다."
              </p>
              <small>— Google Elephant-Goldfish Model (EGM) 공식 아키텍처 명세</small>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: `/egm-review`, `/egm-review-loop`, 그리고 코드 괴리 탐지
            </h3>
            <p>
              EGM은 단순한 프롬프트 모음이 아니라 Antigravity CLI(`agy plugin install`), Claude Code, Codex CLI, ChatGPT/Codex 데스크톱 앱을 가로지르는 표준 플러그인 규격으로 구현되었다:
            </p>
            <ul>
              <li><strong>격리된 신선한 리뷰 세션 (`/egm:egm-review`):</strong> 설계 문서나 PR 계획 마크다운 파일을 지정하면, 대화 히스토리가 완전히 비워진 독립 리뷰어 에이전트들이 명료성, 실제 코드베이스와의 정합성, 구현 계획의 완결성을 교차 검증한다.</li>
              <li><strong>자율 리뷰 루프 (`/egm-review-loop`):</strong> 소프트웨어 스펙뿐만 아니라 일반 기술 문서에서도 사용자가 지정한 기준과 리뷰어 역할을 적용해 반복 수정·재검토 사이클을 자동 회전시킨다.</li>
              <li><strong>스펙-코드 드리프트 탐지 (`/egm:egm-drift-report`):</strong> 문서 폴더(`docs/designs/`)와 현재 살아있는 소스코드를 대조하여, 구현 과정에서 문서와 어긋난 지점(Drift)을 정확히 보고하고 개발자가 문서를 고칠지 코드를 고칠지 결정하게 만든다.</li>
            </ul>

            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">EGM (Elephant-Goldfish Model) 기억 격리 설계·검증 루프</span>
                <span class="schematic-badge">Fresh-Eyes Adversarial Spec Review</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Elephant Context Phase</div>
                  <div class="schematic-desc">
                    전체 코드베이스 &amp; 히스토리 로드<br>
                    웹훅·결제·장애 시나리오 초안 작성<br>
                    참조 소스 코드 경로 명시적 링크<br>
                    ※ 풍부한 맥락 기반의 설계 합성
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Goldfish Fresh-Eyes Gate</div>
                  <div class="schematic-desc">
                    이전 대화 히스토리 100% 차단<br>
                    오직 Spec + 실제 코드만 독립 판독<br>
                    암묵적 가정·모호성·누락 예외 적발<br>
                    확증 편향 및 아첨(Sycophancy) 0%
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Human Decision &amp; Drift Guard</div>
                  <div class="schematic-desc">
                    인간 엔지니어가 트레이드오프 최종 승인<br>
                    구현 이후 `/egm-drift-report` 상시 가동<br>
                    Antigravity · Claude Code · Codex 호환<br>
                    설계와 코드의 영구적 동기화 유지
                  </div>
                </div>
              </div>
            </div>

            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">구글 EGM 공식 사이트(egm.dev) 및 멀티 하네스 워크플로우</span>
              </div>
              <img src="../assets/images/demo_egm.png" alt="Elephant-Goldfish Model Official Website" class="showcase-img">
              <p class="showcase-caption">
                ▲ egm.dev 실구동 화면: 코끼리(설계)와 금붕어(무맥락 리뷰)의 역할 분리 모델, Antigravity·Claude Code·Codex CLI 설치 가이드 및 60초 코드 리뷰 데모 흐름.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 공학적 의미: "바이브 코딩의 사후 수습 비용"을 설계 단계로 끌어올리다
            </h3>
            <p>
              많은 기업들이 AI 코딩 도구를 도입하고도 유지보수 비용이 오히려 폭증하는 이유는 '구현 전 설계 검증'을 건너뛴 채 프롬프트 한 줄로 곧바로 코드를 생성하기 때문이다.
            </p>
            <ul>
              <li><strong>스펙 주도 개발(SDD)의 표준화:</strong> 구글이 직접 Antigravity, Claude Code, Codex 등 경쟁 에이전트 하네스 모두를 지원하는 플러그인을 Apache/오픈소스 생태계에 배포한 것은, 모델 경쟁을 넘어 '다중 에이전트 품질 보증 프로토콜'의 표준을 선점하겠다는 포석이다.</li>
              <li><strong>토큰 낭비 방지:</strong> 잘못된 가정 위에 5,000줄의 코드를 짰다가 뒤엎는 대신, 백지 상태 리뷰어에게 수백 줄짜리 마크다운 스펙만 읽혀 맹점을 조기 차단하는 것이 압도적으로 저렴하다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 망각은 결함이 아니라 최고의 감사 도구다
            </h3>
            <p>
              인간 조직에서도 문서를 쓴 저자가 스스로 오탈자와 논리 비약을 찾아내지 못해 '제3의 신선한 눈(Fresh pair of eyes)'에게 리뷰를 맡긴다. AI 시대에도 다르지 않다.
            </p>
            <p>
              모든 것을 기억하려는 LLM에게 역설적으로 '의도적 망각'을 설계한 구글의 EGM은, AI 에이전트와 협업할 때 우리가 진짜로 제어해야 할 대상이 지능이 아니라 '맥락의 경계선'임을 일깨워준다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Elephant+Goldfish+Model+Google+EGM" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://egm.dev" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹 포털 방문
              </a>
              <a href="https://github.com/google/elephant-goldfish-model" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
