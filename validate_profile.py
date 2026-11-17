import re
import os
import xml.etree.ElementTree as ET
import urllib.request

REPO_DIR = "/home/shaber/.gemini/antigravity/scratch/shabermohamadb"
README_PATH = os.path.join(REPO_DIR, "README.md")
ASSETS_DIR = os.path.join(REPO_DIR, "assets")

print("=== STARTING PROFILE VERIFICATION ===")

# 1. Verify all SVGs in assets
svgs = [f for f in os.listdir(ASSETS_DIR) if f.endswith(".svg")]
print(f"Total SVGs found in assets: {len(svgs)}")
for svg in sorted(svgs):
    svg_path = os.path.join(ASSETS_DIR, svg)
    try:
        ET.parse(svg_path)
        print(f"  [OK] XML Valid: {svg} ({os.path.getsize(svg_path)} bytes)")
    except Exception as e:
        print(f"  [FAIL] XML Broken in {svg}: {e}")

# 2. Verify all local asset links referenced in README.md
with open(README_PATH, "r", encoding="utf-8") as f:
    readme_content = f.read()

local_assets = re.findall(r'assets/([a-zA-Z0-9_\-]+\.svg)', readme_content)
print(f"\nLocal assets referenced in README: {len(set(local_assets))}")
for asset in sorted(set(local_assets)):
    full_path = os.path.join(ASSETS_DIR, asset)
    if os.path.exists(full_path):
        print(f"  [OK] Found on disk: assets/{asset}")
    else:
        print(f"  [FAIL] Missing asset: assets/{asset}")

# 3. Verify external URLs referenced in README.md
external_urls = re.findall(r'https?://[^\s)"\'><]+', readme_content)
print(f"\nExternal URLs referenced in README: {len(set(external_urls))}")
for url in sorted(set(external_urls)):
    # Clean trailing punctuation
    url = url.rstrip('.,;:')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as resp:
            print(f"  [HTTP {resp.status}] {url[:70]}")
    except Exception as e:
        print(f"  [FAIL {e}] {url[:70]}")

print("\n=== PROFILE VERIFICATION COMPLETE ===")
