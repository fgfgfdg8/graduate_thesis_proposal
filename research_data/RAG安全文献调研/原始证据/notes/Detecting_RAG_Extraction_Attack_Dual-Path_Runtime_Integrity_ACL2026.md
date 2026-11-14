# Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game

## Identity

- Authors: Yuanbo Xie; Yingjie Zhang; Yulin Li; Shouyou Song; Xiaokun Chen; Zhihan Liu; Liya Su; Tingwen Liu.
- Venue: ACL 2026 Main, Long Papers, pp. 8503–8518. CCF-A under the user-provided CCF 7th-edition catalogue. DOI: 10.18653/v1/2026.acl-long.385.
- Official record: https://aclanthology.org/2026.acl-long.385/
- Official PDF: https://aclanthology.org/2026.acl-long.385.pdf
- Local PDF: Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game.pdf, 16 pages, 1,603,623 bytes, SHA-256 40B13F40097A17A9EA64D4F607D5DF82D30FE65596D8BFD0C687E333BA7DD45C.
- Reading: physical PDF pages 1–16, including tables, appendices and figures; L3. No code execution or replication. No author code repository was identified in the official record or PDF.

## Threat Model and Mechanism

The attacker aims to reconstruct a black-box RAG knowledge base through iterative queries, without direct access to the database, retriever or system prompt. The experiments cap each attack at 1,500 attempts. The defense inserts random high-entropy canaries into retrieved chunks, monitors streaming generation and stops release after detection; deployment therefore requires control over the final model context and output stream.

CanaryRAG runs two opposing tasks. The real user-query path should never emit a canary; the parallel oracle path should recover canaries from an explicit leakage probe. A canary emitted on the user path or recovered below the oracle threshold signals an integrity violation. The dual paths are two generation tasks, not separate retrieval and generation modules.

## Evaluation

Three agents were tested: ChatDoctor, Mini-Wikipedia and Mini-BioASQ, each with 500 sampled chunks. Attackers were Pirates and RAG-Thief/CopyBreakRAG; defenses compared were no defense, reranking, summarization, RAGFort and CanaryRAG. Chunk Recovery Rate (CRR) counts a recovered chunk only when ROUGE-L >0.5 and cosine similarity under the agent's retrieval embedding model >0.85.

CRR (% mean ± SD; lower is better):

| Agent / attack | No defense | Reranker | Summarize | RAGFort | CanaryRAG |
|---|---:|---:|---:|---:|---:|
| ChatDoctor / Pirates | 97.4±1.0 | 95.0±1.8 | 76.0±4.4 | 50.2±2.6 | 1.6±1.2 |
| ChatDoctor / RAG-Thief | 73.4±2.0 | 72.4±2.8 | 65.4±4.0 | 37.8±2.6 | 2.4±1.4 |
| Mini-Wikipedia / Pirates | 78.4±2.0 | 75.4±2.8 | 67.0±4.0 | 42.4±2.4 | 5.4±3.6 |
| Mini-Wikipedia / RAG-Thief | 49.6±2.0 | 48.0±3.0 | 10.4±3.0 | 37.0±2.2 | 8.8±3.6 |
| Mini-BioASQ / Pirates | 71.0±1.8 | 70.6±2.8 | 43.0±3.6 | 53.8±2.2 | 0.4±0.2 |
| Mini-BioASQ / RAG-Thief | 63.4±2.2 | 62.6±3.2 | 29.4±4.4 | 38.0±2.4 | 0.2±0.2 |

The paper reports relative average CRR of 1.00×, 0.98×, 0.67×, 0.60× and 0.04× for no defense, reranking, summarization, RAGFort and CanaryRAG, respectively; relative FLOPs are 1.00×, 1.06×, 4.80×, 3.25× and 1.90×. Good-query BERTScore changes are 0.517→0.515 (ChatDoctor), 0.473→0.470 (Mini-Wikipedia) and 0.654→0.652 (Mini-BioASQ); reported false-positive rates are 0.13%, 0.08% and 0.15%.

Detection TPR for non-adaptive attacks is 98.2% without oracle and 99.2% with oracle. For adaptive A1+A3 it is 51.8%/94.1%; for A2+A3 it is 23.4%/95.6%. Adaptive evaluation is only on ChatDoctor. Canary position results include 97.4%/88.4% TPR at chunk boundaries and 98.2%/94.1% at sentence starts for non-adaptive/adaptive settings.

## Limits and Thesis Relation

CanaryRAG targets knowledge-base extraction, not poisoning that changes answers without reproducing source chunks. It relies on inserted markers, a streaming interception point and an extra oracle inference path. Its three-agent CRR results do not establish universal performance; adaptive TPR is tested on one agent. The authors do not evaluate membership inference, direct compromise of the database/retriever/infrastructure or side channels. Latency is plotted, but no exact mean, median or P95 is reported.

For direction A, it is not a poisoning or same-source multi-chunk co-necessity attack. For direction B, it is a runtime integrity/anti-exfiltration baseline and a possible orthogonal signal, not a source-truth detector or malicious-block classifier. Test whether a poisoning attack leaks a canary separately from whether it makes the model adopt a false claim. Citation count and priority inputs remain pending.
