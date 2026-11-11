import re
import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

all_imgs = set()
for fname in os.listdir('scraped_pages'):
    with open(os.path.join('scraped_pages', fname), 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.I)
    for img in imgs:
        img = img.strip()
        if img:
            all_imgs.add(img)

print("Found image URLs:", len(all_imgs))
os.makedirs('downloaded_assets', exist_ok=True)

downloaded = []
for img in sorted(all_imgs):
    if img.startswith('http'):
        url = img
    else:
        url = f"https://sjcas.edu.in/{img.lstrip('/')}"
    
    local_name = img.replace('/', '_').replace('\\', '_')
    if '?' in local_name:
        local_name = local_name.split('?')[0]
    
    print(f"Trying: {url} -> {local_name}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            if r.status == 200:
                data = r.read()
                if len(data) > 500:
                    with open(os.path.join('downloaded_assets', local_name), 'wb') as out_f:
                        out_f.write(data)
                    downloaded.append((local_name, len(data)))
    except Exception as e:
        # print("Error:", e)
        pass

print(f"Successfully downloaded {len(downloaded)} assets.")
for name, size in downloaded:
    print(f"  {name} ({size} bytes)")

