# Rule: Daily Open Source & AI Trending Briefing & Deep Tech Journalism SOP

When generating daily trending briefings or HTML reports:

1. **Follow [DAILY_TRENDING_GUIDELINES.md](file:///c:/Program%20Files/1a/src/gitnews/DAILY_TRENDING_GUIDELINES.md)**.
2. **TECH JOURNALISM PRINCIPLES (Wired + Bloomberg + Stratechery 5-Stage Framework)**:
   - **Stage 1 (Lede)**: Scene-setting hook capturing dramatic conflict between monopolies and rogue open-source creators.
   - **Stage 2 (Nut Graf)**: Clear core thesis answering why this matters right now, backed by viral community reactions.
   - **Stage 3 (Mechanism)**: First-principles technical exposition, unmasking clean-room reverse engineering, memory streaming, or protocol bridges.
   - **Stage 4 (The Moat & Legal Stakes)**: Analysis of who loses billions in subscription revenue, software moat collapse, and legal fair-use precedents (*Sega v. Accolade*).
   - **Stage 5 (Kicker)**: Resonant, punchy conclusion leaving lasting impact.
3. **MAIN STORY (COVER STORY) TREATMENT**:
   - The #1 breakthrough project must be designated as `.article-card.main-story` with a `⭐ 오늘의 메인 기사` badge.
   - The overarching primary headline of the day (e.g. *"빅테크 독점의 해자를 허무는 오픈소스 혁명"*) must be embedded inside the first article card as `.main-lead-headline` with `id="hero-title"` (triggering RoughNotation's hand-drawn underline animation), followed by its detailed sub-headline `.article-subheadline`.
   - The page header (`.header-hero`) serves strictly as a clean, elegant masthead (`<h1 class="site-title">GitNews 데일리 오픈소스 & AI 트렌드</h1>`).
4. **DIAGRAMS & VISUALS**:
   - **NO MERMAID**: Never use Mermaid.js inside hidden/accordion divs because it computes 0x0 bounding boxes and renders invisibly.
   - **PURE CSS/SVG SCHEMATICS**: Always use robust, responsive pure HTML/CSS flex/grid boxes (`.schematic-container`, `.schematic-box`) that render instantly at 100% clarity.
   - **REAL DEMO CAPTURES & NO VIDEO IFRAMES**: Incorporate actual software UI screenshots and terminal build logs. Never embed in-page video player iframes (which frequently fail across browser cross-origin/cookie restrictions); instead, provide high-contrast `[▶️ 유튜브 관련 리뷰보기]` action buttons.
   - **NO REDUNDANT FAKE DEMO BUTTONS**: Never generate redundant demo buttons pointing to GitHub anchors (`#quickstart`, `#demo`); only provide a demo/web button when a real, external standalone web app exists (e.g. `voicestudio.sh`).
   - **HAND-DRAWN MEMO AESTHETIC (Rough.js & Rough Notation)**: Use `assets/css/memo_theme.css` with warm grid graph paper background, washi tape, sticky notes, wobbly sketchy borders, and hand-drawn typography (Gaegu, Gowun Dodum). Dynamically apply Rough Notation underlines and highlighter animations via `assets/libs/rough-notation.js`.
   - **NO INLINE CHEESY AI ART**: Never insert generic AI art inside the article body with captions like "▲ 재탄생을 상징화한 시네마틱 아트".
   - **NO FLUFF / META REMARKS**: Never insert developer/agent self-referential debug badges like "● 100% 무결점 렌더링 뷰", "총 5편의 심층 르포 기사 수록", "데일리 오픈소스 필드 메모", or "작성: 테크 저널리즘 인텔리전스 데스크".
   - **STANDARDIZED ACTION BUTTONS**: Use strictly `"메모 펼치기"` / `"메모 접기 ▲"` on cards, and `"전체 메모 펼치기"` / `"전체 메모 접기"` on top.
5. **STANDALONE ALL-IN-ONE PACKAGING (단일 자립형 파일 배포 필수)**:
   - 기사 생성 직후 반드시 `python scripts/make_standalone.py news/YYYY-MM-DD.html`을 실행하여 모든 CSS(`memo_theme.css`), 자바스크립트(`lucide.min.js`, `rough.min.js`, `rough-notation.js`), 썸네일 및 실구동 이미지(10개)를 HTML 내부에 Base64 Data URI 및 인라인 태그로 완전 임베드한다.
   - 단일 HTML 파일만 타인에게 전송하거나 외부 환경에서 열어도 디자인과 이미지가 절대 깨지지 않아야 한다.
6. **QUALITY VERIFICATION**:
   - `python scripts/verify_news.py news/YYYY-MM-DD.html`을 실행하여 100% Standalone 상태와 태그 매핑, 다이어그램 가시성을 정밀 검증한다.
7. Save to `news/YYYY-MM-DD.html` and update `history_seen_projects.md`.
