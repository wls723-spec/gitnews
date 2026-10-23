import json
import re

# 1. Load base step 229
with open(r'c:\Program Files\1a\src\gitnews\scratch\step229.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Apply all replace_file_content calls between 230 and 465 for 2026-10-14.html
with open(r'C:\Users\user\.gemini\antigravity-ide\brain\a1fb9932-b132-42a9-b26f-a34da1d87626\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        idx = obj.get('step_index')
        if 230 <= idx < 465:
            for c in obj.get('tool_calls', []):
                if c['name'] == 'replace_file_content' and '2026-10-14.html' in c['args'].get('TargetFile', ''):
                    target = c['args']['TargetContent']
                    repl = c['args']['ReplacementContent']
                    if target in content:
                        content = content.replace(target, repl, 1)
                        print(f'Applied step {idx}')
                    else:
                        print(f'Failed step {idx}')

# 3. Apply memo theme styles
style_pattern = re.compile(r'<link rel="stylesheet" href="\.\./assets/css/trending_theme\.css">\s*<style>.*?</style>\s*</head>', re.DOTALL)
new_head = '<link rel="stylesheet" href="../assets/css/memo_theme.css">\n</head>'
content, c1 = style_pattern.subn(new_head, content)

header_old_pattern = re.compile(r'<!-- 헤더 -->\s*<header class="header-hero">.*?</header>', re.DOTALL)
new_header = '''<!-- 헤더 -->
    <header class="header-hero">
      <div class="date-badge">
        <i data-lucide="edit-3" style="color:#b45309;"></i>
        <span>2026-10-14 데일리 오픈소스 필드 메모</span>
      </div>
      <h1 id="hero-title">빅테크 독점의 해자를 허무는 오픈소스 혁명</h1>
      <p>개발자 커뮤니티와 유튜브를 뒤흔든 핵심 프로젝트를 손으로 끄적이듯 정리한 심층 기술 메모입니다.</p>
    </header>'''
content, c2 = header_old_pattern.subn(new_header, content)

script_old_pattern = re.compile(r'<script src="\.\./assets/libs/lucide\.min\.js"></script>\s*<script>.*?</script>', re.DOTALL)
new_scripts = '''<script src="../assets/libs/lucide.min.js"></script>
  <script src="../assets/libs/rough.min.js"></script>
  <script src="../assets/libs/rough-notation.js"></script>

  <script>
    lucide.createIcons();

    // Rough Notation 손글씨 하이라이트 & 손그림 밑줄
    window.addEventListener('DOMContentLoaded', () => {
      try {
        if (window.RoughNotation) {
          const title = document.getElementById('hero-title');
          if (title) {
            const annotation = RoughNotation.annotate(title, {
              type: 'underline',
              color: '#f59e0b',
              strokeWidth: 4,
              iterations: 2
            });
            annotation.show();
          }

          document.querySelectorAll('.editorial-quote strong').forEach((el, idx) => {
            if (idx < 6) {
              const a = RoughNotation.annotate(el, {
                type: 'highlight',
                color: '#fef08a',
                multiline: true,
                iterations: 1
              });
              a.show();
            }
          });
        }
      } catch (e) {
        console.warn('RoughNotation init error:', e);
      }
    });

    // 개별 기사 카드 클릭 시 상세 토글
    function toggleArticle(card) {
      card.classList.toggle('active');
      const actionText = card.querySelector('.article-action span');
      
      if (card.classList.contains('active')) {
        actionText.textContent = '메모 접기 ▲';
      } else {
        actionText.textContent = '손글씨 심층 메모 읽기';
      }
    }

    // 전체 펼치기 / 접기 버튼
    let allExpanded = false;
    function toggleAllArticles() {
      allExpanded = !allExpanded;
      const cards = document.querySelectorAll('.article-card');
      const toggleText = document.getElementById('toggle-all-text');
      
      cards.forEach(card => {
        const actionText = card.querySelector('.article-action span');
        if (allExpanded) {
          card.classList.add('active');
          actionText.textContent = '메모 접기 ▲';
        } else {
          card.classList.remove('active');
          actionText.textContent = '손글씨 심층 메모 읽기';
        }
      });

      toggleText.textContent = allExpanded ? '전체 메모 접기' : '전체 메모 펼치기';
    }
  </script>'''
content, c3 = script_old_pattern.subn(new_scripts, content)
print(f'Theme applied: head={c1}, header={c2}, scripts={c3}')

# 4. Now clean up per user instructions:

# (A) Article 1 Video Embed Box Removal:
# Find exact string of the video showcase box in Article 1
art1_video_box = '''            <!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="play-circle" style="color:#ef4444;"></i> ArtCraft 심층 분석 & 포토샵 클린룸 복제 시연
                </span>
                <a href="https://www.youtube.com/watch?v=aL8zzL0ke48" target="_blank" class="media-showcase-badge video" style="text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">
                  <i data-lucide="external-link" style="width:12px;height:12px;"></i> 유튜브 새창 재생
                </a>
              </div>
              <div class="media-showcase-body">
                <div class="video-embed-wrapper">
                  <iframe 
                    src="https://www.youtube.com/embed/aL8zzL0ke48?rel=0&modestbranding=1" 
                    title="ArtCraft Review: Free Photoshop, Premiere & Illustrator Clones in Rust" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                  </iframe>
                </div>
              </div>
              <div class="media-showcase-caption">
                <strong>▲ "ArtCraft Review: Free Photoshop, Premiere & Illustrator Clones in Rust" (Heroic steps)</strong>
                <ul style="margin-top:0.4rem; margin-left:1.2rem; color:#94a3b8; font-size:0.85rem; line-height:1.6;">
                  <li><strong>01:30</strong> — 어도비 대체 오픈소스 ArtCraft(PhotoCraft)의 Rust 기반 GUI 구조 해부</li>
                  <li><strong>04:15</strong> — 포토샵 레이어 합성 속도 vs PhotoCraft WebGPU 실시간 렌더링 성능 실측</li>
                  <li><strong>07:40</strong> — Claude Code 및 MCP 연동을 통한 바이너리 분석과 무제한 무료 배포 시연</li>
                </ul>
              </div>
            </div>'''

print("Art1 video box in content:", art1_video_box in content)
if art1_video_box in content:
    content = content.replace(art1_video_box + "\n\n", "")

# (B) Article 4 Video Embed Box Removal:
art4_video_box = '''            <!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="play-circle" style="color:#ef4444;"></i> Bilawal Sidhu 개발자 공식 데모 영상
                </span>
                <a href="https://www.youtube.com/watch?v=GRJaKcXZS94" target="_blank" class="media-showcase-badge video" style="text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">
                  <i data-lucide="external-link" style="width:12px;height:12px;"></i> 유튜브 새창 재생
                </a>
              </div>
              <div class="media-showcase-body">
                <div class="video-embed-wrapper">
                  <iframe 
                    src="https://www.youtube.com/embed/GRJaKcXZS94?rel=0&modestbranding=1" 
                    title="We Got Open Source God’s Eye Before GTA 6" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                  </iframe>
                </div>
              </div>
              <div class="media-showcase-caption">
                <strong>▲ "We Got Open Source God’s Eye Before GTA 6" (Bilawal Sidhu)</strong>
                <ul style="margin-top:0.4rem; margin-left:1.2rem; color:#94a3b8; font-size:0.85rem; line-height:1.6;">
                  <li><strong>00:45</strong> — 전직 구글 맵스 PM의 CesiumJS 3D 포토리얼 지도 연동 시연</li>
                  <li><strong>02:10</strong> — 음성 자연어 명령으로 대만 해협 통과 항공기·선박 레이더 실시간 추적</li>
                  <li><strong>04:30</strong> — 오픈소스 FLIR 열화상 카메라 HUD 및 공간 정보 관제 기능</li>
                </ul>
              </div>
            </div>'''

print("Art4 video box in content:", art4_video_box in content)
if art4_video_box in content:
    content = content.replace(art4_video_box + "\n\n", "")

# (C) Article 1 Footer:
old_art1_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/morluto/rea#webgpu-demo" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> WebGPU 웹 데모 바로 체험
                </a>
                <a href="https://www.youtube.com/watch?v=aL8zzL0ke48" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 영상 바로보기
                </a>
                <a href="https://github.com/morluto/rea" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

new_art1_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/watch?v=aL8zzL0ke48" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/morluto/rea" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

print("Art1 footer in content:", old_art1_footer in content)
content = content.replace(old_art1_footer, new_art1_footer)

# (D) Article 2 Footer:
old_art2_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://voicestudio.sh" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹 데모 바로 체험
                </a>
                <a href="https://www.youtube.com/results?search_query=VoiceStudio+ElevenLabs+alternative" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰 보기
                </a>
                <a href="https://github.com/debpalash/VoiceStudio" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

new_art2_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://voicestudio.sh" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹사이트 / 데모
                </a>
                <a href="https://www.youtube.com/results?search_query=VoiceStudio+ElevenLabs+alternative" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/debpalash/VoiceStudio" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

print("Art2 footer in content:", old_art2_footer in content)
content = content.replace(old_art2_footer, new_art2_footer)

# (E) Article 3 Footer:
old_art3_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/xtool-org/xtool#getting-started" target="_blank" class="project-link demo">
                  <i data-lucide="zap" style="width:16px;height:16px;"></i> 1분 퀵스타트 가이드
                </a>
                <a href="https://www.youtube.com/results?search_query=xtool+xcode+replacement+linux" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰 보기
                </a>
                <a href="https://github.com/xtool-org/xtool" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

new_art3_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/results?search_query=xtool+xcode+replacement+linux" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/xtool-org/xtool" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

print("Art3 footer in content:", old_art3_footer in content)
content = content.replace(old_art3_footer, new_art3_footer)

# (F) Article 4 Footer:
old_art4_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/bilawalsidhu/gods-eye-view#quickstart" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 3D 위성 웹 뷰어 실행 가이드
                </a>
                <a href="https://www.youtube.com/watch?v=GRJaKcXZS94" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 영상 바로보기
                </a>
                <a href="https://github.com/bilawalsidhu/gods-eye-view" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

new_art4_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/watch?v=GRJaKcXZS94" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/bilawalsidhu/gods-eye-view" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

print("Art4 footer in content:", old_art4_footer in content)
content = content.replace(old_art4_footer, new_art4_footer)

# (G) Article 5 Footer:
old_art5_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/lyogavin/airllm#quickstart" target="_blank" class="project-link demo">
                  <i data-lucide="play" style="width:16px;height:16px;"></i> Colab 무료 즉시 실행
                </a>
                <a href="https://www.youtube.com/results?search_query=AirLLM+run+70b+4gb+gpu" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 벤치마크 보기
                </a>
                <a href="https://github.com/lyogavin/airllm" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

new_art5_footer = '''            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/results?search_query=AirLLM+run+70b+4gb+gpu" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/lyogavin/airllm" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>'''

print("Art5 footer in content:", old_art5_footer in content)
content = content.replace(old_art5_footer, new_art5_footer)

target_html = r"c:\Program Files\1a\src\gitnews\news\2026-10-14.html"
with open(target_html, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved cleaned news/2026-10-14.html! Final length:", len(content), "Lines:", len(content.splitlines()))
