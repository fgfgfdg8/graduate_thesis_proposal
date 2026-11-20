---
tags: [rag-security-evidence, fairness, retriever, clean-utility]
study_id: arxiv-2502.17390
reading_level: L3
checked_date: 2026-11-16
---
# Mitigating Bias in RAG: Controlling the Embedder

**定位：低优先级的自然社会偏见与干净检索效用参考。** 论文研究模型、嵌入器与语料之间的性别和政治偏向，以及调节嵌入器带来的效用变化；它没有构造与开题 A 相应的受限投毒，也没有检验开题 B 的恶意证据检测和干净 query 误删。

## 身份、版本、去重与阅读范围

- **正式文献**：Taeyoun Kim、Jacob Mitchell Springer、Aditi Raghunathan、Maarten Sap，*Findings of the Association for Computational Linguistics: ACL 2025*，2025 年 7 月，18999–19024，DOI `10.18653/v1/2025.findings-acl.974`。[ACL Anthology 正式条目](https://aclanthology.org/2025.findings-acl.974/)；[正式版 PDF](https://aclanthology.org/2025.findings-acl.974.pdf)。
- **作者稿**：[arXiv:2502.17390v1](https://arxiv.org/abs/2502.17390v1)，2025-02-24；截至本次核验，arXiv 提交历史仅列 v1，作者稿页面第二作者署名 Jacob Springer，正式版列 Jacob Mitchell Springer。本文按实际阅读的正式版著录；未逐字比较两个版本，不能假定各项实验完全一致。
- **CCF**：用户提供的[第七版目录](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F) PDF 物理第 57 页列 **ACL 主会为 A 类**；[第七版CCF正式发布说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml)明确指出 Findings 不计入该目录的考虑范围，故本篇不标为主会的 A/B 类。所用本地目录与上述官方文件 SHA-256 均为 `271b630b576bf8a4f802e767f5694caded93680e22b3a19bef7902591c45c1d3`。
- **本地已读文件**：[论文库正式 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Mitigating Bias in RAG_ Controlling the Embedder.pdf>)，26 个物理页，SHA-256 `1aae319ba7a87bf36393862955164fc83eaea2ff492569f86fab09170e4f54d6`；从上述 ACL 官方 PDF 下载。论文库位于仓库之外，不随仓库检出。
- **去重**：既有 ACL Findings 2025 目录快照已收录论文题名、DOI 和摘要；本机 `catalogs/catalog_acl_findings_sources/articles.jsonl` 的对应记录未声称 PDF 已读，`catalogs/local_catalog301_parent_sources/catalog301/no_exact_registered_study_queue301.jsonl` 对既有独立研究与正文阅读状态保留未知。两份快照被 Git 忽略，其他机器默认不可取得；公开书目请核对上方 ACL 条目。本次按 DOI、题名、arXiv ID 搜索三份报告和研究库笔记，未发现独立正文阅读条目；这是对既有目录候选的正文补读。上游参考见 [Bias Amplification 笔记](Bias_Amplification_in_RAG_Poisoning_Knowledge_Retrieval_to_Steer_LLMs__arxiv-2506.11415.md)。
- **阅读状态：L3（正式版主文）**。2026-11-16 读取 PDF 文本层的物理页 1–10（正文、结论与限制；末页开始参考文献），并定向读取附录页 14–17、19、25。以下页码均为这份 PDF **物理页**，印刷页 = 物理页 + 18998。未逐页精读参考文献及其余附录，未逐张目视检查图像，未运行代码或复现实验。引用数未核实，保持未知。

## 方法和实验

- **对象与指标**（pp. 2–4）：研究两组二元社会偏向，分别为女性/男性、保守/自由。每个文本对两组各赋一个 0/1 指示，跨样本对两者之差求平均；范围为 `[-1,1]`。`E_b` 是在指定语料上对每个 query 的 **Top-1 检索结果**求该偏向平均，因此同时包含语料分布的影响，并非只由嵌入器参数决定。作者用 `R_b = s E_b + L_b + ε` 描述 RAG 输出偏向与检索偏向的经验关系；这是所测设定下的模型，不是针对对抗污染的保证。
- **数据与模型**（pp. 4–6）：GENDERBIAS-QA 的训练/测试 query 数为 172/145，POLITICBIAS-QA 为 600/200；任务设计允许不同性别人物或不同立场答案均可被视为合适输出。作者以 GTE-base 为基础构造每任务 60 个不同微调配置，共 120 个；从每任务选择 20 个覆盖偏向范围的嵌入器，分别与 6 个 LLM 组合，因此对应 2×20×6=240 个任务-嵌入器-LLM 组合。主要实验为余弦 Top-1，另测 E5-base-v2。不存在针对同一真实源切块的攻击构造。
- **干预方式**（pp. 5–7）：用对比学习促使嵌入器更常检索女性或保守立场相关文本，比较只调末几层的 PEFT 与全参数微调后插值的 WiSE-FT。作者观察到在部分任务/模型中，适度反向偏置嵌入器能抵消系统层面的原有偏向；最优值随 LLM 和任务而异，低敏感度条件下可能无法达到目标，不能推广为任何系统均可逆向调节成功。
- **干净效用及分母**（pp. 7、16、19）：Table 4/6 报告 BEIR 任务子集的 `NDCG@1`，附录列 TREC-COVID、NFCorpus、SciFact、FiQA-2018、ArguAna、Quora、SCIDOCS。基线 GTE-base 为 0.526；Llama 8B 对应的最优性别嵌入器为 0.519，而最优政治嵌入器为 0.481，分别下降 0.007 和 0.045 个**绝对指标点**。表格没有给出逐数据集数值或误差条，不能将此概括为所有任务无损。作者另以 Llama 8B + RAG Mini-Wikipedia 的问答准确率作验证，但本次未从图中估算数值；常规 NDCG/QA 效用也不等于 query 级恶意证据误删率。
- **语料变化及边界**（pp. 7–9）：小型平衡语料分别含 352 条性别相关文档（176/176）和 2564 条政治相关文档（1282/1282）。在作者构造的小范围语料偏向扰动下，最优嵌入器的效果较稳定；重度偏置的嵌入器会破坏部分线性关系。该合成/采样试验不提供任意来源、投毒或分布转移下的稳健保证。作者承认部署前的最优嵌入器选择、跨任务敏感度、多偏向交叉和复杂 RAG 的问题仍未解决。
- **标注限制**（pp. 14–16）：作者用 GPT-4o-mini 评估文本的组别偏向；针对政治文档，100 条验证集上模型与人工平均一致率 60.0%、Cohen κ=0.3874，人工两两平均一致率 64.0%。该小样本评估不证明标注对其他领域、性别或恶意性识别可靠。

## 与开题 A / B 的关系

| 对照项 | 正式版已读范围的证据 | 可借鉴与限制 |
|---|---|---|
| A：单一真实源和未知切块 | pp. 4–6 操纵的是嵌入器训练，实验使用多个公开语料；主要检索 Top-1。 | 可参考系统组成部分影响输出的分析，未覆盖单源受限修改与未知分块。 |
| A：同 query 共召回及共同必要性 | 已读正文未报告同源互补双块、共召回或逐块/联合删除。 | Top-1 设置尤其不能完成所需的双块共召回实验。 |
| B：检索后恶意证据识别与来源治理 | 干预发生在嵌入器微调、投影或采样，标签描述社会偏向；未报告恶意证据标签或来源认证。 | 不能把社会偏向分类器当作攻击检测器，也不能把调整检索排序当作检索后证据删除。 |
| B：干净 query 误删及问答效用 | pp. 6–7、16、19 使用 QA 验证和 BEIR NDCG@1；未报告干净 query 误删预算与安全检测阈值。 | 可借鉴同时报告干预前后的检索及问答效用；需另行设计 query 级误删指标和独立校准集。 |

## 代码与可复现范围

正式版 p. 2 给出作者[代码与数据仓库](https://github.com/danielkty/debiasing-rag)。2026-11-16 仓库页面与 README 可访问，README 自述包含两个 QA 数据集及训练、推理代码；本次只核对入口，**未审计实现、下载制品或运行复现**。上述“未见”只指声明的正式 PDF 已读页码，不扩展为对未读附录或其他版本的断言。
