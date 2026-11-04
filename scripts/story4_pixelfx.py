# -*- coding: utf-8 -*-
# Story 4: patch-gg/pixelfx

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] patch-gg/pixelfx : 절차적 픽셀 아트 혁신 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_pixelfx.jpg" alt="PixelFX Procedural Pixel Art VFX" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 100% 코드로 구현된 244종 도트 이펙트와 Claude Code 스킬</span>
              <span class="platform-tag">GitHub Creative</span>
              <span class="platform-tag">patch-gg / pixelfx</span>
            </div>
            
            <h2 class="article-headline">
              "도트 노가다는 끝났다": 코드로 빚는 244종 레트로 픽셀 이펙트와 Claude Code 아티스트 스킬
            </h2>

            <div class="article-subheadline">
              "코드는 찰흙이고, 당신의 눈을 믿으십시오" — 화염구, 마법 폭발, 참격 궤적부터 12단계 타격 액팅(Wind-up &rarr; Recovery)까지 단 한 장의 거대 텍스처 없이 순수 자바스크립트 수식으로 렌더링되는 초경량 픽셀 아트 엔진… 까다로운 장인의 피드백 루프를 모방한 Claude Code 전용 생성기 탑재
            </div>
            <p class="article-snippet">
              생성 AI가 쏟아내는 흐릿하고 일관성 없는 가짜 픽셀 그림에 지친 인디 게임 개발자들을 위한 구원투수. 브라우저에서 즉시 체험 가능한 대화형 갤러리와 모든 게임 엔진용 스프라이트 시트 익스포터 제공.
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
              <i data-lucide="flame"></i> 1. 리드: 흐릿한 AI 생성 그림에 질린 도트 장인들의 반격
            </h3>
            <p>
              최근 2년간 인디 게임 개발자들은 깊은 환멸을 맛보았다. 
              미드저니나 스테이블 디퓨전 같은 거대 비전 AI에 "16비트 픽셀 아트 화염 마법을 그려달라"고 요청하면, 픽셀 격자가 비뚤어지고 가장자리가 뭉개진 '픽셀처럼 보이는 흐릿한 고해상도 그림(Pixel Slop)'만 쏟아졌기 때문이다. 
              결국 개발자들은 다시 수천 개의 점을 마우스로 일일이 찍는 가혹한 수작업 도트 노가다로 돌아가야만 했다.
            </p>
            <p>
              그 좌절의 한복판에서 깃허브에 폭발적인 인기를 끌며 등장한 프로젝트가 <strong>patch-gg/pixelfx</strong>다. 
              공개 직후 2,500개 이상의 스타를 모은 이 프로젝트는 비트맵 이미지를 생성하지 않는다. 
              대신 <strong>수학적 물리 시뮬레이션 코드 자체를 픽셀의 캔버스로 삼았다</strong>.
            </p>
            <p>
              화염, 전격, 차원문, 회오리바람, 슬라임 몬스터 등 244가지에 달하는 시각 이펙트(VFX)가 각각 수십 줄의 순수 경량 코드로 작성되어 있다. 
              더욱 놀라운 것은 캐릭터의 움직임이다. 
              마법사가 지팡이를 들어 올리는 예비 동작(Wind-up), 에너지를 방출하는 순간, 타깃에 적중하여 경직되는 찰나(Hit-stop), 그리고 숨을 고르는 회복(Recovery)까지 <strong>12단계의 액팅(Acting) 생명력</strong>이 온전히 코드로 구현되어 있다.
            </p>

            <div class="editorial-quote">
              "픽셀 아트를 만드는 진짜 비결은 거대한 모델에 프롬프트를 던지는 것이 아닙니다. 
              <strong>코드는 점토(Clay)와 같습니다. 코드로 규칙을 짜고, 브라우저에서 렌더링된 결과를 직접 눈으로 확인한 뒤, 까다로운 아티스트처럼 한 픽셀씩 다듬는 것입니다.</strong> 
              pixelfx의 Claude Code 스킬은 바로 그 장인의 시각적 피드백 루프를 자동화합니다."
              <span class="quote-author">— Sprite Fusion 창시자 휴고 듀프레즈(Hugo Duprez) 철학 인용 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 무거운 에셋 번들에서 '결정론적 절차적 코드'로의 전환
            </h3>
            <p>
              현대 2D 게임 개발의 가장 큰 골칫거리는 수백 메가바이트(MB)에 달하는 스프라이트 시트(Sprite Sheet) 텍스처 메모리다. 
              모바일이나 웹 브라우저 게임에서는 에셋 다운로드 용량이 늘어날 때마다 유저 이탈률이 급증한다.
            </p>
            <p>
              pixelfx는 거시적 게임 개발 패러다임을 혁신한다:
            </p>
            <ul>
              <li><strong>극도의 경량성:</strong> 수십 메가바이트짜리 PNG 스프라이트 시트 대신 단 몇 킬로바이트(KB)의 자바스크립트 수식으로 60fps 결정론적 애니메이션을 브라우저 캔버스 위에 실시간으로 그려낸다.</li>
              <li><strong>무한한 자유도의 실시간 리컬러링:</strong> 이미 구워진 픽셀 이미지가 아니기 때문에, 팔레트 배열 하나만 바꾸면 동일한 화염 이펙트를 '지옥불 보라색', '얼음 불꽃 청록색', '독성 에메랄드'로 즉각 변환할 수 있다.</li>
              <li><strong>게임 엔진 중립성:</strong> 브라우저에서 완벽히 튜닝된 이펙트를 클릭 한 번으로 유니티(Unity), 고도(Godot), 언리얼(Unreal)용 무손실 스프라이트 시트나 GIF로 내보낼 수 있다.</li>
            </ul>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> PixelFX: 절차적 물리 연산에서 Claude Code 생성 루프까지의 파이프라인
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">단계 1: 물리 코어 연산</span>
                  <strong>Core Sim (sim.js)</strong>
                  <div class="schematic-desc">
                    격자 좌표계 내 중력, 항력, 수명, 디졸브 셰이더 물리 수식 계산. 서브픽셀 보간 없는 정수 격자 스냅 강제
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 2: 12단계 타격 액팅</span>
                  <strong>Motion & Acting Chain</strong>
                  <div class="schematic-desc">
                    Wind-up &rarr; Release &rarr; Contact Freeze &rarr; Impact Dissipate &rarr; Recovery로 이어지는 격투 게임 타격감 수식화
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 3: 팔레트 동적 사상</span>
                  <strong>Color Cycling Logic</strong>
                  <div class="schematic-desc">
                    16색 레트로 아케이드 팔레트 동적 인덱싱. 명도 그라디언트를 보존하며 실시간 속성(화염/빙결/전격) 색상 스왑
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 4: AI 에이전트 스킬</span>
                  <strong>Claude Code Feedback Loop</strong>
                  <div class="schematic-desc">
                    드래프트 코드 작성 &rarr; 헤드리스 브라우저 캡처 &rarr; 시각적 오차 검증 &rarr; 리파인 반복으로 아티스트급 신규 VFX 자율 산출
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: sim.js 물리 코어와 Claude Code 아티스트 스킬
            </h3>
            <p>
              pixelfx의 심장부는 <code>src/core/sim.js</code>에 위치한 초경량 파티클 엔진이다. 
              일반적인 파티클 시스템이 부동소수점 좌표를 사용하여 픽셀 경계가 흐려지는 반면, 이 엔진은 철저하게 <strong>정수 격자(Integer Grid)에 스냅</strong>되도록 설계되었다. 
              입자의 탄도 궤적과 속도 벡터가 계산된 후에도 최종 렌더링 단계에서는 레트로 게임 콘솔의 하드웨어 레지스터처럼 엄격한 픽셀 단위로 양자화(Quantization)된다.
            </p>
            <p>
              하지만 이 프로젝트의 진정한 킬러 피처는 저장소에 함께 내장된 <strong>Claude Code 전용 스킬(Skill)</strong>이다. 
              사용자가 Claude Code 터미널에서 "다크 소울 스타일의 번개 패링 이펙트를 만들어줘"라고 요청하면, 에이전트는 기존 244개 이펙트의 코드 패턴을 레퍼런스로 학습하여 초안 코드를 작성한다. 
              그런 다음 로컬 브라우저에서 이를 실제로 재생하고, 시각적 불균형이나 픽셀 뭉침을 스스로 감지하여 코드를 수정하는 'Draft &rarr; Render &rarr; Look &rarr; Refine' 루프를 완결한다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_pixelfx.jpg" alt="PixelFX Interactive 244 VFX Gallery and Claude Code Generator" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="monitor"></i> <strong>[실구동 갤러리 캡처]</strong> GitHub Pages(patch-gg.github.io/pixelfx)에 호스팅된 실제 인터랙티브 갤러리 화면. 244가지의 파티클 시뮬레이션이 60fps로 실시간 구동되고 있으며, 우측 제어판을 통해 재생 속도, 컬러 팔레트 반전, 애니메이션 프레임 스텝, 스프라이트 시트 다운로드를 즉시 조작할 수 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 인디 생태계: 에셋 스토어의 파편화를 끝내는 FOSS
            </h3>
            <p>
              인디 게임 스튜디오들이 유니티 에셋 스토어나 언리얼 마켓플레이스에서 이펙트 팩을 구매할 때 겪는 가장 큰 문제는 '아트 스타일의 불일치'다. 
              A 패키지와 B 패키지의 픽셀 크기, 팔레트 색온도, 프레임 레이트가 제각각이라 게임에 섞어 넣으면 조잡한 누더기가 되기 십상이었다.
            </p>
            <p>
              pixelfx의 MIT 오픈소스 배포는 게임 산업에 거대한 기여를 한다:
            </p>
            <ul>
              <li><strong>완벽한 스타일 통일성:</strong> 모든 이펙트가 동일한 <code>sim.js</code> 물리 법칙과 16색 팔레트 규격을 공유하므로, 어떤 이펙트를 조합해도 게임 전체의 비주얼 톤앤매너가 완벽히 유지된다.</li>
              <li><strong>무료 상업적 이용:</strong> 값비싼 라이선스 비용이나 로열티 없이 상용 스팀 게임이나 모바일 앱에 무제한 임베드할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 알고리즘으로 되살아난 클래식의 영혼
            </h3>
            <p>
              1990년대 패미컴과 네오지오의 도트 장인들이 브라운관 TV 앞에서 픽셀 하나를 두고 며칠 밤을 지새우며 추구했던 것은 단순한 해상도가 아니라 '살아 움직이는 물리적 감각'이었다.
            </p>
            <p>
              pixelfx는 거대 인공지능 시대에 우리가 잃어버렸던 그 장인 정신을, 코드를 통한 절차적 제어와 에이전트의 시각적 피드백 루프로 현대에 다시 부활시켰다. 
              기술이 진정으로 창의성을 돕는다는 것의 의미를 이 244개의 작은 도트들이 시원하게 증명하고 있다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 (독립 라이브 웹 데모 포함) -->
          <div class="article-links-bar">
            <a href="https://patch-gg.github.io/pixelfx/" target="_blank" rel="noopener noreferrer" class="project-link demo">
              <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 244종 픽셀 VFX 웹 갤러리 바로 체험
            </a>
            <a href="https://www.youtube.com/results?search_query=pixelfx+pixel+art+vfx+claude+code" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/patch-gg/pixelfx" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
