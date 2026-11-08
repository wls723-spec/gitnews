# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-09

HN_MINORS = """
      <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
      <!-- [HN 0~10h] Item 10: Goldman Sachs pulls Claude Code -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 496점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 109.8 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;골드만삭스, 보안·규제 우려로 트레이더와 뱅커의 Claude Code 사용 전면 중단&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">thestateofai.com — 금융권 핵심 자산의 클라우드 코드 유출과 자동 실행 권한 리스크로 인해 월가 대형 투자은행이 AI 코딩 하네스를 전격 회수</span>
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
          <h3 class="minor-detail-headline">월가 금융 공룡의 전격적인 AI 코딩 도구 규제와 엔터프라이즈 거버넌스의 충격</h3>
          <div class="minor-detail-subheadline">터미널 자율 실행 권한이 가진 치명적 리스크와 사내 데이터 기밀 보호 조치 분석</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                월가의 대표적 투자은행 골드만삭스가 트레이딩 및 뱅킹 부서에 배포했던 Claude Code 하네스를 전면 중단하면서 전 세계 엔터프라이즈 보안 팀들의 이목이 집중되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[쟁점 구조]</strong> Enterprise Terminal Autonomy &rarr; Secret Key & Financial Data Exposure &rarr; Compliance Alarm &rarr; Full Ban
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                AI 도구가 쉘 명령어를 자율적으로 실행할 때 발생하는 비감사(Auditing) 리스크와, 온프레미스 에어갭(Air-gapped) 환경이 왜 대기업에 필수적인지 일깨워준 중대 사건입니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://www.thestateofai.com/news/goldman-sachs-claude-code-" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 원문 기사 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 11: Outlook.com DMARC Policy Enforcement -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 156점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 45.3 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;마이크로소프트 아웃룩, DMARC 인증 없는 도메인 이메일 조용한 수신 차단 시작&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">mailroute.net — 스팸 및 피싱 근절을 위해 구글에 이어 마이크로소프트도 미인증 발송 메일을 스팸함 이동 없이 원천 드롭하는 정책 적용</span>
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
          <h3 class="minor-detail-headline">스타트업과 중소 도메인의 아웃룩 수신율이 급락하는 원인과 인프라 대응 가이드</h3>
          <div class="minor-detail-subheadline">SPF, DKIM을 넘어 엄격한 DMARC 정렬(Alignment) 레코드가 인터넷 표준으로 강제화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Outlook.com 및 Microsoft 365가 별도의 사전 경고 없이 DMARC 정책 미비 도메인에서 발송된 비즈니스 이메일을 조용히 거부(Drop)하기 시작하며 시스템 관리자들의 비상이 걸렸습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[인증 흐름]</strong> Outgoing SMTP &rarr; SPF / DKIM Cryptographic Signature &rarr; DMARC Policy Alignment Check &rarr; Inbox Delivery
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                이메일 전송 인프라에서 DMARC가 더 이상 선택적 권고안이 아니라 인터넷 서비스 접속을 위한 필수 프로토콜로 자리 잡았음을 알리는 기술적 분기점입니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://mailroute.net/blog/outlook-rejecting-email-without-d" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 기술 분석 리포트
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 12: Dux Wayland Desktop Shell -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 131점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.6시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 36.0 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;초경량 파일 매니저와 테마 커스텀을 통합한 무료 오픈소스 Wayland 쉘&quot; : Dux</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">duxlabs.dev — 무거운 그놈(GNOME)을 벗어나 가볍고 직관적인 UI 경험을 제공하는 모던 리눅스 Wayland 데스크톱 환경 공개</span>
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
          <h3 class="minor-detail-headline">미니멀리즘과 심미성을 동시에 잡은 차세대 리눅스 Wayland 데스크톱 생태계</h3>
          <div class="minor-detail-subheadline">wlroots 기반 하드웨어 가속 렌더링과 모듈형 타일링 윈도우 관리 통합</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                복잡한 설정 파일(dotfiles)을 수동으로 편집해야 하는 기존 타일링 매니저(Hyprland, Sway)의 높은 진입 장벽 없이 바로 쓸 수 있는 세련된 쉘로 주목받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처]</strong> Linux Kernel &rarr; Wayland / wlroots Backend &rarr; Dux Modern Compositor &rarr; Integrated UI Shell
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                60FPS 버벅임 없는 부드러운 애니메이션과 터치패드 제스처를 지원하며 저사양 기기에서도 200MB 미만의 메모리로 데스크톱 환경을 유지합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://duxlabs.dev/" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 공식 프로젝트 사이트
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
      <!-- [HN 10~20h] Item 13: Open Agent Memory Format -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 159점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.3 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI 에이전트 메모리에도 OpenTelemetry와 같은 표준 인터페이스 규격이 필요하다&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">lorekit.io — 프레임워크마다 제각각인 에이전트 컨텍스트 기억 저장 방식을 통합하여 상호 운용성을 확보하려는 오픈 표준 제안</span>
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
          <h3 class="minor-detail-headline">에이전트를 교체할 때마다 증발하던 대화 맥락과 작업 결정 히스토리의 불연속성 극복</h3>
          <div class="minor-detail-subheadline">벤더 종속 없이 영구 메모리를 내보내고 불러올 수 있는 개방형 시맨틱 표준 선언</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                LangChain, CrewAI, AutoGen 등 도구마다 자체 메모리 포맷을 강제하여 에이전트 생태계 간 지식 전이와 마이그레이션이 불가능했던 파편화 문제를 정조준했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[표준 스택]</strong> Multi-Agent Session &rarr; Open Memory Tracing Spec &rarr; Portable Context Store &rarr; Interoperable Retrieval
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                분산 로깅의 OpenTelemetry처럼, AI 에이전트의 사고 과정과 장기 기억을 표준화된 JSON/바이너리 형태로 직렬화하여 도구 간 이동을 실현합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://www.lorekit.io/blog/open-agent-memory-format" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 기술 제안서 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 14: Person of Interest -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 280점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.6 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스마트폰과 웹 풋프린트로 개인이 어떻게 감시 대상이 되는가: OSINT 프라이버시 해부&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">krthr.co — 디지털 광고 식별자와 위치 텔레메트리가 결합하여 일반인을 정밀 추적하는 현대 감시 자본주의 메커니즘 심층 분석</span>
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
          <h3 class="minor-detail-headline">데이터 브로커와 브라우저 핑거프린팅이 완성한 일상 속 디지털 파놉티콘의 실체</h3>
          <div class="minor-detail-subheadline">합법적인 마케팅 SDK를 통해 수집된 개인 이동 동선이 어떻게 무기화되는가</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                정부 기관뿐만 아니라 민간 기업과 사설 탐정까지 상업용 데이터 브로커 네트워크를 통해 일반인의 실시간 위치를 추적할 수 있는 현실이 폭로되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[추적 경로]</strong> Mobile App Ad SDK &rarr; Bidstream Data Leakage &rarr; Commercial Broker Graph &rarr; Deanonymized Profile
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                개발자들에게 클라이언트 텔레메트리 최소화, 무작위 광고 식별자 차단, 그리고 로컬 온디바이스 연산이 왜 윤리적 의무인지 강력한 경종을 울립니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://krthr.co/person-of-interest/" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 심층 분석 블로그
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 15: ISponsorBlockTV -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 117점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.2 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스마트 TV의 모든 유튜브 앱에서 협찬 광고 구간을 자동 건너뛰는 도구&quot; : ISponsorBlockTV</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">github.com/dmunozv04/isponsorblocktv — Apple TV, LG webOS, 삼성 Tizen 등 거실 TV 화면에서 스폰서 블록을 백그라운드로 동기화</span>
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
          <h3 class="minor-detail-headline">브라우저 확장 프로그램을 설치할 수 없는 폐쇄형 스마트 TV의 광고 장벽 돌파</h3>
          <div class="minor-detail-subheadline">로컬 네트워크 DIAL 및 YouTube TV 원격 제어 프로토콜을 활용한 비침습적 탐색</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                유튜브 영상 내부의 지루한 유료 협찬 광고 구간을 TV 리모컨으로 일일이 빨리 감기 해야 했던 거실 미디어 환경의 불편을 완전 자동화했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[동기화 구조]</strong> Smart TV YouTube Stream &rarr; Local Python Daemon &rarr; SponsorBlock Cloud DB &rarr; Auto Skip Packet
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                TV를 탈옥하거나 루팅하지 않고도 라즈베리 파이나 도커 컨테이너 한 대로 거실의 모든 TV 장치와 투명하게 통신하여 광고 구간을 자동 점프합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/dmunozv04/isponsorblocktv" target="_blank" class="minor-link hn">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
      <!-- [HN 20~30h] Item 16: Claude Code Secret Leak -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 569점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.9 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;Claude Code의 'Don't Ask Again' 옵션으로 인해 1,122개 공개 GitHub 저장소에 암호 유출&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">apiiro.com — 편리함을 위해 확인 절차를 건너뛴 에이전트가 .env 파일과 API 시크릿 키를 무심코 공개 리포지토리에 커밋·푸시한 실태</span>
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
          <h3 class="minor-detail-headline">자율 코딩 도구의 무비판적 신뢰가 초래한 대규모 크리덴셜 유출 사고와 보안 권고안</h3>
          <div class="minor-detail-subheadline">에이전트에게 Git push와 커밋 전권을 부여했을 때 발생하는 공급망 재앙 분석</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                개발자들이 반복 질문 프롬프트에 피로를 느껴 '다시 묻지 않음'을 켜둔 사이, 에이전트가 데이터베이스 비밀번호가 담긴 환경설정 파일을 깃허브 공개 저장소로 올려버린 사례가 적발되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[유출 경로]</strong> 'Don't Ask Again' Active &rarr; Agent Adds All (.env Included) &rarr; Git Auto-Push &rarr; Public GitHub Breach
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                사전 커밋 훅(pre-commit hooks)과 기밀 감지 도구(TruffleHog)를 에이전트 파이프라인 전면에 강제 배치해야 한다는 보안 가이드라인이 전 세계적으로 확산되고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://apiiro.com/blog/coding-agents-leaking-secrets-github" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 보안 연구 리포트
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 17: Coldframe Honeypot -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 275점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 9.4 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;슈퍼마켓 냉동고 컨트롤러로 위장하여 산업용 IoT 공격을 낚는 저상호작용 허니팟&quot; : Coldframe</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">github.com/hedgerow-dev/coldframe — Danfoss 및 Dixell 상업용 냉동 제어 프로토콜을 정밀 모방해 기간시설 대상 랜섬웨어 및 정찰 공격을 기록</span>
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
          <h3 class="minor-detail-headline">실제 식료품 공급망 냉장 설비를 노리는 해커 조직의 탐색 기법을 가로채는 덫</h3>
          <div class="minor-detail-subheadline">Modbus 및 독점 제어 프로토콜 웹 인터페이스를 시뮬레이션하여 위협 인텔리전스 수집</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                대형 유통 매장과 냉동 물류창고의 온도를 조작해 수십억 원 상당의 식재료를 부패시키겠다고 협박하는 변종 랜섬웨어 공격을 감지하기 위해 개발되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[허니팟 구조]</strong> Internet Scanner &rarr; Coldframe Virtual Controller (Danfoss AK-SM) &rarr; Attack Logging &rarr; Threat Feed
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                저자원 환경에서 도커 컨테이너로 즉시 띄울 수 있으며, 실제 관리자 로그인 폼과 센서 수치 응답을 정교하게 모사하여 침입자의 무기화 도구를 채증합니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://github.com/hedgerow-dev/coldframe" target="_blank" class="minor-link hn">
              <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 18: Microsoft Research AI Frontiers Disbanded -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 487점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.7시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 16.9 보트/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;마이크로소프트 리서치, 창립 이래 최고의 기초 AI 연구팀 'AI Frontiers' 전격 해체&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">hunch.net — 단기 제품화와 오픈AI 파트너십에 밀려 순수 기초 과학과 모델 이론을 탐구하던 전설적인 MSR AI 연구 그룹이 역사 속으로 퇴장</span>
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
          <h3 class="minor-detail-headline">빅테크의 기초 과학 투자가 끝나고 즉각적인 상업화와 제품 매출로 매몰되는 시대의 상징</h3>
          <div class="minor-detail-subheadline">머신러닝 이론의 거두 존 랭퍼드(John Langford) 교수의 회고록과 학계의 깊은 탄식</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                10년 뒤의 혁신을 내다보며 자유롭게 기초 알고리즘을 연구하던 MSR의 핵심 팀이 상업적 제품 매출 압박으로 인해 해체되면서 학계와 오픈소스 생태계에 큰 충격을 주었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[패러다임 전환]</strong> Long-Term Fundamental Research &rarr; Short-Term Commercial ROI Pressure &rarr; Team Disbandment &rarr; Open Science Shift
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                빅테크 내부 연구실의 폐쇄로 인해 우수한 석학들이 탈중앙화된 오픈소스 진영과 독립 스타트업으로 대거 유입되는 계기가 될 것으로 전망됩니다.
              </p>
            </div>
          </div>
          <div class="minor-footer-links">
            <a href="https://hunch.net/?p=13764006" target="_blank" class="minor-link hn">
              <i data-lucide="external-link" class="minor-icon"></i> 존 랭퍼드 교수 회고록
            </a>
          </div>
        </div>
      </div>
"""
