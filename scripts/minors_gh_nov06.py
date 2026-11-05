# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-11-06

GH_MINORS = """
      <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
      <!-- [GH 0~10h] Item 1: southleft/figma-console-mcp -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 242개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;디자인 시스템을 API로 만들어 AI에 직결하다&quot; : figma-console-mcp</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">southleft/figma-console-mcp — AI 코딩 에이전트가 피그마 캔버스를 직접 읽어 디자인 토큰, 컴포넌트 스펙, 레이아웃을 코드로 추출·생성하는 MCP 서버</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">피그마 화면을 복사-붙여넣기 없이 코드로 직수출하는 에이전트 브릿지</h3>
          <div class="minor-detail-subheadline">디자이너와 프론트엔드 개발자 간의 핸드오프 단계를 0초로 단축하는 MCP 프로토콜</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 코딩 도구가 발전했음에도 피그마 디자인의 폰트, 여백, 컬러 변수를 일일이 CSS로 옮겨 적는 수작업은 여전히 비효율적이었습니다. 피그마 REST API와 플러그인 콘솔을 단일 MCP 인터페이스로 감싸 AI가 직접 도면을 탐색하게 만들었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Figma Document Tree &rarr; MCP Server (JSON-RPC) &rarr; Claude Code / Cursor Agent &rarr; Tailored Tailwind / React Components
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                디자인 토큰 변경 사항을 실시간 감지하여 코드베이스의 글로벌 스타일시트와 자동으로 동기화하는 지속적 통합(CI) 워크플로우를 구현합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/southleft/figma-console-mcp" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: tester-army/e2e -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 237개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;웹과 모바일 전 영역을 커버하는 차세대 AI 자율 E2E 테스터&quot; : e2e</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">tester-army/e2e — 사람이 시나리오 코드를 짜지 않아도 앱을 스스로 탐색하며 엣지 케이스와 레이아웃 깨짐을 잡아내는 지능형 테스트 프레임워크</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">깨지기 쉬운 XPath와 셀렉터 기반 테스트 스크립트의 영구 은퇴</h3>
          <div class="minor-detail-subheadline">시각적 지각(Visual Perception)과 자율 강화학습 탐색을 결합한 QA 혁신</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                UI 마크업이 조금만 바뀌어도 기존 Cypress나 Playwright 스크립트가 우르르 실패하던 'Flaky Test'의 악몽을 AI 비전 탐색으로 해결했습니다. 버튼 위치가 바뀌어도 맥락을 이해해 클릭을 지속합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[자율 테스팅]</strong> Web / Mobile App Launch &rarr; Screen OCR & Layout Semantic Tree &rarr; Autonomous Goal Planner &rarr; Visual Regression Report
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                테스트 코드 유지보수 공수를 90% 이상 절감하며, CI 환경에서 매 커밋마다 100여 개의 사용자 행동 경로를 자동으로 퍼징(Fuzzing) 검증합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/tester-army/e2e" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: Nebularotunnel/Token-Sniper -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 391개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 55.3 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;DEX 신규 페어 생성을 밀리초 단위로 추적하는 데스크톱 레이더&quot; : Token-Sniper</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Nebularotunnel/Token-Sniper — 솔라나 및 EVM 체인의 멤풀(Mempool) 이벤트를 직접 스니핑하여 유동성 풀 생성과 러그풀 위험을 판별하는 고속 분석기</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">온체인 트랜잭션 스트림을 실시간 감시하는 시스템 분석 하네스</h3>
          <div class="minor-detail-subheadline">악성 컨트랙트 바이트코드 디컴파일과 허니팟(Honeypot) 판별 엔진 탑재</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                탈중앙화 거래소(DEX)에서 쏟아지는 수만 개의 신규 토큰 중 악성 사기 컨트랙트를 피하고 정량적인 유동성 락업 여부를 즉각 분석하려는 퀀트 엔지니어들의 요구로 급부상했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[스나이핑 구조]</strong> Mempool Event Stream &rarr; Bytecode Static Security Scanner &rarr; Liquidity Lock Verifier &rarr; Real-time Desktop HUD Alert
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                gRPC 스트리밍을 통해 블록 확정 전 멤풀 단계에서 컨트랙트 소유권 포기 여부와 민팅 권한을 사전 검증하여 자금 손실 리스크를 0%로 통제합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Nebularotunnel/Token-Sniper" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
      <!-- [GH 10~20h] Item 4: Wallbycontact/java-mod-rust-port-tool -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 408개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.9 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;마인크래프트 자바 모드 JAR를 넣으면 Rust 코드가 나온다&quot; : Smelt</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Wallbycontact/java-mod-rust-port-tool — Fabric/NeoForge 자바 바이트코드를 파싱하여 Rust 네이티브 게임 엔진용 호환 코드로 자동 변환하는 트랜스파일러</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">자바 가비지 컬렉션의 렉을 지우는 모드 생태계의 러스트 마이그레이션</h3>
          <div class="minor-detail-subheadline">수천 개의 커뮤니티 에셋을 네이티브 C/Rust 환경으로 무손실 포팅</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                10년 넘게 축적된 방대한 자바 모드 생태계를 차세대 고성능 오픈소스 복셀 엔진(Rust 기반)으로 옮겨오기 위한 다리 역할을 수행하며 모딩 커뮤니티의 폭발적인 지지를 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[트랜스파일]</strong> Java Mod JAR (Bytecode) &rarr; AST Decompilation & Type Mapping &rarr; Safe Rust FFI Bindings &rarr; Horizon Engine Component
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                자바의 동적 리플렉션과 이벤트 버스 아키텍처를 러스트의 컴파일 타임 트레이트(Trait)와 ECS(Entity Component System) 시스템으로 1:1 매핑 변환합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Wallbycontact/java-mod-rust-port-tool" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: AtomIllusionistDwell/watson-username-footprint-finder -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 428개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.0시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;3,100개 웹사이트에서 디지털 풋프린트를 1초 만에 추적&quot; : Watson</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">AtomIllusionistDwell/watson-username-footprint-finder — 닉네임, 이메일, 전화번호로 전 세계 3,100여 개 플랫폼의 가입 여부와 프로필을 일목요연하게 리포팅하는 OSINT 도구</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">개인정보 유출 자가 점검과 화이트해커를 위한 초고속 OSINT 검색기</h3>
          <div class="minor-detail-subheadline">헤드리스 브라우저 없이 비동기 HTTP 파이프라인으로 전 세계 플랫폼을 1분 내 스캔</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                과거 셜록(Sherlock) 등 기존 도구의 느린 속도와 높은 오탐률(False Positive)을 극복하고, WAF 회피 헤더와 지능형 응답 검증을 탑재해 보안 담당자들 사이에서 필수 도구로 떠올랐습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[스캔 엔진]</strong> Single Identifier Query &rarr; 3,100+ Async Target Probes &rarr; Status Code & Content Fuzzy Matcher &rarr; Consolidated HTML/PDF Dossier
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                커스텀 비동기 HTTP 워커 풀을 통해 분당 5,000건 이상의 엔드포인트를 병렬 검증하며, 크리덴셜 스터핑 공격 방어를 위한 계정 노출 위험도를 종합 점수화합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/AtomIllusionistDwell/watson-username-footprint-finder" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: dragonwolfshovel/youtube-uploader -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 426개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.6 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;배치 처리와 썸네일 매핑을 자동화한 유튜브 업로드 파이프라인&quot; : youtube-uploader</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">dragonwolfshovel/youtube-uploader — 구글 공식 API 쿼터 제약을 회피하고 세션 쿠키 기반으로 영상 업로드, 메타데이터 작성, 스케줄링을 완결하는 CLI</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">AI 영상 생성 파이프라인의 마지막 단계인 '유튜브 발행' 완전 자동화</h3>
          <div class="minor-detail-subheadline">인증 토큰 만료 처리와 업로드 청크 재전송 메커니즘 내장</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 영상 자동화 툴들이 영상을 쏟아내지만 정작 유튜브에 올릴 때는 웹 스튜디오에서 일일이 마우스로 업로드해야 했던 마지막 병목을 완벽한 헤드리스 스크립트로 해결했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[발행 워크플로우]</strong> Rendered MP4 + Metadata JSON &rarr; Resumable Chunk Upload Protocol &rarr; Auto Thumbnail Attachment &rarr; Scheduled Live Publish
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                네트워크 단절 시에도 바이트 단위로 이어 올리기(Resumable Upload)를 지원하여 수 GB의 고화질 비디오 업로드 실패율을 0%로 줄였습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/dragonwolfshovel/youtube-uploader" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
      <!-- [GH 20~30h] Item 7: vercel-labs/agent-browser -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 181개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;버셀 랩스가 공개한 에이전트 전용 초경량 브라우저 CLI&quot; : agent-browser</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">vercel-labs/agent-browser — 무거운 CDP 프로토콜 대신 에이전트가 이해하기 쉬운 정제된 시맨틱 트리와 스냅샷만을 초고속 교환하는 Rust 브라우저 엔진</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">Playwright의 1/10 메모리로 웹을 탐색하는 AI 전용 경량 브라우저</h3>
          <div class="minor-detail-subheadline">토큰 소모를 극적으로 줄이는 시맨틱 텍스트 맵 추출 알고리즘 탑재</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 에이전트가 웹사이트를 방문할 때 불필요한 이미지와 자바스크립트 광고 트래픽을 차단하고, 오직 의사결정에 필요한 인터랙티브 요소들만 추려내어 속도와 비용을 동시에 잡았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[경량 브라우징]</strong> Target URL &rarr; Rust Headless Engine (No Ad/Tracking) &rarr; Compact Accessibility Graph &rarr; Agent Action Dispatch
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                페이지당 소비되는 LLM 프롬프트 토큰을 80% 이상 절감하며, 터미널 CLI 도구로 제공되어 어떤 쉘 스크립트에서도 손쉽게 파이프라인으로 연결됩니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/vercel-labs/agent-browser" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: Thysrael/Horizon -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 540개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 35.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;나만의 글로벌 AI 뉴스 레이더 및 자동 브리핑 생성기&quot; : Horizon</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Thysrael/Horizon — 수십 개의 RSS, 트위터/X, 아카이브(ArXiv) 소스를 수집해 매일 아침 맞춤형 다국어 브리핑을 팟캐스트/마크다운으로 발행하는 오픈소스</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">정보 과부하 시대를 살아가는 엔지니어를 위한 1인 AI 신문사</h3>
          <div class="minor-detail-subheadline">다양한 관점의 기사를 교차 검증하고 노이즈를 필터링하는 큐레이션 알고리즘</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                알고리즘 추천 피드의 자극적인 낚시성 뉴스에 지친 개발자들이 자신만의 정밀한 필터링 규칙과 LLM 에이전트를 결합해 순수 기술적 가치만을 브리핑받기 위해 활발히 도입하고 있습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[인텔리전스 루프]</strong> Multi-channel Ingestion &rarr; Deduplication & Fact-Cross Check &rarr; LLM Distillation &rarr; Markdown / Audio Podcast Auto-Export
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                SQLite 기반 로컬 임베딩 벡터를 통해 과거 읽은 기사와의 중복도를 측정하여 이미 알고 있는 내용의 반복 노출을 원천 차단합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Thysrael/Horizon" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: sandbox-quantum/switch -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 215개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;슬랙, 팀즈, 디스코드에 상주하는 오픈소스 AI 동료&quot; : Switch</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">sandbox-quantum/switch — 어떤 메신저 플랫폼이든 단일 웹훅으로 묶어 사내 데이터 접근 권한을 가진 자율 AI 팀원을 배치하는 자가 호스팅 하네스</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">팀원들의 업무 메신저 대화 속에서 자연스럽게 협업하는 자율 에이전트</h3>
          <div class="minor-detail-subheadline">사내 위키, 이슈 트래커, CI 빌드 상태를 실시간 스레드 대화로 해결</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기업마다 슬랙, MS 팀즈, 텔레그램 등 사용하는 메신저가 분절되어 있어 봇을 따로 구축해야 했던 문제를 단일 통합 게이트웨이와 롤베이스 권한 관리(RBAC)로 우아하게 통일했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[통합 게이트웨이]</strong> Slack / Teams / Discord Chat &rarr; Switch Unified Gateway &rarr; Tool Execution & RAG Sandbox &rarr; In-thread Markdown Response
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                모든 대화 기록과 기업 내부 지식 조회가 외부 클라우드가 아닌 자체 사내 인프라(On-premise)에서 암호화 처리되어 보안 규제 준수를 보장합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/sandbox-quantum/switch" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>
"""
