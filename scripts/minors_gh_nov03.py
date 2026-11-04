# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-11-03

GH_MINORS = """
      <!-- [GH 0~10h] Item 1: Balanov/shim -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 142개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.3시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.5 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;외부 의존성 제로의 7MB 초경량 로컬 AI 하네스&quot; : Balanov/shim</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Balanov/shim — 어떤 LLM 모델이든 MCP 프로토콜과 Agent Skills를 즉시 바인딩하여 자연어 CLI 환경을 구축하는 순수 Go 기반 미니멀 런타임</span>
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
          <h3 class="minor-detail-headline">단일 정적 바이너리로 구동되는 무의존성 AI 하네스: shim</h3>
          <div class="minor-detail-subheadline">복잡한 파이썬 환경 구축 없이 어디서나 즉시 실행되는 초경량 로컬 퍼스트 AI 제어기</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                최근 AI 에이전트 프레임워크들이 수 기가바이트의 파이썬 종속성과 수십 개의 node_modules를 요구하며 비대해진 가운데, 단 하나의 독립 실행형 바이너리로 모든 로컬/원격 LLM과 표준 MCP 서버를 완벽하게 연결할 수 있는 미니멀 도구로 Go 개발자들의 열광적인 지지를 얻었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[하네스 아키텍처]</strong> User CLI &rarr; shim Core (Pure Go) &rarr; JSON-RPC MCP Socket &rarr; Local / Cloud LLM Pipeline
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Docker 컨테이너나 Alpine Linux 등 최소 환경에서도 추가 설치 없이 즉시 실행되며, 터미널 표준 입출력(stdio) 기반으로 다른 셸 스크립트 파이프라인과 완벽히 융합됩니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/Balanov/shim" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: larajeftic/memechain -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 46개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.2시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;브라우저에서 채굴하고 액션으로 검증하는 밈 블록체인&quot; : larajeftic/memechain</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">larajeftic/memechain — GitHub Actions 러너가 퍼블릭 테스트넷을 채굴하고 브라우저 Web Workers로 밈 아트를 인스크립션하는 유희적 PoW 블록체인</span>
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
          <h3 class="minor-detail-headline">깃허브 인프라와 브라우저가 만난 기상천외한 PoW 실험: memechain</h3>
          <div class="minor-detail-subheadline">블록체인 학습과 유희를 결합하여 실제 동작하는 분산 원장의 핵심 원리를 시각화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                복잡한 금융 투기판으로 변질된 웹3 생태계에 반기를 들고, 비트코인의 원시 작업증명(Proof-of-Work) 알고리즘과 트랜잭션 전파를 순수 파이썬과 브라우저 자바스크립트만으로 투명하게 구현하여 커뮤니티의 유쾌한 찬사를 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[인스크립션 루프]</strong> Browser Canvas Drawing &rarr; SHA-256 Nonce Mining &rarr; GitHub Actions Consensus Validator &rarr; Mempool Broadcast
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                깃허브 레포지토리의 커밋 히스토리를 불변 원장의 체크포인트로 삼는 독창적인 아이디어로 분산 시스템 교육용 교재로서의 가치를 입증했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/larajeftic/memechain" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: 0xCodez/pulsr -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 29개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.8시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;구독료 없는 애플워치용 리퀴드 글래스 생체 회복 코치&quot; : 0xCodez/pulsr</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">0xCodez/pulsr — Whoop의 고가 월 구독 모델에 맞서 100% 온디바이스에서 심박변이도(HRV)와 수면 스트레인을 분석하는 오픈소스 건강 트래커</span>
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
          <h3 class="minor-detail-headline">내 건강 데이터의 주권을 되찾다: Pulsr</h3>
          <div class="minor-detail-subheadline">Apple Watch 센서 데이터를 로컬 신경망으로 해석해 프라이버시 침해 없이 신체 회복도 산출</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                웨어러블 기기 시장이 매달 30달러에 달하는 정기 구독료를 요구하며 생체 데이터를 기업 클라우드에 가두는 행태에 맞서, 애플 HealthKit 원시 데이터를 기기 내에서 직접 가공하여 유려한 Liquid Glass UI로 보여주는 대안으로 호평을 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[생체 알고리즘]</strong> HealthKit SDNN/RMSSD &rarr; On-Device Strain Model &rarr; Circadian Sleep Analysis &rarr; Pure Swift Local Render
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                외부 서버와의 통신이 전면 차단되어 배터리 소모가 극소화되었으며, 사용자의 심박수와 수면 기록이 단 1비트도 외부로 유출되지 않는 완벽한 안전지대를 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/0xCodez/pulsr" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 4: egoist/godraw -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 136개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 9.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스타 개발자 egoist가 mygo로 빚어낸 초경량 무한 캔버스&quot; : egoist/godraw</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">egoist/godraw — 유명 오픈소스 장인 egoist가 Go 언어 기반 초소형 컴파일러 mygo를 활용해 구현한 60fps 무한 인터랙티브 드로잉 보드</span>
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
          <h3 class="minor-detail-headline">웹 기술의 한계를 시험하는 장인정신: godraw</h3>
          <div class="minor-detail-subheadline">수만 개의 벡터 도형이 펼쳐져도 단 1프레임의 버벅임 없는 극단적 성능 최적화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Excalidraw나 tldraw 같은 기존 웹 기반 무한 캔버스들이 무거운 자바스크립트 번들과 가비지 컬렉션(GC) 스터터링으로 고전할 때, Go 언어를 직접 웹어셈블리(Wasm)로 컴파일하여 메모리 할당을 극도로 통제한 실험작으로 개발자들의 눈길을 사로잡았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[렌더링 엔진]</strong> mygo AST Parser &rarr; WebAssembly Bytecode &rarr; WebGL Raw Quad Buffer &rarr; Zero-GC Viewport Pan/Zoom
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                전체 바이너리 크기가 수백 킬로바이트 수준으로 압축되어 모바일 저사양 브라우저에서도 즉각 구동되며, 고성능 웹 그래픽스의 새로운 벤치마크를 제시했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/egoist/godraw" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: shashvat1965/slidesense -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 78개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;맥북 트랙패드 테두리를 0ms 물리 볼륨/밝기 슬라이더로 전환&quot; : shashvat1965/slidesense</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">shashvat1965/slidesense — 멀티터치 원시 이벤트를 인터셉트하여 트랙패드 좌우 여백을 스마트 터치 슬라이더로 변환하는 초경량 macOS 유틸리티</span>
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
          <h3 class="minor-detail-headline">트랙패드의 숨겨진 여백을 깨우는 센서 핵: SlideSense</h3>
          <div class="minor-detail-subheadline">키보드 단축키를 누르거나 마우스를 뗄 필요 없이 손가락 슬라이드 한 번으로 시스템 제어</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                애플이 터치바를 폐지한 이후 볼륨과 화면 밝기를 조절하기 위해 기능 키를 더듬어야 했던 불편함에 착안, 트랙패드의 가장 바깥쪽 5% 영역을 전용 슬라이더 영역으로 인식시키는 번뜩이는 발상으로 맥 유저들의 열렬한 호응을 얻었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[이벤트 가로채기]</strong> MultitouchPrivateAPI &rarr; Edge Coordinates Filter (X &lt; 5% or &gt; 95%) &rarr; CoreAudio / DisplayServices Direct Hook
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                일반적인 포인터 이동이나 제스처와 충돌하지 않도록 엄격한 속도 및 진입 각도 감지 알고리즘을 적용하여 오작동률을 0%에 수렴시켰습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/shashvat1965/slidesense" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: andrewnakas/gtav-recomp -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 48개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.7 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;콘솔 바이너리를 C++ 코드로 역컴파일 재빌드한다&quot; : andrewnakas/gtav-recomp</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">andrewnakas/gtav-recomp — ReXGlue 엔진을 활용해 Xbox 360용 GTA V 바이너리를 현대 PC용 네이티브 C++ 코드로 정적 재컴파일하는 리버스 엔지니어링 프로젝트</span>
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
          <h3 class="minor-detail-headline">에뮬레이터를 뛰어넘는 정적 재컴파일의 충격: gtav-recomp</h3>
          <div class="minor-detail-subheadline">PowerPC 명령어를 네이티브 x86-64 코드로 치환하여 오버헤드 없는 완전한 포팅 실현</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                N64의 젤다의 전설에서 시작된 '정적 재컴파일(Static Recompilation)' 혁명이 7세대 거대 AAA 타이틀인 GTA V에 도달했습니다. 무거운 가상 머신(Xenia) 없이 게임 실행 코드를 순수 C++로 변환해 컴파일하는 시도로 에뮬레이션 씬에 거대한 파장을 일으켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[재컴파일 파이프라인]</strong> Xbox 360 XEX Binary &rarr; ReXGlue Disassembler &rarr; PowerPC to C++ Intermediate AST &rarr; Vulkan Native Runtime Link
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                CPU 에뮬레이션 오버헤드가 완전히 사라져 초저사양 PC나 UMPC 핸드헬드 기기에서도 고주사율 60fps 구동이 가능해지며 비디오 게임 보존의 기술적 분기점을 열었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/andrewnakas/gtav-recomp" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 7: AssassinCreator/steam-stash-value-report-card -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 590개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.5시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;계정 로그인 없이 스팀 보관함 실시간 시세를 카드 한 장으로 요약&quot; : Steam Stash Report</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">AssassinCreator/steam-stash-value-report-card — 비밀번호 탈취 위험 없이 공개 프로필만으로 장터 실시간 시세를 계산해 세련된 공유용 리포트 카드로 뽑아주는 CLI</span>
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
          <h3 class="minor-detail-headline">게이머의 숨은 자산을 발굴하는 투명한 시세 분석기</h3>
          <div class="minor-detail-subheadline">악성 피싱 사이트에 계정을 연동하지 않고도 내 스팀 보관함 가치를 한눈에 검증</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                스팀 인벤토리 평가 사이트들이 서드파티 로그인 토큰을 요구해 계정 도용 피해가 빈번했던 문제를 해결하기 위해, 공개 인벤토리 엔드포인트만 안전하게 스크래핑하여 단일 포터블 바이너리로 리포트 카드를 생성하는 안전성으로 게이머들의 폭발적인 추천을 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[데이터 파이프라인]</strong> Public SteamID64 &rarr; Community Market Price History Aggregator &rarr; Volume Liquidity Weighting &rarr; Terminal ANSI Share Card
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단순 최저 호가가 아닌 실제 체결 거래량 가중 평균가(VWAP)를 적용하여 거품 낀 아이템 시세를 정확하게 필터링해 내는 실전 금융 알고리즘을 도입했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/AssassinCreator/steam-stash-value-report-card" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: justrach/nanolight -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 215개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.4시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;nanoui로 그려낸 1MB짜리 맥 전용 ⌘Space 초경량 런처&quot; : justrach/nanolight</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">justrach/nanolight — 수백 메가바이트의 Electron 런처를 조롱하듯 Zig 언어와 초소형 UI 엔진으로 0.01초 만에 뜨는 미니멀 스포트라이트</span>
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
          <h3 class="minor-detail-headline">시스템 자원을 낭비하지 않는 진정한 네이티브 런처: nanolight</h3>
          <div class="minor-detail-subheadline">수식 계산, 구글 실시간 제안, X/Grok 검색 패널을 단일 경량 팝업 창에 집약</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Raycast나 Alfred 같은 런처들이 점차 무거워지고 유료 구독 기능을 강요하는 추세에 피로감을 느낀 개발자들이, 순수 Zig 언어로 컴파일되어 램을 단 8MB만 사용하는 초경량 네이티브 도구의 등장에 뜨거운 갈채를 보냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[런처 파이프라인]</strong> Global ⌘Space Event &rarr; Zig Nanoui Metal Context &rarr; Local Math AST / Async HTTP Autocomplete &rarr; Instant Keypress Action
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Metal 하드웨어 가속을 이용해 창이 뜨는 순간 프레임 드랍이 전혀 없으며, 메모리 누수가 발생할 수 없는 Zig 특유의 엄격한 수동 메모리 할당자(GPA) 설계를 채택했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/justrach/nanolight" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: ravencaio/tlou-remastered-pc -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 139개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.3시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;Vulkan 렌더러와 커스텀 런타임으로 PS4 대작을 PC에 직접 심다&quot; : TLOU Remastered PC</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ravencaio/tlou-remastered-pc — 에뮬레이터 없이 PS4 자체 x86-64 바이너리를 윈도우 환경에서 네이티브 실행하는 오픈소스 포트 런타임</span>
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
          <h3 class="minor-detail-headline">콘솔 독점의 장벽을 허무는 리버스 엔지니어링 포트</h3>
          <div class="minor-detail-subheadline">PS4 시스템 콜과 그래픽스 라이브러리를 현대 PC Vulkan 백엔드로 직접 리바인딩</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                PS4가 PC와 동일한 x86-64 CPU 아키텍처를 공유한다는 점에 착안, 무거운 가상화 계층을 완전히 걷어내고 운영체제 API만 윈도우 네이티브로 번역하여 공식 PC 리메이크의 발적화 문제를 뛰어넘는 놀라운 퍼포먼스를 보여주었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[포팅 아키텍처]</strong> PS4 ELF/Self Executable &rarr; Custom x86-64 Loader &rarr; Reimplemented LibKernel/LibGnm &rarr; Vulkan SPIR-V Translator
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                게임 원본 파일(CUSA00552)을 사용자가 직접 제공해야 하는 클린룸(Clean-room) 방식으로 개발되어 저작권 침해 논란을 원천 차단하고 순수 기술적 런타임만 배포하는 모범을 보였습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/ravencaio/tlou-remastered-pc" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>
"""
