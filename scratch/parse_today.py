import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def parse_gh(path, label):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return

    items = re.findall(r'<article class="Box-row"[^>]*>(.*?)</article>', text, re.DOTALL)
    if not items:
        items = re.findall(r'<article[^>]*>(.*?)</article>', text, re.DOTALL)
    print(f"\n=== {label} (Found {len(items)}) ===")
    for i, it in enumerate(items):
        repo = re.search(r'href="/([a-zA-Z0-9_\.-]+/[a-zA-Z0-9_\.-]+)"', it)
        repo_name = repo.group(1) if repo else "unknown"
        if any(x in repo_name for x in ['sponsors/', 'apps/', 'features/', 'trending/']):
            continue
        desc = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', it, re.DOTALL)
        if not desc:
            desc = re.search(r'<p[^>]*>(.*?)</p>', it, re.DOTALL)
        desc_text = desc.group(1).strip() if desc else ""
        desc_text = re.sub(r'<[^>]+>', '', desc_text).strip()
        stars_today = re.search(r'([0-9,]+)\s+stars\s+today', it, re.IGNORECASE)
        stars_str = stars_today.group(1) if stars_today else "?"
        total_stars = re.search(r'href="/[^/]+/[^/]+/stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
        tot_str = total_stars.group(1).strip() if total_stars else "?"
        lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
        lang_str = lang.group(1).strip() if lang else "General"
        print(f"[{i+1}] {repo_name} ({lang_str}) | +{stars_str} today | total: {tot_str}")
        print(f"    {desc_text[:140]}")

parse_gh(r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\39\content.md", "Python Trending")
parse_gh(r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\43\content.md", "Rust Trending")

# HF Papers
hf_path = r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\41\content.md"
try:
    with open(hf_path, "r", encoding="utf-8") as f:
        hf_text = f.read()
    print("\n=== Hugging Face Daily Papers ===")
    matches = re.findall(r'<h3[^>]*>.*?<a[^>]*href="\/papers\/([0-9\.]+)"[^>]*>(.*?)<\/a>', hf_text, re.DOTALL)
    if not matches:
        matches = re.findall(r'href="\/papers\/([0-9\.]+)"', hf_text)
        print("Paper IDs:", list(dict.fromkeys(matches))[:10])
    else:
        seen = set()
        for pid, title in matches:
            clean = re.sub(r'<[^>]+>', '', title).strip()
            if pid not in seen and len(clean) > 3:
                seen.add(pid)
                print(f"[{pid}] {clean}")
except Exception as e:
    print(f"HF error: {e}")
