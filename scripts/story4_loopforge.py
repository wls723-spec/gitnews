# -*- coding: utf-8 -*-
# Story 4: Tencent/LoopForge

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] Tencent/LoopForge                                -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_loopforge.jpg" alt="Tencent LoopForge Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="git-branch" style="width:12px;height:12px;fill:#fff;"></i> AGENT SOP</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ede9fe; border-color:#7c3aed; color:#5b21b6;">⚙️ 10종 코딩 CLI · SOP 납품 엔진</span>
              <span class="platform-tag">GitHub Trending &amp; loopforge.cn</span>
              <span class="platform-tag">Tencent / LoopForge</span>
            </div>
            
            <h2 class="article-headline">
              텐센트가 공개한 코딩 에이전트 팀 납품 플랫폼 'LoopForge': "확률에 기대던 바이브 코딩을 Docker 샌드박스와 인간 승인 게이트 기반 표준 SOP로 길들이다"
            </h2>

            <div class="article-subheadline">
              Claude Code·Codex·Antigravity·OpenCode 등 10종 코딩 CLI를 역할별 노드와 결정론적 스크립트 테스트, 인간 승인 게이트로 엮어내는 MIT 오픈소스 셀프호스팅 워크플로우 엔진
            </div>
            <p class="article-snippet">
              코딩 에이전트에게 "이 버그 고쳐줘"라고 시킬 때마다, 어떤 날은 테스트를 건너뛰고 어떤 날은 자기 코드를 자화자찬하며 넘어가기 일쑤입니다. 텐센트가 MIT 라이선스로 공개해 하루 만에 484 스타를 모은 `LoopForge`는 Dify나 n8n 같은 범용 챗봇 빌더가 아니라 오직 '소프트웨어 엔지니어링 팀의 코드 납품'만을 위해 설계된 셀프호스팅 플랫폼입니다. 설계·구현·독립 리뷰·스크립트 검증·인간 승인 게이트를 재현 가능한 SOP 그래프로 고정해 에이전트 개발을 엔지니어링 규율 안으로 끌어올렸습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "데모에선 멋졌는데, 팀 실무엔 도저히 못 쓰겠다"
            </h3>
            <p>
              개인 개발자의 터미널에서 코딩 에이전트는 마법처럼 보인다. 하지만 10명, 50명이 함께 코드를 병합하는 조직으로 들어오는 순간 마법은 두통으로 바뀐다. 에이전트가 설계 문서를 건너뛰고 바로 코드를 뜯어고치거나, 실패한 테스트를 몰래 삭제해 통과시키거나, 누가 어떤 모델 키로 얼마나 많은 토큰을 태워 PR을 올렸는지 추적할 길이 끊기기 때문이다.
            </p>
            <p>
              바로 이 간극을 메우기 위해 텐센트가 공개한 오픈소스 Go 기반 플랫폼 <strong>Tencent/LoopForge</strong>(1,431 스타, MIT 라이선스)가 오늘 GitHub General 및 Go 트렌딩을 동시에 흔들었다. 슬로건은 명쾌하다: <strong>"팀의 소프트웨어 납품 방식을 코딩 에이전트가 반복 실행할 수 있는 SOP(표준작업절차)로 전환하라."</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 에이전트를 교체하지 않고 '에이전트 주변의 조직 규율'을 만든다
            </h3>
            <p>
              LoopForge는 또 하나의 자체 코딩 모델을 훈련하거나 기존 에이전트 CLI를 대체하려 들지 않는다. 대신 이미 개발자들이 사랑하는 **10종의 코딩 CLI(CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness, ZCode)**를 그대로 실행기(Executor)로 수용하면서, 그 바깥에 Docker 샌드박스·역할 분리·인간 승인 게이트라는 단단한 엔지니어링 뼈대를 세운다.
            </p>

            <div class="editorial-quote">
              <p>
                "LoopForge는 코딩 CLI를 대체하지 않고 오케스트레이션한다. <strong>누가 무엇을, 어떤 샌드박스에서, 어떤 순서와 검증 스크립트를 거쳐 실행하고, 누가 최종 승인(Sign-off)을 내릴지 결정론적 SOP와 인간 게이트로 보장</strong>한다."
              </p>
              <small>— Tencent/LoopForge 공식 아키텍처 및 Dify/n8n 비교 FAQ</small>
            </div>

            <p>
              특히 서버를 띄우기 부담스러운 1인 개발자를 위해서는 `npx -y loopforge-cli@latest install claude` 한 줄로 Claude Code·Codex·Cursor·Hermes Agent 환경 안에 내장 워크플로우를 심어주는 **LoopForge Local** 에디션까지 함께 제공해 진입 장벽을 없앴다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 5종 노드 SOP 그래프와 프라이빗 실행 홈 격리
            </h3>
            <p>
              LoopForge 내부에서 하나의 요구사항(Requirement)이 실제 GitHub PR/MR과 산출물로 납품되기까지의 파이프라인은 고도로 구조화되어 있다:
            </p>
            <ul>
              <li><strong>이원화된 워크벤치(Main Bot 채팅 ↔ Visual SOP Designer):</strong> 빠른 탐색과 수정은 채팅창에서 `@역할·스킬·저장소`를 멘션해 Main Bot이 즉석 Docker 샌드박스를 열어 처리하고, 반복 검증이 필요한 정식 개발 프로세스는 시각적 SOP 캔버스에서 고정 파이프라인으로 배포·버전 관리한다.</li>
              <li><strong>AI와 결정론적 스크립트를 분리한 5종 노드:</strong> SOP 그래프는 <code>Agent</code>(역할별 독립 프롬프트·모델·MCP), <code>Script</code>(AI 개입 없이 빌드·린트·테스트를 강제하는 쉘 단계), <code>Human gate</code>(아티팩트를 검토하고 승인하거나 특정 이전 노드로 반려 재작업(Rework)시키는 인간 결재 관문), <code>Sub-SOP</code>, <code>Preview build</code>(정적 미리보기 아카이브)로 구성된다.</li>
              <li><strong>실행별 프라이빗 홈 격리 및 일시정지/개입:</strong> Claude Code 이후 7종의 에이전트 CLI는 실행마다 격리된 전용 홈 디렉터리에 모델 키와 MCP 설정을 보관해 팀 내 자격 증명 혼선을 막는다. 또한 실행 중인 SOP를 채팅창에서 언제든 일시정지(Pause)·스티어(Steer)·직접 인수(Take over)할 수 있고, 공개 단가 기준 토큰·비용 회계까지 자동 기록한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">LoopForge 다중 코딩 CLI 오케스트레이션 &amp; SOP 납품 파이프라인</span>
                <span class="schematic-badge">Docker Sandbox · 5-Node SOP · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Agent &amp; Role Execution</div>
                  <div class="schematic-desc">
                    명세(Clarify) → 설계 → 구현 → 독립 리뷰<br>
                    노드별 상이한 CLI/모델 선택 가능<br>
                    (Claude·Codex·Antigravity·OpenCode 등 10종)<br>
                    격리된 Docker 샌드박스 &amp; 전용 홈 실행
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Deterministic Script &amp; Rework</div>
                  <div class="schematic-desc">
                    AI 배제 순수 쉘 `Script` 노드 실행<br>
                    단위 테스트 · 린트 · 빌드 통과 강제<br>
                    실패 시 재작업 엣지(Rework Edge)로<br>
                    지정된 구현/설계 단계로 자동 반려
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Human Gate &amp; Delivery</div>
                  <div class="schematic-desc">
                    `Needs review` 인박스 결재 대기<br>
                    산출물·테스트·토큰 비용 리포트 검토<br>
                    승인 시 GitHub/GitLab PR·MR 자동 생성<br>
                    요구사항→납품 전체 감사 로그 영구 보존
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">LoopForge 공식 포털 (loopforge.cn) — 셀프호스팅 AI 소프트웨어 납품 플랫폼</span>
              </div>
              <img src="../assets/images/demo_loopforge.png" alt="LoopForge Self-Hosted AI Delivery Platform" class="showcase-img">
              <p class="showcase-caption">
                ▲ loopforge.cn 공식 화면: `./start.sh` 한 줄로 Docker 기반 플랫폼(0.0.0.0:8090)을 구축해 24/7 샌드박스 안에서 다중 코딩 에이전트와 테스트·인간 승인 게이트를 연결하는 구조를 소개하고 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 아키텍처 Trade-off 및 보안 경계: 신뢰 팀(Trusted Team)용 Docker 소켓 모델
            </h3>
            <p>
              엔터프라이즈 AI 오케스트레이션 시장에서 클라우드 SaaS형 코딩 워크스페이스(Devin 팀플랜 등)가 시트당 고가 구독 모델을 밀고 있는 가운데, 텐센트가 Go 기반 셀프호스팅 코어를 MIT 라이선스로 전면 개방한 것은 사내 코드 유출에 민감한 개발 조직들에게 매력적인 대안이다.
            </p>
            <ul>
              <li><strong>명시된 보안 경계 (Trusted Team Boundary):</strong> LoopForge의 기본 Docker Compose 배포는 호스트 Docker 소켓(`/var/run/docker.sock`)을 통해 샌드박스 컨테이너를 띄우며, 로그인한 팀원은 인스턴스 내 프로젝트 데이터를 열람할 수 있다. 텐센트 문서는 이를 "비신뢰 멀티테넌트 격리가 아닌 신뢰할 수 있는 엔지니어링 팀을 위한 설계"라고 투명하게 명시하며, 외부 노출 시 HTTPS 리버스 프록시와 `AGENTFLOW_ALLOW_SIGNUP=false` 설정을 권고한다.</li>
              <li><strong>실행 검증 기록(`validation.md`) 공개:</strong> 4개의 CodeBuddy 역할 에이전트가 Python 버그를 계획·구현·독립 리뷰하고 3개의 실제 테스트를 통과한 뒤 인간 승인 게이트를 거쳐 코드 무결성을 재검증한 End-to-End 수용 테스트(`45-delivery-model.test.mjs`)까지 저장소에 공개해 신뢰도를 높였다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 천재 프리랜서 10명을 데리고도 '공장'이 없으면 납품은 없다
            </h3>
            <p>
              지난 1년간 AI 업계의 관심은 온통 "어떤 코딩 모델이 벤치마크 1등을 찍었는가"에 쏠려 있었다. 하지만 현업 팀장들이 깨달은 냉정한 현실은, 아무리 똑똑한 모델도 공정(SOP)과 품질 게이트(Script + Human Approval) 없이는 매번 다른 품질의 코드를 뱉어낸다는 사실이다.
            </p>
            <p>
              LoopForge는 각자의 터미널에서 고군분투하던 코딩 CLI들을 하나의 조립 라인 위로 불러 모았다. AI가 코드를 짠다고 해서 소프트웨어 공학의 규율이 사라지는 것은 아니다—오히려 지금이야말로 그 규율을 코드로 굳혀야 할 때다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Tencent+LoopForge+coding+agent+SOP" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://loopforge.cn" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 방문
              </a>
              <a href="https://github.com/Tencent/LoopForge" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
