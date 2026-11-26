# -*- coding: utf-8 -*-
# Story 1: progrium/minipg (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = r"""
      <!-- ========================================================== -->
      <!-- [HERO 1] progrium/minipg : COVER STORY                     -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_minipg.jpg" alt="minipg Single Executable PostgreSQL via Plan 9 Hypervisor Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER STORY #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🐘 HN 283점 · Docker 없는 단일 실행 파일 PostgreSQL 18</span>
              <span class="platform-tag">Hacker News Top &amp; Zig Systems</span>
              <span class="platform-tag">progrium / minipg</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"빅테크 클라우드와 거대한 컨테이너 스택을 해체하는 초소형 인프라의 반란" — Docker 없이 단일 파일로 뜬 PostgreSQL 'minipg'</span>
            </h2>

            <div class="article-subheadline">
              Docker Hub의 postgres:18-alpine 이미지를 실행 파일 하나에 품고, Plan 9 커널(hyper9)의 리눅스 성격으로 호스트 하이퍼바이저 위에서 직접 구동하는 Zig 기반 PostgreSQL — .pgdb 폴더 하나로 SQLite처럼 쓰고 필요할 때만 자동 기동 (HN 283점 · ★201 · MIT)
            </div>
            <p class="article-snippet">
              로컬에서 PostgreSQL을 띄우려면 무거운 Docker 데몬을 켜거나 OS 패키지를 설치해 포트와 계정을 맞춰야 한다는 상식이 깨졌습니다. <strong>progrium/minipg</strong>는 공식 <code>postgres:18-alpine</code> 이미지를 단일 실행 바이너리 안에 내장한 뒤, 리눅스 커널 부팅도 VM 이미지도 없이 <strong>Plan 9 커널 라이브러리 <code>hyper9(h9)</code></strong>로 알파인 리눅스 바이너리의 시스템 콜을 가로채 호스트 하이퍼바이저 위에서 직접 실행합니다(HN <strong>283점</strong>). 디렉터리 하나(<code>app.pgdb</code>)에 데이터·설정·암호가 모두 담겨 SQLite처럼 복사하고, 쿼리가 들어올 때만 서버가 2초 만에 깨어났다가 유휴 60초 후 스스로 잠듭니다.
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
              <i data-lucide="flame"></i> 1. 리드: <code>minipg app.pgdb</code> 한 줄이 무너뜨린 Docker의 성벽
            </h3>
            <p>
              개발자가 노트북에서 새 프로젝트를 시작할 때마다 마주하는 의식이 있다. SQLite를 쓰자니 프로덕션의 PostgreSQL과 방언·JSONB·동시성 모델이 어긋나고, 그렇다고 로컬에 PostgreSQL을 띄우자니 수 기가바이트짜리 Docker Desktop을 깨우거나 시스템 전역 서비스와 <code>5432</code> 포트를 두고 씨름해야 한다. 웹훅 표준과 Dokku를 만든 오픈소스 해커 제프 린지(Jeff Lindsay, <code>progrium</code>)가 2026년 11월 26일 해커뉴스에 던진 질문은 이 오래된 체념을 정면으로 찔렀다: <em>"SQLite와 PostgreSQL이 아기를 낳는다면 어떤 모습일까?"</em>
            </p>
            <p>
              그가 내놓은 <strong><code>minipg</code></strong>는 <code>brew install</code>도, <code>docker compose up</code>도, <code>initdb</code> 수동 설정도 요구하지 않는다. 터미널에 <code>minipg app.pgdb</code>라고 치는 순간 <code>app.pgdb/</code> 폴더가 생기고, 자동으로 랜덤 비밀번호와 <code>C.UTF-8</code> 로케일 클러스터가 초기화된 뒤 곧바로 <code>psql</code> 셸이 열린다. <code>\q</code>를 눌러 빠져나오면 서버는 60초 뒤 스스로 종료되며, 멈춘 <code>app.pgdb</code> 디렉터리는 마치 SQLite 파일처럼 통째로 <code>cp</code>하거나 백업할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 WASM 재컴파일(PGlite)이 아니라 'Plan 9 하이퍼바이저'인가
            </h3>
            <p>
              브라우저나 임베디드 환경에 PostgreSQL을 욱여넣으려는 시도는 이전에도 있었다. 대표적인 사례인 <code>PGlite</code>는 PostgreSQL 소스코드를 WebAssembly(WASM) 단일 프로세스 모드로 컴파일해 자바스크립트 런타임에 올린다. 그러나 단일 프로세스 모드 Postgres는 다중 동시 접속, 표준 <code>psql</code>/<code>pg_dump</code> 도구 체인, 그리고 실제 운영 환경과 동일한 다중 프로세스 격리를 온전히 제공하지 못한다. <code>minipg</code>는 정반대의 길을 택했다. Postgres를 억지로 뜯어고쳐 재컴파일하는 대신, <strong>도커 허브의 순정 <code>postgres:18-alpine</code> 바이너리를 수정 없이 그대로 실행할 수 있는 초경량 하이퍼바이저 커널을 Zig로 통째로 품어버린 것</strong>이다.
            </p>

            <div class="editorial-quote">
              <p>
                "알파인의 순정 Postgres 바이너리를 호스트 하이퍼바이저 위에서 직접 실행하고, 그 시스템 콜을 Plan 9 커널이 응답한다. <strong>부팅할 리눅스 커널도, VM 이미지도, Docker도 필요 없다.</strong> 단 하나의 파일 안에 데이터베이스 서버 전체가 들어간다."
              </p>
              <small>— 제프 린지(Jeff Lindsay), <em>minipg</em> 아키텍처 선언 &amp; HN 토론 (283점·44댓글)</small>
            </div>

            <p>
              해커뉴스에서는 <em>"Node.js 앱을 단일 실행 파일로 묶을 때 SQLite조차 네이티브 바인딩 때문에 골치를 썩였는데, 단 하나의 파일로 진짜 Postgres 서버를 내장할 수 있다는 점이 경이롭다"</em>는 반응과 함께, 한 발 더 나아가 브라우저 데모 페이지에서 <code>v86</code> 에뮬레이터와 JSPI(JavaScript Promise Integration)를 통해 실제 리눅스 Postgres를 35MB 전송만으로 페이지 안에서 돌려버린 시연에도 관심이 쏟아졌다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: <code>hyper9(h9)</code> Plan 9 커널과 <code>.pgdb</code> 온디맨드 수명주기
            </h3>
            <p>
              <code>minipg</code>가 순정 Alpine PostgreSQL 18을 단일 정적 바이너리로 구동하면서도 <code>kill -9</code> 강제 종료 테스트(WAL + <code>amcheck</code> 무결성)까지 통과하는 내부 구조는 세 개의 정교한 층위로 맞물려 있다:
            </p>
            <ul>
              <li><strong>Zig 라이브러리로 임베드된 <code>hyper9(h9)</code> 커널과 리눅스 성격(Linux Personality):</strong> <code>minipg</code>는 <code>hyper9</code>라는 연구용 Plan 9 커널을 서브모듈로 내장한다. Windows에서는 WHP(Windows Hypervisor Platform), macOS 애플 실리콘에서는 <code>Hypervisor.framework</code>, Linux에서는 KVM 또는 KVM 없는 환경용 네이티브 시스템콜 인터셉트 백엔드를 사용해 <code>postgres</code> ELF 바이너리의 시스콜을 호스트에서 직접 처리한다.</li>
              <li><strong><code>.pgdb</code> 자기완결형 번들과 <code>C.UTF-8</code> 결정론:</strong> <code>app.pgdb/</code> 내부에는 설정과 자동 생성 비밀번호(권한 <code>0600</code>)를 담은 <code>minipg.toml</code>, 실제 데이터 디렉터리 <code>pgdata/</code>, 배타적 서버 잠금 파일 <code>.lock</code>만 존재한다. 모든 신규 클러스터는 호스트 OS의 <code>libc</code> 버전 업데이트로 텍스트 인덱스가 망가지는 참사를 막기 위해 Postgres 내장 <code>C.UTF-8</code> 로케일로 초기화된다.</li>
              <li><strong>온디맨드 백그라운드 서버와 도구 머신 분리:</strong> <code>minipg app.pgdb "select 1"</code>이나 <code>minipg run app.pgdb -- npm test</code>가 호출되면 클라이언트(<code>src/client.zig</code>)가 유닉스 제어 소켓(Windows에서도 <code>AF_UNIX</code>)을 확인해 유휴 서버를 자동 기동한다. <code>psql</code>·<code>pg_dump</code> 같은 도구는 약 90ms 만에 별도 경량 <code>h9</code> 머신으로 실행되어 루프백 TCP(<code>SCRAM-SHA-256</code>)로 서버에 붙고, <code>pg_stat_activity</code> 기준 접속이 <code>MINIPG_IDLE</code>(기본 60초) 동안 0이 되면 <code>SIGINT</code>로 깔끔히 종료된다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">minipg 단일 실행 파일 하이퍼바이저 데이터베이스 아키텍처</span>
                <span class="schematic-badge">Zig · hyper9 Plan 9 Kernel · postgres:18-alpine</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. .pgdb Portable Vault</div>
                  <div class="schematic-desc">
                    <code>minipg.toml</code> (포트 · SCRAM 비밀번호 0600)<br>
                    <code>pgdata/</code> (순수 Postgres 18 파일 · C.UTF-8)<br>
                    <code>.lock</code> 배타적 파일 락 (크래시 시 OS 자동 해제)<br>
                    임베디드 <code>postgres:18-alpine</code> 루트 (~90 MB)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. hyper9 (h9) Plan 9 Layer</div>
                  <div class="schematic-desc">
                    리눅스 커널 부팅 · Docker 데몬 <strong>0개</strong><br>
                    KVM / Native Syscall / Hypervisor.framework / WHP<br>
                    Plan 9 커널의 Linux Personality가 시스콜 에뮬레이션<br>
                    호스트 루프백 직접 바인딩 + <code>fsync</code> 디스크 직결
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. On-Demand CLI &amp; CI</div>
                  <div class="schematic-desc">
                    <code>minipg run -- go test ./...</code> (<code>DATABASE_URL</code>)<br>
                    단일 <code>SELECT</code> 지연 <code>0.24 ms</code> · 기동 <code>~2s</code><br>
                    유휴 60초 자동 종료 · 90ms 일회용 <code>psql</code> 머신<br>
                    <code>kill -9</code> 스트레스 테스트 후 WAL 자동 복구
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">progrium.github.io/minipg 실화면 — 단일 실행 파일 PostgreSQL 18 CLI 규격 및 브라우저 데모</span>
              </div>
              <img src="../assets/images/demo_minipg.png" alt="minipg Official Site and Live Browser Demo Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ progrium.github.io/minipg/ 실화면: `.pgdb` 디렉터리 구조, `minipg run` 환경변수 주입 워크플로우 및 v86+JSPI 기반 브라우저 내장 PostgreSQL 18 라이브 데모 진입 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 &amp; 아키텍처 분기점: 로컬 개발·CI에서 '도커세(Docker Tax)'를 없애다
            </h3>
            <p>
              솔직한 엔지니어링 한계 역시 분명하다. <code>h9</code>의 네이티브 백엔드(KVM 미사용 Linux)는 시스템 콜마다 스레드 간 왕복이 발생해 단일 <code>SELECT</code> 지연이 네이티브 대비 약 2배(<code>0.24 ms</code> vs <code>0.11 ms</code>), 4클라이언트 읽기 처리량은 약 12배(<code>3,800 tps</code> vs <code>44,900 tps</code>) 느리며, <code>fork()</code> 시 CoW(Copy-on-Write)를 공유하지 않아 커넥션당 약 33 MB의 게스트 메모리를 추가로 사용한다. 따라서 저자는 명확히 선을 긋는다—고부하 프로덕션이 아니라 <strong>로컬 개발, 단일 바이너리로 DB까지 묶어 배포하려는 온프레미스 앱, 그리고 GitHub Actions 같은 비특권 CI 환경</strong>이 주무대라는 것이다.
            </p>
            <ul>
              <li><strong>매니지드 Postgres와 로컬 컨테이너 생태계에 던진 균열:</strong> CI 파이프라인 하나 돌리자고 도커 인 도커(DinD) 권한이나 외부 클라우드 테스트 DB를 프로비저닝하던 관행이 정적 musl 바이너리 1개로 대체된다. <code>minipg init test.pgdb &amp;&amp; minipg run test.pgdb -- go test ./...</code> 두 줄이면 끝이다.</li>
              <li><strong>도커 이미지 자체를 '실행 컴포넌트'로 삼키는 패턴:</strong> <code>minipg</code>는 도커 이미지를 컨테이너 런타임 없이 그냥 '정적 루트 파일시스템 패키지'로 소비한다. <code>minipg fetch 17</code>로 다른 메이저 버전의 공식 Alpine 이미지를 받아 캐시할 수 있다는 발상은, 향후 모든 리눅스 서버 소프트웨어를 단일 실행 파일로 패키징하는 새로운 표준을 예고한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 무거운 클라우드 스택을 주머니 속 폴더 하나로 접어 넣다
            </h3>
            <p>
              소프트웨어 공학의 진보는 때로 기능을 더하는 것이 아니라, 당연하게 감수하던 거대한 껍데기를 통째로 도려낼 때 일어난다. <code>minipg</code>는 우리가 데이터베이스를 쓰기 위해 얼마나 많은 컨테이너 데몬과 설정 지옥을 짊어지고 있었는지를 폭로한다.
            </p>
            <p>
              오늘 밤 당신의 프로젝트 폴더에 <code>app.pgdb</code>라는 작은 디렉터리 하나가 놓인다. SQLite처럼 가볍게 복사하고 지울 수 있으면서도, 그 안에는 진짜 PostgreSQL 18이 숨 쉬고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=minipg+postgresql+single+executable+hyper9" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://progrium.github.io/minipg/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 라이브 웹 데모 체험
              </a>
              <a href="https://github.com/progrium/minipg" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
