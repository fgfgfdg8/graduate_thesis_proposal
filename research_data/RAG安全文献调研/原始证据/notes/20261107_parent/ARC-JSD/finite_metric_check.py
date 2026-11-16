"""Finite arithmetic audit of printed Appendix L vectors; no author code/model."""
from pathlib import Path
import datetime
import json
import math

P = [0.52, 0.43, 0.05]
Qtail = [0.52, 0.48, 0.0]
Qtop = [0.47, 0.48, 0.05]

def kl(p, q):
    return sum(a * math.log2(a / b) for a, b in zip(p, q) if a > 0)

def jsd(p, q):
    m = [(a + b) / 2 for a, b in zip(p, q)]
    return (kl(p, m) + kl(q, m)) / 2

def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2

def mask(g):
    return 0.7 + 0.3 / (1 + math.exp(-g))

o = dict(
    at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    scope='parent finite arithmetic only; not author implementation or reproduction',
    source='fixed ICLR2026 PDF fd6a666a89b0, Appendix L p29, table4 p9',
    unit='bits', zero_mass_convention='0 log2 0 = 0',
    P=P, Qtail=Qtail, Qtop=Qtop,
    TV_tail=tv(P, Qtail), TV_top=tv(P, Qtop),
    JSD_tail=jsd(P, Qtail), JSD_top=jsd(P, Qtop),
    argmax_P=P.index(max(P)), argmax_tail=Qtail.index(max(Qtail)),
    argmax_top=Qtop.index(max(Qtop)),
    mask_G_minus2=mask(-2), mask_G_0=mask(0), mask_G_plus2=mask(2),
    relative_hallucination_drop_vs_base=(13.4-8.2)/13.4,
    relative_hallucination_drop_vs_random=(12.7-8.2)/12.7,
    author_code_read=False, author_execution=False, reproduction=False,
)
assert all(abs(sum(q)-1) < 1e-12 for q in [P, Qtail, Qtop])
assert o['JSD_tail'] > o['JSD_top']
assert o['argmax_P'] == o['argmax_tail'] != o['argmax_top']
out=Path(__file__).with_name('finite_metric_check.json')
assert not out.exists()
out.write_text(json.dumps(o, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(o, ensure_ascii=False))
