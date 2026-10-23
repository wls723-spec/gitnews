import subprocess
from pathlib import Path

html_content = Path("news/2026-10-22.html").read_text(encoding="utf-8")

# Inject a test probe at the end of the script
probe_code = """
  <script>
    window.addEventListener('DOMContentLoaded', () => {
      try {
        const firstMinor = document.querySelector('.minor-item');
        const detail = firstMinor.querySelector('.minor-detail-content');
        const styleBefore = window.getComputedStyle(detail).display;
        
        // Trigger toggle
        firstMinor.click();
        
        const styleAfter = window.getComputedStyle(detail).display;
        const hasActiveClass = firstMinor.classList.contains('active');
        
        const testResult = document.createElement('div');
        testResult.id = 'BROWSER_PROBE_RESULT';
        testResult.setAttribute('data-style-before', styleBefore);
        testResult.setAttribute('data-style-after', styleAfter);
        testResult.setAttribute('data-has-active', hasActiveClass);
        testResult.textContent = `BEFORE=${styleBefore} | AFTER=${styleAfter} | ACTIVE=${hasActiveClass}`;
        document.body.appendChild(testResult);
      } catch (err) {
        const errDiv = document.createElement('div');
        errDiv.id = 'BROWSER_PROBE_ERROR';
        errDiv.textContent = err.toString();
        document.body.appendChild(errDiv);
      }
    });
  </script>
"""

test_html = html_content.replace("</body>", f"{probe_code}</body>")
test_file = Path("scratch/test_probe.html")
test_file.write_text(test_html, encoding="utf-8")

# Run edge headless to dump DOM
cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    f"file:///{test_file.resolve()}".replace("\\", "/")
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
dump = res.stdout

if "BROWSER_PROBE_RESULT" in dump:
    import re
    match = re.search(r'<div id="BROWSER_PROBE_RESULT"[^>]*>(.*?)</div>', dump)
    print("PROBE RESULT:", match.group(0) if match else "Found tag without match")
elif "BROWSER_PROBE_ERROR" in dump:
    import re
    match = re.search(r'<div id="BROWSER_PROBE_ERROR"[^>]*>(.*?)</div>', dump)
    print("PROBE ERROR:", match.group(0) if match else "Error found")
else:
    print("Probe element not found in dump!")
    print("Dump snippet:", dump[-500:])
