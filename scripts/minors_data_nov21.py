# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-21

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
          직전 발행(11월 20일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 스팸·크랙·SEO 봇넷 저장소·기발행 중복 이력 배제 및 재귀적 동일 주제 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: podomy/weld -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 102개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.57 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;ROS 2 대비 지연시간 최대 68% 단축·100kHz 무손실 통신을 구현한 Go 로보틱스 미들웨어&quot; : weld</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">podomy/weld — 링크가 끊기는 현장에서도 군집 로봇을 조율하는 ROS 2 와이어 호환 단일 리더리스 데이터 플레인 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">CycloneDDS 백엔드 위에서 ROS 2와 와이어 호환되며 지연시간과 패킷 유실을 끝낸 Go 미들웨어</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · Go 기반 · 110-row 벤치마크 매트릭스 전 구간 통과 · 토픽/서비스/액션/파라미터 단일 평면 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  현장 로봇 플릿은 무선 링크가 수시로 끊기고 높은 주파수의 센서 스트림을 주고받아야 하지만, 기존 ROS 2 미들웨어 스택은 호스트 내 p50 지연시간과 고주파 패킷 드롭 문제로 골치를 앓아 왔습니다. <code>podomy/weld</code>는 110개 조합의 벤치마크 매트릭스에서 동일 호스트 지연시간을 최대 68% 줄이고 ROS 2가 패킷을 떨어뜨리는 100kHz 구간에서도 무손실을 달성해 5.8시간 만에 102스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[데이터 플레인]</strong> ROS 2 Wire-Compatible Topics/Actions &rarr; Leaderless Go Plane &rarr; CycloneDDS Backend (100kHz Zero-Loss)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  C++ DDS 보일러플레이트 없이 Go의 동시성과 와이어 호환성을 결합해 기존 ROS 2 생태계에 즉시 드롭인 교체할 수 있다는 점이 로보틱스 엔지니어들의 관심을 집중시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/podomy/weld" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: sohzm/winedroid -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 46개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.73 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;안드로이드 OS 부팅 없이 브라우저·macOS·Linux에서 APK를 직접 돌리는 Rust 호환 레이어&quot; : winedroid</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">sohzm/winedroid — Wine에서 영감을 받아 DEX 바이트코드·Skia UI·Cranelift JIT·WebAssembly 웹 데모를 구현 (HN 동시 화제 통합)</span>
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
            <h3 class="minor-detail-headline">에뮬레이터 VM 없이 DEX 바이트코드와 안드로이드 프레임워크를 네이티브·WASM으로 번역 실행하는 WineDroid</h3>
            <div class="minor-detail-subheadline">Rust 기반 · Cranelift JIT(데스크톱) + Skia 렌더링 + WebAssembly 브라우저 데모 · Show HN 69점 클러스터 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  macOS나 웹 브라우저에서 안드로이드 APK를 실행하려면 수 GB짜리 Android 에뮬레이터 VM을 통째로 띄워야 했습니다. Rust로 작성된 <code>winedroid</code>는 리눅스용 Wine처럼 Android OS 커널 부팅 없이 DEX 바이트코드를 직접 해석·JIT 컴파일하고 Skia로 UI를 그려내며, WebAssembly 빌드로 브라우저 데모(<code>winedroid.soham.sh/demo/</code>)까지 띄워 GitHub과 Hacker News에서 동시에 주목받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[호환 계층]</strong> Android APK (DEX Bytecode) &rarr; Rust Runtime + Cranelift JIT / WASM &rarr; Skia Native/Browser UI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에뮬레이터 오버헤드를 걷어낸 클린룸 호환 레이어 접근법 덕분에 웹 기반 앱 미리보기와 경량 CI UI 테스트의 새로운 가능성을 열었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://winedroid.soham.sh/demo/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> WASM 브라우저 데모
              </a>
              <a href="https://github.com/sohzm/winedroid" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: danielwh2/sprite-stacking -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 80개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 9.73 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;4장의 2D 픽셀아트를 회전 가능한 유사 3D 복셀 스프라이트로 굽는 에이전트 스킬&quot; : sprite-stacking</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">danielwh2/sprite-stacking — Python 3 + Pillow + NumPy로 4방향 정사영 도트를 3D 레이어 스택으로 복원하는 MIT 코딩 에이전트 스킬</span>
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
            <h3 class="minor-detail-headline">정면·후면·좌우 픽셀 시트 4장만으로 인디 게임용 360도 회전 스프라이트 스택을 생성하는 스킬</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python 3 + Pillow + NumPy · Claude Code·Codex·Cursor·OpenCode 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  인디 게임 개발에서 2D 픽셀아트에 입체감을 주는 스프라이트 스태킹(Sprite Stacking) 기법은 수작업으로 수십 장의 수평 단면(Slice)을 그려야 해 진입 장벽이 높았습니다. Daniel White가 공개한 이 MIT 스킬은 4장의 직교 픽셀아트 뷰에서 3D 복셀 스택을 역산해 회전 렌더링까지 자동화하며 공개 8.2시간 만에 80스타를 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[복셀 역산]</strong> 4 Orthogonal Pixel Views &rarr; NumPy/Pillow 3D Slice Carving &rarr; Turntable Fake-3D Sprite Stack
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  무거운 3D 모델링 툴 없이도 코딩 에이전트가 에셋 제작 파이프라인 안에서 즉석으로 회전 가능한 게임용 2.5D 에셋을 조립할 수 있게 해줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/danielwh2/sprite-stacking" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: tristanbuckmaster/navier-stokes -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 206개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.03 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;나비에-스토크스 방정식 유한 시간 폭발(Blow-up) 논문 &amp; Lean 4 정형 검증 코드 전격 공개&quot; : navier-stokes</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">tristanbuckmaster/navier-stokes — L. Alpöge·T. Buckmaster의 79페이지 논문과 Mathlib 기반 Lean v4.33.1 증명 패키지 (HN 235점 통합)</span>
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
            <h3 class="minor-detail-headline">밀레니엄 난제 나비에-스토크스 유한 시간 특이점 증명을 Lean 4 컴파일러 검증 가능 형태로 공개</h3>
            <div class="minor-detail-subheadline">Lean v4.33.1 + Mathlib · 79페이지 논문(2026-11-20) + 전체 정형화 소스 수록 · HN 235점 토론 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  클레이 수학연구소 밀레니엄 7대 난제 중 하나인 3차원 나비에-스토크스 방정식의 유한 시간 폭발(Finite-time blow-up)에 대해, L. Alpöge와 T. Buckmaster가 79쪽 분량의 논문과 함께 <strong>Lean v4.33.1 + Mathlib</strong> 정형 검증 코드를 GitHub에 공개하자 수학계와 개발자 커뮤니티가 동시에 들끓으며 12시간 만에 206스타(HN 235점)를 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[정형 수학 검증]</strong> 79-Page PDE Proof (Alpöge &amp; Buckmaster) &rarr; Lean v4.33.1 + Mathlib &rarr; Machine-Checked Singularity Verification
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  수십 쪽짜리 편미분방정식 논문의 공백을 피어 리뷰 이전 단계에서 누구나 <code>lake build</code>로 기계적 검증(Machine-check)할 수 있도록 공개한 점이 현대 수학·정형 검증 워크플로우의 전환점을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://news.ycombinator.com/item?id=50576232" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (235 pts)
              </a>
              <a href="https://github.com/tristanbuckmaster/navier-stokes" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: nestjs/agent-skills -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 88개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 15.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.86 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;테스트는 통과하지만 프로덕션을 터뜨리는 AI 백엔드 버그를 막는 NestJS 공식 스킬&quot; : agent-skills</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nestjs/agent-skills — 모델 학습 데이터 이후의 최신 Nest API와 이메일 유출·null 통과 500 에러 등 함정을 차단하는 MIT 공식 스킬</span>
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
            <h3 class="minor-detail-headline">단위 테스트를 통과하고도 실서버에서 뚫리는 NestJS 안티패턴을 사전 봉쇄하는 퍼스트파티 Agent Skills</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · NestJS 공식 조직 저장소 · agentskills.io 표준 준수 · 최신 퍼스트파티 패키지 API 내장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  LLM은 컷오프 이전의 구형 NestJS 코드를 학습해 최신 API를 놓치거나, <code>@IsOptional()</code> 데코레이터가 <code>null</code>을 통과시켜 500 에러를 유발하거나, 가입 이메일 존재 여부를 응답 차이로 유출하는 미묘한 실수를 자주 저지릅니다. NestJS 공식 팀이 직접 작성해 배포한 <code>nestjs/agent-skills</code>는 이 함정들을 에이전트 컨텍스트에 직접 교정 주입해 15시간 만에 88스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[프레임워크 가드]</strong> Outdated LLM Prior &rarr; Official NestJS Agent Skills &rarr; Up-to-Date API + Auth/Validation Trap Prevention
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  공식 프레임워크 팀이 인간용 문서를 넘어 'AI 에이전트용 방어 스킬'을 1급 배포 산출물로 제공하기 시작한 대표적 사례로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/nestjs/agent-skills" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: AI4XE/ai4ai -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 62개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.65 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 에이전트가 스스로 컨텍스트 잔량·추론 강도를 읽고 자가 복제·갱신하는 하네스 킷&quot; : ai4ai</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AI4XE/ai4ai — Claude Code와 OpenCode 등 이기종 하네스의 런타임 제어 기능을 단일 툴 인터페이스로 추상화한 MIT 킷</span>
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
            <h3 class="minor-detail-headline">에이전트가 자신의 컨텍스트 윈도우·추론 예산·세션 갱신을 직접 제어하는 크로스 하네스 추상화 레이어</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript 기반 · Claude Code &amp; OpenCode 플러그인 동시 지원 · 런타임 메타인지 툴셋</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  에이전트는 작업 중 자신의 컨텍스트 창이 얼마나 찼는지, 현재 어떤 모델과 추론 강도(Reasoning Effort)로 돌고 있는지 몰라 장시간 작업에서 갑자기 기억을 잃곤 합니다. <code>AI4XE/ai4ai</code>는 하네스마다 제각각인 런타임 상태 조회, 컨텍스트 갱신(Renewal), 자가 복제(Self-duplication) API를 공통 인터페이스로 묶어 11시간 만에 62스타를 확보했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[메타인지 루프]</strong> Runtime State Probe (Context/Model/Effort) &rarr; Cross-Harness Adapter &rarr; Self-Renewal &amp; Portable Skill
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  특정 코딩 에이전트 벤더의 내부 슬래시 커맨드에 종속되지 않고, 에이전트 스스로 컨텍스트 포화 직전에 작업을 인수인계할 수 있는 이식형 표준을 제시합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/AI4XE/ai4ai" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: jweihe/Awesome-3D-Coding -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 86개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.27 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;메쉬가 아니라 실행 가능한 코드로 3D 월드와 CAD를 생성·편집하는 에이전트 3D 코딩 총람&quot; : Awesome-3D-Coding</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">jweihe/Awesome-3D-Coding — Blender Python·파라메트릭 CAD·Three.js 인터랙티브 월드 생성 벤치마크·데이터셋·에이전트 큐레이션</span>
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
            <h3 class="minor-detail-headline">수정 불가능한 폴리곤 덩어리를 넘어 파라메트릭 코드 기반 3D 생성·편집 연구를 집대성한 레퍼런스</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · 3D Coding 벤치마크 · Blender/CAD 어셈블리 · Three.js 인터랙티브 구조 편집</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 3D 생성 AI가 뱉어내는 메쉬(Mesh) 파일은 치수 하나를 고치기도 어려워 실제 CAD나 게임 제작에 쓰기 힘들었습니다. 3D 장면을 <strong>실행 가능한 Blender·CAD·Three.js 코드</strong>로 생성하고 구조적으로 수정하는 '3D Coding' 분야가 급부상하면서, 관련 벤치마크와 데이터셋·에이전트를 체계화한 이 저장소가 20시간 만에 86스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[코드 투 3D]</strong> Prompt / Visual Target &rarr; Executable Blender/CAD/Three.js Code &rarr; Parametric Editable 3D Scene
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  VLM과 코딩 에이전트를 3D 에셋 엔지니어링에 투입하려는 연구자와 그래픽스 개발자들에게 가장 빠른 길잡이 역할을 하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/jweihe/Awesome-3D-Coding" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: nickvasilescu/openman -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 84개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.22 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;실시간 컴퓨터 화면을 띄워두고 언제든 사람이 조종간을 넘겨받는 오픈소스 자율 에이전트 사옥&quot; : openman</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nickvasilescu/openman — Orgo 클라우드 컴퓨터 위에서 기획·브라우징·코딩·자동화 스케줄을 수행하며 라이브 뷰 인수를 지원하는 MIT 워크스페이스</span>
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
            <h3 class="minor-detail-headline">유료 Manus식 클라우드 에이전트 경험을 Orgo 기반 오픈소스 워크스페이스로 구현한 OpenMan</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript 기반 · 라이브 컴퓨터 뷰 &amp; 즉시 수동 개입 · 프로젝트·스킬·앱 커넥터 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  사용자가 작업만 던지면 가상 컴퓨터에서 브라우저와 터미널을 굴려 완료하는 범용 에이전트 워크스페이스에 대한 수요가 높지만 대부분 폐쇄형 유료 서비스에 갇혀 있습니다. <code>openman</code>은 Orgo 클라우드 컴퓨터를 백엔드로 연결해 에이전트 화면을 실시간 관전하다가 2FA 인증이나 민감한 결제 단계에서 즉시 사람이 제어권을 넘겨받는 UX를 MIT 소스로 열어 84스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[협업 워크스페이스]</strong> Task + Shared Skills &rarr; Orgo Cloud VM Execution &rarr; Live Screen Stream &amp; Human Takeover
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  공유 지침(Projects), 스킬, 외부 앱 커넥터, 정기 스케줄 자동화까지 한 번에 묶인 깔끔한 풀스택 레퍼런스로 호평받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/nickvasilescu/openman" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: mgolcu00/freeimage-local -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 69개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.68 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;6GB VRAM 노트북 RTX 3060에서 Z-Image Turbo를 풀스피드로 굽는 로컬 이미지 엔진&quot; : freeimage-local</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">mgolcu00/freeimage-local — freeimage.dev의 실제 백엔드로 int8 + SageAttention on stable-diffusion.cpp를 패키징한 MIT 엔진</span>
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
            <h3 class="minor-detail-headline">집 노트북 한 대로 무료 웹사이트(freeimage.dev)까지 호스팅하던 실전 6GB VRAM 최적화 스크립트</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · stable-diffusion.cpp 기반 · int8 + SageAttention · RTX 3060 Laptop 실증</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  무료 AI 이미지 생성 사이트 <code>freeimage.dev</code>가 사실 데이터센터 GPU가 아니라 개발자 집의 단 한 대짜리 RTX 3060 노트북(6GB VRAM)으로 돌아가고 있었다는 사실과 함께 그 핵심 엔진이 MIT 오픈소스로 풀리자 25.7시간 만에 69스타가 모였습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[6GB 최적화]</strong> Z-Image Turbo &rarr; int8 Quantization + SageAttention (stable-diffusion.cpp) &rarr; 6GB Laptop GPU Full-Speed
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  PyTorch 무거운 의존성 없이 C++ 기반 <code>stable-diffusion.cpp</code>에 <code>int8</code>과 <code>SageAttention</code>을 결합해 보급형 노트북에서도 실서비스급 응답 속도를 뽑아내는 정석적인 경량화 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://freeimage.dev" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> freeimage.dev 공식 사이트
              </a>
              <a href="https://github.com/mgolcu00/freeimage-local" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Levent Alpöge GRH Proof + Lean Formalization Cluster -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 2,198 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 258.71 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클로드와 함께 일반화 리만 가설(GRH) 증명 및 Lean 정형화 완료&quot; — Levent Alpöge 발표와 수학계 대격변</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">alpo.ge/remark.pdf — 2,198점·1,505댓글 기록, Masullo(1,210점)·Aaronson·Terry Tao 논평 및 GitHub Lean 미러 저장소 일괄 클러스터</span>
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
            <h3 class="minor-detail-headline">수학 난제 일반화 리만 가설(GRH)의 무가정 Lean 정형 증명 발표로 HN 역대급 2,198점 폭발</h3>
            <div class="minor-detail-subheadline">8.5시간 만에 1,505댓글 · Masullo GRH(1,210점)·Scott Aaronson·Terry Tao·GH Lean 미러 4종 재귀 클러스터 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  정수론의 저명한 수학자 레벤트 알푀게(Levent Alpöge)가 2026년 11월 20일, Claude와의 협업을 통해 디리클레 L-함수로 확장되는 <strong>일반화 리만 가설(GRH)의 증명</strong>을 찾아냈으며 추가 가정 없이 Lean으로 완전 정형화했다고 발표했습니다. 직후 Alessandro Masullo의 동시기 GRH 발표(1,210점), 스콧 아론슨과 테렌스 타오의 긴급 분석, 그리고 GitHub의 Lean 검증 미러 저장소(<code>CocoSgt/riemann-hypothesis-lean</code>·<code>Deicyde/riemann-hypothesis</code>·<code>rohanarun/alpoge-rh-replay</code>)가 동시다발적으로 터지며 기술계 최대 화제로 부상했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[증명 검증]</strong> Mathematician + Claude Collaboration &rarr; GRH Remark PDF &amp; Lean Proof &rarr; Global Independent Replay Audit
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  논문의 최종 수학적 진위와 별개로, 정형 증명 언어 Lean의 공리(Axiom) 위조·정의 트릭 여부를 전 세계 개발자들이 몇 시간 만에 분산 리플레이 스크립트로 감사하는 새로운 '오픈소스 수학 검증 문화'가 입증되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://alpo.ge/remark.pdf" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 증명 노트 PDF 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50574968" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (2,198 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Inkling 2 Mini -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 440 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 172.43 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Thinking Machines Lab의 차세대 초소형 모델 'Inkling 2 Mini' 및 가변 루프(varlooped) 변종 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">thinkingmachines.ai — 2.6시간 만에 440점 급등, 체감 성능이 벤치마크를 웃도는 초경량 아키텍처와 반복 깊이 추론 변종에 연구계 환호</span>
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
            <h3 class="minor-detail-headline">대형 모델의 단순 축소가 아닌 가변 루프 추론(varlooped) 연구를 함께 연 Inkling 2 Mini</h3>
            <div class="minor-detail-subheadline">2.6시간 만에 440점 · Thinking Machines Lab 발표 · 실사용 체감 품질과 varlooped 연구 트랙 주목</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  미라 무라티 등이 이끄는 Thinking Machines Lab이 차세대 소형 모델 <code>Inkling 2 Mini</code>를 공개하자 불과 2.6시간 만에 440점이 몰렸습니다. 특히 연구자들은 기본 모델뿐만 아니라 계산 깊이를 동적으로 반복 조절하는 <strong>varlooped 변종</strong>을 함께 공개한 연구 투명성에 크게 호응했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[소형 추론 혁신]</strong> Inkling 2 Mini Base &rarr; Variable-Loop Recurrent Depth (varlooped) &rarr; High Efficiency Reasoning
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  벤치마크 수치 짜맞추기(Benchmaxing)보다 실제 코딩·에이전트 루프에서의 안정적인 체감 성능과 루프형 추론(Looped Transformers) 아키텍처의 실용성을 증명한 분기점으로 평가됩니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://thinkingmachines.ai/news/inkling-2-mini/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 발표 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50581260" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (440 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: I'll never buy Framework hardware again -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 747 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 112.16 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;다시는 Framework 하드웨어를 사지 않겠다&quot; — 모듈형 수리권 랩톱의 품질·지원 현실을 꼬집은 519댓글 격론</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">poolp.org — OpenSMTPD 개발자 Gilles Chehade가 제기한 내구성·CS 경험 비판과 MacBook Pro 대비 엔지니어 실무 워크스테이션 논쟁</span>
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
            <h3 class="minor-detail-headline">모듈형 노트북의 이상(Right to Repair)과 실무 신뢰성 사이의 간극을 정면 논쟁하다</h3>
            <div class="minor-detail-subheadline">6.7시간 만에 747점·519댓글 · OpenBSD/OpenSMTPD 개발자의 실사용 고발 · 하드웨어 신뢰성 토론</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  '자가 수리 가능한 모듈형 노트북'의 상징이던 Framework를 장기간 업무용으로 사용하던 유명 오픈소스 개발자(poolp.org)가 반복적인 하드웨어 결함과 고객지원 마찰을 이유로 절연을 선언하자, 6.7시간 만에 747점과 519개의 열띤 댓글이 쏟아졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[하드웨어 딜레마]</strong> Modular Repairability Ideal &harr; Chassis/Thermal/CS Friction &rarr; Enterprise Fleet Reliability Debate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개인의 리눅스 실험·이념적 지지 하드웨어로서의 매력과 달리, 회사 엔지니어 팀에 수십 대씩 지급할 때는 배터리·빌드 완성도·무상 AS 속도가 압도적인 결정 변수라는 냉정한 실무 합의가 형성되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 포스트
              </a>
              <a href="https://news.ycombinator.com/item?id=50576855" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (747 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Frostbite: A new CPU architecture discovered, designed and verified by AI -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 595 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 46.78 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI가 스스로 발굴·설계·정형 검증까지 끝낸 새로운 CPU 아키텍처 'Frostbite'&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">architectlabs.com — 595점·315댓글, 명령어 집합 탐색부터 RTL 설계·하드웨어 정형 검증까지 AI 파이프라인이 완결한 실리콘 혁신</span>
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
            <h3 class="minor-detail-headline">단순 HDL 코드 보조를 넘어 새로운 마이크로아키텍처를 발명하고 검증한 AI 하드웨어 설계</h3>
            <div class="minor-detail-subheadline">12.7시간 만에 595점·315댓글 · AI-Driven ISA/RTL Discovery &amp; Verification · 반도체 설계 패러다임 논의</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Architect Labs가 인간의 기존 설계 관습에서 벗어나 AI 에이전트 탐색을 통해 도출하고, 논리 검증까지 통과시킨 CPU 아키텍처 <strong>Frostbite</strong>를 공개하자 반도체·시스템 엔지니어들이 315개의 댓글을 달며 열띤 검증 논의를 벌였습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[AI 실리콘]</strong> Architecture Space Search &rarr; AI RTL Synthesis &rarr; Formal Hardware Verification (Frostbite CPU)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  소프트웨어를 넘어 칩 설계 단계까지 AI가 자율 진입하면서, 향후 컴퓨팅 패권이 모델·연산 자원(전력/칩)·파운드리·소재의 4대 축으로 압축될 것이라는 산업 통찰이 큰 공감을 얻었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://architectlabs.com/blog/frostbite" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Architect Labs 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=50572503" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (595 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Signal Is Serious About Protecting Your Privacy -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 450 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 34.45 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Signal은 당신의 프라이버시 보호에 진심이다&quot; — 전화번호·결제 수단 익명성 한계까지 파고든 283댓글 검증</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">signal.org — 450점 기록, 각국 정부의 암호화 백도어 압박에 맞선 Signal의 기술적 방어선과 계정 생성 시 익명 결제 논쟁</span>
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
            <h3 class="minor-detail-headline">최소 메타데이터 원칙을 고수하는 Signal의 공식 프라이버시 선언과 커뮤니티의 더 높은 익명성 요구</h3>
            <div class="minor-detail-subheadline">13.1시간 만에 450점·283댓글 · Zero-Metadata &amp; E2EE 방어 원칙 · Monero 등 무신원 결제 도입 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  영국·EU 등 각국 정부의 종단간 암호화(E2EE) 우회 압박과 감시 기술 고도화 속에서 Signal 재단이 메타데이터를 일절 저장하지 않는 아키텍처와 프라이버시 원칙을 재천명한 블로그를 올려 450점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[메타데이터 0]</strong> Sealed Sender + SGX Contact Discovery &rarr; Zero Server-Side Social Graph &harr; Phone/Payment Onboarding Friction
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  토론에서는 현존 최강의 프라이버시 메신저라는 점에 동의하면서도, 스팸 방지용 계정 생성 시 전화번호나 추적 가능한 카드 결제 외에 익명 암호화폐(Monero 등) 옵션을 열어야 진정한 무신원 익명성이 완성된다는 날카로운 지적이 이어졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://signal.org/blog/protecting-your-privacy/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Signal 공식 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=50572348" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (450 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Google is pushing OEMs against GrapheneOS and bootloader unlocking -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 470 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.98 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;구글, 제조사(OEM)에 GrapheneOS 협력 중단 및 부트로더 잠금 해제 차단 압박 의혹&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">grapheneos.social — 470점·186댓글 기록, Pixel 부트로더 잠금 가능성과 Android Authority 후속 보도(53점) 통합 클러스터</span>
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
            <h3 class="minor-detail-headline">모바일 보안 OS의 마지막 보루 GrapheneOS와 구글 간 '부트로더 개방성' 정면 충돌</h3>
            <div class="minor-detail-subheadline">17.4시간 만에 470점·186댓글 · Pixel 부트로더 잠금 우려 및 후속 2건(53점·22점) 클러스터 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  프라이버시·보안 특화 모바일 OS인 GrapheneOS 측이 공식 채널을 통해 구글이 스마트폰 제조사(OEM)들에게 GrapheneOS와의 협력을 막고 부트로더 잠금 해제(Bootloader Unlocking)를 제한하도록 압박하고 있다고 폭로했습니다. 뒤이어 차기 Pixel 기기의 부트로더 잠금 가능성까지 보도되며 안드로이드 개방성 훼손에 대한 거센 반발이 터져 나왔습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[플랫폼 통제]</strong> Google GMS/OEM Pressure &rarr; Bootloader Unlock Restriction &rarr; Custom Security OS (GrapheneOS) Threat
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  사용자가 직접 구매한 하드웨어에서 운영체제를 교체하고 구글의 데이터 수집·AI 학습에서 벗어날 수 있는 권리(Device Ownership)가 안드로이드 진영에서도 사라질 위기에 놓였다는 경고가 쏟아졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://grapheneos.social/@GrapheneOS/117645038299496084" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> GrapheneOS 성명 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50570479" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (470 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Pancreatic cancer halted by virus injection in three patients -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 870 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 29.65 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;바이러스 주사로 말기 췌장암 환자 3명의 암 진행을 멈추다&quot; — 항암 바이러스 치료 임상 성과</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">newscientist.com — 870점 기록, 치명률이 가장 높은 고형암 중 하나인 췌장암에서 종양 증식을 정지시킨 초기 바이오 Breakthrough</span>
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
            <h3 class="minor-detail-headline">암세포만 표적 파괴하고 면역 반응을 깨우는 항암 바이러스 요법의 극적인 췌장암 임상 결과</h3>
            <div class="minor-detail-subheadline">29.3시간 만에 870점·154댓글 · Oncolytic Virus Therapy · New Scientist 보도</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  조기 발견이 어렵고 기존 항암제에 잘 반응하지 않는 췌장암 환자 3명에게 유전자 변형 바이러스를 주입한 결과 종양의 진행이 멈췄다는 New Scientist 보도가 Hacker News에서 870점의 높은 관심을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[생물학적 타겟팅]</strong> Engineered Oncolytic Virus Injection &rarr; Selective Tumor Lysis &amp; Immune Activation &rarr; Disease Halt
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  소규모 초기 임상이라는 신중론과 함께, 합성생물학과 유전자 편집 기반 표적 바이러스 플랫폼이 난치성 고형암 치료의 실질적 돌파구로 올라서고 있음을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> New Scientist 기사
              </a>
              <a href="https://news.ycombinator.com/item?id=50563066" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (870 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Claude solves two open problems in the physics of black holes -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 550 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.80 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Claude, 블랙홀 물리학의 미해결 난제 2건을 풀다&quot; — Anthropic 과학 추론 연구</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">anthropic.com — 550점·266댓글 기록, 이론물리학자의 가설 검증과 복잡한 수리 계산을 뚫어 미해결 문제를 해결한 AI 과학 공동연구</span>
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
            <h3 class="minor-detail-headline">코딩과 문서를 넘어 이론물리학의 미해결 경계를 밀어낸 AI 추론 모델의 과학적 성과</h3>
            <div class="minor-detail-subheadline">29.3시간 만에 550점·266댓글 · Anthropic Research · 블랙홀 물리학 난제 해결 사례</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Anthropic이 공식 리서치 블로그를 통해 Claude가 이론물리학 연구자들과 함께 블랙홀 물리학 분야의 미해결 난제 두 가지를 풀어냈다고 발표하자 550점과 266개의 댓글이 달렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[AI 과학 발견]</strong> Open Black-Hole Physics Conjecture &rarr; Symbolic Derivation + Reasoning Search &rarr; Verified Analytical Solution
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단순 요약 도구가 아니라 고난도 대수적 변형과 비자명한 물리학적 직관을 보조하는 과학 연구 파트너로서의 프론티어 모델 위상을 재확인했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.anthropic.com/research/claude-black-hole-physics" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Anthropic 연구 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50563148" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (550 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: OpenSSL: Buffer overflow in EVP_EncodeBlock() (CVE-2026-121481, CVSS 9.8) -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 362 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.45 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;OpenSSL <code>EVP_EncodeBlock()</code> 버퍼 오버플로우(CVE-2026-121481, CVSS 9.8)&quot; — 긴급 패치 PR과 심각도 논란</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">github.com/openssl/openssl — 362점·328댓글 기록, Base64 인코딩 함수의 치명적 경계 오류 수정 PR과 실제 익스플로잇 조건 분석</span>
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
            <h3 class="minor-detail-headline">전 세계 인프라의 암호화 기반 OpenSSL에서 발견된 CVSS 9.8 버퍼 오버플로우와 실전 위협 평가</h3>
            <div class="minor-detail-subheadline">20.7시간 만에 362점·328댓글 · CVE-2026-121481 · EVP_EncodeBlock() 경계 검사 패치</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  OpenSSL의 Base64 인코딩 경로인 <code>EVP_EncodeBlock()</code>에서 CVSS 9.8 등급의 버퍼 오버플로우 취약점(CVE-2026-121481)을 수정하는 PR(#33652)이 공개되자 보안 커뮤니티가 즉각 반응하며 328개의 기술 검증 댓글이 달렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[메모리 안전]</strong> EVP_EncodeBlock() Input Edge Case &rarr; Heap/Buffer Overflow Risk (CVE-2026-121481) &rarr; Upstream Bounds Check PR #33652
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  보안 엔지니어들은 CVSS 9.8이라는 최고점 산정이 실제 원격 RCE 도달 가능성과 일치하는지 치열하게 따지는 한편, C 기반 핵심 암호화 라이브러리의 오래된 인코딩 유틸리티까지 메모리 안전 감사와 패치 자동화가 필수적임을 다시 확인했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/openssl/openssl/pull/33652" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> OpenSSL PR #33652
              </a>
              <a href="https://news.ycombinator.com/item?id=50569226" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (362 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
