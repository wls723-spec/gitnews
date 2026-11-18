# -*- coding: utf-8 -*-
# Story 2: agent-substrate/substrate

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] agent-substrate/substrate                        -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_substrate.jpg" alt="Agent Substrate Zero-Trust Kubernetes Sandbox Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield" style="width:12px;height:12px;fill:#fff;"></i> ZERO-TRUST INFRA</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ccfbf1; border-color:#0d9488; color:#115e59;">🐙 수백만 AI 에이전트용 제로트러스트 OS</span>
              <span class="platform-tag">GitHub Trending &amp; ate.dev</span>
              <span class="platform-tag">agent-substrate / substrate</span>
            </div>

            <h2 class="article-headline">
              에이전트가 '멍때리며 기다리는 시간'의 클라우드 낭비를 끝낸다: 500ms 만에 microVM을 순간이동시키는 'Agent Substrate'
            </h2>

            <div class="article-subheadline">
              대기 중인 에이전트의 메모리·디스크 상태를 통째로 스냅샷해 10~30배 밀도로 압축하고, 샌드박스 내부에 API 키를 단 1바이트도 두지 않는 Apache-2.0 쿠버네티스 런타임 (+469스타/일)
            </div>
            <p class="article-snippet">
              자율 코딩 에이전트가 수천, 수만 개로 늘어나면서 기업 인프라는 두 가지 악몽에 직면했습니다. 하나는 LLM 응답과 사람의 승인을 기다리며 90%의 시간을 허비하는 컨테이너가 클라우드 비용을 폭증시키는 문제이고, 다른 하나는 프롬프트 인젝션에 뚫린 에이전트가 환경변수의 API 키를 털어가는 보안 사고입니다. 오늘 469스타를 보태며 급상승한 <strong>agent-substrate/substrate</strong>(v1.0)는 gVisor와 Cloud Hypervisor microVM 스냅샷 텔레포트와 외부 이그레스 게이트웨이 자격증명 주입으로 이 난제를 한 번에 해결합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 8개의 파드 위에 250명의 AI 에이전트를 올려놓고 벌어지는 일
            </h3>
            <p>
              쿠버네티스 클러스터 모니터링 대시보드에 불과 8개의 물리적 워커 파드(Pod)만 떠 있다. 그런데 그 위에서 실제로 살아 움직이며 코드 파일을 수정하고, 테스트를 돌리고, 외부 API와 대화하는 상태 유지(Stateful) AI 에이전트는 무려 250개에 달한다. 에이전트 한 명이 LLM 토큰 스트리밍을 기다리거나 사용자의 다음 지시를 기다리며 멈추는 순간, 시스템은 그 에이전트의 RAM과 파일시스템 상태를 통째로 스냅샷으로 얼려 치우고, 0.5초(500ms)도 안 되는 찰나에 대기열의 다른 에이전트를 빈 워커 파드 위로 깨워 올린다.
            </p>
            <p>
              구글의 분산 에이전트 런타임(<code>google/ax</code>)과 CNCF 샌드박스 프로젝트 <code>kagent</code>가 기반 인프라로 채택하며 오늘 하루 469스타(누적 7,592스타)를 끌어모은 <strong>agent-substrate/substrate</strong>는 기존 웹 서버용 컨테이너 오케스트레이션이 풀지 못했던 '에이전트 시대의 인프라 병목'을 정면으로 겨냥한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 웹 서버가 아닌 '대기 시간이 90%인 악의적 액터'를 위한 런타임
            </h3>
            <p>
              전통적인 마이크로서비스는 요청이 들어오면 수 밀리초 만에 계산을 마치고 상태를 버린다. 반면 자율 코딩 에이전트는 작업 디렉토리와 백그라운드 프로세스, 세션 메모리를 유지한 채 모델 추론과 도구 실행, 인간의 확인을 기다리며 일생의 대부분을 유휴 상태(Idle)로 보낸다. 동시에 에이전트가 실행하는 임의의 코드와 웹 브라우징 결과는 언제든 프롬프트 인젝션으로 오염될 수 있는 '적대적 워크로드'다.
            </p>

            <div class="editorial-quote">
              <p>
                "Substrate는 모든 액터(에이전트)를 신뢰할 수 없고 상호 적대적인 존재로 취급한다. <strong>샌드박스 내부에는 JWT나 API 키, 클라우드 토큰이 단 하나도 존재하지 않으며</strong>, 외부 이그레스 게이트웨이가 승인된 아웃바운드 요청에만 경계 밖에서 자격증명을 주입한다."
              </p>
              <small>— Agent Substrate v1.0 Zero-Trust Security Model 공식 문서 (Apache-2.0)</small>
            </div>

            <p>
              이는 보안 패러다임의 완전한 역전이다. 일반 리눅스 컨테이너(Plain Linux Container) 자체를 지원 대상에서 아예 배제하고, 모든 액터를 VM급 격리 경계인 <code>gVisor (runsc)</code> 또는 <code>Cloud Hypervisor</code> microVM 내부에만 가둠으로써 다중 테넌트가 물리 노드를 공유해도 탈출 불가능한 벽을 세웠다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 액터 텔레포트와 무자격증명(Zero-Credential) 경계 방어
            </h3>
            <p>
              Go로 작성된 Agent Substrate 1.0 아키텍처는 표준 쿠버네티스(Pods, NetworkPolicies, Autoscaling) 위에서 세 가지 독자적인 서브시스템을 맞물려 돌아가게 만든다:
            </p>
            <ul>
              <li><strong>액터 텔레포트 &amp; 10~30배 초과 구독 (Oversubscription):</strong> 수많은 상태 유지 '액터(Actors)'를 소수의 웜(Warm) '워커(Workers)' 파드 풀에 매핑한다. 유휴 상태에 빠진 액터의 RAM 작업 메모리와 디스크 상태를 스냅샷해 내리고, 요청이 들어오면 초당 500회 이상의 활성화 속도로 <strong>500ms 미만</strong>에 임의의 워커 위로 원형 복구한다.</li>
              <li><strong>SPIFFE 기반 암호학적 신원 &amp; <code>atenet-egress</code>:</strong> 모든 활성 액터는 단기 수명 SPIFFE X.509 인증서를 부여받지만, 정작 에이전트 프로세스는 API 키를 만질 수 없다. 모든 아웃바운드 트래픽은 <code>atenet-egress</code> 게이트웨이를 통과하며 정책 엔진(DLP·프롬프트 인젝션 검사·IAM)이 승인한 요청에만 경계 밖에서 시크릿 헤더를 삽입한다.</li>
              <li><strong>프레임워크 무관 OCI 호환성:</strong> 특정 에이전트 SDK에 종속되지 않으며 표준 OCI 컨테이너 이미지를 그대로 받아 ADK, LangChain, Claude Code, Codex, MCP 서버까지 수정 없이 microVM 액터로 격리 실행한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Agent Substrate 제로트러스트 microVM 텔레포트 &amp; 이그레스 격리 아키텍처</span>
                <span class="schematic-badge">Apache-2.0 · Go · K8s Native</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Untrusted Actor Sandbox</div>
                  <div class="schematic-desc">
                    <code>gVisor (runsc)</code> / <code>Cloud Hypervisor</code><br>
                    일반 리눅스 컨테이너 원천 차단<br>
                    API 키·토큰 0% (탈취 불가능 환경)<br>
                    인바운드는 <code>atenet-router</code>만 허용
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Actor Teleport &amp; Warm Pool</div>
                  <div class="schematic-desc">
                    유휴 액터 RAM + 파일시스템 스냅샷<br>
                    8개 파드에 250+ 액터 10~30배 밀집<br>
                    요청 시 <strong>&lt;500ms</strong> 내 워커로 즉시 복원<br>
                    초당 500+ 액티베이션 처리량 달성
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Egress Gateway PEP</div>
                  <div class="schematic-desc">
                    <code>atenet-egress</code> 경계 밖 시크릿 주입<br>
                    SPIFFE X.509 및 온디맨드 JWT 발급<br>
                    플러그인형 DLP·인젝션 차단 정책<br>
                    외부 LLM·DB·SaaS API 안전 호출
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Agent Substrate 공식 포털 (ate.dev) 실구동 아키텍처 뷰</span>
              </div>
              <img src="../assets/images/demo_substrate.png" alt="Agent Substrate Official Portal" class="showcase-img">
              <p class="showcase-caption">
                ▲ ate.dev 공식 포털 실화면: 유휴 에이전트를 메모리에서 동결하고 요청 시 500ms 이내에 워커 파드로 복구해 10배 이상의 클러스터 밀도를 달성하는 제로트러스트 런타임 구조를 소개한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 클라우드 경제학의 전환점: '초당 과금'에서 '사고(Thinking) 시간만 과금'으로
            </h3>
            <p>
              Agent Substrate v1.0의 등장은 클라우드 에이전트 호스팅 시장의 단위 경제학(Unit Economics)을 송두리째 바꾼다.
            </p>
            <ul>
              <li><strong>유휴 비용 90% 증발:</strong> 코딩 에이전트가 사람의 리뷰를 기다리며 밤새 켜져 있어도 물리 메모리와 CPU를 점유하지 않는다. 스냅샷 스토리지 비용만 남기고 실제 연산 자원은 다른 활성 에이전트에게 즉시 재할당된다.</li>
              <li><strong>엔터프라이즈 도입 장벽 해소:</strong> 금융·의료·빅테크 보안팀이 자율 에이전트 도입을 주저하던 가장 큰 이유인 "프롬프트 인젝션 한 방에 사내 GitHub 토큰과 클라우드 키가 털리는 악몽"을 아키텍처 레벨에서 차단했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 수백만 에이전트가 공존하는 도시의 '보이지 않는 전력망'
            </h3>
            <p>
              2025년이 에이전트가 코드를 짜고 도구를 부르는 법을 익힌 해였다면, 2026년 말은 그 수백만 개의 에이전트를 어떻게 파산하지 않고 해킹당하지 않으며 한 클러스터에 태울 것인가를 푸는 인프라 전쟁의 해다.
            </p>
            <p>
              화려한 모델 발표 뒤에 숨어 조용히 1.0을 선언한 Agent Substrate는, AI 시대의 쿠버네티스가 무엇을 기본 전제로 삼아야 하는지 가장 냉철한 답안을 제시했다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Agent+Substrate+Kubernetes+microVM+sandbox" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://ate.dev/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 홈페이지 (ate.dev)
              </a>
              <a href="https://github.com/agent-substrate/substrate" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
