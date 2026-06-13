import re, os

parts = [
    'tmp/sec1_p1_intro.tex',
    'tmp/sec1_p2_capability.tex',
    'tmp/sec1_p3_security.tex',
    'tmp/sec1_p4_provenance.tex',
    'tmp/sec1_p5_measurement.tex',
    'tmp/sec1_p6_gaps.tex',
    'tmp/sec1_p7_innovation.tex',
]

combined = []
for p in parts:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove comment header lines
    lines = content.split('\n')
    lines = [l for l in lines if not l.strip().startswith('% =====')]
    combined.append('\n'.join(lines).strip())

full_text = '\n\n'.join(combined)

# Count unique cite keys
all_keys = re.findall(r'\\cite\{([^}]+)\}', full_text)
unique_keys = set()
for k in all_keys:
    for key in k.split(','):
        unique_keys.add(key.strip())

print(f'Total unique cite keys: {len(unique_keys)}')
print('Keys:')
for k in sorted(unique_keys):
    print(' ', k)

# Write to section1_basis.tex
out_path = 'partitions/section1_basis.tex'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text + '\n')

print(f'\nWritten to {out_path}')
print(f'Total lines: {len(full_text.splitlines())}')
