# -*- coding: utf-8 -*-
# Story 2: microsoft/markitdown

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] microsoft/markitdown                             -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_markitdown.jpg" alt="Microsoft MarkItDown LLM Document Prism Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="file-text" style="width:12px;height:12px;fill:#fff;"></i> LLM DATA PIPELINE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e40af;">📄 오늘의 미발행 트렌딩 1위 (+466★/일) · 모든 오피스 문서를 LLM 모국어로</span>
              <span class="platform-tag">GitHub Trending #1 (Unseen) &amp; MCP</span>
              <span class="platform-tag">microsoft / markitdown</span>
            </div>

            <h2 class="article-headline">
              "LLM의 진짜 모국어는 PDF가 아니라 마크다운이다" — 전 세계 에이전트 파이프라인의 표준 전처리기로 자리잡은 마이크로소프트 'MarkItDown'
            </h2>

            <div class="article-subheadline">
              PDF·PowerPoint·Word·Excel·이미지(EXIF/LLM Vision)·오디오 전사·HTML·ZIP·YouTube URL·EPub을 구조 보존 Markdown으로 변환하며 markitdown-mcp 서버 및 markitdown-ocr 플러그인으로 확장 (+466스타/일, 누적 197,865스타, MIT)
            </div>
            <p class="article-snippet">
              AI 에이전트가 기업의 지식 베이스를 읽을 때 가장 먼저 마주하는 장벽은 모델의 추론력이 아니라 PDF, PPTX, XLSX, 압축 파일 속에 뒤엉킨 비정형 바이너리 포맷입니다. 오늘 하루에만 <strong>466개의 스타(누적 197,865스타)</strong>를 추가하며 GitHub Python 트렌딩 최상단을 지킨 마이크로소프트의 <strong>MarkItDown</strong>은 수십 종의 사내 문서와 멀티미디어 데이터를 토큰 효율이 극대화된 순수 Markdown으로 압축 변환하고, 단일 도구 MCP 서버(<code>markitdown-mcp</code>)와 비전 OCR 플러그인(<code>markitdown-ocr</code>)을 통해 모든 에이전트의 기본 입출력 계층을 장악하고 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 20만 스타 고지 앞에서 다시 타오르는 '전처리의 역습'
            </h3>
            <p>
              화려한 멀티에이전트 프레임워크와 새 모델 벤치마크가 매주 쏟아지는 와중에도, 오늘 GitHub Python 트렌딩에서 466개의 신규 스타를 휩쓸며 누적 <strong>197,865스타</strong>에 도달한 프로젝트는 다름 아닌 문서 변환 유틸리티 <strong>microsoft/markitdown</strong>이다. 출시 2년이 지난 지금까지도 하루 수백 명씩 엔지니어들이 별표를 누르는 이유는 단순하다. 프로덕션 AI 시스템을 굴려본 팀이라면 누구나 깨닫기 때문이다. <em>"거대언어모델 성능의 절반은 프롬프트가 아니라, 입력 문서를 얼마나 덜 망가뜨리고 적은 토큰으로 먹이느냐에 달려 있다."</em>
            </p>
            <p>
              과거의 텍스트 추출기(<code>textract</code> 등)는 PDF나 Word 문서에서 글자만 긁어내다 보니 표(Table)의 열 정렬, 제목 계층(H1~H3), 불릿 리스트, 하이퍼링크 같은 문서의 논리적 골격을 모두 뭉개버렸다. 반대로 HTML이나 원본 XML을 그대로 LLM 컨텍스트에 넣으면 스타일 태그와 보일러플레이트가 토큰 비용의 70% 이상을 태워버린다. MarkItDown은 바로 그 간극에서 <strong>'인간용 고충실도 렌더링' 대신 'LLM 소비용 구조화 마크다운'</strong>이라는 명확한 철학을 밀어붙여 사실상의 업계 표준으로 등극했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "프론티어 모델은 이미 마크다운으로 사고하고 말한다"
            </h3>
            <p>
              MarkItDown 팀이 내세운 핵심 통찰은 명쾌하다. 현대의 주류 LLM들은 방대한 기술 문서, GitHub README, 위키 데이터를 통해 학습되면서 사실상 <strong>Markdown을 모국어처럼 구사한다</strong>. 별도 지시가 없어도 모델이 스스로 <code>#</code> 헤더와 마크다운 표, 코드 펜스로 답을 구조화해 출력하는 이유가 여기에 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "마크다운은 순수 평문(Plain text)에 극도로 가까워 토큰 효율이 압도적으로 높으면서도, 제목·목록·표·링크라는 핵심 문서 구조를 온전히 보존한다. <strong>MarkItDown은 사람이 보기 좋은 복제본이 아니라, 텍스트 분석 엔진과 LLM이 가장 잘 이해하는 구조를 복원한다.</strong>"
              </p>
              <small>— microsoft/markitdown 공식 설계 철학 (MIT License)</small>
            </div>

            <p>
              여기에 <code>markitdown-mcp</code> 패키지가 STDIO·Streamable HTTP·SSE 기반의 단일 도구(<code>convert_to_markdown(uri)</code>)로 합류하고, LLM 비전 모델을 재사용해 PDF·PPTX·DOCX·XLSX 내부 이미지 텍스트까지 추출하는 <code>markitdown-ocr</code> 플러그인이 얹히면서, MarkItDown은 단순 Python 라이브러리를 넘어 에이전트 시대의 범용 파일 시스템 어댑터로 진화했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 12종 포맷 컨버터·LLM Vision OCR 플러그인·MCP 게이트웨이
            </h3>
            <p>
              MarkItDown은 Python 3.10~3.14 환경에서 모듈형 의존성(<code>pip install 'markitdown[pdf, docx, pptx]'</code> 등)으로 가볍게 조합할 수 있도록 설계됐다:
            </p>
            <ul>
              <li><strong>이종 포맷 통합 추상화 엔진:</strong> PDF, PowerPoint, Word, Excel(<code>xlsx</code>/<code>xls</code>), Outlook 메시지, HTML, CSV/JSON/XML, EPub은 물론, 이미지(EXIF 메타데이터 + 멀티모달 캡션), 오디오(EXIF + 음성 전사), ZIP 아카이브(내부 파일 재귀 순회), YouTube URL(자막/트랜스크립트 추출)까지 단일 파이프라인으로 정규화한다.</li>
              <li><strong><code>markitdown-ocr</code> &amp; 서드파티 플러그인 생태계:</strong> 기본은 안전을 위해 플러그인이 비활성화돼 있으나, <code>--use-plugins</code> 또는 <code>enable_plugins=True</code>를 켜면 별도 무거운 바이너리 OCR 엔진 없이 기존에 연결된 OpenAI 호환 <code>llm_client</code>/<code>llm_model</code>을 그대로 활용해 스캔 PDF와 슬라이드 내 도표 이미지를 텍스트로 복원한다.</li>
              <li><strong>로컬 신뢰 경계와 <code>convert_stream()</code> 보안 원칙:</strong> 파일 시스템 및 네트워크 I/O를 현재 프로세스 권한으로 수행하므로, 비신뢰 입력 환경에서는 최소 권한 원칙에 따라 <code>convert_stream()</code> 또는 <code>convert_local()</code>을 분리 호출하도록 권고하며, <code>markitdown-mcp</code> 역시 HTTP/SSE 구동 시 기본적으로 <code>127.0.0.1</code> 로컬 바인딩만 허용한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">MarkItDown 멀티포맷 정규화 → OCR 플러그인 → MCP 에이전트 투입 아키텍처</span>
                <span class="schematic-badge">Python 3.10–3.14 · MIT · 197.8k★ · STDIO/Streamable HTTP MCP</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Heterogeneous Ingestion</div>
                  <div class="schematic-desc">
                    Office (PDF·DOCX·PPTX·XLSX·Outlook)<br>
                    Media (Image EXIF·Audio·YouTube URL)<br>
                    Archive (ZIP 재귀 순회·EPub·HTML)<br>
                    <code>convert_stream()</code> 최소 권한 I/O 격리
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Structure &amp; Vision Plugins</div>
                  <div class="schematic-desc">
                    제목 계층·표(Table)·리스트·링크 복원<br>
                    <code>markitdown-ocr</code>로 임베디드 이미지 OCR<br>
                    <code>#markitdown-plugin</code> 서드파티 확장<br>
                    토큰 낭비 HTML/XML 보일러플레이트 제거
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Agent &amp; RAG Delivery</div>
                  <div class="schematic-desc">
                    <code>markitdown-mcp</code> (<code>convert_to_markdown</code>)<br>
                    <code>http:</code> / <code>https:</code> / <code>file:</code> / <code>data:</code> URI 통합<br>
                    STDIO · Streamable HTTP · SSE 전송<br>
                    LLM 네이티브 Markdown 컨텍스트 즉시 공급
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">microsoft/markitdown 저장소 실화면 — 4대 코어 패키지와 MCP·OCR 플러그인 아키텍처</span>
              </div>
              <img src="../assets/images/demo_markitdown.png" alt="Microsoft MarkItDown GitHub Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/microsoft/markitdown 실화면: AutoGen 팀이 설계한 markitdown 코어, markitdown-mcp 서버, markitdown-ocr 비전 플러그인, 샘플 플러그인 패키지 구조와 보안 권고 및 선택적 포맷 의존성 명세.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 상용 PDF 파싱 SaaS를 위협하는 오픈소스 미들웨어
            </h3>
            <p>
              지난 3년간 AI 데이터 엔지니어링 시장에서는 "복잡한 기업 PDF와 엑셀을 RAG용 텍스트로 바꿔준다"며 API 호출당 과금하거나 엔터프라이즈 라이선스를 판매하는 수많은 상용 파싱 스타트업이 등장했다. 그러나 19만 8천 명의 개발자가 선택한 <code>MarkItDown</code>(MIT)은 파일 변환 계층이 독점 SaaS가 아니라 누구나 로컬에서 <code>pip install</code>로 꽂아 쓰는 무료 공용 인프라로 수렴하고 있음을 보여준다.
            </p>
            <ul>
              <li><strong>데이터 유출 없는 폐쇄망 파싱:</strong> 금융·법률·의료 기업들은 사내 Word·Excel 계약서를 외부 클라우드 파싱 API로 보내는 것 자체를 규정 위반으로 간주한다. MarkItDown은 로컬 프로세스 내에서 모든 오피스 문서를 처리하고 필요시에만 사내 LLM 엔드포인트에 이미지 캡션/OCR을 위임할 수 있어 컴플라이언스 장벽을 완전히 없앤다.</li>
              <li><strong>SSRF 및 악성 문서 방어 책임:</strong> 반면 <code>markitdown-mcp</code>가 <code>http:</code>/<code>file:</code>/<code>data:</code> URI를 폭넓게 수용하는 만큼, 사내 에이전트에 무방비로 연결할 경우 내부망 파일 열람이나 SSRF(서버 측 요청 위조) 경로가 될 수 있어 신뢰된 로컬 에이전트 환경에 격리 배포해야 하는 과제도 분명하다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 화려한 에이전트도 결국 '깔끔한 마크다운 한 줄' 위에서 춤춘다
            </h3>
            <p>
              모델 파라미터가 커지고 에이전트 루프가 정교해질수록, 역설적으로 현장에서 승부를 가르는 것은 수십 년 묵은 오피스 문서 포맷의 찌꺼기를 얼마나 깨끗하게 씻어내는가 하는 기초 토목 공사다.
            </p>
            <p>
              20만 스타의 문턱에 선 MarkItDown의 꾸준한 상승세는 AI 엔지니어링의 성숙을 상징한다. 미래의 거대 지능을 먹여 살리는 가장 강력한 연료는 여전히, 군더더기 없이 정제된 순수 마크다운 텍스트다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Microsoft+MarkItDown+Python+MCP+tutorial" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/microsoft/markitdown" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
