import glob

mobile_bar_snippet = '''  <!-- Mobile Bottom Action Bar (Sticky Mobile Speed Actions) -->
  <div class="mobile-bottom-bar" aria-label="Mobile Speed Actions">
    <div class="mobile-bottom-actions">
      <a href="tel:+917305088202" class="btn btn-outline btn-sm" style="font-size: 0.82rem;">
        <i class="fas fa-phone-alt"></i> Call Us
      </a>
      <a href="https://docs.google.com/forms/d/e/1FAIpQLScLhklakSKkZHLRGe_U0IObBUgWUsLnIZfnJ0RVahQJ35N6Jw/viewform" target="_blank" class="btn btn-secondary btn-sm" style="font-size: 0.82rem;">
        <i class="fas fa-paper-plane"></i> Apply Online
      </a>
    </div>
  </div>
'''

for path in glob.glob('*.html'):
    if path.startswith('scraped'): continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'mobile-bottom-bar' not in content and '</body>' in content:
        content = content.replace('</body>', mobile_bar_snippet + '\n</body>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added mobile bar to {path}")
    else:
        print(f"Skipped {path} (already has bar)")

