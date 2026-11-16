---
tags: [rag-security-evidence, cross-domain-neighbor]
reading_level: L3
checked_date: 2026-11-14
---

# Explainability-Guided Untargeted Attacks on Knowledge Graph Embedding

> **2026-11-15复核范围：** 本次核对本地PDF首末页、版本标识、页数、已有哈希和可验证链接；既有阅读记录未因本次复核扩大。

## Formal identity and reading scope

- **Authors:** Yawei Lin; Hao Yu; Ke Liang; Mengzhu Wang; Liang Yang; Xinwang Liu.
- **Venue:** IEEE *Transactions on Information Forensics and Security*, vol. 21, 2026, pp. 5133–5148; DOI `10.1109/TIFS.2026.3689651`; CCF-A under the supplied seventh-edition directory.
- **Version read:** IEEE publisher-final PDF, all 16 physical pages; L3. No independent proof audit or implementation run.
- **Local PDF:** [Research database copy](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Explainability-Guided Untargeted Attacks on Knowledge Graph Embedding.pdf>); SHA-256 `951C87765FD4F48C4C00F2AE9A0F6F0AA7E82E50B66336FF7DC936E2F24B5C93`.
- **Citation count:** not observed. No code repository was validated in this reading record.

## Method and findings

PathAttack uses explainability signals to select knowledge-graph triples for untargeted attacks on knowledge-graph embedding link prediction. Its operations delete influential triples or inject malicious triples to degrade prediction. The paper discusses possible implications for GraphRAG, but its experiments do not include a RAG retriever, GraphRAG generation endpoint, text-document corpus, or chunking pipeline.

## Relation to the thesis

- **A:** It is a graph-structure integrity neighbor, not an attack on a long natural-language source or on chunks produced by a victim's unknown chunker. It does not test same-query co-retrieval or joint necessity of same-source chunks.
- **B:** It is an attack, not a detector or filter. It reports no malicious-document classification, clean-query false-deletion calibration, or QA utility after query-level OR deletion.
- **Scope:** Treat it as a CCF-A cross-domain graph attack and threat-model reference. Its possible GraphRAG impact is a discussion point, not an experimentally established RAG result.

## Sources and cross-references

- DOI registration metadata: [Crossref record](https://api.crossref.org/works/10.1109/TIFS.2026.3689651), containing IEEE-deposited title, authors, volume and pages. On 2026-11-15 the DOI redirected to IEEE Xplore article 11503437, which returned an empty HTTP 202 response; the publisher page could not be rechecked. The [homepage of the first author](https://linyawei1127.github.io/) lists the paper; it is not the publisher full text.
- Metadata and issue-scan record: [TIFS 2026 index 355](../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261114-tifs26-355).
- Evidence-map record: [PathAttack](../../../../docs/RAG安全证据地图_20261102.md#src-20261114-tifs26-pathattack).
- Comparative discussion: [RAG-security neighbors](../../../../docs/RAG安全文献攻防技术手段总结报告.md#src-fb1682dc8e7f28a5-h111).
