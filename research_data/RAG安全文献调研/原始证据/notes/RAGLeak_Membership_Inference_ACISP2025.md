---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: doi-10.1007-978-981-96-9101-2_8
reading_level: L1
checked_date: 2026-11-13
---
# RAGLeak: Membership Inference Attacks on RAG-Based Large Language Models

**阅读状态：L1。** 仅核对出版者书目页和完整摘要；全文未取得，不据摘要扩写方法细节或实验限制。

- **作者**：Kaiyue Feng；Guangsheng Zhang；Huan Tian；Heng Xu；Yanjun Zhang；Tianqing Zhu；Ming Ding；Bo Liu
- **正式出处**：ACISP 2025，Springer proceedings chapter，pp. 147–166
- **DOI**：[10.1007/978-981-96-9101-2_8](https://doi.org/10.1007/978-981-96-9101-2_8)
- **CCF**：ACISP按第七版目录为CCF-C（venue级）
- **全文 / PDF**：出版者标记为非开放全文；未取得本地PDF，不尝试绕过访问限制
- **引用与优先级**：Google Scholar引用未观测；优先级待相关候选池完成后统一计算
- **代码**：未核实

## 摘要级内容与边界

出版者摘要称论文考察黑盒与灰盒RAG成员推断，使用两个数据集和三种LLM，报告多个设置下准确率超过80%，并称攻击可规避一种few-shot提示防护。这些均为摘要转述，未由正文独立核验。

成员推断以检索数据库机密性为目标，不是外部知识投毒、后门触发或恶意证据块检测；该文是相关的隐私威胁邻域，但不能作为A/B完整性检测的直接撞车结论。因全文未取得，机制、分母、统计不确定性和防御代价均待核。

## 来源与追溯

来源为[Springer出版者记录与摘要](https://link.springer.com/chapter/10.1007/978-981-96-9101-2_8)；[UTS机构仓储](https://opus.lib.uts.edu.au/handle/10453/188869)同样将接受稿标为closed access。不与2026年arXiv同名但研究不同的 *RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation* 合并。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-ragleak-acisp) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
