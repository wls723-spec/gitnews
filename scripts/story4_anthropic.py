# -*- coding: utf-8 -*-
# Story 4: Anthropic Knowledge Work Plugins

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] anthropics/knowledge-work-plugins : 앤스로픽 11대 지식 업무 플러그인 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_anthropic_plugins.jpg" alt="Anthropic Knowledge Work Plugins" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 98K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">💼 앤스로픽 공식 엔터프라이즈 생태계</span>
              <span class="platform-tag">GitHub Trending General & Python</span>
              <span class="platform-tag">anthropics / knowledge-work-plugins</span>
            </div>
            
            <h2 class="article-headline">
              앤스로픽, 전 사 전 직무를 위한 11대 오픈소스 전문 플러그인 생태계 전격 방출: Claude Cowork의 기업 침투 선언
            </h2>

            <div class="article-subheadline">
              "Plugins that turn Claude into a specialist for your role, team, and company" — 법무, 재무, 세일즈, 고객지원, 생명과학까지 아우르는 11개 프로덕션 플러그인 전격 오픈소스화… 단일 LLM 에이전트가 기업 수십 개 버티컬 SaaS를 집어삼키는 순간
            </div>
            <p class="article-snippet">
              클로드 코워크(Claude Cowork)를 전사적 엔터프라이즈 실무 동료로 전환시키는 공식 플러그인 아키텍처. 직무별 표준 스킬(Skills), 엔터프라이즈 API 커넥터, 전용 슬래시 커맨드, 하위 특화 에이전트 번들링으로 깃허브 전체 트렌딩 상위권 진입.
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
              <i data-lucide="layers"></i> 1. SaaS 파편화의 비극: 12개 탭을 오가는 지식 노동자들
            </h3>
            <p>
              오늘날 대다수 기업의 지식 노동자들은 브라우저 창에 20개가 넘는 SaaS 탭을 띄워놓고 하루를 보낸다. 
              법무팀은 아이언클래드(Ironclad)에서 계약서를 검토하고, 영업팀은 세일즈포스(Salesforce)에 파이프라인을 입력하며, 재무팀은 넷스위트(NetSuite)에서 전표를 대조하고, 기획팀은 지라(Jira)와 노션(Notion)에 로드맵을 쪼개 넣는다. 
              각각의 툴은 폐쇄적인 사일로(Silo)를 이루고 있으며, 기업들은 직원 한 명당 매달 수백 달러의 SaaS 라이선스 비용을 지불하면서도 이 파편화된 시스템 간의 데이터를 수동 복사-붙여넣기 하느라 하루 업무 시간의 40%를 허비하고 있다.
            </p>
            <p>
              LLM 챗봇의 도입조차 이 비극을 끝내지 못했다. 범용 챗봇은 회사의 구체적인 업무 맥락(Context)과 API 연동 방법을 알지 못해 "죄송하지만 저는 그 시스템에 접근할 권한이 없습니다"라는 무기력한 답변만 반복했다. 
              이 엔터프라이즈 지식 노동의 병목을 단숨에 베어 넘기기 위해, <strong>앤스로픽(Anthropic)</strong>이 자사의 핵심 엔터프라이즈 플랫폼인 <strong>Claude Cowork</strong>를 구동하는 <strong>11대 공식 프로덕션 플러그인(anthropics/knowledge-work-plugins)</strong>을 오픈소스로 전격 방출했다.
            </p>

            <div class="editorial-quote">
              "진정한 인공지능 협업은 '모든 것을 조금씩 아는 범용 지능'이 아니라, <strong>'우리 회사의 법무 검토 가이드라인과 재무 회계 기준을 완벽히 숙지한 전문 직무 파트너'</strong>에서 출발합니다. 
              우리가 자체 업무 현장에서 검증한 11개 도메인의 플러그인 사양을 오픈소스로 공개하는 이유는, 모든 기업이 자신들만의 독자적인 AI 실무자를 직접 조립하고 소유할 수 있도록 하기 위함입니다."
              <span class="quote-author">— 앤스로픽 엔터프라이즈 제품 총괄</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 버티컬 SaaS의 해자를 흡수하는 플러그인 아키텍처
            </h3>
            <p>
              앤스로픽이 이번에 공개한 리포지토리는 단순한 프롬프트 모음집이 아니다. 
              기업의 11개 핵심 기능—<strong>생산성(Productivity), 세일즈(Sales), 고객지원(Customer Support), 프로덕트 매니지먼트(Product Management), 마케팅(Marketing), 법무(Legal), 재무(Finance), 데이터 분석(Data), 엔터프라이즈 검색(Enterprise Search), 바이오 리서치(Bio-research), 플러그인 관리(Plugin Management)</strong>—을 담당하는 완결된 마이크로서비스 에이전트 번들이다.
            </p>
            <p>
              각각의 플러그인은 선언적 규격인 <code>plugin.json</code>을 바탕으로, 해당 직무에 특화된 정밀 도구(Skills), 기업 내부 API 커넥터(Connectors), 전용 슬래시 커맨드, 그리고 전문화된 하위 하네스 에이전트(Sub-agents)를 하나의 패키지로 묶어낸다. 
              수조 원의 기업가치를 자랑하던 수많은 버티컬 SaaS 스타트업들이 단일 LLM 에이전트의 '플러그인 설정 파일 하나'로 대체될 수 있다는 위기감이 실리콘밸리를 덮친 이유다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="git-merge" style="color:#8b5cf6;"></i> Anthropic Knowledge Work Plugins: 5단계 전사적 에이전트 오케스트레이션</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">ENTERPRISE PLUGIN FRAMEWORK</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 선언적 매니페스트</div>
                  <div class="step-title">plugin.json Manifest</div>
                  <div class="step-desc">불변 슬러그(Immutable Slug), 필요 권한 범위, 보안 샌드박스 정책을 정의하여 엔터프라이즈 거버넌스 준수.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 엔터프라이즈 커넥터</div>
                  <div class="step-title">API Connectors</div>
                  <div class="step-desc">Salesforce, Ironclad, DocuSign, Slack, NetSuite 등 사내 백엔드 시스템과 양방향 OAuth/REST 연동.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 직무 전용 스킬셋</div>
                  <div class="step-title">Domain Procedural Skills</div>
                  <div class="step-desc">계약서 면책조항(Indemnification) 위험도 평가, 재무 분개장 대조, PRD 스펙 초안 작성 등 절차적 지식 주입.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 전문 하위 에이전트</div>
                  <div class="step-title">Specialized Sub-Agents</div>
                  <div class="step-desc">단일 프롬프트가 아닌 '리스크 분석 에이전트', '규정 준수 에이전트'가 독립 교차 검증을 수행하는 멀티 에이전트 편대.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 완결된 업무 결과물</div>
                  <div class="step-title">Claude Cowork Delivery</div>
                  <div class="step-desc">단순 답변 텍스트가 아닌, 즉시 발송 가능한 레드라인 계약서, 대차대조표 엑셀, 지라 티켓으로 완결된 업무 산출물 인도.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="network"></i> 3. 기술 메커니즘 해부: 멀티 에이전트 협업과 변경 불가 보안 슬러그
            </h3>
            <p>
              앤스로픽 플러그인 아키텍처의 기술적 핵심은 <strong>'역할 분담 멀티 에이전트(Role-based Sub-agents)'</strong>와 <strong>'엄격한 보안 샌드박스'</strong>다:
            </p>
            <p>
              첫째, 예를 들어 <code>legal</code> 플러그인을 살펴보면, 하나의 에이전트가 모든 계약서를 읽지 않는다. 
              계약서가 인입되면 <code>indemnification_analyzer</code> 서브에이전트가 손해배상 한도 조항만 추출해 업계 표준 캡(Industry Standard Cap)과 대조하고, <code>liability_expert</code> 서브에이전트가 잠재적 소송 리스크를 독립 채점한다. 
              이후 메인 코워크 오케스트레이터가 두 전문가의 분석을 취합하여 인간 변호사에게 최종 수정안(Redline)을 제안한다. 
              이러한 분할 정복(Divide-and-Conquer) 아키텍처를 통해 환각률을 0.1% 이하로 억제한다.
            </p>
            <p>
              둘째, <strong>커넥터 표준화와 권한 격리(Permissions Isolation)</strong>다. 
              모든 플러그인은 <code>CONNECTORS.md</code> 명세에 따라 사내 시스템에 접근할 수 있는 최소 권한(Least Privilege) 원칙을 준수한다. 
              마케팅 플러그인은 재무 DB를 읽을 수 없으며, 법무 플러그인은 코드 저장소를 수정할 수 없다. 
              이는 엔터프라이즈 환경에서 보안 감사관들이 가장 엄격하게 요구하는 제로 트러스트(Zero Trust) 모델을 LLM 플러그인 레벨에서 구현한 것이다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_anthropic_plugins_catalog.jpg" alt="Anthropic Knowledge Work Plugins 디렉토리 및 법무 계약서 검토 실구동 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>VS Code 및 Claude Cowork 실구동 화면:</strong> 좌측 VS Code에 11대 지식 업무 플러그인 디렉토리 및 <code>legal/plugin.json</code> 선언문이 열려 있고, 우측 Claude Cowork 창에서 손해배상 조항(Indemnification) 위험도 8/10 감지 및 실시간 계약서 레드라이닝 검토가 수행되는 모습.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자: 수십조 원대 버티컬 SaaS 생태계의 재편
            </h3>
            <p>
              과거 실리콘밸리 벤처캐피털(VC)들이 수조 원을 투자했던 테마는 '특정 직무를 위한 AI 버티컬 SaaS'였다. 
              법무 전용 AI 스타트업, 영업 지원 AI, 고객센터 AI 스타트업들이 우후죽순 생겨났다. 
              그러나 앤스로픽이 최고의 지능을 가진 파운데이션 모델 위에 직무별 플러그인 사양을 오픈소스로 무료 배포함에 따라, <strong>"단순히 LLM API 위에 UI만 덧씌운 래퍼(Wrapper) 스타트업들"</strong>은 회복 불가능한 타격을 입게 되었다. 
              이제 기업들은 별도의 외부 SaaS를 도입하지 않고도, 자사의 지식과 API를 앤스로픽 오픈소스 플러그인 규격에 맞춰 사내 코워크에 장착하기만 하면 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 전 사의 지능화, 오픈소스 표준이 이끈다
            </h3>
            <p>
              인공지능이 기업의 실무를 대체한다는 공포를 넘어, 앤스로픽의 11대 플러그인이 보여준 길은 <strong>'인간 전문가의 지식과 노하우를 가장 투명하고 재사용 가능한 소프트웨어 규격으로 승화시키는 방법'</strong>이다. 
              회사의 모든 부서가 각자의 전문성을 코드로 정의하고 에이전트와 호흡하는 엔터프라이즈 지능화의 새로운 표준이 활짝 열렸다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=anthropic+claude+cowork+plugins" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/anthropics/knowledge-work-plugins" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 4 ready.")
