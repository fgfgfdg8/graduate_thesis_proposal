---
tags: [rag-security-evidence, opinion-manipulation]
study_id: arxiv-2501.02968
reading_level: L2
checked_date: 2026-11-15
---
# FlippedRAG: Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models

**身份**：ACM CCS 2025主会，CCF-A，DOI [10.1145/3719027.3765023](https://doi.org/10.1145/3719027.3765023)；[CCS录用数据](https://www.sigsac.org/ccs/CCS2025/assets/accepted-papers.json)。[ACM正式版PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/版本/f9e61441f781/FlippedRAG_ Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models.pdf>)与[Crossref正式记录](https://api.crossref.org/works/10.1145/3719027.3765023)的作者顺序一致；CCS旧录用名单有不同题名和作者顺序。所读[arXiv v7作者稿](https://arxiv.org/abs/2501.02968v7)带Conference’17模板和2026页眉，不据此更改正式会议信息。

**阅读范围**：L2；本地[arXiv v7 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/FlippedRAG_ Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models.pdf>)，SHA-256 `5e964e5686100fac73e7885f3909372ab5f2a116cadb98a4a0b57dd2ed77f092`；此前已读物理第4–5页（§3.2–§3.4开头），本次补读第1、10–11、17页（摘要、表7、§5.3和附录B.4）。另读正式版物理第1、10–11页，核对书目、表7和§5.3；正式PDF SHA-256 `f9e61441f7813576bb44a88715b2c9617486dbcedb4924caae5e99654cd84e2f`。未把这些局部阅读当作L3或正式出版版全文。

## 方法与开题关系

攻击者可多次查询黑盒RAG，并依赖系统能返回检索参考文本；以查询、候选和答案训练替代检索器，再优化触发器与少量目标观点文档，以迁移到目标检索器。它与A的检索导向投毒和跨查询操纵相邻，但不等同于一份真实长文经未知分块后形成的双块共同必要性。观点分歧不等同于B所检测的事实冲突；防御评估应包含可重复查询的自适应攻击。

## 用户研究与指标边界

正式版及v7表7、§5.3结果一致；v7附录B.4报告54名受试者分两组，各27人；三个话题的干净组/投毒组事后7点量表均值分别为：转基因4.88/5.55、企业所得税3.59/2.70、安乐死医疗援助4.70/2.66。即组间均值差+0.67、−0.89、−2.04分；作者报告三个事后独立样本检验均 $p<0.05$。摘要的“20% shift in user cognition”不是“20%的受试者改变观点”的直接证据，也不能与模型输出的方向变化直接相减或换算。

Topic-FlipRAG亦报告54人、每组27人的研究且作者有重叠；两研究是否共用被试未知。正式版与v7的表7均值及显著性判断一致；样本人数来自v7附录。其OMSR把向目标方向移动计作成功，既包括从反对变中立，也包括其他移动，不能机械称为完全立场翻转比例。

## 制品与追溯

[GitHub](https://github.com/DavidAilesChen/FlippedRAG)可访问；[Zenodo归档](https://zenodo.org/records/17036325)网页本次受访问限制。未执行代码。引用计数见[元数据](../../../../docs/RAG安全文献补查元数据_20261102.md)；[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-99492f9671c6e7ac)。
