---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-e3491578c4fa
reading_level: L3
checked_date: 2026-11-13
---
# TimeR4: Time-aware Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering

**阅读状态：L3。** 已精读 ACL Anthology 收录的 EMNLP 2024 正式 PDF：正文 p1–9、附录 A 的两类 prompt（p11）；参考文献 p10–11 浏览。与 TKDE 2026 *Plan of Knowledge* 的会议前序/期刊扩展关系尚待核，见下文。

- **作者**：Xinying Qian；Ying Zhang；Yu Zhao；Baohang Zhou；Xuhui Sui；Li Zhang；Kehui Song。
- **会议 / track / 页码**：EMNLP 2024 Main，6942–6952；CCF-B（依用户提供的第七版目录）。
- **DOI**：`10.18653/v1/2024.emnlp-main.394`。
- **本地 PDF**：[科研数据库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/TimeR4 _ Time-aware Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering.pdf>)
- **SHA-256**：`baa2e50d12ab6fa9ba906d0c76a4618021840985eeaafb2750065af851cdb927`。
- **来源**：[ACL Anthology 正式页面与 PDF](https://aclanthology.org/2024.emnlp-main.394/) · [论文所列代码仓库](https://github.com/qianxinying/TimeR4)。仓库链接可访问；本次未读代码、未运行或复现。

## 方法与实验

TimeR4 面向时序知识图谱问答效用，采用 retrieve–rewrite–retrieve–rerank：冻结的 Sentence-BERT 将图谱事实编码入 FKS，先取背景事实并用 GPT-3.5-turbo-0125 将隐式时间问题改写为显式时间问题；另用对比式时间感知训练 Sentence-BERT 建立 TKS，以时间错误、关系/内容错误及二者同时错误构造负例，最终把语义检索分数与时间过滤分数结合排序。推理 LLM 为 LLaMA2-Chat-7B。

实现设置：时间检索器训练 10 epochs；推理模型在 2 张 NVIDIA A6000 上训练 2 epochs；MULTITQ 只取 20% 训练集；重排系数 μ=0.4；每题取 15 个事实。主要数据集是 MULTITQ 和 TimeQuestions，指标为 Hits@1。表 3/4 总体分别报告 72.8% 和 78.1%；作者相对增益的基线口径沿用其正文表述，不将不同表格分母合并。

PDF p6 的 MULTITQ Table 1 总计行将 dev 数写为 587,979，但六类 dev 数合计为 57,979；与表格子项及数据描述不符，作为原文疑点保留，未自行改写。作者局限为复杂时间事实检索和未微调 LLM 的答案格式控制；没有投毒、恶意源检测、误报率校准或未知分块实验。

## 对开题的边界

它是正常任务中时间条件检索、问题改写、对比训练与重排的近邻，可约束“首次在 RAG 中处理时间/条件约束”的宽泛主张；但它不判断文档恶意性/真伪，不检查来源关系，不输出块级风险或最终 query 级误删保证。对 A 的单真实源、未知 chunker、同源互补块共召回及逐块共同必要性不构成直接碰撞证据；对 B 是功能与效用基线，不是安全检测器。

## 与 Plan of Knowledge 的关系及待核事项

[Plan of Knowledge arXiv v1 作者稿](https://arxiv.org/pdf/2511.04072v1)在 PDF 第 6–7 页将 TimeR4 列为比较基线，第 11 页参考文献 [18] 引用 [TimeR4 的 ACL 正式版](https://aclanthology.org/2024.emnlp-main.394/)；两篇有五位共同署名作者，研究主题重合。比较基线和引用本身不足以确认或排除会议前序/期刊扩展关系；IEEE Xplore 本次请求返回 HTTP 202 空响应，最终出版版是否明确说明该关系及具体扩展范围仍待核。对比时按各自原文逐项比较，不把 PoK 方法视为已证实的版本增量；计权时考虑潜在关联，暂不将两篇当作相互独立的安全证据。

## 阅读边界

正式 PDF 共 11 页；正文 p1–9 完整阅读，含方法、公式、数据设置、主要表格、消融、效率、案例与结论；附录 A 的改写和推理 prompt 已读，参考文献已浏览。未逐条外部核验全部参考文献，未读取仓库或运行代码。版本页码和实际阅读范围不延伸到其他后续稿。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md)。逐篇笔记目录未纳入版本控制。
