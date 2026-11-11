import urllib.request
import urllib.parse
import ssl
import re
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('scraped_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract text paragraphs and headings
headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', html, re.I | re.S)
clean_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings if re.sub(r'<[^>]+>', '', h).strip()]

print("--- HEADINGS ---")
for h in clean_headings[:25]:
    print("-", h)

# Extract navigation links
link_pattern = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', re.I | re.S)
links = link_pattern.findall(html)
clean_links = {}
for href, text in links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    clean_text = ' '.join(clean_text.split())
    if clean_text and href not in ['#', 'javascript:void(0);', '']:
        clean_links[href] = clean_text

print("\n--- DISTINCT LINKS ---")
for href, text in list(clean_links.items())[:35]:
    print(f"{text} ===> {href}")

# Check for phone numbers, emails, addresses
emails = set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', html))
phones = set(re.findall(r'(?:\+?91[\-\s]?)?[6-9]\d{9}|(?:\d{3,5}[\-\s]?\d{6,8})', html))
print("\n--- CONTACT INFO IN HOME ---")
print("Emails:", emails)
print("Phones:", phones)

# Check images
images = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html, re.I)
print("\n--- IMAGES (Sample) ---")
for img in images[:15]:
    print(img)

