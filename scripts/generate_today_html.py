import os
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of news/2026-10-23.html...")

# Helper to build schematic
def make_schematic(title, tag, steps):
    step_boxes = []
    for idx, (step_title, step_desc) in enumerate(steps, 1):
        step_boxes.append(f"""
            <div class="schematic-box step-{idx}">
              <div class="step-tag">PHASE {idx}. {step_title}</div>
              <div class="step-title">{step_title}</div>
              <div class="step-desc">{step_desc}</div>
            </div>""")
    boxes_html = "\n".join(step_boxes)
    return f"""
        <div class="schematic-container">
          <div class="schematic-header">
            <span><i data-lucide="cpu" style="color:#f59e0b;"></i> {title}</span>
            <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">{tag}</span>
          </div>
          <div class="schematic-grid">
            {boxes_html}
          </div>
        </div>"""

print("Helper ready.")
