import re
from collections import Counter

BIBFILE = r'd:\学在东南\毕业论文\开题\硕论开题草案\ConnectedPapers-for-Prompt-Injection-Attacks-on-Large-Language-Models%3A-A-Survey-of-Attack-Methods%2C-Root-Causes%2C-and-Defense-Strategies.bib'

# ── Manual key mapping ──────────────────────────────────────────────
# Format: authorYearFirstSubstantiveWord (all lowercase)
# "First word" = first non-stopword from title; acronyms lowercased
KEY_MAP = {
    'geng2025prompt':        'geng2025prompt',
    'zhang2025browsesafe':   'zhang2025browsesafe',
    'maloyan2026prompt':     'maloyan2026prompt',
    'zhu2025miniscope':      'zhu2025miniscope',
    'yin2026pismith':        'yin2026pismith',
    'li2025dynamic':         'li2025drift',          # DRIFT -> drift
    'wang2025defending':     'wang2025defending',
    'bhagwatkar2025indirect':'bhagwatkar2025indirect',
    'zhang2025agents':       'zhang2025agents',
    'shi2025promptarmor':    'shi2025promptarmor',
    'li2026secure':          'li2026secure',
    'mamidwar2025individual':'mamidwar2025beyond',   # "Beyond" is first substantive word
    'yang2025checkpoint':    'yang2025checkpoint',
    'zhu2025provable':       'zhu2025melon',         # MELON -> melon
    'lee2026red':            'lee2026tmap',          # T-MAP -> tmap
    'costa2025securing':     'costa2025securing',
    'zhang2026thinker':      'zhang2026thinker',
    'feng2025testing':       'feng2025tai3',         # TAI3 -> tai3
    'wen2026agentsys':       'wen2026agentsys',
    'pfister2025gandalf':    'pfister2025gandalf',
    'chang2026know':         'chang2026know',
    'pandya2025attention':   'pandya2025attention',
    'geng2026piarena':       'geng2026piarena',
    'ji2025taxonomy':        'ji2025taxonomy',
    'le2026prompt':          'le2026prompt',
    'he2026attriguard':      'he2026attriguard',
    'xiang2026architecting': 'xiang2026architecting',
    'debenedetti2024agentdojo':'debenedetti2024agentdojo',
    'nasr2025attacker':      'nasr2025attacker',
    'walter2025soft':        'walter2025soft',
    'li2026agentdyn':        'li2026agentdyn',
    'kang2025mitigating':    'kang2025mitigating',
    'chen2025meta':          'chen2025metasecalign',  # Meta SecAlign -> metasecalign
    'chhabra2025agentic':    'chhabra2025agentic',
    'evtimov2025benchmarking':'evtimov2025wasp',      # WASP -> wasp
    'christodorescu2025systems':'christodorescu2025systems',
    'shen2026invisible':     'shen2026invisible',
    'ma2025context':         'ma2025context',
    'liu2026redvisor':       'liu2026redvisor',
    'dziemian2026vulnerable':'dziemian2026vulnerable',
    'patlan2025real':        'patlan2025real',
}

# ── Author name fixes (ConnectedPapers encoding issues) ─────────────
AUTHOR_FIXES = {
    "V'aclav":      r"V{\'a}clav",
    "Bazi'nska":    r"Bazi{\'n}ska",
    "Dami'an":      r"Dami{\'a}n",
    "B'eguelin":    r"B{\'e}guelin",
    "Balunovi'c":   r"Balunovi{\'c}",
    "Tram\\`er":    r"Tram{\`e}r",
    "Tram\\`{e}r":  r"Tram{\`e}r",
    "K\\\"opf":     r"K{\"o}pf",
    "K\\\\\"opf":   r"K{\"o}pf",
    "Sa-hana":      "Sahana",
    "&amp;":        r"\&",
}

def fix_special(s):
    """Fix encoding artifacts in author/journal strings."""
    for old, new in AUTHOR_FIXES.items():
        s = s.replace(old, new)
    return s

def parse_field(entry, field):
    """Extract a field value from entry text."""
    m = re.search(rf'\b{field}\s*=\s*\{{(.*?)\}}(?:\s*[,}}])', entry, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None

def convert_entry(entry):
    """Convert a single entry: rename key, fix special chars, ensure proper format."""
    old_key_m = re.match(r'@(\w+)\{([^,]+),', entry)
    if not old_key_m:
        return entry
    etype = old_key_m.group(1)
    old_key = old_key_m.group(2)
    new_key = KEY_MAP.get(old_key, old_key)

    # Parse fields
    title   = parse_field(entry, 'title')
    author  = parse_field(entry, 'author')
    year    = parse_field(entry, 'year')
    journal = parse_field(entry, 'journal')
    volume  = parse_field(entry, 'volume')
    number  = parse_field(entry, 'number')
    pages   = parse_field(entry, 'pages')
    doi     = parse_field(entry, 'doi')

    if not title or not author:
        return entry

    # Fix special chars
    author  = fix_special(author)
    journal = fix_special(journal) if journal else None
    title   = fix_special(title)

    # Determine if arXiv
    is_arxiv = journal and 'arxiv' in journal.lower()

    # Build output
    lines = [f"@article{{{new_key},"]
    lines.append(f"  title={{{title}}},")
    lines.append(f"  author={{{author}}},")
    if journal:
        lines.append(f"  journal={{{journal}}},")
    if volume:
        lines.append(f"  volume={{{volume}}},")
    if number:
        lines.append(f"  number={{{number}}},")
    if pages:
        lines.append(f"  pages={{{pages}}},")
    if year:
        lines.append(f"  year={{{year}}},")
    if doi:
        lines.append(f"  doi={{{doi}}}")
    # Remove trailing comma from last field
    # Find last line that has a comma at the end (before })
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].endswith(','):
            lines[i] = lines[i][:-1]
            break
    lines.append("}")
    return '\n'.join(lines)

# ── Main ────────────────────────────────────────────────────────────
with open(BIBFILE, encoding='utf-8') as f:
    content = f.read()

entries = re.split(r'\n\n(?=@)', content.strip())

converted = []
seen_keys = {}
for e in entries:
    ce = convert_entry(e)
    # Handle duplicate keys
    km = re.match(r'@\w+\{([^,]+),', ce)
    if km:
        k = km.group(1)
        if k in seen_keys:
            seen_keys[k] += 1
            suffix = chr(ord('a') + seen_keys[k] - 1)
            ce = ce.replace(f'{{{k},', f'{{{k}{suffix},', 1)
            k = k + suffix
        else:
            seen_keys[k] = 1
    converted.append(ce)

output = '\n\n'.join(converted) + '\n'

# Verify
all_keys = re.findall(r'@\w+\{([^,]+),', output)
dups = [k for k, v in Counter(all_keys).items() if v > 1]
print(f"Total: {len(all_keys)} entries")
print(f"Duplicates: {dups}")

# Check trailing commas before }
bad = len(re.findall(r',\s*\n\}', output))
print(f"Trailing commas before }}: {bad}")

with open(BIBFILE, 'w', encoding='utf-8', newline='\n') as f:
    f.write(output)
print("Done.")
