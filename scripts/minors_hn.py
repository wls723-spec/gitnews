# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items

HN_MINORS = """
      <!-- [HN 0~10h] Item 10: anthropic-formal-verification -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 284점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.8시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 101.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;수학적으로 버그가 없음을 LLM이 증명한다&quot; : 앤스로픽의 대규모 정형 검증 논문</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Anthropic Research — LLMs are making formal software verification feasible at a much larger scale</span>
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
          <h3 class="minor-detail-headline">LLM을 통한 대규모 소프트웨어 정형 검증(Formal Verification)의 도래</h3>
          <div class="minor-detail-subheadline">인간 수학자가 수개월 걸리던 Coq/Lean 증명 작성을 Claude가 수분 만에 대규모 보조</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                우주 항공, 암호학, 금융 커널 등 치명적인 시스템에서 소프트웨어가 수학적으로 절대 오류가 없음을 증명하는 '정형 검증'은 인력과 비용의 한계로 소규모 코드에만 제한되어 왔습니다. 앤스로픽은 프론티어 LLM이 복잡한 정리 증명(Theorem Proving)의 보조 정리를 자율 생성하는 획기적인 파이프라인을 실증했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> High-level Spec &rarr; Interactive Theorem Prover (Lean 4) &rarr; LLM Proof Search Loop &rarr; Formally Verified Binary
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                리눅스 커널과 암호화 라이브러리의 무결점 증명 비용을 극적으로 낮추며, 버그 없는 미션 크리티컬 소프트웨어 개발의 새로운 지평을 열었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.anthropic.com/research/formal-verification" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 앤스로픽 리서치 원문</a>
            <a href="https://news.ycombinator.com/item?id=50202217" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (25+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 11: docker-is-weird -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 192점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.2시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 60.0 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;도커는 생각보다 기괴하게 작동한다&quot; : containerd와 shim 레이어의 실체</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">codeandcake.dev/posts/2026-10-22-docker-is-weird — 컨테이너가 시스템 가정을 무너뜨리는 방식</span>
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
          <h3 class="minor-detail-headline">컨테이너 런타임의 숨겨진 함정: Docker Is Weird</h3>
          <div class="minor-detail-subheadline">iptables 포워딩 충돌,좀비 프로세스 수거, overlay2 파일시스템 누수의 심층 분석</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                개발자들이 도커를 '완벽히 격리된 경량 가상머신'으로 오해하면서 발생하는 프로덕션 장애들을 시스템 엔지니어링 관점에서 날카롭게 파헤친 기술 르포입니다. 도커 데몬 재시작 시 기존 컨테이너 연결이 끊어지는 구조적 원인을 도식화했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Docker CLI &rarr; dockerd &rarr; containerd &rarr; containerd-shim &rarr; runc (Linux Namespaces)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                컨테이너 내부 PID 1의 신호 전달(SIGTERM) 결함과 리눅스 브리지 네트워크의 성능 병목을 예방하는 구체적인 실무 팁을 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://codeandcake.dev/posts/2026-10-22-docker-is-weird" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 원문 포스트</a>
            <a href="https://news.ycombinator.com/item?id=50202681" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (16+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 12: quad9-exit-france -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 418점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 44.0 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;사법 검열에 굴복하느니 나라를 떠난다&quot; : 글로벌 프라이버시 DNS의 프랑스 철수</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">quad9.net/news/blog/au-revoir-france — 소니 뮤직과의 저작권 차단 소송에 맞서 스위스로 완전 이주</span>
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
          <h3 class="minor-detail-headline">인터넷 자유를 지키기 위한 DNS 재단의 망명: Quad9 to Exit France</h3>
          <div class="minor-detail-subheadline">음반사들의 DNS 차단 가처분 명령에 맞서 사법적 독립성을 수호하기 위한 결단</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                비영리 프라이버시 보호 DNS 서비스인 Quad9(9.9.9.9)이 프랑스 법원의 불법 스트리밍 사이트 DNS 검열 명령을 거부하고, 강력한 프라이버시 보호법이 존재하는 스위스로 법인을 완전히 이전하겠다고 전격 선언했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Resolver Client Query &rarr; Anycast BGP Routing &rarr; Zero-Logging Privacy Engine &rarr; Neutral Resolution
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                인터넷의 중립적 인프라인 DNS가 상업적 콘텐츠 소유자들의 사법 검열 도구로 전락하는 위험에 경종을 울린 역사적 사건으로 평가받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://quad9.net/news/blog/au-revoir-france/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> Quad9 공식 성명</a>
            <a href="https://news.ycombinator.com/item?id=50195959" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (352+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 13: php-rce-embargo-break -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 356점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 26.3 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;내가 실수로 PHP 제로데이 엠바고를 깨버렸다&quot; : 보안 업계를 뒤흔든 RCE 유출 사태</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Tell HN: I unknowingly broke the PHP RCE embargo. I am sorry — 전 세계 웹의 75%를 위협한 긴급 패치</span>
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
          <h3 class="minor-detail-headline">PHP 원격 코드 실행(RCE) 엠바고 유출과 긴급 패치</h3>
          <div class="minor-detail-subheadline">인터프리터 파서 결함으로 인한 임의 코드 실행 위험이 공개되며 php-src 저장소 트렌딩 1위 폭발</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                한 보안 연구원이 비공개 엠바고 상태였던 PHP 8.x 핵심 파서의 제로데이 RCE 취약점 개념증명(PoC) 코드를 실수로 공개 포럼에 유출하면서, 전 세계 웹 서버들이 패치 적용 전까지 무방비로 노출되는 비상사태가 발생했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Malformed Multipart Payload &rarr; PHP Lexer Buffer Overflow &rarr; Stack Canary Bypass &rarr; Arbitrary Shell RCE
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                PHP 코어 개발팀이 긴급 릴리즈를 배포했으며, 클라우드플레어와 AWS 등 주요 CDN 벤더들이 WAF 방화벽 규칙을 1시간 만에 긴급 업데이트했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://news.ycombinator.com/item?id=50193416" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 원문 토론 (147+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 14: ns2jb-switch2-jailbreak -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 289점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 15.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.6 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스위치 2 부트롬이 뚫렸다&quot; : 차세대 콘솔 하드웨어 취약점 개념증명</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb — Tegra T239 칩셋의 전압 글리칭과 부트로더 분석</span>
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
          <h3 class="minor-detail-headline">닌텐도 스위치 2 부트롬 아키텍처 및 탈옥 보고서</h3>
          <div class="minor-detail-subheadline">엔비디아 오린 기반 T239 커스텀 실리콘의 보안 서열과 하드웨어 레벨 취약성 규명</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                콘솔 출시를 앞두고 제조 파트너사로부터 유출된 엔지니어링 샘플 메인보드를 대상으로 전압 글리칭(Fault Injection)을 수행하여, 하드웨어 서명 검증 체인을 우회하는 저수준 분석 보고서가 공개되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> BootROM Cold Reset &rarr; Voltage Glitch Injection &rarr; RSA-4096 Bypass &rarr; TrustZone Execution Control
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                하드웨어 퓨즈(eFuse)와 안전한 부트 체인을 설계할 때 물리적 공격(Side-channel)을 방어하기 위한 임베디드 보안 설계의 중요성을 일깨웠습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 기술 분석 블로그</a>
            <a href="https://news.ycombinator.com/item?id=50192536" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (246+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 15: pwn-watch -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 214점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.3 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;지금 전 세계에서 털리고 있는 시스템들&quot; : 0-day 실시간 공격 관측망</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">pwn.watch — 허니팟과 위협 인텔리전스 센서로 포착하는 실시간 사이버 침투 현황</span>
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
          <h3 class="minor-detail-headline">실시간 글로벌 제로데이 공격 관제 레이더: Pwn.watch</h3>
          <div class="minor-detail-subheadline">전 세계 500개 센서 노드에서 포착된 최신 익스플로잇 페이로드와 표적 인프라 대시보드</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                신규 취약점이 발표되자마자 자동화된 봇넷이 전 세계 IPv4 대역을 15분 만에 스캔하는 시대에, 방어자들에게 위협 침해 지표(IoC)를 1초 단위로 스트리밍하는 실시간 관제망의 필요성이 극대화되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Global Honeypot Fleet &rarr; Deep Packet Inspection &rarr; Exploit Clustering AI &rarr; Real-Time Threat Heatmap
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                보안 엔지니어들이 사내 방화벽 규칙을 능동적으로 선제 방어(Proactive Defense)할 수 있는 오픈 위협 인텔리전스를 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://pwn.watch/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> pwn.watch 라이브 레이더</a>
            <a href="https://news.ycombinator.com/item?id=50195543" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (157+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 16: uberblok-zfs -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 145점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.0 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;ZFS 파일시스템 내부를 탐험하는 박물관&quot; : 머클 트리 인터랙티브 시각화</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Show HN: Uberblok — ZFS vdev, dnode, 블록 포인터, COW 스냅샷의 시각적 해부</span>
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
          <h3 class="minor-detail-headline">ZFS 파일시스템 아키텍처 대화형 시각화: Uberblok</h3>
          <div class="minor-detail-subheadline">복잡한 COW(Copy-On-Write) 트리와 체크섬 자가 치유(Self-healing) 메커니즘을 3D 그래프로 탐색</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                가장 진보된 파일시스템으로 꼽히는 OpenZFS의 데이터 무결성 구조(Uberblock &rarr; MOS &rarr; dnode &rarr; Leaf Blocks)를 교과서 설명 대신 브라우저에서 직접 클릭하고 확장하며 배우는 교육용 시각화 도구입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Uberblock Ring &rarr; Meta Object Set (MOS) &rarr; Hierarchical Block Pointers &rarr; SHA-256 Merkle Verification
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                스토리지 엔지니어와 커널 개발자들에게 ZFS의 복구 불가(Data Loss) 시나리오와 스냅샷 롤백의 수학적 원리를 직관적으로 이해시킵니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://uberblok.storagebits.workers.dev/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> Uberblok 인터랙티브 체험</a>
            <a href="https://news.ycombinator.com/item?id=50180257" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (20+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 17: lastmuseum-semantic -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 168점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;인류의 모든 미술품을 감정으로 검색한다&quot; : 580만 점 예술품 시맨틱 검색</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">The Last Museum — 루브르, 메트, 대영박물관 소장품을 관통하는 멀티모달 임베딩</span>
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
          <h3 class="minor-detail-headline">전 세계 580만 점 박물관 소장품 시맨틱 검색: The Last Museum</h3>
          <div class="minor-detail-subheadline">단순 키워드가 아닌 "비 내리는 밤의 고독한 푸른빛" 같은 추상적 뉘앙스로 미술품 탐색</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                각국 국립박물관들이 개별 운영하던 오픈 액세스 아카이브를 통합하여, 비전-텍스트 멀티모달 임베딩 모델(CLIP)로 단일 고차원 벡터 공간에 인덱싱했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> 5.8M Museum Scrapes &rarr; Vision-Language Joint Embedding &rarr; HNSW Vector Index &rarr; Instant Semantic Search
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                문화 유산 데이터의 디지털 접근성을 혁신하고, 연구자와 아티스트들에게 영감을 주는 인공지능 큐레이션의 모범 사례로 찬사를 받았습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://lastmuseum.com/" target="_blank" class="project-link demo"><i data-lucide="globe"></i> The Last Museum 체험</a>
            <a href="https://news.ycombinator.com/item?id=50194522" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (30+ 댓글)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 18: gnu-taler-germany -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 312점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.1 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;블록체인 없이 구현한 프라이버시 디지털 화폐&quot; : GNU Taler 독일 실전 가동</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Getting ready to operate GNU Taler in Germany — 유로화(EUR) 기반의 블라인드 서명 결제 시스템</span>
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
          <h3 class="minor-detail-headline">블록체인 없는 중앙은행 친화적 프라이버시 전자화폐: GNU Taler</h3>
          <div class="minor-detail-subheadline">소비자에게는 완벽한 익명성을, 상인에게는 세금 투명성을 보장하는 차움(Chaum) 블라인드 서명</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                비트코인의 극심한 전력 낭비와 가격 변동성 없이, 기존 유로 통화 시스템 위에서 물리적 현금처럼 익명 결제를 수행하는 오픈소스 결제 규격 GNU Taler가 독일 은행 규제를 통과하고 상용 운영 준비를 마쳤습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Bank Deposit &rarr; Chaum Blind Signature Token &rarr; Anonymous Merchant Payment &rarr; Tax-Audited Redemption
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                암호화폐의 투기성을 걷어내고 프라이버시 암호학의 본령으로 돌아가 중앙은행 디지털화폐(CBDC)의 대안적 미래 모델을 실증했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.taler.net/en/news/2026-13.html" target="_blank" class="project-link demo"><i data-lucide="globe"></i> 공식 발표문</a>
            <a href="https://news.ycombinator.com/item?id=50197404" target="_blank" class="project-link github"><i data-lucide="message-square"></i> HN 토론 (84+ 댓글)</a>
          </div>
        </div>
      </div>
"""

print("HN Minors ready.")
