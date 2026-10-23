import re

filepath = r"c:\Program Files\1a\src\gitnews\news\2026-10-14.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove video-embed-wrapper showcase box in Article 1
pattern_art1_video = re.compile(
    r'\s*<!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->\s*<div class="media-showcase-box">.*?ArtCraft 심층 분석 & 포토샵 클린룸 복제 시연.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)
# Let's inspect if that matches
m1 = pattern_art1_video.search(content)
print("Article 1 video box match:", bool(m1))

# 2. Remove video-embed-wrapper showcase box in Article 4
pattern_art4_video = re.compile(
    r'\s*<!-- 유튜브 영상 브라우저 내 직접 재생 플레이어 & 핵심 타임라인 요약 -->\s*<div class="media-showcase-box">.*?Bilawal Sidhu 개발자 공식 데모 영상.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)
m4 = pattern_art4_video.search(content)
print("Article 4 video box match:", bool(m4))
