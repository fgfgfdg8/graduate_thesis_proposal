---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-59be3d575999
reading_level: L3
checked_date: 2026-11-13
---
# Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output

**阅读状态：L3。** 正式9页PDF正文物理页1–9已完整阅读；印刷页码为1305–1313。不据此声称另有未提供的附录已读。

- **作者**：["Hithesh Sankararaman", "Mohammed Nasheed Yasin", "Tanner Sorensen", "Alessandro Di Bari", "Andreas Stolcke"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2024 / EMNLP / Industry Track，pp.1305–1313
- **发表状态**：ACL Anthology正式卷条目；DOI `10.18653/v1/2024.emnlp-industry.97`
- **CCF**：EMNLP venue-level B；Industry Track不单独继承或标注venue等级。
- **引用量**：未核；引用核验仍按整批文献统一执行。
- **代码**：论文正文及正式条目未见专属代码仓库；不据此断言代码不存在。
- **关联标题**：["Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output"]

## 一句话总结与核心贡献

Provenance在回答生成后对答案事实与检索上下文进行NLI核验，并将判断回溯到相关chunks；属于B方向事实核验和来源定位的近邻，不是生成前的恶意文档检测器。

## 与开题逐项比较

**A：** 未测试真实长源经受害者未知chunker切分、实际同query共召回或同源多块共同必要性；不能作为A方向完整撞车证据。

**B：** 与答案事实核验和chunk来源回指直接相邻，但作用于生成后答案；未提供clean-query最终OR删块误报控制，不等价于本课题生成前的投毒检测/过滤。

## 局限、可比性与不确定性

全文结果依赖模型与评测配置；AUC及HotpotQA聚合结果不能脱离相应配置作普遍优劣结论，也不构成生产环境风险保证。未评估未知chunker、真实索引中的同源多块共同必要，或正常query经最终OR动作删除证据的风险。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### 2024.emnlp-industry.97 — 正式正文阅读

- **书目来源**：ACL Anthology正式条目 `2024.emnlp-industry.97`；阅读记录见[证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-66b72247fe37d0d8)。
- **DOI / arXiv**：`10.18653/v1/2024.emnlp-industry.97` / 未发现对应arXiv版本。
- **本地PDF**：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Provenance_ A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output.pdf>)；9页；SHA-256 `CD4442ED519E661A7EED916B7F6D3FD5F10638CDD1D15470F941A47BF9F0737A`。
- **实际阅读**：L3；正式PDF物理页1–9全文，印刷页1305–1313。

#### 方法、结果与适用条件

### 2024.emnlp-industry.97 — Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output

- **作者**：Hithesh Sankararaman；Mohammed Nasheed Yasin；Tanner Sorensen；Alessandro Di Bari；Andreas Stolcke。
- **正式卷/track**：2024 EMNLP Industry Track；EMNLP venue-level CCF-B，Industry Track不单独评级。
- **阅读等级/范围**：L3；正式9页PDF全文，印刷页1305–1313。
- **DOI**：`10.18653/v1/2024.emnlp-industry.97`。
- **本地PDF**：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Provenance_ A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output.pdf>)。
- **处置**：direct_B_L3_post_generation_fact_checking。

**一句话总结及A/B比较**：生成后以NLI核验答案事实与检索上下文，并回溯到支撑chunks；与B的事实核验/来源定位相邻，但不检测生成前恶意文档，也不等价于query级最终删块风险控制。

**证据边界/局限**：AUC及HotpotQA结果随配置变化；不外推到未测试的模型、语料与索引。没有未知chunker或同源多块共同必要实验，也未报告clean-query最终OR误删保证；未运行实现或独立复现。

## 待核事项与追溯

引用数及跨研究样本重叠未核；未做实现运行或独立复现。正文与ACL正式条目未显示代码仓库，资源是否另行发布保持未知。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#src-c2aa1714998f8ac9)
