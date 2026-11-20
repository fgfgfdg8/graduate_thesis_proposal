---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-013aed241abe
reading_level: L3
checked_date: 2026-11-11
---
# The Other Side of the Coin: Exploring Fairness in Retrieval-Augmented Generation

**阅读状态：L3（12 页作者稿正文已逐页阅读；不是已核验的 IEEE 最终出版 PDF）。**

- **作者**：Zheng Zhang, Ning Li, Qi Liu, Rui Li, Weibo Gao, Qingyang Mao, Zhenya Huang, Baosheng Yu, Dacheng Tao
- **年份 / venue**：2026 / IEEE Transactions on Knowledge and Data Engineering, 38(9), 6208–6225
- **DOI / arXiv**：10.1109/TKDE.2026.3704753 / 2504.12323v2（本地 PDF 首页及官方版本记录均有该标记）
- **CCF**：A 类，按第七版目录的期刊等级核对
- **官方记录**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11569354/) · [Crossref 出版登记](https://api.crossref.org/works/10.1109/TKDE.2026.3704753) · [arXiv 2504.12323v2](https://arxiv.org/abs/2504.12323v2)
- **本地作者稿**：[本地 PDF（相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/The Other Side of the Coin_ Exploring Fairness in Retrieval-Augmented Generation.pdf>)
- **PDF 校验**：12 页；SHA-256 `9A8430829311F5C9B5C889AAC134B2F53D7A044C85DD71AA7BA28352C8C3A684`；2026-11-15 核验与 [arXiv v2 官方 PDF](https://arxiv.org/pdf/2504.12323v2) 相同。
- **访问边界**：2026-11-15 请求 IEEE Xplore 返回 HTTP 202 空响应；出版书目按可访问的 Crossref 登记核对，未直接对照 IEEE 最终出版 PDF。

## 方法与发现

论文系统考察 LLM、retriever 与检索来源对 RAG 公平性的影响，并提出 FairFT 和 FairFilter：前者以公平性对齐 retriever 与 LLM；后者在检索之后过滤有偏内容。目标是降低群体偏见，同时保持回答效用。

作者报告小于 8B 的模型接入 RAG 后公平性可能恶化；但摘要将阈值写作“小于 8B”时又列出 Llama3-8B 作为例子。具体规模边界需以版本一致的实验表核定。本次恢复的阅读日志没有保留足以复述的逐数据集数值、分母及置信区间，故不补写数字。

## 与开题的关系

FairFilter 是“检索后内容过滤”这一处理位置的直接方法参照，可启发清洗器与生成器之间的接口、效用保持评估。它过滤的是社会偏见内容而不是恶意/投毒文档；公平指标不能替代恶意证据识别、clean-query 误删控制或有限样本保证，因此属于属性相邻而非同一安全问题。

## 阅读范围与证据边界

- 原线程确认 arXiv v2 作者稿 PDF 共 12 页，并对 PDF pp. 1–12 分段提取/逐页阅读（pp. 1–4、5–8、9–12）；第 9 页文本提取乱码处另有页面视觉检查记录。
- 本地稿页眉含期刊模板占位文本 `JOURNAL OF XXX`，故不把它标为最终出版版。首页标注 arXiv:2504.12323v2（2025-04-19），且其 SHA-256 与对应官方 PDF 一致；原线程实际使用的下载链接仍未恢复，不能由文件一致反推下载来源。
- 记录的方法判断以已读 PDF 和官方书目/摘要为边界。逐项数值、代码提交、测试数据与运行预算没有完整转录，不宣称已核实。

**样本/版本依赖：** 不同检索来源、模型尺度和公平指标不可直接合并；同一研究多版本不独立计权。

[全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes) · [返回证据地图对应条目](../../../../docs/RAG安全证据地图_20261102.md#src-224a9a8a8709ef36-h6)
