# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-10-28

HN_MINORS = """
      <!-- [HN 0~10h] Item 10: Git for US Legislation -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 133점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 39.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;미국 법률 200년 개정을 Git 커밋으로 본다&quot; : 미국 법전(US Code)의 형상관리 혁명</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Lexifina — 의회 수정안을 Pull Request로, 법률 조항 변경을 Git Diff로 완벽하게 시각화</span>
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
          <h3 class="minor-detail-headline">입법 관료주의의 불투명성을 깬 엔지니어링 개가: Git for US Code</h3>
          <div class="minor-detail-subheadline">수천 페이지에 달하는 미국 법전의 개정 이력을 프로그래밍 언어의 소스코드처럼 추적하고 브랜치 비교</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                의회에서 통과되는 법안들은 수십 년 전 법전의 '몇 조 몇 항의 단어를 삭제하고 대체한다'는 식의 난해한 텍스트로 구성되어 일반 시민이나 법조인조차 실제 법률이 어떻게 바뀌는지 직관적으로 알기 어려웠습니다. Lexifina는 미국 법전 전체를 Git 리포지토리로 변환하여 누구나 커밋 히스토리와 diff로 법률 변경을 확인할 수 있게 했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> US Code XML Bulk Data &rarr; Semantic Section Parser &rarr; Chronological Git Commits &rarr; Interactive Web Diff & Blame View
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                입법 연구원들이 특정 법 조항의 원작자(Author)와 개정 연혁을 <code>git blame</code> 형태로 즉시 추적할 수 있어 법률 분석 시간이 획기적으로 단축되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://lexifina.com/blog/git-for-the-us-code" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 블로그 아티클</a>
            <a href="https://news.ycombinator.com/item?id=50268380" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (133점 / 58댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 11: Survival LLM -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 255점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 27.5 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;전력망과 인터넷이 끊겨도 작동한다&quot; : 오프라인 비상 생존 AI 라이브러리</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Survival LLM (brangus.io) — 위키피디아·응급의학·야외생존 지식을 단일 노트북에서 0와트로 구동</span>
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
          <h3 class="minor-detail-headline">아포칼립스를 대비하는 디지털 노아의 방주: Survival LLM</h3>
          <div class="minor-detail-subheadline">인터넷 차단, 자연재해 상황에서 인류 문명의 핵심 지식을 검색하고 대화형으로 안내하는 로컬 어시스턴트</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                클라우드 의존적인 현대 기술 문명이 태풍, 지진, 전력망 붕괴 등 비상사태에서 무력화되는 위기감이 커졌습니다. Survival LLM은 방대한 의학 매뉴얼, 정수법, 전기 설비 수리 지식을 초경량 양자화 LLM과 결합하여 배터리 전력만으로 구동되도록 패키징되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Curated Emergency Knowledge &rarr; SQLite FTS5 Index &rarr; Offline Quantized LLM (llama.cpp) &rarr; Zero-Network Localhost WebUI
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                128GB USB 메모리 스틱 하나에 인류의 생존 지식과 추론 엔진 전체를 담아 어떤 구형 PC에서도 즉시 부팅 실행할 수 있는 자립성을 확보했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.brangus.io/survival-llm" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 웹사이트</a>
            <a href="https://news.ycombinator.com/item?id=50264853" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (255점 / 120댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 12: Tailscale SSH -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 242점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;제로 트러스트의 심장을 긴급 수술하다&quot; : Tailscale SSH 보안 조사 및 조치 업데이트</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Tailscale — SSH 세션 키 검증 결함에 대한 투명한 기술 포스트모템 및 전역 인프라 안전 패치</span>
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
          <h3 class="minor-detail-headline">투명한 공개로 신뢰를 지켜낸 엔지니어링: Tailscale SSH Incident</h3>
          <div class="minor-detail-subheadline">노드 간 세션 핸드셰이크 과정에서 발견된 엣지 케이스 취약점을 전사적 키 교체와 커널 패치로 즉시 방어</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                수많은 기업의 내부 인프라 접속을 지탱하는 Tailscale SSH에서 특정 조건 하의 세션 키 검증 예외가 발견되었습니다. Tailscale 팀은 사고 은폐 없이 전 과정을 초 단위 타임라인으로 투명하게 공개하고 근본적 아키텍처 개선안을 공유하여 커뮤니티의 찬사를 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[조치 파이프라인]</strong> Vulnerability Triage &rarr; Root-Cause Code Audit &rarr; Global Coordination Server Hotfix &rarr; Client Key Rotation & Post-Mortem Release
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                소프트웨어 정의 네트워크(SDN)에서 암호화 세션 키 수명 주기와 노드 신원 증명 메커니즘을 한 단계 더 강화하는 모범 사례를 확립했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://tailscale.com/ssh-investigation-update" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 조사 보고서</a>
            <a href="https://news.ycombinator.com/item?id=50264857" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (242점 / 120댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 13: Ghostty 1.4 -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 871점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 70.7 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;미첼 하시모토의 역작, 정점에 도달하다&quot; : GPU 가속 터미널 Ghostty 1.4 대규모 릴리즈</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ghostty.org — HashiCorp 창업자가 바닥부터 깎아 만든 네이티브 고성능 터미널의 완성형</span>
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
          <h3 class="minor-detail-headline">개발자의 손가락 끝에 붙는 궁극의 반응속도: Ghostty 1.4</h3>
          <div class="minor-detail-subheadline">Metal 및 OpenGL 네이티브 렌더러, 커스텀 셰이더, 서브픽셀 텍스트 렌더링 최적화 탑재</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                일렉트론 기반 터미널들의 무거운 지연시간과 글리치에 지친 개발자들 사이에서, 테라폼 창시자 미첼 하시모토가 Zig 언어로 개발한 Ghostty는 혁신 그 자체였습니다. 이번 1.4 릴리즈는 멀티플랫폼 창 분할, 셰이더 효과, 전력 소비 절감에서 극적인 도약을 이뤄냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Zig Core Native Binary &rarr; GPU Pipeline (Metal/Vulkan) &rarr; Zero-Latency Input Loop &rarr; Custom Pixel Shader Post-Processing
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                120Hz 고주사율 모니터에서도 프레임 드롭 0%의 완벽한 스크롤링과 키 입력 응답성을 달성하여 에이전트 CLI 출력 스트리밍의 최고 파트너로 자리 잡았습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://ghostty.org/docs/install/release-notes/1-4-0" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 릴리즈 노트</a>
            <a href="https://news.ycombinator.com/item?id=50261998" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (871점 / 272댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 14: Genie 4 -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 804점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 61.5 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;물리 엔진 없는 가상 현실이 열린다&quot; : 구글 딥마인드 차세대 월드 시뮬레이터 Genie 4</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">deepmind.google — 텍스트와 프롬프트만으로 실시간 인터랙션 가능한 물리 세계를 신경망으로 직접 생성</span>
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
          <h3 class="minor-detail-headline">게임 개발과 로보틱스의 패러다임을 바꿀 신경망 월드: Genie 4</h3>
          <div class="minor-detail-subheadline">키보드 조작과 카메라 궤적에 따라 충돌, 중력, 빛 반사를 신경망이 실시간 렌더링</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 비디오 생성 AI는 단순히 정해진 영상을 수동적으로 보여주는 데 그쳤습니다. 딥마인드의 Genie 4는 사용자의 액션 입력(조작키, 마우스)을 실시간 조건부 인과관계로 수용하여 게임 플레이가 가능한 인터랙티브 환경을 직접 계산해 냅니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> User Controller Action &rarr; Spatiotemporal Latent World Model &rarr; Physical Dynamics Prediction &rarr; 60fps Real-time Neural Stream
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                로봇 에이전트의 강화학습(RL)을 실제 현실이 아닌 무한히 생성되는 신경망 시뮬레이션 안에서 수백만 배 속도로 학습시킬 수 있는 시뮬레이션 혁명을 열었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 딥마인드 연구 블로그</a>
            <a href="https://news.ycombinator.com/item?id=50261319" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (804점 / 489댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 15: Python's experimental JIT to be removed -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 469점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.9시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;득보다 실이 컸다&quot; : 파이썬 코어 개발팀, CPython 실험적 JIT 컴파일러 전면 제거 합의</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">lwn.net — 기대에 못 미친 성능 향상과 코드베이스 복잡도 증가로 인해 3.14 릴리즈에서 JIT 제외 결정</span>
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
          <h3 class="minor-detail-headline">실용주의로 회귀한 귀도 반 로섬과 코어 팀: Python JIT 퇴출</h3>
          <div class="minor-detail-subheadline">복잡한 기계어 컴파일 대신 티어2 인터프리터 최적화와 메모리 구조 개선에 집중하기로 결의</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                파이썬 3.13에서 실험적으로 도입되었던 카피-앤-패치(Copy-and-patch) JIT 컴파일러는 유지보수 비용과 바이너리 크기 증가 대비 실제 벤치마크 성능 향상이 미미했습니다. 코어 팀은 과감히 레거시를 덜어내는 어려운 결단을 내렸습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[로드맵 전환]</strong> Experimental JIT Deprecation &rarr; Tier-2 Bytecode Specializer &rarr; Free-Threaded (No-GIL) Core Optimization Focus
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                불필요한 복잡도를 덜어냄으로써 파이썬 3.14의 핵심 목표인 '노-GIL(No-GIL) 멀티코어 병렬성'과 '빠른 시동 시간'에 모든 엔지니어링 리소스를 집중하게 되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> LWN 심층 분석 기사</a>
            <a href="https://news.ycombinator.com/item?id=50257419" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (469점 / 253댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 16: The Mythical Man-Month in the Age of AI -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 448점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.7시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.7 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI 에이전트를 더 많이 투입할수록 프로젝트는 더 늦어진다?&quot; : 인공지능 시대의 맨먼스 미신</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">j11g.com — 프레더릭 브룩스의 1975년 명저가 자율 에이전트 시대에 다시 던지는 차가운 통찰</span>
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
          <h3 class="minor-detail-headline">에이전트 군단의 함정: 브룩스의 법칙은 여전히 건재하다</h3>
          <div class="minor-detail-subheadline">인력 대신 AI 서브에이전트를 무한대로 복제할 때 발생하는 컨텍스트 오염과 검증 비용의 기하급수적 폭증</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                "에이전트 100개를 동시에 돌려 하룻밤 만에 대규모 시스템을 완성하겠다"는 환상이 커지고 있습니다. 본 에세이는 에이전트 간 의사소통 프로토콜의 오버헤드와 인간 아키텍트의 인지적 검증 한계를 수리적으로 증명하여 전 세계 테크 리더들의 격한 공감을 이끌어냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[인과관계 그래프]</strong> More Sub-Agents &rarr; O(N^2) Context Drift & Cross-Hallucination &rarr; Exponential Review Burden on Human Architect
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                무조건적인 에이전트 병렬화 대신 단일 에이전트의 사양서(Spec) 완성도와 엄격한 결정론적 테스트 게이트가 프로젝트 성공의 절대 요소임을 환기시켰습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://j11g.com/the-mythical-man-month-in-the-age-of-ai" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 원문 에세이 읽기</a>
            <a href="https://news.ycombinator.com/item?id=50255298" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (448점 / 185댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 17: 16-bit Windows on 64-bit Windows (winevdm) -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 138점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.9시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.9 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;최신 윈도우 11 위에서 윈도우 3.1 앱을 살려내다&quot; : 64비트 OS 위 16비트 바이너리 에뮬레이션</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">otya128/winevdm — 마이크로소프트가 제거한 NTVDM을 대신해 30년 전 소프트웨어를 무결점 구동</span>
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
          <h3 class="minor-detail-headline">사라진 16비트의 혼을 복원한 해커 정신: winevdm</h3>
          <div class="minor-detail-subheadline">x86-64 롱 모드에서 지원되지 않는 16비트 세그먼트 주소 지정을 사용자 공간 CPU 에뮬레이션으로 극복</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                산업 현장과 공장 자동화에는 아직도 1990년대 초반 16비트로 작성된 독점 제어 소프트웨어가 필수적입니다. 마이크로소프트가 64비트 Windows에서 16비트 서브시스템(NTVDM)을 완전히 삭제해 폐기 위기에 놓였던 레거시 앱들을 winevdm이 완벽히 구원했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> 16-bit Win16 Binary &rarr; winevdm Loader Hook &rarr; User-Space 8086/286 Emulator &rarr; Win32 API Translation Layer
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                가상머신(VM)이나 DOSBox 없이도 일반 최신 윈도우 앱처럼 더블클릭만으로 창이 매끄럽게 뜨는 경이로운 하위 호환성을 선사합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/otya128/winevdm" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
            <a href="https://news.ycombinator.com/item?id=50253529" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (138점 / 45댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 18: Writing about pratt parsing so I remember it -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 83점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.6 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;연산자 우선순위의 지옥을 탈출하는 법&quot; : 가장 우아한 수식 파서, 프랫 파싱(Pratt Parsing) 해설</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">unix.dog/~yosh — 재귀 하강 파서의 한계를 바인딩 파워(Binding Power)로 돌파하는 알고리즘의 미학</span>
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
          <h3 class="minor-detail-headline">컴파일러 제작자들의 오랜 비밀 병기: Pratt Parsing</h3>
          <div class="minor-detail-subheadline">전위·중위·후위 연산자가 엉킨 복잡한 수식을 테이블 없이 단 20줄의 직관적 재귀 함수로 파싱하는 기술</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                프로그래밍 언어 인터프리터나 독자적 쿼리 언어(DSL)를 설계할 때 수식 파싱은 가장 까다로운 난관입니다. 본 아티클은 1973년 본 프랫(Vaughan Pratt)이 고안한 알고리즘을 현대적인 감각과 직관적인 다이어그램으로 풀어내어 전 세계 언어 제작자들의 찬사를 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파싱 알고리즘 루프]</strong> Token Stream &rarr; Prefix Parse Function &rarr; Loop While (Current Precedence &lt; Next Binding Power) &rarr; Infix Combine AST
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Rust, Go, TypeScript 등 현대 시스템 언어로 작성되는 AST 파서의 코드 가독성과 실행 성능을 동시에 극대화하는 표준 레퍼런스를 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.unix.dog/~yosh/blog/2026-10-25_pratt-parsing.html" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 블로그 원문 읽기</a>
            <a href="https://news.ycombinator.com/item?id=50255177" target="_blank" class="project-link hacker-news"><i data-lucide="message-square"></i> HN 토론 (83점 / 32댓글)</a>
          </div>
        </div>
      </div>
"""

print("minors_hn_oct28 loaded successfully.")
