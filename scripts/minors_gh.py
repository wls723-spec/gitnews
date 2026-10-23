# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items

GH_MINORS = """
      <!-- [GH 0~10h] Item 1: bowenliang123/dsh-context -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 3,405개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.2시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 29.6 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;딥시크 하네스 컨텍스트가 한눈에 보인다&quot; : 멀티 에이전트 생애주기 투시 플러그인</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">bowenliang123/dsh-context — DeepSeek Harness 전용 풀 컨텍스트 대시보드 및 플릿 모니터</span>
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
          <h3 class="minor-detail-headline">딥시크 하네스(DeepSeek Harness) 컨텍스트 투시경: Dsh-Context</h3>
          <div class="minor-detail-subheadline">토큰 압축률, 에이전트 패밀리 트리(Fleet), 메시지 진화 과정을 실시간 사이드바 캔버스에 시각화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                DeepSeek의 오픈 하네스 생태계가 급팽창하면서 수많은 서브에이전트들이 복잡한 세션을 주고받고 있으나, 컨텍스트 윈도우 내부에서 어떤 토큰이 낭비되고 압축되는지 모니터링할 방법이 없었습니다. <code>dsh-context</code>는 DeepSeek 공식 코어 개발진의 추천을 받으며 실시간 대시보드와 <code>/context</code> 슬래시 커맨드를 즉시 제공합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Session Context Stream &rarr; Token Decomposition AST &rarr; Fleet Family Tree &rarr; Real-Time UI Sidebar
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                현재 실행 중인 부모 에이전트와 서브에이전트들의 카드별 토큰 점유율을 실시간으로 추적하여, 컨텍스트 오버플로로 인한 세션 유실을 사전에 차단합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/bowenliang123/dsh-context" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: max-sixty/worktrunk -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 9,398개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.5시간 전 릴리즈</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 31.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;에이전트 10마리를 동시에 돌린다&quot; : 브랜치처럼 쉬워진 깃 워크트리 CLI</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">max-sixty/worktrunk — Claude Code 및 Codex 병렬 작업을 위한 러스트 워크트리 매니저</span>
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
          <h3 class="minor-detail-headline">병렬 에이전트 작업을 위한 워크트리 혁신: Worktrunk</h3>
          <div class="minor-detail-subheadline">번거로운 `git worktree add` 타이핑을 종식하고 단 한 줄 명령어로 격리 작업공간 자동 스캐폴딩</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Claude Code와 Codex 같은 코딩 에이전트가 1시간 이상 자율 작업을 수행할 수 있게 되면서, 개발자들은 5~10개의 에이전트를 동시에 돌리기 시작했습니다. 그러나 동일 디렉토리에서 작업하면 파일 충돌이 발생하고, 깃 순정 워크트리 명령어는 브랜치 이름과 경로를 3번씩 쳐야 할 정도로 번거로웠습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> <code>wt switch feat</code> &rarr; Template Path Resolution &rarr; Isolated Worktree Directory &rarr; Agent Parallel Execution
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                러스트로 구현되어 0ms에 디렉토리를 전환하며, 에이전트들이 서로의 변경 사항을 덮어쓰지 않고 완전 병렬로 기능 개발을 완료할 수 있도록 보장합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/max-sixty/worktrunk" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://worktrunk.dev" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 문서</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: agentgateway/agentgateway -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 1,842개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;MCP 서버와 에이전트 트래픽의 보안 관문&quot; : 차세대 에이전틱 리버스 프록시</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">agentgateway/agentgateway — 엔비디아와 앤스로픽 툴콜을 위한 제로 트러스트 게이트웨이</span>
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
          <h3 class="minor-detail-headline">MCP 서버와 자율 에이전트를 위한 보안 프록시: AgentGateway</h3>
          <div class="minor-detail-subheadline">JSON-RPC 툴콜 인가, 토큰 버킷 속도 제한, 프롬프트 인젝션 런타임 차단 엔진</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Model Context Protocol(MCP) 서버들이 엔터프라이즈 사내망에 직접 연결되면서, 악의적인 툴 인자(Tool Arguments)나 과도한 API 호출로 백엔드가 마비되는 사태가 발생하고 있습니다. Envoy/Nginx로는 이해할 수 없는 에이전트 전용 L7 프록시가 요구되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Agent JSON-RPC Request &rarr; Schema Validation & Policy Filter &rarr; Upstream MCP Server &rarr; Redacted Response
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                모든 툴 호출에 세분화된 RBAC 권한을 부여하고, 외부로 반출되는 민감한 PII 데이터를 런타임에 자동 마스킹하여 안전한 MCP 생태계를 구축합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/agentgateway/agentgateway" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 4: twentyhq/twenty -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 16,840개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14시간 전 릴리즈</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 43.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;세일즈포스의 아성을 허무는 AI 오픈소스 CRM&quot; : Twenty 1.0 대규모 업데이트</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">twentyhq/twenty — 코드로 정의하는 고객 데이터 파이프라인과 자율 AI 에이전트 연동</span>
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
          <h3 class="minor-detail-headline">세일즈포스를 대체하는 오픈소스 AI CRM: Twenty</h3>
          <div class="minor-detail-subheadline">CLI 스캐폴딩(`npx create-twenty-app`)과 네이티브 AI 워크플로 엔진 탑재</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                세일즈포스의 복잡하고 비싼 라이선스에 지친 테크 기업들이 엔지니어링 친화적인 오픈소스 CRM으로 대거 이주하고 있습니다. Twenty는 객체, 필드, 뷰를 타입스크립트 코드로 버전 관리할 수 있도록 지원합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Code-first CRM Schema &rarr; GraphQL/REST Gateway &rarr; Autonomous Sales Agent Hook &rarr; Modern React UI
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                AI 에이전트가 고객 파이프라인 상태를 실시간 감지하여 맞춤형 제안서를 자동 생성하고 거래 성사 확률을 예측하는 올인원 워크플로를 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/twentyhq/twenty" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://twenty.com" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 웹사이트</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: HKUDS/Vibe-Trading -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 2,980개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16시간 전 릴리즈</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;명령어 한 줄로 만드는 개인화 퀀트 트레이더&quot; : 홍콩대 데이터사이언스 랩 Vibe-Trading</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">HKUDS/Vibe-Trading — FastAPI 백엔드와 React 19 기반의 자율 금융 거래 에이전트</span>
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
          <h3 class="minor-detail-headline">개인용 자율 트레이딩 에이전트: Vibe-Trading</h3>
          <div class="minor-detail-subheadline">시장 뉴스 감성 분석, 기술 지표 연산, 포트폴리오 리밸런싱을 자율 실행</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                헤지펀드의 전유물이었던 복합 다중 지표 기반 알고리즘 트레이딩을 개인 개발자도 오픈소스 LLM 에이전트 프레임워크로 구현할 수 있게 되었습니다. PyPI 패키지로 <code>pip install vibe-trading-ai</code> 즉시 가동을 지원합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Multi-Exchange Ticker Feed &rarr; Sentiment NLP Engine &rarr; Risk Parameter Solver &rarr; Automated Trade Dispatcher
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                손실 제한(Stop-loss)과 위험 선호도를 에이전트 정책으로 엄격히 강제하여 감정적 뇌동매매를 차단하는 결정론적 리스크 가드레일을 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/HKUDS/Vibe-Trading" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: luongnv89/claude-howto -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 4,510개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18시간 전 업데이트</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;클로드 코드를 지배하는 실전 시각화 쿡북&quot; : 기초부터 멀티 에이전트 편대까지</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">luongnv89/claude-howto — 즉시 복사해 쓰는 실전 프롬프트와 에이전트 하네스 템플릿</span>
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
          <h3 class="minor-detail-headline">Claude Code 완벽 마스터 가이드: Claude-Howto</h3>
          <div class="minor-detail-subheadline">터미널 CLI 단축키부터 서브에이전트 스킬 연동까지 다이어그램으로 시각화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                공식 문서만으로는 알기 어려운 Claude Code의 숨겨진 설정(비용 제한, 컨텍스트 압축 우회, 커스텀 슬래시 커맨드 바인딩)을 100여 개의 시각 자료와 실행 가능한 코드로 집대성했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> CLI Primitives &rarr; Context Management Rules &rarr; Custom Skill Templates &rarr; Autonomous Loop Mastery
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                개발자가 수작업으로 겪어야 했던 수십 번의 시행착오를 단축하고, 첫 실행부터 최적화된 에이전트 코딩 생산성을 이끌어냅니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/luongnv89/claude-howto" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 7: remotion-dev/remotion -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 23,410개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22시간 전 릴리즈</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 34.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;React 코드로 굽는 60fps 결정론적 비디오&quot; : Remotion 5.0 메이저 도약</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">remotion-dev/remotion — 웹 개발자가 동영상 편집기를 대체하는 프로그래밍 비디오 엔진</span>
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
          <h3 class="minor-detail-headline">코드로 비디오를 프로그래밍하는 프레임워크: Remotion</h3>
          <div class="minor-detail-subheadline">CSS 애니메이션과 SVG 캔버스를 FFmpeg 파이프라인으로 무손실 60fps MP4 렌더링</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                생성형 AI 에이전트들이 텍스트나 정적 이미지를 넘어 동적 쇼츠(Shorts)와 데이터 기반 인포그래픽 영상을 대량 생성해야 하는 요구가 폭발하면서, 브라우저 표준 기술로 프레임 바이 프레임 비디오를 렌더링하는 Remotion이 표준으로 확고히 자리 잡았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> React Component Composition &rarr; Timeline State Interpolator &rarr; Headless Chrome Capture &rarr; FFmpeg Serverless Encoding
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                프리미어 프로나 애프터 이펙트 없이도 클라우드 람다 함수에서 수천 개의 맞춤형 개인화 비디오를 분당 수백 편씩 대량 렌더링할 수 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/remotion-dev/remotion" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://remotion.dev" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 웹사이트</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: shiyu-coder/Kronos -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 43,220개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26시간 전 업데이트</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 41.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;금융 캔들스틱을 자연어처럼 읽는 모델&quot; : 45개 거래소 학습 파운데이션 모델</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">shiyu-coder/Kronos — AAAI 2026 채택, 연속형 시계열을 이산 토큰으로 변환한 혁신</span>
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
          <h3 class="minor-detail-headline">금융 시장의 언어를 번역하는 파운데이션 모델: Kronos</h3>
          <div class="minor-detail-subheadline">전 세계 45개 주식·외환·암호화폐 거래소의 봉차트(OHLCV)를 자기회귀 트랜스포머로 사전 학습</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 시계열 예측 모델들은 단순 회귀 분석에 의존하여 급격한 시장 변동성을 포착하지 못했습니다. Kronos는 연속형 K-라인 데이터를 계층적 이산 토큰(Hierarchical Discrete Tokens)으로 양자화하여 LLM 언어 모델처럼 학습시키는 패러다임 전환을 이뤄냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Multi-Exchange Candlestick Stream &rarr; Hierarchical Tokenizer &rarr; Autoregressive Decoder &rarr; Multi-Horizon Forecast
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Hugging Face 가중치와 파인튜닝 스크립트가 오픈소스로 공개되어, 누구나 자신의 포트폴리오 자산에 특화된 퀀트 추론 엔진을 구축할 수 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/shiyu-coder/Kronos" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://shiyu-coder.github.io/Kronos-demo/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 라이브 데모</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: firecrawl/firecrawl -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 194,312개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29시간 전 릴리즈</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 35.3 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;웹 전체를 에이전트용 마크다운으로 굽는다&quot; : 초지능을 위한 데이터 라이브러리</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">firecrawl/firecrawl — 자바스크립트 렌더링과 프록시 회피를 통과하는 올인원 웹 추출기</span>
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
          <h3 class="minor-detail-headline">AI 에이전트를 위한 초고속 웹 스크래핑 엔진: Firecrawl</h3>
          <div class="minor-detail-subheadline">복잡한 SPA 웹사이트의 노이즈 태그를 걷어내고 LLM 친화적인 정제 마크다운으로 실시간 변환</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 에이전트가 웹 리서치를 수행할 때 광고, 내비게이션 바, 무의미한 자바스크립트 번들로 인해 컨텍스트 토큰이 폭발하는 문제가 지속되었습니다. Firecrawl은 단일 API 호출로 전체 도메인을 크롤링하여 순수한 마크다운 본문만 뽑아냅니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> URL Target &rarr; Headless Browser Rendering &rarr; Noise Removal Tree &rarr; Clean LLM-ready Markdown
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                웹 검색 기반 RAG 파이프라인의 토큰 소모량을 85% 이상 절감하며, 에이전트에게 환각 없는 최신 실시간 웹 데이터를 공급합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/firecrawl/firecrawl" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://firecrawl.dev" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 웹사이트</a>
          </div>
        </div>
      </div>
"""

print("GitHub Minors ready.")
