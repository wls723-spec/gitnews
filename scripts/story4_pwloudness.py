# -*- coding: utf-8 -*-
# Story 4: xoxorwr/pw-loudness-eq (Windows Loudness Equalization Reverse-Engineered for PipeWire)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] xoxorwr/pw-loudness-eq : Windows Audio DSP Port  -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_pwloudness.jpg" alt="pw-loudness-eq Windows Audio DSP Reverse-Engineered for Linux PipeWire Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="volume-2" style="width:12px;height:12px;"></i> LINUX AUDIO RE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🎧 HN 299점 · 168댓글 · WMALFXGFXDSP.dll &amp; AudioEng.dll 바이너리 역공학</span>
              <span class="platform-tag">Hacker News Hot &amp; PipeWire DSP</span>
              <span class="platform-tag">xoxorwr / pw-loudness-eq</span>
            </div>

            <h2 class="article-headline">
              "윈도우의 '음량 평준화' 체크박스 하나 때문에 리눅스를 못 떠났다" — DLL을 통째로 역공학한 'pw-loudness-eq'
            </h2>

            <div class="article-subheadline">
              Microsoft Windows 오디오 스택의 WMALFXGFXDSP.dll과 출력 리미터 AudioEng.dll의 부동소수점 상수 비트 패턴까지 역공학해, 가상 싱크 없이 앱 스트림 단위로 작동하는 순정 Linux PipeWire LADSPA 모듈·GTK3 앱으로 이식 (★160 · C)
            </div>
            <p class="article-snippet">
              밤중에 유튜브나 영화를 틀면 대사는 모기 소리인데 폭발음만 천장을 뚫는 현상—Windows 사용자에게는 소리 설정의 '라우드니스 이퀄라이제이션(Loudness Equalization)' 체크박스 하나로 해결되지만, Linux 데스크톱 이주자들에게는 수년째 풀리지 않던 고질병이었습니다. 오늘 해커뉴스(<strong>299점·댓글 168개</strong>)에서 뜨거운 찬반을 불러일으킨 <strong>xoxorwr/pw-loudness-eq</strong>는 바로 그 Windows 오디오 엔진(<code>WMALFXGFXDSP.dll</code> &amp; <code>AudioEng.dll</code>)을 직접 역공학해, <strong>정확한 16진수 IEEE-754 상수 비트 패턴</strong>까지 PipeWire 1.4+ 네이티브 C 모듈로 재현해 냈습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 체크박스 하나가 갈라놓은 데스크톱의 체감 품질
            </h3>
            <p>
              리눅스 데스크톱 커뮤니티에서 "Windows에서 Linux로 완전히 갈아타지 못하는 사소하지만 치명적인 이유"를 꼽을 때 단골로 올라오는 항목이 있다. 바로 야간 영화 시청이나 게임을 할 때 작은 소리는 키워주고 갑작스러운 굉음은 눌러주는 Windows의 <strong>Loudness Equalization</strong>이다. 리눅스에도 <code>EasyEffects</code>나 범용 다중밴드 컴프레서 플러그인은 많지만, 매번 수십 개 노브를 만져도 Microsoft가 수십 년 전 튜닝해 둔 그 자연스러운 청감 보정이 나오지 않는 데다, 가상 오디오 싱크(Virtual Sink)를 끼우면 앱별 볼륨 제어와 지연시간이 꼬이기 일쑤였다.
            </p>
            <p>
              개발자 <code>xoxorwr</code>는 대충 비슷한 컴프레서를 짜는 대신 정면 돌파를 택했다. Windows 시스템 폴더 안에 잠든 <code>WMALFXGFXDSP.dll</code>(Windows Media Audio APO)과 <code>AudioEng.dll</code> 리미터를 디스어셈블해 그 안의 알고리즘과 매직 넘버들을 끄집어낸 뒤, 순수 C언어 LADSPA 플러그인과 PipeWire 동적 모듈로 빚어낸 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 오디오파일의 분노와 실사용자의 환호가 교차한 168개의 댓글
            </h3>
            <p>
              <code>pw-loudness-eq</code>가 해커뉴스 전면에 오르자 168개의 댓글창은 순식간에 뜨거운 논쟁터가 됐다. 오디오 엔지니어들은 <em>"작곡가가 의도한 다이내믹 레인지를 뭉개버리는 기능을 기본 탑재하지 말라"</em>며 손사래를 쳤지만, 다수의 데스크톱 사용자들은 <em>"믹싱이 엉망인 할리우드 영화와 유튜브 영상에서 가족들을 깨우지 않고 대사를 들을 수 있게 해준 유일한 구원투수"</em>라며 반겼다. 특히 단순 필터가 아니라 <strong>Windows APO의 앱별 스트림 처리(SFX) + 디바이스별 클리핑 방지 리미터</strong> 구조를 PipeWire 네이티브로 고스란히 옮긴 엔지니어링 완성도에 찬사가 쏟아졌다.
            </p>

            <div class="editorial-quote">
              <p>
                "Windows는 Loudness Equalization을 스트림 이펙트(SFX)로 실행한다—믹싱 전 애플리케이션 스트림마다 독립된 인스턴스와 자체 게인을 가진다. <strong>이 모듈은 가상 장치를 만들지 않고 PipeWire 레지스트리에서 앱 재생 스트림을 감시해 정확히 같은 구조를 구현한다.</strong>"
              </p>
              <small>— xoxorwr/pw-loudness-eq <code>module-loudness-eq.c</code> 주석</small>
            </div>

            <p>
              실제로 <code>modules/loudness/src/leq.c</code> 소스 코드를 열어보면 소름이 돋을 만큼 정밀한 재현을 확인할 수 있다. 저자는 Windows DLL의 <code>.rdata</code>와 <code>.data</code> 섹션(<code>0x1801b6620</code> 등)에서 추출한 <strong>25개 청각 임계 대역(Bark-like Bands: 100Hz~24,000Hz) 경계값과 대역별 문턱값(<code>band_thresh</code>)</strong>은 물론, 심지어 원본 DLL 창 함수(<code>lm_init</code>) 안에 미세하게 어긋나 있던 <code>2π</code> 부동소수점 비트(<code>0x401921fb54442d11ULL</code>)까지 그대로 복원해 냈다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 25개 주파수 대역 FFT 심리음향 모델과 PipeWire 동적 그래프 삽입
            </h3>
            <p>
              많은 사람이 Windows의 라우드니스 평준화를 단순한 '2밴드 RMS 컴프레서'로 오해해 왔지만, <code>pw-loudness-eq</code>의 역공학 결과는 훨씬 정교한 3단계 DSP 아키텍처를 보여준다:
            </p>
            <ul>
              <li><strong>심리음향 25대역 라우드니스 추정 (<code>leq.c</code>):</strong> FFT로 스펙트럼을 분석한 뒤 100Hz부터 24,000Hz까지 인간 청각 특성을 반영한 25개 대역의 에너지를 모든 채널에서 합산한다. 각 대역에서 정해진 임계치(<code>band_thresh</code>)를 뺀 뒤, <code>1.72</code> 스케일과 지수 <code>1.6</code> 곡선으로 목표 라우드니스(<code>1300.0f</code>)와의 차이를 계산하고 최대 10배(<code>+20dB</code>)까지 게인을 산출한다.</li>
              <li><strong>릴리즈 타임 제어 &amp; <code>AudioEng.dll</code> 출력 리미터 (<code>modules/limiter/</code>):</strong> 사용자가 GTK3 창이나 <code>pw-metadata</code> CLI로 2(빠름)~7(느림, Windows 기본값 4) 사이의 Release Time을 조절하면 릴리즈 감쇠 스텝(<code>0.1</code> 또는 <code>0.316</code>)이 즉시 반영된다. 이후 최종 재생 장치 앞단에 <code>AudioEng.dll</code>에서 역공학한 출력 리미터를 걸어 부스트로 인한 디지털 클리핑(찌그러짐)을 원천 차단한다.</li>
              <li><strong>가상 장치 없는 PipeWire 레지스트리 후킹 (<code>module-loudness-eq.c</code>):</strong> PipeWire 1.4 이상의 레지스트리에서 <code>media.class = Stream/Output/Audio</code>를 실시간 감시해 Discord 등 예외 앱(<code>disabled-apps</code>)은 건너뛰고 일반 앱 스트림마다 <code>loudness_eq_1ch..8ch</code> LADSPA 노드를 그래프에 직접 연결한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">pw-loudness-eq PipeWire 네이티브 스트림 이펙트 &amp; 리미터 구조</span>
                <span class="schematic-badge">PipeWire ≥ 1.4 · LADSPA · GTK3 UI</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Per-App Stream Hook</div>
                  <div class="schematic-desc">
                    <code>module-loudness-eq.c</code> 레지스트리 감시<br>
                    가상 싱크 없이 앱별 오디오 스트림 직접 연결<br>
                    <code>pw-metadata</code>로 실시간 ON/OFF<br>
                    Discord/DAW 등 <code>disabled-apps</code> 예외 처리
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. 25-Band Psychoacoustic DSP</div>
                  <div class="schematic-desc">
                    <code>WMALFXGFXDSP.dll</code> 역공학(<code>leq.c</code>)<br>
                    100Hz~24kHz 25개 대역 에너지 합산<br>
                    대역별 문턱값 차감 + 지수 1.6 게인 곡선<br>
                    Release Time 2~7단계 실시간 감쇠 조절
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Hardware Limiter Stage</div>
                  <div class="schematic-desc">
                    <code>AudioEng.dll</code> 출력 리미터 이식<br>
                    모든 물리 재생 디바이스 출력단 보호<br>
                    급격한 피크 증폭 시 디지털 클리핑 방지<br>
                    GTK3 데스크톱 설정 UI (<code>pw-loudness-eq</code>)
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">xoxorwr/pw-loudness-eq 저장소 실화면 — GTK3 제어 UI 및 PipeWire CLI 메타데이터 설정</span>
              </div>
              <img src="../assets/images/demo_pwloudness.png" alt="xoxorwr pw-loudness-eq GTK3 Window and PipeWire Configuration" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/xoxorwr/pw-loudness-eq 실화면: 앱별 활성화 토글과 Release Time 슬라이더를 제공하는 GTK3 인터페이스 및 PipeWire 메타데이터 스크립팅 가이드.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적·생태계 쟁점: 독점 OS 바이너리의 '상수 추출'과 데스크톱 이식성
            </h3>
            <p>
              <code>pw-loudness-eq</code>는 기술적 완성도 못지않게 오픈소스 법무와 데스크톱 생태계 관점에서도 흥미로운 지점을 건드린다.
            </p>
            <ul>
              <li><strong>바이너리 역공학의 합법적 경계와 상호운용성:</strong> Microsoft의 저작권 코드나 DLL 바이너리를 재배포하는 대신, 동작 분석을 통해 도출한 수학적 필터 구조와 캘리브레이션 계수만 C 코드로 깨끗하게 새로 구현한 형태다. (참고로 현재 GitHub 저장소에는 별도 <code>LICENSE</code> 파일이 명시되지 않아 배포판 패키지화 전에 라이선스 명시가 필요하다는 지적도 나온다.)</li>
              <li><strong>"왜 PipeWire 코어에 기본 포함되지 않길 바라는가":</strong> 해커뉴스에서는 <em>"훌륭한 작업이지만 음악 감상이나 오디오 작업자를 위해 PipeWire 기본값으로 강제 편입되지는 말아야 한다"</em>는 신중론이 우세했다. 결국 가장 이상적인 형태는 사용자가 원할 때만 선택해 설치하는 독립 모듈(옵트인)이며, 바로 그 지점에서 <code>pw-loudness-eq</code>는 리눅스 데스크톱의 오래된 '체감 품질 격차' 하나를 조용히 메웠다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 리눅스 이주의 마지막 장벽은 거창한 커널이 아니라 25개의 상수였다
            </h3>
            <p>
              운영체제 전쟁의 승패는 종종 거창한 벤치마크가 아니라, 자정 넘어 넷플릭스를 볼 때 볼륨 리모컨에 손이 몇 번 가느냐 같은 사소한 생활감에서 갈린다.
            </p>
            <p>
              <code>WMALFXGFXDSP.dll</code> 속에 수십 년간 갇혀 있던 25개의 주파수 문턱값이 이제 순수 C 코드로 풀려나 PipeWire 그래프 위를 흐른다. 리눅스 오디오가 '전문가의 실험실'을 넘어 '누구나 밤에 편히 쓰는 거실의 스피커'로 내려오는 데 필요했던 마지막 한 조각이 드디어 맞춰졌다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=pw-loudness-eq+PipeWire+Linux+Windows+Loudness+Equalization" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/xoxorwr/pw-loudness-eq" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
