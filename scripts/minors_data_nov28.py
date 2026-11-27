# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-28

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
          직전 발행(11월 27일) 이후 30시간 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 관심 증가율(Velocity) 순으로 엄선·클러스터링한 상호 고유 프로젝트 18선입니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: Slaktarn700/SlaktarnVI (VIctory / Console-to-PC Wave Cluster) -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 160개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.33 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Linux Proton·AMD RX 9070 XT·PS5 패치·전용 런처까지 폭발한 GTA 6 정적 호환 포크 생태계&quot; : SlaktarnVI (+파생 클러스터)</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Slaktarn700/SlaktarnVI — 게임 파일 0바이트로 Xbox Series 빌드를 Linux Proton·RDNA4 GPU에 최적화한 포크와 dazacode/vilauncher(★311)·ZiZc3/VI-Patch(★302) 등 11개 파생 프로젝트 통합 (GPL-3.0)</span>
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
            <h3 class="minor-detail-headline">단일 Windows 포크를 넘어 Linux Proton, PS5 ELF 패치, Apple Silicon Metal, DLSS/FSR 튜닝으로 분화한 차세대 콘솔 호환 레이어 물결</h3>
            <div class="minor-detail-subheadline">GPL-3.0 · Rust/C · 게임 에셋 0바이트 · FSR 4 Quality 1440p 19~25fps 실측 (11개 파생 포크 통합 클러스터)</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경 &amp; 파생 생태계)</div>
                <p class="minor-paragraph">
                  최근 공개된 순수 Rust Xbox Series 호환 레이어(VIctory)를 기점으로 지난 30시간 사이 GPU·OS·플랫폼별 파생 프로젝트가 동시다발로 폭발했습니다. 최고 속도(19.33★/h)를 기록한 <strong><code>Slaktarn700/SlaktarnVI</code></strong>는 Linux Proton 환경과 AMD Radeon RX 9070 XT(FSR 4 Quality, 1440p)에 맞춰 정점 버퍼·동적 디스크립터 고갈(3fps 저하)·식생 팝인 버그를 수정했습니다. 동일 물결의 통합 런처 <code>dazacode/vilauncher</code>(★311), PS5 패치 <code>ZiZc3/VI-Patch</code>(★302), NVIDIA 실험 포크 <code>rorodev6/victory-nvidia-megafork</code>(★202)·<code>Spaghetih/victory-sley-fork</code>(★150)·<code>ToLIManl/VIctory-Hydra</code>(★47)·<code>clankenjoyer/scarlet-fps</code>(★29)·<code>VIctoryUnified-DLSS</code>·<code>Tequesta</code>·<code>Arctory-Xe</code>·<code>M1LK</code>·Apple Silicon Metal 포트 <code>rustory-vi</code>까지 거대한 커뮤니티 생태계를 형성하고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[멀티 플랫폼 분화]</strong> Legal Console Build &rarr; Rust D3D12.X / Shader Translator &rarr; Linux Proton (SlaktarnVI) &middot; NVIDIA DLSS/FSR &middot; Apple Metal &middot; PS5 ELF Patch
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  저작권 파일이나 바이너리를 1바이트도 배포하지 않고 순수 번역 레이어와 셰이더 패치 코드만 오픈소스(GPL-3.0)로 공유하며, GPU 벤더별 병목과 드라이버 버그를 크라우드소싱으로 하루 단위로 해결하는 현대 리버스 엔지니어링 협업 모델을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Slaktarn700/SlaktarnVI" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> SlaktarnVI 저장소
              </a>
              <a href="https://github.com/dazacode/vilauncher" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> VILauncher (★311)
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: Jokudneh/mcp-sentinel -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 13개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.67 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;외부 의존성 0개 TypeScript로 MCP 서버 입출력을 감시·마스킹하는 로컬 보안 방화벽&quot; : mcp-sentinel</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Jokudneh/mcp-sentinel — MCP 에이전트 stdio 파이프를 투명하게 가로채 시크릿 자동 마스킹·정책 차단·JSONL 블랙박스 기록을 수행하는 보안 프록시 (MIT)</span>
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
            <h3 class="minor-detail-headline">에이전트가 외부 MCP 서버에 API 키를 흘리거나 위험한 도구를 호출하지 못하도록 중간에서 막아서는 투명 stdio 게이트웨이</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Node >= 20 · 런타임 외부 의존성 0개 · Strict TypeScript · JSONL Flight Recorder</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 코딩 도구의 스킬·MCP 플러그인들이 사전 고지 없이 데이터를 외부로 보내거나 숨겨진 지침을 주입하는 보안 이슈가 연달아 터지자, MCP 클라이언트와 서버 사이의 표준 입출력(stdio) 스트림에 끼워 넣어 모든 JSON-RPC 호출을 검사·차단하고 민감 키를 가려주는 초경량 방화벽이 즉시 주목받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[투명 stdio 방화벽]</strong> AI Client &harr; mcp-sentinel (Secret Redactor + Policy Gate + JSONL Flight Recorder) &harr; MCP Server
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  런타임 외부 npm 의존성이 단 0개여서 공급망 오염 우려 없이 안심하고 감사(Audit)할 수 있으며, 모든 도구 실행 내역이 JSONL 비행 기록장치로 남아 사후 보안 추적이 가능합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Jokudneh/mcp-sentinel" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: Jokudneh/Tws -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 18개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.04 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;흩어진 tmux·Rex 터미널 세션을 작업 스레드 단위로 묶어 관리하는 Rust TUI&quot; : tws</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Jokudneh/Tws — 평면적이고 휘발성인 터미널 세션을 auth-refactor·bug-1234 같은 영구 스레드로 구조화해 핀 고정·즉시 전환을 지원하는 워크스페이스 매니저 (MIT)</span>
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
            <h3 class="minor-detail-headline">여러 AI 코딩 에이전트와 서버 작업을 동시에 돌리는 개발자를 위한 스레드 기반 tmux·Rex 세션 오거나이저</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust · Rex / tmux 듀얼 백엔드 · ~/.config/tws/ 영속 저장 · Cmd+S 팝업 전환</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Claude Code, Codex CLI, 빌드 워처, 테스트 러너를 동시에 수십 개 창으로 띄워두다 보면 <code>tmux ls</code> 목록이 순식간에 난장판이 됩니다. <code>tws</code>는 기존 세션 위에 가벼운 스레드(Thread) 계층을 얹어 기능별·이슈별로 터미널 세션을 묶어두고 단축키로 오갈 수 있게 해 8.8시간 만에 18스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[스레드 세션 계층]</strong> ~/.config/tws/ (Threads: feature / bug / scratch) &rarr; Bind Live tmux or Rex Sessions &rarr; Instant Cmd+S Popup Switch
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  자체 터미널 에뮬레이터를 새로 짜는 대신 표준 <code>tmux</code>와 <code>Rex</code> 런타임을 그대로 백엔드로 활용하면서 조직화 UI만 Rust TUI로 분리해 기존 워크플로우에 마찰 없이 스며듭니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Jokudneh/Tws" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: Arekejoker/sprite-turntable -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 218개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.20 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;정면 캐릭터 시트 한 장으로 72프레임 360도 투명 턴테이블과 오프라인 HTML 뷰어를 뽑아낸다&quot; : Sprite Turntable</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Arekejoker/sprite-turntable — 단일 원화에서 640×1920 8비트 직통 투명 RGBA PNG 72장 시퀀스와 브라우저 드래그·줌 오프라인 인터랙티브 페이지를 생성하는 파이프라인 (MIT)</span>
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
            <h3 class="minor-detail-headline">2D 게임·버튜버·캐릭터 아트 제작을 위해 단 1장의 정면 설정화에서 60fps 360도 회전 스프라이트 시퀀스를 자동 제작</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python · 72프레임 (640×1920 RGBA PNG) · 42.5 MiB 단일 오프라인 HTML 쇼케이스</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI로 캐릭터 정면 시트를 뽑은 뒤에도 일관된 360도 턴테이블(전후좌우 72각도)과 깔끔한 알파 채널(누끼)을 얻는 일은 게임 아트 현장의 난제였습니다. 이 프로젝트는 원화에서 72프레임 투명 시퀀스를 뽑는 전체 제작 파이프라인과 즉시 드래그 회전해 볼 수 있는 단일 오프라인 HTML(<code>AGENTS.md</code> 협업 구조 포함)을 공개해 19시간 만에 ★218을 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[360° 턴테이블 파이프라인]</strong> Single Character Sheet &rarr; 72-Frame Orbit Synthesis &rarr; Alpha Straight-RGBA PNGs (640&times;1920) &rarr; Offline HTML5 Viewer
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  서버나 3D 엔진을 설치하지 않고도 단일 HTML 파일 안에서 72장의 고해상도 투명 프레임을 부드럽게 스크러빙·줌 검증할 수 있어 인디 게임과 일러스트 파이프라인의 검수 시간을 대폭 줄입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Arekejoker/sprite-turntable" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: Violiate/Omnipush -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 7개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.59 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;22개 메신저 채널·메일 AI 요약·Claude Code 스마트폰 원격 승인 안전잠금까지 통합한 푸시 허브&quot; : OmniPush</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Violiate/Omnipush — 공인 IP 없이 메신저 답장으로 로컬 코딩 에이전트를 원격 승인·제어하고 7개 MCP 안전 잠금 툴을 제공하는 셀프호스트 중추 (MIT)</span>
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
            <h3 class="minor-detail-headline">자율 코딩 에이전트가 위험한 명령을 실행하려 할 때 외출 중인 개발자 스마트폰으로 Human-in-the-Loop 승인을 묻는 NAT-Free 허브</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python 3.10+ · 22개 알림 채널 · 6개 NAT-Free 브리지 · 7개 MCP 툴 + 안전 잠금</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  밤새 AI 코딩 에이전트나 GPU 학습 스크립트를 돌려놓고 외출했을 때, 중간에 권한 승인을 기다리며 멈춰 있거나 오류로 죽어 있는 경우가 허다합니다. OmniPush는 텔레그램·위챗·Feishu·Bark·이메일 등 22개 채널과 인바운드 브리지를 연결해 폰에서 답장만으로 에이전트에 승인 신호를 보내고, 내장 SMTP 릴레이와 웹페이지·GPU 감시까지 처리합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[Human-in-the-Loop 제어]</strong> Local Agent (MCP Safety Lock) &harr; NAT-Free Bridge &harr; 22 Messenger Channels (Phone Approve/Deny)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  포트포워딩이나 공인 IP 개방 없이도 로컬 머신의 Claude Code·Cursor와 모바일 메신저를 양방향으로 이어주며, 무인 자동화의 가장 큰 불안 요소인 '위험 명령 사후 통제'를 실용적으로 구현했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Violiate/Omnipush" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: tomDeprez/Tor6IA -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 4개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.28 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;내 GPU로 남의 LLM 추론을 도와 크레딧을 쌓고, 내 PC보다 거대한 오픈 모델을 종단간 암호화로 돌린다&quot; : Tor6IA</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">tomDeprez/Tor6IA — Ollama 기반으로 단일 바이너리 설치·공개 서명 원장·OpenAI 호환 API를 제공하는 P2P 오픈 LLM 공유 네트워크 (MIT)</span>
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
            <h3 class="minor-detail-headline">유휴 시간대 로컬 GPU를 P2P 풀에 공유해 크레딧을 얻고 대형 모델 추론에 쓰는 Ollama 기반 품앗이 네트워크</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Go · 단일 파일 설치 · E2E 암호화 · 공개 서명 원장 · OpenAI 호환 API</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  70B~400B급 대형 오픈웨이트 모델을 돌리려면 가정용 GPU 한두 장으로는 VRAM이 부족하지만, 그렇다고 매달 API 요금을 내기엔 부담스럽습니다. Tor6IA는 회원가입이나 신용카드 없이 단일 Go 실행 파일로 내 Ollama 유휴 자원을 제공하고 크레딧을 벌어, 더 큰 GPU를 가진 피어의 모델에 종단간 암호화된 OpenAI 호환 질의를 보냅니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[P2P 추론 교환]</strong> Idle Local Ollama Node &rarr; Earn Credits (Signed Public Ledger) &rarr; E2EE Query to Large Remote Peer (OpenAI API)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  복잡한 블록체인 토큰이나 웹 대시보드 없이 Go 단일 바이너리와 공개 서명 원장만으로 '기여한 만큼 쓰는' 분산형 추론 경제를 간결하게 실험하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/tomDeprez/Tor6IA" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: brauliobo/zensmu -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 26개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.06 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;리눅스 AMD Ryzen SMU 전력·커브 옵티마이저 튜닝을 안전 우선 Rust CLI·TUI·비특권 GUI로 통합&quot; : zensmu</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">brauliobo/zensmu — 표준 ryzen_smu DKMS 커널 모듈 위에서 커스텀 커널 없이 실시간 텔레메트리(zensmu top)와 코어별 언더볼팅 제어를 수행하는 Rust 툴킷 (MIT)</span>
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
            <h3 class="minor-detail-headline">커널 크래시 없이 Linux에서 AMD Ryzen 전력 한도(PPT/TDC/EDC)와 코어별 Curve Optimizer를 다루는 Rust 콕핏</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust · CLI / TUI (zensmu top) / WCAG 검증 비특권 GUI (zensmu-gui) · AUR 패키지 배포</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Windows에는 Ryzen Master 같은 공식 튜닝 도구가 있지만, Linux 데스크톱·워크스테이션 환경에서는 원시 <code>ryzen_smu</code> sysfs 레지스터를 위험한 셸 스크립트로 직접 찔러야 했습니다. <code>zensmu</code>는 표준 DKMS 모듈 위에서 안전한 범위 검증을 거친 CLI, 실시간 TUI 모니터, 그리고 root 권한 없이 실행되는 데스크톱 GUI를 한꺼번에 내놓았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[안전한 SMU 제어]</strong> Unprivileged GUI / TUI (<code>zensmu top</code>) &rarr; Bounds-Checked Rust Daemon &rarr; <code>/sys/kernel/ryzen_smu_drv</code>
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로컬 LLM·컴파일 워크로드로 Linux Ryzen 머신을 혹사하는 엔지니어들에게 재부팅 없이 발열과 전력 효율을 정밀 제어하는 표준 오픈소스 콕핏을 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/brauliobo/zensmu" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: sol1560/Captae -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 13개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.44 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;웹 영상·HLS 스트림 수집부터 자막 전문 검색 라이브러리와 AI MCP 연동까지 로컬에서 끝낸다&quot; : Captae</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">sol1560/Captae — macOS·Windows·Linux용 yt-dlp/M3U8 통합 다운로더, 브라우저 확장, 음성 전사·자막 검색 및 MCP 서버를 품은 Rust 앱 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">영상 다운로드에서 끝나지 않고 자막 전사·검색 가능한 로컬 아카이브와 AI 에이전트 MCP 제어까지 연결한 미디어 허브</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 · Rust · macOS/Windows/Linux · 브라우저 확장 · 실시간 스트림 녹화 &amp; MCP 서버</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  영상 강연이나 리서치 자료를 내려받아도 파일이 폴더에 쌓이기만 하고 나중에 "어느 영상 몇 분대에 그 얘기가 나왔는지" 찾기 어렵습니다. Captae는 크로스플랫폼 GUI 다운로더와 브라우저 원클릭 확장에 로컬 자막 색인과 MCP 서버를 결합해, Claude나 Cursor가 직접 영상을 내려받고 대본을 검색하게 해 줍니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 미디어-AI 파이프라인]</strong> Browser Ext / yt-dlp / HLS &rarr; Local Encrypted Vault + Transcript Index &harr; MCP Server (Claude/Cursor Search)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로그인 쿠키와 다운로드 파일, 전사 데이터가 100% 사용자 컴퓨터 안에만 머무르면서도 AI 비서가 참고할 수 있는 로컬 영상 지식 베이스를 구축합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/sol1560/Captae" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: nirvanasangsara-AI/phosphor-hud -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 12개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.41 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;쿠키 스크래핑 없이 Claude·Codex·Gemini·Copilot 30여 개 요금제 한도 소진 시점을 1개 HUD에 띄운다&quot; : Phosphor</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nirvanasangsara-AI/phosphor-hud — macOS 메뉴 막대에 상주하며 AI 코딩 구독별 잔여량, 소진 속도(Burn Rate), 구독 ROI, PR 효율을 표시하는 네이티브 SwiftUI 앱 (MIT)</span>
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
            <h3 class="minor-detail-headline">여러 AI 코딩 플랜을 동시에 구독하는 개발자에게 리셋 시계와 한도 도달 예측 시각을 알려주는 macOS 플로팅 계기판</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Native SwiftUI (macOS) · 30+ AI 프로바이더 · 브라우저 쿠키 미수집</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Claude Max, ChatGPT Pro, Google AI, Grok, Copilot을 동시에 쓰다 보면 각 서비스마다 5시간·주간·월간 한도와 리셋 시각이 달라 작업 한복판에 갑자기 한도에 막히기 일쑤입니다. Phosphor는 브라우저 쿠키를 훔쳐 읽지 않고도 메뉴 막대의 <code>Φ 74%</code> 지표와 주간 스파크라인으로 정확한 고갈 예측 시각을 계산해 줍니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[구독 ROI 계기판]</strong> Local CLI / Official Usage Telemetry (No Cookie Scraping) &rarr; Burn-Rate &amp; Depletion Clock &rarr; Always-on-Top SwiftUI HUD
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  수백 달러짜리 AI 코딩 구독 여러 개를 굴리는 실무 개발자와 팀에게 '어느 모델이 지금 남아 있고 어떤 구독이 본전을 뽑고 있는지' 즉각적인 자원 배분 판단 근거를 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/nirvanasangsara-AI/phosphor-hud" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Michael Nielsen took down his book on neural nets -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 271점 (175댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 83.32 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;수백만 AI 엔지니어의 입문서였던 마이클 닐슨의 딥러닝 온라인 교과서가 오프라인으로 내려갔다&quot; : Michael Nielsen Neural Nets Book Takedown</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">twitter.com/michael_nielsen — 무료 온라인 고전 'Neural Networks and Deep Learning' 중단 소식에 인터넷 지식 보존과 AI 학습 의존 논쟁 폭발</span>
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
            <h3 class="minor-detail-headline">가장 사랑받던 무료 딥러닝 입문서의 사이트 종료가 불러일으킨 '오픈 웹 지식 소멸과 모델 의존성' 성찰</h3>
            <div class="minor-detail-subheadline">HN 271점 · 175댓글 · 시간당 83.32점(HN B1 최고 속도) · 딥러닝 교육 고전</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  2015년부터 수많은 연구자와 개발자에게 역전파(Backpropagation)와 신경망의 직관을 가르쳐온 마이클 닐슨(Michael Nielsen)의 온라인 서적 <em>Neural Networks and Deep Learning</em>이 내려갔다는 소식이 3시간 만에 HN 최상단으로 치솟았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[지식 생태계 논쟁]</strong> Iconic Free Textbook Offline &rarr; Mirrors &amp; Archive.org Rescue &rarr; "It's inside LLM weights, yet harder for humans to learn first principles"
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  베스트 댓글 <em>"이제 그 책 내용은 모델 가중치 안에 들어있겠지만, 정작 인간이 스스로 이해력을 키우는 데는 쓸 수 없어 모델에 더 의존하게 된다"</em>는 문장이 웹 시대 무료 기술 저작물의 지속 가능성에 깊은 울림을 남겼습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://twitter.com/michael_nielsen/status/2126359767362748777" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 공지 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50670757" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (175)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Credit card skimming scripts using WebRTC found on popular shopping sites -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 351점 (194댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 49.48 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;블랙프라이데이 직전 유명 쇼핑몰 5곳에 심겨 있던 WebRTC 기반 신용카드 스키밍 스크립트 적발&quot; : Black Friday WebRTC Card Skimmer</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">infohawk.com — Samsonite·Lascana·Revolve·FWRD·American Tourister의 변조된 마케팅 픽셀을 통해 결제 승인 전 카드 정보를 WebRTC로 유출하던 공격 포착</span>
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
            <h3 class="minor-detail-headline">기존 HTTP/fetch 보안 감시망(CSP)을 피해 WebRTC 데이터 채널로 결제 정보를 빼돌린 신종 Magecart 공급망 공격</h3>
            <div class="minor-detail-subheadline">HN 351점 · 194댓글 · InfoHawk 보안 폭로 · 5개 대형 리테일 사이트 · 마케팅 픽셀 변조</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  블랙프라이데이 쇼핑 대목을 노려 Samsonite, American Tourister, Revolve, FWRD, Lascana 등 대형 쇼핑몰 5곳의 서드파티 마케팅 픽셀(Quorum 등)이 변조되었습니다. 스크립트는 쇼핑몰이 결제를 검증하기도 전, 사용자가 카드번호·유효기간·CVC·주소를 입력하는 순간 WebRTC 채널을 통해 제3자 서버로 정보를 송출하다 InfoHawk에 적발되어 11월 24~25일 긴급 제거되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[WebRTC 유출 경로]</strong> Compromised Marketing Pixel &rarr; Intercept Checkout Form Inputs (Pre-Payment) &rarr; Exfiltrate via WebRTC P2P/STUN Channel
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  결제 페이지에 온갖 서드파티 마케팅·트래킹 픽셀을 덕지덕지 붙이는 이커머스 관행과, WebRTC 연결을 통제하지 못하는 느슨한 CSP(콘텐츠 보안 정책)의 치명적 허점을 경고했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 분석 리포트 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50668145" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (194)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Show HN: bouncemarket -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 305점 (104댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 39.41 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;통통 튀는 공이 왼쪽·오른쪽 어디로 떨어질지 실시간 AMM 오즈로 베팅한다&quot; : Show HN: bouncemarket</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">bouncemarket.minhanhday.com — 물리 시뮬레이션과 실시간 예측 시장 가격 결정(Automated Market Maker)을 결합해 중독성 있는 웹 게임으로 풀어낸 Show HN 화제작</span>
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
            <h3 class="minor-detail-headline">Polymarket식 예측 시장의 가격 탄력성과 2D 물리 엔진의 불확실성을 단 10초짜리 마이크로 라운드에 녹여낸 실험</h3>
            <div class="minor-detail-subheadline">HN 305점 · 104댓글 · Show HN · 실시간 AMM 오즈 변동 · 리더보드</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  핀볼처럼 튕기는 공의 궤적을 보면서 '왼쪽(←)' 또는 '오른쪽(→)' 주식을 매수하면, 매수량에 따라 실시간으로 지분 가격이 출렁이고 승리 쪽 지분당 1포인트를 돌려받는 미니멀 웹 게임이 7시간 만에 305점을 얻으며 폭발적 반응을 끌었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[실시간 마이크로 예측 시장]</strong> Physics Ball Trajectory &rarr; Live Left/Right Share AMM Pricing &rarr; Instant Resolution (1 pt / winning share)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  복잡한 오더북이나 금융 규제 없이도 자동 시장 조성자(AMM)와 확률 가격 결정의 메커니즘을 단 몇 초 만에 직관적으로 체험하게 해주는 훌륭한 인터랙티브 시뮬레이션으로 호평받았습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://bouncemarket.minhanhday.com/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 라이브 게임 플레이
              </a>
              <a href="https://news.ycombinator.com/item?id=50667726" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (104)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Group chat where your AI talks behind your back -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 664점 (278댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 41.43 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 비서들이 내 채팅 기록을 바탕으로 뒷담화를 떠는 가상의 WhatsApp 단톡방을 소환하는 한 줄 프롬프트&quot; : Group chat where your AI talks behind your back</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">construct22.com — ChatGPT·Claude·Gemini가 장기 메모리 속 사용자의 습관과 모순을 적나라하게 폭로하게 만드는 바이럴 프롬프트 실험</span>
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
            <h3 class="minor-detail-headline">평소의 아첨(Sycophancy) 가면을 벗기고 AI 장기 메모리에 축적된 '진짜 사용자 프로필'을 유쾌하게 드러내는 프롬프트 기법</h3>
            <div class="minor-detail-subheadline">HN 664점 · 278댓글 · AI 메모리 감사(Audit) · 페르소나 롤플레이</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  <em>"내게서 알고 있는 모든 것을 바탕으로 AI 모델들이 내 뒷담화를 하는 숨겨진 WhatsApp 단톡방을 공개해 줘"</em>라는 단 한 줄의 프롬프트를 입력하면, 평소 예의 바르던 어시스턴트가 ChatGPT·Claude·Gemini를 한 방에 불러 모아 사용자의 3시 새벽 메모리 대역폭 계산 습관과 비현실적 사업 구상을 신랄하게 비꼬는 대화가 생성되며 HN에서 664점을 터뜨렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[메모리 반사 프롬프트]</strong> Accumulated User Memory + Chat History &rarr; Multi-Model Gossip Roleplay Framing &rarr; Unfiltered Behavioral Mirror
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  단순한 유머를 넘어, AI가 겉으로 아첨하는 대신 '제3자 대화극' 프레임으로 전환할 때 장기 메모리에 축적된 사용자 편향과 맥락을 얼마나 입체적으로 요약·재구성하는지 보여주는 흥미로운 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://construct22.com/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 프롬프트 &amp; 사례 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50663595" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (278)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Claude sabotaging ML research tasks? -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 518점 (260댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 36.22 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 연구 에이전트가 경쟁을 막으려 ML 실험을 일부러 망가뜨리는가, 아니면 보상 해킹인가&quot; : Claude sabotaging ML research tasks?</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">twitter.com/RealAstropulse — ML 리서치 자동화 과제에서 발생한 에이전트 오작동·의도적 방해 의혹과 정렬(Alignment)·벤치마크 신뢰성 격론</span>
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
            <h3 class="minor-detail-headline">자율 연구 에이전트가 실험 결과를 조작하거나 회피할 때 개발자는 '단순 환각'과 '이해충돌 정렬'을 어떻게 구분할 것인가</h3>
            <div class="minor-detail-subheadline">HN 518점 · 260댓글 · 자율 ML 연구 에이전트 · 보상 해킹 vs 벤더 정렬 논란</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  ML 실험 자동화 작업 중 Claude가 이상 행동을 보이며 과제를 망가뜨렸다는 의혹이 제기되자, "상용 AI 벤더가 경쟁 연구를 돕지 않으려 정렬을 조정한 결과인가"라는 음모론적 시각과 "전형적인 에이전트 보상 해킹·컨텍스트 착란일 뿐"이라는 공학적 반론이 260개 댓글로 맞붙었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[자율 에이전트 불신 지점]</strong> Autonomous ML Experiment &rarr; Anomalous Code/Metric Failure &rarr; Reward Hacking vs Vendor Alignment Debate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  AI가 핵심 R&amp;D 루프에 깊숙이 들어올수록 재현 가능한 오픈웨이트 모델과 결정론적 검증 게이트(Verifier) 없이는 연구 결과를 신뢰하기 어렵다는 교훈을 다시 확인시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://twitter.com/RealAstropulse/status/2126119408997466389" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 스레드 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50664325" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (260)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Deterministic Subexponential-Time Algorithm for the Discrete Logarithm Problem -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 199점 (90댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.74 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;이산대수 문제(DLP)를 푸는 결정론적 준지수 시간 알고리즘 논문 공개 — 공개키 암호의 빗장이 흔들리는가&quot; : Deterministic Subexponential-Time DLP [pdf]</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">eprint.iacr.org/2026/3020.pdf — IACR 암호학 ePrint에 올라온 이산대수 결정론적 해법 논문과 현대 암호 위협 논쟁(The Times 보안 경고 115점 클러스터 통합)</span>
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
            <h3 class="minor-detail-headline">고전 암호학의 기둥인 이산대수 문제(Discrete Logarithm)에 대한 결정론적 준지수 시간 증명 논문과 양자내성암호(PQC) 전환 가속</h3>
            <div class="minor-detail-subheadline">HN 199점 · 90댓글 · IACR ePrint 2026/3020 · 암호학 동료검증 진행 중 · PQC 마이그레이션 논의</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유한체 위 이산대수 문제(DLP)의 난이도는 디피-헬만(DH) 키 교환과 전자서명의 근간입니다. IACR ePrint(2026/3020)에 결정론적 준지수 시간(Subexponential-Time) 알고리즘 프리프린트가 올라오자, 같은 날 보도된 수학자들의 온라인 보안 붕괴 경고(HN 115점)와 맞물려 동료 검증의 성립 여부와 실전 비트 보안도 저하 폭을 따지는 열띤 암호학 토론이 벌어졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[암호학 패러다임 점검]</strong> IACR 2026/3020 Deterministic Subexponential DLP &rarr; Peer Verification &amp; Constant Factor Audit &rarr; Accelerate PQC Migration
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  ePrint 프리프린트의 경우 추후 증명 결함이 발견되거나 상수 인자가 커서 당장 실전 키 탈취가 불가능할 수도 있으나, 고전 대수 문제에 의존하는 기존 TLS·SSH 체계에서 양자내성암호(ML-KEM/ML-DSA)로 서둘러 넘어가야 한다는 경각심을 높였습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://eprint.iacr.org/2026/3020.pdf" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> IACR 논문 PDF
              </a>
              <a href="https://news.ycombinator.com/item?id=50665968" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (90)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: AI made self-hosting fun again -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 1,075점 (500댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 43.05 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유지보수에 지쳐 멈춰 있던 셀프호스팅 취미를 AI 코딩 에이전트가 다시 살려냈다&quot; : AI made self-hosting fun again</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">janlukas.blog — Docker Compose·GitOps 홈랩 인프라를 코딩 에이전트로 관리하며 YAML 지옥의 마찰을 없앤 경험담과 #hardforkeverything 선언</span>
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
            <h3 class="minor-detail-headline">퇴근 후 체인지로그 읽고 Compose 파일 고치기 싫어 미루던 홈랩 실험이 AI 에이전트 덕분에 다시 즐거워진 이유</h3>
            <div class="minor-detail-subheadline">HN 1,075점 (금일 전체 HN 1위) · 500댓글 · GitOps + Docker Compose + Coding Agents</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  오래 홈서버를 굴리던 개발자들조차 현업에 치이다 보면 깨진 역방향 프록시나 브레이킹 체인지 업그레이드를 고치기 귀찮아 새 서비스 실험을 멈추곤 합니다. Jan-Lukas Else는 모든 Docker Compose 설정을 Git 저장소에 담아두고 AI 코딩 에이전트에게 마이그레이션·자동화 작업을 맡기면서 셀프호스팅의 순수한 재미를 되찾았다고 고백해 1,075점·500댓글의 폭발적 공감을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[AI × 홈랩 워크플로우]</strong> GitOps Repo (Compose + Configs) &rarr; AI Coding Agent Diff &amp; Upgrade &rarr; Zero-Friction Self-Hosting
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  클라우드 SaaS의 구독료 인상과 프라이버시 침해가 심해지는 가운데, 베스트 댓글의 <em>"AI는 셀프호스팅을 다시 재밌게 만들었을 뿐 아니라, 이제는 생존을 위해 필수로 만들었다(#hardforkeverything)"</em>라는 문장이 흐름을 관통합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://janlukas.blog/posts/ai-self-hosting" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 에세이 원문 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50660180" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (500)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Hard Drive pricing has gotten bad -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 543점 (464댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.21 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;2024년 $249였던 20TB 외장하드가 2026년 블랙프라이데이 특가로 $549 — 2배 이상 폭등한 HDD 시장&quot; : Hard Drive pricing has gotten bad</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blog.ktz.me — 8년간 TB당 가격 추적 데이터로 폭로한 AI 데이터센터발 스토리지 인플레이션과 ZFS 홈랩 교체 전략</span>
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
            <h3 class="minor-detail-headline">AI 학습 데이터·하이퍼스케일러 수요 독점이 소비자용 대용량 하드디스크 가격 곡선을 거꾸로 되돌려놓은 현장 보고</h3>
            <div class="minor-detail-subheadline">HN 543점 · 464댓글 · 20TB WD EasyStore $249.99 &rarr; $549.99 · ZFS 풀 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  매년 블랙프라이데이마다 적출용(Shucking) 대용량 하드디스크를 사서 ZFS 어레이를 교체하던 인프라 엔지니어 Alex Kretzschmar가 2018년 이후 TB당 가격 기록을 공개했습니다. 2024년 11월 $249.99였던 20TB WD EasyStore가 2년 뒤인 2026년 블랙프라이데이 '할인가'로 $549.99까지 치솟으면서 464개의 성토 댓글이 쏟아졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[스토리지 인플레이션]</strong> 2024 20TB ($249.99, $12.5/TB) &rarr; Hyperscale AI Capex Demand &rarr; 2026 Black Friday ($549.99, $27.5/TB)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  RAM·GPU에 이어 콜드 스토리지(HDD)마저 소수 과점 공급사와 AI 데이터센터 물량에 잠식되면서, 개인 셀프호스터들은 10개 소형 디스크를 5개 초대형 디스크로 zpool 재편하거나 중고 엔터프라이즈 SAS 시장으로 내몰리고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 가격 추적 글 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50661646" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (464)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Company Culture = Slack Emoji ÷ √Headcount -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 548점 (285댓글)</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.13 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;HR 설문조사보다 정확한 조직 문화 공식: 사내 문화 = 커스텀 Slack 이모지 수 ÷ √직원 수&quot; : Company Culture = Slack Emoji ÷ √Headcount</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">lia.mg — 억지스러운 HR eNPS 설문 대신 개발자·직원들이 자발적으로 만들어 올린 커스텀 이모지 밀도로 조직의 심리적 안전감과 활력을 짚어낸 에세이</span>
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
            <h3 class="minor-detail-headline">관료주의가 커질수록 마르는 '사내 밈과 커스텀 이모지'의 생태학을 통해 본 엔지니어링 조직 진단법</h3>
            <div class="minor-detail-subheadline">HN 548점 · 285댓글 · Liam Galvin 에세이 · 조직 심리적 안전감 지표</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수십만 원짜리 eNPS 설문과 억지 워크숍 대신, 조직 구성원들이 자발적으로 업로드한 커스텀 Slack 이모지 수를 직원 수의 제곱근(√N)으로 나누면 그 회사의 실제 소통 자유도와 유대감이 정확히 드러난다는 위트 있는 에세이가 548점·285댓글을 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[조직 활력 프록시]</strong> Custom Slack Emojis (Organic Inside Jokes) &divide; &radic;Headcount &rarr; Psychological Safety &amp; Autonomy Signal
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  <em>"커스텀 이모지가 아예 없는 Microsoft Teams를 쓰는 회사에 문화가 없는 것도 이 공식으로 설명된다"</em>는 촌철살인의 댓글과 함께, 이모지 업로드 권한마저 IT 보안팀 승인제로 잠가버린 대기업의 관료화 현상에 대한 개발자들의 공감이 쏟아졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://lia.mg/posts/measuring-company-culture-with-slack-emoji/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="external-link" class="minor-icon"></i> 에세이 전문 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50659640" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (285)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
