# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

class DynamicSearchWindow:
    def __init__(self, last_date_str, now_dt=None, buffer_hours=6, min_window_hours=30):
        self.now = now_dt or datetime.now(timezone.utc)
        
        # Parse last published date (YYYY-MM-DD assumed at 00:00:00 UTC)
        self.last_date = datetime.strptime(last_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        
        # Calculate raw gap in hours
        self.raw_gap_hours = max((self.now - self.last_date).total_seconds() / 3600.0, 0.0)
        self.gap_days = (self.now.date() - self.last_date.date()).days
        
        # Dynamic search window W
        self.window_hours = round(max(self.raw_gap_hours + buffer_hours, min_window_hours), 1)
        self.since_dt = self.now - timedelta(hours=self.window_hours)
        self.since_iso = self.since_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.since_timestamp = int(self.since_dt.timestamp())
        
        # 3-Bucket Split (W / 3)
        self.bucket_step = round(self.window_hours / 3.0, 1)
        self.b1_range = (0.0, self.bucket_step)
        self.b2_range = (self.bucket_step, self.bucket_step * 2)
        self.b3_range = (self.bucket_step * 2, self.window_hours)
        
        # Formatted labels for UI badges
        def fmt_range(r):
            s = int(r[0]) if r[0].is_integer() else r[0]
            e = int(r[1]) if r[1].is_integer() else r[1]
            return f"{s}~{e}h"
            
        self.b1_label = fmt_range(self.b1_range)
        self.b2_label = fmt_range(self.b2_range)
        self.b3_label = fmt_range(self.b3_range)

    def summary(self):
        return (
            f"=== DYNAMIC SEARCH WINDOW ===\n"
            f"Last Published Date: {self.last_date.strftime('%Y-%m-%d')} (Gap: {self.gap_days} days / {self.raw_gap_hours:.1f}h)\n"
            f"Target Search Window (W): {self.window_hours} hours (Since: {self.since_iso})\n"
            f"3-Bucket Split: [{self.b1_label}] (0~1/3) | [{self.b2_label}] (1/3~2/3) | [{self.b3_label}] (2/3~1)\n"
            f"Need Weekly Trending: {'YES (Gap >= 2 days)' if self.gap_days >= 2 else 'NO (Daily sufficient)'}\n"
        )

def get_last_published_date(seen_file_path=None):
    if seen_file_path:
        seen_file = Path(seen_file_path)
    else:
        seen_file = Path(__file__).resolve().parent.parent / "history_seen_projects.md"

    if not seen_file.exists():
        return "2026-11-04"
    
    with open(seen_file, "r", encoding="utf-8") as f:
        text = f.read()
        
    dates = re.findall(r'\*\*(\d{4}-\d{2}-\d{2})\*\*', text)
    if dates:
        # Return latest date
        return sorted(dates)[-1]
    return "2026-11-04"

def get_dynamic_window(now_dt=None, seen_file_path=None):
    last_date = get_last_published_date(seen_file_path)
    return DynamicSearchWindow(last_date, now_dt=now_dt)

if __name__ == '__main__':
    win = get_dynamic_window()
    print(win.summary())
