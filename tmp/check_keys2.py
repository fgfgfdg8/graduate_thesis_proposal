import re
with open('ref/citation.bib','r',encoding='utf-8') as f: content=f.read()
keys_to_check = ['wang2024survey_agents','rebedea2023nemo','chen2024agentpoison','gu2024agent','dong2025philosopher','pearce2025asleep','shi2024optimization','zhang2025traceback','bagdasarian2024airgapagent','wang2024autored','ma2024combining','wang2025protect','tsai2025contextual','weidinger2022taxonomy']
for k in keys_to_check:
    found = k in content
    # get title
    if found:
        m = re.search(r'@\w+\{' + re.escape(k) + r',[\s\S]*?title\s*=\s*\{(.*?)\}', content)
        title = m.group(1)[:60] if m else '?'
        vm = re.search(r'@\w+\{' + re.escape(k) + r',[\s\S]*?(?:booktitle|journal)\s*=\s*\{(.*?)\}', content)
        venue = vm.group(1)[:50] if vm else '?'
        print(k + ': YES | ' + title + ' | ' + venue)
    else:
        print(k + ': NO')
