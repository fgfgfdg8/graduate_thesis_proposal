---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: doi-10.5220-0013108300003899
reading_level: L3
checked_date: 2026-11-13
---
# Is My Data in Your Retrieval Database? Membership Inference Attacks Against Retrieval Augmented Generation

**阅读状态：L3。** 本地12页PDF正文已全文阅读；未独立复现。

- **作者**：Maya Anderson；Guy Amit；Abigail Goldsteen
- **正式出处**：11th International Conference on Information Systems Security and Privacy (ICISSP 2025), pp. 474–485
- **DOI**：`10.5220/0013108300003899`
- **CCF**：第七版目录未列ICISSP，不赋CCF等级
- **PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Is My Data in Your Retrieval Database_ Membership Inference Attacks Against Retrieval Augmented Generation.pdf>)；12页
- **引用与优先级**：Google Scholar引用未观测；优先级待相关候选池完成后统一计算
- **代码**：未核实

## 核心方法与结论

论文研究攻击者能否仅凭目标RAG的回答推断指定文本是否存于检索数据库，并讨论基于提示指令的防护。全文结果显示防护效果依模型和设置而异；部分设置下提示防护带来明显拒答或正常效用损失，不应概括成统一、无代价的防御效果。

## 与开题的关系

该论文处理检索数据库成员隐私，不处理检索库投毒、恶意来源判别或多块协同误导。它提醒开题将机密性（某条数据是否在库）与完整性（检索证据是否被恶意污染）分开定义；对A/B是相邻威胁边界，不是直接方法撞车。

## 来源与阅读范围

书目信息按ICISSP正式PDF首页及DOI著录；本地PDF共12页并已全文阅读。作者机构页面也列出此论文和会议；2026-11-15出版者页面返回403或网络超时，本次未能重新读取。引用未核，未执行源码或独立复现。

[作者机构的会议记录](https://research.ibm.com/publications/is-my-data-in-your-retrieval-database-membership-inference-attacks-against-retrieval-augmented-generation--1)

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-is-my-data-mia) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
