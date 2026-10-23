# -*- coding: utf-8 -*-
# Story 2: NVIDIA OpenShell

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] NVIDIA/OpenShell : 엔비디아의 에이전트 소버린 OS -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openshell.jpg" alt="NVIDIA OpenShell Sovereign Agent Runtime" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 89K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🛡️ 엔비디아 공식 릴리즈 · 커널 보안 혁명</span>
              <span class="platform-tag">GitHub Trending Rust · Hacker News</span>
              <span class="platform-tag">NVIDIA / OpenShell</span>
            </div>
            
            <h2 class="article-headline">
              엔비디아가 공개한 에이전트 전용 소버린 OS: 커널 레벨 eBPF 샌드박스와 정형 검증 보안 런타임 'OpenShell'
            </h2>

            <div class="article-subheadline">
              "The safe, private runtime for fleets of autonomous AI agents" — 컴퓨터 화면과 셸을 쥐고 자율 행동하는 AI 에이전트 편대의 무차별 시스템 침투와 데이터 탈취를 어떻게 통제할 것인가… 엔비디아, 리눅스 커널 심층 계측(eBPF)과 Z3 수학적 정형 검증(Formal Verification)을 결합한 오픈소스 런타임 전격 공개 (+1.7만 스타)
            </div>
            <p class="article-snippet">
              터미널과 운영체제 전권을 쥔 에이전트의 위험천만한 폭주를 차단하기 위해 탄생한 차세대 보안 런타임. 에이전트마다 cgroups v2 기반의 격리 샌드박스를 부여하고, 정책 변경 시 Z3 수리논리 검증기로 안전성을 수학적으로 증명한 뒤 142개 시스템 콜을 실시간 감시한다.
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
              <i data-lucide="shield-alert"></i> 1. 컴퓨터 유즈의 공포: 에이전트에게 루트 권한을 맡길 수 있는가
            </h3>
            <p>
              2026년 하반기, AI 에이전트는 이미 단순한 채팅 창을 넘어섰다. 
              앤스로픽의 클로드 3.5 소넷 컴퓨터 유즈(Computer Use), 오픈AI의 오퍼레이터(Operator), 코딩 에이전트 클로드 코드(Claude Code)와 데빈(Devin)은 이제 인간 개발자처럼 터미널에 명령어를 입력하고, 로컬 디스크의 설정 파일을 고치며, 프로덕션 서버에 직접 SSH 접속을 시도한다.
            </p>
            <p>
              하지만 엔터프라이즈 보안 책임자(CISO)들에게 이는 끔찍한 악몽이다. 
              에이전트가 프롬프트 인젝션(Prompt Injection) 공격을 받거나 환각(Hallucination)에 빠져 <code>/etc/shadow</code> 계정 파일을 외부로 유출하거나, <code>rm -rf /</code> 같은 재앙적인 명령을 실행할 가능성을 배제할 수 없기 때문이다. 
              기존의 도커(Docker) 컨테이너나 가상머신은 정적인 서버용으로 설계되었을 뿐, 실시간으로 결정을 바꾸며 움직이는 수십 마리의 자율 에이전트 편대를 미세하게 감시하기에는 너무 무겁고 둔탁했다. 
              이 치명적인 안보 공백에 하드웨어 제국 <strong>엔비디아(NVIDIA)</strong>가 마침내 오픈소스 하이퍼바이저 <strong>OpenShell(NVIDIA/OpenShell)</strong>을 들고 등판했다.
            </p>

            <div class="editorial-quote">
              "AI 에이전트가 실질적인 업무를 수행하려면 필연적으로 파일 시스템과 네트워크 소켓에 접근해야 합니다. 
              그러나 전통적인 OS 권한 모델(POSIX)은 '이 프로세스를 실행하는 주체가 변덕스러운 확률론적 신경망'이라는 사실을 전혀 고려하지 않고 만들어졌습니다. 
              <strong>OpenShell은 에이전트가 내리는 모든 판단을 리눅스 커널의 최하단(eBPF)에서 물리적으로 포획하고, 정책의 안전성을 수학적 공리계로 먼저 입증한 뒤에만 시스템 콜을 허용합니다.</strong>"
              <span class="quote-author">— 엔비디아 AI 시스템 아키텍처 연구팀, OpenShell 기술 백서</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 엔비디아가 'AI 운영체제' 계층을 겨냥하는 이유
            </h3>
            <p>
              엔비디아가 GPU 칩셋 회사를 넘어 소프트웨어 생태계를 집어삼키는 방식은 언제나 동일했다. 
              CUDA로 딥러닝 컴파일러를 장악했듯, 이제는 수백만 대의 서버에서 자율 구동될 <strong>'에이전트 인프라 런타임 계층'</strong>을 선점하려는 것이다.
            </p>
            <p>
              OpenShell은 러스트(Rust)로 정밀하게 작성된 초경량 게이트웨이와 슈퍼바이저 아키텍처를 취한다. 
              개별 AI 에이전트가 생성되는 즉시 0.01초 만에 격리된 cgroups v2 네임스페이스와 읽기 전용(RO) 가상 파일시스템 샌드박스를 형성하고, 142개 주요 리눅스 시스템 콜을 실시간으로 가로채는 eBPF 프로브를 활성화한다. 
              에이전트가 아무리 정교한 사회공학적 기만술이나 탈옥(Jailbreak) 프롬프트를 시도하더라도, 커널 계층의 하드웨어 트랩에 걸려 즉각 무력화되는 구조다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="cpu" style="color:#10b981;"></i> NVIDIA OpenShell: 커널 레벨 eBPF 심층 감시 및 정형 검증 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">SECURITY RUNTIME ARCHITECTURE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 에이전트 명령 수신</div>
                  <div class="step-title">Autonomous Agent Call</div>
                  <div class="step-desc">자율 AI 에이전트(Claude Code, Codex 등)가 셸 터미널에서 파일 읽기/쓰기, 패키지 설치 명령을 요청.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 수리논리 정형 검증</div>
                  <div class="step-title">Z3 Formal Verification</div>
                  <div class="step-desc">정책 변경(Policy Definition) 발생 시 Z3 정리 증명기(Theorem Prover)가 0.04초 만에 보안 불변 조건을 수학적으로 증명.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 커널 eBPF 가로채기</div>
                  <div class="step-title">142 Syscall Probes</div>
                  <div class="step-desc">리눅스 커널 내부의 kprobes/tracepoints에 eBPF 프로그램을 결합하여 connect, openat, ptrace 호출을 0ns 지연으로 가로챔.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 샌드박스 봉쇄</div>
                  <div class="step-title">cgroups v2 & RO VFS</div>
                  <div class="step-desc">민감 경로(/etc/shadow, ~/.ssh) 접근 시 즉시 BLOCKED 처리하고, 허가된 임시 작업 디렉토리만 가상화 투영.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 안전한 실행 및 감사</div>
                  <div class="step-title">Live Policy Telemetry</div>
                  <div class="step-desc">모든 시스템 상호작용을 위변조 불가능한 감사 로그로 기록하며, Docker, Podman, K8s 클러스터와 네이티브 연동.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="binary"></i> 3. 기술 메커니즘 해부: Z3 정형 증명과 0오버헤드 eBPF 하이퍼바이저
            </h3>
            <p>
              OpenShell의 핵심 차별화 요소는 <strong>'정형 검증(Formal Verification)'</strong>과 <strong>'커널 eBPF 계측'</strong>의 융합에 있다:
            </p>
            <p>
              첫째, <strong>Z3 증명기를 통한 정책 무결성 검증</strong>이다. 엔터프라이즈 환경에서 보안 정책 파일(<code>*.nopol</code>)이 복잡해지면, 관리자가 의도치 않게 구멍을 뚫는 '정책 모순(Policy Contradiction)'이 발생한다. OpenShell은 정책 컴파일 시 마이크로소프트 리서치의 SMT 솔버인 Z3를 호출하여, "어떤 에이전트 상태에서도 외부 미승인 IP로의 원시 패킷 전송이 도달 불가능함(Unreachable)"을 수학적으로 증명한다. 이 수학적 증명이 통과되지 않으면 런타임 자체가 기동되지 않는다.
            </p>
            <p>
              둘째, <strong>syscall_monitor.o eBPF 드라이버</strong>다. 기존의 <code>ptrace</code> 기반 보안 솔루션은 시스템 콜마다 프로세스 컨텍스트 스위칭이 발생해 성능이 최대 80%까지 급락했다. OpenShell은 리눅스 커널 링0(Ring 0) 공간에서 실행되는 eBPF 바이트코드를 활용하여, 유저스페이스 전환 없이 커널 메모리 단에서 142개 시스템 콜의 인자(Arguments)를 검사하고 허용/차단을 결정한다. 지연 시간 오버헤드는 1% 미만에 불과하다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_openshell_cli.jpg" alt="NVIDIA OpenShell 터미널 CLI 구동 및 eBPF 정형 검증 실행 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>NVIDIA OpenShell v0.9.3 실구동 터미널 캡처:</strong> sovereign-agent 프로필로 런타임을 초기화하고 Z3 정리 증명기(Z3 Proof Engine: PASSED [0.04s])가 정책 안전성을 입증한 모습. 하단 실시간 스트림에서 rogue 에이전트의 <code>/etc/shadow</code> 접근과 원시 소켓 생성이 커널 레벨에서 즉각 BLOCKED 처리됨.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="trending-up"></i> 4. 비즈니스 해자: 엔터프라이즈 소버린 AI의 새로운 관문
            </h3>
            <p>
              지금까지 오픈소스 진영의 에이전트 프레임워크들은 '어떻게 똑똑하게 문제를 풀 것인가'에만 매몰되어 있었다. 
              그러나 포춘 500대 기업들이 수천억 원의 예산을 집행하며 자율 에이전트를 도입하지 못했던 유일한 병목은 '안전성과 규제 준수(Compliance)'였다.
            </p>
            <p>
              엔비디아는 OpenShell을 아파치 2.0 라이선스로 전격 공개함으로써, 기업들이 폐쇄형 독점 클라우드 에이전트 서비스에 종속되지 않고 <strong>온프레미스 사내 인프라에서 자율 에이전트 편대를 안전하게 굴릴 수 있는 소버린(Sovereign) 표준</strong>을 제시했다. 
              이는 에이전트를 굴리기 위한 고성능 H100/B200 GPU 서버 판매를 가속화하는 동시에, 에이전트 인프라의 사실상 표준(De-facto Standard) 하이퍼바이저 자리를 굳히려는 고도의 플랫폼 전략이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 자율성의 시대, 신뢰를 담보하는 커널의 방패
            </h3>
            <p>
              인공지능 에이전트에게 더 많은 자유와 권능을 줄수록, 그 자유를 담보할 시스템의 울타리는 더 차갑고 단단해야 한다. 
              OpenShell이 보여준 비전은 인공지능의 지능을 억압하는 통제가 아니라, <strong>수학적 증명과 커널의 엄격함으로 에이전트의 잠재력을 세상 밖으로 해방시키는 새로운 신뢰 인프라</strong>의 시작이다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=nvidia+openshell+agent+runtime" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/NVIDIA/OpenShell" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 2 ready.")
