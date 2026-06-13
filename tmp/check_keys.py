import re
with open('ref/citation.bib','r',encoding='utf-8') as f: content=f.read()
keys_to_check = ['inam2023sok','zhang2024injectagent','liu2024formalizing','chen2025struq','zverev2025can','bi2024backdoor','wang2024codeact','chen2025can','abdelnabi2025drift','wang2025webinject','shi2026pitoolselection','li2026ace','an2025ipiguard','li2025piguard','zhan2025adaptive','hung2025attention','greshake2023proceedings','chhabra2025agentic','andriushchenko2025jailbreaking','yi2024survey','das2025security','wu2025isolategpt','wang2025agentvigil','greshake2023notwhat3','weidinger2022taxonomy','schulhoff2023ignore','yu2025survey','zhang2025memory']
for k in keys_to_check:
    found = k in content
    status = 'YES' if found else 'NO'
    print(k + ': ' + status)
