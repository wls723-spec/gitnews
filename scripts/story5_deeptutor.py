# -*- coding: utf-8 -*-
# Story 5: HKUDS/DeepTutor

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] HKUDS/DeepTutor : 평생 맞춤형 1:1 인공지능 튜터 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_deeptutor.jpg" alt="HKUDS DeepTutor Personalized Tutoring" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="graduation-cap" style="width:12px;height:12px;fill:#fff;"></i> HKU RESEARCH</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🎓 에듀테크 지각변동</span>
              <span class="aggro-tag">🔥 4.6만 스타 · 체그(Chegg) 몰락 후 등장한 소크라테스 튜터</span>
              <span class="platform-tag">GitHub Trending & arXiv</span>
              <span class="platform-tag">HKUDS / DeepTutor</span>
            </div>
            
            <h2 class="article-lead-headline">
              체그(Chegg)의 몰락과 1:1 소크라테스 튜터의 탄생: 평생 학습 인지 그래프 기반 개인화 과외 에이전트 'DeepTutor'
            </h2>

            <div class="article-subheadline">
              "정답을 복붙해 주던 앵무새 AI는 교육이 아니다" — 홍콩대학교 데이터사이언스 연구실(HKUDS), 학생의 오개념을 실시간 추적하고 소크라테스식 문답법으로 뇌를 자극하는 오픈소스 평생 튜터 DeepTutor v1.6.15 전격 공개
            </div>
            <p class="article-snippet">
              유한 튜터링 메모리(Bounded Memory)로 학습 결손 복구, LightRAG 기반 교재·논문 지식 그래프, 수학 기호 및 코드 실행 네이티브 지원. 월 수백만 원짜리 입시 사교육을 모든 학생의 브라우저에서 0원으로 실현한 교육 평등의 분기점.
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
              <i data-lucide="flame"></i> 1. 리드: 14조 원짜리 에듀테크 공룡의 몰락과 그 너머
            </h3>
            <p>
              한때 기업가치 120억 달러(약 16조 원)에 달했던 미국 최대 온라인 교육 기업 <strong>체그(Chegg)</strong>의 주가는 지난 2년간 99% 폭락했다. 
              대학생들이 매달 20달러씩 내고 숙제 정답을 베끼던 플랫폼이, 챗GPT(ChatGPT)의 등장과 함께 순식간에 사망 선고를 받은 것이다.
            </p>
            <p>
              그러나 챗GPT가 과연 진정한 교육을 실현했는가? 대다수 교육학자들의 대답은 냉소적이다: 
              <em>"정답을 1초 만에 알려주는 생성형 AI는 학생들에게 생각할 기회를 빼앗고 '인지적 무기력증(Cognitive Atrophy)'만을 안겨주었다."</em> 
              정답을 출력하는 기계와 인간의 지적 성장을 이끄는 '진짜 스승' 사이에는 메울 수 없는 심연이 존재했다.
            </p>
            <p>
              이 교육적 위기를 돌파하기 위해, 아시아 최고 연구진인 <strong>홍콩대학교 데이터사이언스 연구실(HKUDS)</strong>이 
              <strong>arXiv:2604.26962 연구 논문과 함께 오픈소스 프로젝트 DeepTutor(HKUDS/DeepTutor)</strong>를 공개하며 
              <strong>누적 스타 4만 6,000개</strong>를 돌파했다. 
              학생에게 정답을 던져주지 않고, 질문과 힌트를 통해 스스로 깨우치게 만드는 **'소크라테스식 평생 개인 튜터'**의 완성이다.
            </p>

            <div class="editorial-quote danger">
              "교육의 본질은 답을 주는 것이 아니라, 질문을 던져 학생의 뇌 신경망을 재배선하는 것입니다. 
              <strong>DeepTutor는 학생이 어디서 왜 막혔는지 인지 그래프(Cognitive Graph)로 추적하며, 
              학생이 논리적 오류를 스스로 발견할 때까지 결코 최종 답안을 먼저 발설하지 않습니다.</strong> 
              이것이야말로 2,400년 전 소크라테스가 아테네 거리에서 실천했던 산파술(Maieutics)의 디지털 부활입니다."
              <span class="quote-author">— 홍콩대 DeepTutor 수석 연구진 논문 발표 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 학생의 지식 결손을 메우는 5단계 소크라테스 문답 루프
            </h3>
            <p>
              <code>DeepTutor</code>의 핵심 아키텍처는 단순한 텍스트 챗봇이 아니다. 
              학생이 제출한 질문, 코드, 수식 풀이 과정을 역추적하여 <strong>'오개념(Misconception) 맵'</strong>을 실시간 생성하고, 
              학생의 수준에 맞는 스캐폴딩(Scaffolding: 인지적 발판)을 단계별로 제공한다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="book-open" style="color:#f59e0b;"></i> DeepTutor: 소크라테스 문답법 & 평생 인지 그래프 순환 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">SOCRATIC PEDAGOGY LOOP</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 학생 상태 진단</div>
                  <div class="step-title">Cognitive Tracing</div>
                  <div class="step-desc">학생의 발화와 수식 입력에서 미적분·선형대수 선행 개념 이해도 및 오개념 발생 지점 정밀 포착.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 소크라테스 반문 생성</div>
                  <div class="step-title">Guided Inquiry</div>
                  <div class="step-desc">정답을 숨긴 채, 학생이 모순을 자각할 수 있도록 단계별 유도 질문과 힌트를 동적으로 출제.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. LightRAG 교재 연동</div>
                  <div class="step-title">Graph Knowledge Base</div>
                  <div class="step-desc">PDF 전공서적, 논문, 연습문제를 지식 그래프로 구조화하여 권위 있는 출처 근거 제시.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 유한 메모리 세션 복구</div>
                  <div class="step-title">Bounded Tutoring Memory</div>
                  <div class="step-desc">세션이 끊겨도 과거 수주일간의 오답 노트와 취약 단원 맥락을 손실 없이 다음 대화에 주입.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 마스터리 패스 인증</div>
                  <div class="step-title">Mastery Path Progression</div>
                  <div class="step-desc">스스로 문제를 해결했을 때만 다음 고난도 챕터를 개방하고 개인 맞춤형 성취도 리포트 발행.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 유한 메모리 큐와 네이티브 다국어·수식 파싱
            </h3>
            <p>
              이번 10월 <code>v1.6.15</code> 최신 릴리즈에서 <code>DeepTutor</code>는 상용화 수준의 견고함을 달성했다:
            </p>
            <ul style="margin: 1rem 0 1.5rem 1.5rem; line-height: 1.8; color: var(--text-dark);">
              <li><strong>유한 튜터링 메모리(Bounded Memory):</strong> 수십 시간에 달하는 긴 대화 속에서도 핵심 학습 이력만을 지능적으로 압축하여 컨텍스트 윈도우 초과를 방지하고 세션을 안정적으로 복구.</li>
              <li><strong>다중 언어 및 수식 렌더링:</strong> 영어, 한국어, 일본어, 프랑스어 등 12개 언어 네이티브 지원 및 KaTeX 수식, 파이썬 코드 실행기 완벽 통합.</li>
              <li><strong>로컬 폴더 지식 베이스:</strong> 사용자가 자신의 강의 자료나 교재 PDF 폴더를 지정하기만 하면, 원클릭으로 LightRAG 인덱스를 생성하여 학습에 활용.</li>
              <li><strong>차세대 풀스택 스택:</strong> Next.js 16 프론트엔드와 고성능 FastAPI 백엔드로 구성되어 개인 노트북(Apple Silicon / RTX)에서 완전 오프라인 구동 가능.</li>
            </ul>

            <!-- 실제 소프트웨어 UI 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_deeptutor_ui.jpg" alt="DeepTutor의 소크라테스 대화 인터페이스 및 학습 워크스페이스" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>DeepTutor 웹 워크스페이스 실구동 캡처:</strong> 교재 지식 베이스를 기반으로 학생에게 단계별 소크라테스 반문을 제시하고, 학생의 답변을 인지 그래프에 반영하며 수식과 도표를 실시간 인터랙티브하게 풀어가는 화면.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 수십조 원 사교육 시장의 민주화
            </h3>
            <p>
              지금까지 양질의 1:1 맞춤형 과외는 시간당 수십만 원을 지불할 수 있는 부유층 자녀들만의 전유물이었다. 
              체그나 코세라(Coursera) 같은 플랫폼조차 일방향 강의나 정답 자판기 수준에 머물렀다.
            </p>
            <p>
              <code>DeepTutor</code>의 등장은 <strong>'양질의 개인 교사를 모든 학생에게 무상 보급'</strong>할 수 있는 기술적 토대를 마련했다. 
              학교 교사는 학생 개개인의 취약점을 분석하는 보조 도구로 활용할 수 있고, 개발도상국의 학생들은 최상급 명문대 교수 수준의 1:1 튜터링을 무료로 누릴 수 있다. 
              교육의 사다리가 인공지능을 통해 복원되고 있는 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 호기심이라는 불꽃을 지피는 오픈소스의 힘
            </h3>
            <p>
              시인 윌리엄 버틀러 예이츠는 <em>"교육은 양동이를 채우는 것이 아니라, 불을 지피는 것이다(Education is not the filling of a pail, but the lighting of a fire)"</em>라고 갈파했다.
            </p>
            <p>
              정답을 복사해 주는 인공지능은 양동이를 넘치게 할 뿐이지만, 
              학생에게 질문을 던지고 사고를 확장해 주는 <code>DeepTutor</code>는 호기심의 불꽃을 지핀다. 
              오픈소스 기술이 인간의 지적 존엄성과 만나는 가장 아름다운 현장이 지금 펼쳐지고 있다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://deeptutor.info" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 바로가기
              </a>
              <a href="https://www.youtube.com/results?search_query=HKUDS+DeepTutor+Personalized+Tutoring" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/HKUDS/DeepTutor" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 5 (deeptutor) module loaded successfully.")
