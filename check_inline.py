import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check inline styles in index.html
inline_styles = re.findall(r'style=["\']([^"\']+)["\']', html)
for s in inline_styles:
    if any(k in s for k in ['min-width', 'width:']):
        print("Inline style:", s)

