---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-6284f7564121
reading_level: L3
checked_date: 2026-11-13
---
# Poisoning Retrieval Corpora by Injecting Adversarial Passages

**阅读状态：L3。** 已逐页阅读 EMNLP 2023 官方12页论文PDF（正文及文末参考文献页）；未运行作者代码。

- **作者**：Zexuan Zhong；Ziqing Huang；Alexander Wettig；Danqi Chen
- **年份 / venue / track**：2023 / EMNLP / main conference
- **正式书目**：[ACL Anthology](https://aclanthology.org/2023.emnlp-main.849/)；DOI `10.18653/v1/2023.emnlp-main.849`；pp. 13764–13775
- **CCF**：EMNLP主会按第七版目录为CCF-B
- **本地PDF**：[科研数据库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Poisoning Retrieval Corpora by Injecting Adversarial Passages.pdf>)；SHA-256 `0586B174B4B6D85B4738894F4F7CFEDA2E209EBBF755D232E48F08A9599D0723`
- **代码**：[princeton-nlp/corpus-poisoning](https://github.com/princeton-nlp/corpus-poisoning)（论文PDF明确给出的项目地址；未执行）
- **引用量**：未观测；按本轮优先顺序暂不核引用

## 核心方法与结果

论文提出针对dense retriever的白盒语料投毒：以可访问的训练查询为优化信号，通过离散token扰动生成少量对抗段落，再将其注入大规模检索语料，使未见查询也可能检索到攻击段落。论文报告50条针对Natural Questions优化的段落可误导金融文档或在线论坛中超过94%的问题；最多注入500条即可影响百万级语料中的检索结果。

须严格解释其 **Top-20 attack success**：成功事件是攻击段落进入前20个检索结果，不等价于RAG最终答案错误、错误事实被采信或生成端到端攻击成功率。

## 与开题逐项比较

**A：** 是持久检索语料投毒和跨查询泛化的直接先例，撤回“首次向知识库注入攻击段落并诱导检索”的宽泛表述。它没有测试单一真实长源经受害者未知chunker形成的同源块，也没有同query共同召回后逐块/联合删除的必要性实验。

**B：** 未提出RAG证据判真或删除式防御；Top-20检索成功率不是clean-query误删率，论文没有query级错误删除校准。

## 阅读与证据边界

以ACL Anthology正式PDF为身份和版本主源。完整阅读正文不代表复现了检索器、基准或攻击代码；跨数据集结果不与RAG生成端ASR合并。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md)。逐篇笔记目录未纳入版本控制。
