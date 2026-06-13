import re, shutil

path = r'd:\学在东南\毕业论文\开题\硕论开题报告\ref\citation.bib'
content = open(path, encoding='utf-8').read()

bts = re.findall(r'booktitle\s*=\s*\{([^}]+)\}', content)
# Pattern: ABBR 'YY: Proceedings... or ABBR YY: Proceedings...
prefixed = [b for b in bts if re.match(r"[A-Za-z']+\s+'?\d+\s*:", b)]
print(f'Prefixed booktitles: {len(prefixed)}')
for b in prefixed:
    print(f'  {repr(b[:150])}')
