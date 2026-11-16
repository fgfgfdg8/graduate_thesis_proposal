---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-1a46b5c409c1
reading_level: L3
checked_date: 2026-11-13
---
# Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering

**阅读状态：L3（作者预印本）。** 已逐页读完本地 12 页 arXiv v1；这不是 IEEE 最终排版版，未取得独立补充材料。

- **正式出版元数据**：TKDE 38(10), 6912–6925, 2026；DOI `10.1109/TKDE.2026.3718295`；CCF-A。
- **版本作者顺序**：Crossref 出版登记为 Ying Zhang、Xinying Qian、Yu Zhao、Baohang Zhou、Xuhui Sui、Xiaojie Yuan；所读 arXiv PDF 首页为 Xinying Qian、Ying Zhang、Yu Zhao、Baohang Zhou、Xuhui Sui、Xiaojie Yuan。按版本保留差异。
- **预印本**：arXiv:2511.04072v1，PDF 日期标记 2025-11-06。
- **本地 PDF**：[arXiv v1 作者稿（相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Plan of Knowledge_ Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering.pdf>)
- **SHA-256**：`D367BE0E55F4E9E12B691B78DB41B984C57B23DD5FBF0124A22EFDAC3A2BB032`
- **来源**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11656337/) · [Crossref 出版登记](https://api.crossref.org/works/10.1109/TKDE.2026.3718295) · [arXiv v1 版本记录](https://arxiv.org/abs/2511.04072v1) · [arXiv v1 官方 PDF](https://arxiv.org/pdf/2511.04072v1)。
- **版本核验（2026-11-15）**：本地 PDF 为 12 页，SHA-256 与 arXiv v1 官方 PDF 相同；IEEE Xplore 返回 HTTP 202 空响应，出版书目按 Crossref 登记核对，未直接对照 IEEE 最终版。
- **代码**：所读主文未提供代码地址，未确认公开实现。
- **代码运行 / 复现**：未进行。

## 核心内容

PoK 面向时序知识图谱问答的多跳检索与推理效用。它让 LLM 将问题规划为 `Retrieve`、`Rank`、`Reason` 等可执行子目标；以任务提示和对比式时间感知训练构造时序知识存储，再对候选事实作语义与时间联合评分及排序，最后由 LLM 综合事实作答。论文不提出恶意知识源、投毒攻击或安全检测机制。

检索器以 Qwen3-Embedding-0.7B 为基础，使用时间错误、内容错误、双重错误三类难负例进行 InfoNCE 训练 2 个 epoch；计划模块使用 GPT-4o API；推理使用 LLaMA2-Chat-7B，并在 2 张 NVIDIA A6000 上微调 2 个 epoch。MULTITQ 训练仅取 20%；推理每题取 top-20 事实。

## 实验与限制

四个数据集为 MULTITQ、TimeQuestions、Timeline-ICEWS 与 Timeline-CronQuestions。论文报告 Hits@1：PoK 在 MULTITQ 为 77.9%，TimeQuestions 为 83.2%；Timeline-CronQuestions 为 65.1%，Timeline-ICEWS 为 60.2%。这些是时序问答效用结果，不是投毒鲁棒性、误报率或安全保证。Table III 的 MULTITQ dev 分类项合计与总计均为 57,979；此前笔记误把该总量写成十倍值，现已勘误。

作者列出的局限包括复杂时序事实检索仍可改进，以及未微调 LLM 的答案格式控制困难。全文未报告恶意检索内容威胁模型、攻击成功率、正常块误删率、query 级校准或未知 chunker 评估。它是 B 的正常检索/条件推理效用近邻，不构成 A 或 B 安全方法的直接覆盖证据。

## 与 TimeR4 的关系及待核事项

所读 arXiv v1 将 EMNLP 2024 的 *TimeR4* 列为比较基线和参考文献（PDF 第 6–7、11 页），两篇作者和研究主题存在重合；另见 [TimeR4 逐篇笔记](TimeR4_Time-aware_Retrieval-Augmented_Large_Language_Models_for_Temporal__work-e3491578c4fa.md)。这些可定位位置本身不足以证明 PoK 是该论文的会议扩展版。原笔记称 IEEE 版明确列出四项扩展，但本次无法读取 IEEE 页面或最终版，未能核实这一说法；版本链关系及具体扩展范围均待核。比较时应注明两项研究可能相关，避免未经核实就将其作为独立安全证据合并计权。

## 实际阅读范围

- **PDF**：arXiv 作者稿 p1–12 全文逐页阅读；覆盖方法、公式、实验设置、结果表、分析、结论及参考文献。主文/图表未作代码复现，也未将图像曲线数值化。
- **版本边界**：出版元数据已核，未取得 IEEE 最终版逐页对照；不把作者稿与最终版宣称为逐字相同。
- **开题比较**：A 未见单源污染、未知 chunker、同源块角色或逐块共同必要性实验；B 可引用为正常检索及时间/条件推理效用参照，但不提供安全判别或误删控制。

[返回证据地图对应条目](../../../../docs/RAG安全证据地图_20261102.md#src-24da808fac1ee5e6-h10) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes)
