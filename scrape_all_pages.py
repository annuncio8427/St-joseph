import urllib.request
import ssl
import re
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Search in scraped_home.html for all .php and internal links
with open('scraped_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all links
raw_links = re.findall(r'href=["\']([^"\']+)["\']', html)
pages_to_check = set()
for l in raw_links:
    l = l.strip()
    if not l or l.startswith('#') or l.startswith('javascript') or l.startswith('mailto:') or l.startswith('tel:'):
        continue
    if l.startswith('http') and not 'sjcas.edu.in' in l:
        continue
    # clean relative
    l = l.split('#')[0].split('?')[0]
    if l.endswith('.php') or l.endswith('.html') or not '.' in l.split('/')[-1]:
        pages_to_check.add(l)

# Add standard expected pages for college
standard_pages = [
    'about.php', 'secretary.php', 'principal.php', 'governingbody.php',
    'committees.php', 'extension_act.php', 'courses.php', 'course.php',
    'admission.php', 'admissions.php', 'departments.php', 'department.php',
    'contact.php', 'contact-1.html', 'contact-2.html', 'facilities.php',
    'gallery.php', 'placement.php', 'iqac.php', 'naac.php', 'alumni.php',
    'rules.php', 'faculty.php', 'ug-courses.php', 'pg-courses.php',
    'shift1.php', 'shift2.php', 'campus.php', 'library.php'
]
pages_to_check.update(standard_pages)

os.makedirs('scraped_pages', exist_ok=True)

success_pages = {}

for page in sorted(pages_to_check):
    if page.startswith('http'):
        url = page
        filename = page.split('/')[-1] or 'index.html'
    else:
        url = f"https://sjcas.edu.in/{page.lstrip('/')}"
        filename = page.replace('/', '_')
        if not filename.endswith(('.php', '.html')):
            filename += '.html'

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            if resp.status == 200:
                content = resp.read().decode('utf-8', errors='ignore')
                # check if it's 404 disguised or valid
                if len(content) > 1000 and "404" not in content[:300].lower():
                    filepath = os.path.join('scraped_pages', filename)
                    with open(filepath, 'w', encoding='utf-8') as out_f:
                        out_f.write(content)
                    success_pages[page] = len(content)
                    print(f"[FOUND] {url} -> {len(content)} bytes")
    except Exception as e:
        # print(f"[FAILED] {url}: {e}")
        pass

print(f"\nTotal valid pages scraped: {len(success_pages)}")
