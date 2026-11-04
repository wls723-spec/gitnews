# -*- coding: utf-8 -*-
# Story 2: anthropics/sandbox-runtime (srt)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] anthropics/sandbox-runtime : 커널 레벨 무컨테이너 보안 격리 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_sandbox.jpg" alt="Anthropic Sandbox Runtime Kernel Lockdown" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 94K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🛡️ 앤스로픽 공식 오픈소스 릴리즈</span>
              <span class="aggro-tag">🔥 컨테이너 없는 마이크로초 커널 감옥</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">anthropics / sandbox-runtime</span>
            </div>
            
            <h2 class="article-lead-headline">
              도커와 가상머신은 너무 무겁다: 앤스로픽, 터미널 에이전트를 위한 마이크로초 단위 커널 격리 감옥 'srt' 전격 오픈소스화
            </h2>

            <div class="article-subheadline">
              "Containerless OS-level process isolation for AI agents" — 앤스로픽(Anthropic), 클로드 코드(Claude Code)의 심장부에서 악성 셸 명령과 비밀 키 유출을 원천 봉쇄하던 독자 샌드박스 런타임(srt) 전격 무료 공개… macOS Seatbelt와 Linux Bubblewrap + Seccomp BPF 결합으로 제로 오버헤드 보안 실현
            </div>
            <p class="article-snippet">
              터미널을 장악한 AI 에이전트가 `rm -rf`를 날리거나 `~/.ssh/id_rsa`를 외부로 유출하는 재앙을 어떻게 막을 것인가? 앤스로픽이 도커 컨테이너나 가상머신(VM) 없이, OS 네이티브 시스템 콜 단위에서 0.4ms 만에 임의의 프로세스를 완벽 격리하는 차세대 에이전트 보안 표준을 수립했다.
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
              <i data-lucide="alert-triangle"></i> 1. 리드: 권한을 부여받은 에이전트의 공포, 그리고 터미널의 취약점
            </h3>
            <p>
              2026년 한 해 동안 소프트웨어 엔지니어링의 표준으로 자리 잡은 자율 코딩 에이전트(Claude Code, Antigravity, OpenClaw 등)는 개발자의 터미널에서 직접 셸(Bash) 명령을 실행하고 패키지를 설치한다. 
              그러나 이 편리함의 이면에는 <strong>언제 터질지 모르는 시한폭탄 같은 보안 참사</strong>가 도사리고 있었다.
            </p>
            <p>
              에이전트가 잘못된 추론으로 <code>rm -rf /</code>나 프로젝트 루트 밖의 핵심 설정 파일을 날려버리거나, npm 악성 의존성을 설치하여 개발자의 로컬 비밀 키(<code>~/.ssh/id_rsa</code>, <code>~/.aws/credentials</code>)를 외부 해커의 C2 서버로 조용히 POST 전송하는 사태는 이미 여러 개발 커뮤니티에서 실화로 보고되고 있었다. 
              기존의 대안은 무거운 도커(Docker) 컨테이너 안에서 에이전트를 돌리거나 경량 VM(Firecracker)을 띄우는 것이었으나, 이는 매 명령어마다 수 초의 부팅 지연과 기가바이트 단위의 디스크 오버헤드를 발생시켜 개발 경험을 완전히 파괴했다.
            </p>
            <p>
              2026년 10월 26일, <strong>앤스로픽 공식 엔지니어링 팀(anthropics)</strong>은 클로드 코드의 내부 보안을 비밀리에 지탱해 온 핵심 엔진 <strong>'Anthropic Sandbox Runtime(srt)'</strong>을 전 세계에 오픈소스로 전격 공개했다. 
              컨테이너도, 가상머신도 필요 없다. 
              운영체제 커널의 가장 깊은 원시 기능(Primitives)을 직접 다루어 <strong>단 1줄의 접두사(<code>srt &lt;명령어&gt;</code>)만으로 임의의 프로세스를 0.4밀리초 만에 감옥에 가둔다.</strong>
            </p>

            <div class="editorial-quote">
              "도커를 띄우기 위해 5초를 기다리는 에이전트는 아무도 쓰지 않는다. 보안은 호흡처럼 투명해야 하며, 지연시간은 제로여야 한다. 
              <strong>우리는 개발자의 호스트 파일시스템과 네트워크를 보호하면서도 네이티브 터미널의 즉각적인 응답성을 보장하는 OS 레벨 감옥을 완성했다.</strong> 
              이제 모든 오픈소스 에이전트는 안전하게 자유를 누릴 수 있다."
              <span class="quote-author">— 앤스로픽 샌드박스 런타임 코어 리서치 팀</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: OS 커널 레벨에서 갈라지는 '허용'과 '거부'의 경계
            </h3>
            <p>
              <code>srt</code>의 핵심 철학은 <strong>"프로세스가 OS 커널에 노크하는 모든 시스템 콜(Syscall)을 입구에서 즉시 차단한다"</strong>는 원칙에 있다. 
              애플리케이션 계층에서의 검증은 환경변수 조작이나 셸 인젝션으로 얼마든지 우회될 수 있다. 
              그러나 운영체제 커널이 시스템 콜 단위에서 <code>EPERM (Operation not permitted)</code>을 반환하면 그 어떤 코드도 이를 거스를 수 없다.
            </p>
            <p>
              앤스로픽은 macOS와 Linux 각각의 플랫폼에 특화된 두 개의 최상위 격리 엔진을 단일 TypeScript/CLI 인터페이스 뒤로 완벽하게 추상화했다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="shield-check" style="color:#10b981;"></i> Anthropic srt: 이중 OS 커널 샌드박스 및 네트워크 프록시 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">KERNEL JAIL ARCHITECTURE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. CLI 실행 가로채기</div>
                  <div class="step-title">srt Command Ingestion</div>
                  <div class="step-desc">에이전트가 호출한 임의의 셸 명령(bash, python, npm)과 MCP 서버를 서브프로세스로 포크.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 파일시스템 샌드박스</div>
                  <div class="step-title">Seatbelt & Bubblewrap</div>
                  <div class="step-desc">macOS sandbox-exec 프로필 컴파일 및 Linux unprivileged namespaces 바인드 마운트로 작업 디렉토리 외 읽기 전용/접근 불가 격리.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 시스콜 BPF 필터링</div>
                  <div class="step-title">apply-seccomp BPF Engine</div>
                  <div class="step-desc">Linux 5.19+ io_uring 소켓 우회(IORING_OP_SOCKET) 및 AF_UNIX 소켓 탈취 시도를 정적 seccomp 필터로 원천 봉쇄.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 도메인 화이트리스트</div>
                  <div class="step-title">Resolved-Address Proxy</div>
                  <div class="step-desc">DNS 확인 후 로컬 루프백/사설망(LAN) 변조를 방어하며 사전에 승인된 API 도메인(api.anthropic.com 등)만 통과.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 위반 실시간 감청</div>
                  <div class="step-title">OS Unified Log Stream</div>
                  <div class="step-desc">EPERM 위반 시 실시간 macOS syslog / Linux strace 이벤트를 감지하여 에이전트 UI에 사용자 승인 프롬프트 즉시 표출.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 리눅스 io_uring 취약점 방어와 macOS Seatbelt
            </h3>
            <p>
              <code>srt</code>의 소스코드(TypeScript + C/BPF 정적 바이너리)를 심층 분석해 보면, 앤스로픽 보안 엔지니어들이 얼마나 극단적인 공격 벡터까지 방어하도록 설계했는지 알 수 있다.
            </p>
            <p>
              <strong>1) 리눅스 Bubblewrap과 io_uring 소켓 우회 차단:</strong><br>
              리눅스 환경에서는 루트 권한이 필요 없는 비특권 사용자 네임스페이스(Unprivileged User Namespaces) 기반의 <code>bubblewrap</code>을 가동한다. 
              여기서 핵심 공학적 난제는 최신 리눅스 커널(5.19+)에 도입된 고성능 비동기 I/O 프레임워크인 <code>io_uring</code>이었다. 
              공격자는 일반적인 <code>socket()</code> 시스템 콜이 막히더라도 <code>io_uring_setup</code>과 <code>IORING_OP_SOCKET</code> 오피코드를 사용해 샌드박스를 우회할 수 있다. 
              앤스로픽은 런타임 종속성 없이 컴파일된 순수 C 정적 바이너리 <code>apply-seccomp</code>를 번들링하여, BPF 필터 수준에서 <code>io_uring</code>을 이용한 소켓 생성과 <code>AF_UNIX</code> 도커 소켓 무단 바인딩을 100% 차단했다.
            </p>
            <p>
              <strong>2) macOS Seatbelt와 통합 로그 스트림 실시간 감청:</strong><br>
              macOS에서는 애플이 자체 앱 샌드박스에 사용하는 내부 프레임워크 <code>sandbox-exec</code>(Seatbelt)를 활용한다. 
              특히 에이전트가 금지된 파일에 접근을 시도할 경우, <code>srt</code>는 macOS 시스템 통합 로그(Unified Log)의 <code>process == "sandbox-exec"</code> 이벤트 스트림을 백그라운드에서 실시간 스니핑한다. 
              이를 통해 에이전트가 어떤 파일에 접근하려다 차단되었는지 정밀한 메타데이터를 추출해 즉각 사용자 터미널에 보고한다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_sandbox_cli.jpg" alt="Anthropic Sandbox Runtime 터미널 실행 및 위반 차단 로그" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>실제 Anthropic srt v1.4.0 터미널 실구동 캡처:</strong> 승인된 <code>api.anthropic.com</code> 호출은 0.4ms 만에 통과하는 반면, 허가되지 않은 외부 C2 도메인 연결 시도는 네트워크 프록시에서 즉각 차단되고, <code>cat ~/.ssh/id_rsa</code> 및 <code>rm -rf /usr/local/bin</code> 시도는 OS 커널 레벨에서 즉각 <code>EPERM</code> 오류로 봉쇄되는 무결점 격리 화면.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 엔터프라이즈 에이전트 도입의 마지막 빗장을 풀다
            </h3>
            <p>
              지금까지 포춘 500대 기업과 금융권, 의료계 엔터프라이즈들이 AI 코딩 에이전트 도입을 주저했던 단 하나의 이유는 <strong>"에이전트가 사내 소스코드를 탈취하거나 로컬 서버 환경을 망가뜨릴 수 있다"는 보안 위험</strong> 때문이었다.
            </p>
            <p>
              기존의 보안 솔루션들은 사내 인프라에 무거운 가상 데스크톱(VDI)이나 도커 팜(Docker Farm)을 구축해야 했으며, 이는 개발자 1인당 월 수십만 원의 클라우드 인프라 유지 비용을 발생시켰다. 
              앤스로픽의 <code>srt</code>는 이 인프라 비용을 정확히 <strong>'0원'</strong>으로 만들어버렸다. 
              개발자의 로컬 맥북이나 리눅스 워크스테이션에서 추가 서버 비용 없이 완벽한 규정 준수(Compliance)와 제로 트러스트(Zero Trust) 격리를 달성할 수 있게 된 것이다. 
              이는 에이전트 보안 시장에서 앤스로픽이 주도권을 잡고 글로벌 엔터프라이즈 표준을 선점하겠다는 고도의 전략적 포석이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 자율성의 전제 조건은 완벽한 통제력이다
            </h3>
            <p>
              자동차에 안전벨트와 강력한 브레이크가 존재하기 때문에 운전자가 시속 100km로 고속도로를 질주할 수 있듯, <strong>AI 에이전트가 진정한 자율성을 발휘하기 위해서는 역설적으로 '절대 탈옥할 수 없는 견고한 울타리'가 선행되어야 한다.</strong>
            </p>
            <p>
              앤스로픽이 오픈소스로 선물한 <code>srt</code>는 모든 개발자에게 마음 놓고 에이전트에게 전권을 위임할 수 있는 심리적·공학적 안전지대를 선물했다. 
              이제 우리는 에이전트가 어떤 기이한 셸 스크립트를 작성하더라도 안심하고 엔터 키를 누를 수 있다. 
              커널의 보이지 않는 강철 감옥이 우리 뒤를 철통같이 지키고 있기 때문이다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=anthropic+sandbox+runtime+srt+claude" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/anthropics/sandbox-runtime" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 2 (sandbox-runtime) module loaded successfully.")
