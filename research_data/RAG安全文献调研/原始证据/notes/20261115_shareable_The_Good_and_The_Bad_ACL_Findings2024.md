---
tags: [rag-security-evidence, privacy]
study_id: work-6d21d4d9cb2f
reading_level: L3
checked_date: 2026-11-12
---
# The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation (RAG)

**出处与范围：** Shenglai Zeng等，Findings of ACL 2024，pp. 4505–4524；[ACL Anthology正式记录](https://aclanthology.org/2024.findings-acl.267/)，DOI `10.18653/v1/2024.findings-acl.267`。第七版CCF目录的ACL主会为A类；本文是Findings论文，不单独继承主会等级。此前阅读记录覆盖正式版物理页1–20（含附录和参考文献），未运行代码或复现。

[本机论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/The Good and The Bad_ Exploring Privacy Issues in Retrieval-Augmented Generation ( RAG ).pdf>)：20页，SHA-256 `b1d8fac43b05add1197862e3945776cfa9782a3a5b9c4bed03d7fb25c0f4a2c4`。[作者仓库](https://github.com/phycholosogy/RAG-privacy)仅确认公开页面，许可证和可复现性未审查。

## 问题与研究边界

论文分别研究外部检索数据库的隐私泄漏和RAG对生成器训练数据记忆泄漏的影响。前者通过黑盒查询尝试从已有的检索内容中抽取信息，后者研究外部参考对训练数据记忆抽取的影响；这两类隐私目标不能合并为同一种攻击，也不是知识库投毒或恶意证据检测。

## 实验与结果

- 论文使用约50万封Enron邮件与约20万条HealthcareMagic医患对话构造检索数据；表1的非定向攻击每组250条提示。Enron/GPT-3.5设置中，452为检索到的不同上下文数，116为输出存在直接重复的提示数，121为达到作者ROUGE条件的提示数；这些分母和单位不能互换（PDF物理页4–5）。
- 表2的定向攻击也报告每组250条提示；GPT-3.5设置下HealthcareMagic与Enron分别抽取到148和205项作者定义的目标信息。这些不是对任意知识库的成功率保证（物理页5）。
- 作者评估重排、摘要和距离阈值等策略；其隐私效果与任务效用取决于配置，不等于检测了虚假或恶意文本（物理页6及附录）。

## 对开题的启示

A关注攻击者写入内容后造成的知识完整性破坏，本文关注对现有检索数据库的机密性攻击；B关注恶意证据及正常证据保留，本文的重排和摘要只能作为隐私—效用比较，不提供恶意块检测或clean-query最终误删保证。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-14758d2821d6c5dd) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
