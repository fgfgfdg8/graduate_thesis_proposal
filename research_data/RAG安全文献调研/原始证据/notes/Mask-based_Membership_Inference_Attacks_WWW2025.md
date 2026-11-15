---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: doi-10.1145-3696410-3714771
reading_level: L3
checked_date: 2026-11-13
---
# Mask-based Membership Inference Attacks for Retrieval-Augmented Generation

**阅读状态：L3。** 本地14页PDF正文已全文阅读；未独立复现。

- **作者**：Mingrui Liu；Sixiao Zhang；Cheng Long
- **正式出处**：Proceedings of the ACM Web Conference 2025 (WWW '25)
- **DOI / arXiv**：`10.1145/3696410.3714771`；arXiv:2410.20142v2
- **CCF**：WWW按第七版目录为CCF-A（venue级）
- **PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Mask-based Membership Inference Attacks for Retrieval-Augmented Generation.pdf>)；14页
- **引用与优先级**：Google Scholar引用未观测；优先级待相关候选池完成后统一计算
- **代码**：未核实

## 核心方法与结论

该研究以成员推断为目标，通过mask-based查询/响应信号判断候选文本是否属于RAG检索数据库。攻击者观察目标RAG的输出，不需要修改知识库；关注的是数据库内容的成员隐私，而非检索文档的真实性或攻击恶意性。

## 与开题的关系

WWW 2025 CCF-A中的RAG成员推断工作，适合作为广义RAG安全和检索数据隐私近邻。它与语料投毒、后门触发及恶意证据块识别是不同威胁面：成员身份推断正确不等于识别毒文档，毒文档检测也不覆盖未授权成员信息泄露。对开题的关系是边界与威胁模型参考，不是A/B方法的直接撞车。

## 来源与阅读范围

本地14页PDF首页标注arXiv v2并列出ACM引文；2026-11-15访问ACM页面返回HTTP 403，未能重新读取出版者页面，也未逐项比对出版终版。未运行论文代码，未核引用数。

[arXiv v2记录](https://arxiv.org/abs/2410.20142v2)

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-mask-mia) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
