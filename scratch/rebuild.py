import json
import re

with open(r'c:\Program Files\1a\src\gitnews\scratch\step229.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open(r'C:\Users\user\.gemini\antigravity-ide\brain\a1fb9932-b132-42a9-b26f-a34da1d87626\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        idx = obj.get('step_index')
        if 230 <= idx < 502:
            for c in obj.get('tool_calls', []):
                if c['name'] == 'replace_file_content':
                    target = c['args']['TargetContent']
                    repl = c['args']['ReplacementContent']
                    if target in content:
                        content = content.replace(target, repl, 1)
                        print(f'Applied step {idx}')
                    else:
                        print(f'FAILED to find target in step {idx}')

# Apply memo theme
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

with open(r'c:\Program Files\1a\src\gitnews\scratch\pristine_memo.html', 'w', encoding='utf-8') as out:
    out.write(content)

print('Pristine memo created successfully! Length:', len(content), f'Head: {c1}, Header: {c2}, Scripts: {c3}')
