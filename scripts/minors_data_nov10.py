# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-10

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
          직전 발행(11월 9일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: adriadam10/mkw-recomp -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 108개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.2 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;마리오 카트 월드(스위치 2)를 PC 네이티브 바이너리로 정적 재컴파일&quot; : mkw-recomp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">adriadam10/mkw-recomp — 에뮬레이터 없이 AArch64 기계어를 C 코드로 역번역하고 Vulkan 위에서 NVN2 그래픽을 재구현한 정적 리컴파일러 (MKW-THWOMP 통합 흡수)</span>
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
            <h3 class="minor-detail-headline">JIT나 인터프리터 병목 없이 PC 네이티브 x86-64 144Hz 구동</h3>
            <div class="minor-detail-subheadline">닌텐도 스위치 2 AArch64 바이너리를 C 코드로 사전 변환하고 NVN2를 Vulkan API로 재매핑</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  차세대 콘솔 에뮬레이션이 높은 사양을 요구하는 문제를 극복하기 위해, 게임 롬의 AArch64 머신 코드를 정적 분석하여 직접 PC C 소스코드로 트랜스파일하는 파괴적 시도가 성공했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Switch 2 ROM &rarr; Static AArch64-to-C Transpiler &rarr; Vulkan NVN2 Layer &rarr; Native x86 PC Binary
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에뮬레이터 런타임 오버헤드가 전무하여 일반 내장 그래픽 노트북에서도 4K 120FPS의 부드러운 레이싱 프레임을 뽑아냅니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/adriadam10/mkw-recomp" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: herrbimmer/IDEmu -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 69개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.0 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;맥북 위에서 돌아가는 BMW iDrive 4/5/6/7/8 헤드유닛 가상 머신&quot; : IDEmu</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">herrbimmer/IDEmu — QEMU와 웹 UI를 결합해 실제 차량 없이도 CAN 버스, GPS 텔레메트리, ECU 코딩을 시뮬레이션하는 인포테인먼트 에뮬레이터</span>
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
            <h3 class="minor-detail-headline">실제 차량에 앉아 방전 위험을 감수하던 ECU 코딩과 앱 개발의 해방</h3>
            <div class="minor-detail-subheadline">QNX 기반 BMW 헤드유닛 펌웨어를 macOS QEMU에서 가상화하고 소켓 CAN으로 패킷 주입</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  차량용 앱 개발자와 튜너들이 실제 차량 배터리를 소모하며 진행하던 위험한 테스트를 책상 위 브라우저에서 안전하게 재현하기 위해 제작되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> BMW iDrive QNX Image &rarr; QEMU Virtual HW &rarr; Web SocketCAN Bridge &rarr; Safari/Chrome Web UI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  차량 인포테인먼트 리버스 엔지니어링 및 커스텀 내비게이션 앱 개발 주기를 10배 이상 단축시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/herrbimmer/IDEmu" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: kolbicz/WQFiles -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 158개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.5 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;탈옥 없이 iOS 27 전체 앱 데이터와 샌드박스를 탐색하는 파일 브라우저&quot; : WQFiles</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">kolbicz/WQFiles — worse_query 샌드박스 우회를 활용해 시스템 캐시 청소와 앱 샌드박스 내부 문서를 직접 백업하는 Objective-C 파일 매니저</span>
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
            <h3 class="minor-detail-headline">아이튠즈 백업 없이 아이폰 저장 공간의 수십 기가 유령 캐시를 직접 삭제</h3>
            <div class="minor-detail-subheadline">iOS 폐쇄 파일시스템을 열어젖히고 개별 앱 문서와 컨테이너를 직접 제어</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플의 철저한 앱 간 파일 격리로 인해 앱을 지웠다 깔아야만 정리가 되던 고질적인 앱 캐시 비대화 문제를 기기 내부에서 직접 해결합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> worse_query Sandbox Escape &rarr; /var/mobile File Descriptor &rarr; App Bundle Ingestion &rarr; Local File UI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Filza 없는 순정 iOS 기기에서도 엔지니어들이 로컬 SQLite DB나 로그 파일을 즉각 덤프해 디버깅할 수 있게 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/kolbicz/WQFiles" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 1: Claude Fable 5.2 and Mythos 5.2 -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 797 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 207.4 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;앤스로픽, 차세대 플래그십 Claude Fable 5.2 및 Mythos 5.2 전격 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">anthropic.com — 인공지능 분석 벤치마크 최고점(65점)을 갱신하며 복잡한 다단계 논리 추론과 창작적 코딩 하네스를 새롭게 정의 (벤치마크 토론 통합)</span>
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
            <h3 class="minor-detail-headline">오픈AI의 o1 계열을 넘어서는 결정론적 장문 추론 아키텍처 제시</h3>
            <div class="minor-detail-subheadline">인공지능 분석(Artificial Analysis) 인덱스 65점 달성 및 에이전트 다단계 검증 강화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  앤스로픽이 모델 경량화와 추론 깊이의 균형을 맞춘 신규 라인업(Fable/Mythos)을 기습 발표하며 프론티어 AI 경쟁의 주도권을 다시 쥐었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> User Prompt &rarr; Mythos Metacognition &rarr; Fable Parallel Drafting &rarr; Verified Output
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  SWE-bench Verified에서 74.2%를 기록하며 자율 코딩 에이전트의 단일 세션 성공률을 획기적으로 개선했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.anthropic.com/claude-fable-and-mythos-5-2" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 앤스로픽 공식 발표
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 2: USPS Official ZIP Code Boundary Polygons -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 306 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 109.2 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;미국 우체국(USPS), 공식 우편번호(ZIP Code) 경계 GIS 폴리곤 데이터 전면 무료 개방&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">postalpro.usps.com — 수십 년간 수천만 원의 라이선스 비용을 요구하던 민간 GIS 데이터 브로커 카르텔을 일거에 무너뜨린 국가 공간정보 개방</span>
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
            <h3 class="minor-detail-headline">스타트업과 오픈소스 지도 개발자들의 숙원이었던 공공 주소 경계선 무료화</h3>
            <div class="minor-detail-subheadline">ESRI나 핏니보우스(Pitney Bowes)에 지불하던 고가 GIS 데이터 구독 모델 종식</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  우편번호는 배송 경로일 뿐 면적(Polygon)이 아니라는 이유로 정부 공식 경계가 없어 민간 업체들이 독점 판매하던 왜곡된 시장이 마침내 종식되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> USPS Route Ingestion &rarr; Voronoi Spatial Tessellation &rarr; GeoJSON Boundary Polygons &rarr; Public Download
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  배달, 물류, 핀테크 스타트업들이 수천만 원의 데이터 구매 비용 없이도 법적 무결성을 가진 주소 지오코딩을 구현할 수 있게 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://postalpro.usps.com/zcb" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> USPS 공식 데이터 포털
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 3: Payments Canada Real-Time Rail -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 432 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 63.8 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;캐나다, 24/7 연중무휴 즉시 결제 국가망 Real-Time Rail (RTR) 공식 가동&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">payments.ca — 수수료 3%의 신용카드 결제망을 우회하여 은행 계좌 간 수수료 0원에 가까운 초고속 자금 정산을 지원하는 국가 인프라</span>
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
            <h3 class="minor-detail-headline">비자와 마스터카드의 독점 해자를 위협하는 ISO 20022 표준 실시간 레일</h3>
            <div class="minor-detail-subheadline">수일씩 걸리던 은행 간 상호 정산을 60초 미만 즉시 결제로 단축</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  글로벌 핀테크 경쟁에서 뒤처지던 북미 결제 시스템을 현대화하고 소상공인들의 카드 가맹점 수수료 부담을 획기적으로 줄이기 위해 국가 주도로 출범했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Payer Bank &rarr; ISO 20022 XML Message &rarr; RTR Central Clearing &rarr; Payee Instant Credit (60s)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  오픈 뱅킹 API와 결합되어 기업 간 B2B 대금 결제 및 급여 즉시 지급 소프트웨어의 폭발적 성장을 견인할 전망입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.payments.ca/canada-launches-real-time-rail-bring" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Payments Canada 발표문
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: yetone/rewind-for-x -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 226개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.0 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;타임라인에서 스크롤로 지나쳐버린 트윗을 찾아내는 로컬 타임머신&quot; : rewind-for-x</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">yetone/rewind-for-x — X(트위터) 홈 피드에서 스크롤을 내리며 화면에 렌더링된 모든 글을 브라우저 로컬 IndexedDB에 인덱싱해 검색하는 크롬 확장</span>
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
            <h3 class="minor-detail-headline">'아까 그 글 어디 갔지?'의 영원한 고통을 로컬 시맨틱 검색으로 해결</h3>
            <div class="minor-detail-subheadline">X의 유료 API 없이도 브라우저 뷰포트 MutationObserver로 실시간 스트림 캡처</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  알고리즘 피드가 새로고침되면서 영원히 사라져버리던 유용한 테크 정보와 북마크 미지정 트윗을 완벽히 복원하고자 개발되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> X Feed DOM Mutation &rarr; Text & Media Ingestion &rarr; Local IndexedDB FTS &rarr; Instant Popup Search
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  외부 서버 전송이 전무한 100% 온디바이스 로컬 검색을 통해 사용자의 프라이버시를 완벽히 보호합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/yetone/rewind-for-x" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: skild-ai/steel -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 69개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.8 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;피지컬 AI와 로봇 시뮬레이션을 위한 초경량 강체 물리 엔진&quot; : steel</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">skild-ai/steel — 무거운 PhysX나 MuJoCo의 의존성을 걷어내고 대규모 병렬 강화학습 환경에 최적화된 C++/CUDA 물리 솔버</span>
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
            <h3 class="minor-detail-headline">수만 대의 로봇 팔과 사족보행 로봇을 단일 GPU에서 실시간 물리 연산</h3>
            <div class="minor-detail-subheadline">선형 보완 문제(LCP) 접촉 역학을 GPU 메모리 연속 배치로 병렬화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  로보틱스 파운데이션 모델 학습에 필수적인 초고속 물리 시뮬레이션 환경의 라이선스 제약과 메모리 병목을 극복하기 위해 오픈되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Robot URDF &rarr; CUDA Rigid Body Solver &rarr; LCP Contact Constraints &rarr; Parallel RL Policy Update
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  기존 엔진 대비 프레임 처리량이 4배 향상되어 Sim-to-Real 강화학습 소요 시간을 며칠에서 몇 시간으로 단축했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/skild-ai/steel" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: professorsolderin/project-lighthouse -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 47개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.9 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;역사가 읽지 못한 고문서와 고지도를 복원하는 AI 파이프라인&quot; : Project Lighthouse</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">professorsolderin/project-lighthouse — 곰팡이와 마모로 훼손된 중세 필사본과 아카이브 스캔본의 레이아웃을 복구하고 텍스트를 전사하는 파이썬 툴체인</span>
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
            <h3 class="minor-detail-headline">사람의 눈으로 판독 불가능한 잉크 번짐과 얼룩을 신경망 확산으로 복원</h3>
            <div class="minor-detail-subheadline">다파장 분광 이미지와 초해상화 모델을 결합해 훼손된 인류 기록을 디지털화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  국립 도서관과 박물관 수장고에서 썩어가던 수백만 권의 미판독 고문서를 인공지능 비전 기술로 구출하려는 학술적 프로젝트입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Damaged Manuscript Scan &rarr; Diffusion Inpainting &rarr; Layout Segmentation &rarr; TEI XML Transcript
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  문서 복원 비용을 90% 이상 절감하며 인문학 연구자들이 수백 년 전 잊힌 역사적 진실을 발굴하는 데 기여하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/professorsolderin/project-lighthouse" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 4: Fold Epic Paper Airplanes -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 779 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 74.5 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;공기역학 시뮬레이션 기반 궁극의 종이비행기 접기 공학&quot; : Foldable Flight</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">foldableflight.com — 단순한 취미를 넘어 양력(Lift), 항력(Drag), 상반각(Dihedral) 안정성을 3D 브라우저 시뮬레이터로 계산한 인터랙티브 종이비행기 설계소</span>
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
            <h3 class="minor-detail-headline">A4 용지 한 장에 담긴 항공우주 역학과 기하학적 접기 알고리즘</h3>
            <div class="minor-detail-subheadline">단계별 3D 인터랙티브 가이드와 활공비(Glide Ratio) 극대화 설계 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  항공 엔지니어링 원리를 일반인과 아이들에게 가장 직관적이고 아름다운 웹 인터페이스로 시각화하여 해커뉴스 사용자들의 폭발적 추천을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Fold Geometry &rarr; CFD Aerodynamic Solver &rarr; 3D WebGL Step-by-Step &rarr; 100m Flight Glider
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  복잡한 항공 물리 공식을 누구나 브라우저에서 조작할 수 있는 순수 웹 교육 콘텐츠의 정점을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.foldableflight.com" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 웹사이트
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 5: Is Opus 5.5 Nerfed? -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 680 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 15.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 43.3 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클로드 오퍼스 5.5 너프 논란: 11월 3일 시스템 프롬프트 변경과 사고 패턴 퇴행 분석&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">twitter.com/shanemelaugh — 앤스로픽이 서버 비용 절감을 위해 오퍼스의 내부 CoT(생각 과정)를 강제 조기 종료시키고 있다는 정밀 벤치마크 폭로</span>
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
            <h3 class="minor-detail-headline">'더 빠르게' 대답하려다 복잡한 리팩토링 능력을 상실한 빅테크 LLM의 딜레마</h3>
            <div class="minor-detail-subheadline">다단계 코딩 검증에서 생각 토큰(Thinking Tokens) 길이가 40% 강제 축소된 실측 데이터 제시</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유료 구독자들이 체감하던 코딩 능력 저하가 단순한 기분 탓이 아니라 시스템 수준의 강제 제약이었음이 통계적으로 입증되며 거센 반발이 일어났습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[분석 데이터]</strong> Nov 2 Pre-patch CoT (8.2k tokens) &rarr; Nov 3 Post-patch (3.4k tokens) &rarr; Complex Bug Regression
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  클라우드 기반 폐쇄형 모델의 묵시적 잠수함 패치 위험성을 부각하며 로컬 오프라인 오픈소스 LLM(DeepSeek)으로의 전환을 가속화하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://twitter.com/shanemelaugh/status/2119192075505893695" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 커뮤니티 분석 전문
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 6: Humans Will Never Again Create Wikipedia -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 463 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 45.0 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;인류는 다시는 위키피디아 같은 프로젝트를 만들지 못할 것이다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">economist.com — AI 지식 합성 엔진의 범람으로 인해 웹의 순수한 이타적 집단 지성과 크라우드소싱 백과사전의 시대가 영원히 막을 내렸다는 이코노미스트의 문명 비평</span>
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
            <h3 class="minor-detail-headline">사람이 기여하던 웹에서 AI가 요약하고 인간은 소비만 하는 웹으로의 전환</h3>
            <div class="minor-detail-subheadline">검색 트래픽 급감과 기여자 고갈로 위기에 처한 위키피디아의 존립 기반 조명</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  퍼플렉시티나 챗GPT 같은 답변 엔진이 출처 웹사이트 방문을 대체하면서, 자원봉사자들의 동기부여가 소멸하는 인터넷 생태계의 비극을 진단했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[생태계 악순환]</strong> Zero-Click AI Answer &rarr; Wikipedia Pageview Drop &rarr; Editor Depletion &rarr; Primary Knowledge Collapse
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  원천 지식 생산자에 대한 새로운 보상 프로토콜과 공공 지식 커먼즈(Commons) 보호 기금 조성을 촉구하는 담론을 촉발했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.economist.com/culture/2026/10/29/humans-will-never-again-create-a-project-quite-like-wikipedia" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> The Economist 원문
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: 0xCodez/iphone-mirror-windows -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 112개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.8 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;윈도우 PC에서 맥OS처럼 아이폰을 띄우고 마우스로 조작하는 미러링 도구&quot; : iphone-mirror-windows</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">0xCodez/iphone-mirror-windows — 윈도우 화면에 프레임리스 아이폰 창을 띄워 에어플레이 화면과 소리를 수신하고 USB 마우스/키보드로 제어하는 파이썬 유틸리티</span>
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
            <h3 class="minor-detail-headline">맥 전용 기능이었던 '아이폰 미러링(iPhone Mirroring)'을 윈도우 환경에 이식</h3>
            <div class="minor-detail-subheadline">AirPlay 프로토콜 역공학과 WebDriverAgent 입력 파이프라인 결합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플 실리콘 맥에서만 지원되던 화면 미러링 연동 기능을 윈도우 및 리눅스 PC 사용자들에게도 동일한 사용자 경험으로 제공하기 위해 오픈되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> iPhone AirPlay Stream &rarr; Windows AirPlay Receiver &rarr; Frameless GUI &rarr; USB WebDriverAgent Input
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  아이폰에 별도 앱을 설치할 필요 없이 순정 상태 그대로 윈도우 작업 표시줄 옆에서 알림 확인과 타이핑이 가능합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/0xCodez/iphone-mirror-windows" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: gokayfem/image-to-sculpt -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 189개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.5 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;단 한 장의 사진으로 실측 치수를 가진 정밀 3D 조각 메시를 생성&quot; : image-to-sculpt</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">gokayfem/image-to-sculpt — 피사체 사진 한 장에서 카메라 렌즈 왜곡을 역산하고 표면 법선 벡터와 깊이 맵을 합성해 3D 프린팅 가능한 STL을 추출하는 파이썬 파이프라인</span>
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
            <h3 class="minor-detail-headline">포토그래메트리의 번거로운 수백 장 다각도 촬영을 단일 샷으로 대체</h3>
            <div class="minor-detail-subheadline">단안 깊이 추정(Monocular Depth)과 표면 세부 디테일의 하이브리드 등록</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  피규어 조각가와 제품 디자이너들이 스케치나 제품 사진 한 장만으로도 즉시 3D CAD나 블렌더(Blender)에서 수정 가능한 기초 베이스 메시를 얻기 위해 개발되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> 2D RGB Image &rarr; Intrinsic Camera Calibration &rarr; Surface Normal Depth Map &rarr; Watertight STL Mesh
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  기존 NeRF나 가우시안 스플래팅과 달리 부피가 닫힌 방수(Watertight) 솔리드 메시를 직접 생성하여 3D 프린터로 즉시 출력 가능합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/gokayfem/image-to-sculpt" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: stevenmichaelthomas/numbrone -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 107개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.2 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;여러 코딩 에이전트들을 조율하는 총괄 비서실장(Chief of Staff)&quot; : numbrone</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">stevenmichaelthomas/numbrone — 사용자의 광범위한 요구사항을 프로젝트별 매니저 에이전트와 QA 에이전트에게 지능적으로 라우팅하는 경량 오케스트레이션 쉘</span>
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
            <h3 class="minor-detail-headline">에이전트가 늘어날수록 통제 불능이 되던 멀티 에이전트 병목을 계층형 지휘 체계로 해결</h3>
            <div class="minor-detail-subheadline">Claude Code, Codex, Aider 인스턴스를 단일 총괄 콘솔에서 하위 티켓으로 배분</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  개발자가 수많은 터미널 창을 띄워놓고 각 에이전트에게 일일이 작업을 지시하다가 발생하는 컨텍스트 오염과 중복 작업을 막기 위해 고안되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> High-level User Goal &rarr; Numbrone Chief of Staff &rarr; Sub-task Delegation &rarr; Cross-agent State Sync
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단일 개발자가 수십 대의 에이전트 편대를 거느린 소프트웨어 개발팀의 총괄 엔지니어링 매니저 역할을 수행할 수 있도록 지원합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/stevenmichaelthomas/numbrone" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 7: Unlocking Any Car from Brand X -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 594 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.3 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;글로벌 완성차 X사의 전 세계 모든 차량을 원격으로 열 수 있었던 취약점 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">shubs.io — 스마트폰 커넥티드 카 텔레매틱스 API의 인증 토큰 검증 부실로 수백만 대의 차량 문을 열고 시동을 걸 수 있었던 치명적 결함 분석</span>
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
            <h3 class="minor-detail-headline">클라우드와 연결된 커넥티드 카가 직면한 현대 자동차 보안의 허술한 민낯</h3>
            <div class="minor-detail-subheadline">차대번호(VIN) 조작만으로 차량 소유권을 가로채는 BOLA(Broken Object Level Auth) 취약점</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  책임감 있는 보안 공개(Responsible Disclosure) 이후 패치가 완료됨에 따라 전 세계 수백만 대의 스마트 자동차를 위협했던 API 취약점의 실체가 상세히 공개되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[공격 벡터]</strong> Mobile App Telematics API &rarr; VIN Parameter Tampering &rarr; BOLA Auth Bypass &rarr; Remote Door Unlock
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  완성차 제조사들이 소프트웨어 정의 차량(SDV)을 개발할 때 클라우드 API 게이트웨이의 보안 감사 기준을 근본적으로 강화하는 계기가 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-t" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 보안 연구원 분석 전문
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 8: Chimera Vocal Synth -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 335 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 13.9 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;WebGPU 기반 브라우저 모듈형 보컬 신시사이저&quot; : Chimera</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">chimera-vocal-synth.vercel.app — 물리적 성대(Vocal Tract) 음향 시뮬레이션과 실시간 포먼트 모듈레이션을 브라우저에서 무지연 연산하는 웹 신디사이저</span>
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
            <h3 class="minor-detail-headline">기존 샘플러 악기의 한계를 넘어선 파라메트릭 인간 성대 물리 모델링</h3>
            <div class="minor-detail-subheadline">음절과 자음, 모음의 전이 과정을 오디오 워클릿(AudioWorklet)과 WebGPU로 실시간 합성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  무거운 VST 플러그인 설치 없이도 브라우저에서 키보드 연주만으로 사람의 음성과 합창단 소리를 유기적으로 합성할 수 있어 뮤지션들의 찬사를 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> MIDI Input &rarr; Vocal Tract Physical ODE &rarr; Formant Filter Bank &rarr; WebAudio Realtime Buffer
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹 브라우저가 전문가용 음악 제작(DAW) 워크스테이션 수준의 복잡한 물리 모델링 연산을 지연 없이 처리할 수 있음을 증명했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://chimera-vocal-synth.vercel.app/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Chimera 라이브 웹 연주
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 9: RAM Altman -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 247 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.4 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;샘 올트먼에게 매일 내 PC의 남는 RAM을 기부하겠다고 메일을 보내는 리눅스 스크립트&quot; : RAM Altman</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">respawnfirst.com — 수조 원의 데이터센터 증설에 혈안이 된 빅테크 AI 카르텔을 풍자하며 매일 아침 미사용 RAM 용량을 측정해 오픈AI CEO에게 발송하는 오픈소스 데몬</span>
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
            <h3 class="minor-detail-headline">'AI 거품론'과 천문학적 컴퓨트 비용에 지친 개발자들의 유쾌한 반란</h3>
            <div class="minor-detail-subheadline">cron 데몬과 sendmail을 이용해 리눅스 `free -h` 출력을 정중한 자선 기부 제안서로 가공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수천억 달러의 투자금 유치와 전기·메모리 부족을 호소하는 AI 업계 거물들의 호들갑을 유쾌한 오픈소스 코드로 패러디하여 폭발적인 공감을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> /proc/meminfo Read &rarr; Unused RAM Formatter &rarr; Polite Donation Letter &rarr; Cron Daily Mail Dispatch
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단순한 유머를 넘어, 리눅스 시스템 메모리 튜닝과 불필요한 데몬 정리를 상기시키는 훌륭한 시스템 관리 교육 도구로 회자되고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://respawnfirst.com/linux-script-emails-sam-altman-unus" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 프로젝트 해설 기사
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
