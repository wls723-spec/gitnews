import subprocess
from pathlib import Path

html_content = Path("news/2026-10-22.html").read_text(encoding="utf-8")

# Let's see: how many script tags are in news/2026-10-22.html?
# Let's insert a console or body probe right at the very beginning of the HTML, and after each script!

test_html = html_content.replace(
    "<head>",
    "<head><script>window.__STEP = ['START']; window.addEventListener('error', e => window.__STEP.push('ERR:' + e.message));</script>"
)

# Replace the last script to add logging
test_html = test_html.replace(
    "lucide.createIcons();",
    "window.__STEP.push('BEFORE_LUCIDE'); lucide.createIcons(); window.__STEP.push('AFTER_LUCIDE');"
)

# And right before </body>, print __STEP
test_html = test_html.replace(
    "</body>",
    "<script>const d = document.createElement('div'); d.id='STEPS'; d.textContent = JSON.stringify(window.__STEP); document.body.appendChild(d);</script></body>"
)

Path("scratch/test_steps.html").write_text(test_html, encoding="utf-8")

cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    "file:///c:/Program Files/1a/src/gitnews/scratch/test_steps.html"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
dump = res.stdout

for line in dump.split("\n"):
    if 'id="STEPS"' in line:
        print("STEPS RESULT:", line)
