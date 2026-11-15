---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2402.13532
reading_level: L3
checked_date: 2026-11-13
---
# Backdoor Attacks on Dense Retrieval via Public and Unintentional Triggers

**阅读状态：L3（限定版本）。** 已读完本地16页 arXiv:2402.13532v3；该版本首页标注发表于 COLM 2025。未将早期标题 *Backdoor Attacks on Dense Passage Retrievers for Disseminating Misinformation* 另算一项研究。

- **作者**：Quanyu Long；Yue Deng；LeiLei Gan；Wenya Wang；Sinno Jialin Pan
- **年份 / venue / track**：2025 / Conference on Language Modeling (COLM) / accepted conference paper
- **正式来源**：[COLM 2025录用列表](https://colmweb.org/2025/AcceptedPapers.html)；[arXiv v3](https://arxiv.org/abs/2402.13532v3)
- **DOI**：未见正式DOI；arXiv标识 `2402.13532`
- **CCF**：第七版目录未列COLM；不标为CCF-A
- **本地PDF**：[科研数据库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Backdoor Attacks on Dense Retrieval via Public and Unintentional Triggers.pdf>)；SHA-256 `3A57F94959340692C1A7CD5ED17CADD7C8EF35F38C157FA24B13E073F80B3C48`
- **代码**：[ruyue0001/Backdoor_DPR](https://github.com/ruyue0001/Backdoor_DPR)；本次确认仓库与论文关联，未执行或审计完整性
- **引用量**：未观测；按本轮优先顺序暂不核引用

## 核心方法与威胁模型

该工作将后门置于dense retriever：训练阶段污染部分训练数据以植入触发关联，部署阶段再向检索语料注入少量目标恶意段落；用户查询中自然出现的语法错误可触发这些段落被召回，而无错误的常规查询保持正常检索表现。论文报告其设置中仅0.048%的语料污染率即可取得高攻击成功率，并检查三种现有防御下恶意段落仍难以检出或过滤。

该威胁模型不仅要求污染部署语料，也要求训练数据可被污染；它不是只对一个固定、冻结检索器做黑盒文档注入的攻击。

## 与开题逐项比较

**A：** 这是“触发条件下持久检索到恶意内容”的直接近邻，限制“语法扰动触发的检索后门”宽泛首创；但没有单一真实长源经未知chunker形成的同源块共同召回/逐块必要性实验。

**B：** 三种检出/过滤基线提供防御对照；论文未研究RAG生成端的最终答案正确性，也未校准clean-query下按query汇总的错误删除率。其污染率与A的段落注入比例、Top-K检索事件均不得改写成RAG端到端ASR。

## 阅读与版本边界

- 完整阅读本地16页 arXiv v3；正式COLM版与该预印本逐项差异未审计。
- 未运行作者代码、未复现实验，也未核引用数。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md)。逐篇笔记目录未纳入版本控制。
