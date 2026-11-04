# -*- coding: utf-8 -*-
# 9 GitHub Minor Radar Items for 2026-10-28

GH_MINORS = """
      <!-- [GH 0~10h] Item 1: vaishantsah/watson-AI-osint-all-in-one -->
      <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 192개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.1시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 37.9 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;계정도 추적도 없는 완전 무료 인텔리전스&quot; : 3,100개 웹사이트 교차 OSINT 검색기</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">vaishantsah/watson-AI-osint-all-in-one — 닉네임·이메일·전화번호로 디지털 발자국을 즉시 탐색하는 윈도우용 오픈소스 도구</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">개인정보 추적 없는 로컬 OSINT 수사관: Watson</h3>
          <div class="minor-detail-subheadline">전 세계 3,100개 이상의 공개 웹사이트와 소셜 플랫폼을 비동기로 스캔하여 디지털 풋프린트를 시각화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 상용 OSINT 서비스들이 고액의 구독료를 요구하고 검색자 본인의 신원 정보를 역추적하는 문제가 만연했습니다. Watson은 단 하나의 회원가입도 요구하지 않고 외부 서버 로깅 없이 로컬에서만 3,100개 서비스의 공개 엔드포인트를 병렬 프로빙하는 순수 오픈소스로 공개되어 큰 반향을 일으켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Query Input (Username/Email) &rarr; Async Probing Engine (3,100+ Endpoints) &rarr; HTTP Status & Response Fingerprinting &rarr; Local Correlation Graph
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                윈도우 네이티브 비동기 I/O로 설계되어 1분 이내에 수천 개 사이트의 계정 등록 여부와 프로필 사진, 최종 활동 타임스탬프를 로컬 SQLite에 정형 리포트로 저장합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/vaishantsah/watson-AI-osint-all-in-one" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 2: ChannelCooperStart/capri-ai -->
      <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 169개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.2시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.4 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;사이버펑크 감성으로 OS를 지휘한다&quot; : 엣지러너 스타일 데스크톱 자율 AI 에이전트</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ChannelCooperStart/capri-ai — Claude Code, Codex, Antigravity와 연동되는 네온 미학 데스크톱 관제탑</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">네온 인터페이스 위에서 춤추는 자율 OS 비서: Capri</h3>
          <div class="minor-detail-subheadline">사이버펑크 엣지러너에서 영감을 받은 레트로-퓨처 HUD와 백그라운드 코딩 에이전트의 결합</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                CLI 환경에 갇혀 있던 코딩 에이전트들의 작업 현황을 시각화하려는 시도가 이어지는 가운데, Capri는 레트로 사이버펑크 애니메이션 HUD 인터페이스를 채택하여 시각적 몰입감과 OS 실시간 제어(파일 I/O, 브라우저 탭 핸들링, 프로세스 킬)를 동시에 제공해 인기를 끌고 있습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Neon HUD Interface &rarr; Agent IPC Bridge (Claude/Codex/Antigravity) &rarr; OS Context Monitor &rarr; Visual Action Feedback
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Tauri 기반 초경량 데스크톱 앱으로 메모리 점유율을 40MB 이하로 유지하면서 로컬 프로세스와 소켓 통신을 통해 에이전트의 상태를 실시간 HUD 애니메이션으로 브로드캐스팅합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/ChannelCooperStart/capri-ai" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 0~10h] Item 3: oxnw/ai-phone -->
      <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 0~10h</span>
              <span class="minor-metric">⭐ 52개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.9시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;맥북 한 대로 전화 교환국을 차린다&quot; : 애플 실리콘 온디바이스 SIP 전화 데몬</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">oxnw/ai-phone — 외부 클라우드 통신 없는 완전 로컬 음성인식(STT) 및 LLM 기반 통화 자율 응대 엔진</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">데이터 유출 없는 프라이빗 전화 상담원: ai-phone</h3>
          <div class="minor-detail-subheadline">SIP 프로토콜 음성 패킷을 Mac의 NPU에서 실시간 Whisper로 디코딩하고 로컬 Llama로 대답하는 온디바이스 데몬</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기업들이 AI 고객센터를 구축할 때 가장 두려워하는 것은 통화 음성과 개인정보가 오픈AI 등 미국 클라우드로 유출되는 리스크였습니다. ai-phone은 표준 SIP VoIP 망과 직접 연결되어 애플 실리콘 Mac 상에서 100% 오프라인으로 수신 전화를 받고 대화를 나눕니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> VoIP/SIP Inbound Call &rarr; RTP Audio Stream &rarr; Local Whisper STT (MLX) &rarr; Local SLM Inference &rarr; Piper TTS &rarr; RTP Return
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                MLX 프레임워크를 기반으로 음성 입력부터 응답 오디오 합성까지 350ms 미만의 지연시간을 달성하여 인간 상담원과 통화하듯 자연스러운 실시간 턴테이킹(Turn-taking)을 구현했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/oxnw/ai-phone" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 4: anhao/ai-pose-gallery-zh -->
      <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 810개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.8시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 48.2 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI 작화와 3D 모델링의 완벽한 뼈대&quot; : 1,439세트 인체 포즈 무의존성 정적 갤러리</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">anhao/ai-pose-gallery-zh — 2,878장의 고해상도 인체 포즈와 오픈포즈(OpenPose) 키포인트 정적 뷰어</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">설치 없이 브라우저로 여는 오픈포즈 레퍼런스 사전: ai-pose-gallery</h3>
          <div class="minor-detail-subheadline">복잡한 Node.js 백엔드 없이 정적 파일만으로 구동되는 방대한 애니메이션·일러스트레이션 포즈 카탈로그</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                Stable Diffusion이나 ControlNet을 사용할 때 적절한 인체 포즈 스켈레톤을 찾는 작업은 막대한 시간이 소요되었습니다. 본 프로젝트는 1,439개 카테고리의 실제 모델 포즈와 골격 추출 이미지를 100% 무의존성 정적 웹페이지로 패키징하여 디자이너들의 작업 속도를 극대화했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> 1,439 Pose Categories &rarr; Dual View (Real Photo + OpenPose Bones) &rarr; Zero-Dependency Static DOM &rarr; 1-Click JSON/PNG Export
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                외부 CDN 의존성을 완전히 제거하여 인터넷이 연결되지 않은 로컬 오프라인 작업실에서도 즉시 열람 및 키포인트 JSON 추출이 가능합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/anhao/ai-pose-gallery-zh" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 5: krushant1122/MetalNX -->
      <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 51개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.3시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.8 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스위치 게임을 Mac에서 네이티브로 돌린다&quot; : 애플 실리콘 Metal 그래픽스 포팅 스튜디오</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">krushant1122/MetalNX — M1/M2/M3/M4 그래픽 파이프라인 튜너 및 NVN-to-Metal 셰이더 트랜스파일러</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">하드웨어 병목을 허무는 원클릭 Metal 변환기: MetalNX</h3>
          <div class="minor-detail-subheadline">닌텐도 스위치 독점 그래픽스 API를 애플 실리콘 MSL로 1:1 하드웨어 가속 매핑</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                ARM64 기반의 공통점에도 불구하고 그래픽스 API의 차이(NVN vs Metal)로 인해 Mac에서 스위치 게임 구동 시 셰이더 컴파일 끊김(Stuttering)이 심했습니다. MetalNX는 셰이더 바이트코드를 사전에 Metal Shading Language로 정적 트랜스파일하여 끊김 없는 60fps 렌더링을 구현했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> NVN Shader Bytecode &rarr; Static IR Analysis &rarr; MSL (Metal Shading Language) Transpiler &rarr; Apple GPU Pipeline Cache
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                Apple Silicon의 통합 메모리(UMA) 구조를 100% 활용하여 CPU-GPU 간 제로 카피 텍스처 스트리밍을 구현, 배터리 소모량을 기존 대비 45% 절감했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/krushant1122/MetalNX" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 10~20h] Item 6: OpenBMB/MiniCPM-OCR -->
      <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 10~20h</span>
              <span class="minor-metric">⭐ 49개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 15.9시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.1 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스스로 오타를 의심하고 바로잡는 AI OCR&quot; : 초정밀 자가 오류 검증 문서 파서</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">OpenBMB/MiniCPM-OCR — 복잡한 다단 문서, 정밀 표, 과학 수식을 온디바이스에서 무결점 마크다운으로 변환</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">문서 파싱의 신뢰성 혁명: MiniCPM-OCR</h3>
          <div class="minor-detail-subheadline">추출된 텍스트와 좌표의 일관성을 비전 모델이 자가 평가(Correctness Assessment)하는 2단계 아키텍처</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                RAG 파이프라인의 가장 큰 실패 원인은 PDF 파싱 단계의 표 뭉개짐과 수식 왜곡이었습니다. OpenBMB는 가벼운 MiniCPM 비전 백본 위에 '정확도 판정 헤드(Assessment Head)'를 얹어, 불확실한 텍스트 영역을 스스로 재스캔하는 고신뢰성 OCR을 공개했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> High-Res Document Image &rarr; Layout Segmentation &rarr; Token Generation &rarr; Self-Correctness Assessment &rarr; Structured Markdown
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단 2.4B 파라미터의 초소형 모델로 독점 상용 OCR 엔진 대비 과학 수식 및 다단 표 인식 정확도에서 98.4%의 SOTA 성능을 기록했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/OpenBMB/MiniCPM-OCR" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 7: patch-gg/anymove -->
      <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 231개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.2시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.9 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;영상 속 모든 생명체의 뼈대를 캔다&quot; : DINOv2 기반 임의 생명체 3D 모션 캡처</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">patch-gg/anymove — 2시점 영상 한 프레임에서 인간·동물·괴수의 관절을 자동 추정하여 3D GLB로 즉시 리깅</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">센서 장비 없는 애니메이션 스튜디오: anymove</h3>
          <div class="minor-detail-subheadline">메타의 DINOv2 비전 특징 맵을 활용해 임의 형태의 생명체 관절을 피팅하고 3D 스켈레톤 추출</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 모션 캡처는 사전에 정의된 '인간 24개 관절'에만 작동했습니다. anymove는 말, 호랑이, 상상의 드래곤까지 영상 속 움직이는 모든 유기체의 관절 자유도를 비지도 방식으로 감지하여 3D 아티스트의 수작업 리깅 공수를 90% 이상 단축시켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Dual-Camera AI Video &rarr; DINOv2 Feature Correspondence &rarr; Dynamic Skeleton Solver &rarr; Rigged GLB 3D Asset
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                블렌더(Blender) 및 언리얼 엔진 5(UE5) 표준 포맷인 GLB로 직접 내보내기를 지원하여 인디 게임 개발자들의 3D 캐릭터 애니메이션 파이프라인을 완전히 민주화했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/patch-gg/anymove" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 8: rudderlabs/devbox -->
      <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 114개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.9시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;클라우드 속 에이전트 전용 무균실&quot; : 작업당 1개 샌드박스 격리 엔지니어링 하네스</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">rudderlabs/devbox — 시크릿 키 유출 없는 안전한 인프라 내에서 자율 소프트웨어 에이전트를 가동하는 오픈소스 플랫폼</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">기업용 자율 코딩의 방화벽: devbox</h3>
          <div class="minor-detail-subheadline">태스크마다 독립된 일회용(Ephemeral) 클라우드 컨테이너를 생성하여 소스코드 탈취와 사이드 이펙트를 원천 봉쇄</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                개발자 로컬 머신에서 에이전트에게 셸 권한을 주는 것에 대한 기업 보안팀의 거부감이 극에 달했습니다. RudderLabs의 devbox는 사내 프라이빗 클라우드 안에 태스크별 마이크로 샌드박스를 띄워, 에이전트가 아무리 파괴적인 명령을 실행해도 운영 환경에 영향을 미치지 못하도록 설계되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Task Dispatcher &rarr; Micro-VM/Container Provisioning &rarr; Synthetic Secret Injection &rarr; Isolated Test Run &rarr; Clean Diff Extract
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                실제 프로덕션 데이터베이스 비밀번호 대신 자동 생성된 가상 모의 시크릿(Mock Secrets)만을 주입하여 공급망 공격이나 에이전트 환각으로 인한 데이터 유출 가능성을 제로로 만들었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/rudderlabs/devbox" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>

      <!-- [GH 20~30h] Item 9: giantbitmonitor/NextFilee -->
      <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-gh">GH 20~30h</span>
              <span class="minor-metric">⭐ 118개</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.3시간 전 생성</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.0 스타/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;내 파일은 단 1바이트도 서버로 나가지 않는다&quot; : 100% 완전 오프라인 드래그 앤 드롭 파일 변환기</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">giantbitmonitor/NextFilee — WebAssembly 기반 브라우저 메모리 로컬 고속 미디어·문서 트랜스코딩</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">웹 변환기 광고와 데이터 유출의 종말: NextFilee</h3>
          <div class="minor-detail-subheadline">FFmpeg WASM과 libvips를 브라우저 내부에 이식하여 네트워크 통신 없이 파일 변환 완결</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 온라인 파일 변환 사이트(CloudConvert 등)는 악성 광고와 대기열, 그리고 민감한 기업 문서 유출 위험이 있었습니다. NextFilee는 파일을 드래그하는 순간 브라우저 탭 자체 메모리에서 WebAssembly로 직접 연산하여 기밀 문서 변환의 표준으로 떠올랐습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[아키텍처 파이프라인]</strong> Drag & Drop File &rarr; WebWorker In-Memory Allocation &rarr; FFmpeg/WASM Transcoder &rarr; Instant Local Blob Download
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                서버 네트워크 업로드 지연이 완전히 사라져 수백 메가바이트의 대용량 비디오나 고화질 이미지 배치 변환 시 기가비트급 속도를 체감할 수 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/giantbitmonitor/NextFilee" target="_blank" class="project-link github"><i data-lucide="github"></i> GitHub 저장소</a>
          </div>
        </div>
      </div>
"""

print("minors_gh_oct28 loaded successfully.")
