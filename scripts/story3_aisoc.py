# -*- coding: utf-8 -*-
# Story 3: beenuar/AiSOC

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] beenuar/AiSOC : 차세대 자율 사이버 보안 요새 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_aisoc.jpg" alt="AiSOC Autonomous Security Operations Center" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 보안 관제사 번아웃을 종식하는 자율 사이버 방패</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">beenuar / AiSOC</span>
            </div>
            
            <h2 class="article-headline">
              "하루 10,000건의 오탐 알림 지옥을 끝낸다": 오픈소스 자율 AI 보안 관제 센터(AiSOC)의 등장
            </h2>

            <div class="article-subheadline">
              "경보 피로(Alert Fatigue)로 무너진 방어선을 AI 에이전트 군단이 지킨다" — SIEM, EDR, 방화벽에서 쏟아지는 방대한 텔레메트리를 120초 만에 그래프 기반으로 융합(Fusion)하고, MITRE ATT&CK 전술 매핑부터 공격 차단 승인 요청까지 자율 완결하는 무료·셀프호스팅 AI SOC의 혁명
            </div>
            <p class="article-snippet">
              수억 원대 상용 솔루션(Splunk, Palo Alto) 없이도 사내 온프레미스에서 0원의 API 비용으로 구동. AI 에이전트의 모든 추론과 판단 과정을 암호학적 결정 원장(Decision Ledger)에 투명하게 기록하는 엔터프라이즈 보안의 새 기준.
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
              <i data-lucide="flame"></i> 1. 리드: 새벽 2시, 쏟아지는 1만 건의 붉은 경보와 침묵하는 보안 요새
            </h3>
            <p>
              사이버 보안 관제 센터(SOC)의 야간 근무는 현대 IT 산업에서 가장 가혹한 노동 현장 중 하나다. 
              수백 대의 서버와 클라우드 인프라에서 매일 수만 건의 붉은색 경보가 모니터에 점멸한다. 
              그러나 그중 99%는 정상적인 배치 작업이나 오작동으로 인한 <strong>'오탐(False Positive)'</strong>이다. 
              관제사들은 눈이 충혈된 채 알림 창을 닫는 단순 반복 작업에 짓눌리고, 그 피로의 틈새로 침투한 진짜 해커의 공격 한 건이 기업의 운명을 무너뜨린다.
            </p>
            <p>
              이 고질적인 '경보 피로(Alert Fatigue)'의 사슬을 끊기 위해 깃허브에 혜성처럼 등장한 프로젝트가 바로 <strong>beenuar/AiSOC</strong>다. 
              버전 21.0.0으로 공개된 이 오픈소스 플랫폼은 엔터프라이즈 보안 관제의 전 과정을 <strong>자율 AI 에이전트 스웜(Swarm)</strong>으로 자동화했다.
            </p>
            <p>
              AiSOC에 보안 로그가 유입되면, 인간 관제사 대신 지능형 에이전트들이 120초 만에 파편화된 수천 건의 알림을 단일 공격 시나리오로 엮어낸다. 
              그리고 MITRE ATT&CK 매트릭스에 기반해 침투 경로를 추적한 뒤, "이것은 정상 백업이 아니라 APT 조직의 크리덴셜 탈취 시도입니다. 감염 노드를 격리하시겠습니까?"라는 단 하나의 명확한 질문과 실행 버튼을 인간 책임자에게 제시한다.
            </p>

            <div class="editorial-quote danger">
              "공격자들은 이미 LLM과 자동화 스크립트로 무장하여 초 단위로 기업의 빈틈을 스캔하고 있습니다. 
              <strong>인간이 수작업으로 로그를 열어보고 엑셀 시트에 정리하는 20년 전 방식으로는 기계의 속도로 닥쳐오는 사이버 공격을 절대 막을 수 없습니다.</strong> 
              AiSOC은 모든 엔지니어링 조직이 자신만의 지능형 보안 지휘소를 단 몇 분 만에 온프레미스에 구축할 수 있도록 만든 완전 무료 소프트웨어입니다."
              <span class="quote-author">— AiSOC 기술 백서(Technical Guide) 서문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 엔터프라이즈 보안의 병목과 오픈소스 AI SOC의 필연성
            </h3>
            <p>
              사이버 보안 시장은 팔로알토 네트웍스(Palo Alto), 스플렁크(Splunk), 크라우드스트라이크(CrowdStrike) 같은 거대 벤더들이 과점하고 있다. 
              이들의 차세대 보안 관제(SOAR/XDR) 솔루션은 연간 수억 원에 달하는 천문학적 라이선스 비용을 요구하며, 중소기업이나 오픈소스 팀에게는 그림의 떡이었다.
            </p>
            <p>
              AiSOC은 이 시장 구조를 근본적으로 뒤흔든다:
            </p>
            <ul>
              <li><strong>비용 제로의 셀프 호스팅:</strong> 외부 클라우드 API 호출 없이 로컬 오픈소스 가중치(Ollama, vLLM)로 완벽히 구동되어 토큰 비용이 발생하지 않는다.</li>
              <li><strong>극도의 프라이버시 보호:</strong> 기업의 내부 IP 대역, 서버 아키텍처, 취약점 로그가 외부 빅테크 서버로 단 1바이트도 유출되지 않는다.</li>
              <li><strong>재현 가능한 감사 원장(Replayable Decision Ledger):</strong> 기존 AI가 지닌 '블랙박스 날조' 위험을 막기 위해, 에이전트가 어떤 로그를 근거로 어떤 추론을 내렸는지 암호학적으로 기록하여 법적 분쟁 시 규제 당국에 증거로 제출할 수 있다.</li>
            </ul>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> AiSOC: 멀티소스 로그 수집에서 자율 조사 및 인간 승인까지의 파이프라인
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">단계 1: 텔레메트리 인제스천</span>
                  <strong>Multi-Source Telemetry</strong>
                  <div class="schematic-desc">
                    Syslog, Falco, Zeek, AWS CloudTrail, K8s 감사 로그를 실시간 수집. 노이즈 제거 및 단일 이벤트 포맷 정규화
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 2: 그래프 경보 융합</span>
                  <strong>Alert Fusion Engine</strong>
                  <div class="schematic-desc">
                    동일 공격 체인에 속한 수백 건의 경보를 시간축과 자산 ID 기준으로 묶어 그래프 클러스터링(단일 사건으로 압축)
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 3: 자율 추론 & 검증</span>
                  <strong>MITRE ATT&CK Agent</strong>
                  <div class="schematic-desc">
                    초기 침투(Initial Access)부터 횡적 이동(Lateral Movement)까지 전술 단계 매핑. MITRE 지식베이스 기반 교차 반증
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 4: 원장 기록 & 조치</span>
                  <strong>Ledger & Human Approval</strong>
                  <div class="schematic-desc">
                    모든 추론 근거를 변경 불가능한 원장에 서명. 방화벽 IP 차단 및 토큰 무효화 제안서를 생성해 인간 최종 승인 대기
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: 그래프 융합, MITRE 매핑, 그리고 의사결정 원장
            </h3>
            <p>
              AiSOC의 기술적 우수성은 <strong>'경보 융합(Alert Fusion)'</strong> 알고리즘에서 출발한다. 
              네트워크 스캔이 발생하면 방화벽은 수천 번의 거부 로그를 뿜어낸다. 
              AiSOC은 이를 개별 알림으로 취급하지 않고, 소스 IP와 포트 변화를 단일 방향성 비순환 그래프(DAG)로 묶어 하나의 사건(Incident)으로 축약한다.
            </p>
            <p>
              이어지는 심층 조사는 특화된 전문 에이전트들이 분담한다:
            </p>
            <ul>
              <li><strong>포렌식 에이전트:</strong> 의심스러운 엔드포인트의 메모리 덤프와 프로세스 트리(Process Tree)를 조회해 비인가 쉘 실행 여부를 판별한다.</li>
              <li><strong>인텔리전스 에이전트:</strong> 침해지표(IoC, IP, 도메인, 파일 해시)를 알려진 사이버 위협 조직(Threat Actor)의 시그니처와 대조한다.</li>
              <li><strong>감사관 에이전트(Auditor):</strong> AI의 조치 제안이 사내 SLA 규정에 부합하는지 교차 검증하고, 모든 단계를 <code>Decision Ledger</code>에 JSON-LD 형식으로 박제한다.</li>
            </ul>
            <p>
              또한 개발자를 위해 <strong>Claude Code, Cursor, Continue와 연동되는 전용 MCP(Model Context Protocol) 서버</strong>를 기본 탑재하여, 보안 담당자가 자신의 익숙한 개발 터미널 안에서 <code>@aisoc investigate incident #104</code> 형태로 실시간 대화형 조사를 지휘할 수 있다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_aisoc.jpg" alt="AiSOC Security Command Console and MITRE ATT&CK Matrix" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="monitor"></i> <strong>[실구동 아키텍처 캡처]</strong> 엔터프라이즈 환경에 배포된 AiSOC의 통합 관제 대시보드. 실시간 인프라 텔레메트리 속에서 탐지된 침투 시나리오가 MITRE ATT&CK 14대 전술 단계별로 정밀하게 시각화되어 있으며, 우측 하단에는 에이전트의 자율 판단 과정과 인간 승인용 원클릭 격리 버튼이 배치되어 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 거버넌스: 폐쇄형 보안 벤더의 해자를 허무는 오픈소스
            </h3>
            <p>
              기존 엔터프라이즈 보안 솔루션의 비즈니스 해자는 '고객 락인(Vendor Lock-in)'에 있었다. 
              수집한 로그 데이터의 양이 늘어날수록 타사 제품으로의 이전 비용이 천문학적으로 치솟았기 때문이다.
            </p>
            <p>
              AiSOC의 등장은 다음과 같은 산업적 격변을 예고한다:
            </p>
            <ul>
              <li><strong>오픈 스탠다드 기반 상호 운용성:</strong> ElasticSearch, OpenSearch, ClickHouse 등 오픈소스 빅데이터 인프라를 그대로 백엔드로 사용할 수 있어 인프라 비용을 최대 80% 이상 절감한다.</li>
              <li><strong>인공지능 규제(EU AI Act) 선제 준수:</strong> 금융 및 공공 인프라 보안에 AI를 적용할 때 필수적인 '설명 가능성(Explainability)'과 '감사 가능성(Auditability)'을 시스템 레벨에서 원장 구조로 완벽히 충족한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 기계의 속도로 맞서는 수호자들의 방패
            </h3>
            <p>
              사이버 공간의 전쟁은 이미 인간의 인지 속도를 넘어섰다. 
              해커들이 자동화된 AI 편대로 기업의 네트워크를 유린하는 시대에, 전통적인 수동 보안 관제는 더 이상 유효하지 않다.
            </p>
            <p>
              AiSOC이 던지는 메시지는 명확하다. 
              진정한 보안의 미래는 수억 원짜리 라이선스 계약서가 아니라, <strong>투명하고 감사 가능하며 누구나 스스로 구축할 수 있는 오픈소스 자율 방패</strong> 위에 지어져야 한다는 사실이다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=AiSOC+autonomous+security+operations+center" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/beenuar/AiSOC" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
