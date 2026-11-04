# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-11-05

GH_MINORS = """
      <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
      <!-- [GH 0~10h] Item 1: Balanov/equal -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 147개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.7시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;실제 API 트래픽을 즉시 로컬 샌드박스로 박제하다&quot; : Equal</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Balanov/equal — 정적 Go 바이너리 하나로 실서버 HTTP/REST 트래픽을 가로채 결정론적 로컬 모의 환경과 OpenAPI 3.0 스펙 문서를 자동 생성</span>
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
          <h3 class="minor-detail-headline">실제 운영 API 트래픽을 1초 만에 테스트 샌드박스로 역공학</h3>
          <div class="minor-detail-subheadline">복잡한 모킹(Mocking) 코드 작성의 종말… 라이브 트래픽 스니핑 기반 OpenAPI 자동화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                마이크로서비스와 써드파티 API 의존성이 커지면서 로컬 통합 테스트 환경을 구축하는 것이 엔지니어들의 최대 고통이 되었습니다. 수작업으로 모킹 서버를 코딩하지 않고, 실제 오가는 요청과 응답을 스니핑해 그대로 재현 가능한 로컬 샌드박스로 박제하는 수요를 정확히 충족합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Live API Inbound/Outbound Traffic &rarr; eBPF/Proxy Capture (Go) &rarr; Schema Inference Engine &rarr; Deterministic Local Mock Server + OpenAPI 3.0 YAML
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단일 Go 바이너리로 외부 의존성이 전혀 없으며, CI 파이프라인에서 써드파티 유료 API 호출을 완전 격리된 로컬 모의 응답으로 대체하여 테스트 비용을 0원으로 만듭니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Balanov/equal" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: Balanov/latch -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 157개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;에이전트와 서비스 사이의 단일 보안 계약&quot; : Latch</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Balanov/latch — AI 에이전트가 외부 유료 API나 민감 작업을 실행하기 전 견적(Quote), 인간 승인(Approve), 원자적 지불 실행을 강제하는 초경량 HTTPS 프로토콜</span>
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
          <h3 class="minor-detail-headline">AI 에이전트의 지갑과 권한을 통제하는 마이크로 계약 레이어</h3>
          <div class="minor-detail-subheadline">불투명한 과금과 파괴적 API 호출을 사전에 차단하는 3단계 핸드셰이크</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                자율 에이전트가 클라우드 자원을 프로비저닝하거나 유료 모델을 연속 호출하다가 예상치 못한 수백만 원의 청구서를 만드는 '에이전트 과소비 사고'가 빈번해졌습니다. Latch는 실행 전 반드시 비용과 영향도를 견적서로 제출하게 만드는 안전장치를 제공합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[프로토콜 흐름]</strong> Agent Task &rarr; Latch Quote Phase (비용/자원 산정) &rarr; Human/Policy Gatekeeper Approval &rarr; Atomic Execution Token 발급
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                REST API 규격에 단 2개의 헤더만을 추가하여 동작하며, 기업 내부 결재 시스템(Slack, Teams 등)과 웹훅으로 연동되어 엔터프라이즈 거버넌스를 완벽히 충족합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Balanov/latch" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: silverdugongenhance/PromptReel -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 104개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.9시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 13.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;프롬프트 한 줄로 내 PC에서 숏폼 비디오 생성&quot; : PromptReel</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">silverdugongenhance/PromptReel — 로컬 GPU에서 텍스트 프롬프트를 고품질 비디오 숏폼 클립으로 직접 렌더링하는 무료 데스크톱 오픈소스</span>
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
          <h3 class="minor-detail-headline">클라우드 구독료 없는 온디바이스 텍스트-투-비디오 스튜디오</h3>
          <div class="minor-detail-subheadline">Wan2.1 및 오픈 비디오 확산 모델을 원클릭 패키징으로 로컬 구동</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                유료 AI 영상 생성 SaaS(Runway, Kling 등)의 비싼 크레딧 정책에 지친 크리에이터와 개발자들을 위해, 최신 오픈 소스 비디오 디퓨전 모델들을 파이썬 환경 설정 없이 실행 가능한 독립 데스크톱 앱 형태로 배포해 화제를 모았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[렌더링 파이프라인]</strong> Text Prompt &rarr; Open Video Diffusion Model (FP8 Quantized) &rarr; Temporal Attention Frame Synthesis &rarr; Local MP4 Export
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                8GB VRAM의 보급형 엔비디아 GPU에서도 돌아가도록 FP8 양자화와 메모리 오프로딩을 최적화해 일반 PC에서도 영상 합성이 가능하도록 문턱을 낮췄습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/silverdugongenhance/PromptReel" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
      <!-- [GH 10~20h] Item 4: ChannelDivinerCast/VSCode-Extension-Helper -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 163개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.2시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;VS Code 메모리 누수의 주범을 찾아내는 감시견&quot; : Extension-Helper</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ChannelDivinerCast/VSCode-Extension-Helper — 수십 개의 확장 프로그램 중 CPU와 RAM을 잠식하고 에디터를 멈추게 하는 불량 확장을 실시간 프로파일링</span>
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
          <h3 class="minor-detail-headline">느려진 VS Code의 범인을 1초 만에 색출하는 성능 진단 유틸리티</h3>
          <div class="minor-detail-subheadline">Extension Host 프로세스 모니터링과 자동 격리 재시작 기능 지원</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 어시스턴트, LSP, 린터 등 다양한 확장을 설치하면서 VS Code 에디터가 수 GB의 메모리를 먹고 프리징되는 현상이 잦아졌습니다. 내장 프로세스 탐색기보다 훨씬 직관적으로 문제를 일으키는 원인 모듈을 즉시 비활성화할 수 있습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[모니터링 체계]</strong> Extension Host IPC Traffic &rarr; Memory Leak & Event Loop Lag Detector &rarr; Extension Freeze Alert & Auto Throttle
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                이벤트 루프 지연(Event Loop Lag)을 마이크로초 단위로 추적하여, 타이핑 렉의 직접적인 원인이 되는 백그라운드 JSON-RPC 통신을 즉시 잡아냅니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/ChannelDivinerCast/VSCode-Extension-Helper" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: floci-io/floci -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 1,082개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 75.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;LocalStack 유료화에 반발한 완전 무료 AWS 로컬 에뮬레이터&quot; : Floci</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">floci-io/floci — 가볍고 푹신하며 영원히 무료(Always Free)… S3, SQS, DynamoDB, Lambda 로컬 에뮬레이션을 단일 경량 컨테이너로 완벽 지원</span>
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
          <h3 class="minor-detail-headline">클라우드 로컬 테스트의 자유를 되찾다: 포터블 AWS 에뮬레이터</h3>
          <div class="minor-detail-subheadline">상용 라이선스 제약 없는 순수 오픈소스 대안의 폭발적 반응</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 로컬 AWS 개발의 표준이었던 LocalStack이 핵심 엔터프라이즈 기능들을 유료 Pro 플랜으로 전환하고 라이선스를 강화하자, 오픈소스 커뮤니티가 "가볍고 영원히 무료인 대안"을 모토로 자발적으로 구축한 순수 오픈소스 프로젝트입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처]</strong> AWS SDK CLI Calls &rarr; Floci Universal Gateway (Netty) &rarr; Mock Engine (S3/SQS/DynamoDB/Lambda) &rarr; Zero-Cloud Offline Response
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                시작 시간이 1초 미만으로 매우 가벼우며, 기존 AWS SDK 코드나 테라폼(Terraform) 스크립트에서 엔드포인트 URL 하나만 바꾸면 즉시 호환되어 CI 환경의 테스트 실행 속도를 극적으로 단축합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/floci-io/floci" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: thedotmack/claude-mem -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 1,165개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 82.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;세션이 끝나도 기억을 잃지 않는 AI 에이전트 메모리&quot; : claude-mem</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">thedotmack/claude-mem — 여러 세션에 걸쳐 모든 에이전트 인터랙션과 개발 맥락을 영구 보존하고 연관 컨텍스트를 동적으로 주입하는 매니저</span>
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
          <h3 class="minor-detail-headline">AI 에이전트의 단기 기억 상실증을 치료하는 영구 컨텍스트 레이어</h3>
          <div class="minor-detail-subheadline">세션 재시작 때마다 반복 설명하던 개발 히스토리를 SQLite 벡터 DB에 자동 축적</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Claude Code나 터미널 에이전트를 재부팅할 때마다 이전 대화 맥락과 아키텍처 결정 사항을 다시 설명해야 했던 고질적 불편함을 해결합니다. 백그라운드에서 모든 프롬프트와 수정 내역을 시맨틱 태깅하여 지속 보존합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[메모리 파이프라인]</strong> Session Interaction &rarr; Semantic Distillation Engine &rarr; Local SQLite + Vector Index &rarr; Pre-Prompt Context Injector
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                토큰 한도를 낭비하는 무차별 전체 대화 주입 대신, 현재 질문과 가장 관련성이 높은 과거 의사결정 레코드 상위 3~5개만을 추려 프롬프트 앞에 스마트 주입합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/thedotmack/claude-mem" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
      <!-- [GH 20~30h] Item 7: github/spec-kit -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 810개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 45.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;GitHub이 공식 제안하는 명세 주도 개발(SDD) 툴킷&quot; : spec-kit</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">github/spec-kit — AI 에이전트 코딩 시대에 걸맞은 요구사항 명세 작성, 계약 기반 검증, 스펙-구현 일치성 자동 점검 도구 모음</span>
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
          <h3 class="minor-detail-headline">AI 시대에는 '코드 작성'보다 '정밀한 스펙 정의'가 핵심이다</h3>
          <div class="minor-detail-subheadline">GitHub Next 팀의 노하우가 집약된 Spec-Driven Development 프레임워크</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                에이전트가 코드를 눈 깜짝할 사이에 짤 수 있게 되면서, 개발자의 역할은 '코더'에서 '명세 작성자(Specifier)'로 전환되고 있습니다. GitHub 공식 팀이 불명확한 자연어 요구사항을 기계 검증 가능한 정형 스펙으로 가공하는 표준 툴킷을 배포했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[SDD 파이프라인]</strong> High-Level PRD &rarr; spec-kit Formal Schema Synthesizer &rarr; Agent Code Generation Loop &rarr; Spec Contract Test Runner
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                생성된 코드가 원래 스펙을 100% 만족하는지 AST(추상 구문 트리)와 테스트 케이스로 역방향 추적 검증하여, 에이전트가 저지르기 쉬운 조용한 기능 누락을 잡아냅니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/github/spec-kit" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: shiyu-coder/Kronos -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 506개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 32.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;금융 시장의 언어를 이해하는 오픈 파운데이션 모델&quot; : Kronos</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">shiyu-coder/Kronos — 주가 시계열, 오더북 호가창 흐름, 금융 뉴스를 단일 트랜스포머 임베딩 공간에서 융합 처리하는 금융 특화 AI 모델</span>
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
          <h3 class="minor-detail-headline">시계열 수치와 비정형 텍스트를 하나의 토큰 공간으로 통합</h3>
          <div class="minor-detail-subheadline">퀀트 알고리즘과 거시 경제 이벤트의 상관관계를 추론하는 금융 파운데이션 아키텍처</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                일반적인 거대 언어 모델(LLM)은 정밀한 시계열 수치 예측에 약하고, 기존 머신러닝 시계열 모델은 뉴스의 복잡한 맥락을 해석하지 못했습니다. Kronos는 이 두 영역을 결합한 최초의 고성능 오픈 가중치 금융 모델로 퀀트 개발자들의 큰 주목을 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[멀티모달 융합]</strong> High-Frequency Order Book Data + Macro News Stream &rarr; Dual-Stream Transformer &rarr; Volatility & Trend Probabilistic Head
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                패치 단위 시계열 토크나이저(PatchTST) 기법을 개량하여 연속형 수치 데이터를 정보 손실 없이 양자화 인코딩하며, 백테스팅 프레임워크와 직접 연동됩니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/shiyu-coder/Kronos" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: liguobao/ds-harness-remote -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 237개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 트렌딩 급상승</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;DeepSeek 에이전트를 모바일과 웹 어디서나 P2P 원격 제어&quot; : ds-harness-remote</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">liguobao/ds-harness-remote — 저지연 종단간 암호화 P2P 네트워크를 통해 사무실 PC의 DeepSeek Harness 인프라를 스마트폰에서 통제</span>
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
          <h3 class="minor-detail-headline">중앙 서버 없는 WebRTC 기반의 초저지연 AI 에이전트 리모트 컨트롤</h3>
          <div class="minor-detail-subheadline">외부 클라우드를 거치지 않는 프라이빗 P2P 터널링으로 보안 누출 방지</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                로컬 데스크톱에서 장시간 돌아가는 DeepSeek 추론 및 에이전트 작업을 외출 중에도 모바일로 확인하고 지시를 내리고 싶어 하는 개발자들을 위해, 중간 중계 서버 없이 직접 암호화 터널을 뚫어주는 경량 원격 솔루션입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[P2P 구조]</strong> Mobile Web Client &rarr; Encrypted WebRTC DataChannel &rarr; Local Desktop DeepSeek Harness &rarr; Real-time Terminal Stream
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                포트 포워딩이나 복잡한 VPN 설정 없이 NAT 트래버설(STUN/TURN)을 통해 즉시 연결되며, 반응 속도가 20ms 미만으로 매끄러운 모바일 터미널 타이핑을 보장합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/liguobao/ds-harness-remote" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
          </div>
        </div>
      </div>
"""
