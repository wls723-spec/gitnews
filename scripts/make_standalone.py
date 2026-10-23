import os
import re
import sys
import base64
import mimetypes
from pathlib import Path

# Force UTF-8 output in Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def get_mime_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.jpg', '.jpeg']:
        return 'image/jpeg'
    elif ext == '.png':
        return 'image/png'
    elif ext == '.webp':
        return 'image/webp'
    elif ext == '.svg':
        return 'image/svg+xml'
    elif ext == '.gif':
        return 'image/gif'
    return mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

def file_to_base64(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    mime = get_mime_type(file_path)
    return f"data:{mime};base64,{b64_str}"

def make_html_standalone(input_html_path, output_html_path=None):
    input_path = Path(input_html_path).resolve()
    base_dir = input_path.parent
    
    if output_html_path is None:
        output_path = input_path
    else:
        output_path = Path(output_html_path).resolve()
        
    print(f"📦 Converting to Standalone HTML: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # 1. Inline CSS stylesheets
    def replace_css_link(match):
        rel_href = match.group(1)
        if rel_href.startswith(('http://', 'https://', '//', 'data:')):
            return match.group(0) # Keep external CDNs
            
        css_file = (base_dir / rel_href).resolve()
        if css_file.exists():
            print(f"  [Inlining CSS] {rel_href} ({css_file.stat().st_size:,} bytes)")
            with open(css_file, 'r', encoding='utf-8') as cf:
                css_content = cf.read()
            return f"<style>\n/* Inlined from: {rel_href} */\n{css_content}\n</style>"
        else:
            print(f"  [WARNING CSS NOT FOUND] {rel_href}")
            return match.group(0)

    html = re.sub(r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>', replace_css_link, html, flags=re.IGNORECASE)
    # Also handle href before rel
    html = re.sub(r'<link\s+[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*>', replace_css_link, html, flags=re.IGNORECASE)

    # 2. Inline Javascript files
    def replace_js_script(match):
        rel_src = match.group(1)
        if rel_src.startswith(('http://', 'https://', '//', 'data:')):
            return match.group(0)
            
        js_file = (base_dir / rel_src).resolve()
        if js_file.exists():
            print(f"  [Inlining JS] {rel_src} ({js_file.stat().st_size:,} bytes)")
            with open(js_file, 'r', encoding='utf-8') as jf:
                js_content = jf.read()
            # Prevent accidental </script> termination inside script body
            escaped_js = js_content.replace('</script>', r'<\/script>')
            return f"<script>\n/* Inlined from: {rel_src} */\n{escaped_js}\n</script>"
        else:
            print(f"  [WARNING JS NOT FOUND] {rel_src}")
            return match.group(0)

    html = re.sub(r'<script\s+[^>]*src=["\']([^"\']+)["\'][^>]*>\s*</script>', replace_js_script, html, flags=re.IGNORECASE)

    # 3. Inline images as Base64 Data URIs
    img_count = 0
    def replace_img_src(match):
        nonlocal img_count
        full_tag = match.group(0)
        src = match.group(1)
        
        if src.startswith(('http://', 'https://', '//', 'data:')):
            return full_tag
            
        img_file = (base_dir / src).resolve()
        if img_file.exists():
            data_uri = file_to_base64(img_file)
            img_count += 1
            sz = img_file.stat().st_size
            print(f"  [Inlining Image #{img_count}] {src} ({sz:,} bytes) -> Data URI")
            return full_tag.replace(f'src="{src}"', f'src="{data_uri}"').replace(f"src='{src}'", f'src="{data_uri}"')
        else:
            print(f"  [WARNING IMAGE NOT FOUND] {src}")
            return full_tag

    html = re.sub(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', replace_img_src, html, flags=re.IGNORECASE)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    final_size = output_path.stat().st_size
    print(f"\n✅ Standalone conversion complete: {output_path}")
    print(f"   Final standalone file size: {final_size:,} bytes ({final_size / (1024*1024):.2f} MB)")
    print(f"   Total embedded images: {img_count}")
    return output_path

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html"
    make_html_standalone(target)
