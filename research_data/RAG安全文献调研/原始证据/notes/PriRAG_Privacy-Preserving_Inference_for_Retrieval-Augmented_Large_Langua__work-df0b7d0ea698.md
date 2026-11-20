---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-df0b7d0ea698
reading_level: L3
checked_date: 2026-11-04
---
# PriRAG: Privacy-Preserving Inference for Retrieval-Augmented Large Language Models

**阅读状态：L3。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Huili Wang", "Yuanhong Huang", "Wenjie Zheng", "Pingyi Fan", "Guoshun Nan", "Shangguang Wang", "Mengwei Xu", "Tao Qi"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / TDSC / Journal
- **发表状态**：official_journal_PDF_complete_main_body_read
- **CCF**：正式身份已核等级 ["A"]；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](<../../../../docs/RAG安全文献补查元数据_20261102.md>)。
- **代码**：未核实 / 未提取
- **关联标题**：["PriRAG: Privacy-Preserving Inference for Retrieval-Augmented Large Language Models"]

## 一句话总结与核心贡献

PriRAG已有query相关块表示压缩、聚合与隐私推理；encoder适配不同冻结特征，多跳正常效用下降、DP条件及成本边界保留。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** PriRAG已有query相关块表示压缩、聚合与隐私推理；encoder适配不同冻结特征，多跳正常效用下降、DP条件及成本边界保留。 完整单真实长源、未知chunker、角色分离、共召回且每块必要的联合设置须逐项比较，不作全球排除。

**B：** PriRAG已有query相关块表示压缩、聚合与隐私推理；encoder适配不同冻结特征，多跳正常效用下降、DP条件及成本边界保留。 不自动涵盖冻结ModernBERT四统计/20维RF、独立clean-query TopK-max及最终G/R/F OR误删校准。

## 局限、可比性与不确定性

- 未读附录、实现不补猜证明条件、N、CI或认定源码错误。
- 未执行作者实现或独立复现；引用量及资源许可按独立侧车。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### R42-PriRAG-official-all-main-L3-20261104

- **书目来源**：[原始页面](https://ieeexplore.ieee.org/document/11540404/)
- **DOI / arXiv**：10.1109/tdsc.2026.3698487 / 未核实 / 未提取
- **本地PDF**：[打开PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/PriRAG_ Privacy-Preserving Inference for Retrieval-Augmented Large Language Models.pdf>)；SHA-256 `7d97e741c61a5ea849c793466467a94b10045040785e66731361d5f6efb825ba`
- **原始PDF链接**：未核
- **实际阅读**：L3；正式12页PDF完整读物理p1–11主文；目视[3, 4, 5, 6, 7, 8, 9, 10, 11]；主文末参考及其后参考/传记仅定位，未授在线附录、源码或独立复现。

#### 方法、结果与适用条件

## R42-PriRAG

- 正式TDSC2026 23(5):10115–10126，CCF A；DOI `10.1109/TDSC.2026.3698487`。publication2026-05-29、current version2026-09-01及Sept/Oct期分开。浏览器官方document11540404显示Southeast University权限，官方PDF链接及已呈现iframe下载12页PDF；页脚2026-11-04 01:51:55UTC。
- 实读p1–11全部主文（p11末参考仅定位），p12参考仅定位；目视p3相关工作、p4 Figure1、p5/6公式、p7设置、p8 Figures2–4、p9/10 TablesI–III及p11 Figure5。在线附录A–D/证明未取得未读，不授源码/实现/独立复现。旧CSDL完整摘要已读，当前是研究登记与主文补充，不重复称新发现该摘要。

**对象与信任边界。** 本地私有库检索后，将受保护知识表示交给云端LLM；保护知识机密性，query本身送云。p9实测对手honest-but-curious，看到query/代理表示、黑盒访问LLM，不知原始知识或encoder参数。不是恶意库完整性检测、文档事实核验或source授权判定；DP不能代替这些性质。论文p7也承认多数商业平台只提供文本API，需embedding输入/平台配合才可部署。

**与B的方法近邻。** p4先训练encoder对齐目标LLM表示空间，p5按query对细粒度块softmax加权聚合，再以参考答案生成损失和完整RAG teacher蒸馏训练。生成LLM冻结不等encoder冻结：SFR-Embedding-Mistral初始化且encoder须适配训练，非冻结ModernBERT直接抽四统计/20维RF。已有“检索后、query相关、低维聚合、选择性保留信息”的先例，不能仅以主题为隐私而排除。p5主动承认严格query压缩会漏必要语义，混入通用表示；B保留低相似度必要前提、否定和跨块关系需专门负控。

**隐私声明的精确边界。** p5–6对各块表示clip并一次高斯扰动，跨query重用同一随机表示；Lemma1是chunk级(ε,δ)-LDP，Lemma2共享噪声重复query，Lemma3同预算噪声方差1/l。证明指向未读AppendixB，因此仅记录作者声明及主文条件，不称已独立验证整个pipeline/任意自适应对手。后处理需要后续计算仅依赖已私有化表示和适当固定的query/其他输入；原始检索选择、知识更新、分块数/文档级组合和外泄原始query如何纳入完整相邻定义仍待证明/实现核对，不能由图数据处理链直接授端到端保证。Eq.(6)前式clip后表示与展开省略clip，Eq.(4)将两个log概率和写入KL，符号/实现待核，不宣判代码错误。不能仅由维度更小无条件推出每坐标噪声1/l，须同邻接/范数/敏感度条件。

**数据、预算与独立性。** p7训练Wikipedia截至2021-12、33.1m中取200k；下游PwC/SQuADv2共37kQA，作者声明评价数据集与训练分开。7测集TriviaQA/HotpotQA/TruthfulQA/2WikiQA/StrategyQA/BioASQ/PubMedQA；四模型Mistral7B、Qwen2.5 7/14/32B。训练1epoch、batch4、warmup.03、β.1、λ2等主文给出。精确测试样本数、同Wikipedia源隔离、seed/重复次数及表中±代表std/SEM/CI未在主文闭合；数据集名分开不自动证明源级独立，也不判实际泄漏已证。p10 TableIII Qwen32适配约8+25=33小时、两A800；47.20MB是原表参数存储量，不改称47.20m参数。在线延迟与离线训练/预计算成本分列。

**不沿用“无效用损失”概括。** p9 TableI RAG→PriRAG的Uavg：Mistral62.78→52.33，Qwen7 56.49→52.22，Qwen14 53.95→56.21，Qwen32 59.29→53.97；逐行差-10.45/-4.27/+2.26/-5.32分值。多跳2WikiQA分别69.13→34.63、49.93→44.70、72.67→47.63、70.50→46.30；MistralHotpot39.73→26.67。这些负例对保留必要证据有直接参考意义，但没有逐chunk必要性删除实验，不能归因某一个模块已证。正文“matching”是作者概括，不覆盖这些逐任务下降。7类效用如何逐任务计分、Uavg异构均值范围待附录；不叫安全ASR/误删率。TableI不是全表同ε：例如Qwen14 LDP-RAGε80与PriRAGε1，另有Figure4同预算对照；不能用主表直接称严格同隐私预算胜出。

**实测隐私不是安全事实性。** p8 Figure2无目标重建平均表现32.95/30.27/21.96/7.80，最后为PriRAG；F1/ROUGE/BLEU词面恢复度在图称ASR，不等成员推断或注入成功率。p10 TableII Pavg按四模型为8.22/5.64/6.51/4.91，针对辅助问题的模型表现；与Uavg相减Trade-off44.11/46.58/49.70/49.06是作者定义评分，不是统一概率风险或DP证明。威胁模板、case在未读AppendixC，不臆造参数或可执行内容。

**成本与迁移证据。** p8 Figure3首token42.70ms、online1078.85ms、context memory.05GB为图中PriRAG标值；比较RAG75.57ms/1106.26ms/.19GB，但未闭合具体模型、每queryN、硬件/传输、预计算和p95，不泛化生产总延迟。不同encoderbackbone仍需适配/训练，不能称任意新LLM无需训练即兼容。Figure4和TableI同ε1个别均值不完全一致，保留报告/配置待核，非推断实现错误。

**后续。** B需分别比较正常多跳效用、丢失前提与隐私目标；不能把DP预算当clean-query TopK-max或最终G/R/F OR误删校准。作者p2明确公开PrivacyRAG项目链接，其代码/数据/模型许可证及固定版本由资源子代理单独核；普通URL存在不授可复现信用。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-e65ab6f347f77396>) · [全部逐篇笔记](<../../../../docs/RAG安全证据地图_20261102.md#paper-notes>)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [PriRAG: Privacy-Preserving Inference for Retrieval-Augmented Large Language Models](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/PriRAG_ Privacy-Preserving Inference for Retrieval-Augmented Large Language Models.pdf>)
<!-- PDF_LIBRARY_END -->
