import subprocess

html = '<html><body><script>document.body.innerHTML += "<h1>HELLO_JS</h1>";</script></body></html>'
with open('scratch/mini.html', 'w', encoding='utf-8') as f:
    f.write(html)

cmd = [r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', '--headless=new', '--disable-gpu', '--dump-dom', 'file:///c:/Program Files/1a/src/gitnews/scratch/mini.html']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print('Mini result:', res.stdout)
