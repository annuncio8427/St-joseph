import glob
import re

brand_regex = re.compile(
    r'<a href="index\.html" class="brand-wrapper"[^>]*>.*?</a>',
    re.DOTALL
)

replacement = '''<a href="index.html" class="brand-wrapper" title="St. Joseph College of Arts and Science">
        <img src="assets/images/logo.png" alt="St. Joseph College of Arts and Science" class="brand-logo">
        <div class="brand-location-badge">
          <span class="loc-place"><i class="fas fa-map-marker-alt"></i> Tenkasi</span>
          <span class="loc-meta">MSU Affiliated</span>
        </div>
      </a>'''

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = brand_regex.subn(replacement, content, count=1)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated brand header in {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

