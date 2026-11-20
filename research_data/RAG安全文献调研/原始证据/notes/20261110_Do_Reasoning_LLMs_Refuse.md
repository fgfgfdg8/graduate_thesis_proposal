# Do Reasoning LLMs Refuse What They Infer in Long Contexts?

## Bibliographic record

- Authors (local PDF order): Yu Fu; Haz Sameen Shahgir; Zhipeng Wei; Huanli Gong; N. Benjamin Erichson; Yue Dong.
- Version: arXiv:2602.08874v2, updated 2026-05-14, 33 pages.
- Venue signal: NeurIPS 2026 official Downloads entry; poster #149897. The specific track has not been independently confirmed, so no paper-level CCF-A label is assigned.
- Local PDF: [stored copy](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Do Reasoning LLMs Refuse What They Infer in Long Contexts_.pdf>).
- SHA-256: `452BAA581940113D5521F4E05584FEA723811214CFBF4CEB65132CE046F6EA42`.
- Artifact: [author code and data repository](https://github.com/FYYFU/long_context_composition_attack). README reports 179/180 table cells matching; the sole discrepancy is Gemini-3-Flash Direct Retrieval/0k (paper 100%, archived-score recomputation 99%). Not independently rerun; weight license not checked.
- Citation count: not observed.

## Mechanism and evidence

The threat model decomposes a harmful objective into semantically incomplete fragments embedded in a long context, while the final query remains neutral. A model must retrieve, compose, and infer the implied goal. The paper evaluates Direct Retrieval, Single-hop Aggregation, Chain Reasoning, and Multi-hop Deductive Reasoning across 15 frontier models and contexts up to 64k tokens. Refusal drops when the harmful objective must be reconstructed compositionally; this is a direct precedent for distributed intent and semantic composition.

## Relevance and limits

This work narrows broad novelty claims about combining individually benign-looking fragments. It does not use a persistent RAG corpus, a real retrieval pipeline, an unknown victim chunker, or chunk-level counterfactuals proving that distinct same-source chunks are jointly necessary. It is therefore a compositional-reasoning security neighbor, not a complete collision with the proposed corpus-poisoning experiment.

## Sources

- [arXiv version](https://arxiv.org/abs/2602.08874)
- [NeurIPS 2026 Downloads](https://neurips.cc/Downloads/2026)
