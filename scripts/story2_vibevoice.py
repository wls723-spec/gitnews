# -*- coding: utf-8 -*-
# Story 2: microsoft/VibeVoice (HERO 2)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] microsoft/VibeVoice -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_vibevoice.png" alt="microsoft VibeVoice" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="mic" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 기계음의 시대를 끝내는 마이크로소프트의 반격</span>
              <span class="platform-tag">GitHub Trending #2</span>
              <span class="platform-tag">microsoft / VibeVoice</span>
            </div>
            
            <h2 class="article-headline">
              "숨소리와 떨림까지 인간 그대로" — 마이크로소프트의 오픈소스 프론티어 음성 AI VibeVoice
            </h2>

            <div class="article-subheadline">
              빅테크의 독점적 음성 AI 장벽을 허물다… 초저지연 스트리밍 음성 합성(StreamingTTS)과 실시간 턴테이킹, 자연스러운 말 끊김(Interruption)을 오픈 가중치로 전격 공개
            </div>
            <p class="article-snippet">
              OpenAI의 '고급 음성 모드(Advanced Voice Mode)'에 필적하는 감정 표현과 실시간 대화 유연성을 오픈소스로 구현한 마이크로소프트의 VibeVoice. 기존 기계적 TTS의 한계를 뛰어넘은 어쿠스틱 디퓨전 아키텍처를 심층 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 로봇 같던 AI 목소리의 마지막 불쾌한 골짜기
            </h3>
            <p>
              그동안 수많은 오픈소스 텍스트 음성 변환(TTS) 모델이 쏟아져 나왔지만, 사람의 귀는 여전히 그 인공적인 티를 단번에 알아챘다. 
              일정한 억양, 부자연스럽게 잘려 나간 호흡, 그리고 상대방이 말을 가로막았을 때 대처하지 못하는 일방통행식 스트리밍 구조 때문이었다. 
              인간다운 상호작용은 오직 오픈AI나 구글의 비싼 독점 API 클라우드 뒤에 갇혀 있었다.
            </p>
            <p>
              하지만 오늘, 마이크로소프트(Microsoft) 연구팀이 깃허브에 기습 공개한 <strong>microsoft/VibeVoice</strong>는 이 거대한 장벽을 일거에 무너뜨렸다. 
              말하는 도중 섞여 나오는 미세한 숨소리, 웃음기 섞인 목소리, 질문에 고개를 끄덕이며 맞장구치는 감탄사까지 인간 음성의 미묘한 뉘앙스를 완벽하게 살려낸 <strong>프론티어급 음성 파운데이션 모델을 누구나 무료로 다운로드할 수 있는 오픈소스</strong>로 풀어놓은 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 실시간 양방향 듀플렉스 대화의 해법
            </h3>
            <p>
              VibeVoice는 단순한 글자 읽어주기 프로그램이 아니다. 
              초저지연 스트리밍 음성 합성(StreamingTTS)과 차세대 음성 인식(ASR)을 하나의 유기적인 뉴럴 파이프라인으로 통합했다.
            </p>

            <div class="editorial-quote">
              <p>
                "진정한 음성 지능은 '문장을 다 듣고 나서 생각한 뒤 말하는 것'이 아니다. 
                상대방의 음색과 속도에 실시간으로 보조를 맞추고, 중간에 말이 끊기면 즉각 멈추며 유연하게 반응하는 <strong>전이중(Full-duplex) 실시간 어쿠스틱 상호작용</strong>이다."
              </p>
              <small>— Microsoft VibeVoice 연구 백서 요약</small>
            </div>

            <p>
              VibeVoice는 첫 번째 오디오 청크를 생성하는 데 걸리는 첫 토큰 지연 시간(First-chunk Latency)을 수십 밀리초(ms) 수준으로 단축하여, 인간과의 실시간 전화 통화에서도 어색한 침묵이 발생하지 않는다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: 어쿠스틱 디퓨전과 연속형 시맨틱 토크나이저
            </h3>
            <p>
              VibeVoice가 독보적인 자연스러움을 자랑하는 기술적 기둥은 두 가지다:
            </p>
            <ul>
              <li><strong>연속형 시맨틱-어쿠스틱 듀얼 토크나이저:</strong> 이산형 토큰(Discrete Tokens)으로 음성을 쪼갤 때 발생하는 음질 손실과 기계적 거칠기를 극복하기 위해, 연속형 잠재 공간(Continuous Latent Space)에서 억양과 음색 정보를 보존.</li>
              <li><strong>스트리밍 신경망 보코더(Neural Vocoder):</strong> 텍스트 토큰이 입력되는 즉시 뒤이어 올 맥락을 예측하며 파형을 생성하는 스트리밍 디퓨전 백본을 채택하여 버퍼링 없는 무지연 오디오 합성 달성.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> VibeVoice 전이중 스트리밍 오디오 파이프라인
                </span>
                <span class="schematic-badge">FULL-DUPLEX VOICE PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">실시간 텍스트/맥락 스트림 수신</div>
                  <div class="step-tech">Continuous Semantic Encoder</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">감정·호흡 결합 어쿠스틱 합성</div>
                  <div class="step-tech">Latent Diffusion Backbone</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">초저지연 무손실 파형 출력</div>
                  <div class="step-tech">Streaming Neural Vocoder (&lt;50ms)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 파이프라인 흐름:</strong> 문장이 끝날 때까지 기다리지 않고 첫 음절부터 즉각 파형을 합성하여 출력하며, 상대방의 오디오 입력이 들어오면 실시간 인터럽트 게이트를 통해 0.05초 만에 말을 멈추고 경청 모드로 전환합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="globe"></i> 4. 오픈소스 커뮤니티의 폭발적 반응
            </h3>
            <p>
              마이크로소프트는 VibeVoice의 전체 연구 논문(ArXiv), 허깅페이스(Hugging Face) 가중치 체크포인트, 구글 코랩(Google Colab) 원클릭 실행 노트북을 전면 무료로 공개했다. 
              개발자들은 이제 거대 빅테크의 유료 음성 API에 종속되지 않고, 자신의 로컬 GPU 서버에서 완벽한 실시간 AI 비서나 통역 봇을 자체 구축할 수 있게 되었다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> VibeVoice 공식 아키텍처 엠블럼 & 데모
                </span>
                <span class="media-showcase-badge demo">OFFICIAL SHOWCASE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_vibevoice.png" alt="Microsoft VibeVoice Architecture" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 마이크로소프트 VibeVoice 공식 엠블럼:</strong> 프론티어 음성 AI의 오픈소스화를 선언하며 공개된 연구 리포트와 모델 체크포인트.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="heart"></i> 5. 시사점: 온디바이스 음성 에이전트의 대중화
            </h3>
            <p>
              VibeVoice는 음성 AI가 클라우드 독점의 굴레를 벗어나 진정한 오픈 생태계로 진입했음을 알리는 신호탄이다. 
              자연스러운 호흡과 미세한 감정선까지 재현해내는 이 모델은 스마트홈 기기, 로봇 공학, 차량용 인포테인먼트의 음성 인터페이스를 송두리째 바꿀 잠재력을 품고 있다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://microsoft.github.io/VibeVoice" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 프로젝트 페이지
                </a>
                <a href="https://github.com/microsoft/VibeVoice" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
