# -*- coding: utf-8 -*-
# Story 4: Fission-AI/OpenSpec

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] Fission-AI/OpenSpec                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openspec.jpg" alt="OpenSpec Spec-Driven Development Blueprint Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="file-check-2" style="width:12px;height:12px;fill:#fff;"></i> SPEC-DRIVEN SDD</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#166534;">📐 7만 5천 스타突破 · '바이브 코딩' 난맥상을 설계 명세로 잡는 SDD 표준</span>
              <span class="platform-tag">GitHub Trending &amp; openspec.dev</span>
              <span class="platform-tag">Fission-AI / OpenSpec</span>
            </div>

            <h2 class="article-headline">
              "코드 한 줄 짜기 전에 스펙부터 합의한다" — 다중 저장소·멀티 에이전트 시대의 설계 규격 'OpenSpec' (+105★/일)
            </h2>

            <div class="article-subheadline">
              /openspec-explore → /openspec-propose(proposal·specs·design·tasks) → /openspec-apply-change → /openspec-archive-change 순환 워크플로와 멀티 레포 동기화 'Stores(Beta)' 제공 (누적 75,565스타, MIT)
            </div>
            <p class="article-snippet">
              AI 코딩 에이전트에게 프롬프트 한 줄을 던져 수천 줄의 코드를 순식간에 생성하는 '바이브 코딩'이 확산될수록, 실무 팀들은 "에이전트가 기존 아키텍처와 어긋난 코드를 맘대로 찍어내고, 백엔드·프론트엔드 저장소 간 요구사항이 표류한다"는 고통에 직면했습니다. 오늘 하루 <strong>105개의 스타를 추가하며 누적 75,565스타</strong>를 돌파한 <strong>Fission-AI/OpenSpec</strong>은 무거운 폭포수 모델 없이도 평문 마크다운 기반의 <code>proposal.md</code>·<code>specs/</code>·<code>design.md</code>·<code>tasks.md</code>를 에이전트와 사람이 함께 검토하고, 다중 저장소를 <code>Stores</code>로 묶어내는 경량 명세 주도 개발(SDD) 표준으로 자리매김했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 프롬프트 채팅창에서 사라진 설계도, 브라운필드 코드베이스의 반란
            </h3>
            <p>
              비어 있는 폴더에서 토이 앱 하나를 뚝딱 만드는 데는 채팅창 프롬프트 한 줄이면 충분하다. 하지만 이미 수십만 줄의 레거시 코드와 API 서버, 웹 앱, 공유 라이브러리가 얽혀 있는 <strong>브라운필드(Brownfield)</strong> 실무 저장소에 에이전트를 풀어놓는 순간 악몽이 시작된다. 컨텍스트 창이 길어질수록 에이전트는 3턴 전에 합의한 요구사항을 까먹고, 테스트 없는 임시 코드를 덮어쓰며, 동료 개발자는 PR에 올라온 40개 파일의 맥락을 도저히 추적할 수 없게 된다.
            </p>
            <p>
              오늘 GitHub TypeScript 트렌딩 상위권을 지키며 누적 <strong>75,565스타(포크 5,165개)</strong>에 도달한 <strong>Fission-AI/OpenSpec</strong>은 바로 이 '에이전트 기억 상실과 설계 표류'를 정조준한다. 특이한 점은 이 프로젝트 자체가 거대한 사유 SaaS 플랫폼이 아니라 <code>npm install -g @fission-ai/openspec</code> 또는 <code>brew install openspec</code>으로 설치되는 MIT 오픈소스 CLI와 순수 마크다운 스킬 묶음이라는 사실이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "폭포수가 아닌 유동적 명세 — 에이전트가 쓰고 인간이 승인한다"
            </h3>
            <p>
              기존 엔터프라이즈의 명세서나 위키(Confluence, Notion)가 실패했던 이유는 '코드와 분리된 죽은 문서'였기 때문이다. OpenSpec은 정반대의 전략을 택한다. 명세 작성을 인간에게 떠넘기지 않고 <strong>AI 에이전트가 코드베이스를 먼저 읽은 뒤 제안서와 시나리오 스펙을 초안 작성하게 하고, 인간은 코드를 짜기 전에 그 4장의 마크다운만 리뷰</strong>한다.
            </p>

            <div class="editorial-quote">
              <p>
                "딱딱하지 않고 유동적으로, 폭포수가 아니라 반복적으로, 신규 프로젝트뿐만 아니라 기존 브라운필드 코드베이스를 위해 설계했다. <strong>AI가 제안서와 시나리오를 쓰면 당신은 코드가 단 한 줄도 작성되기 전에 계획을 검토한다.</strong>"
              </p>
              <small>— Fission-AI/OpenSpec 공식 설계 철학 (MIT License)</small>
            </div>

            <p>
              여기에 최근 베타로 공개된 <strong><code>Stores</code></strong> 기능이 결합되면서, OpenSpec은 1인 개발자 도구를 넘어 API 팀·웹 팀·SDK 팀이 여러 Git 저장소에 걸쳐 하나의 변경 계획을 공유하는 조직 단위 명세 버스(Spec Bus)로 확장됐다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 4단계 변경 사이클과 Cross-Repo <code>Stores</code> 구조 해부
            </h3>
            <p>
              <code>openspec init</code>을 실행하면 프로젝트 내부에 Claude Code, Codex(<code>$openspec-propose</code>), Cursor, OpenCode 등 주요 에이전트가 즉시 인식하는 슬래시 스킬이 설치되며, 모든 변경은 명확한 생명주기를 따른다:
            </p>
            <ul>
              <li><strong>탐색과 제안(<code>/openspec-explore</code> → <code>/openspec-propose</code>):</strong> 먼저 <code>explore</code> 단계에서 기존 스타일·의존성 설정을 읽기 전용으로 진단한 뒤, <code>propose &lt;기능명&gt;</code>을 호출하면 <code>openspec/changes/&lt;name&gt;/</code> 폴더 아래에 4개 문서—<code>proposal.md</code>(배경과 변경 범위), <code>specs/</code>(<code>WHEN/THEN</code> 기반 요구사항 시나리오), <code>design.md</code>(기술 구현 접근법), <code>tasks.md</code>(체크리스트)—가 일괄 생성된다.</li>
              <li><strong>실행과 아카이빙(<code>/openspec-apply-change</code> → <code>/openspec-archive-change</code>):</strong> 에이전트는 <code>tasks.md</code>의 항목을 순서대로 구현·체크하며, 완료 후에는 <code>archive-change</code>를 통해 변경 내역을 날짜별 아카이브로 옮기고 살아있는 마스터 <code>specs/</code>를 최신 상태로 병합한다. 확장 프로파일을 켜면 <code>verify-change</code>, <code>ff-change</code>, <code>onboard</code> 등 세밀한 제어 스킬도 쓸 수 있다.</li>
              <li><strong>멀티 레포 단일 진실 공급원(<code>Stores</code>):</strong> 플랫폼 팀이 중앙 스펙 저장소(Store)에 공용 요구사항을 <code>git push</code>하면, 제품 팀의 코딩 에이전트들이 각자의 저장소에서 이를 읽기 전용으로 참조해 API 스키마 불일치와 위키 노후화를 원천 차단한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">OpenSpec 명세 주도 개발(SDD) 4단계 루프 &amp; 멀티 레포 Stores 아키텍처</span>
                <span class="schematic-badge">TypeScript · MIT · 75.5k★ · Claude/Codex/Cursor/OpenCode</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Explore &amp; Propose</div>
                  <div class="schematic-desc">
                    <code>/openspec-explore</code>로 기존 코드 진단<br>
                    <code>/openspec-propose</code> 실행 시 4종 파일 생성<br>
                    <code>proposal.md</code> · <code>specs/</code> (WHEN/THEN)<br>
                    <code>design.md</code> · <code>tasks.md</code> 체크리스트
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Human Gate &amp; Apply</div>
                  <div class="schematic-desc">
                    코드 작성 전 인간이 설계·시나리오 검토<br>
                    <code>/openspec-apply-change</code>로 순차 구현<br>
                    <code>verify-change</code>로 스펙 대비 정합 검증<br>
                    에이전트 컨텍스트 유실 없이 작업 재개
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Archive &amp; Cross-Repo Stores</div>
                  <div class="schematic-desc">
                    <code>/openspec-archive-change</code>로 마스터 스펙 갱신<br>
                    <code>openspec/</code> 자체가 살아있는 문서로 유지<br>
                    <strong>Stores(Beta)</strong>: 별도 Git 레포에 계획 공유<br>
                    API·웹·라이브러리 팀 동시 에이전트 정렬
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">openspec.dev 공식 플랫폼 실화면 — 에이전트 불문 명세 주도 개발(SDD) 워크플로</span>
              </div>
              <img src="../assets/images/demo_openspec.png" alt="Fission-AI OpenSpec Official Website" class="showcase-img">
              <p class="showcase-caption">
                ▲ openspec.dev 실화면: 7만 5천여 스타를 돌파한 OpenSpec의 공식 웹 인터페이스 및 CLI 원클릭 설치, 멀티 레포 Stores 아키텍처 안내.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 개발 도구 시장: 'IDE 락인' 대신 'Git 안의 평문 마크다운'이 승리하는 이유
            </h3>
            <p>
              최근 일부 유료 AI IDE와 엔터프라이즈 에이전트 플랫폼들은 자체 클라우드 기획 보드와 독점 컨텍스트 서버를 팔며 팀의 요구사항 문서를 자사 서비스 안에 가두려 한다. OpenSpec이 <code>github/spec-kit</code>과 함께 이 시장을 오픈소스로 빠르게 평정한 비결은 극단적인 <strong>탈중앙화</strong>에 있다.
            </p>
            <ul>
              <li><strong>어느 에이전트로 갈아타도 남는 설계 자산:</strong> OpenSpec의 산출물은 특정 툴의 비공개 DB가 아니라 레포지토리 안의 평범한 <code>openspec/</code> 마크다운 디렉터리다. 오늘 Claude Code로 <code>propose</code>를 작성하고 내일 Cursor나 Codex, OpenCode로 <code>apply-change</code>를 실행해도 동일한 문맥이 100% 이어진다.</li>
              <li><strong>'도구 자체를 도구로 개발(Dogfooding)'한 신뢰성:</strong> OpenSpec 저장소 자체도 <code>openspec/specs</code>와 진행 중인 <code>openspec/changes</code> 폴더로 개발되고 있어, 개발자들이 실제 대규모 프로젝트에서 스펙 디렉터리가 어떻게 관리되는지 소스에서 바로 확인할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: AI 시대의 시니어 엔지니어는 코드를 타이핑하지 않고 '계약'을 승인한다
            </h3>
            <p>
              에이전트가 초당 수백 줄의 코드를 뱉어내는 시대에 진짜 병목은 타자 속도가 아니라 "우리가 지금 정확히 무엇을 만들고 있는가"에 대한 팀과 에이전트 간의 합의다.
            </p>
            <p>
              그 합의를 독점 SaaS가 아니라 Git 커밋 한 줄로 버전 관리되는 4장의 마크다운으로 되돌려 놓은 <code>OpenSpec</code>의 7만 5천 스타는, 바이브 코딩의 야생 시대가 끝나고 규율 있는 엔지니어링의 시대가 시작됐음을 알리는 신호다.
            </p>

            <div class="project-links">
              <a href="https://openspec.dev/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> OpenSpec 공식 사이트
              </a>
              <a href="https://www.youtube.com/results?search_query=OpenSpec+Fission+AI+spec+driven+development" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/Fission-AI/OpenSpec" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
