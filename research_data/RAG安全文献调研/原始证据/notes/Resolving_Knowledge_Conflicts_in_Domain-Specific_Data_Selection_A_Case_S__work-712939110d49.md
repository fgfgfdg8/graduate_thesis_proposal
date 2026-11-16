---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-712939110d49
reading_level: L3
checked_date: 2026-11-11
---
# Resolving Knowledge Conflicts in Domain-Specific Data Selection: A Case Study on Medical Instruction-Tuning

**阅读状态：L3（14 页作者稿逐页检查并阅读正文；未把未恢复的附加材料范围外推）。**

- **作者**：Qihuang Zhong, Liang Ding, Fei Liao, Juhua Liu, Bo Du, Dacheng Tao
- **机构**：Nanyang Technological University; University of Sydney; Wuhan University
- **年份 / venue**：2026 / IEEE Transactions on Knowledge and Data Engineering, 38(10), 6969–6986
- **DOI / arXiv**：10.1109/TKDE.2026.3720785 / 2505.21958v1
- **CCF**：A 类，按第七版目录的期刊等级核对
- **官方记录**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11641842/) · [Crossref 出版登记](https://api.crossref.org/works/10.1109/TKDE.2026.3720785) · [arXiv 2505.21958v1](https://arxiv.org/abs/2505.21958v1)
- **本地作者稿**：[本地 PDF（相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Resolving Knowledge Conflicts in Domain-Specific Data Selection_ A Case Study on Medical Instruction-Tuning.pdf>)
- **PDF 校验**：14 页；SHA-256 `D4710A10B7C684ED96ED78DB37B7D507733AA40563BD56A0A1BB3E9FFB241A2D`；2026-11-15 核验与 [arXiv v1 官方 PDF](https://arxiv.org/pdf/2505.21958v1) 相同。
- **访问边界**：2026-11-15 请求 IEEE Xplore 返回 HTTP 202 空响应；出版书目按可访问的 Crossref 登记核对，未直接对照 IEEE 最终出版 PDF。

## 方法与发现

论文提出 Knowledge-aware Data Selection（KDS），面向医学指令微调数据，使用两类指标刻画知识冲突：context–memory knowledge alignment，以及 intra-memory knowledge consistency；随后过滤高冲突样本，并对较高质量且多样的数据采样。作者报告该策略改善领域任务表现与泛化，并缓解幻觉。

线程保留了方法页和实验/结论页的阅读线索，但未保存足以复核的逐模型数值、实验分母或完整表格转录。本笔记不填补这些数字；复现代码与最终出版版差异待核。

## 与开题的关系

这是知识冲突定量化和数据筛选的机制邻近工作，可参考“参数知识与上下文证据不一致”如何操作化。但 KDS 的筛选发生在医学指令微调训练数据阶段，不是运行时 RAG 检索结果过滤；论文没有检验恶意文档植入、查询级攻击成功率、良性 query 误删或有限样本安全保证。故它是较弱的方法参照，不是 RAG 投毒直接撞车。

## 阅读范围与证据边界

- 原线程记录：本地 14 页 PDF 全稿均被检查，正文完成阅读；可恢复的页级阅读线索包括 PDF pp. 2–7 的方法材料、pp. 8–11 的实验/结论材料及第 10 页结论。主文结束页与附录/参考文献分界在中断日志中未完整转录，故不把补充材料声明为已读。
- 版本：arXiv 2505.21958v1 作者稿。PDF 哈希在恢复时重新计算，与前一代理记录一致；不将作者稿等同最终出版版。
- 结论中的结果只记录论文主张，不补写无法从保留日志复核的具体分数、效应量或显著性。

**样本/版本依赖：** 医学微调评测不能直接代表 RAG 在线安全；同研究多版本不独立计权，跨研究逐 query 重叠未知。

[全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes) · [返回证据地图对应条目](../../../../docs/RAG安全证据地图_20261102.md#src-608929ce70d06c6b-h6)
