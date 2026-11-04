# -*- coding: utf-8 -*-
# Story 5: calesthio/OpenMontage

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 5] calesthio/OpenMontage -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openmontage.jpg" alt="OpenMontage Autonomous Video Production" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #5</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fce7f3; border-color:#ec4899; color:#be185d;">🎬 자율 영상 프로덕션 오케스트레이션</span>
              <span class="platform-tag">Python Daily #1</span>
              <span class="platform-tag">calesthio / OpenMontage</span>
            </div>
            
            <h2 class="article-headline">
              프롬프트 한 줄로 프리미어와 캡컷을 지휘하다: 세계 최초의 에이전트 기반 오픈소스 영상 프로덕션 시스템
            </h2>

            <div class="article-subheadline">
              "영상 생성 AI가 클립만 뱉어낼 때, 진정한 프로덕션은 타임라인 위에서 시작된다" — 기획, 대본 분할, B-roll 푸티지 매칭, 컷 편집, 오디오 마스터링, 자막 타이밍까지 12개 전문 파이프라인과 700여 개 제작 스킬이 완전 자율 작동… 코딩 어시스턴트를 풀스케일 영상 제작 스튜디오로 탈바꿈시키는 OpenMontage 전격 공개 (+7.5만 스타)
            </div>
            <p class="article-snippet">
              수백 개의 클립을 일일이 자르고 붙이느라 밤을 새우던 크리에이터들의 오랜 고통을 해방. Sora나 Runway 같은 파편화된 비디오 생성 모델들을 하나의 유기적인 비선형 편집 타임라인(NLE)으로 엮어내며 프로덕션 자동화의 새 지평을 연 프로젝트.
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
              <i data-lucide="flame"></i> 1. 리드: 쏟아지는 AI 비디오 클립과 텅 빈 타임라인의 아이러니
            </h3>
            <p>
              오픈AI의 Sora, 런웨이(Runway)의 Gen-3, 클링(Kling) 등 화려한 비디오 생성 모델들이 등장했을 때, 세상은 이제 영화와 유튜브 영상이 저절로 쏟아져 나올 것이라 믿었다. 
              그러나 영상 제작 현장의 현실은 정반대였다. 
              AI 모델들은 고작 5초, 10초짜리 단편적인 비디오 조각들만 뱉어낼 뿐이었다.
            </p>
            <p>
              결국 인간 영상 편집자는 그 수십 개의 조각들을 어도비 프리미어 프로나 파이널 컷 타임라인에 올려놓고, 일일이 자르고(Cut), 대본의 음성 파형에 맞춰 싱크를 조절하며, B-roll 인서트 컷을 끼워 넣고, 배경음악의 데시벨을 깎아내는 지루한 수작업을 밤새도록 반복해야 했다. 
              진정한 영상 제작의 병목은 <strong>'클립의 생성'이 아니라 '서사의 조립과 편집'</strong>에 있었던 것이다.
            </p>
            <p>
              이 깊은 갈증을 해결하기 위해 깃허브 파이썬 생태계 1위로 폭발적인 주목을 받으며 등장한 프로젝트가 바로 <strong>calesthio/OpenMontage</strong>다. 
              공개 직후 무려 7만 5천 개 이상의 스타를 모은 이 프로젝트는 단언한다: 
              <strong>"우리는 또 하나의 비디오 생성 모델을 만들지 않는다. 우리는 영상 제작사(Production House) 전체를 에이전트로 프로그래밍한다."</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 12개 파이프라인, 100여 개 도구, 700여 개 프로덕션 스킬의 집합체
            </h3>
            <p>
              <code>OpenMontage</code>는 Claude Code, Cursor, Cline 같은 범용 AI 코딩 어시스턴트에 마운트되는 **세계 최초의 자율 비디오 프로덕션 에이전트 시스템**이다. 
              내부에는 실제 헐리우드와 유튜브 탑 프로덕션의 실무 노하우를 집대성한 <strong>12개의 전문 제작 파이프라인</strong>과 <strong>700여 개의 정밀 에이전트 스킬 파일</strong>이 내장되어 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신이 '양자 컴퓨터의 원리를 설명하는 3분짜리 테크 다큐멘터리를 만들어줘'라고 지시하면, OpenMontage는 단순히 스크립트만 쓰는 것이 아닙니다. 
                스토리보드를 쪼개고, 각 씬에 필요한 푸티지를 로컬 라이브러리나 생성 모델에서 수급하며, 배경음악의 킥 드럼 비트에 맞춰 <strong>0.1초 단위로 컷을 치고 프리미어 프로 XML 프로젝트 파일로 익스포트</strong>합니다."
              </p>
              <small>— Calesthio AI Labs 수석 디렉터, 론칭 키노트 중</small>
            </div>

            <p>
              영상 크리에이터는 이제 타임라인 위에서 마우스를 쥐고 씨름할 필요 없이, 마치 영화감독처럼 에이전트 팀이 1차 가편집(Rough Cut)해 놓은 타임라인을 감상하고 최종 디렉팅만 내리면 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 메커니즘 해부: 기획부터 비파괴 XML 익스포트까지의 풀 루프
            </h3>
            <p>
              OpenMontage의 아키텍처는 단순한 비디오 파일 합치기(FFmpeg 무지성 연결)가 아닌, <strong>비파괴(Non-Destructive) 전문가용 프로젝트 파일 생성</strong>에 최적화되어 있다.
            </p>

            <!-- 순수 CSS 다이어그램: OpenMontage Autonomous Production Pipeline -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">PRODUCTION PIPELINE SCHEMATIC</span>
                <span class="schematic-title">OpenMontage 12대 자율 영상 제작 파이프라인 흐름도</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #f59e0b;">
                  <div class="schematic-card-title" style="color: #b45309;">Phase 1: 기획 & 대본 비트 분할</div>
                  <div class="schematic-step">• Story Arc Planner: 서사 구조 및 시청 지속률 텐션 설계</div>
                  <div class="schematic-step">• Script Beat Analyzer: 문장별 초(Second) 단위 타이밍 산출</div>
                  <div class="schematic-step">• Visual Prompt Generator: 씬별 시각적 요구사항 명세서 작성</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #3b82f6;">
                  <div class="schematic-card-title" style="color: #1d4ed8;">Phase 2: 멀티 에셋 소싱 & 음향</div>
                  <div class="schematic-step">• Asset Harvester: 로컬 스톡, 3D 에셋, AI 생성 비디오 취합</div>
                  <div class="schematic-step">• Voiceover Synthesizer: 억양과 감정이 실린 TTS 자동 생성</div>
                  <div class="schematic-step">• Audio Ducking & Mastering: 내레이션 감지 시 배경음 볼륨 자동 감소</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">Phase 3: 멀티트랙 조립 & 프로 익스포트</div>
                  <div class="schematic-step">• Multi-track Timeline Assembly: 비디오/B-roll/오디오/자막 트랙 배치</div>
                  <div class="schematic-step">• Smart Cut Engine: 점프 컷 방지 및 리듬감 있는 전환(Transition)</div>
                  <div class="schematic-step">• FCPXML / EDL / CapCut JSON: 전문 편집 툴 즉시 호환 프로젝트 출력</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ OpenMontage는 결과물을 렌더링된 단일 MP4로 끝내지 않고, 편집자가 재가공할 수 있는 멀티트랙 타임라인 프로젝트 파일로 출력하여 인간과의 완벽한 협업을 지원한다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_openmontage.png" alt="OpenMontage 백롯 보드 및 제작 대시보드 화면" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ OpenMontage 백롯 라이브 보드 (demo_openmontage.png):</strong> 
                실제 제작 파이프라인에서 씬별 비주얼 프롬프트, 오디오 파형, 자막 인/아웃 타임코드, 비트 타이밍이 시각화된 인터랙티브 프로덕션 보드 화면.
              </div>
            </div>

            <p>
              특히 독보적인 강점은 <strong>캡컷(CapCut)과 프리미어 프로(Premiere Pro)의 양방향 연동</strong>이다. 
              에이전트가 생성한 타임라인 데이터를 캡컷 데스크톱 프로젝트나 프리미어 프로의 XML 시퀀스로 원클릭 임포트할 수 있어, 후반 작업에서 자막 폰트나 색보정(LUT)을 손쉽게 미세 조정할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 영상 외주 시장과 크리에이터 이코노미의 지각변동
            </h3>
            <p>
              그동안 유튜브 롱폼 영상 한 편을 편집하는 데는 편당 수십만 원에서 수백만 원의 외주 비용과 사흘 이상의 시간이 소요되었다. 
              이는 1인 미디어 크리에이터들에게 가장 큰 비용 장벽이었다.
            </p>
            <p>
              OpenMontage는 이 가편집과 컷 구성의 비용을 사실상 '0원'으로 떨어뜨린다. 
              대본만 던져주면 단 5분 만에 완성도 높은 멀티트랙 초안이 조립되어 나오기 때문이다. 
              어도비가 파이어플라이(Firefly)를 통해 클라우드 구독을 강화하려는 전략에 맞서, 로컬과 오픈소스 진영이 완전히 자율화된 비디오 파이프라인을 구축해 낸 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 컷(Cut)의 리듬이야말로 영화의 영혼이다
            </h3>
            <p>
              영화 역사상 가장 위대한 감독 중 한 명인 세르게이 에이젠슈테인은 "영화의 본질은 카메라가 찍은 단일 숏에 있는 것이 아니라, 서로 다른 숏이 충돌하는 몽타주(Montage)의 순간에 있다"고 갈파했다.
            </p>
            <p>
              수많은 AI 모델들이 그저 예쁜 픽셀을 그려내는 데 머물 때, OpenMontage는 서로 다른 클립을 서사적 리듬으로 충돌시키는 <strong>'편집의 혼(Soul)'</strong>을 컴퓨터에게 가르쳤다. 
              인공지능 비디오의 진정한 혁명은 생성의 방아쇠가 아니라, 타임라인을 벼리는 가위의 끝에서 완성되고 있다.
            </p>

            <div class="project-links-bar">
              <a href="https://www.openmontage.video/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>공식 웹사이트 둘러보기</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=openmontage+agentic+video+production" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/calesthio/OpenMontage" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+75.3k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
