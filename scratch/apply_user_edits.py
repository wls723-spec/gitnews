import re

html_path = r"c:\Program Files\1a\src\gitnews\news\2026-10-14.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove date badge in header:
old_date_badge = '''      <div class="date-badge">
        <i data-lucide="edit-3" style="color:#b45309;"></i>
        <span>2026-10-14 데일리 오픈소스 필드 메모</span>
      </div>\n'''
if old_date_badge in content:
    content = content.replace(old_date_badge, "")
    print("1. Removed date badge successfully.")
else:
    print("1. FAILED to find exact date badge.")

# 2. Remove subtitle in header:
old_header_p = '''      <p>개발자 커뮤니티와 유튜브를 뒤흔든 핵심 프로젝트를 손으로 끄적이듯 정리한 심층 기술 메모입니다.</p>\n'''
if old_header_p in content:
    content = content.replace(old_header_p, "")
    print("2. Removed header p successfully.")
else:
    print("2. FAILED to find exact header p.")

# 3. Remove "총 5편의 심층 르포 기사 수록" in feed-controls:
old_feed_controls = '''    <!-- 피드 제어 바 -->
    <div class="feed-controls">
      <span style="font-size:0.92rem; color:#94a3b8;">
        총 <strong>5편</strong>의 심층 르포 기사 수록
      </span>
      <button class="btn-toggle-all" onclick="toggleAllArticles()">
        <i data-lucide="layers"></i> <span id="toggle-all-text">전체 기사 펼치기</span>
      </button>
    </div>'''

new_feed_controls = '''    <!-- 피드 제어 바 -->
    <div class="feed-controls" style="justify-content: flex-end;">
      <button class="btn-toggle-all" onclick="toggleAllArticles()">
        <i data-lucide="layers"></i> <span id="toggle-all-text">전체 메모 펼치기</span>
      </button>
    </div>'''

if old_feed_controls in content:
    content = content.replace(old_feed_controls, new_feed_controls)
    print("3. Removed 총 5편 and updated feed-controls successfully.")
else:
    print("3. FAILED to find feed-controls.")

# 4. Remove "작성: 테크 저널리즘 인텔리전스 데스크":
old_author_span = '              <span style="font-size:0.85rem; color:#94a3b8;">작성: 테크 저널리즘 인텔리전스 데스크</span>\n'
c4 = content.count(old_author_span)
content = content.replace(old_author_span, '')
# Also make article-footer-links justify-content: flex-end
content = content.replace('<div class="article-footer-links">', '<div class="article-footer-links" style="justify-content: flex-end;">')
print(f"4. Removed {c4} author spans and aligned footer links.")

# 5. Modify button texts: "심층 장문 기사 읽기" -> "메모 펼치기"
c5_1 = content.count('<span>심층 장문 기사 읽기</span>')
content = content.replace('<span>심층 장문 기사 읽기</span>', '<span>메모 펼치기</span>')
print(f"5.1 Replaced {c5_1} card preview button texts with '메모 펼치기'.")

# 5.2 Modify JS toggle functions: "손글씨 심층 메모 읽기" -> "메모 펼치기"
c5_2 = content.count("'손글씨 심층 메모 읽기'")
content = content.replace("'손글씨 심층 메모 읽기'", "'메모 펼치기'")
print(f"5.2 Replaced {c5_2} JS toggle occurrences with '메모 펼치기'.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated 2026-10-14.html successfully!")
