# -*- coding: utf-8 -*-
# Story 2: ashayas/icloud-s3

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] ashayas/icloud-s3 : 기상천외한 리버스 엔지니어링 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_icloud_s3.jpg" alt="iCloud S3 Free Object Store" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 애플 공유 앨범 정책의 빈틈을 찌른 해커 정신</span>
              <span class="platform-tag">GitHub Viral</span>
              <span class="platform-tag">ashayas / icloud-s3</span>
            </div>
            
            <h2 class="article-headline">
              "애플 계정 하나로 12TB 무료 AWS S3를 만든다": 기상천외한 Rust 이미지 스테가노그래피의 반란
            </h2>

            <div class="article-subheadline">
              "기타 솔로가 흐르는 추억 슬라이드쇼는 99.999999999% SLA가 아닙니다" — 애플의 '공유 앨범은 iCloud 저장 공간 용량에 산정되지 않는다'는 공식 정책 허점을 파고들어, 무손실 2048px PNG 픽셀에 바이너리 데이터를 욱여넣고 표준 AWS S3 REST API를 구현한 괴짜 엔지니어링의 정점
            </div>
            <p class="article-snippet">
              200개 공유 앨범 × 5,000장 × 12.18MB = 1,000,000개 객체(약 12.18TB)를 0원의 비용으로 호스팅. 아이폰 사진 앱에서 스크롤을 내리면 데이터베이스 덤프 파일명이 HUD 배너로 보이는 유쾌한 오픈소스 풍자 프로젝트.
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
              <i data-lucide="flame"></i> 1. 리드: 아이폰 사진 앱을 열었더니 회사의 데이터베이스 백업이 펼쳐졌다
            </h3>
            <p>
              주말 저녁, 가족들과 찍은 사진을 보기 위해 아이폰의 '사진(Photos.app)'을 켠 한 개발자는 눈을 의심했다. 
              최근 공유 앨범 탭에 알록달록한 노이즈 패턴의 정사각형 이미지 수백 장이 빼곡하게 차 있었기 때문이다. 
              그리고 각 이미지 상단에는 마치 군용 HUD처럼 선명한 푸른색 배너가 각인되어 있었다: <code>pg_dump_production_20261102.sql.gz (11.8 MB) | CRC32: 0x8FA43E19</code>.
            </p>
            <p>
              이 기괴한 풍경의 정체는 오픈소스 개발자 <strong>ashayas</strong>가 공개한 <strong>iCloudS3(ashayas/icloud-s3)</strong> 프로젝트다. 
              AWS S3의 비싼 아웃바운드 트래픽 요금과 월간 스토리지 비용에 분노하던 한 엔지니어가, 애플 생태계의 가장 깊은 곳에 숨겨진 약관의 맹점을 집요하게 파고들어 만들어낸 결과물이다.
            </p>
            <p>
              터미널에서 표준 AWS CLI 명령어인 <code>aws s3 cp backup.tar.gz s3://my-bucket/</code>을 실행하면, 이 Rust 프로그램은 바이너리 파일을 무손실 PNG 이미지의 RGB 픽셀 채널로 변환한 뒤 애플의 무료 공유 앨범 서버로 조용히 밀어 넣는다. 
              그리고 필요할 때 다시 <code>aws s3 cp</code>를 치면 감쪽같이 원본 파일이 복원된다.
            </p>

            <div class="editorial-quote">
              "애플의 공식 정책 문서(Support #108916)를 읽어보셨습니까? 
              <strong>'공유 앨범에 업로드된 사진과 비디오는 사용자의 iCloud 저장 공간에 포함되지 않는다'</strong>고 명시되어 있습니다. 
              계정당 200개의 공유 앨범, 앨범당 5,000장, 최대 2048×2048 해상도. 
              이것은 애플이 전 세계 개발자들에게 무제한으로 선물한 12테라바이트의 무료 분산 오브젝트 스토리지입니다."
              <span class="quote-author">— 개발자 ashayas 프로젝트 README 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 기가바이트당 0.023달러에 맞서는 12TB 무료 루프홀의 수학
            </h3>
            <p>
              아마존 웹 서비스(AWS)의 S3 스탠다드 요금은 기가바이트(GB)당 월 0.023달러다. 
              12테라바이트를 저장하려면 매달 약 280달러(연간 3,360달러, 한화 약 450만 원)가 소요된다. 
              게다가 데이터를 외부로 뺄 때 부과되는 송신(Egress) 요금은 개발자들을 끊임없이 옭아매는 공포다.
            </p>
            <p>
              iCloudS3는 이 수학적 공식을 완전히 무너뜨린다:
            </p>
            <ul>
              <li><strong>무손실 24비트 RGB 픽셀 용량:</strong> 2048 × 2048 해상도의 PNG 이미지는 픽셀당 3바이트(Red, Green, Blue)를 가지므로, 장당 정확히 <strong>12.18 MB</strong>의 순수 바이너리 데이터를 담을 수 있다.</li>
              <li><strong>공유 앨범 한도 곱셈:</strong> 200개 앨범 × 앨범당 5,000장 = 총 1,000,000개의 객체 슬롯.</li>
              <li><strong>최종 저장 용량:</strong> 1,000,000 × 12.18 MB &approx; <strong>12.18 TB (테라바이트)</strong>.</li>
              <li><strong>실제 청구 금액:</strong> <strong>$0.00</strong> (iCloud Drive 5GB 기본 무료 할당량 소모량 0바이트).</li>
            </ul>
            <p>
              이것은 단순한 장난을 넘어, 거대 클라우드 기업들이 독점적 인프라 마진을 착취하는 구조에 대한 가장 날카롭고 유머러스한 해커적 풍자다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> iCloudS3: AWS S3 REST 요청에서 애플 공유 앨범 PNG 픽셀로의 변환 파이프라인
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">단계 1: 표준 S3 API 수신</span>
                  <strong>Rust Axum REST Server</strong>
                  <div class="schematic-desc">
                    AWS CLI, boto3, rclone의 PUT/GET/HEAD/LIST 요청을 100% 호환하는 로컬 S3 XML 게이트웨이 구동
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 2: 픽셀 스테가노그래피</span>
                  <strong>Byte to RGB Array</strong>
                  <div class="schematic-desc">
                    바이너리 바이트 스트림을 2048x2048 무손실 24비트 PNG 픽셀 버퍼로 1:1 패킹. 청크 분할 및 CRC32 해시 계산
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 3: 64px HUD 오버레이</span>
                  <strong>Visual Header Burning</strong>
                  <div class="schematic-desc">
                    사진 앱에서 육안 식별이 가능하도록 상단 64픽셀에 파일명, MIME 타입, 청크 인덱스, 타임스탬프 텍스트 렌더링
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 4: 공유 앨범 푸시</span>
                  <strong>Apple PhotoKit Gateway</strong>
                  <div class="schematic-desc">
                    애플 공유 앨범 엔드포인트로 무손실 이미지 전송. iCloud 5GB 용량 소모 0바이트 상태로 글로벌 CDN 캐싱 완료
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: 2048px 무손실 PNG 패킹과 64px HUD 배너의 비밀
            </h3>
            <p>
              iCloudS3의 기술적 구현은 생각보다 훨씬 견고하다. 
              Rust 언어로 작성된 서버는 고성능 웹 프레임워크인 <code>Axum</code>을 기반으로 작동하며, 아마존 S3의 표준 서명(SigV4)과 버킷 조작 프로토콜을 그대로 흉내 낸다.
            </p>
            <p>
              가장 흥미로운 부분은 <strong>'애플 사진 압축 알고리즘의 회피'</strong>다. 
              애플의 공유 앨범은 대역폭을 아끼기 위해 업로드되는 JPEG 이미지를 무자비하게 재압축한다. 
              만약 JPEG에 데이터를 숨기면 손실 압축 과정에서 비트가 뒤틀려 원본 파일이 깨져버린다. 
              그러나 개발자는 애플 서버가 <strong>2048×2048 이하 크기의 PNG 파일에 대해서는 무손실(Lossless) 압축을 유지한 채 원본 픽셀 데이터를 그대로 보존한다</strong>는 사실을 리버스 엔지니어링으로 발견했다.
            </p>
            <p>
              또한 개발자는 위트 있는 안전장치를 마련했다: 
              이미지 최상단 64개 픽셀 라인에는 데이터를 기록하지 않고, 파일명과 용량, CRC32 체크섬을 시각적 텍스트로 구워 넣었다. 
              덕분에 사용자가 아이폰 사진 앱에서 앨범을 넘기면, 데이터 덩어리가 아니라 마치 첨단 데이터 카탈로그처럼 파일 정보가 깔끔하게 노출된다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_icloud_s3.jpg" alt="iCloud S3 Architecture and Photos App Live Verification" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="monitor"></i> <strong>[실구동 아키텍처 캡처]</strong> 좌측: 아이폰 Photos.app 공유 앨범에 64px HUD 배너와 함께 보관된 실제 프로덕션 DB 백업 이미지들. 우측: 로컬 9000번 포트로 구동된 Rust 게이트웨이를 향해 표준 AWS CLI(aws s3 cp)로 파일을 업로드 및 다운로드하며 무결성(CRC32)을 검증하는 터미널 세션.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적 분기점과 약관의 경계: 풍자(Satire)와 서비스 약관(ToS) 사이
            </h3>
            <p>
              당연하게도 이 프로젝트는 실전 운영용(Production)으로 만들어진 것이 아니다. 
              개발자 스스로도 리드미에 큰 글씨로 경고를 적어두었다: 
              <strong>"경고: 본 프로젝트는 풍자(Satire)입니다. 통기타 음악이 배경으로 깔리는 아이폰 추억 슬라이드쇼는 AWS의 99.999999999% 내구성 SLA를 제공하지 않습니다."</strong>
            </p>
            <p>
              법적으로 볼 때, 이 프로젝트는 다음과 같은 복잡한 쟁점을 품고 있다:
            </p>
            <ul>
              <li><strong>애플 이용약관(ToS) 위반 위험:</strong> 비상업적 용도의 사진 공유 서비스를 일반 데이터 스토리지로 전용하는 행위는 애플 클라우드 서비스 약관의 '서비스의 비정상적 오용' 조항에 저촉되어 계정 정지 처분을 받을 수 있다.</li>
              <li><strong>저작권 및 컴퓨터 사기 방지법(CFAA):</strong> 리버스 엔지니어링 자체는 상호 운용성을 위한 합법적 연구로 보호받을 여지가 있으나, 인증 토큰을 탈취하거나 비인가 API를 자동 호출하는 스크립트는 법적 분쟁의 빌미가 될 수 있다.</li>
              <li><strong>빅테크의 정책 대응:</strong> 과거 구글 포토 무제한 백업 허점이 막혔듯, 애플 역시 공유 앨범의 픽셀 엔트로피(Entropy)를 검사하여 데이터 노이즈로 판명된 이미지를 차단하는 방어 알고리즘을 도입할 가능성이 높다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 해커들이 거대 빅테크를 비웃는 가장 우아한 방식
            </h3>
            <p>
              어떤 이들은 "이런 쓸모없는 짓을 왜 하느냐"고 물을지도 모른다. 
              하지만 오픈소스 역사의 위대한 도약들은 언제나 규칙에 얽매이지 않는 호기심과 불합리한 시스템에 대한 조롱에서 시작되었다.
            </p>
            <p>
              수조 달러 가치의 실리콘밸리 제국들이 만들어 놓은 철옹성 같은 유료 구독의 벽 뒤편에서, 단 몇백 줄의 Rust 코드로 12테라바이트의 무료 저장소를 뚫어낸 이 유쾌한 해킹은 우리에게 묻고 있다: 
              <strong>"당신이 당연하다고 믿는 클라우드의 규칙들은 과연 영원한가?"</strong>
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=iCloud+S3+free+object+storage+hack" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/ashayas/icloud-s3" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
