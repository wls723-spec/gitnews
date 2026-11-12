# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-13

FULL_MINORS_SECTION = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 & 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 12일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: DevedevT/FFmpeg-GUI-Editor-Windows -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 143개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 72.91 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;FFmpeg CLI의 난해함을 덜어낸 무설치 초경량 무손실 영상 컷 편집기&quot; : FFmpeg-GUI-Editor-Windows</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">DevedevT/FFmpeg-GUI-Editor-Windows — 복잡한 명령어 없이 키프레임 기반 스트림 카피(Stream Copy)로 단 0.1초 만에 영상을 무재인코딩 분할하는 윈도우 네이티브 오픈 GUI</span>
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
            <h3 class="minor-detail-headline">재인코딩 화질 손실 없이 I-프레임을 실시간 파싱하여 4K 영상 분할 속도를 100배 가속</h3>
            <div class="minor-detail-subheadline">FFmpeg 7.1 바이너리와 순수 WPF 프론트엔드를 번들링해 단일 실행 파일로 즉시 작동</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유튜브 캡처나 화면 녹화 후 불필요한 부분을 잘라낼 때 무거운 프리미어나 렌더링 대기 시간에 지친 개발자들을 위해, 시스템 레지스트리 오염 없이 비디오 패킷을 바이트 단위로 복사해 저장하는 도구가 오픈소스로 공개되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Video Stream &rarr; MP4 Demuxer &rarr; Keyframe Boundary Split &rarr; Stream Copy Remux (No Re-encode)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  상용 유료 툴이나 웹 업로드 없이 내 PC에서 10GB 4K 영상을 1초 만에 무손실 슬라이싱하는 극단적 I/O 효율을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/DevedevT/FFmpeg-GUI-Editor-Windows" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: lawandrorder/mate -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 138개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.88 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;쇼핑몰 유료 광고와 트래킹을 걷어낸 텍스트 퍼스트 쇼핑 에이전트&quot; : mate</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">lawandrorder/mate — 복잡한 상품 상세페이지 광고와 어뷰징 리뷰를 정제하고 최저가 및 실질 캐시백을 터미널 대화로 찾아주는 로컬 AI 쇼핑 파트너</span>
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
            <h3 class="minor-detail-headline">다크 패턴과 미끼 상품을 LLM 구조화 추출로 걸러내는 소비자 권익 보호 에이전트</h3>
            <div class="minor-detail-subheadline">헤드리스 브라우저로 실시간 가격 히스토리와 숨은 배송비를 역추적해 비교 분석</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  이커머스 플랫폼들의 스폰서 검색 결과와 복잡한 할인 쿠폰 미로에 지친 유저들을 위해, 원하는 스펙과 예산만 자연어로 입력하면 가장 정직한 판매처를 찾아주는 텍스트 기반 인터페이스입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> User Prompt &rarr; Headless Scraper &rarr; Price History Analysis &rarr; Structured Verdict
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  상업적 알고리즘의 유혹 없이 순수 로컬 클라이언트에서 동작하여 개인 쇼핑 성향과 검색 기록의 유출을 원천 봉쇄했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/lawandrorder/mate" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: credoksopho1984/blender-ai-copilot-studio -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 21개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.42 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자연어로 3D 메시와 셰이더를 실시간 빌드하는 Blender MCP 스튜디오&quot; : blender-ai-copilot-studio</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">credoksopho1984/blender-ai-copilot-studio — Blender 뷰포트와 로컬 LLM을 FastMCP 프로토콜로 묶어 복잡한 지오메트리 노드 설정을 한 문장으로 시공</span>
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
            <h3 class="minor-detail-headline">3D 모델링 파이프라인의 메뉴 클릭 노동을 AI 에이전트 도구 호출로 치환</h3>
            <div class="minor-detail-subheadline">Python bpy 라이브러리의 방대한 속성을 샌드박스 안전 실행으로 격리하여 오류 없는 렌더링 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  3D 그래픽 아티스트들이 조명 셋업, 물리 재질 세팅, 카메라 구도 조정에 쏟는 반복 시간을 에이전트의 실시간 뷰포트 피드백 루프로 축소하기 위해 탄생했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Natural Language &rarr; Model Context Protocol &rarr; Safe bpy Sandbox &rarr; 3D Scene Manipulation
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  LLM이 단순히 2D 이미지를 생성하는 것을 넘어 실제 편집 가능한 3D 버텍스와 노드 그래프를 직접 제어하는 진화 경로를 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/credoksopho1984/blender-ai-copilot-studio" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: AIRzZ90/study-materials-fork -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 326개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 27.38 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Tauri 2와 Rust 백엔드로 완성한 크로스플랫폼 학습 인터페이스 하네스&quot; : study-materials-fork</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AIRzZ90/study-materials-fork — 무거운 일렉트론 없이 15MB 초경량 메모리 점유율로 구동되는 크로스플랫폼 데스크톱 지식 관리 프레임워크</span>
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
            <h3 class="minor-detail-headline">Tauri 2의 다중 윈도우 IPC와 Rust 로컬 SQLite FTS5 색인을 통한 밀리초 검색</h3>
            <div class="minor-detail-subheadline">웹뷰2 네이티브 바인딩을 활용해 수만 개의 마크다운 문서와 PDF를 지연 없이 렌더링</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  노션 등 클라우드 노트 도구의 구독료 인상과 네트워크 지연에 반발하여, 오프라인 우선(Local-First)과 극한의 반응 속도를 추구하는 엔지니어들의 지지를 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Markdown/PDF &rarr; Rust SQLite FTS5 &rarr; Tauri 2 Zero-Copy IPC &rarr; Native WebView Rendering
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Tauri 2의 정식 안정화 이후 데스크톱 앱 생태계에서 일렉트론을 실질적으로 대체할 수 있는 완성도 높은 아키텍처 레퍼런스를 제시했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/AIRzZ90/study-materials-fork" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: siwen-121/agent-shared-facts -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 53개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.23 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;이기종 AI 에이전트 간 검증된 사실(Fact)을 안전하게 분산 동기화하는 참조 구현체&quot; : agent-shared-facts</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">siwen-121/agent-shared-facts — 멀티 에이전트 편대에서 환각을 방지하고 상호 합의된 시스템 상태만을 불변 CRDT 그래프로 공유하는 프로토콜</span>
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
            <h3 class="minor-detail-headline">에이전트가 생성한 정보의 출처와 검증 해시를 머클 트리로 연결해 충돌 없는 협업 실현</h3>
            <div class="minor-detail-subheadline">네트워크 단절과 병렬 작업 환경에서도 최종 일관성(Eventual Consistency)을 보장하는 분산 메모리</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  여러 에이전트가 동시에 대규모 코드베이스를 리팩토링하거나 데이터 분석을 수행할 때, 서로 모순되는 컨텍스트를 주입받아 발생하는 연쇄 장애를 해결하기 위해 설계되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Agent Fact Emission &rarr; Merkle Proof Verification &rarr; CRDT Consensus &rarr; Shared Knowledge Graph
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  중앙 데이터베이스 없이도 로컬 파일 시스템과 피어 투 피어 연결만으로 신뢰 가능한 다중 에이전트 메모리 계층을 구축할 수 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/siwen-121/agent-shared-facts" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: CrommaAI/crommacode -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 14개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.75 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Claude Code·Codex·Gemini 에이전트들의 코딩 대결을 실시간 관전하는 게이미피케이션 IDE&quot; : crommacode</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">CrommaAI/crommacode — 동일한 요구 명세서(Spec)를 주고 여러 AI 코딩 모델이 서로 다른 터미널에서 경합하며 벤치마크를 수행하는 시각화 환경</span>
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
            <h3 class="minor-detail-headline">테스트 통과율, 소모 토큰, 작성 속도를 실시간 대시보드로 계측하는 투기장 인터페이스</h3>
            <div class="minor-detail-subheadline">도커 컨테이너로 격리된 각 모델의 작업 브랜치를 실시간 diff로 3단 분할 렌더링</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  다양한 코딩 하네스가 쏟아지는 가운데, 실제 프로젝트 환경에서 어떤 모델이 가장 적은 토큰으로 버그 없는 코드를 합성하는지 개발자가 직관적으로 비교하기 위해 개발되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Unified Spec &rarr; Multi-Model Harness Dispatch &rarr; Test Suite Verification &rarr; Live Arena Scoreboard
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  맹목적인 벤치마크 점수 대신 실제 런타임 단위 테스트를 통과하는 실용적 코드 생성 능력을 실시간으로 비교 검증할 수 있는 오픈 플랫폼입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/CrommaAI/crommacode" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: tigerogijzooav/Hyperliquid-Trade-Bot -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 289개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.48 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Hyperliquid 탈중앙화 거래소(DEX)의 공개 API로 승률과 손익을 실시간 분석하는 퀀트 봇&quot; : Hyperliquid-Trade-Bot</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">tigerogijzooav/Hyperliquid-Trade-Bot — L1 영구선물 DEX의 오더북 뎁스와 펀딩비 왜곡을 웹소켓으로 초저지연 스트리밍 분석하는 오픈 파이프라인</span>
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
            <h3 class="minor-detail-headline">온체인 오더북 슬리피지를 계산하고 시장가 충격을 예측하는 고성능 비동기 엔진</h3>
            <div class="minor-detail-subheadline">Python Asyncio와 Rust 확장 모듈을 결합해 10밀리초 이내 체결 상태를 추적</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  중앙화 거래소(CEX)의 신뢰 위기와 규제 압박 속에서 폭발적으로 성장하는 L1 온체인 선물 시장의 유동성을 투명하게 추적하고자 하는 트레이더들의 호응을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> DEX L1 Websocket &rarr; Orderbook Microstructure &rarr; Volatility Engine &rarr; Execution Signal
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  탈중앙 금융 인프라의 복잡한 서명 인증과 논스 처리를 완전히 캡슐화하여 알고리즘 트레이딩 진입 장벽을 낮췄습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/tigerogijzooav/Hyperliquid-Trade-Bot" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: DandanLLab/SnowCatQQ -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 207개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.49 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;NapCat과 SnowLuma 커널을 융합해 최신 QQ 9.9 런타임을 무후크 V8로 구동하는 오픈 클라이언트&quot; : SnowCatQQ</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">DandanLLab/SnowCatQQ — 위험한 메모리 인젝션 없이 공식 일렉트론 샌드박스의 V8 채널을 직접 인터셉트하여 봇 자동화 파이프라인을 전면 오픈소스로 공개</span>
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
            <h3 class="minor-detail-headline">계정 정지 리스크를 최소화하기 위해 OneBot v11 표준 IPC 채널을 순수 자바스크립트로 브릿지</h3>
            <div class="minor-detail-subheadline">메신저의 최신 9.9.37 빌드에 맞춰 프로토콜 패킷을 안정적으로 디코딩하는 오픈 프레임워크</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  폐쇄적인 상용 메신저 플랫폼들이 외부 봇 접근을 차단하는 상황에서, 커뮤니티가 합심하여 안전하고 투명한 오픈소스 연결 계층을 구축했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Electron Renderer V8 &rarr; Safe Context Intercept &rarr; OneBot v11 Protocol &rarr; Community Agent Bots
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  바이너리 변조나 DLL 하이재킹 대신 런타임 네이티브 API를 활용한 안전한 리버스 엔지니어링의 정석을 보여주었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/DandanLLab/SnowCatQQ" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: sirioberati/gradient-descent-for-a-face -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 64개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.48 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;신경망 라이브러리 없이 순수 코드로 수천 개 색상 반점에 경사하강법을 적용해 초상화를 렌더링&quot; : gradient-descent-for-a-face</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">sirioberati/gradient-descent-for-a-face — PyTorch나 TensorFlow 없이 수작업으로 유도한 편미분과 손실 함수만으로 캔버스 위의 원형 점들을 사람 얼굴로 수렴시키는 예술적 미적분</span>
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
            <h3 class="minor-detail-headline">딥러닝의 블랙박스를 벗겨내고 기하학적 프리미티브의 좌표와 반경, 색상을 직접 최적화</h3>
            <div class="minor-detail-subheadline">수학적 1차 원리(First Principles)에 기반한 경사하강법의 시각적 카타르시스</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수십억 개의 파라미터로 무장한 초거대 AI 모델의 홍수 속에서, 기계학습의 기본 단위인 미적분과 경사하강법 본연의 아름다움을 되새기고자 하는 엔지니어들의 극찬을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Random Color Blobs &rarr; Analytical Loss MSE &rarr; Analytical Gradient Step &rarr; Emergent Portrait
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  외부 라이브러리 종속성 없이 순수 알고리즘만으로 수학적 수렴 과정을 직관적 그래픽스로 증명한 탁월한 교육용 오픈소스입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/sirioberati/gradient-descent-for-a-face" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Jensen Huang Resignation -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 2,617 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 293.87 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;젠슨 황 CEO 전격 사퇴… 싱가포르 의혹과 사내 스캔들 속 33년 엔비디아 리더십 막내려&quot; : Jensen Huang Resigns</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AP News & Reuters — 미국 법무부의 대중 수출 규제 우회 조사 및 이사회 독립 감사 직후 발표된 젠슨 황의 즉각 퇴임 발표와 전 세계 반도체 시장의 지각변동</span>
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
            <h3 class="minor-detail-headline">AI 반도체 제국을 일군 전설적 창업자의 퇴장과 차기 리더십 및 공급망 불확실성</h3>
            <div class="minor-detail-subheadline">싱가포르 페이퍼컴퍼니를 통한 칩 우회 수출 의혹과 사내 규정 위반이 결합된 이사회 결정</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  해커뉴스에서 2,600개 이상의 업보트와 2,000개가 넘는 댓글이 쏟아지며 단일 테크 뉴스 중 역사상 최고 기록을 경신했습니다. 1993년 창립 이래 33년간 엔비디아를 이끌며 시가총액 1위로 올려놓았던 상징적 인물이 갑작스럽게 물러나면서 실리콘밸리가 거대한 충격에 휩싸였습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[경과 요약]</strong> Regulatory Inquiries &rarr; Special Board Audit &rarr; Resignation Announcement &rarr; Global Market Shockwave
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  독점적 가속기 생태계를 지배하던 카리스마적 리더십의 공백은 CUDA 생태계와 경쟁 오픈 표준(ROCm, OneAPI, WebGPU)의 역학 관계에 중대한 변곡점을 예고합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f" target="_blank" class="minor-link hn">
                <i data-lucide="newspaper" class="minor-icon"></i> AP 통신 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=45910231" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (2,617 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Gemini 4 Hydrogen and Orchestrator -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 404 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 85.05 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;구글 딥마인드, 초경량 실시간 스웜 오케스트레이션 모델 'Gemini 4 Hydrogen' 전격 발표&quot; : Gemini 4 Hydrogen</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Google DeepMind Blog — 거대 파라미터의 비효율을 깨고 5밀리초 추론 지연과 극단적 경량화로 멀티 에이전트 편대를 실시간 지휘하는 분산 오케스트레이터</span>
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
            <h3 class="minor-detail-headline">수십 개의 서브에이전트가 동시에 통신하는 Antigravity 환경을 위해 설계된 전용 추론 코어</h3>
            <div class="minor-detail-subheadline">KV 캐시를 10분의 1로 압축하고 도구 호출(Tool Calling) 지연 시간을 제로에 수렴시킨 차세대 아키텍처</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  에이전트가 단독으로 코딩하는 단계를 넘어 수십 개의 전문 에이전트가 팀을 이뤄 실시간 협동하는 '스웜(Swarm)' 패러다임이 확산되면서, 이를 총괄 조율할 초저지연 오케스트레이션 모델이 필수적이었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> High-level Goal &rarr; Gemini 4 Hydrogen Router &rarr; Subagent Parallel Dispatch &rarr; Realtime Consensus
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트 조율에 소모되던 수억 개의 잉여 토큰 비용을 90% 이상 절감하며 진정한 상시 가동(Always-On) 자율 에이전트 시스템을 가능하게 만들었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 구글 공식 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=45912401" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (404 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Rust 1.100.0 Release -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 307 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 70.12 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;러스트의 역사적 100번째 마이너 릴리즈 달성: 'Rust 1.100.0' 공식 출시와 언어 안정성의 승리&quot; : Rust 1.100.0 Released</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Rust Release Team — 2015년 Rust 1.0 출범 이후 11년간 하위 호환성을 완벽히 수호하며 세 자릿수 버전 고지에 도달한 기념비적 이정표</span>
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
            <h3 class="minor-detail-headline">비동기 클로저(Async Closures) 전격 안정화 및 병렬 프론트엔드 컴파일러 기본 활성화</h3>
            <div class="minor-detail-subheadline">10년 전 작성된 Rust 1.0 코드가 단 한 줄의 컴파일 에러 없이 빌드되는 불변의 안정성 증명</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  소프트웨어 생태계가 잦은 파괴적 변경(Breaking Changes)으로 몸살을 앓는 가운데, 러스트는 100번의 마이너 릴리즈 동안 엄격한 안정성 원칙을 고수하며 엔터프라이즈 시스템 언어로서의 위상을 확고히 했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[11년의 여정]</strong> Rust 1.0 (2015) &rarr; Epoch 2018/2021/2024 &rarr; Parallel Frontend &rarr; Rust 1.100.0 Milestone
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  커널, 브라우저, AI 인프라 등 현대 테크 스택의 심장부에서 C/C++을 대체하는 메모리 안전 시스템 언어로서 독보적인 신뢰도를 재확인했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/" target="_blank" class="minor-link hn">
                <i data-lucide="file-text" class="minor-icon"></i> 공식 릴리즈 공지
              </a>
              <a href="https://news.ycombinator.com/item?id=45912850" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (307 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Anthropic IPO S-1 Filing -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 763 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 69.35 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;앤스로픽, 뉴욕 증시 상장(IPO) 신청서 전격 제출… 오픈AI 대항마의 80조 원 규모 공모 착수&quot; : Anthropic IPO</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Wall Street Journal & S-1 Registration — Claude Code와 Sonnet 4의 엔터프라이즈 독주에 힘입어 전격 기업공개에 나선 앤스로픽의 재무제표와 성장 로드맵</span>
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
            <h3 class="minor-detail-headline">공공이익법인(PBC) 지배구조를 유지하며 프론티어 AI 연구 자금을 자본시장에서 직접 조달</h3>
            <div class="minor-detail-subheadline">연간 반복 매출(ARR)의 가파른 수직 상승과 컴퓨팅 인프라 비용 지출 구조 첫 공개</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  오픈AI가 영리 법인 전환 진통을 겪는 사이, 앤스로픽이 전 세계 프론티어 AI 랩 중 최초로 제도권 증권거래소에 입성하여 투명한 재무 구조를 공개하는 첫 타자가 되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[자본 구조]</strong> Research Lab Founded &rarr; Claude API Enterprise Scale &rarr; S-1 Filing &rarr; Public Market Debut
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 에이전트와 도구 호출 생태계가 단순한 기술 데모를 넘어 막대한 현금 흐름을 창출하는 거대 산업으로 제도권 검증을 받았음을 의미합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://ipo.anthropic.com/us/" target="_blank" class="minor-link hn">
                <i data-lucide="trending-up" class="minor-icon"></i> S-1 공시 사이트
              </a>
              <a href="https://news.ycombinator.com/item?id=45907812" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (763 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Why writing correct software is hard and why math won't help us -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 340 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 27.63 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;소프트웨어 무결점 검증의 한계: 정형 기호 논리와 수학만으로는 실제 버그를 박멸할 수 없는 이유&quot; : Why Writing Correct Software is Hard</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Ron Pressler (pron.github.io) — 형식 증명(Formal Proofs)과 수리 논리학이 왜 복잡계 현실 소프트웨어 엔지니어링의 모든 예외 상황을 포섭하지 못하는가에 대한 정밀 비판</span>
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
            <h3 class="minor-detail-headline">계산 복잡도와 불완전성 정리가 시스템 아키텍처와 엔지니어링 실무에 던지는 차가운 진실</h3>
            <div class="minor-detail-subheadline">수학적 모델 자체가 현실의 물리적 제약(메모리 오류, 하드웨어 타이밍)을 완벽히 모사할 수 없다는 근원적 통찰</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 에이전트의 코드 무결점 검증을 위해 형식 증명 언어(Lean 4, Coq)를 결합하려는 시도가 유행하는 가운데, 자바 가상머신(JVM) 아키텍트인 론 프레슬러의 과거 명저가 재조명되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[논리 전개]</strong> Abstract Formal Model &rarr; Mathematical Proof &ne; Real Physical Reality &rarr; Engineering Heuristics Essential
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  완벽한 수리적 검증이라는 환상에 매몰되지 않고 실용적인 관측 가능성(Observability)과 결함 격리 설계의 중요성을 일깨웠습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://pron.github.io/posts/correctness-and-complexity" target="_blank" class="minor-link hn">
                <i data-lucide="book-open" class="minor-icon"></i> 원문 에세이
              </a>
              <a href="https://news.ycombinator.com/item?id=45906871" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (340 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Humble Bundle security killed by vibecoding -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 358 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 15.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.52 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;검증 없는 무분별한 바이브 코딩(Vibecoding) 도입으로 주요 인증 보안이 붕괴된 험블번들의 비극&quot; : Vibecoding Security Fallout</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Security Community Disclosures — AI 프롬프트로 생성된 프론트엔드/백엔드 코드를 최소한의 보안 코드리뷰 없이 배포했다가 게임 키 라이브러리가 노출된 충격적 사례</span>
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
            <h3 class="minor-detail-headline">개발 속도에만 취해 보안 원칙을 망각했을 때 프로덕션에서 벌어지는 참사</h3>
            <div class="minor-detail-subheadline">API 토큰 유효성 검사 누락과 CORS 와일드카드 개방 등 AI 슬롭 코드가 빚어낸 총체적 난국</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  "AI가 코드를 짜주니 이제 시니어 엔지니어가 필요 없다"는 경영진의 과욕이 어떻게 실제 서비스의 치명적인 취약점으로 귀결되는지 생생하게 폭로되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[사고 경로]</strong> Vibe Coding Prompt &rarr; Unreviewed Code Merge &rarr; Insecure API Deployment &rarr; Key Extraction Breach
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 에이전트 도구를 채택할 때 정적 분석(SAST)과 정형 샌드박스 보안 게이트가 결코 생략될 수 없음을 알리는 경종이 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/" target="_blank" class="minor-link hn">
                <i data-lucide="alert-triangle" class="minor-icon"></i> 포럼 분석문
              </a>
              <a href="https://news.ycombinator.com/item?id=45904510" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (358 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Gemini Decisions API -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 553 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.59 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자율 에이전트의 10밀리초 분기 결정을 위한 구글 공식 'Gemini Decisions API' 출시&quot; : Gemini Decisions API</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Google Cloud & AI Developers — 장황한 자연어 생성 대신 수치형 보상 함수와 정책 결정을 고속 직렬화된 텐서로 즉시 반환하는 에이전트 특화 API</span>
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
            <h3 class="minor-detail-headline">불필요한 텍스트 토큰 디코딩 병목을 건너뛰고 이진 분기 판단만을 추출</h3>
            <div class="minor-detail-subheadline">게임 봇, 로봇 모빌리티 제어, 실시간 결제 사기 탐지 등 초저지연 도메인 전격 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  에이전트가 "예/아니오" 또는 "다음 액션 선택"만 필요할 때도 수십 개의 텍스트 토큰을 생성하느라 500밀리초 이상 대기해야 했던 낭비를 근절하기 위해 출시되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> State Vector &rarr; Logit-Direct Decision Engine &rarr; 10ms Fast Classification &rarr; Direct Action Exec
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  LLM을 텍스트 챗봇이 아닌 실시간 시스템 제어기(Controller)로 전환하는 핵심 인터페이스 인프라를 마련했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 구글 개발자 공지
              </a>
              <a href="https://news.ycombinator.com/item?id=45899812" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (553 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Critical RCE Vulnerability in Apache HTTP Server (CVE-2026-119618) -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 351 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.04 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;아파치 HTTP 웹 서버의 20년 된 핵심 모듈에서 미인증 원격 코드 실행(RCE) 제로데이 발견&quot; : Apache RCE Vulnerability</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Wiz Research Blog — 전 세계 수억 대의 레거시 리눅스 서버에서 구동되는 Apache 2.4 mod_rewrite 경로 정규화 취약점 CVE-2026-119618 분석</span>
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
            <h3 class="minor-detail-headline">특수하게 조작된 URI 인코딩 시퀀스로 버퍼 오버플로우를 유도하여 루트 권한 쉘 획득</h3>
            <div class="minor-detail-subheadline">CISA 긴급 보안 경보 발령 및 패치 버전(2.4.63) 긴급 릴리즈</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  2000년대 초반 작성된 C 코드의 메모리 관리 결함이 현대 방화벽과 WAF를 우회할 수 있다는 사실이 입증되며 인프라 보안 팀들이 비상 대응에 돌입했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[공격 체인]</strong> Crafted Malicious URI &rarr; mod_rewrite Canonicalization Flaw &rarr; Heap Overflow &rarr; Remote Shell Exec
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  오랜 세월 검증되었다고 믿었던 기반 인프라 소프트웨어라도 지속적인 메모리 안전성 감사와 리팩토링이 필수적임을 환기했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability" target="_blank" class="minor-link hn">
                <i data-lucide="shield-alert" class="minor-icon"></i> Wiz 기술 보고서
              </a>
              <a href="https://news.ycombinator.com/item?id=45902144" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (351 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Show HN: Term Sheet, Please! -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 238 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.63 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;YC 파트너가 되어 AI 허풍 스타트업의 텀시트 투자 여부를 심사하는 페이퍼즈 플리즈 패러디 게임&quot; : Term Sheet, Please!</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">termsheetplease.com — 과장된 AI 피치덱, 가짜 ARR 지표, 알맹이 없는 래퍼 앱들 사이에서 진짜 유망 기업을 감별해 승인 도장을 찍는 웹 시뮬레이션</span>
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
            <h3 class="minor-detail-headline">실리콘밸리의 AI 거품과 벤처캐피털의 묻지마 투자를 날카롭게 풍자한 인터랙티브 수작</h3>
            <div class="minor-detail-subheadline">제한된 펀드 잔액 속에서 'Glorified Wrapper' 스타트업을 걸러내지 못하면 펀드가 파산하는 디스토피아 룰</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유명 인디 게임 'Papers, Please'의 입국 심사관 메커니즘을 빌려와, 오늘날 실리콘밸리 테크 씬의 현실을 기막힌 유머와 블랙 코미디로 비틀어 큰 공감을 샀습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[게임 루프]</strong> Pitch Deck Arrival &rarr; Cross-Check Claimed Metrics &rarr; Stamp APPROVED or REJECTED &rarr; Fund Survival Check
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹 브라우저에서 무설치로 즐길 수 있는 픽셀 아트와 음향 효과로 개발자 커뮤니티의 자조와 성찰을 이끌어냈습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://termsheetplease.com/" target="_blank" class="minor-link demo">
                <i data-lucide="play" class="minor-icon"></i> 웹 게임 바로 플레이
              </a>
              <a href="https://news.ycombinator.com/item?id=45900129" target="_blank" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (238 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
