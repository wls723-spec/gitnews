# -*- coding: utf-8 -*-
# Story 3: superplanehq/superplane - Autonomous One-Shot Engineering Factory

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 3] superplanehq/superplane : Go Trending 1위 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_superplane.jpg" alt="SuperPlane Autonomous Software Factory" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> GO TRENDING</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag highlight-badge">🚀 깃허브 이슈가 스스로 PR이 되는 공장</span>
              <span class="aggro-tag">🔥 100% 온프레미스 자율 엔지니어링</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">superplanehq / superplane</span>
            </div>
            
            <h2 class="article-headline">
              "이슈만 올리면 PR이 완성되어 날아온다" — 원샷(One-Shot) 소프트웨어 자율 엔지니어링 팩토리 'SuperPlane'
            </h2>

            <div class="article-subheadline">
              단순 챗봇과 코파일럿의 한계를 넘어선 백로그(Backlog)→구현(Implement)→검증(Verify)→PR 완결 파이프라인: Go 기반 무정지 자율 개발자 공장의 등장
            </div>
            <p class="article-snippet">
              개발자가 터미널에 붙어 앉아 에이전트와 대화를 주고받아야 했던 기존 '바이브 코딩'의 한계를 깬 오픈소스 자율 엔지니어링 플랫폼 'SuperPlane'이 화제입니다. 깃허브 백로그 이슈를 스스로 분석하고, 격리된 샌드박스에서 빌드와 테스트를 통과시킨 후 검증된 PR까지 전자동으로 제출하는 이 단일 Go 바이너리 시스템의 내부 구조를 파헤칩니다.
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
              <i data-lucide="flame"></i> 1. 리드: 채팅창을 벗어나 진짜 '공장 라인'으로 들어간 AI
            </h3>
            <p>
              2024~2025년의 AI 코딩 열풍은 '채팅창 안의 조수'에 갇혀 있었다. 
              개발자가 프롬프트를 쳐 넣고, 에이전트가 코드를 토해내면, 
              개발자가 다시 터미널에서 컴파일 에러를 확인하고 에이전트에게 오류 로그를 복사해 붙여넣는 끝없는 핑퐁의 연속이었다. 
              생산성은 늘어났지만, 결국 인간 엔지니어가 에이전트의 모니터 앞 베이비시터로 전락했다는 회의론이 팽배했다.
            </p>
            <p>
              오늘 깃허브 Go 랭킹을 집어삼킨 <strong>superplanehq/superplane</strong>(스타 9,435개 돌파)은 
              이 지루한 패러다임에 근본적인 종언을 고한다. 
              SuperPlane은 인간과의 대화형 인터랙션을 최소화하고, 소프트웨어 개발을 <strong>포드 자동차의 콘베이어 벨트 조립 라인처럼 규격화된 '공장(Factory)'의 개념으로 재정의</strong>한 프로젝트다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '원샷 엔지니어링(One-Shot Engineering)'의 충격
            </h3>
            <p>
              SuperPlane의 동작 원리는 믿을 수 없을 정도로 간결하다. 
              기획자나 엔지니어가 GitHub이나 지라(Jira)에 버그 리포트나 신규 기능 요구사항(Issue)을 등록하면, 
              공장의 파이프라인이 즉각 가동된다:
            </p>

            <div class="editorial-quote danger">
              <p>
                "우리는 더 이상 에이전트에게 '이 버그 고쳐줘'라고 애원하고 기다리지 않는다. 
                <strong>SuperPlane은 백로그 이슈를 입력받아 도메인 스펙을 역엔지니어링하고, 격리된 마이크로VM에서 E2E 테스트를 스스로 작성·통과시킨 뒤 즉시 머지 가능한 PR을 완성한다.</strong> 
                소프트웨어 엔지니어링이 비로소 수작업 공예에서 무인 자동화 공장으로 진화했다."
              </p>
              <small>— SuperPlane 아키텍처 화이트페이퍼 & 엔지니어링 커뮤니티 발췌</small>
            </div>

            <p>
              코드 변경뿐만 아니라 기존 CI 파이프라인을 그대로 물려받아, 
              단위 테스트, 린트(Lint), 통합 회귀 테스트가 100% 그린 라이트를 켤 때까지 
              에이전트가 자체 수정 루프(Self-healing loop)를 백그라운드에서 격리 수행한다. 
              인간 리뷰어는 완성된 PR과 테스트 증명 리포트만을 검토하고 'Merge' 버튼만 누르면 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 기술 아키텍처: 4단계 결정론적 스테이지와 Go 동시성
            </h3>
            <p>
              SuperPlane이 수많은 조잡한 자율 에이전트 프로젝트들과 결정적으로 궤를 달리하는 비결은, 
              확률적인 LLM을 엄격한 소프트웨어 검증 파이프라인에 가둔 아키텍처에 있다:
            </p>
            <ul>
              <li><strong>Backlog Ingestion & Specification Synthesis:</strong> 깃허브 웹훅으로 수신된 이슈에서 모호성을 제거하고, 프로젝트의 README, 아키텍처 문서, 기존 테스트 코드를 분석하여 단일 '실행 명세서(Spec Contract)'를 자동 도출.</li>
              <li><strong>Ephemeral Sandbox Isolation:</strong> 컨테이너나 호스트를 오염시키지 않도록 임베디드 가상화 환경을 즉각 프로비저닝. 에이전트가 컴파일과 의존성 설치, 마이그레이션을 안전하게 수행.</li>
              <li><strong>Verification Engine & Self-Correction:</strong> 테스트 실패 시 로그 트레이스를 에이전트에게 피드백하여 최대 허용 반복 내에서 코드 자가 수정. 무한 루프나 슬롭 방지를 위한 토큰 세이프가드 가동.</li>
              <li><strong>Review-Ready Pull Request Assembly:</strong> 변경 사유, 전후 아키텍처 다이어그램, 테스트 통과 스크린샷과 커버리지 리포트를 정갈하게 마크다운으로 작성하여 원클릭 머지 상태로 제출.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">SuperPlane One-Shot Engineering 4단계 자율 조립 라인</span>
                <span class="schematic-badge">Pipeline Factory Flow</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Backlog Ingestion</div>
                  <div class="schematic-desc">
                    GitHub / GitLab 이슈 수신<br>
                    코드베이스 AST 및 컨텍스트 파싱<br>
                    결정론적 실행 스펙 자동 수립
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Implement & Verify</div>
                  <div class="schematic-desc">
                    격리 샌드박스 내 코드 자율 작성<br>
                    테스트 실행 및 자가 치유(Self-healing)<br>
                    Zero-Human 의존성 루프
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Verified PR Ship</div>
                  <div class="schematic-desc">
                    CI 100% 그린 통과 보증<br>
                    완전한 테스트 증명 리포트 동봉<br>
                    인간 리뷰어 최종 1초 승인
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">SuperPlane 대시보드 및 실시간 이슈 공장 파이프라인</span>
              </div>
              <img src="../assets/images/demo_superplane.png" alt="SuperPlane Software Factory Live UI" class="showcase-img">
              <p class="showcase-caption">
                ▲ superplane.com 라이브 런타임: Backlog, Implement, Verify, Done 4단계 칸반 보드 위에서 자율 에이전트들이 깃허브 이슈를 병렬로 픽업해 테스트 검증 완료 PR로 전환하는 무인 팩토리 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 파괴력: 연간 수억 원 SaaS 구독을 대체하는 온프레미스 자립성
            </h3>
            <p>
              최근 코그니션(Cognition)의 데빈(Devin)이나 깃허브 워크스페이스 같은 상용 자율 에이전트 SaaS는 
              좌석당 수십만 원의 고가 구독료와 소스코드 외부 반출이라는 보안 위험을 안고 있었다. 
              기업의 소스코드 전체를 사설 클라우드로 넘겨야 하는 제약 때문에 금융, 방산, 의료 분야는 이를 도입할 엄두조차 내지 못했다.
            </p>
            <p>
              SuperPlane은 <strong>단일 Go 바이너리로 컴파일되어 사내 자체 서버(On-premise)나 사설 VPC에 단 1분 만에 배포</strong>된다. 
              OpenAI, Anthropic뿐만 아니라 로컬 Ollama나 vLLM(DeepSeek) 모델과도 자유롭게 결합되어 
              단 1바이트의 지적 재산권(IP) 유출 없이 완전한 무인 개발 공장을 회사 내부망에 구축할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 개발자는 지휘자가 되고, 공장은 코드를 짠다
            </h3>
            <p>
              SuperPlane이 열어젖힌 미래는 개발자의 소멸이 아니라, 
              개발자가 일일이 오타를 잡고 빌드 오류와 씨름하던 막노동에서 해방되어 
              '아키텍처의 의사결정권자'로 거듭나는 전환점이다. 
              이슈 티켓 한 장이 완벽한 소프트웨어로 변환되어 머지되는 세상. 
              SuperPlane은 오픈소스가 엔터프라이즈 엔지니어링의 문법을 어떻게 재작성하는지 보여주는 살아있는 교과서다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=SuperPlane+autonomous+engineering+factory" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://superplane.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> SuperPlane 공식 사이트 방문
              </a>
              <a href="https://github.com/superplanehq/superplane" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
