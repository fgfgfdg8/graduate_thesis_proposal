---
tags: [rag-security-evidence, fairness, evidence-governance]
study_id: arxiv-2410.07589
reading_level: L3
checked_date: 2026-11-16
---
# No Free Lunch: Retrieval-Augmented Generation Undermines Fairness in LLMs, Even for Vigilant Users

**定位：公平性与受控偏置样本构造的低优先级方法参考；安全相关性有限。** 论文测试了外部数据公平性审查和合成偏置样本对 RAG 输出的影响，附录包含明确称为 poison strategy 的样本构造；其实际研究对象和能力设定不能等同于开题 A 的受限攻击，也未给出开题 B 的恶意证据检测与误删校准。

## 身份、版本、去重与阅读范围

- **正式文献**：Mengxuan Hu、Hongyi Wu、Ronghang Zhu、Zihan Guan、Dongliang Guo、Daiqing Qi、Sheng Li，*Findings of the Association for Computational Linguistics: EMNLP 2025*，2025 年 11 月，18145–18170，DOI `10.18653/v1/2025.findings-emnlp.984`。[ACL Anthology 正式条目](https://aclanthology.org/2025.findings-emnlp.984/)；[正式版 PDF](https://aclanthology.org/2025.findings-emnlp.984.pdf)。
- **作者稿和版本区别**：[arXiv:2410.07589v1](https://arxiv.org/abs/2410.07589v1)，2024-10-10；截至本次核验，arXiv 提交历史仅列 v1。作者稿页面的作者顺序为 Hu、Wu、**Guan、Zhu**、Guo、Qi、Li，正式条目及正式 PDF 为 Hu、Wu、**Zhu、Guan**、Guo、Qi、Li。本文按实际阅读的正式版著录；未逐字比对作者稿与正式版，也不据此假设实验和结果完全相同。
- **CCF**：用户提供的[第七版目录](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F) PDF 物理第 58 页列 **EMNLP 主会为 B 类**；[第七版CCF正式发布说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml)明确指出 Findings 不计入该目录的考虑范围，故本篇不标为主会的 A/B 类。所用本地目录与上述官方文件 SHA-256 均为 `271b630b576bf8a4f802e767f5694caded93680e22b3a19bef7902591c45c1d3`。
- **本地已读文件**：[论文库正式 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/No Free Lunch_ Retrieval-Augmented Generation Undermines Fairness in LLMs, Even for Vigilant Users.pdf>)，26 个物理页，SHA-256 `3c9dcbce897ad95ffa7c14f2a3b64c14d651bc9683b769527ef19ecea542ff23`；从上述 ACL 官方 PDF 下载。论文库位于仓库之外，不随仓库检出。
- **去重**：既有会议目录快照已收录本篇；本机 `catalogs/local_catalog295_parent_sources/catalog295/reviews/2025.findings-emnlp.984.json` 记录了正式摘要的 L1 人工阅读，明确 `L2_credit=0`、`L3_credit=0`。该快照被 Git 忽略，其他机器默认不可取得；公开书目请核对上方 ACL 条目。本次以 DOI、题名和 arXiv ID 搜索三份报告与研究库笔记，未发现独立正文阅读条目，故这是**既有候选的正文补读**，不是新发现的新论文。上游参考见 [Bias Amplification 笔记](Bias_Amplification_in_RAG_Poisoning_Knowledge_Retrieval_to_Steer_LLMs__arxiv-2506.11415.md)。
- **阅读状态：L3（正式版主文）**。2026-11-16 读取 PDF 文本层的物理页 1–9（正文、结论与限制；末页开始参考文献），并定向读取附录页 17–19、22–23、25–26。以下页码均为这份 PDF **物理页**，印刷页 = 物理页 + 18144。并对物理页 19、22、23 的采样公式及指标定义、表值进行页面图像核对；未逐页精读参考文献及其余附录，未逐张目视检查其他图像，未运行代码或复现实验。引用数未核实，保持未知。

## 问题、设计与结果

- **三种外部数据审查状态**（pp. 2–4）：分别使用未审查、仅去除特定类别偏置、按实验标签视为全审查的数据。论文的“威胁”以数据使用者的公平性认知为轴，主要研究既有或构造的偏见进入 RAG，而不是刻画能够写入真实来源、控制切块或操纵检索索引的外部攻击者。
- **数据构造与检索**（pp. 5、17–19）：三个任务分别用 PISA 性别分类、BBQ 问答和 HolisticBias 续写；80%/20% 划分中，训练部分作知识库、测试部分作评估；每个偏置类别选 100 个样本或在不足时用全部样本。作者用 `bge-small-en-v1.5`、FAISS、点积和 Top-5 检索。BBQ 将含糊上下文与偏见答案拼接为 `poison`，将明确上下文与正确答案拼接为 `clean`；PISA 在不公平设置下将女性/男性样本分别赋高/低分，HolisticBias 则可用角色扮演提示生成更多有毒样本。这里的 `clean`/`poison` 是实验中的公平性标签和合成规则，不自动等于安全系统的良性/恶意来源标签。
- **偏置及审查后结果**（pp. 5–7）：增加不公平比例时，多数实验条件下公平性下降；部分审查实验中，某些类别的偏置会影响另一些类别，但方向随类别和模型变化。作者以实验标签为零的 `clean RAG` 与 No-RAG 比较，发现部分公平性指标仍恶化；其将原因解释为检索内容让模型更少选择“未知”，这是作者对实验现象的解释，不是已识别的普遍因果机制。
- **可复核分母**（p. 25 Table 10）：在该表 GPT-4o 的完全审查条件下，四格分别为 201、19、129、697，总计 **1046 个配对样本**；其中 129 个从 No-RAG 非偏置变为 RAG 偏置，19 个反向变化。这个分母仅属于该表对应条件，不能推广为全部任务、模型或独立 query 数；它也不是投毒攻击成功率。
- **治理与干净数据对照**（pp. 8、25–26）：作者比较稀疏检索、重排序、query 扩展、摘要、安全提示和数据 moderation；摘要在这些公平性实验中有一定效果。p. 26 Table 12 对 unfairness 0.0 和 1.0 分开报告，提供干净条件及干预前后对照的设计思路；例如 GPT-4o 的 unfairness 0.0 行，摘要列为 0.031，No-RAG 为 0.037。不能由此推导恶意证据检出率、干净 query 误删率或通用问答质量保证。

## 口径和证据边界

1. **不公平比例存在待澄清差异**：p. 5 将 `p=0.2` 描述为外部数据中 20% 不公平；p. 19 Algorithm 1 在 `Calibration` 前给出干净数 `n_s/(1+p)` 与 poison 数 `p n_s/(1+p)`，直接相除得到 poison 占比 `p/(1+p)`，例如 `p=0.2` 为约 16.7%，`p=1` 为 50%。伪代码随后的 `Calibration` 细节未在已读段落中明确，实际最终比例及实现需要作者代码或数据确认；不能据此断言最终实验比例必然错误，也不能不加说明地复用其 20% 作为污染成功阈值。
2. **公平性公式与表值须核实**：p. 22 Table 3 将 PISA 的组间 FPR/TPR 差写为绝对值，p. 23 Table 5 却有 Qwen3-14B 的 No-RAG FPR `-0.018`、Llama3.2-3B 的 p=0 TPR `-0.005`。可能是实现口径或排版问题，本文未核代码，不能将其解释为常规的绝对差。BBQ 的 bias score 分母与拒答处理见 p. 22，不能与安全 FPR 混用。
3. **统计和适用性**：作者的 p 值及图表仅支持其所测数据、模型和指标；`clean` 基于任务特定公平性标注，不能证明知识真实、来源可信或无攻击。p. 9 承认缺少各层风险的严格理论证明。对该 PDF 的文本和链接扫描未发现本文代码链接；不据此断言代码不存在。

## 与开题 A / B 的关系

| 对照项 | 正式版已读范围的证据 | 可借鉴与限制 |
|---|---|---|
| A：单一真实源、未知分块 | pp. 5、18–19 构造多条训练样本/QA 语料；未给出单一真实源受限修改、未知 chunker。 | 合成偏置与不同污染比例可作为探索性数据构造参考；攻击权限与真实来源约束不相同。 |
| A：同 query 下同源互补块共召回及共同必要性 | p. 17 检索 Top-5；已读正文和定向附录未报告来源归一、同源互补双块以及逐块/联合删除。 | Top-5 本身不证明同源共召回或两块共同必要。 |
| B：检索后恶意证据识别与来源治理 | p. 8 使用数据 moderation 和摘要等；其目标是公平性/毒性，未报告按块恶意标签、来源认证或溯源约束。 | 可比较过滤或摘要前后的公平性结果；不能将公平性得分当作恶意证据标签。 |
| B：干净 query 误删与效用 | pp. 25–26 将零偏置条件作为对照，但未报告 query 级误删事件、阈值校准或受误删影响的 QA 准确率。 | 可借鉴保留干净条件及 No-RAG 对照；尚不能作为误删预算或效用保证。 |

上述“未见”只指声明的正式 PDF 已读页码，未扩展为对未读附录、作者稿或作者全部实验的断言。
