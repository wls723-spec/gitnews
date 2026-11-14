# -*- coding: utf-8 -*-
# Story 5: every-app/open-seo

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] every-app/open-seo                               -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openseo.jpg" alt="OpenSEO Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> SAAS DISRUPTOR</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#166534;">💸 월 20만 원 Semrush·Ahrefs 해체</span>
              <span class="platform-tag">GitHub TS Trending & openseo.so</span>
              <span class="platform-tag">every-app / open-seo</span>
            </div>
            
            <h2 class="article-headline">
              월 수십만 원대 Semrush·Ahrefs 독점에 반기 든 'OpenSEO': 내 API 키(BYOK)로 쓴 만큼만 내고, Claude·Codex 에이전트가 MCP로 직접 검색 시장을 감사한다
            </h2>

            <div class="article-subheadline">
              키워드 리서치·순위 추적·백링크·사이트 감사·AI 가시성 분석을 종량제 DataForSEO API와 Docker/Cloudflare 무료 셀프호스팅으로 해방하고, 에이전트 전용 MCP 서버·스킬까지 직결한 오픈소스 SEO 플랫폼
            </div>
            <p class="article-snippet">
              스타트업과 인디 개발자가 검색엔진 최적화(SEO) 데이터를 보려면 Semrush나 Ahrefs에 매달 139~499달러에 달하는 고정 구독료를 바쳐야 했습니다. 쓰지도 않는 기능까지 억지로 묶어 파는 이 거대한 B2B SaaS 성벽을 향해 오픈소스 프로젝트 'OpenSEO'(27,717 스타)가 정면 돌파를 선언했습니다. DataForSEO API 키를 직접 연결해 실제 호출한 만큼만 몇 달러 수준으로 지불하고, Cloudflare Workers 무료 플랜이나 Docker로 1분 만에 자체 호스팅할 수 있으며, 무엇보다 Claude Code·ChatGPT·Codex가 MCP를 통해 직접 SEO 감사와 콘텐츠 전략을 실행합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 쓰지 않아도 매달 빠져나가는 $139~$499, B2B SaaS '번들링 세금'의 붕괴
            </h3>
            <p>
              수년간 디지털 마케팅과 그로스 엔지니어링 영역은 Semrush와 Ahrefs라는 양대 공룡이 사실상 과점해왔다. 키워드 검색량 몇백 개를 조회하고 경쟁사 백링크를 확인하고 싶을 뿐인데도, 1년에 수백만 원에 달하는 월정액 구독과 시트당 추가 요금, 그리고 API 접근권을 인질로 잡은 엔터프라이즈 요금제를 피할 길이 없었다.
            </p>
            <p>
              TypeScript 주간 트렌딩 상위권에서 27,717개 이상의 스타를 기록하며 폭발적인 지지를 얻고 있는 <strong>every-app/open-seo</strong>는 이 구시대적 구독 모델에 정면으로 사망 선고를 내린다. 데이터 원천 API와 깔끔한 오픈소스 UI, 그리고 AI 에이전트 프로토콜이 결합할 때 기존의 비대한 SaaS가 얼마나 순식간에 증발하는지를 보여주는 교과서적 사례다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: UI 클릭을 넘어 'AI 에이전트'를 1급 사용자로 설계한 차세대 SEO 스택
            </h3>
            <p>
              OpenSEO가 단순한 오픈소스 대시보드 클론에 그치지 않고 순식간에 개발자들의 필수 도구로 자리 잡은 이유는 <strong>'에이전트 네이티브(Agent-Native)' 아키텍처</strong>에 있다. 사람이 대시보드에서 CSV를 다운받아 분석하는 시대는 끝났다. 코딩 에이전트가 웹앱 소스코드와 SEO 데이터를 동시에 쥐고 있어야 진짜 수정이 일어난다.
            </p>

            <div class="editorial-quote">
              <p>
                "<strong>구독료는 없다. 본인의 DataForSEO API 키를 연결해 실제 사용한 만큼만 지불(Pay-as-you-go)하면 된다.</strong> 또한 OpenSEO는 <strong>전용 MCP 서버와 재사용 가능한 Agent Skills</strong>를 노출하므로, Claude Code·OpenClaw·Hermes·ChatGPT·Codex 같은 AI 에이전트가 당신의 SEO 데이터를 직접 읽어 6대 핵심 워크플로우를 수행한다."
              </p>
              <small>— EveryApp / OpenSEO 공식 README &amp; 아키텍처 개요</small>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 6대 SEO 워크플로우 + Docker/Cloudflare 서버리스 배포 + MCP 직결
            </h3>
            <p>
              OpenSEO는 거대한 레거시 SaaS에서 군더더기를 모두 도려내고, 실무에 필수적인 6개 워크플로우를 현대적 웹 기술과 에이전트 인터페이스로 재구축했다:
            </p>
            <ul>
              <li><strong>6대 핵심 워크플로우:</strong> 키워드 리서치, 실시간 순위 추적(Rank Tracking), 경쟁사 인사이트, 백링크 분석, 사이트 기술 감사(Site Audits), 그리고 생성형 AI 검색 시대에 필수인 <strong>AI 가시성(AI Visibility)</strong> 추적까지 단일 앱에 통합.</li>
              <li><strong>유연한 제로 비용 셀프호스팅:</strong> Docker Compose(Coolify, Portainer, Dokploy 호환)로 개인 서버나 Tailscale 사설망 뒤에 로그인 없는 사내 전용 모드로 띄우거나, 서버 유지비 0원인 <strong>Cloudflare Workers 무료 플랜 + Cloudflare Access</strong> 인증으로 원클릭 배포가 가능하다.</li>
              <li><strong>MCP 서버 &amp; Agent Skills 표준 탑재:</strong> ChatGPT(무료·유료 모두 지원), Codex, Claude Code, Cursor가 동일한 MCP 엔드포인트로 접속해 "우리 사이트에서 기술 감사 오류가 뜬 페이지 메타태그를 PR로 바로 고쳐줘" 같은 종단간 자동화를 실행한다.</li>
            </ul>

            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">OpenSEO 무구독(BYOK) 셀프호스팅 및 MCP 에이전트 직결 구조</span>
                <span class="schematic-badge">Zero-Subscription Agentic SEO</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">BYOK Raw Data Tier</div>
                  <div class="schematic-desc">
                    DataForSEO 종량제 API 직결<br>
                    고정 월정액 $139~$499 완전 제거<br>
                    호출량만큼만 실비 과금(수 달러 수준)<br>
                    데이터 주권 및 쿼리 완전 통제
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">OpenSEO Core &amp; MCP Server</div>
                  <div class="schematic-desc">
                    키워드 · 순위 · 백링크 · AI 가시성<br>
                    Cloudflare 무료 플랜 / Docker 배포<br>
                    Tailscale &amp; CF Access 보안 격리<br>
                    포크 및 커스텀 워크플로우 자유 확장
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">AI Agent Execution Layer</div>
                  <div class="schematic-desc">
                    Claude Code · Codex · ChatGPT 연동<br>
                    사전 구축된 Agent Skills 워크플로우<br>
                    감사 결과 &rarr; 코드/메타태그 즉시 패치<br>
                    분석에서 배포까지 단일 루프 완결
                  </div>
                </div>
              </div>
            </div>

            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">OpenSEO 공식 웹 플랫폼(openseo.so) 및 워크플로우 인터페이스</span>
              </div>
              <img src="../assets/images/demo_openseo.png" alt="OpenSEO Official Web Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ openseo.so 실구동 화면: Semrush·Ahrefs의 복잡한 UI 대신 키워드 리서치, 경쟁사 분석, AI 가시성 감사와 MCP 연동을 직관적으로 제공하는 오픈소스 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 시장 충격: '데이터 언번들링(Unbundling)'이 쏘아 올린 SaaS 종말론
            </h3>
            <p>
              과거의 B2B SaaS 해자는 두 가지 위에 세워졌다: "원천 데이터를 긁어 모으는 크롤링 파이프라인"과 "그걸 보여주는 깔끔한 웹 대시보드". 하지만 DataForSEO 같은 로우 데이터 API 공급자들이 가격을 파괴하고, 오픈소스 커뮤니티와 바이브 코딩이 대시보드 구축 비용을 0원으로 낮추면서 중간 마진을 취하던 거대 SaaS들의 해자가 허물어지고 있다.
            </p>
            <ul>
              <li><strong>EveryApp 생태계의 파괴력:</strong> 개발 팀 `every-app`은 OpenSEO 외에도 각종 과금형 SaaS를 사용자가 직접 포크하고 수정해 셀프호스팅하는 오픈소스 앱 플랫폼을 구축 중이며, 맘에 들지 않는 화면이 있으면 AI에게 시켜 입맛대로 고쳐 쓰는 '소프트웨어 자급자족' 모델을 현실화하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 이제 모든 SaaS는 'API 원가 + 오픈소스 UI + MCP'로 환원된다
            </h3>
            <p>
              "사람이 마우스로 클릭하는 대시보드"에 월 수십만 원을 청구하던 시대는 끝나가고 있다. 앞으로 살아남는 소프트웨어는 인간이 아니라 AI 에이전트가 MCP로 가장 깔끔하게 호출할 수 있거나, 사용자가 비용을 투명하게 통제하며 자기 인프라 위에 얹을 수 있는 도구뿐이다.
            </p>
            <p>
              OpenSEO는 그 거대한 SaaS 해체 도미노가 SEO 마케팅 산업의 한복판에서 이미 시작되었음을 알리는 가장 선명한 신호탄이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=OpenSEO+open+source+Semrush+alternative+MCP" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://openseo.so" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹 앱 방문
              </a>
              <a href="https://github.com/every-app/open-seo" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
