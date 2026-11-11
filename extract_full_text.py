import os
from html.parser import HTMLParser

class CleanText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style']:
            self.skip = True
        elif tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'br', 'tr']:
            self.text.append('\n')

    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.skip = False
        elif tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr']:
            self.text.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)

with open('full_extracted_details.txt', 'w', encoding='utf-8') as out:
    for fname in sorted(os.listdir('scraped_pages')):
        with open(os.path.join('scraped_pages', fname), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        p = CleanText()
        p.feed(content)
        t = '\n'.join([line.strip() for line in ''.join(p.text).splitlines() if line.strip()])
        out.write(f"\n\n=================== FILE: {fname} ===================\n\n")
        out.write(t)

print("Saved to full_extracted_details.txt")

