import os
import re
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
        self.in_script_or_style = False

    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style', 'noscript']:
            self.in_script_or_style = True
        elif tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'div']:
            self.fed.append('\n')

    def handle_endtag(self, tag):
        if tag in ['script', 'style', 'noscript']:
            self.in_script_or_style = False
        elif tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr']:
            self.fed.append('\n')

    def handle_data(self, d):
        if not self.in_script_or_style:
            self.fed.append(d)

    def get_text(self):
        return ''.join(self.fed)

for fname in os.listdir('scraped_pages'):
    fpath = os.path.join('scraped_pages', fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    extractor = HTMLTextExtractor()
    extractor.feed(content)
    text = extractor.get_text()
    # clean lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean_content = '\n'.join(lines)
    print(f"==================== {fname} ====================")
    print(clean_content[:1500])
    print("\n...\n")

