# Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data

## Identity

- Authors: Shenglai Zeng; Jiankun Zhang; Pengfei He; Jie Ren; Tianqi Zheng; Hanqing Lu; Han Xu; Hui Liu; Yue Xing; Jiliang Tang.
- Venue: EMNLP 2025 Main, pp. 24527–24558; DOI `10.18653/v1/2025.emnlp-main.1247`; arXiv:2406.14773. Under the supplied CCF 7th-edition catalogue, EMNLP Main is CCF-B.
- Official record and PDF: https://aclanthology.org/2025.emnlp-main.1247/ and https://aclanthology.org/2025.emnlp-main.1247.pdf.
- Official BibTeX key: `zeng-etal-2025-mitigating`.
- Local PDF: `D:\学在东南\科研数据库\20_Research\Papers\RAG安全文献\Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data.pdf`; 32 pages, 536,674 bytes, SHA-256 `3064F65A91AA68874FE7F62CD9115A79D4E490DE9E8AF57A59CDE9558643A85B`.
- Code: https://github.com/phycholosogy/RAG-SAGE. The paper PDF appears to misspell the owner as `phycolosogy`; the reachable repository uses `phycholosogy`. Repository contents and license were not audited, and code was not run.
- Reading: physical pages 1–32, including main text, tables, references and appendices; L3. No independent replication.

## Method and Evidence

SAGE replaces the original retrieval corpus with generated synthetic data. Its pipeline extracts attributes and generates synthetic records, then uses an iterative privacy-agent rewrite stage to reduce recoverable private content while retaining task utility. This is data-level privacy mitigation, not a detector for malicious or poisoned retrieved passages.

In the 250-prompt targeted-attack evaluation (Table 3), Stage 2 reports zero targeted-information items in all four settings; `Target-wiki-GPT-3.5` still has 7 repeated prompts. Stage 2's untargeted-attack counts in Table 4 are zero. These results are not a formal zero-leakage guarantee. In the separate 100-sample worst-case direct-overlap analysis (Appendix A.5, Table 8), the authors report one targeted-information item for HealthCareMagic and one ROUGE-based context-overlap item. These are distinct metrics and should not be pooled. Utility comparisons are mixed across datasets rather than uniformly better than the original corpus.

## Limits and Relevance

- SAGE is not a formal differential-privacy mechanism; the paper leaves strict differential privacy as future work.
- The preprocessing workflow sends original records to its language-model components. For a hosted model, raw-data handling and retention are part of the trust boundary; provider-side handling is not evaluated in the paper.
- It is a close RAG-privacy and corpus-substitution defense reference, but it does not model attacker-authored poisoning, source authenticity, malicious-block detection, or clean-query false-removal calibration. It constrains broad novelty claims about privacy-preserving replacement of RAG corpora, not the thesis's poisoning/detection niche as currently defined.
- Google Scholar citations were not observed; priority inputs and ranking have not been computed.
