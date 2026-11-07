# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-08

HN_MINORS = """
      <!-- ==================== HACKER NEWS BUCKET 1 (0~18h) ==================== -->
      <!-- [HN 0~18h] Item 10: Need for Speed Underground 2 in browser -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~18h</span>
              <span class="minor-metric">🔺 733점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.2시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 55.6 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;추억의 명작 레이싱 게임을 브라우저에서 60FPS로 돌리다&quot; : nfsu2.xyz</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Need for Speed Underground 2 online in the browser — Wasm과 WebGL을 결합하여 설치 없이 웹 탭 안에서 완벽히 실행되는 오픈소스 레이싱 포트</span>
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
          <h3 class="minor-detail-headline">고전 x86 윈도우 바이너리를 현대 웹 기술로 완벽히 되살려낸 역공학</h3>
          <div class="minor-detail-subheadline">WebAssembly 메모리 가상화와 WebAudio, 게임패드 API를 직결한 브라우저 네이티브 에뮬레이션</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                2004년 출시된 전설적인 레이싱 게임 NFSU2의 물리 엔진과 그래픽 렌더러를 웹 브라우저에서 다운로드 없이 즉시 실행할 수 있게 복원하여 전 세계 게이머들의 폭발적인 향수를 자극했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Game Asset Streaming &rarr; Emscripten Wasm Runtime &rarr; WebGL 2.0 Shader Pipeline &rarr; 60FPS Zero-Install In-Browser Racing
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                DirectX 9 드로콜을 WebGL 2.0 셰이더로 실시간 변환하고, P2P WebRTC 데이터 채널을 통해 별도 서버 없이도 브라우저 간 저지연 멀티플레이어 레이싱을 구현했습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://nfsu2.xyz/" target="_blank" class="minor-link demo">
              <i data-lucide="globe" class="minor-icon"></i> 웹 데모 실행
            </a>
            <a href="https://news.ycombinator.com/item?id=43290456" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~18h] Item 11: $10 USD OpenStick homelab -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~18h</span>
              <span class="minor-metric">🔺 236점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.6시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 51.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;1만 원짜리 LTE USB 모뎀을 완전한 리눅스 서버로 개조하다&quot; : OpenStick Homelab</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">What I run on my $10 USD OpenStick homelab — 알리익스프레스 10달러 4G 모뎀에 데비안 리눅스를 올려 홈랩 서버로 탈바꿈시킨 시스템 해킹기</span>
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
          <h3 class="minor-detail-headline">스냅드래곤 410 SoC와 512MB RAM으로 구축한 초저전력 1W 마이크로 서버</h3>
          <div class="minor-detail-subheadline">Tailscale 메시 VPN, Pi-hole DNS 차단기, 로컬 MQTT 브로커를 단 1와트 소비전력으로 상시 구동</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                값비싼 라즈베리 파이나 고전력 미니 PC 없이도, 버려지는 4G LTE USB 동글의 하드웨어 부트로더를 잠금 해제해 완전한 리눅스 배포판을 구동할 수 있다는 가능성을 보여주었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Snapdragon 410 USB Dongle &rarr; EDL Bootloader Unlock &rarr; Debian 12 Minimal &rarr; Tailscale & Pi-hole Edge Node
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                ZRAM 스왑 압축과 경량 패키지 튜닝을 통해 512MB라는 극도로 제한된 램에서도 시스템 프리징 없이 안정적으로 백그라운드 데몬들을 구동하는 경량화 노하우를 공유했습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://blog.bosscher.ch/posts/openstick/" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> 원문 블로그 보기
            </a>
            <a href="https://news.ycombinator.com/item?id=43293012" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~18h] Item 12: Mac undocumented family member classifier -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~18h</span>
              <span class="minor-metric">🔺 545점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 41.8 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;모든 맥북에 숨겨진 애플의 비공개 가족·지인 분류 모델&quot; : PKG Classifier</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Every Mac comes with an undocumented family member classifier — macOS 시쿼이아 시스템 내부에서 발견된 애플 인텔리전스의 개인 지식 그래프(PKG) 리버스 엔지니어링</span>
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
          <h3 class="minor-detail-headline">아이메시지와 사진 데이터를 분석해 혈연관계를 추론하는 온디바이스 그래프</h3>
          <div class="minor-detail-subheadline">사용자 동의 창 없이 백그라운드 데몬에서 상시 가동되는 관계 추론(Kinship Inference) 엔진의 실체</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                애플 인텔리전스(Apple Intelligence)가 사용자의 Siri 질문에 답변하기 위해 로컬 맥OS 파일시스템 깊숙한 곳에서 사용자의 부모, 배우자, 자녀 관계를 몰래 점수화하고 있는 바이너리가 적발되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Photos & iMessage Metadata &rarr; CoreKnowledge.framework &rarr; On-Device PKG Classifier &rarr; Kinship Confidence Matrix
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                클라우드로 데이터를 전송하지는 않으나, 온디바이스 프라이버시를 표방하는 애플 OS 내부에서도 사용자가 제어할 수 없는 불투명한 인구통계학적 추론이 이뤄지고 있다는 점이 해커뉴스에서 거센 논쟁을 불렀습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://8rank.ai/game/apple-intelligence-personal-knowledge-graph" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> 분석 보고서
            </a>
            <a href="https://news.ycombinator.com/item?id=43289945" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 2 (18~35h) ==================== -->
      <!-- [HN 18~35h] Item 13: A Jev that can ask Opus for help -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 18~35h</span>
              <span class="minor-metric">🔺 568점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.1 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;경량 판정 모델이 Opus에게 SOS를 치면 비용이 4배 줄어든다&quot; : Jev-Opus Hybrid</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost — 확신도(Confidence) 기반 계층적 에스컬레이션으로 엔터프라이즈 LLM 비용을 75% 절감한 아키텍처</span>
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
          <h3 class="minor-detail-headline">모든 요청에 비싼 초거대 모델을 쓰지 않고 신뢰도 임계값으로 분기하는 지혜</h3>
          <div class="minor-detail-subheadline">90%의 평이한 케이스는 초저가 모델이 10ms 만에 판정하고, 모호한 10%만 최상위 모델로 포워딩</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                데이터 식별 및 고객 신원 확인(Identity Resolution) 작업에 고가의 Claude Opus를 전수 투입하다가 수억 원의 청구서 폭탄을 맞던 기업들에게 가장 실용적인 비용 최적화 설계도를 제시했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> High-Volume Entity Records &rarr; Fast Small Judge (Jev/Haiku) &rarr; Confidence < 0.85 Check &rarr; Claude Opus Escalation
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단순 앙상블이 아니라 소프트맥스 엔트로피와 설명 가능성 점수를 결합한 스마트 라우팅으로, 전체 데이터셋에서 99.4%의 Opus 동일 정확도를 유지하면서도 연산 비용을 정확히 4분의 1로 압축했습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://hightouch.com/blog/llm-judges-identity-resolution" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> 기술 블로그 보기
            </a>
            <a href="https://news.ycombinator.com/item?id=43282110" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 18~35h] Item 14: Firecracker VM Escape -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 18~35h</span>
              <span class="minor-metric">🔺 277점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.2시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AWS 람다의 철옹성을 뚫다: 파이어크래커 VM 탈출 해부&quot; : PwnEscape Part 2</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Firecracker VM Escape: PwnEscape Part 2 — AWS Lambda와 Fargate의 기초가 되는 Rust 가상화 하이퍼바이저의 vhost-user 취약점 실전 익스플로잇</span>
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
          <h3 class="minor-detail-headline">메모리 안전 언어 Rust로 작성된 마이크로VM도 피해갈 수 없었던 논리 버그</h3>
          <div class="minor-detail-subheadline">KVM 메모리 슬롯 공유 레이스 컨디션을 악용해 게스트 VM 권한으로 호스트 루트 쉘 획득</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                아마존웹서비스(AWS)의 서버리스 인프라 전체를 지탱하는 핵심 격리 기술인 파이어크래커(Firecracker)에서 완전한 VM 탈출(VM Escape) 시나리오가 상세한 PoC와 함께 공개되어 클라우드 보안계에 큰 충격을 주었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Guest Micro-VM Payload &rarr; Virtio Shared Memory Race &rarr; KVM Host Page Overwrite &rarr; Root Shell Escape
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Rust로 작성된 소프트웨어라 할지라도 unsafe 블록과 C 기반 리눅스 커널 KVM 시스템 콜이 만나는 인터페이스에서의 엄격한 경계 검증이 얼마나 중대한지 교훈을 남겼습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://pwn.ai/blog/firecracker-escape" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> 보안 분석 원문
            </a>
            <a href="https://news.ycombinator.com/item?id=43281988" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 18~35h] Item 15: Bare-metal programming using UEFI -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 18~35h</span>
              <span class="minor-metric">🔺 246점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 30.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;운영체제 없이 CPU 위에서 직접 코드를 돌리는 법&quot; : UEFI Bare-Metal</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">First steps in bare-metal programming using UEFI — 리눅스나 윈도우 커널 없이 x86_64 CPU 전원이 켜지자마자 실행되는 순수 C 펌웨어 앱 작성 가이드</span>
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
          <h3 class="minor-detail-headline">BIOS의 유물에서 벗어나 최신 64비트 롱 모드(Long Mode)를 곧바로 장악하다</h3>
          <div class="minor-detail-subheadline">복잡한 어셈블리어 부트로더 없이 표준 C 컴파일러(Clang/GCC)로 부팅 가능한 .efi 바이너리 빌드</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                과거 베어메탈 시스템 프로그래밍은 16비트 리얼 모드와 A20 게이트를 다루는 악몽 같은 작업이었으나, UEFI 표준 덕분에 현대 64비트 하드웨어를 직접 제어하는 문턱이 획기적으로 낮아졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Standard C99 Source &rarr; Clang Target x86_64-unknown-windows &rarr; bootx64.efi &rarr; Pure Hardware Screen Output
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                자신만의 초경량 OS 커널을 개발하거나 고성능 하이퍼바이저 펌웨어를 연구하는 엔지니어들에게 가장 직관적인 실습 로드맵을 제공하여 시스템 개발자들의 찬사를 받았습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://kevinboone.me/efitest_index.html" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> 튜토리얼 보기
            </a>
            <a href="https://news.ycombinator.com/item?id=43279124" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 3 (35~53h) ==================== -->
      <!-- [HN 35~53h] Item 16: GitHub's new Git storage architecture -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 35~53h</span>
              <span class="minor-metric">🔺 216점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 38.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.9 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;수십억 개 저장소를 지탱하는 깃허브의 차세대 분산 스토리지&quot; : New Git Storage</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">GitHub's new Git storage architecture — 수십 년간 사용해온 파일시스템 기반 스포크(Spokes) 클러스터를 분산 SSD 블록 엔진으로 전면 교체한 기술 보고서</span>
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
          <h3 class="minor-detail-headline">초당 수백만 번의 git push/fetch 트래픽을 견디는 스토리지 아키텍처 대혁신</h3>
          <div class="minor-detail-subheadline">저장소 단위 디스크 마운트 한계를 끝내고 Rust와 분산 로그 복제 기반 멀티 테넌트 스토리지로 진화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                깃허브에 등록된 오픈소스와 프라이빗 리포지토리가 기하급수적으로 폭증함에 따라 기존 파일 서버(NFS/Spokes)의 inode 고갈과 페일오버 지연 한계를 극복해야 했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Git RPC Client &rarr; Global Routing Proxy &rarr; Distributed Raft Log Engine &rarr; NVMe Block Object Storage
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                서버 장애 시 리포지토리 복구 시간을 몇 분에서 수 밀리초로 단축하고, 수백 기가바이트의 거대 모노레포도 지연 없이 분산 파티셔닝 처리할 수 있는 토대를 마련했습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/" target="_blank" class="minor-link demo">
              <i data-lucide="external-link" class="minor-icon"></i> GitHub 블로그
            </a>
            <a href="https://news.ycombinator.com/item?id=43274567" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 35~53h] Item 17: Multiplayer tanks OSM demolition -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 35~53h</span>
              <span class="minor-metric">🔺 172점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 38.9시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;실제 지도 건물을 포탄으로 부수는 멀티플레이어 전차전&quot; : worldstrike.fun</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Multiplayer tanks that demolish real buildings from OpenStreetMap — 전 세계 오픈스트리트맵 실제 건축물 데이터를 실시간 3D 복셀로 변환해 파괴하는 웹 브라우저 게임</span>
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
          <h3 class="minor-detail-headline">공개 지리공간 빅데이터(OSM)와 복셀 물리 엔진의 절묘한 결합</h3>
          <div class="minor-detail-subheadline">서울, 도쿄, 뉴욕 등 실존 도시 한가운데서 포격을 주고받으며 현실 건물을 실시간 잔해로 붕괴시키는 기술</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                오픈스트리트맵(OSM)의 2D 건물 외곽선과 층수 메타데이터를 실시간 절차적 3D 복셀 메시로 생성하고, 포탄 피격 시 주변 블록을 동적으로 무너뜨리는 인터랙티브 물리 엔진으로 화제를 모았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> OpenStreetMap Vector Tiles &rarr; Procedural Voxel Extruder &rarr; Rapier Wasm Physics &rarr; Real-Time WebGL Demolition
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                무거운 3D 에셋 다운로드 없이 타일 기반으로 지리 데이터를 스트리밍하며, Wasm 기반의 물리 연산으로 수천 개의 파편 충돌을 웹 브라우저에서 60FPS로 렌더링합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://worldstrike.fun/" target="_blank" class="minor-link demo">
              <i data-lucide="globe" class="minor-icon"></i> 웹게임 접속
            </a>
            <a href="https://news.ycombinator.com/item?id=43272991" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 35~53h] Item 18: Dutch bank ASN blocks GrapheneOS -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 35~53h</span>
              <span class="minor-metric">🔺 644점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 37.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;이상주의 표방 은행이 오픈소스 안드로이드(GrapheneOS)를 차단하다&quot; : ASN Bank</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Dutch 'idealist' bank ASN blocks non-Google Android — 구글 플레이 인티그리티(Play Integrity) API 강제로 인해 보안 특화 OS 사용자를 원천 차단한 유럽 금융권 논란</span>
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
          <h3 class="minor-detail-headline">빅테크의 독점 무결성 증명이 자유 소프트웨어 생태계를 질식시키는 역설</h3>
          <div class="minor-detail-subheadline">구글 승인을 받지 않은 탈구글 안드로이드 폰은 온라인 뱅킹조차 할 수 없는 '디지털 신분증' 독점 위험성</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                사회적 가치와 환경을 표방하던 네덜란드 ASN 은행이 앱 업데이트를 통해 구글의 하드웨어 인증서가 없는 모든 커스텀 롬(GrapheneOS, CalyxOS)의 접속을 차단하면서 거센 역풍을 맞았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[파이프라인]</strong> Banking App Launch &rarr; Google Play Integrity Cloud Check &rarr; Hardware Attestation Failure &rarr; Hard App Block
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                오픈소스 운영체제 사용자가 금융 서비스에서 배제되는 사태를 조명하며, W3C 및 유럽연합(EU) 디지털 시장법(DMA) 차원에서 웹 기반 오픈 인증 표준의 필요성을 환기시켰습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/PrivSec-dev/banking-apps-compat-report/issues/32" target="_blank" class="minor-link github">
              <i data-lucide="github" class="minor-icon"></i> 이슈 리포트
            </a>
            <a href="https://news.ycombinator.com/item?id=43275210" target="_blank" class="minor-link hn">
              <i data-lucide="message-square" class="minor-icon"></i> HN 토론 보기
            </a>
          </div>
        </div>
      </div>
"""
