# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-27

FULL_MINORS_SECTION = r"""
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 &amp; 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 26일) 이후 30시간 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 관심 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: Pixel679-cmyk/windows-titlebar-blur-customizer -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 88개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 66.67 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Windows 10·11 창 제목 표시줄을 Aero·Acrylic·Mica DWM 블러로 복원한다&quot; : Titlebar Blur Customizer</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Pixel679-cmyk/windows-titlebar-blur-customizer — DWM 백드롭 API와 셰이더 훅으로 모든 데스크톱 앱 창에 맞춤형 유리 블러를 입히는 순수 C++ 툴킷 (LGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">평면화된 Windows 11 창 테두리에 Windows 7 Aero·Acrylic·Mica 유리 질감을 되살리는 C++ DWM 커스터마이저</h3>
            <div class="minor-detail-subheadline">LGPL-3.0 라이선스 · C++ · Windows 10/11 지원 · 다국어 UI 및 미세 DWM 블러 제어</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Windows 11의 기본 창 테두리가 단색 플랫 디자인으로 굳어지면서, 구형 Win32 앱과 최신 앱 모두에 일관된 반투명 유리(Aero Glass / Mica / Acrylic) 효과를 적용하려는 데스크톱 튜닝 수요가 큽니다. 공개 1.3시간 만에 ★88을 기록하며 유료 유틸리티(StartAllBack·MicaForEveryone 폐쇄형 포크 등)의 무료 오픈소스 대안으로 급부상했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[DWM 컴포지터 제어]</strong> App Window Handle &rarr; DWM Backdrop Hook (Aero / Acrylic / Mica) &rarr; Custom Blur &amp; Tint Rendering
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  LGPL-3.0 라이선스로 소스코드가 공개되어 있어 시스템 권한 도구를 설치할 때 가장 우려되는 백도어·텔레메트리 걱정 없이 직접 빌드하고 감사할 수 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Pixel679-cmyk/windows-titlebar-blur-customizer" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: 0x1A6C1A9Y/focus-clock -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 363개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 40.96 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;단 두 개의 파일(HTML+README)로 완성한 무설치 뽀모도로 집중 타이머&quot; : Focus Clock</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">0x1A6C1A9Y/focus-clock — 빌드 과정·서버·트래커 없이 브라우저 탭 제목에 남은 시간을 띄우고 단축키로 제어하는 초미니 웹 타이머</span>
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
            <h3 class="minor-detail-headline">npm install도 회원가입도 없이 index.html 하나를 여는 순간 작동하는 미니멀 포커스 타이머</h3>
            <div class="minor-detail-subheadline">단일 HTML 파일(5 KB) · 25/5/15분 사이클 · 스페이스바 단축키 · 탭 타이틀 실시간 표시</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  단순한 뽀모도로 타이머 앱조차 클라우드 로그인, 구독 결제, 수백 MB 일렉트론 런타임을 요구하는 현실에 지친 개발자들이 단 1개의 <code>index.html</code>로 25분 집중·5분 휴식·15분 긴 휴식과 현재 작업 메모를 구현한 이 저장소에 9시간 만에 ★363을 던졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[Zero-Build 싱글 파일]</strong> index.html (5 KB) &rarr; Circular SVG Progress + Document.title Sync &rarr; Offline Instant Focus
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로컬 파일로 그대로 열어 쓸 수 있는 '한 장짜리 소프트웨어(Single-file Web App)'가 무거운 SaaS 생산성 도구의 대척점으로 꾸준히 사랑받고 있음을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/0x1A6C1A9Y/focus-clock" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: f/family-migration-story -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 67개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.65 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;가계도 PDF를 넣으면 에이전트가 시대별 역사 조사·보고서·이주 지도 영상까지 굽는다&quot; : family-migration-story</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">f/family-migration-story — 족보 PDF/GEDCOM에서 조상의 이동 경로와 당시 역사적 맥락을 조사해 출처 기반 보고서와 내레이션 영상을 만드는 Claude Code 스킬 (MIT)</span>
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
            <h3 class="minor-detail-headline">가족 족보 문서 한 장을 역사 리서치·지도 애니메이션·음성 다큐멘터리로 바꾸는 에이전트 스킬</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python + Claude Code Plugin · GEDCOM/PDF 파싱 · 역사적 출처 교차 검증</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유명 프롬프트 오픈소스 제작자 <code>f</code>가 공개한 Claude Code 플러그인으로, 전자정부 가계도 PDF나 GEDCOM 족보 데이터를 입력하면 에이전트가 조상들이 살았던 시대·지역의 역사적 배경을 조사해 각주가 달린 보고서와 음성 내레이션 지도 영상까지 자동 생성합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[멀티모달 다큐 파이프라인]</strong> Genealogy PDF/GEDCOM &rarr; Historical Web Research &rarr; Cited Report + Animated Migration Map Video
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  코딩 에이전트 스킬 생태계가 단순 소프트웨어 개발을 넘어 인문학·개인 기록 아카이빙·영상 다큐 자동 제작으로 확장되는 대표 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/f/family-migration-story" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: es-ine/mcp -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 145개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.11 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;정부 공식 통계청 데이터를 AI 환각 없이 MCP로 직접 질의한다&quot; : INE MCP</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">es-ine/mcp — 스페인 통계청(INE) 공공 JSON API를 stdio 및 Streamable HTTP 기반 읽기 전용 MCP 도구로 노출하는 Python 서버 (EUPL-1.2)</span>
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
            <h3 class="minor-detail-headline">LLM의 구식 학습 데이터 대신 국가 통계청(INE) 실시간 공식 수치를 연결하는 EUPL-1.2 MCP 서버</h3>
            <div class="minor-detail-subheadline">EUPL-1.2 라이선스 · Python 3.11+ · stdio &amp; Streamable HTTP · 읽기 전용 공식 통계 API</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI에게 거시경제·인구·물가 지표를 물으면 학습 시점 이후의 수치를 지어내는 문제가 고질적이었습니다. 스페인 통계청(INE)의 공공 JSON API를 깔끔한 MCP 스키마로 감싼 이 서버는 공개 14시간 만에 ★145를 받으며 공공 데이터 MCP 표준화 흐름을 이끌고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[공공 통계 직결]</strong> AI Assistant &rarr; INE MCP (stdio / Streamable HTTP) &rarr; Spanish National Statistics Institute JSON API
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  유럽 공공 소프트웨어 라이선스(EUPL-1.2)와 최신 Streamable HTTP 트랜스포트를 채택해 정부·공공기관 데이터 개방의 새 기준을 제시합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/es-ine/mcp" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: sergiobanhos/generate-icons -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 77개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.41 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;우리 앱 디자인 토큰에 딱 맞춘 전용 SVG 아이콘 38종을 에이전트가 직접 그린다&quot; : generate-icons</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">sergiobanhos/generate-icons — 테마·폰트·기존 아이콘을 읽어 스타일 시트를 검증한 뒤 React·Vue·Svelte용 수제 SVG 아이콘 세트를 생성하는 스킬 (MIT)</span>
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
            <h3 class="minor-detail-headline">어색한 범용 아이콘 팩 대신 내 프로젝트의 선 두께·곡률·색상을 학습해 일관된 아이콘 라이브러리를 뽑아내는 스킬</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python · React/Vue/Svelte/RN/SVG 출력 · 다크모드 CSS 및 스프라이트 자동 생성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI로 UI를 짜다 보면 흔한 아이콘 라이브러리(Lucide/Heroicons)의 기성품 느낌에서 벗어나기 어렵거나, 에이전트가 SVG를 제멋대로 그려 선 굵기와 코너 반경이 제각각이 되기 일쑤입니다. <code>generate-icons</code>는 먼저 디자인 토큰으로 스타일 명세를 합의하고 샘플을 UI 옆에 띄워 승인받은 뒤에야 전체 아이콘 세트를 생성합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[디자인 시스템 동기화]</strong> Tokens &amp; Fonts Scan &rarr; Style Sheet &amp; Sample Proof &rarr; Validated SVG / Sprite / Framework Components
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  '샘플 선검증 후 일괄 생성'이라는 2단계 게이트를 스킬에 심어 AI 생성 디자인 에셋의 일관성 문제를 실용적으로 해결했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/sergiobanhos/generate-icons" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: musijava/JIDE -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 56개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.29 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;안드로이드 폰 안에서 Eclipse JDT·ECJ 컴파일·Git·AI 자동완성까지 돌린다&quot; : JIDE</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">musijava/JIDE — 일반 폴더 기반 워크스페이스로 기기 내 Java 편집·진단·JAR 패키징 및 DeepSeek FIM 인라인 보완을 지원하는 모바일 IDE (Apache-2.0)</span>
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
            <h3 class="minor-detail-headline">클라우드 컨테이너 없이 안드로이드 단말기 파일시스템 위에서 직접 Java를 빌드하는 온디바이스 IDE</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · Java · Eclipse JDT &amp; ECJ 내장 · Git · DeepSeek FIM 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  모바일에서 코딩하려면 원격 SSH나 유료 클라우드 IDE에 의존해야 했던 제약을 깨고, Eclipse JDT 시맨틱 자동완성과 ECJ 컴파일러 진단, 정의 이동, Git, 그리고 선택형 DeepSeek FIM 인라인 코드 추천까지 안드로이드 앱 하나에 꽉 눌러 담았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[온디바이스 Java 파이프라인]</strong> Android Workspace &rarr; Eclipse JDT + DeepSeek FIM &rarr; ECJ Compile &amp; Standard JAR Package
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  독자적 폐쇄 포맷이 아니라 표준 디렉터리와 JAR 의존성을 그대로 다루어 모바일과 PC 간 프로젝트 호환성을 완벽히 유지합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/musijava/JIDE" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: MasterKPG/rust-glass -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 108개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.14 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;애플의 Liquid Glass를 Vulkan·DX12·Metal GPU 셰이더와 즉시 모드 Rust API로 구현했다&quot; : rust-glass</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">MasterKPG/rust-glass — 배경을 굴절·색분산·블러 처리하고 물방울처럼 융합하는 40여 종 위젯과 AccessKit을 갖춘 GPU UI 프레임워크 (Apache-2.0)</span>
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
            <h3 class="minor-detail-headline">단일 패스 egui의 한계를 넘어 다중 백드롭 텍스처 체인으로 광학 굴절 유리를 그리는 Rust GUI 프레임워크</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · Rust 1.90+ · Vulkan/DX12/Metal · AccessKit 스크린 리더 · 0% 유휴 CPU</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플이 선보인 'Liquid Glass' UI는 유리 뒤의 배경과 다른 유리 요소까지 실시간으로 굴절·블러·색수차 처리해야 해 단일 패스 기반의 기존 Rust <code>egui</code> 구조로는 구현이 불가능했습니다. <code>rust-glass</code>는 다중 축소 블러 체인과 거리장(SDF) 베벨 셰이더를 도입해 유휴 시 CPU 점유율 0%의 크로스플랫폼 광학 유리 UI를 완성했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[다중 패스 광학 셰이더]</strong> Scene Texture &rarr; Downsampled Blur Chain &rarr; SDF Bevel Refraction (R/B Dispersion) &amp; Spring Fusion
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  슬라이더·탭·버튼이 물방울처럼 갈라졌다 합쳐지는 물리 스프링 모션과 접근성(AccessKit), 가상화 테이블까지 한 번에 제공해 Rust 데스크톱 GUI의 표현력을 한 단계 끌어올렸습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://crates.io/crates/rust-glass" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> Crates.io
              </a>
              <a href="https://github.com/MasterKPG/rust-glass" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: rit3zh/expandable-bottom-tabs -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 107개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.91 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;하단 탭 바가 매끄러운 유리 카드로 변신하는 React Native/Expo Liquid Glass 인터랙션&quot; : expandable-bottom-tabs</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">rit3zh/expandable-bottom-tabs — iOS 네이티브 모듈을 결합해 탭 바에서 워크스페이스·프로필 상태 메뉴로 자연스럽게 펼쳐지는 TypeScript UI (MIT)</span>
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
            <h3 class="minor-detail-headline">고정된 탭 바를 유동적인 컨텍스트 카드로 확장시키는 모바일 UI 마이크로 인터랙션 컴포넌트</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript · Expo / React Native iOS 네이티브 모듈 · Liquid Glass 모핑</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  모바일 앱에서 화면 전환 모달과 하단 내비게이션을 별개로 띄우는 대신, 하단 탭 바 자체가 워크스페이스 전환 카드나 프로필 상태 메뉴로 팽창하는 네이티브 급 모핑 애니메이션을 Expo 환경에서 바로 쓸 수 있게 오픈소스화해 프론트엔드 개발자들의 큰 호응을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[모핑 UI 상태 전환]</strong> Compact Bottom Tab Bar &rarr; Native Liquid Glass Morph &rarr; Expandable Workspace / Profile Card
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  React Native/Expo 생태계에서도 네이티브 브리지 최적화만으로 120Hz 급 촉각 인터랙션 구현이 가능함을 입증합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/rit3zh/expandable-bottom-tabs" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: Dimi-Sama/OrbitalsPCRecomp -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 81개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.93 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Switch 2 게임을 에뮬레이션 없이 C 코드로 정적 재컴파일해 Steam Deck 네이티브로 돌린다&quot; : Liftoff (OrbitalsPCRecomp)</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Dimi-Sama/OrbitalsPCRecomp — MZ Labs SwitchRecomp 기반으로 23,134개 셰이더를 사전 번역해 Windows·Linux·Steam Deck Vulkan 네이티브 포트로 변환 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">합법 소장 게임 덤프의 ARM64 기계어와 23,134개 셰이더를 PC용 C/Vulkan 바이너리로 직조하는 정적 재컴파일러</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · C · v0.1.5 · Linux AppImage &amp; Steam Deck OLED 60fps 지원 · 게임 파일 0바이트</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  동적 에뮬레이션의 CPU/셰이더 스터터링 한계를 넘어, ARM64 콘솔 실행 코드를 PC용 C 코드로 한 번에 재컴파일(20~60분)하고 23,134개 셰이더를 첫 실행 전에 사전 컴파일해 Steam Deck OLED에서도 매끄러운 60fps 분할 화면 협동 플레이를 구현했습니다. (참고: <code>reshaped/sonic-adventure-2</code>의 드림캐스트 100% 바이트 일치 디컴파일 등 정적 재컴파일·보존 흐름이 동반 상승 중입니다.)
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[클린룸 정적 재컴파일]</strong> User-Supplied exefs/romfs &rarr; ARM64-to-C Lifter + 23,134 Shader Pre-Compile &rarr; Native Vulkan 1.3 PC Binary
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  저장소에 게임 코드·키·에셋을 단 1바이트도 싣지 않고 사용자 기기에서 변환을 수행하는 '정적 재컴파일 포트' 표준이 최신 콘솔 세대까지 빠르게 확산되고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Dimi-Sama/OrbitalsPCRecomp" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Tracking Diseases Cured by AI -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 290점 (176댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 52.82 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;ChatGPT 출시 1,452일, AI 신약 시장 69.3억 달러 — 그러나 AI가 완치한 질병은 아직 0건&quot; : Tracking Diseases Cured by AI</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">diseasescuredbyai.com — FDA/EMA 정식 승인 기준 AI 발굴 신약·완치 질병 수를 냉정하게 기록하는 공개 원장</span>
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
            <h3 class="minor-detail-headline">과장된 AI 신약 마케팅 대신 실제 FDA·EMA 규제 승인 통과 건수만 추적하는 '0의 카운터'</h3>
            <div class="minor-detail-subheadline">HN 290점 · 176댓글 · 임상 진입 117건 중 3상 도달 1건(Rentosertib) · 최종 승인 0건</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI가 인류 질병을 곧 정복할 것이라는 화려한 발표가 쏟아지는 와중에, 실제 FDA와 유럽의약품청(EMA) 승인 기록을 대조해 'AI가 발견한 치료제로 완치된 질병 수: 0'을 담담하게 기록하는 웹 대시보드가 5시간 만에 HN 290점을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[임상 현실 원장]</strong> 63 Companies &middot; 117 Candidates in Human Trials &rarr; 1 in Phase III (Rentosertib) &rarr; 0 FDA/EMA Approved Cures
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  댓글에서는 "단순 조롱 사이트가 아니라 진지한 임상 파이프라인 추적기"라는 호평과 함께, 바이오 분야의 진짜 병목은 디지털 추론이 아니라 실제 습식 실험실과 수년짜리 인체 임상 검증 속도라는 냉정한 합의가 이어졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://diseasescuredbyai.com/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 사이트 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50657307" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (176)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: YouTube Ad Punisher -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 192점 (271댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 37.24 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유튜브 광고가 뜨면 차단기 대신 페이지를 2번 새로고침해 재생 위치를 유지한 채 광고를 날린다&quot; : YouTube Ad Punisher</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">antonpictures/youtube-punisher — 안티 애드블록 탐지를 우회하기 위해 재생 위치를 기억했다가 자동 리로드하는 MV3 크롬 확장 (MIT)</span>
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
            <h3 class="minor-detail-headline">광고 차단기를 막는 유튜브의 탐지망을 '단순 페이지 리로드'라는 무식하지만 치명적인 전략으로 돌파한 오픈소스 확장</h3>
            <div class="minor-detail-subheadline">HN 192점 · 271댓글 · MIT 라이선스 · Chrome Manifest V3 · 재생 타임스탬프 자동 복원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유튜브가 60초마다 광고를 들이밀고 기존 애드블로커를 탐지해 경고를 띄우자, 광고 스크립트를 가로채는 대신 광고 DOM이 뜨는 순간 타임스탬프를 저장하고 탭을 새로고침해 버리는 기발한 Manifest V3 확장이 271개 댓글의 격론을 불러일으켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[리로드 우회 루프]</strong> Ad Overlay Detected &rarr; Save Current Timestamp &rarr; Auto-Reload Tab (×2) &rarr; Resume Video Instantly
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  댓글에서는 Firefox + uBlock Origin + SponsorBlock 조합을 추천하는 목소리와 더불어 "광고주가 뜰 때마다 PeerTube·yt-dlp에 자동 기부하는 진짜 징벌 확장을 만들자"는 유쾌한 반광고 아이디어들이 쏟아졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/antonpictures/youtube-punisher" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://news.ycombinator.com/item?id=50657530" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (271)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: 45°C inlets just killed the chiller -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 240점 (123댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.77 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;45°C 온수 냉각이 데이터센터의 거대 냉동기(Chiller)를 퇴출시키고 있다&quot; : 45°C Inlets Killed the Chiller</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">The Register HPC — 차세대 AI GPU가 45°C 입수 온도를 견디기 시작하면서 전력 먹는 냉동기 없이 건식 열교환만으로 AI 팹을 식히는 열역학 혁신</span>
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
            <h3 class="minor-detail-headline">대기 온도보다 뜨거운 45°C 액체 냉각으로 기계식 냉동기를 제거하고 AI 데이터센터 PUE를 극한으로 낮추는 물리적 전환</h3>
            <div class="minor-detail-subheadline">HN 240점 · 123댓글 · The Register HPC 리포트 · 45°C 온수 수냉 &amp; 칠러리스(Chillerless) 냉각</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI GPU 랙의 열밀도가 100kW를 넘기며 공랭이 한계에 부딪힌 가운데, 차세대 가속기 아키텍처들이 45°C의 뜨거운 냉각수 입력을 공식 허용하기 시작했습니다. 외기 온도가 40°C에 육박하는 여름철에도 거대한 압축기 냉동기 없이 외부 공기로 직접 열을 버릴 수 있게 된 것입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[칠러리스 수냉 루프]</strong> 45°C Liquid Direct-to-Chip &rarr; Dry Cooler Heat Rejection (No Mechanical Chiller) &rarr; Massive CapEx/Power Savings
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  AI 데이터센터 확장의 최대 병목인 전력망과 물 소비 문제를 소프트웨어 최적화가 아닌 열역학(입수 온도 상향)으로 정면 돌파하는 인프라 지각변동입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://news.ycombinator.com/item?id=50655278" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (123)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Nextcloud Office Desktop app -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 386점 (197댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 35.34 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유럽 디지털 주권과 MS Office 탈출을 겨냥한 데스크톱 오피스&quot; : Nextcloud Office Desktop App</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nextcloud.com — Euro-Office 컨소시엄 엔진을 탑재해 로컬·Nextcloud 문서를 통합 편집하는 신규 오픈소스 데스크톱 오피스 출시 (197댓글 격론)</span>
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
            <h3 class="minor-detail-headline">브라우저 전용이던 Nextcloud Office를 로컬 PC 네이티브 데스크톱으로 확장한 'Euro-Office' 합작품</h3>
            <div class="minor-detail-subheadline">HN 386점 · 197댓글 · Nextcloud + Euro-Office · 클라우드·오프라인 통합 문서 편집</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유럽 공공기관과 기업들의 미국 빅테크 클라우드(M365·Google Docs) 탈피 요구가 거세지는 가운데, Nextcloud가 Euro-Office 기반 데스크톱 오피스 앱을 전격 발표하며 HN 386점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[유럽 소버린 오피스]</strong> Nextcloud Hub / Local Files &rarr; Euro-Office Desktop Engine &rarr; Real-Time Co-Editing without Big Tech Cloud
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  HN 댓글에서는 환영 목소리 못지않게 ONLYOFFICE 포크 논란과 LibreOffice·Collabora와의 완성도 비교 등 오픈소스 오피스 진영의 복잡한 역학 관계가 치열하게 검증됐습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 발표 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50654289" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (197)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Intel One Mono font -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 437점 (234댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 34.72 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;저시력·시각 피로 개발자를 위해 인텔이 만든 오픈소스 코딩 폰트 재발굴&quot; : Intel One Mono</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">intel/intel-one-mono — 프론티어 코딩 시대에도 여전히 개발자 생산성의 1순위는 눈의 피로를 줄이는 명쾌한 고정폭 타이포그래피 (SIL OFL)</span>
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
            <h3 class="minor-detail-headline">저시력 개발자들의 피드백을 반영해 유사 문자(0/O, 1/l/I) 변별력과 가독성을 극대화한 인텔의 오픈소스 서체</h3>
            <div class="minor-detail-subheadline">HN 437점 · 234댓글 · SIL Open Font License · Light/Regular/Medium/Bold + Italic · Ligatures</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 코딩 에이전트가 쏟아내는 방대한 diff와 터미널 로그를 하루 종일 검수해야 하는 개발자들에게 서체 피로도가 핵심 이슈로 떠오르며, 인텔이 저시력 엔지니어 패널과 함께 설계한 <code>Intel One Mono</code>가 다시 HN 437점·234댓글의 열띤 호응을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[접근성 타이포그래피]</strong> Low-Vision Developer Panel &rarr; Elevated x-height &amp; Distinct 1/l/I, 0/O &rarr; High-Clarity IDE &amp; Terminal Font
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  JetBrains Mono, Iosevka, Berkeley Mono, Maple Mono 등 개발자 커뮤니티 최고의 서체 비교 토론이 펼쳐지며 '읽기 좋은 코드 환경'의 본질을 환기했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/intel/intel-one-mono" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://news.ycombinator.com/item?id=50653667" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (234)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: OpenAI cuts GPT-6.2 usage (Clustered with OpenAI cost control mode) -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 455점 (259댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.76 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;OpenAI, GPT-6.2 Astra 한도 40%·Sol 한도 25% 전격 축소 — 비용 통제 모드 돌입&quot; : OpenAI Quota Cuts</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">thsottiaux &amp; micjm.com(198점 통합) — 수학 난제 돌파 발표 직후 터진 추론 컴퓨트 한도 대폭 삭감과 클라우드 AI 비용 한계 논쟁</span>
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
            <h3 class="minor-detail-headline">프론티어 추론 모델의 막대한 연산 비용이 촉발한 쿼터 축소 쇼크 (파생 클러스터 2건 통합)</h3>
            <div class="minor-detail-subheadline">HN 455점(259댓글) + 파생 에세이 OpenAI may be in cost control mode(198점·180댓글) 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  OpenAI가 GPT-6.2 라인업의 코딩·추론 모델인 <code>Astra</code>의 사용량 한도를 40% 더 빠르게 소진되도록 조정하고 <code>Sol</code> 역시 25% 축소하자, 같은 날 올라온 <em>"OpenAI may be in cost control mode"</em>(198점) 분석과 맞물려 총 650점 이상·439댓글 규모의 대토론이 벌어졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[추론 경제학 압박]</strong> Heavy Test-Time Compute (Astra / Sol) &rarr; GPU Unit Economics Strain &rarr; 25~40% Faster Rate-Limit Throttle
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  고정 월 구독료 안에서 무제한 테스트-타임 추론을 돌리던 에이전트 사용자들이 레이트 리밋 벽에 부딪히면서, 로컬 오픈웨이트 추론과 하이브리드 모델 라우팅의 필요성이 더욱 커지고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://micjm.com/blog/openai-is-in-cost-control-mode/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 비용 분석 에세이
              </a>
              <a href="https://news.ycombinator.com/item?id=50651117" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (259)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: NYT warns photographers not to update Photoshop over AI features -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 645점 (514댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.33 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;뉴욕타임스, 포토저널리즘 신뢰 지키려 사진기자들에게 포토샵 업데이트 금지령&quot; : NYT vs Adobe AI</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">The Verge — Photoshop 신규 AI 자동 보정·생성 기능 도입이 보도사진 윤리 기준과 충돌하자 NYT가 구버전 유지를 긴급 지시</span>
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
            <h3 class="minor-detail-headline">픽셀의 진실성이 생명인 보도사진 현장에서 빅테크 소프트웨어의 '기본 탑재 AI 기능'을 거부한 첫 대형 언론사 사례</h3>
            <div class="minor-detail-subheadline">HN 645점 · 514댓글 · The Verge 보도 · 보도사진 C2PA/진본성 윤리 충돌</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  어도비가 Photoshop의 기본 작업 흐름 깊숙이 AI 픽셀 재합성 기능을 밀어 넣자, 뉴욕타임스 편집국이 보도사진의 사실성 훼손 및 오작동 위험을 이유로 사진기자들에게 소프트웨어 업데이트를 보류하라고 공지하며 514개 댓글의 거센 논쟁을 불렀습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[저널리즘 vs 강제 AI]</strong> Adobe Photoshop AI Default Pipeline &rarr; Risk of Altered Photojournalism Pixels &rarr; NYT Version Freeze Directive
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  강제 AI 기능이 오히려 전문 산업군의 '버전 동결'과 오픈소스 비파괴 RAW 현상 도구(Darktable 등) 재평가를 유발하는 역설을 드러냅니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://news.ycombinator.com/item?id=50647673" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (514)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Collection of preserved UI style guides -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 395점 (93댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.87 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;1980년대부터 오늘날까지 79개 전설적 UI 스타일 가이드 원본 아카이브&quot; : Preserved UI Style Guides</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">aresluna.org — <em>Shift Happens</em> 저자 마르친 비하리가 수집·분류한 Apple·NeXT·IBM·BeOS 인터페이스 규범서 디지털 박물관</span>
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
            <h3 class="minor-detail-headline">웹에 흩어져 사라져가던 45년 치 그래픽 인터페이스 설계 철학 PDF 79권을 한곳에 엮은 보존관</h3>
            <div class="minor-detail-subheadline">HN 395점 · 93댓글 · 79 Style Guides · 1980년대~2026년 · 시대별·테마별 큐레이션</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI가 천편일률적인 웹 UI를 찍어내는 시대에, 1980년대 초 데스크톱 GUI 탄생기부터 현대에 이르기까지 주요 컴퓨터 기업들이 픽셀 하나·버튼 간격 하나의 근거를 치열하게 기록한 79종의 휴먼 인터페이스 가이드라인(HIG) 원본 PDF를 한데 모은 아카이브가 큰 울림을 주었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[인터페이스 역사 보존]</strong> Scattered 1980s~2020s HIG PDFs &rarr; Era &amp; Theme Curation (79 Guides) &rarr; Open Design Reference Library
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  현대 디자인 시스템과 에이전트 UI 스킬(<code>impeccable</code> 등)이 기댈 수 있는 검증된 고전 인터페이스 문법의 보고로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://aresluna.org/ui-style-guides/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 아카이브 열기
              </a>
              <a href="https://news.ycombinator.com/item?id=50649834" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (93)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Jev is probably Qwen3.5-35B-A3B -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 337점 (94댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.15 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;지연시간(Latency)은 거짓말하지 않는다 — 미공개 모델 'Jev'의 실체는 Qwen3.5-35B-A3B&quot; : Latency Doesn't Lie</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">modaic.dev — 스텔스 API 엔드포인트의 토큰 간 지연시간·프리필 곡선 지문만으로 배후의 오픈웨이트 MoE 아키텍처를 역추적한 분석</span>
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
            <h3 class="minor-detail-headline">블랙박스 AI API의 가중치 크기와 MoE 활성 파라미터 수를 네트워크 타이밍 프로파일로 감식한 기술 리포트</h3>
            <div class="minor-detail-subheadline">HN 337점 · 94댓글 · Modaic 엔지니어링 블로그 · 스텔스 모델 타이밍 핑거프린팅</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 리더보드나 API 플랫폼에 정체를 숨긴 채 올라오는 스텔스 모델 'Jev'가 독자 프론티어 모델인지 기존 오픈웨이트 모델의 래핑인지 확인하기 위해, 출력 품질이 아닌 하드웨어 추론 지연시간(TTFT 및 TPOT) 곡선을 정밀 계측해 <code>Qwen3.5-35B-A3B</code> 지문을 찾아낸 분석이 큰 화제를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[타이밍 모델 감식]</strong> Stealth API Endpoint &rarr; Prefill / Inter-Token Latency Fingerprinting &rarr; Active Parameter Signature (35B-A3B MoE)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  단순 응답 텍스트뿐 아니라 물리적 연산 지연시간 자체가 모델 아키텍처를 노출하는 사이드채널이 될 수 있음을 보여주며 API 투명성 검증 기법으로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://modaic.dev/blog/latency-doesnt-lie" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 분석 읽기
              </a>
              <a href="https://news.ycombinator.com/item?id=50648823" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (94)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
