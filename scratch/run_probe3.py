import subprocess
from pathlib import Path

html_content = Path("news/2026-10-22.html").read_text(encoding="utf-8")

probe_code = """
  <script>
    (function() {
      try {
        const item = document.querySelector('.minor-item');
        const detail = item.querySelector('.minor-detail-content');
        const btnText = item.querySelector('.minor-btn-text');
        
        const b4_display = window.getComputedStyle(detail).display;
        const b4_text = btnText.textContent;
        
        // Dispatch actual click event
        item.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        
        const after_display = window.getComputedStyle(detail).display;
        const after_text = btnText.textContent;
        
        // Dispatch click again to test collapsing
        item.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        
        const collapsed_display = window.getComputedStyle(detail).display;
        const collapsed_text = btnText.textContent;
        
        // Test global toggle all
        toggleAllArticles();
        const all_display = window.getComputedStyle(detail).display;
        
        const testResult = document.createElement('div');
        testResult.id = 'CLICK_PROBE_RESULT';
        testResult.textContent = `B4=${b4_display}(${b4_text}) -> CLICK=${after_display}(${after_text}) -> COLLAPSE=${collapsed_display}(${collapsed_text}) -> ALL=${all_display}`;
        document.body.appendChild(testResult);
      } catch (err) {
        const errDiv = document.createElement('div');
        errDiv.id = 'CLICK_PROBE_ERROR';
        errDiv.textContent = 'ERR: ' + err.toString();
        document.body.appendChild(errDiv);
      }
    })();
  </script>
"""

test_html = html_content.replace("</body>", f"{probe_code}</body>")
test_file = Path("scratch/test_probe3.html")
test_file.write_text(test_html, encoding="utf-8")

cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    f"file:///{test_file.resolve()}".replace("\\", "/")
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
dump = res.stdout

for line in dump.split("\n"):
    if "CLICK_PROBE_RESULT" in line and "<script" not in line and "function" not in line:
        print("CLICK TEST:", line)
