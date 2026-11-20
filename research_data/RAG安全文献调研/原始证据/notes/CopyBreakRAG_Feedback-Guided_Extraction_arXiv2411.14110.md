---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: arxiv-2411.14110
reading_level: L3
checked_date: 2026-11-13
---
# Feedback-Guided Extraction of Knowledge Base from Retrieval-Augmented LLM Applications

**阅读状态：L3。** arXiv v2本地19页PDF正文及附录已全文阅读；未独立复现。

- **作者**：Changyue Jiang；Xudong Pan；Geng Hong；Chenfu Bao；Yang Chen；Min Yang
- **版本关系**：arXiv:2411.14110v1（2024-11-21）题为 *RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks*；v2（2025-08-08）改题并命名方法为CopyBreakRAG，新增Yang Chen。两个版本是同一研究，不重复计数
- **正式发表状态**：截至2026-11-13未核实正式会议或期刊出处；DBLP的CoRR记录采用旧题名和v1作者，仅作为预印本佐证
- **CCF**：没有已核正式venue，不赋CCF等级
- **PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Feedback-Guided Extraction of Knowledge Base from Retrieval-Augmented LLM Applications.pdf>)；19页；SHA-256 `0BB448E7F989C27F83E366B98FB198D09168DB5686BA50AB72ADF60FA5C6A63C`
- **引用与优先级**：Google Scholar未观测；优先级未计算
- **代码**：未核实

## 方法与结果

威胁模型为黑盒API查询与回答观察。攻击分无领域先验的untargeted和有领域先验的targeted：先用对抗查询诱导应用暴露检索上下文，再解析保存文本块，通过随机探索和已知块的前向/后向推理生成后续查询，并以针对常见RAG模板的正则重建块。

Table III每组预算为200次攻击查询。九个数据集/目标模型组合的宏平均CRR为CopyBreakRAG 66.4%/70.0%（untargeted/targeted），PIDE为14.4%/23.3%；DGEA需访问目标embedding模型，不是同权限黑盒基线。作者报告的“平均高约45%”未给出聚合口径，不应与宏平均绝对百分点差混用。

作者创建并测试的GPTs、Coze应用使用公开数据，不是对第三方线上应用的攻击。所测grep匹配防御在若干targeted设置下仅降低1个百分点；该结果不代表对成熟防护的鲁棒性。

## 与开题的关系

这是知识库原文提取/隐私近邻；若研究范围包含知识库机密性，应直接比较其黑盒威胁模型、查询预算、CRR/EED及返回块数。但它读取并复制知识库，不写入或篡改语料，也不检测恶意证据块或后门触发，故不是语料完整性检测的直接撞车。它说明“首次研究RAG知识库抽取/泄露”的宽泛表述不能成立。

## 来源与追溯

[arXiv v2记录](https://arxiv.org/abs/2411.14110v2) · [arXiv v1记录](https://arxiv.org/abs/2411.14110v1)。本次 DBLP 请求返回 HTTP 202，未核到记录正文；全文页码按本地19页PDF计，远端PDF直链本次未单独核验。引用数未核，未运行作者代码。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-copybreakrag) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
