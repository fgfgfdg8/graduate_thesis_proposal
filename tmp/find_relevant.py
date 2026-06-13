import re

with open('ref/citation.bib','r',encoding='utf-8') as f:
    content = f.read()

entries = re.findall(r'@\w+\{([^,]+),', content)
print(f'Total entries: {len(entries)}')

# Parse entries
pattern = re.compile(r'(@\w+\{([^,\n]+),[\s\S]*?^\})', re.MULTILINE)
formal = []
for m in pattern.finditer(content):
    entry = m.group(1)
    key = m.group(2).strip()
    has_booktitle = 'booktitle' in entry.lower()
    has_journal = 'journal' in entry.lower()
    is_arxiv = bool(re.search(r'journal\s*=\s*[{"].*?[Aa]r[Xx]iv', entry))
    if (has_booktitle or has_journal) and not is_arxiv:
        title_m = re.search(r'title\s*=\s*\{(.*?)\}', entry, re.IGNORECASE)
        title = title_m.group(1)[:60] if title_m else ''
        venue_m = re.search(r'(?:booktitle|journal)\s*=\s*\{(.*?)\}', entry, re.IGNORECASE)
        venue = venue_m.group(1)[:50] if venue_m else ''
        formal.append((key, title, venue))

keywords = ['agent','tool','provok','inject','attack','defense','llm','language','graph','trace','security','audit','benchmark','prompt','survey','risk']
relevant = [(k,t,v) for k,t,v in formal if any(kw in t.lower() or kw in k.lower() for kw in keywords)]
print(f'Formally published relevant entries: {len(relevant)}')
for k,t,v in relevant:
    print(f'  {k}: {t[:55]} | {v[:40]}')
