import os
from bs4 import BeautifulSoup

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Remove script/style
    for tag in soup(['script', 'style']):
        tag.decompose()
    return soup.get_text(separator=' ', strip=True)

pages = []
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
        text = extract_text(html)
        title = BeautifulSoup(html, 'html.parser').title.string if BeautifulSoup(html, 'html.parser').title else filename
        pages.append({'title': title, 'path': filename, 'text': text})

with open('search-index.js', 'w', encoding='utf-8') as out:
    out.write('window.SEARCH_INDEX = [\n')
    for page in pages:
        out.write(repr(page).replace("'", '"') + ',\n')
    out.write('];\n')