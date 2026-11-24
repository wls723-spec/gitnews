# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-25

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
          직전 발행(11월 24일) 이후 30시간 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 관심 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: jakobhviid/verso -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 51개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.03 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;내 Immich 사진첩 전체를 Finder·파일 앱의 네이티브 드라이브로 마운트한다&quot; : Verso</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">jakobhviid/verso — Rust 공유 코어 위에 iPhone·iPad·Mac(SwiftUI/AppKit) 및 Linux(GTK4/libadwaita) 네이티브 UX를 얹은 비공식 Immich 클라이언트 (MIT)</span>
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
            <h3 class="minor-detail-headline">셀프호스팅 Immich 서버를 Apple Photos 수준의 네이티브 앱과 OS 파일시스템 드라이브로 연결하는 크로스플랫폼 프로젝트</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Swift + Rust 공통 코어 · macOS Homebrew Cask &amp; Linux deb/rpm/Flatpak 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  구글 포토의 유력한 셀프호스팅 대안인 Immich는 웹·모바일 앱이 훌륭하지만, 데스크톱 환경에서 OS 순정 사진 앱처럼 부드러운 스크롤과 Finder/GNOME 파일 관리자 내 가상 드라이브 연동까지 한 번에 제공하는 네이티브 클라이언트에 대한 갈증이 컸습니다. <code>Verso</code>는 하단 동기화 엔진과 그리드 날짜 계산을 Rust 단일 코어로 공유하면서 UI만 플랫폼별 순정 툴킷(SwiftUI/UIKit/AppKit/GTK4)으로 구현해 공개 9.9시간 만에 51스타를 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[크로스 네이티브 구조]</strong> Immich Server API &rarr; Shared Rust Core (Sync &amp; Virtual Drive Layout) &rarr; SwiftUI (Apple) / GTK4 (Linux)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹 래퍼(Electron/WebView) 대신 OS 네이티브 파일 프로바이더와 네이티브 위젯을 택해 셀프호스팅 사진 백업 UX를 상용 클라우드 수준으로 끌어올렸습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/jakobhviid/verso" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://jakob.hviid.phd/verso/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 페이지
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: shlokkhemani/lifestream -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 14개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.9 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;40개 소스에서 수집한 내 삶의 기록을 Mac 암호화 폴더 한 곳에 모아 내 에이전트에게만 연다&quot; : Lifestream</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">shlokkhemani/lifestream — 메시지·메일·사진·위치·건강·스크린 및 Google Takeout을 로컬 암호화 타임라인으로 통합하는 오픈소스 (Apache-2.0)</span>
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
            <h3 class="minor-detail-headline">빅테크 클라우드에 흩어진 개인 생애 데이터를 내 Mac 로컬 암호화 아카이브로 회수해 AI 에이전트 메모리로 제공하는 프로토콜</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · TypeScript · macOS 앱 + iPhone 베타 · 40+ 커넥터 &amp; Google Takeout 임포트</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  진정한 개인 비서 AI 에이전트가 작동하려면 내가 지난주 누구와 어떤 메시지를 주고받았는지, 어디를 방문했는지 맥락이 필요하지만, 이를 빅테크 클라우드에 일괄 위임하는 것은 심각한 프라이버시 위험을 동반합니다. <code>Lifestream</code>은 iPhone 백업과 Google Takeout을 포함한 40여 종의 데이터 소스를 Mac의 단일 로컬 암호화 폴더에 통합하고 사용자가 허가한 에이전트만 접근하도록 제어합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[개인 컨텍스트 주권]</strong> 40+ Personal Sources &amp; Backups &rarr; Encrypted Local Mac Vault &rarr; Permissioned AI Agent Access
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트 시대의 '개인 기억 저장소'를 중앙 SaaS가 아닌 로컬 파일시스템과 암호화 소유권 위에 재정립하는 흐름을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/shlokkhemani/lifestream" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://trylifestream.com" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 사이트
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: bjarneo/editor -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 13개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.75 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;생각이 끝나기 전에 열리는 초고속 Rust 모달 코드 에디터&quot; : editor</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">bjarneo/editor — Rune 기반으로 Neovim 근육 기억·13개 언어 Tree-sitter·LSP를 즉각 기동하는 경량 Rust 에디터 (MIT)</span>
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
            <h3 class="minor-detail-headline">무거운 IDE를 대신해 코드를 빠르게 열어 읽고, Tree-sitter·LSP로 즉시 수정하는 집중형 Rust 에디터</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust + Rune 스크립팅 · Vim 모달 &amp; 클래식 멀티커서 동시 지원 · 13개 언어 Tree-sitter</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 코딩 에이전트가 방대한 코드를 쏟아내는 시대일수록, 개발자가 파일을 순식간에 열어 코드를 검토하고 핵심 한두 줄만 손보는 '읽기 및 빠른 편집' 도구의 가치가 커집니다. <code>bjarneo/editor</code>는 풀 IDE의 비대함을 거부하고 Rust와 Rune 엔진 위에 실제 Vim 모션·레지스터·매크로, 13개 언어 Tree-sitter 텍스트 객체(<code>af</code>, <code>ic</code>), LSP 진단과 AI 에이전트 연동까지 담아냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[초고속 편집 경로]</strong> Instant Cold Start &rarr; Vim Modal / Multi-Cursor &rarr; 13-Lang Tree-sitter + LSP &rarr; AI Agent Hooks
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Neovim의 설정 지옥과 VS Code 포크 IDE의 메모리 점유율 사이에서 '즉시 열려 바로 읽는' 경량 네이티브 에디터 수요를 정확히 겨냥합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/bjarneo/editor" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://bjarneo.github.io/editor/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 사이트
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: NguyenQuocDat06-AI/kaggle-shell-mcp -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 30개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.12 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;주간 무료 Kaggle Dual-T4 GPU 30시간을 AI 에이전트 전용 실시간 원격 터미널로 연결한다&quot; : kaggle-shell-mcp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">NguyenQuocDat06-AI/kaggle-shell-mcp — ngrok·브라우저 클릭 없이 API 키만으로 최대 4×Tesla T4 GPU VM을 MCP로 조종하는 브리지 (MIT)</span>
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
            <h3 class="minor-detail-headline">배치 실행만 되던 Kaggle 무료 GPU 세션을 대화형 셸과 백그라운드 학습 러너로 바꿔 AI 에이전트에 쥐여주는 MCP 서버</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python PyPI(kaggle-shell-mcp / kgsh) · Dual Concurrent T4 VM 지원 · Zero ngrok Setup</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Kaggle은 매주 약 30시간(세션당 12시간)의 무료 GPU 연산을 제공하지만, 공식 CLI는 단발성 배치 푸시만 가능해 코딩 에이전트가 인터랙티브하게 모델을 학습·디버깅하기 어려웠습니다. <code>kaggle-shell-mcp</code>(<code>kgsh</code>)는 기존 <code>KAGGLE_USERNAME</code>과 키만으로 <code>ngrok</code>이나 수동 브라우저 조작 없이 AI 에이전트가 GPU 터미널 명령을 실행하고 장시간 학습 잡을 관리할 수 있게 해 공개 14시간 만에 30스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[무료 GPU 에이전트 브리지]</strong> AI Agent (MCP Client) &rarr; <code>kgsh</code> Bridge &rarr; Kaggle Dual-T4 GPU VM (Up to 60GB VRAM)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로컬 GPU가 없는 학생·인디 연구자의 코딩 에이전트도 무료 클라우드 GPU를 원격 손발처럼 부리며 실험을 자동화할 수 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: YHD-yhd-coder/nl2tex -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 8개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.57 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자연어 설명과 스크린샷을 KaTeX 컴파일 검증 완료된 LaTeX·Word 수식으로 즉시 변환&quot; : nl2tex</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">YHD-yhd-coder/nl2tex — 계산·추측 없이 오직 정확한 LaTeX·MathML·Word OMML 전사 및 모호성 경고를 수행하는 로컬 우선 도구 (MIT)</span>
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
            <h3 class="minor-detail-headline">범용 챗봇의 환각과 컴파일 에러를 없애기 위해 KaTeX 즉시 컴파일·신뢰도 표기·6대 학문 규칙을 내장한 수식 전사기</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Node.js 20+ 로컬 서버(127.0.0.1) · KaTeX 자동 재시도 검증 · Word OMML·MathML 내보내기</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  논문이나 보고서를 쓸 때 수식 손코딩은 문법보다 기호 이름을 떠올리는 일이 고역이며, 일반 LLM에 맡기면 수식을 임의로 간소화하거나 컴파일되지 않는 깨진 LaTeX를 내놓기 일쑤입니다. <code>nl2tex</code>는 "오직 전사만 하고 계산·추측하지 않는다"는 원칙 아래, 생성된 모든 결과를 그 자리에서 KaTeX로 컴파일 검증해 에러 시 자동 재시도하고 신뢰도가 낮으면 최대 3개 후보 해석을 제시합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[무오류 수식 파이프라인]</strong> NL Text / Ctrl+V Image &rarr; Domain Rules (Math/Phys/Chem) &rarr; KaTeX Compile Gate &rarr; LaTeX / Word OMML
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  6개 학문(수학·물리·화학 <code>\ce{}</code>·컴퓨터·경제통계·생물) 전용 포매팅과 Word OMML 원클릭 복사로 연구자의 문서 작성 마찰을 크게 줄여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/YHD-yhd-coder/nl2tex" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: akazwz/bash-autosuggest -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 10개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.53 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;외부 의존성 0개 Rust .so 플러그인으로 순정 Bash에 0.13ms Fish 자동완성·구문 강조를 심다&quot; : bash-autosuggest</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">akazwz/bash-autosuggest — PTY 래퍼 없이 GNU Readline을 직접 후킹하는 초저지연 네이티브 Bash 로드 가능 빌트인 (MIT)</span>
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
            <h3 class="minor-detail-headline">Zsh나 Fish로 갈아타지 않고도 순정 GNU Bash에서 깜빡임 없는 실시간 명령어 하이라이팅과 히스토리 자동완성을 구현한 Rust 모듈</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Pure Rust (0 Crate Dependencies) · GNU Readline 직접 후킹 · 0.13ms 스캔 &amp; &lt;0.6ms 기동</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  많은 엔지니어들이 셸 스크립트 호환성 때문에 Bash를 유지하고 싶지만 Fish·Zsh의 인라인 히스토리 추천과 유효 명령어 실시간 색상 강조(Syntax Highlighting)가 아쉬워 울며 겨자 먹기로 셸을 바꿉니다. <code>bash-autosuggest</code>는 무거운 PTY 래퍼나 불안정한 <code>bind -x</code> 트릭 대신 Rust 크레이트 의존성 0개로 컴파일된 공유 라이브러리(<code>.so</code>)가 Bash 내부 빌트인으로 적재되어 키 입력당 힙 할당 없이 0.13ms 만에 추천을 띄워줍니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[Zero-Fork Readline Hook]</strong> Keystroke &rarr; In-Process Rust Builtin (.so) &rarr; 0.13ms History Scan + Lazy $PATH &rarr; Single-Write Render
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  서버·컨테이너의 기본 Bash 환경을 깨뜨리지 않으면서도 최신 모던 셸의 시각적 피드백과 생산성을 그대로 누릴 수 있는 깔끔한 시스템 공학 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/akazwz/bash-autosuggest" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 141개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.01 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;오가노이드 생체 신경 전기 신호를 LLM 강화학습 정책 입력으로 넣으면 탐험 행동이 달라질까?&quot; : BioSignal-Guided-LLM-RL</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning — Godot 생존 게임 환경에서 오프라인 오가노이드 신경 기록을 정책·가치망에 결합한 논문·코드 (MIT)</span>
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
            <h3 class="minor-detail-headline">생물학적 뇌 오가노이드의 전기적 활동 리플레이가 언어모델 에이전트의 생존·탐험 의사결정에 미치는 영향을 정량 측정한 오픈 리서치</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python + Godot 생존 환경 · 프리프린트(paper.pdf)·체크포인트·원시 생체신호 데이터셋 동시 공개</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  생물학적 신경 신호(오가노이드)와 실리콘 AI를 결합하려는 '바이오-하이브리드 컴퓨팅'이 철학적 사변을 넘어 재현 가능한 강화학습 실험으로 내려왔습니다. 상하이 Brainintelli 연구팀은 Godot 기반 2D 생존 게임에서 LLM 에이전트의 정책·가치 신경망에 오가노이드 신경 전기 기록(Offline Replay)을 주입했을 때, 동일한 시간 예산 내 지형 탐사 범위와 갈증·허기 대처 행동이 어떻게 달라지는지 대조 실험한 전체 코드와 데이터를 공개해 20시간 만에 141스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[바이오-실리콘 RL 루프]</strong> Organoid Neural Replay &rarr; LLM Policy &amp; Value Network &rarr; Godot Survival Agent Actions &rarr; Paired Eval
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  주관적 감정 의인화를 배제하고 측정 가능한 생존 행동 지표와 공개 체크포인트로 바이오신호 결합 RL의 기준선을 제시했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: AyushRajSinghParihar/weaponized-curiosity -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 166개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.44 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;코딩하기 전에 먼저 반증 가능한 증거로 아키텍처를 검증시키는 에이전트 스킬&quot; : weaponized-curiosity</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AyushRajSinghParihar/weaponized-curiosity — Claude Code·Codex에서 Quick/Deep 모드로 가설·실험·예산 한정 리서치를 수행하는 포터블 스킬 (MIT)</span>
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
            <h3 class="minor-detail-headline">성급한 코드 생성 대신 &quot;결론을 뒤집을 핵심 증거&quot;부터 탐색하게 강제하는 에이전트 의사결정 프레임워크</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Claude Code (/weaponized-curiosity) &amp; Codex ($weaponized-curiosity) · Quick / Deep 모드</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 코딩 에이전트에게 "Postgres 큐를 유지할지 전용 브로커로 옮길지 검토해 줘"라고 물으면, 십중팔구 그럴듯한 장단점 표만 출력하고 실제 워크로드 검증은 건너뜁니다. <code>weaponized-curiosity</code>는 에이전트가 결론을 바꿀 가능성이 가장 높은 결정적 증거부터 먼저 수집하고, 상충하는 증거가 나오면 깊이 파고들되 정해진 시간·토큰 예산 안에서 멈추도록 설계해 하루 만에 166스타를 확보했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[증거 기반 탐색]</strong> Hypothesis &rarr; Highest-Leverage Disproving Evidence &rarr; Quick/Deep Bounded Experiment &rarr; Decision Brief
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트의 무분별한 '아첨성 동의'와 성급한 코드 작성을 막고 시니어 엔지니어 수준의 기술 검토 루틴을 표준 스킬로 이식했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/AyushRajSinghParihar/weaponized-curiosity" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: iniwex5/VoWiFiX -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 116개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.09 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;통신사 MBN 변조 없이 퀄컴 스냅드래곤 기저대역 EFS를 안전 병합해 해외 로밍 VoWiFi를 해방하다&quot; : VoWiFiX</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">iniwex5/VoWiFiX — Root EFS(/dev/diag·diag-router)·QRTR 듀얼심 핫스왑 데몬·LSPosed 4계층을 통합한 VoWiFi 풀스택 (GPL-3.0)</span>
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
            <h3 class="minor-detail-headline">통신사·제조사가 임의로 잠가둔 안드로이드 Wi-Fi 통화와 로밍 차단을 기저대역과 프레임워크 양면에서 재부팅 없이 해제하는 엔지니어링 툴킷</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · 퀄컴 스냅드래곤 (구형 /dev/diag &amp; GKI diag-router 동시 대응) · KernelSU/Magisk/LSPosed</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  외산 스마트폰이나 해외 로밍 환경에서는 하드웨어가 VoWiFi를 지원해도 통신사 화이트리스트와 MBN 프로파일 제한 때문에 Wi-Fi 통화가 막히는 경우가 많습니다. <code>VoWiFiX</code>는 원본 MBN 이미지를 훼손하지 않고 기저대역 <code>EFS</code> 설정에 최소한의 바이트만 안전 병합한 뒤, 듀얼 SIM 전환 시 <code>QRTR(AF_QIPCRTR)</code>으로 재부팅 없이 슬롯을 열로 새로고침해 22시간 만에 116스타를 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[4계층 VoWiFi 해제]</strong> EFS Safe Merge (diag/diag-router) &rarr; QRTR Hot Refresh &rarr; LSPosed CarrierConfig Bypass &rarr; Native UI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  스냅드래곤 8 Gen 2~8 Elite의 최신 GKI 커널 환경까지 무부작용 정적 바이너리로 자동 대응해 모바일 통신 해킹 생태계의 기준을 높였습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/iniwex5/VoWiFiX" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Tidal bans AI-generated music -->
        <div class="minor-item" id="minor-hn-10" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 310점 · 293댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 47.26 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;90일간 업로드된 곡의 43%가 AI, 그중 96%는 재생수 0회&quot; — Tidal, AI 생성 음악 전면 퇴출 단행</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Tidal bans AI-generated music — 하루 8만~8만 5천 곡씩 쏟아지는 AI 스팸 음원 차단을 위해 기존 2,900만 곡 정리 선언</span>
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
            <h3 class="minor-detail-headline">스트리밍 로열티 파밍과 카탈로그 오염을 막기 위해 메이저 음원 플랫폼 최초로 AI 음원 전면 금지를 선언한 Tidal</h3>
            <div class="minor-detail-subheadline">Variety 보도 · HN 310점 · 293댓글 · 최근 90일 업로드 43% AI 생성 · 일일 8만~8.5만 곡 차단</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  고음질 음원 스트리밍 서비스 Tidal이 자사 카탈로그에서 2,900만 곡에 달하는 AI 생성 트랙을 대거 도려내고 향후 AI 생성 음악 업로드를 전면 금지한다고 발표했습니다. 공개된 수치는 충격적입니다. 최근 90일간 플랫폼에 올라온 전체 곡의 <strong>43%</strong>가 AI 생성 음원이었으며, 그중 <strong>96%</strong>는 단 한 번도 재생되지 않은 스팸이었고 매일 8만~8만 5,000곡씩 쏟아지며 추천 알고리즘과 스토리지를 잠식하고 있었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[AI 슬롭 방어전]</strong> 43% AI Uploads (96% Zero-Play) &rarr; Storage &amp; Royalty Pool Pollution &rarr; 29M Track Purge &amp; Daily Ban
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  생성형 AI의 한계생산비용이 0으로 수렴할 때 콘텐츠 플랫폼이 '무제한 수용' 대신 '큐레이션 방화벽'으로 회귀할 수밖에 없음을 보여주는 대표적 분기점입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 기사 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50630309" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (293댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Active intrusion campaign against Check Point security management servers -->
        <div class="minor-item" id="minor-hn-11" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 236점 · 96댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 37.87 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;기업 방화벽의 관제탑이 뚫렸다&quot; — GreyNoise, Check Point 보안 관리 서버 겨냥 대규모 침투 캠페인 포착</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Check Point Security Management Intrusion — 초기 침해 서버를 다시 스캔해 Linux IPv4 UAF(CVE-2026-98432)를 노리는 연쇄 위협 추적</span>
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
            <h3 class="minor-detail-headline">네트워크 경계 장비 관리 서버를 겨냥한 다중 위협 행위자들의 동시다발적 침해와 후속 취약점 악용 정황</h3>
            <div class="minor-detail-subheadline">GreyNoise 위협 인텔리전스 보고서 · HN 236점 · GT13 행위자 · Linux IPv4 UAF(CVE-2026-98432) 연계</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  위협 인텔리전스 기업 GreyNoise가 기업 네트워크의 핵심 통제점인 Check Point 보안 관리 서버(Security Management Servers)를 겨냥한 실제 침투 캠페인을 공개했습니다. 특히 11월 초 이후에는 GT13 등 다른 위협 행위자들까지 이미 침해된 서버를 재스캔하며 Linux IPv4 Use-After-Free 취약점(<code>CVE-2026-98432</code>) 점검 스크립트를 실행하는 '이중 약탈' 양상까지 관측되며 보안팀에 비상이 걸렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[침투 연쇄 경로]</strong> Exposed Check Point Mgmt Server &rarr; Initial Compromise &rarr; GT13 Secondary Scan (CVE-2026-98432 UAF)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 보안 임팩트</div>
                <p class="minor-paragraph">
                  보안 관리 서버의 외부 노출 최소화, 즉각적 패치 및 관리 포트 격리의 중요성을 다시 한번 일깨우는 경보입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 보고서 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50630594" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (96댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Jetty Pro -->
        <div class="minor-item" id="minor-hn-12" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 235점 · 101댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 36.8 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유틸리티 앱마저 구독제여야 하는가?&quot; — John Siracusa의 신작 Mac 앱 'Jetty Pro'와 구독 피로감 논쟁</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">hypercritical.co — 클래식 Mac DragThing 감성을 계승한 화면 가장자리 단축키 독 앱 출시와 일회성 구매 vs 구독 가격 정책 격론</span>
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
            <h3 class="minor-detail-headline">저명한 Apple 기술 평론가 겸 인디 Mac 개발자 John Siracusa가 공개한 신작 유틸리티가 불러일으킨 소프트웨어 가격 철학 토론</h3>
            <div class="minor-detail-subheadline">Hypercritical 블로그 · HN 235점 · 101댓글 · macOS 생산성 유틸리티 가격 모델 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  2019년 은퇴한 전설적 Mac 앱 <em>DragThing</em>의 기능을 현대 macOS에 이식해 온 John Siracusa가 신작 <code>Jetty Pro</code>를 발표했습니다. 그런데 앱의 정교한 완성도와 별개로, 해커뉴스에서는 이 작은 유틸리티의 구독(Subscription) 가격 모델에 대해 101개의 뜨거운 댓글이 달렸습니다. 개발자들은 <em>"연 1달러든 100달러든 또 하나의 구독은 참을 수 없다, 차라리 40~50달러 일회성 영구 라이선스(Lite 버전)를 팔아달라"</em>며 소프트웨어 소유권에 대한 강한 피로감을 표출했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[소프트웨어 가격 딜레마]</strong> Classic Utility App Craft &harr; Annual Subscription Model &rarr; User Fatigue (&quot;Let Me Buy It Once&quot;)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 생태계 임팩트</div>
                <p class="minor-paragraph">
                  인디 데스크톱 소프트웨어 시장에서 지속 가능한 유지보수 수익과 사용자의 '영구 소유' 욕구 사이의 간극을 여실히 드러낸 토론입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="http://hypercritical.co/2026/11/23/jetty-pro" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 블로그 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50630462" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (101댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: LLM agents work for their parent companies, not for you -->
        <div class="minor-item" id="minor-hn-13" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 849점 · 353댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 84.07 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클라우드 LLM 에이전트는 당신이 아니라, 그 모회사를 위해 일한다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">michaelharley.net — 중앙 통제형 폐쇄 모델 에이전트의 이해충돌 구조와 오픈웨이트·로컬 에이전트의 필연성을 짚은 에세이</span>
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
            <h3 class="minor-detail-headline">에이전트가 사용자의 브라우저와 지갑, 코드베이스를 대리할 때 누구의 이익을 최우선으로 대변하는가를 묻는 기술 비평</h3>
            <div class="minor-detail-subheadline">Michael Harley 에세이 · HN 849점 · 353댓글 · Principal-Agent Problem &amp; 오픈 모델 대안 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 에이전트가 단순 챗봇을 넘어 구매·검색·코딩·업무 결정을 대행하기 시작하면서, 플랫폼 기업이 모델의 시스템 프롬프트와 정렬(Alignment)을 통해 자사 광고·생태계 락인·수익 모델에 유리한 방향으로 은밀히 유도할 수 있다는 '대리인 문제(Principal-Agent Problem)'가 수면 위로 떠올랐습니다. 이 글은 HN 849점을 받으며 오픈웨이트 로컬 모델이 왜 단순 비용 절감을 넘어 '사용자 충성도'의 문제인지 격렬한 토론을 촉발했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[대리인 이해충돌]</strong> User Goal &harr; Cloud Vendor Alignment / Ad / Lock-in &rarr; Shift Toward Local Open-Weight Agents
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  오늘 <code>Bonsai 2.5 27B</code>나 <code>Songe</code> 같은 로컬 에이전트 인프라가 각광받는 철학적·경제적 배경을 정확히 설명해 주는 담론입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 에세이 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50627340" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (353댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: 2035 came early -->
        <div class="minor-item" id="minor-hn-14" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 929점 · 351댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 57.13 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;2035년이 일찍 도착했다&quot; — 브라우저 탭 안에서 Firefox·X11 GUI 리눅스 앱을 그대로 부팅한 'trynix.dev'</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">fzakaria.com — NixOS·WebAssembly 기반으로 솔리테어·glxgears·Firefox까지 웹에서 즉시 띄우며 '자바스크립트의 탄생과 죽음' 예언 소환</span>
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
            <h3 class="minor-detail-headline">WebAssembly 위에서 NixOS와 X11 GUI 데스크톱 앱(심지어 Firefox 안의 Firefox)을 구동한 경이로운 웹 VM 실험</h3>
            <div class="minor-detail-subheadline">Farid Zakaria 블로그 · HN 929점 · 351댓글 · trynix.dev 라이브 구동 · WebAssembly &amp; Nix</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  2014년 Gary Bernhardt는 전설적인 강연 <em>"The Birth &amp; Death of JavaScript"</em>에서 2035년이 되면 모든 네이티브 소프트웨어와 OS가 웹 브라우저 샌드박스 안으로 빨려 들어갈 것이라고 풍자 섞인 예언을 남겼습니다. 개발자 Farid Zakaria는 Nix 패키지 생태계와 WebAssembly를 결합한 <code>trynix.dev</code>에서 <code>solitaire</code>, <code>glxgears</code>, <code>xeyes</code>는 물론 풀 GUI 웹브라우저인 Firefox까지 브라우저 안에서 부팅시켜 HN 929점의 경탄을 이끌어냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[WASM OS 매트료시카]</strong> Host Browser &rarr; WebAssembly Nix Runtime &rarr; X11 Display &rarr; Native Linux GUI (Firefox / GL Gears)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 기술 임팩트</div>
                <p class="minor-paragraph">
                  재현 가능한 Nix 빌드 그래프와 WASM의 결합이 웹 브라우저를 명실상부한 범용 OS 하이퍼바이저로 탈바꿈시키고 있음을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://fzakaria.com/2026/11/23/2035-came-early" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 블로그 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50624497" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (351댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Quad9 pulled their DNS service from France -->
        <div class="minor-item" id="minor-hn-15" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 320점 · 160댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.51 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;사법부의 저작권 DNS 검열 명령에 결국 철수&quot; — 비영리 보안 DNS Quad9, 프랑스 내 서비스 전면 중단</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">quad9.net — 11월 24일 오전 9시(CET) 기점으로 프랑스 사용자 DNS 질의 전면 거부 결정, 중립적 인터넷 인프라의 위기</span>
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
            <h3 class="minor-detail-headline">스포츠 중계권자(La Liga 등)의 사법적 DNS 차단 명령 압박 끝에 프랑스 서비스를 내린 스위스 비영리 DNS 재단</h3>
            <div class="minor-detail-subheadline">Quad9 공식 공지 · HN 320점 · 160댓글 · 프랑스 내 9.9.9.9 / 149.112.112.112 질의 응답 중단</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  프라이버시 보호와 악성 도메인 차단으로 사랑받던 비영리 재귀 DNS 서비스 Quad9이 11월 24일 오전 9시(파리 시각)부로 프랑스 내 모든 사용자의 DNS 질의를 공식 거부(Refused)하며 서비스를 비활성화했습니다. 앞서 유럽 법원에서 저작권 침해 사이트 차단을 공공 리졸버에까지 강제하는 판결이 잇따르자, 운영 비용과 법적 리스크를 감당하기 어려워진 비영리 DNS 인프라가 국가 단위 철수라는 초강수를 둔 것입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[인터넷 중립성 충돌]</strong> Broadcast Copyright Blocking Orders &rarr; Public Resolver Liability &rarr; Quad9 France Service Exit
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 인프라 임팩트</div>
                <p class="minor-paragraph">
                  오픈 인터넷의 중립적 전화번호부 역할을 하던 공용 DNS가 각국 저작권·검열 법정의 대리 집행 기관으로 변질될 위험에 대한 경종입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://quad9.net/news/blog/quad9-service-deactivation-in-france/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 공지 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50625384" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (160댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: New York Bans Subscription and Post-Purchase Fees on Cars -->
        <div class="minor-item" id="minor-hn-16" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 757점 · 395댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 37.26 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;이미 내 차에 달려 있는 열선 시트·기능에 월 구독료를 물릴 수 없다&quot; — 뉴욕주, 자동차 기능 구독 금지법 서명</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">New York Car Subscription Ban — 호컬 주지사 법안 서명(2027년 2월 발효), 차량 하드웨어 페이월과 테슬라 FSD 영향권까지 395댓글 격론</span>
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
            <h3 class="minor-detail-headline">자동차 제조사들이 이미 장착된 하드웨어 기능을 소프트웨어 잠금으로 묶어 월정액 수익을 짜내던 관행에 제동을 건 뉴욕주 입법</h3>
            <div class="minor-detail-subheadline">뉴욕 주지사실 공식 서명 · HN 757점 (WGNA 파생 기사 145점 클러스터 통합) · 2027년 2월 27일 시행</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  캐시 호컬 뉴욕 주지사가 차량 구매 이후 기존 장착 기능에 반복적인 구독료나 사후 과금을 물리는 행위를 제한하는 법안에 최종 서명했습니다. 90일 뒤인 2027년 2월 27일부터 발효되는 이 법안이 전해지자 해커뉴스에서는 757점(관련 후속 보도 포함 900점 이상)과 395개 댓글이 폭발하며, 제조사의 '하드웨어 페이월'이 소비자 소유권을 얼마나 침해해 왔는지, 그리고 Tesla FSD 구독이나 원격 시동 같은 커넥티드 서비스에는 어떻게 적용될지 치열한 분석이 이어졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[하드웨어 소유권 회복]</strong> Factory-Installed Hardware &rarr; Software Paywall / Monthly Fee &rarr; NY Statutory Ban (Effective Feb 2027)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  소프트웨어 정의 차량(SDV)을 내세우며 반복 매출(ARR)을 노리던 완성차 업계의 구독 수익 모델에 첫 대형 주법 장벽이 세워졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://wgna.com/car-bill-extra-fees/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 관련 보도 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50622774" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (395댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Apple removed my open-source app from EU App Stores after 9 years -->
        <div class="minor-item" id="minor-hn-17" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 612점 · 164댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.88 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;9년간 운영한 오픈소스 앱을 Apple이 EU 앱스토어에서 퇴출하고 고객지원마저 묵살했다&quot; : FSNotes</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">glushchenko/fsnotes — macOS/iOS 인기 마크다운 노트 앱의 EU 강제 삭제와 빅테크 플랫폼 자동화 심사의 벽</span>
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
            <h3 class="minor-detail-headline">EU DSA 사업자 신원 확인과 Apple 앱스토어 자동 통제 속에서 소통 창구 없이 사라지는 1인 오픈소스 앱의 현실</h3>
            <div class="minor-detail-subheadline">GitHub Discussion #2056 · HN 612점 · 164댓글 · 9년 차 오픈소스 노트 앱 FSNotes</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  macOS와 iOS용 오픈소스 마크다운 노트 관리자 <code>FSNotes</code>를 9년간 유지해 온 개발자가 유럽연합(EU) 앱스토어에서 앱이 예고 없이 내려간 뒤 Apple 지원 티켓이 계속 무시당하고 있다는 호소문을 올려 HN 612점을 기록했습니다. 개발자들은 <em>"공식 고객지원 대신 해커뉴스 1면 추천수가 실질적인 고객센터 입장권이 되어버린 기형적 플랫폼 권력"</em>을 강하게 비판했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[플랫폼 게이트키퍼 마찰]</strong> 9-Year Open-Source App &rarr; Automated EU Store Removal &rarr; Unanswered Tickets &rarr; Public HN Escalation
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 생태계 임팩트</div>
                <p class="minor-paragraph">
                  소규모 오픈소스 개발자가 폐쇄형 앱스토어 배포에 의존할 때 겪는 단일 실패 지점(SPOF) 리스크를 적나라하게 드러냈습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/glushchenko/fsnotes/discussions/2056" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 토론 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50616933" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (164댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: GPUI is getting its own repository -->
        <div class="minor-item" id="minor-hn-18" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 377점 · 140댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.56 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Zed 에디터의 심장, 독립 선언&quot; — GPU 가속 Rust UI 프레임워크 'GPUI' 전용 리포지토리 분리</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">zed-industries/gpui (gpui.rs) — 에디터 거대 모노레포에서 떼어내 독립 크레이트·문서 체제로 전환, 라이선스·생태계 기대와 논란 교차</span>
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
            <h3 class="minor-detail-headline">Immediate/Retained 하이브리드 Rust GUI 엔진 GPUI의 독립 리포지토리(★1,555) 출범과 커뮤니티 라이선스 논쟁</h3>
            <div class="minor-detail-subheadline">zed-industries/gpui · gpui.rs · crates.io/crates/gpui · HN 377점 · 140댓글</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  초고속 에디터 Zed의 렌더링 엔진으로 유명한 <code>GPUI</code>가 거대한 Zed 모노레포에서 빠져나와 <code>zed-industries/gpui</code>와 전용 사이트(<code>gpui.rs</code>)로 독립을 선언("See you in a few weeks")하며 HN 377점을 받았습니다. 오늘 GitHub 신생 에뮬레이터 <code>FastEmu</code> 같은 앱들까지 GPUI로 만들어질 만큼 인기가 높지만, 댓글에서는 기존 <code>crates/ui</code> 요소들의 제한적 라이선스 정책이 독립 이후 완치될지 여부와 문서화 부족을 날카롭게 짚었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[Rust GUI 생태계 분화]</strong> Zed Monorepo (Internal GPUI) &rarr; Standalone <code>zed-industries/gpui</code> &rarr; Ecosystem Crates &amp; License Review
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Rust 데스크톱 GUI 춘추전국시대에서 GPU 직접 가속 하이브리드 엔진이 범용 앱 프레임워크로 도약하기 위한 분수령입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/zed-industries/gpui" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://news.ycombinator.com/item?id=50619103" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (140댓글)
              </a>
            </div>
          </div>
        </div>

      </div>
    </section>
"""
