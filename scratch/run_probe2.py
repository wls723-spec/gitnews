import subprocess
from pathlib import Path

html_content = Path("news/2026-10-22.html").read_text(encoding="utf-8")

probe_code = """
  <script>
    (function() {
      try {
        const firstMinor = document.querySelector('.minor-item');
        const detail = firstMinor.querySelector('.minor-detail-content');
        const styleBefore = window.getComputedStyle(detail).display;
        
        // Call toggleMinorItem directly!
        toggleMinorItem(firstMinor);
        
        const styleAfter = window.getComputedStyle(detail).display;
        const hasActiveClass = firstMinor.classList.contains('active');
        
        const testResult = document.createElement('div');
        testResult.id = 'BROWSER_PROBE_RESULT';
        testResult.textContent = 'BEFORE=' + styleBefore + ' | AFTER=' + styleAfter + ' | ACTIVE=' + hasActiveClass;
        document.body.appendChild(testResult);
      } catch (err) {
        const errDiv = document.createElement('div');
        errDiv.id = 'BROWSER_PROBE_ERROR';
        errDiv.textContent = 'ERROR: ' + err.toString();
        document.body.appendChild(errDiv);
      }
    })();
  </script>
"""

test_html = html_content.replace("</body>", f"{probe_code}</body>")
test_file = Path("scratch/test_probe2.html")
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
    if "BROWSER_PROBE" in line and "<script" not in line and "function" not in line:
        print("FOUND RESULT LINE:", line)
