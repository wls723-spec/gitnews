# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-10-26

GH_MINORS = """
      <!-- [GH 0~10h] Item 1: unclebob/ub-mode -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 348개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 48.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;클린 코드 대부의 잔소리가 터미널에 떴다&quot; : AI 에이전트 클린 아키텍처 강제 모드</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">unclebob/ub-mode — Robert C. Martin(Uncle Bob)의 SOLID & TDD 원칙을 코딩 에이전트에 엄격 주입</span>
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
          <h3 class="minor-detail-headline">클린 코드(Clean Code)의 절대 법칙을 에이전트에 이식하다: ub-mode</h3>
          <div class="minor-detail-subheadline">SOLID 5대 원칙, 함수 10줄 제한, 테스트 주도 개발(TDD)을 어기면 커밋을 거부하는 엄격한 하네스</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 에이전트가 코드를 빠르게 짜면서 1,000줄이 넘는 거대 스파게티 함수와 테스트 없는 배포가 쏟아지는 부작용이 만연했습니다. 소프트웨어 장인정신의 창시자 '엉클 밥'의 철학을 코드 규칙으로 정형화한 <code>ub-mode</code>는 에이전트가 리팩토링 단계에서 단일 책임 원칙(SRP)과 의존성 역전(DIP)을 강제하도록 만들어 큰 화제를 모았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Agent Code Generation &rarr; AST Complexity Analyzer &rarr; SOLID Violation Gate &rarr; Auto-Refactor Loop &rarr; TDD Verified Commit
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                함수 길이 15줄 초과, 매개변수 3개 초과 시 에이전트의 PR 작성을 자동으로 중단시키고, 반드시 인터페이스 분리와 단위 테스트를 먼저 작성하도록 유도합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/unclebob/ub-mode" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: misshexa66/OunceCake -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 310개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.0시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 34.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;차세대 스위치 2 파일시스템 빗장이 풀렸다&quot; : romFS 및 exeFS 무암호화 추출기</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">misshexa66/OunceCake — Nintendo Switch 2 (Tegra T239 / Horizon OS) 롬FS 덤프 분석 도구</span>
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
          <h3 class="minor-detail-headline">차세대 콘솔 보안의 첫 번째 균열: OunceCake</h3>
          <div class="minor-detail-subheadline">스위치 2(Ounce) 암호화 패키지 헤더 분석 및 바이너리 자산 언팩 오픈소스 유틸리티</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                닌텐도의 차세대 콘솔(코드명 Ounce) 출시를 앞두고 초기 개발자 킷과 SDK 패키지에서 유출된 것으로 추정되는 바이너리 파일시스템 구조(romFS, exeFS)를 읽어내는 도구가 공개되었습니다. 보안 리서처들이 신규 하드웨어의 보안 아키텍처와 메모리 맵을 확인하기 위해 몰려들며 반나절 만에 300스타를 돌파했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Encrypted Package Header &rarr; Key Derivation Stage &rarr; romFS Directory Tree Parsing &rarr; Raw Binary Extraction
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                차세대 콘솔의 에뮬레이션 및 홈브루 생태계를 위한 초기 기초 분석 자료로 활용되고 있으며, 닌텐도 법무팀의 DMCA 대응 여부가 주목받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/misshexa66/OunceCake" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: lemiur/Game-Decompilation-Skill-For-Claude -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 48개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.7시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.9 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;고전 게임을 C 코드로 100% 되살린다&quot; : Claude 전용 바이트 매칭 디컴파일러</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">lemiur/Game-Decompilation-Skill-For-Claude — 기계어 바이너리를 인간이 읽는 C 소스로 완전 복원</span>
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
          <h3 class="minor-detail-headline">AI 에이전트와 결합한 리버스 엔지니어링의 신기원</h3>
          <div class="minor-detail-subheadline">컴파일 결과물이 원본 ROM과 비트 단위로 일치할 때까지 스스로 코드를 교정하는 TDD 디컴파일 스킬</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                고전 콘솔 게임의 C 소스코드 복원(Decompilation)은 수년이 걸리는 극도의 고난도 작업이었습니다. 이 스킬은 Ghidra 및 IDA 출력을 Claude Code에 연동하여, 재컴파일된 바이너리가 원본 ROM과 100% 바이트 단위로 일치할 때까지 어셈블리와 C 문법을 스스로 맞추는 자동 루프를 제공합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Raw ROM Binary &rarr; Disassembly Feed &rarr; Claude C Reconstruction &rarr; GCC Compiler &rarr; Byte-Exact Hash Verification
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                닌텐도 64, 게임보이 어드밴스 게임들의 PC 네이티브 포팅 및 60fps 와이드스크린 패치 제작 기간을 수개월에서 수일로 대폭 단축시킵니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/lemiur/Game-Decompilation-Skill-For-Claude" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 4: DenisSergeevitch/ex-ussr-kinship-research -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 527개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 40.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;흩어진 역사 기록에서 조상의 발자취를 추적한다&quot; : 증거 기반 AI 가계 분석 하네스</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">DenisSergeevitch/ex-ussr-kinship-research — 옛 소련 및 동유럽 고문서 교차 검증 전용 에이전트 스킬</span>
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
          <h3 class="minor-detail-headline">역사학자와 AI의 결합: 증거 우선(Evidence-First) 계보학</h3>
          <div class="minor-detail-subheadline">교회 기록부, 인구 조사 문서, 전쟁 사망자 명부를 그래프 데이터베이스로 엮는 지식 추론기</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                전쟁과 체제 전환으로 파편화된 동유럽 기록물에서 가계를 찾는 일은 극심한 기록 불일치와 지명 변경으로 난항을 겪어왔습니다. 이 프로젝트는 Claude Code와 Codex에 '사료 비판(Source Criticism)' 스킬을 부여해 날조 없이 확실한 증거 체인만을 연결해 계보 트리를 구축합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Handwritten Census OCR &rarr; Entity Disambiguation &rarr; Temporal Kinship Graph &rarr; Provenance Confidence Audit
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                할루시네이션에 취약한 LLM이 역사 및 법률 기록을 다룰 때 어떻게 '엄격한 증거 체인 검증 규칙'을 강제해야 하는지 보여주는 모범 사례로 평가받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/DenisSergeevitch/ex-ussr-kinship-research" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: mizorewww/gdirect -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 547개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.3시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 31.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;구글 드라이브 대용량 다운로드 제한을 찢다&quot; : Rust 초고속 멀티스레드 CLI</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">mizorewww/gdirect — libaria2를 핀 고정하여 브라우저 경고 없이 기가비트 속도로 고속 인출</span>
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
          <h3 class="minor-detail-headline">구글 드라이브의 속도 족쇄를 풀어내는 다운로드 가속기</h3>
          <div class="minor-detail-subheadline">바이러스 검사 우회, 토큰 만료 자동 갱신, 세그먼트 병렬 청크 다운로드 구현</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                100GB 이상의 오픈소스 LLM 가중치나 데이터셋을 구글 드라이브 링크로 내려받을 때 브라우저 멈춤, 쿠키 만료, 바이러스 스캔 확인 창 때문에 실패하는 일이 잦았습니다. Rust로 작성된 <code>gdirect</code>는 libaria2의 소켓 멀티플렉싱을 직접 제어하여 다운로드 실패 없는 극한의 속도를 실현했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> GDrive Share Link &rarr; Bypass Token Extraction &rarr; libaria2 Pinned Engine &rarr; 16-Segment Parallel Stream
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단일 스레드 브라우저 대비 8~12배 빠른 100MB/s 이상의 기가비트 대역폭을 온전히 활용할 수 있어 AI 연구자들 사이에서 필수 유틸리티로 급부상했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/mizorewww/gdirect" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: designfuchen/word-atlas -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 400개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.8시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 27.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;단어마다 그림 한 점, 어학의 지도를 밝히다&quot; : 7,298개 IELTS 인터랙티브 어휘 사전</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">designfuchen/word-atlas — 词光(Word Atlas): 어원 지식 그래프와 예술적 삽화로 빚은 시각 언어 사전</span>
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
          <h3 class="minor-detail-headline">텍스트 암기를 공간적 예술 경험으로 전환한 단어 아틀라스</h3>
          <div class="minor-detail-subheadline">WebGPU 기반 줌인/줌아웃 인터랙티브 캔버스에 펼쳐지는 7,000여 개 어휘의 시각적 그물망</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                단순 단어장 앱의 기계적 플래시카드 방식에서 벗어나, 생성형 AI와 디자이너의 협업으로 7,298개 어휘의 정밀한 의미를 고유 삽화와 어원적 연결고리로 시각화한 오픈소스 웹 애플리케이션입니다. 유려한 인터랙션 디자인으로 출시 반나절 만에 교육계와 프론트엔드 커뮤니티의 극찬을 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Lexical Knowledge Graph &rarr; Etymology Vector Embedding &rarr; WebGPU Infinite Canvas &rarr; Interactive Visual Recall
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                대규모 벡터 데이터와 고해상도 벡터 그래픽을 브라우저 메모리 병목 없이 60fps로 부드럽게 렌더링하는 가상화 뷰포트 아키텍처를 공개했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/designfuchen/word-atlas" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 7: mirkobrombin/raven -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 379개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 30.0시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.6 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;앱들이 진짜 윈도우로 착각하는 컨테이너&quot; : Bottles 창시자의 차세대 윈도우 런타임</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">mirkobrombin/raven — 리눅스/macOS 상에서 레거시 및 최신 윈도우 환경을 완벽 복제하는 마이크로 격리 계층</span>
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
          <h3 class="minor-detail-headline">와인(Wine)의 한계를 넘어선 차세대 호환성 플랫폼: Raven</h3>
          <div class="minor-detail-subheadline">프로세스 샌드박싱, 의존성 지연 주입, 네이티브 그래픽 브리지를 통합한 경량 런타임</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                리눅스 게이밍 및 윈도우 앱 구동의 대표 주자인 'Bottles'의 메인 개발자 Mirko Brombin이 기존 아키텍처의 부채를 청산하고 밑바닥부터 새로 설계한 <code>Raven</code>을 공개했습니다. 복잡한 접두사(Prefix) 설정 없이 앱이 요구하는 레지스트리와 DLL 환경을 즉각적으로 에뮬레이트합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Windows PE Binary &rarr; Micro-Registry Sandbox &rarr; Dynamic DXVK/VKD3D Bridge &rarr; Zero-Overhead Process Host
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                스팀 덱(Steam Deck) 및 ARM 기반 리눅스 하드웨어에서 윈도우 데스크톱 및 게임 소프트웨어의 구동 호환성을 비약적으로 끌어올렸습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/mirkobrombin/raven" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: KohakuBlueleaf/KohakUnlock -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 148개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.9시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;잠들어 있던 엔비디아 텐서 코어를 강제 각성시킨다&quot; : TU102 하드웨어 언락 리서치</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">KohakuBlueleaf/KohakUnlock — 튜링 및 암페어 GPU에서 인위적으로 제한된 텐서 연산 파이프라인 우회 해제</span>
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
          <h3 class="minor-detail-headline">소프트웨어로 엔비디아의 하드웨어 티어 차등을 허물다</h3>
          <div class="minor-detail-subheadline">마이크로코드 가드 초기화 역공학을 통한 소비자용 그래픽카드 텐서 처리량 35% 증대 연구</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                엔비디아는 소비자용 지포스 카드에서 기업용 쿼드로/테슬라와의 가격 차별화를 위해 특정 혼합 정밀도(FP16/INT8) 텐서 코어 클럭과 파이프라인을 펌웨어 수준에서 제한해 왔습니다. <code>KohakUnlock</code>은 GPU 초기화 시점의 레지스터 쓰기 가드를 패치하여 숨겨진 연산력을 끌어내는 개념 증명(PoC)을 제시했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> VBIOS Guard Analysis &rarr; TU102 MMIO Hook &rarr; Tensor Core Pipeline Throttling Bypass &rarr; +35% Inference Speedup
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                구형 RTX 2080 Ti 및 3090 사용자들에게 로컬 LLM 양자화 추론 속도를 무료로 업그레이드할 수 있는 가능성을 열어주며 하드웨어 해커들의 지지를 받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/KohakuBlueleaf/KohakUnlock" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: YoyoLin008/mcreplay -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 200개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 30.0시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;에이전트가 무슨 짓을 했는지 한 프레임씩 되돌려본다&quot; : MCP 리플레이 디버거</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">YoyoLin008/mcreplay — 구조적 스냅샷, 변경 리포트, 로컬 세션 인터랙션 타임머신 재현</span>
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
          <h3 class="minor-detail-headline">블랙박스였던 AI 에이전트의 실행 과정을 완벽 분해하다</h3>
          <div class="minor-detail-subheadline">MCP 프로토콜 메시지, 브라우저 클릭 이벤트, 파일 diff를 시간 순서대로 인터랙티브 재생</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                자율 에이전트가 코드베이스를 수정하다 에러가 터졌을 때, 수천 줄의 텍스트 로그만으로는 '어느 도구 호출 시점에 판단이 꼬였는지' 파악하기가 극도로 어렵습니다. <code>mcreplay</code>는 에이전트의 모든 행동을 게임 리플레이처럼 단계별로 되감고 재생하며 검증할 수 있는 로컬 웹 뷰어를 제공합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> MCP Tool Event Stream &rarr; Snapshot State Store &rarr; Differential AST Tracking &rarr; Interactive Timeline Scrubbing
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                에이전트 개발팀의 디버깅 시간을 획기적으로 줄여주며, 복잡한 다중 에이전트 협업 과정의 회귀 테스트 하네스로 자리매김하고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/YoyoLin008/mcreplay" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>
"""

print("GH Minors module loaded.")
