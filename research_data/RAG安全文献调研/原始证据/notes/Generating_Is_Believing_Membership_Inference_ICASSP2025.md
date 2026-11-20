---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: arxiv-2406.19234
reading_level: L3
checked_date: 2026-11-13
---
# Generating Is Believing: Membership Inference Attacks against Retrieval-Augmented Generation

**阅读状态：L3。** 本地8页PDF正文已全文阅读；未独立复现。

- **作者**：Yuying Li；Gaoyang Liu；Chen Wang；Yang Yang
- **正式出处**：IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2025)
- **DOI / arXiv**：`10.1109/ICASSP49660.2025.10889013`；arXiv:2406.19234v2
- **CCF**：ICASSP按第七版目录为CCF-B（venue级）
- **PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Generating Is Believing_ Membership Inference Attacks against Retrieval-Augmented Generation.pdf>)；8页
- **引用与优先级**：Google Scholar引用未观测；优先级待相关候选池完成后统一计算
- **代码**：未核实

## 核心方法与结论

论文提出S²-MIA，以生成回答与候选成员文本之间的语义相似性作为成员推断信号，判断该文本是否进入RAG检索数据库。其攻击终点是数据库成员隐私；语义相似度信号不能解释为对检索内容的事实核验或恶意性判断。

## 与开题的关系

这是RAG数据成员推断的正式ICASSP近邻。它应与知识投毒、触发式检索后门及检索块恶意性检测分列：即便能判定文本曾被检索数据库收录，也不能由此判定文本为真、为毒或具有攻击意图；反向亦然。对开题主要提供威胁模型和构念边界参考，不直接占据A/B检测生态位。

## 来源与阅读范围

正式会议身份见作者论文列表；本地8页PDF首页标识为arXiv:2406.19234v2（2024-09-26），与IEEE出版版未逐项比对。2026-11-15 DOI跳转IEEE后返回HTTP 202且无网页内容，本次未能重新核验出版者页面；未运行代码，未核引用数。

[作者论文列表](https://www.chenwang.net.cn/publications.html) · [arXiv v2](https://arxiv.org/abs/2406.19234v2)

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-generating-is-believing) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
