# -*- coding: utf-8 -*-
# Story 5: ethanplusai/sellbird

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] ethanplusai/sellbird                             -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_sellbird.jpg" alt="Sellbird Open-Source Outreach Platform Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="send" style="width:12px;height:12px;fill:#fff;"></i> ZERO API BILL</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#14532d;">🕊️ API 과금 제로·내 Claude/ChatGPT 구독으로 도는 세일즈 엔진</span>
              <span class="platform-tag">GitHub Trending &amp; sellbird.ai</span>
              <span class="platform-tag">ethanplusai / sellbird</span>
            </div>

            <h2 class="article-headline">
              월 수십만 원짜리 B2B 영업 SaaS를 내 로컬 머신 하나로 대체한다: 오픈소스 아웃리치 엔진 'Sellbird'
            </h2>

            <div class="article-subheadline">
              OpenStreetMap 무료 기업 발굴·무과금 웹사이트 구매 신호 스크래핑·이메일 검증·개인화 콜드메일 작성 및 승인제 Outbox를 기존 Claude/ChatGPT 구독만으로 구동 (+358스타/일, AGPL-3.0)
            </div>
            <p class="article-snippet">
              초기 스타트업이나 1인 개발자가 B2B 영업을 시작하려면 Apollo, Clay, ZoomInfo, 시퀀서 SaaS, 거기에 대량 LLM API 토큰 비용까지 매달 수백 달러를 태워야 했습니다. 최근 <code>Harvey</code>에서 새 이름으로 리브랜딩하며 오늘 하루 358스타(누적 6,486스타)를 모은 <strong>ethanplusai/sellbird</strong>는 이미 결제 중인 Claude Pro/Max 또는 ChatGPT Codex CLI 구독과 로컬 Python 데몬만으로 잠재 고객 발굴부터 답장 초안 작성까지 전 과정을 수행합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 15분마다 잠에서 깨어 영업을 대신 뛰는 터미널 속 작은 새
            </h3>
            <p>
              터미널 창에 <code>sellbird run</code>을 입력하자 파이프라인 상태 점검 로그가 흘러간다. 지난밤 사이 OpenStreetMap에서 찾아낸 지역 치과와 지붕 수리 업체 목록 중, 자체 웹사이트에 온라인 예약 폼이 없거나 채용 공고를 올린 곳만 추려졌다. 이어서 담당자 이름과 유효한 이메일 주소가 검증되고, 각 회사의 맥락에 맞춘 2단계 콜드메일 시퀀스가 작성된 뒤 마지막 줄에 멈춘다: <code>outbox → 5 emails waiting for your approval</code>.
            </p>
            <p>
              수천 달러짜리 엔터프라이즈 GTM(Go-To-Market) SaaS 스택을 단 하나의 로컬 저장소로 압축하며 오늘 GitHub 트렌딩에 오른 <strong>ethanplusai/sellbird</strong>(구 Harvey, v0.4.0)는 "무분별한 AI 스팸 봇"이 아니라 "인간의 승인(Human-in-the-loop)과 정액제 구독 경제를 결합한 개인용 영업 비서"로 폭발적 호응을 얻고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '토큰 종량제'와 'B2B 데이터 SaaS 월세'를 동시에 우회한 영리한 설계
            </h3>
            <p>
              Sellbird가 스타트업 창업자와 인디 해커들의 마음을 사로잡은 비결은 철저한 비용 파괴와 안티-스팸 안전장치의 결합이다. API 키를 발급받아 종량제 과금 폭탄을 맞는 대신, 개발자가 이미 쓰고 있는 <code>claude login</code>(Claude Code CLI)이나 ChatGPT Codex CLI를 두뇌로 연결하고, 자체 속도 제한(Throttling)을 걸어 사용자의 본업 작업량을 침범하지 않도록 설계했다.
            </p>

            <div class="editorial-quote">
              <p>
                "API 키도, 토큰당 종량제 과금도, Apollo·ZoomInfo·Clearbit·Clay 같은 비싼 발굴 툴도 필요 없다. <strong>사용자가 승인하기 전까지는 단 한 통의 이메일도 밖으로 나가지 않으며</strong>, 결정론적 사전 검사기가 모든 초안을 검증한다."
              </p>
              <small>— ethanplusai/sellbird 공식 문서 및 아키텍처 원칙 (AGPL-3.0)</small>
            </div>

            <p>
              심지어 기업 웹사이트를 읽어 '구매 신호(Buying Signals)'—예컨대 온라인 예약 미지원, 광고 집행 여부, 특정 직무 채용 중 등—를 판별하는 단계는 <strong>LLM 호출 없이 단 3회의 HTTP 요청($0)</strong>만으로 처리해 속도와 비용 효율을 극한으로 끌어올렸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 6단계 로컬 파이프라인과 무모델(Zero-Model) 발송 가드
            </h3>
            <p>
              Python 3.11+과 로컬 대시보드(<code>http://127.0.0.1:5555</code>)로 구동되는 Sellbird는 <code>sellbird train &lt;url&gt;</code>로 내 제품을 학습한 뒤, 다음 6단계 자율 루프를 15분 주기로 실행한다:
            </p>
            <ul>
              <li><strong>무비용 발굴 및 시그널 스크래핑 (Discover &amp; Signals):</strong> 기본 소스로 OpenStreetMap을 무료 조회하고(유료 소스 선택 시 실행 전 예상 비용 사전 고지), 각 대상 기업 웹사이트를 3회 HTTP 요청으로 크롤링해 확정된 구매 신호를 추출한다.</li>
              <li><strong>의사결정자 식별 &amp; 4단계 주소 신뢰도 분류 (Enrich &amp; Verify):</strong> 기업 당 최대 2명의 소유주·매니저만 추린 뒤, 도메인 이메일 패턴을 학습해 모든 주소를 <code>verified</code>, <code>risky</code>, <code>guess</code>, <code>invalid</code>로 태깅한다. 실제 발송은 오직 <code>verified</code> 등급에만 허용된다.</li>
              <li><strong>결정론적 사전 발송 검사 &amp; <code>Outbox</code> 승인 게이트:</strong> 작성된 메일은 Google Workspace, Microsoft 365, SMTP를 통해 상대방 업무 시간과 일일 발송 한도 내에서 나간다. 발송 직전에는 LLM이 아닌 규칙 기반 검사기가 미치환 태그(<code>{{name}}</code>), 금지 문구, 과도한 길이, 외부 도메인 링크, 시스템 프롬프트 유출 문구를 걸러내고 <code>sellbird sending pause</code> 한 번으로 즉시 전체 중단할 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Sellbird 제로-API-빌(Zero-API-Bill) 로컬 자율 아웃리치 파이프라인</span>
                <span class="schematic-badge">AGPL-3.0 · Python 3.11+ · Local SQLite</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Zero-Cost Discovery</div>
                  <div class="schematic-desc">
                    OpenStreetMap 무료 타겟 발굴 ($0)<br>
                    웹사이트 3회 HTTP 요청 (LLM 호출 0)<br>
                    <code>sellbird signals</code> 구매 신호 판별<br>
                    <code>sellbird export</code> 시퀀서용 CSV 추출
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Subscription Brain &amp; Verify</div>
                  <div class="schematic-desc">
                    Claude Code CLI / Codex CLI 구독 연동<br>
                    기업당 최대 2명 의사결정자 매칭<br>
                    이메일 4등급 검증 (<code>verified</code>만 발송)<br>
                    개인화 시퀀스 작성 및 답장 초안 생성
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Deterministic Guard &amp; Outbox</div>
                  <div class="schematic-desc">
                    로컬 대시보드 <code>Outbox</code> 수동 승인 기본<br>
                    무모델 사전 검사기(태그·금지어·유출 차단)<br>
                    수신거부(Opt-out)·부재중 자동 분류<br>
                    상대 오피스 아워·일일 한도 준수 발송
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Sellbird 공식 포털 및 로컬 아웃박스 대시보드 (sellbird.ai)</span>
              </div>
              <img src="../assets/images/demo_sellbird.png" alt="Sellbird Official Portal Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ sellbird.ai 공식 포털 실화면: API 종량제 요금 없이 기존 Claude/ChatGPT 정액제 구독만으로 동작하는 로컬 우선 아웃리치 워크플로우와 승인형 Outbox 철학을 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. SaaS 해자 침식과 윤리적 경계: '클린 아웃바운드' vs '스팸 공해'
            </h3>
            <p>
              Sellbird가 채택한 AGPL-3.0 라이선스와 <code>sellbird.ai</code> 호스팅 서비스 병행 모델은 오픈코어(Open-Core) 전략의 교과서를 보여주지만, 동시에 콜드메일 자동화 생태계에 두 가지 쟁점을 던진다.
            </p>
            <ul>
              <li><strong>B2B 데이터·GTM SaaS의 가격 파괴:</strong> <code>Clay</code>나 <code>Apollo</code>에 매월 수백 달러를 내던 소규모 에이전시와 SaaS 창업자들이 공개 지도 데이터(OSM)와 로컬 웹 스크래핑, 정액제 코딩 에이전트 구독 조합으로 갈아타면서 기존 GTM 툴들의 가격 결정력이 시험대에 올랐다.</li>
              <li><strong>구독 약관과 발송 평판(Deliverability) 문제:</strong> Claude Code나 Codex CLI 같은 정액제 코딩 에이전트를 영업 파이프라인 백엔드로 돌리는 방식은 개인 생산성 도구와 자동화 백엔드 사이의 구독 약관 경계선에 걸쳐 있으며, 도메인 평판 보호를 위해 별도 발송 도메인과 웜업(Warmup)이 필수적이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 영업팀 없는 1인 기업이 얻은 '자기 승인을 기다리는 디지털 세일즈 데스크'
            </h3>
            <p>
              AI 에이전트가 코드를 짜주는 시대에는 제품 하나를 만드는 시간보다 그 제품을 써줄 첫 10명의 고객을 찾는 시간이 훨씬 더 길고 고통스럽다.
            </p>
            <p>
              오토파일럿 스팸을 뿌리는 대신 아침마다 승인 대기함(Outbox)에 정갈하게 정리된 다섯 통의 진심 어린 제안서를 올려놓는 Sellbird는, 자본이 없는 1인 제작자에게 가장 정직하고 강력한 영업 무기를 쥐여주었다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Sellbird+open+source+outreach+Claude+Code" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://sellbird.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 홈페이지 (sellbird.ai)
              </a>
              <a href="https://github.com/ethanplusai/sellbird" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
