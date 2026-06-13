import re
with open('ref/citation.bib','r',encoding='utf-8') as f: content=f.read()
# Keys to add (not yet in section1)
candidates = ['gu2024agent','dong2025philosopher','shi2024optimization','tsai2025contextual','chen2023fireact','hong2024cogagent','qiao2025worfbench','an2025rag','wang2024large','zhang2024defending','cheng2024kairos']
for k in candidates:
    if k in content:
        m = re.search(r'@\w+\{' + re.escape(k) + r',[\s\S]*?title\s*=\s*\{(.*?)\}', content)
        title = m.group(1)[:70] if m else '?'
        vm = re.search(r'@\w+\{' + re.escape(k) + r',[\s\S]*?(?:booktitle|journal)\s*=\s*\{(.*?)\}', content)
        venue = vm.group(1)[:60] if vm else '?'
        print(k + ': ' + title + ' | ' + venue)
    else:
        print(k + ': NOT FOUND')
