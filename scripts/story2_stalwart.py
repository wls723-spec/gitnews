# -*- coding: utf-8 -*-
# Story 2: stalwartlabs/stalwart (Stalwart 1.2.0 - Drop-in Microsoft Exchange Replacement)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] stalwartlabs/stalwart : Exchange Replacement     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_stalwart.jpg" alt="Stalwart Rust Mail Server Replacing Microsoft Exchange Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="mail" style="width:12px;height:12px;"></i> ENTERPRISE DISRUPTION</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">📮 HN 684점 · 342댓글 · MAPI/EWS/ActiveSync 네이티브 구현</span>
              <span class="platform-tag">Hacker News Top &amp; Rust Infra</span>
              <span class="platform-tag">stalwartlabs / stalwart</span>
            </div>

            <h2 class="article-headline">
              "아웃룩은 그대로, 서버만 바꾼다" — 20년 철옹성 Microsoft Exchange를 대체하는 Rust 서버 'Stalwart 1.2.0'
            </h2>

            <div class="article-subheadline">
              Exchange 2016/2019 지원 및 ESU 종료와 Exchange Online 강제 이주 압박 속에서, MAPI over HTTP·EWS·ActiveSync 16.1·Autodiscover를 AGPL-3.0 오픈소스로 완전 구현해 Outlook·Apple Mail 무수정 연결을 달성 (★16,281)
            </div>
            <p class="article-snippet">
              지난 20여 년간 기업용 이메일 인프라에서 "메일 서버"는 곧 Microsoft Exchange의 동의어였고, 탈출의 최대 걸림돌은 서버가 아니라 수천 명의 임직원 PC에 깔린 <strong>Outlook의 근육 기억</strong>이었습니다. 오늘 해커뉴스(<strong>684점·댓글 342개</strong>)를 뒤흔든 <strong>Stalwart 1.2.0</strong>은 Rust 단일 바이너리 메일 서버 안에 <strong>MAPI over HTTP(EMSMDB·NSPI), EWS, ActiveSync, Autodiscover</strong>를 통째로 구현해, 사용자가 이메일과 비밀번호만 입력하면 기존 Outlook·Apple Mail·모바일 앱이 Exchange 서버와 구분하지 못하고 즉시 동기화되는 '드롭인 교체'를 오픈소스(AGPL-3.0)로 열어젖혔습니다.
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
              <i data-lucide="flame"></i> 1. 리드: Exchange ESU 종료의 날, Outlook의 뒷문을 연 Rust 서버
            </h3>
            <p>
              전 세계 수많은 기업 IT 관리자들에게 2025년과 2026년은 뼈아픈 최후통첩의 시간이었다. Microsoft Exchange 2016과 2019는 2025년 10월 공식 지원이 끝났고, 유료 연장 보안 업데이트(ESU)마저 2026년 10월 추가 연장 없이 막을 내렸다. 남은 선택지는 기능 혁신이 멈춘 연간 구독형 <em>Exchange Server Subscription Edition(SE)</em>을 붙잡거나—심지어 Microsoft의 '신형 Outlook'조차 온프레미스 Exchange를 지원하지 않는다—아니면 전사 메일함을 통째로 미국 클라우드(Microsoft 365 / Exchange Online)로 올려 보내는 것뿐이었다.
            </p>
            <p>
              바로 그 막다른 골목에서 Rust 기반 올인원 메일·협업 서버 <strong>Stalwart</strong>의 메인테이너 Mauro D.가 1.2.0 릴리스를 발표했다. 해커뉴스 댓글창에는 즉각 환호와 논쟁이 폭발했다. 한 IT 엔지니어는 이렇게 썼다. <em>"Microsoft가 라이선스를 연간 과금으로 바꾼 이후 온프레미스 Exchange를 탈출할 방법을 찾고 있었는데, 완벽한 타이밍이다."</em>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 마이그레이션이 매번 실패했던 진짜 이유, '클라이언트'를 건드리지 않다
            </h3>
            <p>
              지금까지 Exchange를 표준 IMAP+CalDAV 서버로 대체하려는 프로젝트가 매번 무산된 이유는 서버 기능이 부족해서가 아니었다. 임직원들에게 <em>"내일부터는 썬더버드나 웹메일을 쓰세요, 아웃룩에서는 캘린더와 주소록·회의실 예약이 안 됩니다"</em>라고 통보하는 순간 사내 반발로 마이그레이션 계획이 폐기되기 때문이었다.
            </p>

            <div class="editorial-quote">
              <p>
                "Exchange를 떠나는 데 있어 진짜 장애물은 서버가 아니라 클라이언트였다. <strong>Stalwart 1.2.0에서는 사용자가 아무것도 바꿀 필요가 없다. 관리자가 메일함과 DNS 레코드만 Stalwart로 옮기면, 직원은 어제 쓰던 Classic Outlook에 이메일과 비밀번호만 입력해 그대로 일할 수 있다.</strong>"
              </p>
              <small>— Mauro D., Stalwart 1.2.0 공식 발표문 및 Hacker News 684점 토론 중</small>
            </div>

            <p>
              여기에 유럽과 공공기관, 법률·의료·방산 분야를 중심으로 급부상한 <strong>데이터 주권(Data Sovereignty)</strong>과 미국 <strong>CLOUD Act</strong> 리스크가 맞물렸다. 미국 클라우드 사업자에게 이메일 데이터를 맡기면 데이터가 물리적으로 어디에 저장되어 있든 미국 당국의 제출 명령 대상이 될 수 있다는 우려 때문에, "내 서버 위에서 돌아가는 Exchange 호환 오픈소스 서버"에 대한 수요가 그 어느 때보다 절실해진 시점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 단일 HTTPS 포트 위에서 춤추는 4대 Exchange 프로토콜 스택
            </h3>
            <p>
              Stalwart 1.2.0은 기존의 IMAP4rev2, JMAP(RFC 8621), POP3, SMTP, CalDAV/CardDAV/WebDAV 엔진을 버리지 않고, 동일한 단일 HTTPS 포트와 스토리지 백엔드 위에 Microsoft의 방대한 독점 프로토콜 4종을 직접 얹었다:
            </p>
            <ul>
              <li><strong>MAPI over HTTP (<code>EMSMDB</code> &amp; <code>NSPI</code>):</strong> Classic Outlook for Windows(2016 이후 및 Microsoft 365 Apps)가 사용하는 네이티브 바이너리 프로토콜이다. 캐시 모드와 온라인 모드를 모두 지원하며 메일·캘린더·연락처·작업·메모는 물론 증분 동기화, 전역 주소록(GAL)·오프라인 주소록(OAB), 위임 접근, 공용 메일함, 부재중 알림, 검색 폴더까지 처리한다.</li>
              <li><strong>Exchange Web Services (EWS, 2010 SP2~2016 스키마):</strong> Outlook for Mac, macOS Apple Mail/캘린더/연락처, Evolution-EWS, Thunderbird를 연결한다. Microsoft가 Exchange Online에서 2026년 10월부터 EWS를 끄기 시작해 2027년 4월 완전 폐기하는 것과 정반대로, Stalwart는 EWS 기반 사내 도구와 클라이언트의 수명을 온프레미스에서 영구 연장시켰다.</li>
              <li><strong>Exchange ActiveSync 14.1/16.1 &amp; Autodiscover (POX/SOAP/JSON):</strong> iOS/iPadOS 기본 메일 앱과 안드로이드(Gmail, 삼성 이메일, Nine)에 Push(Ping) 동기화를 제공하고, 사용자가 도메인 계정과 비밀번호만 입력해도 클라이언트가 스스로 엔드포인트와 인증 방식을 찾아내도록 3종 Autodiscover 규격을 모두 응답한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Stalwart 1.2.0 단일 HTTPS 멀티 프로토콜 Exchange 호환 아키텍처</span>
                <span class="schematic-badge">Rust Single Engine · AGPL-3.0 Community · IMAP/JMAP/Exchange Unified</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Unmodified Clients</div>
                  <div class="schematic-desc">
                    Classic Outlook Win (MAPI/HTTP)<br>
                    Outlook Mac &amp; Apple Mail (EWS)<br>
                    iPhone/Android (ActiveSync 16.1)<br>
                    POX/SOAP/JSON Autodiscover 자동 설정
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Stalwart Protocol Gateway</div>
                  <div class="schematic-desc">
                    단일 HTTPS 포트 + 단일 Rust 바이너리<br>
                    EMSMDB · NSPI 바이너리 RPC 파서<br>
                    JMAP · IMAP4rev2 · CalDAV 상호 호환<br>
                    DKIM2 · DMARCbis · OIDC · 2FA 통합
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Sovereign Data Store</div>
                  <div class="schematic-desc">
                    공용 메일함 · 위임 캘린더 · GAL 동기화<br>
                    온프레미스 Linux/Docker/클러스터 배포<br>
                    미국 CLOUD Act 비대상 자체 주권 보관<br>
                    Exchange / M365 무중단 메일함 이관
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Stalwart 1.2.0 공식 릴리스 문서 — Microsoft Exchange 프로토콜 완전 구현 및 지원 클라이언트 매트릭스</span>
              </div>
              <img src="../assets/images/demo_stalwart.png" alt="Stalwart Microsoft Exchange Replacement Official Release" class="showcase-img">
              <p class="showcase-caption">
                ▲ stalw.art/blog/microsoft-exchange-replacement/ 실화면: Exchange 2016/2019 지원 종료 대응 전략과 MAPI over HTTP·EWS·ActiveSync·Autodiscover 지원 내역.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자와 라이선스 공방: AGPL-3.0은 축복인가 족쇄인가
            </h3>
            <p>
              Microsoft가 Exchange 고객을 Microsoft 365 월 구독 수익 모델로 밀어 넣는 거대한 비즈니스 해자 앞에서, Stalwart 팀은 뜻밖의 결단을 내렸다. 이 거대한 Exchange 호환 프로토콜 스택 전체를 유료 Enterprise 전용 기능으로 잠그지 않고 <strong>오픈소스 Community Edition(<code>AGPL-3.0</code>)</strong>에 그대로 포함시킨 것이다.
            </p>
            <ul>
              <li><strong>대기업 법무팀의 'AGPL 알레르기' 논쟁:</strong> 해커뉴스 토론에서는 한 보수적인 엔지니어가 <em>"Exchange에 묶인 대기업 상당수는 사내 컴플라이언스 규정상 AGPL 소프트웨어를 금지한다"</em>고 지적했다. 그러나 반론도 거셌다. SaaS로 수정 재배포하지 않고 사내 메일 서버로 운영하는 자체만으로는 AGPL 소스 공개 의무가 발동하지 않으며, 상용 기술지원·클러스터링이 필요한 기업은 Stalwart의 상용 Enterprise 라이선스를 선택하면 된다.</li>
              <li><strong>클린룸 호환성과 AI 시대의 구현 속도:</strong> 과거 수십 년이 걸리던 거대 사유 바이너리 프로토콜(MAPI/RPC, EWS XML 스키마) 재구현을 소규모 Rust 팀이 완성해 낸 배경에는 공개된 Microsoft Open Specifications 문서와 현대 AI 보조 엔지니어링의 결합이 자리하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 마지막 온프레미스 성벽마저 오픈소스로 복원되다
            </h3>
            <p>
              클라우드로 가지 않으면 도태되도록 설계된 빅테크의 소프트웨어 수명 주기 속에서, "기존 클라이언트의 습관을 단 1%도 바꾸지 않고 서버의 주권만 되찾아온다"는 전략은 가장 현실적인 반격이다.
            </p>
            <p>
              20년 넘게 Microsoft의 독점 사유 프로토콜 뒤에 숨어 있던 기업 협업의 심장부가 이제 단일 Rust 바이너리로 열렸다. 내일 아침 출근해 아웃룩을 여는 직원은 아무것도 눈치채지 못한 채, 회사의 모든 이메일을 비로소 자기 회사의 서버 위에서 주고받게 될지도 모른다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Stalwart+mail+server+Microsoft+Exchange+replacement" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://stalw.art/blog/microsoft-exchange-replacement/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 발표 원문 보기
              </a>
              <a href="https://github.com/stalwartlabs/stalwart" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
