# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-03

HN_MINORS = """
      <!-- [HN 0~10h] Item 1: Astra Weight Space Programming -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 1,591점</span>
              <span class="minor-metric">💬 511개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.9시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 325.2 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;모델을 재학습하지 않고 가중치 공간을 직접 코딩한다&quot; : Astra의 혁신</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Astra can read and write weights to improve Qwen — 수억 원의 파인튜닝 비용 없이 LLM 내부 가중치 매트릭스를 기하학적으로 조작해 성능을 수직 상승시키는 연구 공개</span>
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
          <h3 class="minor-detail-headline">블랙박스 신경망을 프로그래밍 가능한 화이트박스로: 가중치 공간 개조</h3>
          <div class="minor-detail-subheadline">경사하강법의 무작위성에 의존하지 않고 특정 지식과 추론 회로를 가중치에 직접 주입</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                모델을 미세조정(Fine-Tuning)할 때마다 기존 능력을 잊어버리는 '파괴적 망각(Catastrophic Forgetting)'과 막대한 GPU 연산 비용에 좌절하던 AI 연구계에, 가중치 텐서의 특정 부분공간(Subspace)을 직접 읽고 쓰는 'Weight-Space Programming' 기법을 실증해 폭발적인 반응을 이끌어냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[가중치 조작 흐름]</strong> Qwen Base Weights &rarr; Linear Representation Probing &rarr; Direct Tensor Editing (Astra Core) &rarr; Zero-Training Alignment
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단 몇 초 만에 모델의 환각(Hallucination) 발현 벡터를 영구적으로 제거하거나 특정 도메인 코딩 정확도를 끌어올릴 수 있어, 향후 오픈소스 LLM 커스텀 생태계의 판도를 완전히 바꿀 것으로 평가받습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://rikiyat.github.io/blog/weight-space-programming/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 원문 아티클</a>
            <a href="https://news.ycombinator.com/item?id=50341029" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (511개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 2: WTF Ubuntu 0day RCE Scandal -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 1,468점</span>
              <span class="minor-metric">💬 607개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.4시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 146.8 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;치명적 리눅스 0day RCE를 3주째 방치하다니&quot; : 우분투 신뢰의 위기</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">WTF Ubuntu? / 3주간 방치된 커널 취약점 — CVE-2026-98432 원격 코드 실행 취약점이 보고되었음에도 패치를 미룬 캐노니컬을 향한 엔지니어들의 거센 분노 폭발</span>
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
          <h3 class="minor-detail-headline">엔터프라이즈 리눅스 신뢰의 붕괴: CVE-2026-98432 사태</h3>
          <div class="minor-detail-subheadline">데비안과 레드햇이 이틀 만에 긴급 패치를 내놓는 동안 침묵한 캐노니컬의 거버넌스 마비</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                우분투 24.04 LTS 및 이전 릴리즈 전반에 걸쳐 인증되지 않은 원격 공격자가 루트 권한을 탈취할 수 있는 치명적 커널 취약점이 공개되었음에도 불구하고, 캐노니컬이 무려 3주간 공식 보안 권고문조차 내놓지 않은 사실이 밝혀지며 시스템 관리자들의 격렬한 비판이 쏟아졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[취약점 경로]</strong> Remote TCP Crafted Packet &rarr; Netfilter State Desync &rarr; Kernel Stack Overflow (RCE) &rarr; Canonical Security Pipeline Stalemate
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                많은 인프라 팀이 상용 지원(Ubuntu Pro) 유료 마케팅에만 열을 올리고 기본 LTS 보안 패치를 소홀히 한 처사를 규탄하며 Debian이나 AlmaLinux로의 마이그레이션을 선언하는 계기가 되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://chalmovsky.com/posts/wtf-ubuntu" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 폭로 블로그 원문</a>
            <a href="https://news.ycombinator.com/item?id=50338912" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (607개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 3: Show HN: Subvocal -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 466점</span>
              <span class="minor-metric">💬 258개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.0시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 77.9 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;소리 내지 않고 컴퓨터와 대화하는 무음 발화 인터페이스&quot; : Subvocal</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Show HN: Subvocal – Talk to your computer without making noise — 후두부와 턱의 미세 근육 전기 신호(sEMG)를 읽어 완전한 침묵 속에서 음성 명령을 내리는 오픈소스 하드웨어</span>
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
          <h3 class="minor-detail-headline">도서관과 지하철에서도 자유로운 무음 AI 대화: Subvocal</h3>
          <div class="minor-detail-subheadline">음성 파형이 아닌 성대 신경 신호를 디코딩하여 프라이버시와 무소음 타이핑 동시 달성</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                사무실이나 대중교통 등 공공장소에서 음성 어시스턴트를 사용할 때 느끼는 민망함과 기밀 누설 문제를 완벽하게 해결하기 위해, 사람이 속으로만 중얼거릴 때 발생하는 미세 근육 전위(Subvocalization)를 오픈소스 하드웨어 센서로 캡처해 문자로 변환하는 혁신을 선보였습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[무음 신호 체계]</strong> Throat Surface Electrodes &rarr; sEMG Signal Conditioning (ESP32) &rarr; Lightweight 1D-CNN Decoder &rarr; Whisper Token Mapping
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                3D 프린팅 가능한 헤드셋 프레임과 저렴한 오프더셸프(off-the-shelf) 센서만으로 누구나 5만 원대에 제작할 수 있도록 회로도와 펌웨어를 전면 공개했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://news.ycombinator.com/item?id=50340088" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 쇼케이스 원문 (258개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 4: Show HN: Wikihack -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 330점</span>
              <span class="minor-metric">💬 102개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.1시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.2 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;해커뉴스 댓글에 숨겨진 위키피디아 지식의 다이나믹 비주얼 피드&quot; : Wikihack</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Show HN: Wikihack – HackerTube for Wikipedia — 지난 15년간 HN에서 엔지니어들이 가장 뜨겁게 인용한 위키 문서들을 릴스/쇼츠 형태로 재구성한 신개념 지식 플랫폼</span>
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
          <h3 class="minor-detail-headline">개발자들의 집단 지성이 큐레이션한 보물창고: Wikihack</h3>
          <div class="minor-detail-subheadline">텍스트 덤프 대신 핵심 도표, 타임라인, 맥락 인용구를 모던 카드 UI로 브라우징</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                알고리즘 추천 피드가 저품질 쇼츠와 어그로 영상으로 오염된 시대에, 해커뉴스 기술자들의 날카로운 토론 속에서 인용된 기이하고 심오한 과학·기술·역사 위키 문서들만 선별해 매력적인 비주얼 스트림으로 제공하며 개발자들의 지적 호기심을 저격했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[지식 추출 엔진]</strong> HN Algolia API Comments Dump &rarr; Wikipedia URL Entity Extraction &rarr; Upvote/Sentiment Weighting &rarr; Modern Responsive Visual Cards
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                복잡한 위키피디아 원본 API의 마크업을 순수 클라이언트사이드 자바스크립트로 경량 파싱하여 서버 부하 없이 번개 같은 페이지 전환을 실현했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://wikihack.netlify.app" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> Wikihack 라이브 웹사이트</a>
            <a href="https://news.ycombinator.com/item?id=50334812" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (102개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 5: Show HN: syscall.sh -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 197점</span>
              <span class="minor-metric">💬 48개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.8시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.3 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;모든 아키텍처의 리눅스 시스템 콜을 즉시 검색하는 API&quot; : syscall.sh</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Show HN: Linux System Call website and API (syscall.sh) — x86_64, ARM64, RISC-V 시스템 콜 번호, 인자 레지스터 매핑, 시그니처를 실시간 검색하고 curl로 쿼리하는 시스템 개발자의 성지</span>
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
          <h3 class="minor-detail-headline">어셈블리어와 커널 해커들을 위한 원스톱 레퍼런스: syscall.sh</h3>
          <div class="minor-detail-subheadline">커널 소스 트리를 뒤질 필요 없이 터미널 한 줄로 시스템 콜 규격 전격 호출</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                아키텍처마다 제각각인 시스템 콜 번호(예: read 시스템 콜이 x86_64에서는 0번, ARM64에서는 63번)와 레지스터 전달 순서(rdi, rsi, rdx vs x0, x1, x2)로 인해 고통받던 저수준 임베디드 및 보안 리버스 엔지니어들에게 단비 같은 도구로 급부상했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[쿼리 시스템]</strong> <code>curl syscall.sh/x86_64/sys_write</code> &rarr; Linux Kernel Source Header Parser &rarr; Instant Clean ANSI Output
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                웹 브라우저뿐만 아니라 터미널 CLI 환경에서 즉각적인 JSON 및 텍스트 출력을 지원하여 자동화 디버깅 셸 스크립트에 바로 파이프로 연결할 수 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://syscall.sh/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> syscall.sh 공식 사이트</a>
            <a href="https://news.ycombinator.com/item?id=50336219" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (48개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 6: Autonomous AI Mouse Brain Surgery -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 117점</span>
              <span class="minor-metric">💬 98개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.4시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.3 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;인간 개입 없이 실험 쥐의 미세 뇌 수술을 완벽 성공시킨 자율 AI 에이전트&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">AI agent performed brain surgery on a mouse — 실시간 광학 단층 비전 피드백과 마이크로 매니퓰레이터로 미세 혈관을 단 하나도 손상시키지 않고 신경 전극을 삽입한 의료 로보틱스의 개가</span>
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
          <h3 class="minor-detail-headline">서브밀리미터 정밀도의 자율 수술 시대 개막</h3>
          <div class="minor-detail-subheadline">인간 의사의 손떨림 한계를 극복하고 뇌신경 인터페이스(BCI) 전극 삽입을 전면 자동화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                뉴럴링크 등 차세대 뇌-컴퓨터 인터페이스의 가장 큰 병목이었던 '초미세 혈관 회피 삽입 수술'을 완전 자율 AI 제어 시스템이 성공적으로 수행한 영상과 논문이 공개되며, 의공학계와 해커뉴스 커뮤니티에 거대한 충격을 던졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[수술 제어 루프]</strong> 4K Optical Coherence Tomography (OCT) &rarr; Sub-micron Blood Vessel Segmentation &rarr; Closed-Loop Actuator (0.01mm) &rarr; Zero Hemorrhage Insertion
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                수술 전 과정에서 뇌 조직 출혈률 0%를 기록하며 인간 전문의의 숙련도에 의존하던 뇌 연구 프로토콜을 대량 생산 가능한 자동화 인프라로 격상시켰습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://twitter.com/OcanaSantero/status/2115442964574908902" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 연구 발표 원문 영상</a>
            <a href="https://news.ycombinator.com/item?id=50337890" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (98개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 7: Ask HN: Privacy TV Guide -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 680점</span>
              <span class="minor-metric">💬 820개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.7시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.6 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;거실의 감시자, 스마트 TV의 ACR 화면 캡처를 피하는 법&quot; : Privacy TV Guide</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Ask HN: Which TV do you recommend for privacy? — TV가 내 시청 화면을 1초마다 캡처해 광고 서버로 전송하는 시대, 스마트 OS 없는 상업용 B2B 사이니지 모니터 활용법 집단 토론</span>
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
          <h3 class="minor-detail-headline">거실 프라이버시를 지키려는 해커들의 반란: 덤 모니터(Dumb TV) 찾기</h3>
          <div class="minor-detail-subheadline">소비자용 스마트 TV의 광범위한 데이터 수집과 강제 광고에 맞서는 하드웨어 회피 전략</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                삼성, LG, 로쿠 등 주요 스마트 TV 제조사들이 기본 탑재한 ACR(자동 콘텐츠 인식) 기술로 HDMI 입력 화면까지 캡처해 프로파일링하는 실태가 폭로되면서, 와이파이 칩셋을 물리적으로 제거하거나 호텔/공항용 상업용 사이니지 디스플레이를 구매해 애플TV를 연결하는 극단적 프라이버시 노하우가 800개 이상의 댓글을 끌어모았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[프라이버시 세팅]</strong> Commercial Signage Display (No Wi-Fi/Tizen) &larr; HDMI Isolation &larr; Dedicated AppleTV / CoreELEC Box + Pi-hole DNS Firewall
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                하드웨어 제조사들의 광고 기반 수익 모델에 경종을 울리며, 네트워크 분리 및 DNS 차단 룰셋(Pi-hole) 공유로 이어지는 적극적인 소비자 주권 운동의 면모를 보여주었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://news.ycombinator.com/item?id=50328896" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문 (820개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 8: OccupySaaS Movement -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 487점</span>
              <span class="minor-metric">💬 304개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.0시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.2 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;기업의 구독료 인질극에 맞서는 탈-SaaS 오픈소스 총결집&quot; : OccupySaaS</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">OccupySaaS — 매년 수십 퍼센트씩 폭등하는 노션, 슬랙, 지라의 월 구독료 청구서에 맞서 검증된 자체 호스팅 오픈소스 대안들을 집결시키고 표준화하는 글로벌 선언</span>
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
          <h3 class="minor-detail-headline">클라우드 렌트 시크(Rent-Seeking)를 종식시키는 셀프 호스팅 연대</h3>
          <div class="minor-detail-subheadline">단일 Docker Compose 스택으로 기업 내 모든 SaaS 도구를 로컬 인프라로 대체</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                경기 둔화 속에서 스타트업과 엔터프라이즈의 IT 예산을 잠식하는 주범으로 지목된 클라우드 SaaS(좌석당 월 수십 달러)에 분노한 개발자들이, Mattermost(슬랙 대체), AppFlowy(노션 대체), Plane(지라 대체) 등을 단일 베어메탈 서버에 원클릭으로 띄우는 배포 템플릿을 완성해 화제가 되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[탈-SaaS 스택]</strong> Unified Traefik Reverse Proxy &rarr; Tailscale WireGuard Mesh &rarr; Self-Hosted F/OSS Docker Containers &rarr; 90% Cost Reduction
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단순한 비용 절감을 넘어 기업의 민감한 내부 문서와 고객 데이터가 서드파티 클라우드로 유출되는 보안 리스크를 근본적으로 원천 차단했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://occupysaas.com/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> OccupySaaS 매니페스토</a>
            <a href="https://news.ycombinator.com/item?id=50331045" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (304개)</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 9: Trigger.dev Env Leak Postmortem -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 162점</span>
              <span class="minor-metric">💬 85개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.1시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.3 점/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;K8s ConfigMap 전파 결함으로 고객 환경변수 노출&quot; : Trigger.dev 침해 분석</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Trigger.dev customer environment variables exposed — 오픈소스 백그라운드 잡 플랫폼 Trigger.dev의 API 키 및 DB 비밀번호 유출 사고 원인과 멀티테넌시 격리 교훈</span>
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
          <h3 class="minor-detail-headline">현대 클라우드 인프라의 아킬레스건: 멀티테넌트 환경변수 누수</h3>
          <div class="minor-detail-subheadline">투명한 포스트모텀 공개로 개발자 커뮤니티의 신뢰를 지켜낸 모범적 사고 대응</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                쿠버네티스 워커 노드의 롤아웃 과정에서 캐시 동기화 오류로 인해 다른 조직의 환경변수(OpenAI API 키, Supabase DB 패스워드 등)가 특정 워커 로그에 섞여 들어간 치명적 보안 사고의 원인과 해결책을 솔직하게 공개하여 아키텍트들의 이목을 집중시켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[사고 및 패치 경로]</strong> K8s Worker Pod Recycled &rarr; In-Memory Env Cache Stale Collision &rarr; Cross-Tenant Secret Leak &rarr; MicroVM Hard Boundary Isolation
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                사고 발생 1시간 만에 전 고객사 키 로테이션을 자동 발동하고 모든 워커를 Firecracker MicroVM 기반의 완전한 하드웨어 격리 환경으로 전환하는 기민한 사후 조치로 찬사를 받았습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://trigger.dev/blog/security-incident-nov-2026" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 공식 포스트모텀 리포트</a>
            <a href="https://news.ycombinator.com/item?id=50331892" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 (85개)</a>
          </div>
        </div>
      </div>
"""
