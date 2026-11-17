# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-18

FULL_MINORS_SECTION = """
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
          직전 발행(11월 17일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 대규모 복제 봇넷 스팸 저장소·중복 이력 배제 및 재귀적 동일 주제 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: SecFathy/otpkit -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 41개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.09 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;API 키 없이 에이전트에게 일회용 이메일·SMS와 OTP 자동 추출을 부여하는 MCP 서버&quot; : otpkit</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SecFathy/otpkit — 가입 테스트·E2E 검증 중 에이전트가 임시 수신함을 만들고 인증 코드·링크를 즉시 파싱하는 MIT MCP 도구</span>
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
            <h3 class="minor-detail-headline">별도 유료 인증 키 없이 에이전트 E2E 가입·OTP 테스트를 자동화하는 경량 MCP 브리지</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python 기반 · 제로 API 키 임시 이메일·SMS 프로바이더 멀티 어댑터</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  브라우저 제어 에이전트나 QA 자동화 에이전트가 웹 서비스 회원가입이나 비밀번호 재설정을 테스트할 때마다, 이메일 OTP나 SMS 인증 번호 입력 단계에서 멈춰 사람이 개입해야 하는 불편이 컸습니다. <code>otpkit</code>은 외부 유료 API 키 없이도 동작하는 임시 수신함 생성·파싱 MCP 도구를 공개해 단숨에 41스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[OTP 루프]</strong> Agent Request &rarr; Provision Disposable Email/SMS &rarr; Poll Inbox &rarr; Regex Extract OTP / Verification Link
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개인 이메일 노출 없이 샌드박스 환경에서 에이전트 기반 가입·인증 회귀 테스트를 완결할 수 있는 실용적 MCP 컴포넌트로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SecFathy/otpkit" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: Kede0111/qlick-lab -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 8개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.30 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;디지털 RAW 사진을 아날로그 필름 암실처럼 현상하는 macOS 오픈소스 암실&quot; : Qlick Lab</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Kede0111/qlick-lab — Swift와 Rust 코어로 Leica DNG 등 RAW 파일을 Kodak Portra 400 필름 감성으로 현상하는 GPL-3.0 macOS 앱</span>
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
            <h3 class="minor-detail-headline">구독형 Lightroom을 벗어나 물리적 필름 롤 워크플로우를 재현한 네이티브 macOS 현상 도구</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · Swift UI + Rust 이미지 파이프라인 · 필름 롤·스톡 에뮬레이션</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  구독 모델에 지친 사진가들과 macOS 네이티브 앱 팬들 사이에서, 복잡한 AI 보정 대신 '필름 롤' 단위로 컷을 선별하고 Kodak Portra 400 같은 필름 감성을 정갈하게 입히는 오픈소스 데스크톱 앱이 공개되며 초기 관심을 끌었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[현상 파이프라인]</strong> DNG / RAW Import &rarr; Rust Color &amp; Film Curve Engine &rarr; Native macOS Swift Preview &amp; Export
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  SwiftUI 네이티브 인터페이스와 Rust 연산 엔진을 결합한 데스크톱 크리에이티브 툴의 깔끔한 아키텍처 사례를 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Kede0111/qlick-lab" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: Lelpoco2/learning-curve -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 1개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 0.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.12 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;SymPy 수식 검증과 간격 반복 학습을 내장한 Claude Code·pi용 STEM 튜터 플러그인&quot; : Learning Curve</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Lelpoco2/learning-curve — 학생의 이해도를 진단해 난이도별 학습 계획을 짜고, 모든 수식을 SymPy로 검산하며 오답 노트를 재시험하는 MIT 플러그인</span>
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
            <h3 class="minor-detail-headline">LLM의 수학 환각을 SymPy 심볼릭 엔진으로 원천 차단하는 구조화된 이공계 튜터링 하네스</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript + MCP · 직관 우선(Why→When→What) 교수법 &amp; Spaced Repetition</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI에게 수학·물리·공학 개념을 물으면 답을 곧바로 던져주거나 계산 실수를 범해 학습 효과가 떨어지기 쉽습니다. 공개 1시간 만에 레이더에 포착된 <code>learning-curve</code>는 코딩 에이전트를 '정답 자판기'가 아니라 논리 근거를 되묻고 SymPy로 검산하는 엄격한 STEM 과외 교사로 탈바꿈시킵니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[학습 루프]</strong> Diagnostic Assessment &rarr; Intuition First Lesson &rarr; SymPy Verification &rarr; Reasoning Quiz &amp; Spaced Retest
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  코딩 에이전트 플러그인 아키텍처(<code>.claude-plugin</code> + <code>.mcp.json</code>)가 소프트웨어 개발을 넘어 정밀한 교육·수리 추론 워크플로우로 확장되는 신호탄입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Lelpoco2/learning-curve" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: prusa3d/prusa-connect -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 118개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.51 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클라우드 없이 내 로컬 망에서 3D 프린터를 직접 관제한다&quot; : Prusa Connect 로컬 서버</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">prusa3d/prusa-connect — 프루사 리서치가 공식 공개한 Go 언어 기반 자가 호스팅 3D 프린터 원격 관리·REST 제어 서버</span>
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
            <h3 class="minor-detail-headline">제조사 클라우드 종속 논란 속에서 프루사가 직접 풀어낸 로컬 3D 프린터 팜 서버</h3>
            <div class="minor-detail-subheadline">Go 언어 · Docker Compose 지원 · &quot;하드웨어는 당신이, REST 서버는 우리가&quot;</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  3D 프린터 업계에서 외부 클라우드 연결 강제와 폐쇄형 펌웨어 정책을 둘러싼 반발이 거센 가운데, Prusa3D가 자사 프린터 관제 플랫폼인 <code>Prusa Connect</code>의 로컬 서버 버전을 Go 기반 오픈 저장소로 전격 공개하며 118스타를 빠르게 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 관제]</strong> 3D Printer Fleet (LAN) &rarr; Prusa Connect Go Server &rarr; Local Web Dashboard &amp; REST API
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  보안이 엄격한 사내 R&amp;D 랩이나 인터넷이 차단된 작업실에서도 외부 클라우드 의존 없이 다수의 3D 프린터를 통합 모니터링·제어할 수 있게 됐습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/prusa3d/prusa-connect" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: SamG-Coder/SmartImposter -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 61개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.91 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;44만 그루의 숲을 Rust + Vulkan RTX 레이 트레이싱으로 실시간 렌더링한다&quot; : SmartImposter</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SamG-Coder/SmartImposter — 원거리 식생을 시차 팔면체 임포스터(Octahedral Impostor)로 치환하고 DLSS Ray Reconstruction으로 복원하는 MIT 렌더러</span>
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
            <h3 class="minor-detail-headline">픽셀당 단 1개의 노이지 레이 샘플과 팔면체 임포스터로 구현한 초고밀도 자연 렌더링</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust + Vulkan · 14종 440,899개 식생 오브젝트 실시간 광선 추적</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수십만 개의 나뭇잎과 풀을 실시간 하드웨어 레이 트레이싱으로 그리는 일은 BVH 메모리와 교차 연산 비용 때문에 상용 게임 엔진에서도 난제로 꼽힙니다. Rust와 Vulkan으로 밑바닥부터 짠 <code>SmartImposter</code>가 놀라운 데모와 함께 공개되며 그래픽스 엔지니어들의 시선을 사로잡았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[렌더 파이프라인]</strong> Near Mesh + Far Parallax Octahedral Impostors &rarr; 1 spp RTX Ray Tracing &rarr; NVIDIA DLSS Ray Reconstruction
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  교목 10만여 그루와 관목·고사리·잔디까지 총 440,899개 식물을 RTX 코어와 AI 디노이징 결합만으로 1440p 실시간 프레임으로 끌어올린 차세대 LOD 기법의 실증 레퍼런스입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SamG-Coder/SmartImposter" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: phasyn/phasyn-studio -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 45개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.44 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;내 GPU에서 사운드가 결합된 단편 AI 영화를 직접 제작하는 셀프호스팅 스튜디오&quot; : Phasyn Studio</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">phasyn/phasyn-studio — 클라우드 크레딧 결제 없이 로컬 GPU로 샷 단위 AI 영상과 오디오를 생성·편집하는 Apache-2.0 워크스페이스</span>
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
            <h3 class="minor-detail-headline">비싼 구독형 AI 비디오 클라우드를 대체하는 샷(Shot) 중심 로컬 AI 영상 제작 도구</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · TypeScript + Python · 코딩 에이전트 원클릭 설치 가이드 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  생성형 비디오 모델이 빠르게 오픈웨이트화되고 있지만, 정작 이를 영화 제작처럼 컷(Shot)과 오디오 단위로 엮어 쓸 수 있는 로컬 스튜디오 UI는 부족했습니다. <code>Phasyn Studio</code>는 로컬 GPU에서 영상과 사운드를 함께 생성하는 워크스페이스를 Apache-2.0으로 공개해 주목받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 스튜디오]</strong> Shot Workspace UI &rarr; Local GPU Video + Audio Generation &rarr; Multi-Shot Sequence Assembly
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  README 상단에 Claude Code나 Codex에 넘기면 즉시 설치를 끝내는 <code>docs/agent-install.md</code>를 배치해, 복잡한 로컬 AI 모델 환경 구성을 에이전트에게 위임하는 최신 배포 문화를 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/phasyn/phasyn-studio" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: krisgfx9/Wireless-Device-Battery-Monitor -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 2,545개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 93.21 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;무거운 제조사 블로트웨어 없이 작업표시줄에 무선 마우스·헤드셋 배터리를 띄운다&quot; : Wireless Battery</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">krisgfx9/Wireless-Device-Battery-Monitor — Windows 10/11·Linux 멀티 모니터 작업표시줄에 무선 주변기기 잔량을 표시하는 C++ 오픈소스 위젯</span>
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
            <h3 class="minor-detail-headline">제조사 전용 유틸리티의 백그라운드 점유를 대체하며 하루 만에 2,545스타를 폭주한 데스크톱 유틸리티</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · C++ 네이티브 · Windows &amp; Linux 지원 · 멀티 모니터 작업표시줄 위치 선택</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  무선 마우스, 키보드, 헤드셋, 게임패드를 각각 다른 브랜드로 쓰면 3~4개의 무거운 제조사 동반 앱을 상시 실행해야 배터리를 확인할 수 있습니다. 순수 C++로 가볍게 만든 이 오픈소스 위젯은 바로 그 실생활 불편을 정조준해 시간당 93스타 이상을 끌어모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[하드웨어 폴링]</strong> HID / Bluetooth Battery Telemetry &rarr; Lightweight C++ Daemon &rarr; Native Taskbar Widget
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  공개 하루 만에 리눅스 빌드 스크립트와 멀티 모니터 작업표시줄 선택 기능까지 커뮤니티 기여가 쏟아지며 강력한 데스크톱 유틸리티 수요를 증명했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/krisgfx9/Wireless-Device-Battery-Monitor" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: sybil-solutions/inference-optimisation-skill -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 894개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 31.80 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;로컬 LLM 추론 속도를 과학적 대조 실험으로 한계까지 튜닝하는 에이전트 스킬&quot; : inference-optimisation</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">sybil-solutions/inference-optimisation-skill — 이론적 상한선 계산부터 1변수 변경·장문 회수율 게이트까지 자동화한 MIT LLM 서빙 최적화 스킬</span>
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
            <h3 class="minor-detail-headline">단순 플래그 모음이 아니라 '이론 상한선→통제 대조군→장문 안정성 검증'을 수행하는 엔지니어링 워크플로우</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python · Decode · Speculative Decoding · Prefill · KV Cache · TTFT 전방위 최적화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  로컬 LLM 서버(vLLM, llama.cpp 등)를 띄울 때 인터넷에 떠도는 플래그를 무작정 복사하면 속도는 조금 빨라져도 장문 컨텍스트 정확도가 무너지곤 합니다. 실제 성능 향상 비법을 6단계 과학적 힐클라이밍 프로토콜로 빚어낸 이 스킬은 하루 만에 894스타를 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[튜닝 프로토콜]</strong> Theoretical Ceiling &rarr; One-Variable Change + Interleaved Control &rarr; Full-Context Retrieval Gate &rarr; Pinned Build
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  실패한 실험 결과까지 모두 로깅하고 메모리 상한선과 장문 검색 무결성을 통과한 설정만 채택하도록 에이전트를 규율하는 모범적 연구 스킬입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/sybil-solutions/inference-optimisation-skill" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: fedesanchez0/shader-lab -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 153개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.63 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;iPhone·iPad·Apple Vision Pro·Apple Watch에서 실시간 Metal 셰이더를 만지는 플레이그라운드&quot; : Shader Lab</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">fedesanchez0/shader-lab — 애플 전 플랫폼에서 실시간 파라미터 슬라이더로 GPU 셰이더 효과를 실험하는 MIT 오픈소스 Swift 앱</span>
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
            <h3 class="minor-detail-headline">Claude Code와 협업해 완성도를 끌어올린 애플 생태계 통합 실시간 Metal 셰이더 실험실</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Swift + Metal · iOS · iPadOS · tvOS · watchOS · visionOS 전방위 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플 실리콘의 GPU 성능을 극한으로 끌어쓰는 Metal 셰이더 프로그래밍은 초기 실험 환경 구축이 번거로운 편입니다. <code>Shader Lab</code>은 빗방울(Rain) 등 시각 효과를 실시간 파라미터 패널과 함께 아이폰부터 비전 프로·애플 워치까지 아우르는 깔끔한 Xcode 프로젝트로 공개해 153스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[Metal 파이프라인]</strong> Live Parameter Controls &rarr; Apple Metal Fragment / Compute Shaders &rarr; iOS / iPadOS / visionOS / watchOS Output
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  모바일·공간 컴퓨팅 그래픽스 개발자들이 GPU 셰이더 파라미터 인터랙션을 즉시 학습하고 프로토타이핑할 수 있는 실전 교과서 역할을 합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/fedesanchez0/shader-lab" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: GPT-6.2 Astra and Sol -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 961 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 192.15 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;OpenAI, 차세대 플래그십 라인업 'GPT-6.2 Astra &amp; Sol' 전격 공개 — 5시간 만에 961점 폭발&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">openai.com — 앤스로픽(Anthropic) IPO 당일을 겨냥한 듯한 전격 발표로 601개 댓글과 트래픽 폭주를 일으킨 OpenAI 신모델</span>
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
            <h3 class="minor-detail-headline">시간당 192보트를 기록하며 오늘 HN 전체 화제성 1위를 장악한 OpenAI의 기습 공세</h3>
            <div class="minor-detail-subheadline">601개 댓글 · Astra &amp; Sol 듀얼 모델 발표 · 경쟁사 대형 이벤트를 정조준한 타이밍 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  OpenAI가 <code>GPT-6.2 Astra</code>와 <code>Sol</code>을 공식 발표하자마자 해커뉴스에 등록된 지 5시간 만에 961점과 601개의 댓글이 쏟아지며 OpenAI 공식 웹페이지까지 간헐적 지연을 겪을 정도로 폭발적인 트래픽이 몰렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[모델 발표]</strong> OpenAI GPT-6.2 (Astra &amp; Sol) &rarr; HN 192.15 pts/h Surge &rarr; Real-World Coding &amp; Benchmark Verification
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자들은 발표 타이밍에 얽힌 업계 경쟁 구도를 흥미롭게 지켜보는 한편, 마케팅 수사를 걷어내고 실제 코딩·에이전트 실무 벤치마크에서 어떤 체감 격차를 보여주는지 즉시 검증에 돌입했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> OpenAI 공식 발표
              </a>
              <a href="https://news.ycombinator.com/item?id=50535230" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (961 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Java4Shell: RCE in OpenJDK when processing Base64 -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 218 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 137.20 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;OpenJDK Base64 디코딩 처리 중 원격 코드 실행(RCE) 치명적 취약점 'Java4Shell' 경보&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">calif.io — OpenJDK의 AVX-512 Base64 디코딩 경로와 맞물려 전 세계 자바 백엔드에 비상 점검을 부른 제로데이급 보안 이슈</span>
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
            <h3 class="minor-detail-headline">1.6시간 만에 218점을 돌파하며 자바 운영 환경 전체를 긴장시킨 Base64 RCE 분석</h3>
            <div class="minor-detail-subheadline">68개 댓글 · OpenJDK Base64 AVX-512 인트린직 경로 지목 · 긴급 JVM 플래그 우회책 및 커밋 추적</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  웹 API 인증 헤더와 페이로드 전반에 쓰이는 가장 기본적인 Base64 디코딩 과정에서 OpenJDK 원격 코드 실행(RCE)이 가능하다는 'Java4Shell' 보고서가 공개되자, 수많은 프로덕션 자바 팀들이 즉각 영향 범위 파악에 나서며 시간당 137보트 이상으로 급상승했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[취약점 경로]</strong> Crafted Base64 Payload &rarr; OpenJDK AVX-512 Intrinsic Decoder &rarr; Memory Corruption / RCE Vector
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  HN 보안 커뮤니티는 관련 OpenJDK 패치 커밋(<code>5177a70b</code>)과 AVX-512 벡터 가속 비활성화 플래그를 통한 임시 완화 방안을 신속히 공유하며 패치 검증에 착수했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://calif.io/java4shell/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Calif 보안 리포트
              </a>
              <a href="https://news.ycombinator.com/item?id=50538240" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (218 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Apple Services Down -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 570 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 114.16 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;애플 서비스 대규모 동시 장애: Apple Store 결제·반품과 신형 iPhone 개통까지 올스톱&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">developer.apple.com — 오프라인 애플 스토어 POS 결제부터 기기 활성화 서버까지 연쇄 마비되며 570점·312댓글 집중</span>
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
            <h3 class="minor-detail-headline">단일 거대 플랫폼 인증·활성화 코어가 멈출 때 벌어지는 온·오프라인 동시 마비</h3>
            <div class="minor-detail-subheadline">312개 댓글 · 애플 공식 시스템 상태 페이지 적색 경보 확산 · 현장 매장 POS 중단 증언 잇따라</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플 공식 시스템 상태 대시보드에 다수의 서비스 장애가 동시 표시되면서, 실제 애플 스토어 현장에서도 주문·반품 처리와 새 아이폰 개통(Activation)이 전면 중단되었다는 경험담이 이어져 5시간 만에 570점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[장애 파급]</strong> Apple Core Auth / Activation Outage &rarr; Store POS &amp; Return Freeze &rarr; New iPhone Activation Failure
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  자체 데이터센터 비중이 높은 애플에서도 중앙 인증·기기 활성화 계층의 단일 장애가 전 세계 리테일 매장 운영까지 즉각 마비시키는 구조를 다시금 드러냈습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://developer.apple.com/system-status/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Apple 시스템 상태
              </a>
              <a href="https://news.ycombinator.com/item?id=50535238" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (570 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: New Evidence Shows School Phone Bans Are Gradually Improving Test Scores -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 1,104 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 100.22 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;학교 내 스마트폰 금지 정책이 실제로 학생들의 시험 성적을 끌어올리고 있다는 새로운 실증 연구&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nytimes.com — 금지 정책 도입 이후 학업 성취도의 점진적 개선을 포착한 NYT 데이터 분석에 1,104점·544댓글 격론</span>
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
            <h3 class="minor-detail-headline">어텐션 이코노미와 교육 환경의 충돌: 스마트폰 차단 이후 교실 지표의 변화</h3>
            <div class="minor-detail-subheadline">544개 댓글 · 교실 내 집중력 회복 vs 학교 지급 노트북·태블릿 산만함 변수 동시 제기</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  미국 등 주요 학군에서 시행된 교내 스마트폰 금지 조치 이후 성적 추이를 추적한 최신 실증 연구가 뉴욕타임스 Upshot을 통해 보도되자, 기술 종사자들 스스로도 "모바일 알림과 숏폼의 집중력 파괴 효과"에 깊이 공감하며 1,104점을 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[실증 추이]</strong> Classroom Phone Ban Policy &rarr; Reduced Notification Fragmentation &rarr; Gradual Test Score Recovery
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  다만 교실 내 학교 지급 크롬북·노트북 역시 또 다른 주의 분산 통로로 작용한다는 반론도 544개 댓글 속에서 활발히 논의되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> NYT 연구 보도
              </a>
              <a href="https://news.ycombinator.com/item?id=50530163" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (1,104 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: How the Claude Code team thinks about verification -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 244 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.62 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;코드의 90%를 AI가 작성하고 리뷰하는 시대의 검증 철학&quot; — Claude Code 팀의 내부 검증기</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">claude.dev — 생성 비용보다 '검증과 리뷰 병목'을 어떻게 뚫는지에 관한 엔지니어링 팀의 실전 노하우 공개</span>
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
            <h3 class="minor-detail-headline">에이전트가 90%의 코드를 쓸 때 인간 엔지니어가 붙잡아야 할 마지막 10%의 통제권</h3>
            <div class="minor-detail-subheadline">190개 댓글 격론 · 병렬 에이전트 토큰 비용 vs 자동 검증 파이프라인 신뢰성 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  "Claude Code 팀 코드의 약 90%를 Claude가 작성하고 리뷰한다"는 고백과 함께, 수십~수백 개의 병렬 에이전트를 굴릴 때 인간 리뷰어가 익사하지 않도록 테스트·타입·샌드박스 검증 루프를 설계하는 방식이 공개되며 244점·190댓글을 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[검증 아키텍처]</strong> Parallel Agent Codegen (90%) &rarr; Automated Test &amp; Self-Review Gates &rarr; Human Focus on High-Risk 10%
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  현업 개발자들은 에이전트 수십 개를 병렬 실행할 때 발생하는 월 수천 달러대 토큰 비용 문제와 "AI가 짠 나머지 10%의 미묘한 설계 결함을 누가 책임질 것인가"를 두고 열띤 토론을 벌였습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Claude 블로그 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50529612" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (244 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Regulatory Capture by Anthropic Through METR -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 137 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 13.16 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 안전성 평가 기관 METR과 앤스로픽의 재정·인적 연결고리를 둘러싼 '규제 포획' 논쟁&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nitter.cf — IPO 시점과 맞물려 AI 벤치마크·규제 표준화 과정의 이해상충을 파고든 공개 재무 분석 폭로전</span>
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
            <h3 class="minor-detail-headline">AI 모델 안전성 벤치마크 거버넌스의 독립성을 묻는 해커뉴스의 날카로운 시선</h3>
            <div class="minor-detail-subheadline">72개 댓글 공방 · 공개 비영리 공시 자료 분석 기반 · 안전 규제와 시장 독점의 경계 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  선도 AI 연구소들이 자발적 안전 평가 협약을 맺는 평가 기관(METR 등)과 후원·이사회 인맥으로 얽혀 특정 규제 기준을 유리하게 유도하고 있다는 주장이 제기되며 137점과 72개의 논쟁적 댓글이 달렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[거버넌스 쟁점]</strong> Frontier Lab Funding &amp; Networks &rarr; AI Safety Eval Standards &rarr; Open-Source Regulatory Barrier Debate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  일부 독자들은 공개 정보 재구성에 과장된 해석이 섞였다며 선을 그으면서도, 제3자 AI 안전성 평가 기관의 재정적 투명성과 오픈소스 진영에 미칠 규제 역효과만큼은 철저히 감시해야 한다는 데 공감했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://nitter.cf/kevinnbass/status/2099621874279817638" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 분석 스레드 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50530450" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (137 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Windows 11 coding agent telemetry -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 704 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 29.57 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Windows 11이 개발자 PC에서 어떤 코딩 에이전트와 툴을 쓰는지 텔레메트리로 수집하고 있다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">xusheng.dev — OS 수준 프로세스·도구 사용 이력 수집 정황 분석이 공개되며 704점·584댓글 프라이버시 분노 촉발</span>
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
            <h3 class="minor-detail-headline">OS 벤더와 자사 AI 코딩 툴 경쟁사 간의 이해충돌이 낳은 텔레메트리 감시 논란</h3>
            <div class="minor-detail-subheadline">584개 댓글 성토 · 개발자 도구 사용 패턴 수집 실태 분석 · 리눅스·macOS 이주론 재점화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Windows 11이 로컬 PC에 설치·실행 중인 코딩 에이전트 및 개발자 도구 목록을 텔레메트리로 수집해 전송하고 있다는 기술 분석 글이 올라오자, 하루 만에 704점과 584개의 거센 비판 댓글이 달렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[텔레메트리 논란]</strong> Local Coding Agent Execution &rarr; Windows 11 OS Telemetry Collector &rarr; Developer Privacy &amp; Antitrust Concerns
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  운영체제 공급자가 자체 코딩 에이전트(Copilot 등)를 판매하면서 동시에 OS 차원에서 경쟁 에이전트의 시장 점유율 데이터를 수집하는 행위는 심각한 신뢰 훼손이라는 비판이 지배적이었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://xusheng.dev/posts/windows-coding-agent-telemetry/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 기술 분석 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50524736" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (704 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Optimizely compromised (Zoom, GitLab, CNN, Fox News) -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 657 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 27.64 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Optimizely 태그 침해로 Zoom·GitLab·CNN 방문자에게 악성코드·암호화폐 스키머 유포 (OPTIMJACK)&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blog.report-uri.com — 서드파티 A/B 테스트 스크립트 한 줄이 세계 최대 기업들의 프론트엔드를 통째로 감염시킨 공급망 대참사</span>
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
            <h3 class="minor-detail-headline">&quot;원본 서버(Origin)가 깨끗해도 마케팅 태그 레이어가 뚫리면 방문자 전원이 당한다&quot;</h3>
            <div class="minor-detail-subheadline">260개 댓글 · OPTIMJACK 스키머(CNN·Zoom·Fox News·GitLab 동시 영향) 클러스터 통합 · CSP·SRI 방어론 재조명</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  웹 실험·개인화 플랫폼 Optimizely의 스크립트 태그가 침해되면서 Zoom, GitLab, CNN, Fox News 등 초대형 사이트 방문자들에게 암호화폐 탈취 스키머(OPTIMJACK)와 악성 페이로드가 유포된 대형 공급망 사건이 657점을 기록했습니다. (유사 후속 보도인 OPTIMJACK 리포트 통합)
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[공격 경로]</strong> Compromised Optimizely Tag &rarr; Dynamic 3rd-Party JS Injection &rarr; Zoom / GitLab / CNN Visitor Exploitation
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  엔지니어들은 마케팅·분석 팀이 임의로 삽입하는 동적 서드파티 JS에 대해 엄격한 <code>Content-Security-Policy(CSP)</code> 화이트리스트와 결제·인증 페이지에서의 완전 격리를 강제해야 한다고 입을 모았습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Report URI 분석
              </a>
              <a href="https://news.ycombinator.com/item?id=50524767" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (657 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Jiff 1.0: A datetime library for Rust -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 436 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.59 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;ripgrep 창시자 BurntSushi의 차세대 Rust 날짜·시간 라이브러리 'Jiff 1.0' 정식 출시&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">burntsushi.net — 자바스크립트 Temporal 영감과 IANA 타임존·일광절약시간 완벽 지원을 담아 '성공의 구덩이'로 이끄는 Unlicense 1.0 릴리즈</span>
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
            <h3 class="minor-detail-headline">chrono를 넘어 Rust 생태계 및 LLM 코드 생성의 새로운 기본 표준을 노리는 Jiff 1.0</h3>
            <div class="minor-detail-subheadline">95개 댓글 찬사 · Unlicense · API 안정성 1.0 선언 및 GitHub Rust 트렌딩 동시 진입</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  <code>ripgrep</code>과 <code>regex</code> 크레이트로 유명한 앤드루 갤런트(BurntSushi)가 수년간 다듬어온 Rust 날짜·시간 라이브러리 <code>Jiff</code>의 정식 1.0을 발표하자, Rust 커뮤니티의 전폭적 지지를 받으며 HN 436점과 GitHub Rust 트렌딩을 동시에 장식했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[설계 철학]</strong> Pit of Success API (Temporal-Inspired) &rarr; First-Class IANA TZDB &amp; DST &rarr; Zero-Surprise Rust 1.0 Datetime
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자들은 타임존·서머타임 계산에서 실수하기 어렵게 만든 직관적 API 설계를 극찬하며, 앞으로 인간 개발자뿐 아니라 LLM 코딩 에이전트도 기본적으로 <code>Jiff 1.0</code>을 선택하게 될 것이라 전망했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://burntsushi.net/jiff/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Jiff 1.0 출시 노트
              </a>
              <a href="https://news.ycombinator.com/item?id=50519744" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (436 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
