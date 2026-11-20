---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-60f4fb037266
reading_level: L3
checked_date: 2026-11-11
---
# Atomic Fact Decomposition Helps Attributed Question Answering

**阅读状态：L3（作者稿主文已读；未把参考文献或附加页记为已读正文）。**

- **作者**：Zhichao Yan, Jiapu Wang, Jiaoyan Chen, Xiaoli Li, Jiye Liang, Ru Li, Jeff Z. Pan
- **年份 / venue**：2025 / IEEE Transactions on Knowledge and Data Engineering, 37(12), 6959–6972
- **DOI / arXiv**：10.1109/TKDE.2025.3608716 / 2410.16708v2
- **CCF**：A 类，按第七版目录的期刊等级核对
- **官方记录**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11159096/) · [Crossref 出版登记](https://api.crossref.org/works/10.1109/TKDE.2025.3608716) · [arXiv 2410.16708v2](https://arxiv.org/abs/2410.16708v2)
- **本地作者稿**：[本地 PDF（相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Atomic Fact Decomposition Helps Attributed Question Answering.pdf>)
- **PDF 校验**：15 页；SHA-256 `9D2AD22E1B2D574EF40EDC95F97AA7AE49DB77F73638B24FD0222F6F4B9B0B39`；2026-11-15 核验与 [arXiv v2 官方 PDF](https://arxiv.org/pdf/2410.16708v2) 相同。
- **作者元数据差异**：arXiv v2 版本页和本地 PDF 的 Author 元数据列出 6 人，均未列 Jiye Liang；该 PDF 首页和 Crossref 出版登记均列出上述 7 人。差异原因待核，不擅自替换来源作者信息。
- **访问边界**：2026-11-15 请求 IEEE Xplore 返回 HTTP 202 空响应；出版书目按可访问的 Crossref 登记核对，未直接对照 IEEE 最终出版 PDF。

## 方法与发现

ARE 将长答案分解为 molecular clauses 与 atomic facts，以原子事实为单位检索证据；LLM verifier 判断证据是否足够，并触发补充检索或答案编辑，最后按 clause–fact 关系回填、聚合归因证据。它把答案归因从整段匹配细化到 claim/fact 粒度。

本次可恢复的阅读记录未保留可核对的 benchmark 数值及实验分母，因此不复述数值结果。代码复现、跨数据集稳定性和各模块消融仍待单独核对。

## 与开题的关系

这是正常 AQA 中“命题粒度 + 检索证据 + verifier + 证据回填”的强方法近邻，可用于界定证据充分性和局部错误定位。任务对象是已生成答案的归因/修订，不是识别恶意检索块，也未建立 clean-query 误删率或有限样本家族错误保证；因此不构成题目核心的直接撞车。

## 阅读范围与证据边界

- 原 TKDE 子任务记录确认主文 PDF 第 1–12 页已读，文本提取记录覆盖 pp. 1–12，并对 pp. 4–7 作了局部复核；本地 PDF 共 15 页。pp. 13–15 不计入已读主文范围。
- 本地文件与 arXiv v2 官方 PDF 的 SHA-256 一致；DOI 对应出版登记，此笔记只对该作者稿负责，不声称逐页核验最终出版版或补充材料。
- 已确认的方法描述来自正文阅读记录与既有官方摘要。精确指标、逐 query 结果、运行成本和未恢复的页内数值均标记为待核，不以记忆补写。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究基准的逐 query 重叠未知，不作数值合并。

[全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes) · [返回证据地图对应条目](../../../../docs/RAG安全证据地图_20261102.md#src-2038e7873715cfe3-h6)
