# -*- coding: utf-8 -*-
# Story 4: makepad/relax

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] makepad/relax                                    -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_relax.jpg" alt="Relax JIT Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> INSTANT RUST</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#d97706; color:#92400e;">⚡ 러스트 컴파일 지옥 탈출</span>
              <span class="platform-tag">GitHub Trending & makepad.github.io</span>
              <span class="platform-tag">makepad / relax</span>
            </div>
            
            <h2 class="article-headline">
              10년 묵은 러스트(Rust) 컴파일 지옥을 끝낸다: Makepad의 'Relax' JIT 컴파일러 — 핫 리로딩 0.1초, 개발자 생산성의 성배
            </h2>

            <div class="article-subheadline">
              rustc와 LLVM의 거대한 링커 대기 시간을 전면 우회하고, Cargo 패키지 소스를 메모리에서 즉시 기계어로 실행하는 순수 Rust 작성 초고속 라이브 JIT 런타임
            </div>
            <p class="article-snippet">
              메모리 안전성과 최고의 실행 속도로 현대 시스템 프로그래밍의 왕좌에 오른 러스트(Rust)지만, 개발자들을 끊임없이 괴롭혀온 유일한 아킬레스건은 바로 '극악의 컴파일 속도'였습니다. 코드 한 줄을 수정하고 결과를 확인하기 위해 수십 초씩 기다려야 했던 이 지옥 같은 루프를 깨부수기 위해, 고성능 GUI 프레임워크 Makepad 팀이 rustc와 LLVM 링커를 완전히 건너뛰고 소스 코드를 메모리에서 0.1초 만에 직접 기계어로 실행하는 라이브 JIT 컴파일러 'Relax'를 공개했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "컴파일 버튼을 누르고 커피를 타러 가는 시대는 끝났다"
            </h3>
            <p>
              러스트 개발자들의 오랜 자조 섞인 밈이 있다: <em>"컴파일 중입니다(Compiling...)"</em>라는 핑계로 하루 업무 시간의 3분의 1을 멍하니 허비한다는 것이다. 
              정교한 빌림 검사기(Borrow Checker)와 거대한 모노모피제이션(Monomorphization), 그리고 LLVM 백엔드의 심층 최적화 파이프라인은 결과물의 속도를 보장하는 대신 개발자의 인지 흐름(Flow State)을 산산조각 내왔다.
            </p>
            <p>
              러스트가 역사적인 100번째 마이너 릴리즈(Rust 1.100.0)에 도달한 바로 지금, 시스템 프로그래밍 생태계의 패러다임을 뿌리째 뒤흔들 프로젝트가 베일을 벗었다. 
              <strong>Relax(릴랙스)</strong>는 이름 그대로 개발자에게 "이제 긴장을 풀고 마음껏 코드를 치라"고 선언한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '실행하면서 빌드하는' 러스트의 새로운 차원
            </h3>
            <p>
              Relax의 설계 철학은 기존의 관행을 180도 전복한다:
            </p>

            <div class="editorial-quote">
              <p>
                "전통적인 rustc는 당신의 프로그램을 완전히 빌드한 뒤에야 실행합니다. 
                <strong>하지만 Relax는 당신의 프로그램을 빌드하면서 '동시에' 즉각 실행합니다.</strong> 
                rustc도 없고, LLVM도 없으며, 시스템 링커도 거치지 않습니다. Cargo.toml이 있는 디렉토리에서 소스 코드를 타이핑하고 저장하는 순간, 
                0.1초 만에 메모리 상에서 네이티브 x86-64 및 ARM64 기계어가 합성되어 화면에 결과가 튀어나옵니다."
              </p>
              <small>— Rik Arends, Makepad 수석 아키텍트 겸 Relax 프로젝트 창립자</small>
            </div>

            <p>
              릴리즈 배포용 최종 빌드는 여전히 `cargo build --release`로 완벽한 최적화를 적용하되, 일상의 반복적인 개발, UI 튜닝, 단위 테스트 검증 단계에서는 
              Relax의 라이브 JIT(Just-In-Time) 런타임을 통해 파이썬이나 자바스크립트 수준의 초고속 피드백 루프를 달성한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: No-LLVM 단일 패스 코드 생성과 메모리 내 함수 핫 스와핑
            </h3>
            <p>
              Relax가 밀리초 단위의 핫 리로딩을 실현한 기술적 메커니즘은 다음과 같다:
            </p>
            <ul>
              <li><strong>Custom In-Memory Parser & Type Resolver:</strong> 무거운 rustc 프론트엔드를 거치지 않고, 러스트 소스 코드를 즉시 메모리 AST(추상 구문 트리)로 파싱하여 필수적인 타입 정보만을 고속 추출.</li>
              <li><strong>Direct-to-Machine Single-Pass Codegen:</strong> 중간 표현(LLVM IR)을 생성하고 최적화 패스를 20번씩 돌리는 병목을 완전히 제거. x86-64 및 Apple Silicon(ARM64) 명령어 바이트스트림을 단일 패스로 메모리에 직접 작성.</li>
              <li><strong>Fine-Grained Function Hot-Swapping:</strong> 파일 전체를 다시 링크하는 대신, 변경된 함수의 메모리 주소(포인터)만을 원자적(Atomic)으로 치환하여 프로그램이 실행 중인 상태에서도 UI 상태나 변수 데이터를 보존한 채 로직만 실시간 갱신.</li>
              <li><strong>Cargo Dependency Pre-caching:</strong> 외부 크레이트(Dependencies)는 최초 1회만 고속 캐싱하고, 사용자 애플리케이션 코드만 차분 감지하여 재컴파일.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Relax vs Traditional Rustc 파이프라인 비교</span>
                <span class="schematic-badge">0.1s Zero-Wait Architecture</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Traditional Rustc Build</div>
                  <div class="schematic-desc">
                    Source Code &rarr; AST &rarr; HIR &rarr; MIR<br>
                    LLVM IR Generation (Heavy)<br>
                    LLVM Optimization &amp; System Linker<br>
                    대기 시간: 25초 ~ 3분 (루프 마비)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Relax Live JIT Runtime</div>
                  <div class="schematic-desc">
                    Direct AST Parsing in Memory<br>
                    Single-Pass Native Machine Codegen<br>
                    In-Memory Function Pointer Patching<br>
                    반영 시간: 0.1초 미만 (즉각 확인)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Production Release</div>
                  <div class="schematic-desc">
                    개발 중: Relax로 초고속 바이브 코딩<br>
                    최종 출시: `cargo build --release`<br>
                    최고의 생산성 + 최고의 런타임 속도<br>
                    두 마리 토끼 완전 포섭
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Relax 공식 웹 기술 문서 및 라이브 JIT 아키텍처 뷰</span>
              </div>
              <img src="../assets/images/demo_relax.png" alt="Relax Live Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ makepad.github.io/relax 공식 문서 포털 뷰: "Rust without the wait. rustc builds your program, then you run it. Relax runs your program while it builds it." LLVM과 링커 없이 메모리에서 소스를 즉시 기계어로 구동하는 아키텍처 명세 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: 엔터프라이즈의 러스트 전면 전환을 가로막던 마지막 장애물 제거
            </h3>
            <p>
              그동안 수많은 기업의 엔지니어링 리더들은 메모리 보안과 성능을 위해 C/C++이나 Go 대신 러스트를 도입하고 싶어 했지만, 
              "개발 주기가 너무 느려져서 타임 투 마켓(Time to Market) 경쟁에서 뒤처진다"는 시니어 엔지니어들의 거센 반대에 부딪혀왔다.
            </p>
            <p>
              Relax의 출현은 이 마지막 반대 논거를 완전히 무력화한다. 개발 단계에서는 스크립트 언어처럼 즉각 수정하고 확인하면서, 
              프로덕션 배포 시점에는 세계에서 가장 안전하고 빠른 정적 네이티브 바이너리를 생산할 수 있게 되었기 때문이다. 
              이는 러스트가 게임 엔진 개발, GUI 데스크톱 클라이언트, 실시간 오디오 처리 등 고도의 인터랙티브 분야로 침투하는 기폭제가 될 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 기다림이 사라진 자리, 순수한 창작의 몰입
            </h3>
            <p>
              도구의 지연 시간이 0.1초 이하로 줄어드는 순간, 인간의 두뇌는 도구와의 경계를 잊고 직관의 속도로 생각하기 시작한다.
            </p>
            <p>
              Relax가 열어젖힌 '기다림 없는 러스트'의 세계는, 개발자가 기계의 속도에 맞춰 인내하던 시대를 끝내고 기계가 온전히 인간의 사고 속도에 복종하는 프로그래밍의 미래를 예고하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Makepad+Relax+Rust+JIT+compiler+demo" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://makepad.github.io/relax/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> Relax 공식 문서
              </a>
              <a href="https://github.com/makepad/relax" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
