import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find any fixed min-width or width > 300px
widths = re.findall(r'(\.[a-zA-Z0-9_-]+[^{]*\{[^}]*(?:width|min-width)[^}]*\})', css)
for w in widths:
    if any(k in w for k in ['px', 'rem', 'vw']) and not any(k in w for k in ['16px', '24px', '32px', '40px', '48px', '50px', '52px', '54px', '56px', '58px', '60px', '64px', '68px', '96px', '100px']):
        print("--- MATCH ---")
        print(w.strip())

