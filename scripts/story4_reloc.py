# -*- coding: utf-8 -*-
# Story 4: Reukix/Reloc (iOS Accessory-Level Location Simulator over iAP2 / MFi-v3 / NMEA)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] Reukix/Reloc : iOS Hardware GPS Protocol Sim     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_reloc.jpg" alt="Reloc iOS Accessory-Level GPS Simulator via iAP2 and MFi-v3 Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="navigation" style="width:12px;height:12px;"></i> PROTOCOL REVERSE ENGINEERING</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">📍 29시간 만에 ★742 폭주 · 탈옥·PC 없이 iPhone 외장 GPS 하드웨어 위장</span>
              <span class="platform-tag">GitHub New Rocket &amp; Swift/Rust</span>
              <span class="platform-tag">Reukix / Reloc</span>
            </div>

            <h2 class="article-headline">
              "탈옥도, 맥북도 필요 없다" — 아이폰 본체만으로 애플 CarKit·MFi-v3 외장 GPS를 흉내 낸 'Reloc'
            </h2>

            <div class="article-subheadline">
              소프트웨어 위치 조작 플래그(isSimulatedBySoftware)에 걸리는 기존 스푸퍼를 넘어, 로컬 루프백(10.7.0.1)과 Rust FFI로 iAP2·MFi-v3 인증 및 NMEA-0183 위성 패킷을 직접 꽂아 iOS가 진짜 CarPlay 외장 GPS로 인식하게 만든 역공학 앱 (★742 · AGPL-3.0)
            </div>
            <p class="article-snippet">
              공개 29시간 만에 ★742를 돌파하며 GitHub 급상승 차트를 강타한 <strong>Reukix/Reloc</strong>은 모바일 개발자들과 프로토콜 해커들을 단숨에 매료시켰습니다. 일반 개발자 모드 위치 시뮬레이터가 <code>isSimulatedBySoftware = true</code>로 탐지되는 한계를 깨고, 아이폰 내부 루프백(<code>10.7.0.1</code>)을 통해 시스템의 <code>com.apple.carkit.service</code>에 직접 말을 걸어 <strong>iAP2 링크 동기화, MFi-v3 인증, NMEA-0183(<code>$GPGGA</code>/<code>$GPRMC</code>) 스트리밍</strong>을 수행합니다. iOS 27+에서는 화면 속 화면(PiP) 플로팅 창으로 6자리 페어링 코드를 띄워 PC 연결조차 필요 없는 완전 독립 실행을 구현했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 소프트웨어 가짜 좌표를 거절하는 iOS의 방벽을 우회하다
            </h3>
            <p>
              iOS 생태계에서 앱의 위치 기반 기능을 테스트하거나 지역별 지도 동작을 검증하려는 개발자들에게 Apple의 보안 장벽은 악명이 높다. iOS 15 이후 Apple은 <code>CLLocationSourceInformation</code> API를 도입해 모든 위치 객체에 두 개의 꼬리표를 붙이기 시작했다: 소프트웨어로 주입됐는지를 알리는 <code>isSimulatedBySoftware</code>와, MFi 인증을 받은 외부 자동차·항공 GPS 액세서리에서 온 신호인지를 뜻하는 <code>isProducedByAccessory</code>다.
            </p>
            <p>
              Xcode나 PC용 동글을 매번 꽂지 않고 아이폰 자체에서 위치를 시뮬레이션하려던 수많은 시도는 이 검증 앞에서 번번이 막혔다. 탈옥 없이는 커널이나 <code>locationd</code> 데몬을 건드릴 수 없고, 일반 개발자 API로 주입한 좌표는 즉시 '소프트웨어 가짜 신호'로 낙인이 찍혔다. 그런데 2026년 11월 25일 등장한 <strong><code>Reukix/Reloc</code></strong>은 탈옥도 상용 동글도 없이, 아이폰 안에서 돌아가는 앱 하나만으로 iOS 시스템이 스스로 <strong>"지금 차량용 MFi 외장 GPS 안테나가 연결되었다"</strong>고 믿게 만드는 기발한 로컬 프로토콜 브리지를 공개했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 하드웨어 동글의 시대를 끝낸 Swift × ObjC × Rust FFI 루프백 설계
            </h3>
            <p>
              <code>Reloc</code>이 29시간 만에 ★742와 포크 133개를 쓸어 담은 비결은 단순한 우회 트릭이 아니라 <strong>애플의 공식 외장 액세서리 프로토콜 스택(Remote Pairing + Lockdown + iAP2 + NMEA)을 순수 사용자 공간(User-space)에서 정면 구현한 기술적 완성도</strong>에 있다. 물리적인 USB 케이블이나 블루투스 차량용 헤드유닛 대신 외부 프록시가 제공하는 로컬 루프백 IP(<code>10.7.0.1</code>)를 타고 자신의 iOS 기기 내부 서비스로 재진입하는 구조 덕분에, 개발자는 전철 안에서든 출장 중이든 MacBook 없이 iPhone 단말 하나로 <code>isProducedByAccessory = true</code> 상태를 재현하며 지오펜싱·내비게이션·좌표 보정 앱을 디버깅할 수 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "로컬 루프백(<code>10.7.0.1</code>)으로 <code>com.apple.carkit.service</code>에 접속해 Remote Pairing, iAP2 동기화, MFi-v3 인증 및 NMEA-0183 스트리밍을 완료한다. <strong>시스템은 이를 표준 외장 GPS 액세서리로 인식하고 <code>isProducedByAccessory = true</code>를 반환한다.</strong>"
              </p>
              <small>— Reukix/Reloc 아키텍처 명세 및 실측 패널 스펙</small>
            </div>

            <p>
              또한 중국 본토 등지에서 Apple <code>MapKit</code>이 자동으로 고덕지도(AMap)와 GCJ-02 암호화 좌표계로 전환되는 문제까지 해결하기 위해, <strong>WGS-84 ↔ GCJ-02 자동 양방향 보정</strong>은 물론 Esri 글로벌 스트리트·OpenStreetMap·위성 타일을 <code>MKMapView</code> 없이 순수 네이티브 타일 렌더러로 구현했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: <code>com.apple.carkit.service</code> 핸드셰이크와 PiP 자가 페어링
            </h3>
            <p>
              <code>Reloc</code> 저장소 내부(<code>Reloc/</code> Swift·ObjC 레이어 및 <code>Rust/</code> 브리지 <code>RelocDeviceBridge.xcframework</code>)를 해부하면, iOS가 외장 GPS를 수용하게 만드는 정밀한 4단계 시퀀스가 드러난다:
            </p>
            <ul>
              <li><strong>1) Remote Pairing / Lockdown &amp; iOS 27+ PiP 무PC 페어링:</strong> iOS 17~26.x에서는 최초 1회 PC에서 <code>pymobiledevice3</code>나 <code>idevice_pair</code>로 페어링 파일(<code>.mobiledevicepairing</code> / <code>.rppairing</code>)을 추출해 가져오면 이후 완전히 독립 실행된다. 한술 더 떠 iOS 27.0+에서는 <code>_remotepairing-pairable-host._tcp.</code>를 앱 스스로 광고하고, <strong>화면 속 화면(PiP) 플로팅 창</strong>에 6자리 페어링 코드를 실시간 띄워 사용자가 설정 → 개발자 모드 화면을 오가지 않고도 아이폰 단독으로 페어링을 마친다.</li>
              <li><strong>2) <code>10.7.0.1</code> 루프백 → <code>com.apple.carkit.service</code> &amp; MFi-v3:</strong> Rust FFI 브리지가 로컬 루프백을 거쳐 CarKit 데몬과 세션을 협상한다. iAP2(iPod Accessory Protocol 2) 링크 동기화 후 로컬에 준비한 합법적 MFi-v3 자격증명(<code>certificate.p7b</code>, <code>identity.pk8</code>)으로 챌린지-응답을 통과한 뒤, <code>0xFFFA</code> 위치 정보 컴포넌트 구독을 트리거한다.</li>
              <li><strong>3) NMEA-0183 고속 버스트 &amp; <code>RST</code> 실측 GPS 복원:</strong> <code>$GPGGA</code>와 <code>$GPRMC</code> 문장을 스트리밍하며 옵션으로 ±0.6m의 자연스러운 미세 드리프트를 섞어 실내 Wi-Fi/GNSS 캐시를 밀어낸다. 중지 시에는 무효 패킷(<code>quality=0 / V</code>)과 iAP2 <code>RST</code> 리셋 패킷을 전송해 실제 기기 GPS가 즉시 되살아나도록 설계했다. (내비게이션 백그라운드 유지 + 무음 초저주파 오디오 이중 보활 포함)</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Reloc Swift·Rust FFI 기반 iOS CarKit 외장 GPS 에뮬레이션 파이프라인</span>
                <span class="schematic-badge">iOS 17~27+ · Swift/ObjC/Rust · AGPL-3.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Pairing &amp; Tile Engine</div>
                  <div class="schematic-desc">
                    iOS 27+: <code>_remotepairing-pairable-host._tcp.</code> + PiP<br>
                    iOS 17~26: <code>.rppairing</code> / <code>.mobiledevicepairing</code><br>
                    MapKit + OSM/Esri 순수 WGS-84 타일 맵<br>
                    ±0.6m 미세 드리프트 &amp; <code>CoreLocation</code> 실측 패널
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Rust FFI &amp; iAP2 / MFi-v3</div>
                  <div class="schematic-desc">
                    <code>RelocDeviceBridge.xcframework</code> (Rust)<br>
                    외부 프록시 루프백(<code>10.7.0.1</code>) 경유<br>
                    <code>com.apple.carkit.service</code> Lockdown 협상<br>
                    iAP2 링크 동기화 + MFi-v3 서명 인증
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. NMEA Stream &amp; CoreLocation</div>
                  <div class="schematic-desc">
                    <code>0xFFFA</code> 펄스 구독 &amp; 초기 고속 버스트<br>
                    <code>$GPGGA</code> / <code>$GPRMC</code> NMEA-0183 실시간 주입<br>
                    시스템 판정: <code>isProducedByAccessory = true</code><br>
                    정지 시 <code>quality=0</code> + iAP2 <code>RST</code>로 실 GPS 복귀
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Reukix/Reloc 저장소 실화면 — Swift/Rust FFI 스택 및 iOS 버전별 무PC 페어링 지원 매트릭스</span>
              </div>
              <img src="../assets/images/demo_reloc.png" alt="Reukix Reloc GitHub Repository Architecture and Compatibility" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/Reukix/Reloc 실화면: 로컬 루프백(10.7.0.1) 기반 iAP2/MFi-v3/NMEA 주입 구조와 iOS 17~27+ 호환성 및 XcodeGen 빌드 가이드.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 보안·플랫폼 쟁점: "액세서리 신뢰 모델의 균열과 AGPL-3.0 방어선"
            </h3>
            <p>
              <code>Reloc</code>은 Apple 플랫폼 보안 설계에서 오래된 맹점을 정확히 찌른다. iOS는 CarPlay와 iPadOS의 차이를 이용해 <code>com.apple.carkit.service</code>가 오직 iPhone에만 존재하므로 iPad에서는 작동하지 않지만, 반대로 iPhone에서는 원격 페어링 데몬이 로컬 루프백 인터페이스를 통해 노출되는 순간 물리적 외장 하드웨어와 소프트웨어 루프백을 구분하기 어려워진다.
            </p>
            <ul>
              <li><strong>MFi 자격증명과 합법적 연구 경계:</strong> 저장소 자체는 어떠한 MFi 개인키나 인증서(<code>certificate.p7b</code>, <code>identity.pk8</code>)도 포함하지 않으며, 사용자가 합법적으로 보유한 연구/개발용 자격증명을 로컬에 배치해 빌드하도록 설계해 저작권·DMCA 분쟁 소지를 차단했다. 또한 라이선스를 <strong>AGPL-3.0-only</strong>로 못 박아 상용 위치 스푸핑 서비스들이 코드를 훔쳐 폐쇄형 유료 앱으로 파는 행위를 원천 봉쇄했다.</li>
              <li><strong>안티치트·모빌리티 앱의 과제:</strong> 이제 단순히 <code>isProducedByAccessory</code> 플래그 하나만 믿고 "외장 하드웨어 GPS이니 무조건 신뢰한다"고 가정하던 위치 검증 로직은 재설계가 불가피해졌다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 하드웨어 동글을 프로토콜 몇 줄로 접어버린 우아한 역공학
            </h3>
            <p>
              수만 원짜리 MFi 외장 GPS 수신기 대신, <code>10.7.0.1</code>이라는 조용한 루프백 주소와 Swift·Rust FFI 코드가 아이폰의 위성 수신 감각을 통째로 지휘한다.
            </p>
            <p>
              폐쇄형 OS가 아무리 두꺼운 샌드박스 벽을 둘러쳐도, 시스템이 외부 하드웨어와 대화하기 위해 열어둔 표준 프로토콜의 틈새는 늘 오픈소스 연구자들의 가장 정교한 놀이터가 된다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=ios+iap2+carkit+nmea+location+simulation+reloc" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/Reukix/Reloc" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
