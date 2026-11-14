# -*- coding: utf-8 -*-
# Story 1: alibaba/open-code-review (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] alibaba/open-code-review : COVER STORY            -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_opencodereview.jpg" alt="OpenCodeReview Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 토큰 1/9 절감 · 정밀도 역전</span>
              <span class="platform-tag">GitHub Trending #1 & open-codereview.ai</span>
              <span class="platform-tag">alibaba / open-code-review</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">알리바바 2년 실전 검증 'OpenCodeReview' 전격 오픈소스화: "범용 코딩 에이전트보다 토큰은 9분의 1, 코드 리뷰 정밀도는 압도적"</span>
            </h2>

            <div class="article-subheadline">
              결정론적 정적 규칙 파이프라인과 도구 호출형 LLM 에이전트의 하이브리드 결합으로 수만 명 개발자 환경에서 수백만 건의 결함을 적발해온 엔터프라이즈 코드 리뷰 CLI 대공개
            </div>
            <p class="article-snippet">
              AI 코딩 에이전트가 하루에 수천 줄의 Pull Request를 쏟아내는 시대, 병목은 '코드 작성'이 아니라 '코드 리뷰'로 옮겨갔습니다. 범용 에이전트에게 PR 리뷰를 맡기면 수십만 토큰을 태우며 사소한 스타일 지적(거짓 양성)만 남발하기 일쑤입니다. 오늘 알리바바 그룹이 사내에서 2년간 수만 명의 엔지니어와 함께 갈고닦아 공개한 'OpenCodeReview'는 50개 오픈소스·200개 실제 PR 벤치마크(AACR-Bench)에서 동일 모델 기준 범용 에이전트보다 정밀도와 F1 점수를 끌어올리면서도 토큰 소모량은 1/9 수준으로 줄여내며 GitHub 트렌딩 1위를 휩쓸었습니다.
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
              <i data-lucide="flame"></i> 1. 리드: AI가 짠 1,000줄 PR 앞에서 마비된 리뷰어들의 피로감
            </h3>
            <p>
              2026년 엔지니어링 조직의 최대 골칫거리는 역설적이게도 '너무 빠른 코드 생산 속도'다. Claude Code와 Codex가 3분 만에 40개 파일에 걸친 거대한 PR을 올려대기 시작하면서, 시니어 엔지니어들의 리뷰 대기열은 끝없이 불어났다. 그렇다고 또 다른 범용 코딩 에이전트를 리뷰어로 세우자니, 맥락을 파악한다며 저장소 전체를 읽어들여 API 청구서는 천정부지로 치솟고 정작 치명적인 스레드 안전성 결함이나 SQL 인젝션 대신 변수명 취향만 늘어놓는 '알람 피로(Alert Fatigue)'가 조직을 덮쳤다.
            </p>
            <p>
              바로 이 지점에서 알리바바 그룹이 사내 공식 AI 코드 리뷰 어시스턴트로 2년 넘게 수만 명의 개발자를 지원하며 수백만 건의 실제 결함을 걸러낸 핵심 무기를 커뮤니티에 풀었다: <strong>alibaba/open-code-review</strong>(51,384 스타).
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 범용 에이전트의 9분의 1 비용으로 정밀도(Precision)를 역전시킨 비결
            </h3>
            <p>
              OpenCodeReview가 단숨에 GitHub Daily General 및 Go 트렌딩 정상에 오른 이유는 단순히 "프롬프트를 잘 짰다"는 수준이 아니다. 수백만 건의 프로덕션 리뷰 로그에서 얻은 잔인할 정도로 실용적인 통찰, 즉 <strong>"재현율(Recall)을 무리하게 쫓다가 가짜 경보로 개발자의 신뢰를 잃는 순간, 어떤 AI 리뷰 도구도 팀에서 버려진다"</strong>는 원칙을 아키텍처에 박아넣었기 때문이다.
            </p>

            <div class="editorial-quote">
              <p>
                "동일한 기반 모델을 사용했을 때, OpenCodeReview는 범용 에이전트(Claude Code) 대비 <strong>토큰의 약 9분의 1(~1/9)만 소모하고 리뷰 완료 속도도 더 빠르면서도, 훨씬 높은 정밀도(Precision)와 F1 점수를 달성했다.</strong> 노이즈 대신 실제 결함에만 집중하는 의도적 트레이드오프의 승리다."
              </p>
              <small>— Alibaba OpenCodeReview 벤치마크 리포트 (AACR-Bench 50개 저장소 · 200 PR · 10개 언어 검증)</small>
            </div>

            <p>
              실제로 알리바바 팀은 주장의 객관성을 입증하기 위해 80명 이상의 시니어 엔지니어가 교차 검증한 1,505개 실제 결함 데이터셋(<strong>AACR-Bench</strong>)까지 Hugging Face(`Alibaba-Aone/aacr-bench`)에 동시 공개하며, 상용 SaaS 리뷰 툴들이 감추던 정량적 평가 지표를 투명하게 열어젖혔다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 결정론적 파이프라인과 도구 호출형 LLM 에이전트의 하이브리드 결합
            </h3>
            <p>
              OpenCodeReview가 적은 토큰으로 줄 단위(Line-level) 정밀 리뷰를 뽑아내는 구조는 크게 세 겹의 정교한 파이프라인으로 작동한다:
            </p>
            <ul>
              <li><strong>1단계 결정론적 규칙 필터 (Deterministic Ruleset):</strong> Go 언어로 구현된 초고속 사전 파이프라인이 Git Diff와 변경 파일을 파싱하며 NPE(Null Pointer Exception), 스레드 안전성, XSS, SQL 인젝션 등 언어별 내장 보안·품질 규칙을 비용 0원으로 먼저 걸러낸다.</li>
              <li><strong>2단계 도구 호출형 컨텍스트 탐색 (Agentic Tool-Use):</strong> LLM 에이전트가 단순히 diff 조각만 보고 추측하는 대신, 필요할 때만 전체 파일 읽기, 코드베이스 심볼 검색, 연관 변경 파일 교차 확인 도구를 능동적으로 호출해 호출부(Caller)와 피호출부(Callee)의 계약 위반을 추적한다.</li>
              <li><strong>3단계 전체 스캔 및 다중 모델 호환 (`ocr scan`):</strong> diff가 없는 신규 저장소나 레거시 모듈 감사 시에는 `ocr scan` 모드로 전환되며, OpenAI와 Anthropic API는 물론 Claude Code·Codex·Cursor·Kimi Code와 매끄럽게 결합한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">OpenCodeReview 하이브리드 2-Stage 정밀 리뷰 파이프라인</span>
                <span class="schematic-badge">Deterministic + Agentic Hybrid</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Deterministic Pre-Pipeline</div>
                  <div class="schematic-desc">
                    Git Diff &amp; AST 고속 파싱<br>
                    다국어 내장 규칙셋(NPE, XSS, SQLi)<br>
                    무관 파일·포맷팅 노이즈 즉시 차단<br>
                    ※ LLM 호출 전 1차 후보 압축
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Tool-Use Review Agent</div>
                  <div class="schematic-desc">
                    변경 파일 + 연관 컨텍스트 선택 조회<br>
                    코드베이스 심볼 역추적(Cross-file)<br>
                    거짓 양성(False Positive) 자가 검증<br>
                    범용 에이전트 대비 토큰 1/9 절감
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Line-Level Action Output</div>
                  <div class="schematic-desc">
                    정밀 줄 단위(Line-level) 코멘트 생성<br>
                    CI/CD PR 자동 코멘트 및 `ocr scan`<br>
                    OpenAI · Anthropic · 사내 LLM 호환<br>
                    OpenSSF Gold 인증 엔터프라이즈 보안
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">OpenCodeReview 공식 포털(open-codereview.ai) 및 CLI 아키텍처 뷰</span>
              </div>
              <img src="../assets/images/demo_opencodereview.png" alt="OpenCodeReview Official Web Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ open-codereview.ai 실구동 화면: 결정론적 파이프라인과 LLM 에이전트 결합 구조, 다중 코딩 에이전트 연동, 그리고 AACR-Bench 실증 지표를 한눈에 제공하는 공식 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 산업 지각변동: 월 수만 원대 AI PR SaaS의 종언
            </h3>
            <p>
              그동안 개발팀들은 GitHub PR마다 코멘트를 달아주는 상용 AI 코드 리뷰 SaaS에 시트당 월 15~30달러를 지불하면서도, 정작 사내 민감 소스코드를 외부 클라우드 리뷰 서버로 보내야 하는 보안 부담과 불투명한 벤치마크를 감수해야 했다.
            </p>
            <ul>
              <li><strong>OpenSSF Gold 인증 &amp; 자체 엔드포인트 주권:</strong> OpenCodeReview는 OpenSSF Best Practices Gold 배지를 획득한 오픈소스 CLI로, 소스코드가 제3자 SaaS 중개 서버를 거치지 않고 조직이 지정한 LLM 엔드포인트(로컬 vLLM/사내 게이트웨이 포함)로만 직접 통신한다.</li>
              <li><strong>벤치마크 기반의 오픈 경쟁 시대:</strong> `Alibaba-Aone/aacr-bench` 데이터셋이 공개되면서 이제 모든 AI 리뷰 도구는 "감성적인 데모 영상"이 아니라 10개 언어 1,505개 실제 버그 앞에서의 F1·정밀도·토큰 효율로 정면 승부를 겨루게 됐다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 코드를 짜는 AI보다 '거절할 줄 아는 AI'가 비싸다
            </h3>
            <p>
              코드 생성 비용이 0에 수렴하는 시대, 소프트웨어 공학의 진짜 가치는 "무엇을 더 만들 것인가"가 아니라 "무엇을 프로덕션에 들이지 않을 것인가"라는 게이트키핑 능력으로 이동하고 있다.
            </p>
            <p>
              수만 명의 알리바바 엔지니어들이 2년간 다듬은 '침묵할 때와 경고할 때를 아는' 리뷰 엔진이 오픈소스로 풀린 오늘, 이제 모든 개발자는 자기 터미널 안에서 빅테크급 시니어 보안·아키텍처 리뷰어를 무료로 고용할 수 있게 됐다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Alibaba+OpenCodeReview+AI+code+review" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://open-codereview.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹 포털 방문
              </a>
              <a href="https://github.com/alibaba/open-code-review" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
