# -*- coding: utf-8 -*-
# Story 2: hieunc229/mailflare + Google Workspace MCP Lockdown

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] hieunc229/mailflare : Google Workspace Exodus    -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_mailflare.jpg" alt="Mailflare Self-Hosted Google Workspace Alternative on Cloudflare Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="mail" style="width:12px;height:12px;"></i> WORKSPACE EXODUS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔒 구글 AI 에이전트 Gmail 전송 봉쇄 역풍 · Cloudflare 무료 셀프호스팅 대이동</span>
              <span class="platform-tag">GitHub Trending &amp; HN 180점</span>
              <span class="platform-tag">hieunc229 / mailflare</span>
            </div>

            <h2 class="article-headline">
              "구글이 AI 에이전트의 Gmail 발송을 막자, 개발자들은 워크스페이스를 통째로 Cloudflare로 옮긴다" — 'Mailflare'
            </h2>

            <div class="article-subheadline">
              2027년 2월부터 AI 에이전트의 REST API 직접 호출을 금지하고 '메일 발송 불가능한' 공식 MCP만 강제한 구글 약관 개정에 맞서, 커스텀 도메인 메일·캘린더·드라이브·부킹·무제한 에이전트 MCP를 무료로 셀프호스팅 (★7,747 · +86★/d · AGPL-3.0)
            </div>
            <p class="article-snippet">
              구글이 11월 24일 발표한 <strong>Workspace AI Tools 부칙</strong>이 개발자 생태계에 불을 질렀습니다. 내년 2월 1일부터 모든 AI 에이전트는 구글 공식 MCP 서버를 경유해야 하며(REST 직접 호출 시 최하위 할당량 제한), 정작 Gmail MCP는 <strong>메일 전송·답장·전달 도구를 일반 개발자에게 막아두었기 때문</strong>입니다(HN <strong>180점·179댓글</strong>). 탈출구를 찾던 개발자들이 몰려든 곳이 하루 만에 ★86을 추가하며 총 <strong>★7,747</strong>에 도달한 <strong>hieunc229/mailflare</strong>입니다. Cloudflare Workers(D1·R2) 무료 티어나 Docker 단일 컨테이너에 이메일·캘린더·드라이브·예약·Takeout 마이그레이션과 제약 없는 MCP 에이전트까지 통째로 띄울 수 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 60일 시한부 통보와 '발송 버튼 없는' Gmail MCP의 역설
            </h3>
            <p>
              2026년 11월 24일, 구글이 8개의 공식 Google Workspace MCP 서버를 정식 출시(GA)하며 슬쩍 끼워 넣은 API 약관 조항 하나가 실리콘밸리와 인디 개발자 커뮤니티를 발칵 뒤집어 놓았다. 새 부칙(Workspace AI Tools Addendum)은 단호했다: <em>"AI 에이전트·하네스·모델이 구동하는 모든 GWS 접근 도구는 반드시 구글 공식 MCP를 사용해야 하며, 에이전트임을 위장해 회피할 수 없다."</em> 2027년 2월 1일부터 기존의 Gmail·Drive REST API를 직접 부르는 AI 비서는 유료 등급과 무관하게 최저 스탠다드 쿼터로 강등되고 계정 정지 위험까지 지게 된다.
            </p>
            <p>
              진짜 폭탄은 공식 Gmail MCP 서버의 도구 목록을 열어본 순간 터졌다. 메일 검색, 스레드 읽기, 라벨 분류, <strong>초안(Draft) 생성</strong>까지는 가능했지만, 정작 <strong>메일 발송(Send), 답장(Reply), 전달(Forward), 초안 수정</strong> 도구는 <em>"파트너 액세스 전용이며 일반 제공되지 않음"</em>으로 잠겨 있었다. 구글 생태계 위에서 자율 메일 비서와 코딩 에이전트 플러그인을 돌리던 개발자들에게 사실상 60일짜리 사형 선고가 내려진 셈이다. 바로 그날, GitHub 트렌딩 TypeScript 부문 상위권에서 폭발적인 관심을 끌어모은 프로젝트가 오픈소스 Google Workspace 대체제 <strong><code>hieunc229/mailflare</code></strong>(총 ★7,747 · 포크 1,386)였다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "왜 구글이 사서 내 계정을 막는가" — 에이전트 시대의 플랫폼 봉쇄
            </h3>
            <p>
              이번 충돌은 단순한 보안 정책 조정이 아니라 <strong>빅테크의 '에이전트 세금(Agent Tax)'과 플랫폼 주권 전쟁</strong>을 상징한다. 오픈AI나 앤스로픽 같은 외부 에이전트 UI 안에서는 구글이 Gmail 광고를 띄울 수도, Gemini 업셀을 유도할 수도 없다. 결국 빅테크는 "에이전트는 우리 관문을 통과하라"며 표준을 내세우지만 실제로는 핵심 쓰기 권한을 거세해 써드파티 자동화를 질식시킨다. <code>Mailflare</code>는 바로 그 반작용으로 부상했다: 도메인 메일부터 캘린더, 드라이브, 일정 예약(Cal.com 대체), 그리고 외부 AI 도구를 붙이는 MCP 서버까지 <strong>단 하나의 TypeScript 코드베이스</strong>로 묶어 내 서버나 Cloudflare 엣지 위에 무료로 세울 수 있게 해준다.
            </p>

            <div class="editorial-quote">
              <p>
                "Gmail은 OpenAI나 Anthropic의 UI 안에서 일반 사용자에게 광고를 보여줄 수 없으니 이런 짓을 하는 것이다. <strong>나는 지난 10년간 구글 인프라에 묶여 있었지만, 이번 조치는 10년의 종속을 끊고 탈출할 충분한 계기가 된다.</strong>"
              </p>
              <small>— Hacker News <em>Google Workspace MCP</em> 토론 스레드 (180점·179댓글)</small>
            </div>

            <p>
              토론 스레드에 <em>"이메일·드라이브·문서를 구글 밖으로 옮길 대안이 있느냐"</em>는 질문이 빗발친 직후, <code>Mailflare</code>가 제공하는 <strong>Gmail Takeout(`.mbox` / `.eml`), Google Calendar, Google Contacts, Google Drive 원클릭 일괄 임포트</strong> 기능은 단순한 흥미 거리가 아니라 즉각적인 '구명보트'로 조명받았다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Cloudflare Workers 엣지 네이티브 × 다중 DB/스토리지 추상화
            </h3>
            <p>
              <code>Mailflare</code>(AGPL-3.0)가 기존 무거운 Linux 메일 서버 스택(Postfix + Dovecot + Roundcube + Nextcloud)과 결정적으로 다른 지점은 <strong>서버리스 엣지 아키텍처와 AI 에이전트 퍼스트 설계</strong>다:
            </p>
            <ul>
              <li><strong>Cloudflare 엣지 0원 풀스택 또는 단일 Docker 컨테이너:</strong> 기본 구성을 Cloudflare Workers + D1(SQLite 엣지 DB) + R2(오브젝트 스토리지) + Cloudflare Email Routing 위에 올리면 별도 VPS 임대료 없이 무료 쿼터 안에서 커스텀 도메인 메일과 드라이브를 굴릴 수 있다. 자체 서버를 선호한다면 <code>DATABASE_URL</code>만 바꿔 PostgreSQL·MySQL·Turso·로컬 SQLite에 연결하고 S3/Backblaze B2와 Docker 컨테이너 하나로 띄울 수 있다.</li>
              <li><strong>실전 송수신 파이프라인 &amp; 자동 라우팅 엔진:</strong> 수신 메일은 Cloudflare Email Worker가 즉시 파싱해 스팸·뉴스레터·프로모션 단일 규칙 필터와 포워딩 규칙을 실행하며, 발신은 Cloudflare Email·Resend·Amazon SES 중 원하는 트랜잭션 백엔드로 라우팅해 높은 전달률(Deliverability)을 확보한다.</li>
              <li><strong>무제약 내장 AI 에이전트 &amp; 개방형 MCP 서버:</strong> 구글처럼 파트너 심사를 강제하지 않고, 메일 검색·초안 작성·실제 발송·캘린더 일정 조율·드라이브 파일 조회까지 소유자 제어 권한 아래 MCP 프로토콜로 Claude Code, Cursor, 개인 에이전트에 직접 노출한다. 한국어를 포함한 <strong>34개 언어 및 RTL(아랍어 등)</strong> UI를 기본 내장한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Mailflare 서버리스/셀프호스트 워크스페이스 &amp; MCP 에이전트 구조</span>
                <span class="schematic-badge">TypeScript · Cloudflare Workers / Docker · AGPL-3.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Ingestion &amp; Migration</div>
                  <div class="schematic-desc">
                    Cloudflare Email / Resend / Amazon SES<br>
                    뉴스레터·프로모션 1-클릭 라우팅 규칙<br>
                    Google Takeout 일괄 임포트<br>
                    (<code>.mbox</code>, <code>.eml</code>, Calendar, Contacts, Drive)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Edge Core &amp; Storage</div>
                  <div class="schematic-desc">
                    Cloudflare Workers 또는 단일 Docker<br>
                    DB: D1 / PostgreSQL / MySQL / SQLite<br>
                    파일: R2 / S3 / Backblaze B2<br>
                    감사 로그 · API 키 · 웹훅 · 34개 언어
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Workspace &amp; Open MCP</div>
                  <div class="schematic-desc">
                    커스텀 도메인 메일 · 캘린더 · 예약(Booking)<br>
                    팀 공유 메일함 &amp; 파일 드라이브<br>
                    구글식 파트너 잠금 없는 <strong>풀권한 MCP</strong><br>
                    외부 AI 에이전트의 검색·초안·발송·일정 제어
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">mailflare.co 실화면 — 커스텀 도메인 메일·캘린더·드라이브·AI 에이전트 통합 콘솔</span>
              </div>
              <img src="../assets/images/demo_mailflare.png" alt="Mailflare Official Website and Workspace Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ mailflare.co 실화면: Cloudflare 원클릭 배포와 Docker 셀프호스팅을 동시에 지원하며 이메일·캘린더·부킹·드라이브·AI 에이전트를 통합한 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 붕괴: "1인당 월 14달러 SaaS 시대가 오픈소스 MCP로 무너진다"
            </h3>
            <p>
              구글 워크스페이스와 마이크로소프트 365가 수조 원대 B2B 구독 매출을 방어해 온 해자는 '메일 전달 평판'과 '통합 툴킷의 편리함'이었다. 그러나 2026년 들어 발신 인프라는 Resend나 Amazon SES가 저렴한 API 상품으로 해체했고, 수신·저장은 Cloudflare의 무료 엣지 티어가 먹어 치웠다. 여기에 빅테크 스스로가 자사 API에 AI 에이전트 통제 울타리를 치기 시작하면서, 개발자 팀과 스타트업에게 셀프호스팅은 '비용 절감'을 넘어 <strong>AI 자동화 생존권</strong>의 문제가 되었다.
            </p>
            <ul>
              <li><strong>구글 API 종속 리스크 헤지:</strong> 어제까지만 해도 개인 Gmail OAuth 토큰으로 잘 돌아가던 에이전트 워크플로우가 플랫폼 약관 개정 한 줄로 2027년 2월 1일부로 불법(ToS 위반) 처리된다. <code>Mailflare</code>(AGPL-3.0) 같은 오픈코어 대안은 무료 셀프호스팅을 보장하면서 동시에 월 4달러대 매니지드 클라우드(<code>Mailflare Cloud</code>)로 상용 전달성까지 선택하게 해 오픈소스 SaaS의 표준 공식을 밟고 있다.</li>
              <li><strong>실전 운용 시 체크할 점:</strong> 자체 도메인 발신 시 SPF/DKIM/DMARC 레코드 관리와 발신 평판(SES 샌드박스 해제 등)은 여전히 운영자가 챙겨야 하며, Cloudflare Workers 무료 티어의 일일 요청 한도를 넘는 대규모 팀이라면 Docker + PostgreSQL + S3 구성으로 전환하는 편이 안정적이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 에이전트가 메일을 보내지 못하게 막은 날, 사람들은 우체국을 직접 지었다
            </h3>
            <p>
              빅테크가 AI 에이전트 시대의 관문을 독점하려 할수록, 오픈소스는 관문 자체를 우회하는 새 도로를 깐다. 구글이 공식 Gmail MCP에서 '보내기' 버튼을 빼버린 바로 그 주간에 <code>Mailflare</code>가 GitHub 트렌딩을 달군 것은 우연이 아니다.
            </p>
            <p>
              2027년 2월 1일이 오기 전, 당신의 AI 에이전트는 여전히 거대 기업의 허락을 기다리며 초안 폴더만 서성거릴 것인가, 아니면 당신의 도메인 위에서 자유롭게 일할 것인가?
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=mailflare+self+hosted+google+workspace+cloudflare" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://mailflare.co" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 공식 웹 사이트 방문
              </a>
              <a href="https://github.com/hieunc229/mailflare" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
