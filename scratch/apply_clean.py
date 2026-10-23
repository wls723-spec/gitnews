import re

filepath = r"c:\Program Files\1a\src\gitnews\news\2026-10-14.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove video box 1
pattern_art1_video = re.compile(
    r'\s*<!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->\s*<div class="media-showcase-box">.*?ArtCraft 심층 분석 & 포토샵 클린룸 복제 시연.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)
content = pattern_art1_video.sub('', content)

# 2. Remove video box 2
pattern_art4_video = re.compile(
    r'\s*<!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->\s*<div class="media-showcase-box">.*?Bilawal Sidhu 개발자 공식 데모 영상.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)
content = pattern_art4_video.sub('', content)

# 3. Article 1 Footer:
# Remove WebGPU 웹 데모 바로 체험
# Update 유튜브 영상 바로보기 -> 유튜브 관련 리뷰보기
old_art1_footer = """            <div class="article-footer-links">
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
            </div>"""

new_art1_footer = """            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/watch?v=aL8zzL0ke48" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/morluto/rea" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>"""

print("old_art1_footer in content:", old_art1_footer in content)

# 4. Article 2 Footer:
# Keep voicestudio.sh (actual standalone website), ensure clean title
old_art2_footer = """            <div class="article-footer-links">
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
            </div>"""

new_art2_footer = """            <div class="article-footer-links">
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
            </div>"""

print("old_art2_footer in content:", old_art2_footer in content)

# 5. Article 3 Footer:
# Remove 1분 퀵스타트 가이드 (which is just github #getting-started)
old_art3_footer = """            <div class="article-footer-links">
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
            </div>"""

new_art3_footer = """            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/results?search_query=xtool+xcode+replacement+linux" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/xtool-org/xtool" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>"""

print("old_art3_footer in content:", old_art3_footer in content)

# 6. Article 4 Footer:
# Remove 3D 위성 웹 뷰어 실행 가이드 (which is just github #quickstart)
old_art4_footer = """            <div class="article-footer-links">
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
            </div>"""

new_art4_footer = """            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/watch?v=GRJaKcXZS94" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/bilawalsidhu/gods-eye-view" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>"""

print("old_art4_footer in content:", old_art4_footer in content)

# 7. Article 5 Footer:
# Remove Colab 무료 즉시 실행 (which is just github #quickstart)
old_art5_footer = """            <div class="article-footer-links">
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
            </div>"""

new_art5_footer = """            <div class="article-footer-links">
              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://www.youtube.com/results?search_query=AirLLM+run+70b+4gb+gpu" target="_blank" class="project-link youtube">
                  <i data-lucide="video" style="width:16px;height:16px;"></i> 유튜브 관련 리뷰보기
                </a>
                <a href="https://github.com/lyogavin/airllm" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>"""

print("old_art5_footer in content:", old_art5_footer in content)

content = content.replace(old_art1_footer, new_art1_footer)
content = content.replace(old_art2_footer, new_art2_footer)
content = content.replace(old_art3_footer, new_art3_footer)
content = content.replace(old_art4_footer, new_art4_footer)
content = content.replace(old_art5_footer, new_art5_footer)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated 2026-10-14.html successfully!")
