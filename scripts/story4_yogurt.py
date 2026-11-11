# -*- coding: utf-8 -*-
# Story 4: FrigadeHQ/yogurt (100% 온디바이스 로컬 AI 회의록)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] FrigadeHQ/yogurt : 100% 온디바이스 로컬 AI 회의록 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_yogurt.jpg" alt="Yogurt Meeting Notes Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔒 100% 온디바이스 프라이빗 회의록</span>
              <span class="aggro-tag">🎙️ 월 30달러 Granola/Otter 완전 대체</span>
              <span class="platform-tag">Show HN Hot & GitHub Trending</span>
              <span class="platform-tag">FrigadeHQ / yogurt</span>
            </div>
            
            <h2 class="article-headline">
              회의실의 빅테크 도청과 유료 구독을 거부한다: 100% 온디바이스 로컬 AI 회의록
            </h2>

            <div class="article-subheadline">
              월 30달러 Granola와 Otter의 기업 기밀 유출 위험을 끝낸 CoreAudio 직결 무손실 전사 및 액션 아이템 추출 오픈소스
            </div>
            <p class="article-snippet">
              이사회 회의실과 1:1 면담에서 상용 AI 회의 요약 봇을 초대하는 순간, 기업의 핵심 영업 비밀과 인사 정보는 제3자 클라우드로 흘러들어갑니다. 매달 직원당 수십 달러를 결제하면서도 기밀 유출 공포에 떨어야 했던 엔터프라이즈 환경에 단비 같은 오픈소스가 등장했습니다. 시스템 오디오 드라이버와 로컬 신경망을 직결해, 단 1바이트의 음성도 외부로 내보내지 않고 실시간 고품질 마크다운 회의록을 생성하는 'Yogurt'가 해커뉴스를 강타했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "이 회의에 AI 봇이 들어와도 됩니까?"
            </h3>
            <p>
              투자 유치 미팅, 신임 임원 면접, 인수합병(M&A) 실사 회의. 
              가장 내밀하고 민감한 대화가 오가는 순간 누군가 "Otter 봇 좀 초대해도 될까요?" 혹은 "Granola 켜고 해도 될까요?"라고 묻는다면 
              참석자들의 표정은 굳어질 수밖에 없다.
            </p>
            <p>
              시중의 상용 AI 미팅 노트 서비스들은 음성 데이터를 자사 클라우드로 전송해 텍스트로 바꾸고 요약한다. 
              편리함의 대가로 지불해야 하는 것은 연간 수백만 원의 구독료뿐만이 아니다. 
              언제 파기될지 모르는 제3자 서버에 회사의 운명이 걸린 음성 원본을 통째로 쥐여주는 치명적인 보안 리스크를 감수해야 했다.
            </p>
            <p>
              오늘, 단 한 조각의 오디오 패킷도 인터넷 망으로 흘려보내지 않는 100% 로컬 프라이빗 오픈소스 회의록 
              <strong>Yogurt</strong>가 공개되며 프라이버시 중심의 테크 씬을 뒤흔들었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: Granola의 독점과 기업 데이터 주권의 충돌
            </h3>
            <p>
              최근 벤처캐피털 업계와 스타트업 씬을 휩쓴 Granola는 미려한 디자인과 훌륭한 요약력으로 큰 인기를 끌었지만, 
              유료 구독 요금(월 $20~30/인당)과 비공개 소스코드라는 클라우드 종속의 굴레를 벗어나지 못했다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신의 가장 은밀한 비즈니스 회의, 급여 협상, 특허 논의가 실리콘밸리 스타트업의 클라우드 데이터베이스에 보관되는 것을 원하십니까? 
                <strong>Yogurt는 순수 오픈소스이며 영원히 무료입니다. 당신의 맥북 M 시리즈 신경망 엔진(NPU) 위에서 100% 오프라인으로 음성을 전사하고, 
                결정 사항(Decisions)과 할 일(Action Items)을 완벽한 마크다운 문서로 내 로컬 디스크에 저장합니다.</strong>"
              </p>
              <small>— FrigadeHQ Yogurt 개발팀 공식 쇼케이스</small>
            </div>

            <p>
              해커뉴스 쇼케이스(Show HN)에서 수많은 CTO와 프라이버시 옹호자들의 찬사를 받은 Yogurt는, 
              회사의 기밀 회의뿐 아니라 병원, 법률 사무소, 공공기관 등 클라우드 녹음이 법적으로 금지된 특수 산업군까지 
              단숨에 사로잡았다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 시스템 오디오 탭과 온디바이스 NPU 전사 엔진
            </h3>
            <p>
              Yogurt는 클라우드 중계 서버를 통째로 덜어내고, 데스크톱 OS의 하드웨어 가속을 극한으로 활용하도록 설계되었다:
            </p>
            <ul>
              <li><strong>Zero-Latency Audio Tap:</strong> Zoom이나 Google Meet 브라우저 세션에 어색한 봇을 초대할 필요 없이, macOS CoreAudio 가상 오디오 디바이스(및 Linux PipeWire)를 직접 탭하여 상대방 스피커 출력과 내 마이크 입력을 무손실 캡처.</li>
              <li><strong>Apple Silicon Neural Engine 가속:</strong> 내장된 `whisper.cpp` 모델이 M1/M2/M3/M4의 NPU 코어를 직접 점유하여, CPU/GPU 점유율을 5% 미만으로 유지하면서 실시간 말소리를 나노초 지연으로 텍스트화.</li>
              <li><strong>구조화된 액션 아이템 추출:</strong> 로컬 Ollama 모델(Llama-3, Qwen)이나 사용자의 개인 API 키(BYOK)를 통해 회의 중 발생한 핵심 아젠다, 합의된 결정 사항, 담당자별 실행 과제를 표준 마크다운 체크리스트로 합성.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Yogurt 100% 온디바이스 로컬 오디오 전사 파이프라인</span>
                <span class="schematic-badge">Air-Gapped Meeting OS</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">System Audio Tap</div>
                  <div class="schematic-desc">
                    CoreAudio / PipeWire 루프백<br>
                    봇 초대 없는 무음 스텔스 캡처<br>
                    스피커(상대방) + 마이크 무손실 혼합
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">On-Device Whisper (NPU)</div>
                  <div class="schematic-desc">
                    whisper.cpp 애플 실리콘 네이티브<br>
                    외부 인터넷 전송 0바이트<br>
                    실시간 화자 분리 & 타임스탬프 색인
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Local Markdown Vault</div>
                  <div class="schematic-desc">
                    결정 사항(Decisions) 자동 추출<br>
                    담당자별 Action Items 체크리스트<br>
                    Obsidian / 로컬 폴더 직접 저장
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Yogurt 공식 웹 데모 및 데스크톱 애플리케이션</span>
              </div>
              <img src="../assets/images/demo_yogurt.png" alt="Yogurt Live Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ yogurt.so 공식 웹사이트 뷰: "Private AI meeting notes. Free and open source." 간결하고 감성적인 타이포그래피와 원클릭 macOS DMG 다운로드, 프라이버시 보증 철학을 담은 공식 런칭 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 엔터프라이즈 컴플라이언스
            </h3>
            <p>
              EU의 GDPR과 미국의 HIPAA, 금융권의 엄격한 데이터 보호 규정(SOC2) 하에서 
              기업들은 회의 음성 데이터를 제3자 SaaS에 위탁하는 행위를 법적으로 금지하거나 극도로 제한해왔다. 
              Granola나 Otter 같은 기업들은 이 규제를 통과하기 위해 값비싼 엔터프라이즈 계약을 강요했지만, 
              Yogurt는 아예 데이터가 물리 디바이스 외부로 나가지 않는 에어갭(Air-Gapped) 구조를 취함으로써 
              복잡한 보안 심의를 단 한 방에 무력화했다.
            </p>
            <p>
              수만 명의 직원을 둔 글로벌 기업 보안 담당자 입장에서, 유료 결제 없이 
              기밀 유출 리스크를 '구조적으로 제로화'할 수 있는 오픈소스 솔루션의 등장은 
              기존 B2B SaaS 시장의 가격 정책을 뒤흔드는 거대한 균열이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 내 말의 주권은 내 컴퓨터에 있다
            </h3>
            <p>
              인공지능의 편리함이 인간의 사생활과 기업의 비밀을 볼모로 잡아야 할 이유는 없다. 
              Yogurt가 증명한 것은, 온디바이스 하드웨어의 눈부신 발전 덕분에 
              이제 우리는 클라우드 빅테크의 도청 없이도 가장 완벽한 인텔리전스를 로컬에서 누릴 수 있다는 사실이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Yogurt+AI+meeting+notes+open+source+review" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://yogurt.so" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> Yogurt 공식 웹사이트 바로가기
              </a>
              <a href="https://github.com/FrigadeHQ/yogurt" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
