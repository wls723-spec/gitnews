# -*- coding: utf-8 -*-
# Story 2: Donchitos/Claude-Code-Game-Studios

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] Donchitos/Claude-Code-Game-Studios -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_game_studios.jpg" alt="Claude Code Game Studios" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#3b82f6; color:#1d4ed8;">🎮 자율 게임 개발 스튜디오 거버넌스</span>
              <span class="platform-tag">GitHub Viral</span>
              <span class="platform-tag">Donchitos / Claude-Code-Game-Studios</span>
            </div>
            
            <h2 class="article-headline">
              단일 챗봇의 혼돈을 끝내다: Claude Code를 49개 부서의 자율 게임 개발 스튜디오로 조직화한 오케스트레이션
            </h2>

            <div class="article-subheadline">
              "스파게티 코드와 매직 넘버 하드코딩으로 무너지던 1인 AI 게임 개발의 종말" — 디렉터, 테크 리드, 셰이더 장인, QA 엔지니어 등 49개 특화 에이전트와 74개 전문 스킬이 실제 AAA 게임 스튜디오의 승인 파이프라인과 엄격한 품질 게이트를 그대로 재현하는 오픈소스 시스템 전격 공개 (+3.3만 스타)
            </div>
            <p class="article-snippet">
              단일 세션 챗봇에게 '게임 만들어줘'를 외치다 코드 붕괴를 겪던 전 세계 인디 개발자들의 구원투수. 비전 수호자(디렉터), 도메인 리드, 실무 스페셜리스트의 엄격한 3계층 위계 거버넌스를 통해 무인 게임 제작의 소프트웨어 공학적 질서를 완성.
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
              <i data-lucide="flame"></i> 1. 리드: 새벽 4시의 참극, 한 줄의 프롬프트가 깨뜨린 3D 던전
            </h3>
            <p>
              AI로 1인 게임 개발을 시도해 본 개발자라면 누구나 겪는 악몽이 있다. 
              장장 사흘 밤낮을 Claude Code나 Cursor와 씨름하며 물리 엔진, 캐릭터 애니메이션, 절차적 맵 생성을 그럴듯하게 엮어놓았을 때다. 
              마지막으로 <code>"인벤토리 UI에 사운드 이펙트 좀 추가해줘"</code>라고 입력한 순간, AI는 인벤토리 코드를 고치면서 조용히 캐릭터 이동 로직의 핵심 상수를 하드코딩으로 덮어쓰고, 셰이더 파이프라인을 날려버린다. 
              게임은 즉시 블랙 스크린으로 굳어버리고, 이전 상태로 되돌리기 위한 디버깅 지옥이 시작된다.
            </p>
            <p>
              이 참극의 원인은 모델의 지능 부족이 아니다. 
              <strong>'아무도 말리지 않는 무질서'</strong> 때문이다. 
              단일 챗봇 세션에는 설계 문서를 검토하는 시스템 기획자도 없고, 매직 넘버 하드코딩을 질타하는 테크니컬 리드도 없으며, 빌드가 깨졌을 때 PR을 즉시 리젝트하는 QA 엔지니어도 없다. 
              모든 작업을 혼자 처리하는 일반형 어시스턴트는 필연적으로 기술 부채와 스파게티 코드의 늪에 빠진다.
            </p>
            <p>
              이 구조적 모순을 정면으로 타파하며 깃허브를 뜨겁게 달군 프로젝트가 바로 <strong>Donchitos/Claude-Code-Game-Studios</strong>다. 
              공개 직후 무려 3만 3천 개 이상의 스타를 끌어모은 이 프로젝트는 단 하나의 명제를 제시한다. 
              <strong>"게임은 코더 한 명이 만드는 것이 아니다. 스튜디오의 규율(Discipline)이 만드는 것이다."</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 49개 에이전트, 74개 워크플로우 스킬의 '위계적 거버넌스'
            </h3>
            <p>
              <code>Claude-Code-Game-Studios</code>는 앤트로픽의 공식 코딩 에이전트인 Claude Code 환경 위에 **실제 AAA 게임 스튜디오의 조직도(Studio Hierarchy)**를 통째로 소프트웨어화하여 이식했다. 
              이 시스템 안에는 총 <strong>49개의 독립적인 특화 에이전트</strong>와 <strong>74개의 도메인 워크플로우 스킬</strong>, 그리고 15개의 자동 훅(Hooks)과 14개의 엄격한 품질 규칙(Rules)이 톱니바퀴처럼 맞물려 돌아간다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신이 '레이저 건을 추가해줘'라고 말하면, 과거에는 AI가 즉시 플레이어 스크립트를 열어잡고 난도질했습니다. 
                하지만 우리 스튜디오에서는 먼저 <strong>크리에이티브 디렉터</strong>가 게임의 톤앤매너를 승인하고, <strong>게임 디자이너</strong>가 밸런스 테이블을 작성하며, <strong>테크 리드</strong>가 컴포넌트 아키텍처를 검토한 뒤에야 <strong>주니어 프로그래머</strong>가 코드를 작성합니다. 마지막엔 <strong>QA 리드</strong>가 테스트를 통과시키지 못하면 병합조차 불가능합니다."
              </p>
              <small>— 프로젝트 창시자 Donchitos, 아키텍처 매니페스토 중</small>
            </div>

            <p>
              사용자는 여전히 프로젝트의 최고 의사결정자(Executive Producer)로 군림한다. 
              그러나 그 밑에는 사소한 실수도 용납하지 않고 질문을 던지며 스스로 코드를 검증하는 철통같은 49인의 전문가 팀이 24시간 상주하게 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 메커니즘 해부: 에스컬레이션 경로와 4단계 게이트웨이 파이프라인
            </h3>
            <p>
              스튜디오 아키텍처는 명확한 <strong>3계층 책임 구조</strong>와 <strong>순환 품질 게이트</strong>로 구성된다.
            </p>

            <!-- 순수 CSS 다이어그램: 49-Agent Studio Hierarchy & Quality Gate -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">STUDIO PIPELINE SCHEMATIC</span>
                <span class="schematic-title">Claude Code Game Studios: 3계층 위계 및 품질 검증 루프</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #8b5cf6;">
                  <div class="schematic-card-title" style="color: #6d28d9;">Tier 1: 스튜디오 디렉터 진영 (3 Agents)</div>
                  <div class="schematic-step">• Creative Director: 세계관, 톤앤매너, 핵심 재미 수호</div>
                  <div class="schematic-step">• Technical Director: 엔진 성능 예산(60fps), 아키텍처 규격 승인</div>
                  <div class="schematic-step">• Operations Director: 마일스톤 관리 및 에이전트 간 업무 병목 조율</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #3b82f6;">
                  <div class="schematic-card-title" style="color: #1d4ed8;">Tier 2: 도메인 리드 & 기획 (12 Agents)</div>
                  <div class="schematic-step">• Systems Designer: 경제, 능력치, 무기 수식 밸런싱</div>
                  <div class="schematic-step">• Art Lead & Audio Lead: 비주얼 무드보드 및 사운드스케이프 스펙</div>
                  <div class="schematic-step">• Gameplay Lead: FSM, 인풋 버퍼링, 카메라 쉐이크 규격화</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">Tier 3: 전문 엔지니어 & QA (34 Agents)</div>
                  <div class="schematic-step">• Shader / Physics / Netcode: 전문 도메인 코드 격리 작성</div>
                  <div class="schematic-step">• Refactor & Lint Specialist: 매직 넘버 색출, SOLID 원칙 감사</div>
                  <div class="schematic-step">• Automated QA Runner: 프레임 드랍 감지, 리그레션 회귀 테스트</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ 하위 엔지니어가 작성한 코드는 상위 리드의 승인과 QA 에이전트의 회귀 테스트 통과 없이는 절대 마스터 브랜치에 병합될 수 없도록 깃허브 훅과 Claude Code 규칙으로 강제된다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_game_studios.png" alt="Claude Code Game Studios 실행 대시보드" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ Claude Code Game Studios 실제 워크플로우 맵:</strong> 
                터미널 슬래시 커맨드(<code>/studio-plan</code>, <code>/review-pass</code>, <code>/qa-audit</code>) 입력 시 49개 에이전트가 호출 스택을 구성하며 실시간 콘솔에 직군별 승인 로그를 출력하는 장면.
              </div>
            </div>

            <p>
              이 시스템의 핵심 무기는 <strong>'문서와 코드의 동기화'</strong>다. 
              기존 AI 개발은 기획 문서 없이 코드부터 때려 박아 결국 길을 잃었다. 
              반면 Game Studios는 모든 기능 구현 전 <code>GDD(Game Design Document)</code>와 <code>TDD(Technical Design Document)</code>를 마크다운으로 먼저 작성하고, 변경 사항이 생기면 문서를 먼저 갱신한 뒤 코드를 일치시킨다. 
              AI 에이전트가 프로젝트 전체의 맥락을 잃어버리는 '컨텍스트 드리프트(Context Drift)' 현상이 원천 차단되는 이유다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 수천억 AAA 스튜디오 거버넌스의 대중화
            </h3>
            <p>
              너티독이나 에픽게임즈 같은 세계 최고의 게임사들이 수천억 원의 제작비를 쏟아붓는 이유는 단순히 코딩할 사람이 많아서가 아니다. 
              수백 명의 개발자가 서로의 코드를 깨뜨리지 않도록 통제하는 <strong>'제도와 프로세스'</strong>를 운영하는 데 돈이 들기 때문이다.
            </p>
            <p>
              <code>Claude-Code-Game-Studios</code>는 그 비싼 프로세스를 단 몇 메가바이트의 오픈소스 프롬프트 및 스킬 세트로 압축해 전 세계 인디 개발자들의 손에 쥐여주었다. 
              이제 방구석의 1인 개발자도 거대 스튜디오 부럽지 않은 엄격한 품질 관리 시스템을 공짜로 가동할 수 있게 되었다. 
              이는 인디 게임 시장의 기술적 완성도 기준치를 단숨에 AAA 급으로 끌어올리는 거대한 분기점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 규율이 창의성을 자유롭게 하리라
            </h3>
            <p>
              많은 이들이 AI가 가져올 미래를 '모든 규칙이 사라진 자유로운 혼돈'으로 상상했다. 
              하지만 실제 현장에서 창의적인 게임을 끝까지 완성해 내는 힘은 제멋대로 코드를 쏟아내는 마법이 아니라, 실수를 걸러내고 방향을 바로잡아주는 <strong>차가운 규율</strong>이었다.
            </p>
            <p>
              Claude Code Game Studios가 증명한 것은 인공지능 시대 소프트웨어 공학의 재발견이다. 
              규율이 세워졌을 때 비로소 1인 개발자는 사소한 버그와의 소모전에서 벗어나, 자신이 꿈꾸던 진짜 게임의 세계를 온전히 지어 올릴 수 있다.
            </p>

            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=claude+code+game+studios" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/Donchitos/Claude-Code-Game-Studios" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+33.5k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
