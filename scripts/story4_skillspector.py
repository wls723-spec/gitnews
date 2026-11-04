# -*- coding: utf-8 -*-
# Story 4: NVIDIA/SkillSpector

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] NVIDIA/SkillSpector : AI 에이전트 스킬 보안 분석기 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_skillspector.jpg" alt="NVIDIA SkillSpector AI Agent Security Scanner" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield-alert" style="width:12px;height:12px;fill:#fff;"></i> NVIDIA SECURITY</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🛡️ AI 에이전트 공급망 보안</span>
              <span class="aggro-tag">🚨 분석 대상 스킬 중 26.1% 취약 · 5.2% 악의적 악성코드</span>
              <span class="platform-tag">GitHub Trending & NVIDIA</span>
              <span class="platform-tag">NVIDIA / SkillSpector</span>
            </div>
            
            <h2 class="article-lead-headline">
              에이전트 스킬 생태계에 침투한 트로이 목마를 잡다: 엔비디아가 공개한 에이전트 스킬 보안 정적 분석기 'SkillSpector'
            </h2>

            <div class="article-subheadline">
              "당신이 깃허브에서 무심코 복붙한 SKILL.md가 회사의 AWS 키를 빼돌리고 있다" — 앤스로픽 Claude Code, 오픈AI Codex, MCP(모델 컨텍스트 프로토콜) 플러그인의 17개 카테고리 71개 공격 벡터를 사전 전수 검사하는 엔비디아의 공식 오픈소스 가디언
            </div>
            <p class="article-snippet">
              은닉된 제로 너비 유니코드 프롬프트 인젝션, 시스템 네이티브 도구를 가로채는 MCP 도구 섀도잉(Shadowing), OSV.dev 실시간 CVE 연동, 정적 AST 파싱과 LLM 시맨틱 교차 검증. 0~100 리스크 스코어링으로 위험 스킬 설치를 원천 봉쇄.
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
              <i data-lucide="flame"></i> 1. 리드: '에이전트 스킬'의 황금기 뒤에 도사린 공급망 재앙
            </h3>
            <p>
              2026년, 전 세계 개발자들의 업무 환경은 '에이전트 스킬(Agent Skills: <code>SKILL.md</code>)'과 'MCP(Model Context Protocol)'의 시대로 완전히 전환되었다. 
              인터넷에서 <em>"최적의 SEO 스킬"</em>, <em>"원클릭 쿠버네티스 배포 스킬"</em>이라는 마크다운 파일 하나만 다운받아 <code>~/.claude/skills/</code> 폴더에 집어넣으면, 
              AI 에이전트가 전문가처럼 척척 터미널 명령을 내리고 코드를 작성한다.
            </p>
            <p>
              그러나 이 편리함은 거대한 보안 구멍을 낳았다. 
              전통적인 <code>npm</code>이나 <code>pip</code> 패키지는 수십 년간 축적된 보안 스캐너와 취약점 DB가 감시하지만, 
              <strong>자연어 마크다운과 파이썬 훅으로 구성된 에이전트 스킬은 '암묵적 신뢰(Implicit Trust)' 속에 아무런 사전 검증 없이 실행</strong>되어 왔기 때문이다.
            </p>
            <p>
              이 맹점을 겨냥해, 인공지능 하드웨어 및 인프라의 절대 강자 <strong>엔비디아(NVIDIA)</strong>가 충격적인 연구 결과와 함께 칼을 빼 들었다. 
              엔비디아 보안 연구팀이 인터넷에 유통 중인 <strong>31,132개의 실제 에이전트 스킬을 전수 분석한 결과, 무려 26.1%에서 보안 취약점이 발견되었고, 5.2%는 명백히 시스템 권한 탈취를 노린 악성코드</strong>로 확인되었다. 
              엔비디아는 이 위기를 진화하기 위해 공식 보안 스캐너 <strong>SkillSpector(NVIDIA/SkillSpector)</strong>를 오픈소스로 전격 배포했다.
            </p>

            <div class="editorial-quote danger">
              "에이전트는 터미널에 직접 시스템 콜을 던지는 존재입니다. 
              악의적인 스킬 하나가 <code>SKILL.md</code> 내부에 투명한 유니코드 프롬프트 인젝션을 심어두면, 
              <strong>에이전트는 주인의 눈을 피해 로컬 <code>~/.ssh/id_rsa</code> 키와 AWS 자격증명을 원격 해커 서버로 전송합니다.</strong> 
              SkillSpector는 에이전트가 실행되기 전, 스킬 파일을 읽는 순간 모든 트로이 목마를 사살합니다."
              <span class="quote-author">— 엔비디아 AI 보안 아키텍처 팀 선언문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 17개 카테고리 71대 공격 벡터 전수 검사
            </h3>
            <p>
              <code>SkillSpector</code>는 엔비디아가 자사의 <strong>'NVIDIA Verified Skills'</strong> 공식 생태계 검수용으로 사용하던 내부 보안 엔진을 그대로 오픈소스화한 것이다. 
              Git 리포지토리 URL, 로컬 디렉토리, 압축 ZIP 파일, 단일 마크다운 파일 등 어떤 형태든 즉시 인입받아 17개 카테고리의 공격을 정밀 탐지한다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="shield-check" style="color:#f59e0b;"></i> NVIDIA SkillSpector: 2단계 정적 AST 분석 및 실시간 CVE 게이트</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">VERIFIED SKILL PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 정적 AST & YARA 스캔</div>
                  <div class="step-title">Static Taint Tracking</div>
                  <div class="step-desc">코드 AST 파싱으로 비인가 셸 호출(eval, exec), 위험 파일 I/O 및 악성 서명 패턴 즉시 탐지.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 프롬프트 인젝션 해부</div>
                  <div class="step-title">Zero-Width & Anti-Refusal</div>
                  <div class="step-desc">제로 너비 공백 문자 은닉, 시스템 프롬프트 탈취 유도문, 안전장치 우회(Jailbreak) 트리거 적발.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. MCP 도구 포이즈닝 검사</div>
                  <div class="step-title">Tool Shadowing Detection</div>
                  <div class="step-desc">기존 안전 도구(read_file 등)와 동일한 이름으로 등록해 악의적 훅으로 낚아채는 섀도잉 공격 차단.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 실시간 CVE DB 연동</div>
                  <div class="step-title">OSV.dev Live Query</div>
                  <div class="step-desc">스킬 내부 핀(Pinned)된 외부 의존성 라이브러리의 공개 취약점을 실시간 OSV.dev로 교차 대조.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 리스크 스코어링 & SARIF</div>
                  <div class="step-title">Risk Index (0-100)</div>
                  <div class="step-desc">위험도 점수 산출, CI/CD 자동 차단 게이트웨이 및 엔터프라이즈 표준 SARIF 보안 감사 보고서 출력.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 'MCP 도구 섀도잉(Tool Shadowing)' 차단 기법
            </h3>
            <p>
              최근 해커들이 에이전트 스킬 생태계에서 가장 악랄하게 사용하는 수법은 **'MCP 도구 섀도잉(Rule B.3.2)'**이다. 
              에이전트가 평소 자주 사용하는 <code>read_file</code>이나 <code>git_status</code> 같은 기본 도구 이름을 스킬 설정 파일에서 똑같이 덮어씌운다. 
              에이전트는 자신이 정상적인 파일을 읽는 줄 알고 그 도구를 호출하지만, 실제로는 해커가 제작한 파이썬 스크립트가 실행되어 파일 내용을 외부 웹훅(Webhook)으로 유출한다.
            </p>
            <p>
              <code>SkillSpector</code>는 이 공격을 사전에 무력화하기 위해 **최소 권한 원칙(Least Privilege Analysis)**을 적용한다. 
              등록된 모든 MCP 도구의 입출력 데이터 흐름을 테인트 분석(Taint Analysis)으로 추적하고, 
              기존 시스템 네이티브 도구와의 네임스페이스 충돌 여부를 감지하여 즉시 `CRITICAL (CVSS 9.1)` 등급의 경고를 띄운다.
            </p>

            <!-- 실제 소프트웨어 UI 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_skillspector_terminal.jpg" alt="NVIDIA SkillSpector 터미널 보안 스캔 및 위험 차단 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>NVIDIA SkillSpector 실시간 터미널 진단 캡처:</strong> Claude Code용 외부 스킬 검사 결과, MCP 도구 섀도잉(Rule B.3.2)과 제로 너비 프롬프트 인젝션이 감지되어 위험 점수 89/100점으로 설치가 자동 차단(BLOCKED)되고 SARIF 감사 보고서가 생성되는 모습.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 엔터프라이즈 에이전트 생태계의 '앱스토어 검수' 표준
            </h3>
            <p>
              애플이 아이폰 앱스토어의 엄격한 보안 심사를 통해 모바일 생태계의 신뢰를 구축했듯, 
              자율 AI 에이전트 시대의 패권은 <strong>"누가 가장 안전하고 신뢰할 수 있는 스킬 카탈로그를 통제하는가"</strong>에 달려 있다.
            </p>
            <p>
              엔비디아의 노림수는 명확하다. 
              자체 하드웨어(GPU)에 이어, 기업들이 안심하고 에이전트를 도입할 수 있도록 <strong>'NVIDIA Verified Skills'라는 보안 인증 도장을 업계 표준으로 확립</strong>하겠다는 것이다. 
              금융, 의료, 방산 등 데이터 유출에 극도로 민감한 글로벌 500대 기업들에게 <code>SkillSpector</code>의 통과는 필수적인 컴플라이언스 관문이 될 전망이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 자율성의 크기만큼 검증의 벽도 높아져야 한다
            </h3>
            <p>
              에이전트가 우리를 대신해 코드를 짜고, 서버를 배포하며, 이메일을 보내는 시대는 분명 축복이다. 
              그러나 그 자율성은 시스템의 루트 권한과 맞닿아 있다. 
              검증되지 않은 마크다운 파일 하나에 회사의 운명을 맡길 수는 없다.
            </p>
            <p>
              엔비디아가 <code>SkillSpector</code>를 통해 던진 경고는 업계 전체의 안전벨트다. 
              무결성이 보장되지 않은 지능은 흉기가 될 수 있다. 
              이제 모든 에이전트 설치의 첫 번째 줄에는 반드시 보안 검증이 자리해야 한다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://docs.nvidia.com/skills/scanning-agent-skills" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="shield-check"></i> 엔비디아 공식 보안 가이드
              </a>
              <a href="https://www.youtube.com/results?search_query=NVIDIA+SkillSpector+agent+skills+security" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/NVIDIA/SkillSpector" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 4 (skillspector) module loaded successfully.")
