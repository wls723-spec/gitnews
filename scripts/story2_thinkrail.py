# -*- coding: utf-8 -*-
# Story 2: JetBrains/thinkrail

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] JetBrains/thinkrail : 젯브레인의 바이브 코딩 전용 IDE -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_thinkrail.jpg" alt="JetBrains ThinkRail Agentic IDE" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> JETBRAINS NEW</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">⚡ 젯브레인의 반격</span>
              <span class="aggro-tag">🔥 인텔리제이 25년 역사 최초 경량 네이티브 선언</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">JetBrains / thinkrail</span>
            </div>
            
            <h2 class="article-lead-headline">
              커서(Cursor)의 독주에 맞선 거인의 반격: 젯브레인이 내놓은 서브세컨드 경량 바이브 코딩 전용 IDE 'ThinkRail'
            </h2>

            <div class="article-subheadline">
              무거운 인텔리제이(IntelliJ) 껍질을 완전히 벗어던지다... pi 코딩 에이전트 런타임, Git Worktree 병렬 격리, 영구 유지되는 SPEC.md 지식 그래프를 결합한 네이티브 워크벤치 ThinkRail 오픈소스 전격 공개
            </div>
            <p class="article-snippet">
              0.3초 부팅 속도와 모나코(Monaco) 에디터 분할 워크벤치. 에이전트가 내 메인 브랜치를 더럽히지 못하도록 Git Worktree로 작업을 물리적 격리하고, 살아 숨 쉬는 사양서(SPEC.md)로 세션 종료 후에도 의도를 100% 보존하는 차세대 에이전틱 작업 공간.
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
              <i data-lucide="flame"></i> 1. 리드: 커서와 윈드서프의 협공 속, 침묵을 깬 25년 IDE 맹주
            </h3>
            <p>
              소프트웨어 개발 도구 시장에서 젯브레인(JetBrains)은 지난 사반세기 동안 범접할 수 없는 '코드 인텔리전스의 황제'였다. 
              IntelliJ IDEA, PyCharm, WebStorm으로 대표되는 그들의 에디터는 AST(추상 구문 트리) 정밀 인덱싱과 리팩토링의 정점으로 군림해 왔다. 
              그러나 지난 2년, 커서(Cursor)와 윈드서프(Windsurf) 같은 차세대 AI 네이티브 IDE들이 시장 점유율을 집어삼키는 동안 젯브레인은 뼈아픈 비판에 직면했다: 
              <em>"수 기가바이트의 메모리를 잡아먹고 10초 이상 로딩이 걸리는 인텔리제이 위에 AI 플러그인을 얹는 식으로는 절대 날렵한 AI 코딩 세대를 만족시킬 수 없다."</em>
            </p>
            <p>
              2026년 10월 28일, 젯브레인은 마침내 그 침묵을 깨고 충격적인 신작을 발표했다. 
              기존 인텔리제이 플랫폼의 무거운 JVM 기반 코어 레거시를 과감히 버리고, 
              <strong>0.3초 만에 번개처럼 부팅되는 초경량 네이티브 에이전틱 IDE 'ThinkRail(JetBrains/thinkrail)'</strong>을 오픈소스 인큐베이터 프로젝트로 전격 릴리즈한 것이다.
            </p>

            <div class="editorial-quote">
              "ThinkRail은 기존 IDE에 사이드바 채팅을 덧붙인 땜질식 제품이 아닙니다. 
              <strong>에이전트가 코드를 생각하는 방식 그대로 인터페이스를 바닥부터 다시 설계했습니다.</strong> 
              인간 개발자는 안전하게 지켜보고, 복수의 AI 에이전트들은 독립된 Git Worktree에서 브랜치를 깎아내며, 살아있는 사양서(SPEC.md)를 통해 영구적인 프로젝트 지식을 축적합니다."
              <span class="quote-author">— 젯브레인 ThinkRail 리드 아키텍트 팀 선언문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: '체크아웃 오염'을 종식시키는 Git Worktree 병렬 격리
            </h3>
            <p>
              기존 AI 코딩 도구의 가장 큰 스트레스는 에이전트가 작업 도중 개발자가 현재 작업 중인 메인 워킹 디렉토리를 마음대로 수정하거나 빌드를 깨뜨리는 '체크아웃 오염(Dirty Tree)' 현상이었다.
            </p>
            <p>
              <code>ThinkRail</code>은 이 문제를 <strong>Git Worktree를 통한 물리적 세션 격리</strong>로 완벽하게 해결했다. 
              프로젝트를 열면 에이전트마다 별도의 임시 브랜치와 독립 디렉토리가 서브세컨드로 생성된다. 
              개발자가 현재 로컬에서 코드를 치고 있는 동안에도, 백그라운드에서 3~4개의 <code>pi</code> 에이전트가 서로 다른 피처와 버그 픽스를 병렬로 테스트하고 커밋한다. 
              완성된 작업물은 버튼 한 번으로 PR로 발행되거나 메인 브랜치로 깔끔하게 머지된다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="git-branch" style="color:#f59e0b;"></i> ThinkRail: Git Worktree 병렬 격리 & SPEC.md 지식 루프 아키텍처</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">MULTI-WORKSPACE PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 격리 워크스페이스 분기</div>
                  <div class="step-title">git worktree spawn</div>
                  <div class="step-desc">개발자의 메인 체크아웃을 건드리지 않고 백그라운드에 독립된 브랜치와 파일 트리를 0.2초 만에 스폰.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. pi 에이전트 세션 구동</div>
                  <div class="step-title">Multi-Turn Thinking</div>
                  <div class="step-desc">스트리밍 토큰 계산과 비용 모니터링을 동반하며 모듈별 코딩 및 서브에이전트 위임 실행.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 살아있는 사양서 동기화</div>
                  <div class="step-title">SPEC.md Knowledge Graph</div>
                  <div class="step-desc">코드 옆에 spec_* 도구로 관리되는 지식 그래프를 갱신하여 세션이 바뀌어도 아키텍처 의도 영구 보존.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 인라인 비주얼 Diff 검토</div>
                  <div class="step-title">Interactive Before/After</div>
                  <div class="step-desc">UI 변경 요청 시 채팅창 내에서 전후 목업과 diff를 렌더링하고 객관식 질문 모달로 피드백 수취.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 안착 및 자동 정리</div>
                  <div class="step-title">Settled Shelf & PR Push</div>
                  <div class="step-desc">PR 머지 시 워크스페이스가 자체 보관소(Settled Shelf)로 안착하고 원클릭으로 깃허브 PR 자동 동기화.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 모나코 분할 뷰와 대화형 의사결정 모달
            </h3>
            <p>
              <code>ThinkRail</code>의 UI/UX 완성도는 역시 젯브레인답다는 탄성을 자아낸다. 
              중앙에는 초고속 모나코(Monaco) 에디터 탭이 분할 배치되어 실시간 Git 변경 마크를 표시하고, 
              좌측에는 프로젝트 워크트리 목록과 최근 1주일간 휴면 상태에 들어간 워크스페이스를 담아두는 <strong>'안착 선반(Settled Shelf)'</strong>이 자리한다.
            </p>
            <p>
              더불어 에이전트가 개발자의 의도를 어림짐작으로 때려 맞추다 산으로 가는 현상을 방지하기 위해, 
              채팅창 내에서 에이전트가 개발자에게 <strong>선택형 다지선다 질문(Multiple-Choice Modal)</strong>을 직접 던질 수 있는 인터랙션 도구를 탑재했다. 
              프론트엔드 변경 시에는 코드 diff뿐만 아니라 시각적인 전후 목업(Mockup)을 채팅 내에서 비교해 주며, 개발자는 이미지 위에 마우스로 앵커 코멘트를 남길 수 있다.
            </p>

            <!-- 실제 소프트웨어 UI 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_thinkrail_workbench.jpg" alt="ThinkRail의 모나코 워크벤치와 Git Worktree 분기 뷰" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>ThinkRail 공식 워크벤치 실구동 캡처:</strong> 좌측 패널의 Git Worktree 격리 브랜치 목록, 중앙의 pi 에이전트 다중 턴 스트리밍 창과 모나코 에디터 코드 diff, 우측의 SPEC.md 살아있는 사양서 트리와 터미널이 한 화면에서 완벽하게 조화를 이루고 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: VS Code 독점 생태계에 균열을 내다
            </h3>
            <p>
              현재 Cursor, Windsurf, Trae 등 시장에 나와 있는 대다수 AI IDE는 마이크로소프트의 VS Code(Code-OSS)를 포크(Fork)하여 래핑한 형태다. 
              이로 인해 VS Code 고유의 확장 프로그램 마켓플레이스 라이선스 제약과 아키텍처적 한계에 묶여 있었다.
            </p>
            <p>
              <code>ThinkRail</code>은 젯브레인이 자체 계정 종속(Vendor Lock-in)을 포기하고 완전한 <strong>BYOK(Bring Your Own Key: JetBrains AI뿐만 아니라 Anthropic, OpenAI, 로컬 Ollama 모델까지 사용자가 자유 선택)</strong>와 MCP(Model Context Protocol) 개방형 표준을 전면 수용했다는 점에서 전략적 파괴력이 크다. 
              이는 AI IDE 시장의 주도권을 마이크로소프트 진영으로부터 다시 탈환하겠다는 젯브레인의 승부수다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 개발자는 지휘관이 되고, IDE는 관제탑이 된다
            </h3>
            <p>
              코드를 한 줄씩 타이핑하던 시절의 IDE가 '텍스트 워드프로세서'였다면, 
              에이전트들이 알아서 코드를 작성하고 브랜치를 테스트하는 시대의 IDE는 <strong>'전투기 편대를 통제하는 항공모함 관제탑'</strong>이어야 한다.
            </p>
            <p>
              <code>ThinkRail</code>은 바로 그 관제탑의 원형을 제시했다. 
              에이전트에게 자율권을 주되 철저한 Worktree 격리로 리스크를 봉쇄하고, 살아있는 사양서로 프로젝트의 맥락을 잃지 않는 환경. 
              25년 IDE 거인의 반격은 이제 막 시작되었다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://thinkrail.ai/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 바로가기
              </a>
              <a href="https://www.youtube.com/results?search_query=jetbrains+thinkrail+agentic+ide" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/JetBrains/thinkrail" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 2 (thinkrail) module loaded successfully.")
