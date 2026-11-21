# -*- coding: utf-8 -*-
# Story 5: superdesigndev/treg

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] superdesigndev/treg                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_treg.jpg" alt="Treg OpenRouter for Agent Tools Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="key-round" style="width:12px;height:12px;fill:#fff;"></i> TOOL GATEWAY</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#d97706; color:#92400e;">💳 1센트 종량제로 B2B SaaS 월정액 벽을 부수는 도구 게이트웨이</span>
              <span class="platform-tag">GitHub Trending &amp; treg.to</span>
              <span class="platform-tag">superdesigndev / treg</span>
            </div>

            <h2 class="article-headline">
              "Semrush·Apollo 구독 없이 토큰 하나로 4,200개 API를 호출하라" — 에이전트 도구 경제의 OpenRouter 'treg'
            </h2>

            <div class="article-subheadline">
              136개 공급자의 4,200여 개 엔드포인트(SEO·백링크·트렌드·음성합성·스크래핑)를 단일 Base URL·단일 토큰으로 호출당 수 센트 과금, 서버 사이드 인증 주입 릴레이 및 사내 API/CLI/SKILL.md 무료 공유까지 셀프호스팅 지원 (+116스타/일, 누적 8,710스타)
            </div>
            <p class="article-snippet">
              코딩 에이전트에게 경쟁사 백링크 3건과 숏폼 트렌드 데이터, 성우 음성 1클립만 뽑아오라고 시키려 해도, 인간은 Semrush(월 $139)·Apollo(좌석당 $59)·각종 데이터 공급사 회원가입과 API 승인 대기줄 앞에서 좌절해야 했습니다. 오늘 하루 116스타를 더하며 누적 8,710스타를 돌파한 <strong>superdesigndev/treg</strong>는 과거 OpenRouter가 LLM API 파편화를 끝냈듯, 에이전트가 필요로 하는 4,200여 개 외부 도구와 사내 CLI·스킬을 단일 게이트웨이와 서버 사이드 시크릿 릴레이로 통합했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 1센트짜리 API 호출 한 번을 위해 월 $139를 결제하던 모순
            </h3>
            <p>
              에이전트에게 진짜 세상의 일을 시키는 순간, 개발자들은 모델 지능이 아니라 '자격 증명(Credentials)과 월정액 구독'의 장벽에 부딪힌다. 마케팅 리서치를 시키려면 Semrush($139/월)·Moz($99/월) 계정을 파야 하고, 리드 발굴을 하려면 Crunchbase($99/월)·Apollo($59/석)에 카드를 긁어야 하며, 어떤 데이터 API는 아예 파트너 심사 없이는 키조차 내주지 않는다. 반대로 팀 내부에서 이미 유료 계정을 갖고 있더라도, 모든 팀원의 로컬 에이전트 환경변수에 마스터 API 키를 복사해 뿌리는 것은 보안 재앙이다.
            </p>
            <p>
              Superdesign 팀이 구축해 공개하고 라이브 서비스(<code>treg.to</code>)와 셀프호스팅 코드까지 함께 배포한 <strong>superdesigndev/treg</strong>(오늘 +116스타, 누적 8,710스타)는 이 답답한 구조를 한 방에 뒤집었다. 에이전트에게 필요한 것은 공급사 이름이 아니라 "도메인 백링크 조회(<code>treg catalog search "backlinks for a domain"</code>)"라는 작업 의도이며, 결제는 호출당 1센트 안팎의 선불 마이크로 과금으로 끝난다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "도구의 이름을 묻지 말고, 하려는 일을 검색해 호출하라"
            </h3>
            <p>
              <code>treg</code>의 핵심 발상은 <strong>"에이전트 도구를 위한 OpenRouter"</strong>라는 한 문장으로 요약된다. 136개 공급자의 4,200개 이상 엔드포인트를 시맨틱 검색 가능한 단일 카탈로그로 묶고, 호출자의 요청을 받을 때는 단 하나의 토큰(<code>X-Treg-Token</code>)만 요구한다.
            </p>

            <div class="editorial-quote">
              <p>
                "프록시는 업스트림을 <strong>모델링하지 않고 그대로 릴레이하며, 인증(Auth)은 오직 서버 사이드에서만 주입한다.</strong> 덕분에 업스트림 API가 바뀌어도 살아남고, 호출하는 에이전트는 단 하나의 시크릿 키도 손에 쥐지 않는다."
              </p>
              <small>— superdesigndev/treg 프록시 설계 제1원칙</small>
            </div>

            <p>
              더욱 강력한 점은 <strong>'내 키(Your Own Tools) 우선 원칙'</strong>이다. 팀원이 사내 유료 API 키, OAuth 토큰, <code>stripe</code>·<code>gh</code>·<code>vercel</code> 같은 벤더 CLI, 또는 <code>SKILL.md</code> 번들을 팀 레지스트리에 등록해 두면, 모든 팀원의 에이전트가 키를 직접 보지 못한 채 서버 릴레이를 통해 호출할 수 있으며 <strong>자체 키를 탄 호출은 일절 과금(Metering)되지 않는다.</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Base URL 드롭인 교체 · <code>strict_query</code> 가드 · CLI/MCP 인젝션 해부
            </h3>
            <p>
              <code>treg</code>가 수천 개의 이기종 API와 CLI를 깨짐 없이 중계하기 위해 도입한 아키텍처는 매우 실용적이다:
            </p>
            <ul>
              <li><strong>원라인 Base URL 스위칭 &amp; 시맨틱 카탈로그:</strong> 기존 SDK나 클라이언트의 Base URL만 <code>https://api.dataforseo.com/v3</code>에서 <code>https://treg.to/call/dataforseo</code>로 바꾸면 그대로 동작한다. <code>treg catalog search</code>로 작업 목적에 맞는 도구를 찾고 가격을 확인한 뒤 즉시 호출한다.</li>
              <li><strong>환각 과금 방지용 <code>strict_query</code> 스키마 가드:</strong> AI 에이전트가 존재하지 않는 파라미터를 지어내 API 호출 실패를 일으키며 잔액을 태우는 문제를 막기 위해, 선언되지 않은 파라미터나 중복 쿼리·지원되지 않는 타입이 들어오면 프록시 단에서 즉시 <code>400 catalog_parameter_invalid</code>로 차단하고 <strong>과금을 0원으로 처리</strong>한다.</li>
              <li><strong>이중 인증 바인딩 &amp; CLI·Claude Code 플러그인:</strong> OAuth Bearer와 개발자 토큰 헤더를 동시에 주입하는 다중 바인딩을 지원하며, Claude Code에서는 <code>/plugin marketplace add superdesigndev/treg</code> 두 줄로 설정 없이 즉시 마켓플레이스 스킬과 도구 카탈로그를 장착한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">treg 단일 토큰 도구 게이트웨이 및 서버 사이드 인증 릴레이 구조</span>
                <span class="schematic-badge">4,200+ Endpoints · 136 Providers · Zero Client-Side Secrets · Self-Hostable</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Intent Discovery &amp; Guard</div>
                  <div class="schematic-desc">
                    <code>treg catalog search</code> 목적 기반 검색<br>
                    단일 토큰(<code>X-Treg-Token</code>) / Claude 플러그인<br>
                    <code>strict_query</code> 파라미터 환각 차단<br>
                    (오류 시 400 반환 · 과금 0원)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Blind Auth-Injecting Relay</div>
                  <div class="schematic-desc">
                    업스트림 스키마 왜곡 없는 순수 릴레이<br>
                    서버 사이드 OAuth/헤더/CLI 시크릿 주입<br>
                    자체 팀 키(BYOK) 등록 시 무조건 우선 적용<br>
                    (팀 키·익명 공개 라우트는 과금 0원)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Catalog &amp; Team Toolbelt</div>
                  <div class="schematic-desc">
                    136개 공급사 4,200+ API (1센트~ 종량제)<br>
                    DataForSEO·TikHub·Fish Audio·스크래핑<br>
                    사내 <code>stripe/gh/vercel</code> CLI 공유<br>
                    <code>SKILL.md</code> + 도구 + 시크릿 원패키지
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">treg.to 공식 라이브 플랫폼 실화면 — 4,200+ 엔드포인트 · 136개 공급자 통합 라우터</span>
              </div>
              <img src="../assets/images/demo_treg.png" alt="Treg OpenRouter for Agent Tools Official Platform Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ treg.to 공식 사이트 실화면: Codex 등 코딩 에이전트가 단일 <code>treg</code> 토큰과 <code>llms.txt</code>만으로 TikTok·Instagram·X·YouTube·Reddit·LinkedIn 등 1,600+ 소셜 엔드포인트 포함 4,200여 도구를 API 승인 대기 없이 호출하는 구조.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: SaaS '시트(Seat) 경제'에서 에이전트 '마이크로 콜 경제'로의 지각변동
            </h3>
            <p>
              지난 15년간 B2B SaaS 산업을 지배한 수익 모델은 "매달 모든 사용자에게 월 $50~$150의 고정 구독료(Seat-based Subscription)를 청구하는 것"이었다. 그러나 자율 에이전트는 월정액 대시보드를 로그인해 구경하지 않는다. 오직 필요할 때 API 엔드포인트 1~2개를 0.5초 만에 호출할 뿐이다.
            </p>
            <ul>
              <li><strong>에이전트 시대의 Long-Tail API 유동화:</strong> <code>treg</code>는 기존 데이터·마케팅 SaaS들이 막아둔 '최소 월정액 벽'을 중개 게이트웨이로 허물고, 트래픽을 호출당 마이크로 과금(Pay-per-call)으로 잘게 쪼개 에이전트 시장에 공급한다.</li>
              <li><strong>팀 시크릿 거버넌스의 표준화:</strong> 대기업이나 스타트업 보안팀 입장에서 "모든 개발자 노트북에 수십 개 SaaS API 키가 흩어져 있는 상태"는 최악의 감사 리스크다. 팀의 모든 도구와 시크릿을 셀프호스팅 가능한 <code>treg</code> 레지스트리 뒤에 숨기고 <code>treg health</code>로 일괄 점검할 수 있다는 점은 기업 채택의 강력한 명분이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 모델 라우터 다음은 '도구 라우터'다
            </h3>
            <p>
              OpenAI와 Anthropic, Gemini와 오픈웨이트 모델의 파편화가 OpenRouter라는 단일 라우터 계층을 탄생시켰듯, 수천 개의 API와 SaaS로 흩어진 에이전트의 손발 역시 결국 하나의 게이트웨이로 모일 수밖에 없다.
            </p>
            <p>
              가입 절차와 월정액의 벽을 넘어 1센트짜리 호출 하나로 에이전트에게 웹과 데이터의 실권을 쥐여주는 <code>treg</code>는, AI 에이전트가 '말만 하는 챗봇'에서 '실제 돈을 쓰고 도구를 부리는 경제 주체'로 넘어가는 가장 현실적인 다리를 놓고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=treg+OpenRouter+for+agent+tools" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://treg.to" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 플랫폼 / 카탈로그
              </a>
              <a href="https://github.com/superdesigndev/treg" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
