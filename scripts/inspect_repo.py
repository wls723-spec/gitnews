import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def inspect_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'<article class="markdown-body[^>]*>(.*?)</article>', text, re.DOTALL)
    if m:
        # replace common html tags
        clean = re.sub(r'<[^>]+>', ' ', m.group(1))
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(clean[:3000])
    else:
        print("No markdown-body found")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\user\.gemini\antigravity-ide\brain\435add80-f970-4300-aa51-040eb4163a92\.system_generated\steps\57\content.md"
    inspect_file(path)
