---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-15a5b08d7ec7
reading_level: L3
checked_date: 2026-11-15
---
# Decomposition, Think, and Action: Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph

**阅读状态：L3（作者接受稿正文）。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Yi Sui", "Chaozhuo Li", "Litian Zhang", "Dawei Song", "Haiming Liu"]
- **机构**：作者接受稿首页：Yi Sui—Beijing Institute of Technology；Chaozhuo Li—Beijing University of Posts and Telecommunications；Litian Zhang—Beihang University；Dawei Song—Beijing Institute of Technology与The Open University；Haiming Liu—University of Southampton。机构按所读版本登记。
- **年份 / 会议 / track**：2026 / TOIS / journal article
- **发表状态**：published_metadata_verified
- **CCF**：正式身份已核等级 ["A"]；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **代码**：未核实 / 未提取
- **关联标题**：["Decomposition, Think, and Action: Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph"]

## 一句话总结与核心贡献

物理p15–20（印刷13–18）§3.4–3.6：熵增益/分支质量触发检索；构query–document–sentence–entity异质图，ReGAT关系注意力与query对比学习，再保留top3证据路径。内部与外部子图用query条件信号的图拉普拉斯二次型得到SEC，结合外部锚定与指数熵校正仲裁。共享实体关联句须低相似且NLI矛盾才标冲突；另查外部有而内部遗漏的节点，再反馈LLM修正。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 正常多步证据组合/图路径保留是效用邻域；已读范围不研究单真实长源经未知chunker形成的恶意互补双块及固定四格必要性。

**B：** 直接限制“实体关系检查+谱结构可靠度+选择性核验+保留多跳”整体首次的宽主张。SEC为证据图拉普拉斯平滑性，区别于B冻结query–chunk嵌入的尾谱马氏；生成中多轮反馈且需log-prob，并非B生成前至多一次批量核验。没有独立clean-query最大风险分位或最终OR删块误报控制的同一证据。

## 局限、可比性与不确定性

外部来源间独立性未认证；高结构一致性不能认证真值。已读主实验无主动投毒、同源来源预算或安全FPR评测；平衡筛选限制总体效度。p22解释可选ReGAT训练，不能把全部组件都写免训练。p33未来工作主要压缩推理/证据；附录案例及期刊终版未完整阅读，不能把所读版本的范围扩大到全部版本。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### IR01-publisher-deposit

- **书目来源**：[原始页面](https://dl.acm.org/doi/10.1145/3827609)
- **DOI / arXiv**：10.1145/3827609 / 未核实 / 未提取
- **本地PDF**：该摘要报告未关联PDF；已读全文见本笔记其他报告。
- **原始PDF链接**：[出版社PDF](https://dl.acm.org/doi/pdf/10.1145/3827609)
- **实际阅读**：L1；出版社向Crossref提交的题名/摘要/卷期；未读出版PDF

#### 方法、结果与适用条件

## IR01 — Decomposition, Think, and Action: Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph

- DOI：`10.1145/3827609`；正式身份：TOIS 2026，CCF A，journal；作者：Yi Sui; Chaozhuo Li; Litian Zhang; Dawei Song; Haiming Liu
- 阅读：作者接受稿正文物理p3–33逐页阅读（L3），附录物理p37的算法1已读；p1–2为机构封面，参考文献仅浏览，附录案例p38–43及出版终版未完整阅读。
- 本地PDF：[reiag_accepted.pdf](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Decomposition, Think, and Action_ Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph.pdf>)

**元数据/版本**：机构仓库https://oro.open.ac.uk/110775/ 标记Accepted Manuscript；https://oro.open.ac.uk/110775/9/110775.pdf 曾取得，2026-11-15复查返回403，访问状态可能变化。作者稿物理p3仍为模板Vol1/No1/June2026/placeholder DOI；不拿模板覆盖Crossref正式44(6)、10.1145/3827609。

**方法**：物理p15–20（印刷13–18）§3.4–3.6：熵增益/分支质量触发检索；构query–document–sentence–entity异质图，ReGAT关系注意力与query对比学习，再保留top3证据路径。内部与外部子图用query条件信号的图拉普拉斯二次型得到SEC，结合外部锚定与指数熵校正仲裁。共享实体关联句须低相似且NLI矛盾才标冲突；另查外部有而内部遗漏的节点，再反馈LLM修正。

**补充方法与版本边界**：作者稿物理p11–14用负对数似然滑窗触发局部分支，结合路径无环/连通性与NLI一致性筛选，并以候选语义共识及轨迹连贯性选择单条推理路径；p37算法1展示逐步检索、图筛选和反馈，不能当作生成前单次删块。p12将NLI纳入逻辑有效性，p13又称其纯结构性，术语边界需依具体检查实现理解。作者稿标题为“Decomposition, Think and Action”，期刊登记标题为“Decomposition, Think, and Action”，二者以DOI与作者关联，终版未读。

**设置**：p21–22：HotpotAdv308、2Wiki1000（按基线正确/错误平衡筛选）、MuSiQue2417、Bamboogle125；LLaMA3-8B/Qwen2.5 3B/7B；BM25、2018-12-20 Wikipedia、每query取5文档。所谓training-free明确限底层LLM；可选ReGAT需15000样本离线训练。

**作者报告结果**：作者p23 Table2：LLaMA3-8B Hotpot EM39.30→44.10、MuSiQue21.90→22.80（对照DeepRAG；百分点增量分别4.80/0.90）；p28 Table4移除reasoning–evidence interaction时Hotpot EM41.4、MuSiQue19.8，对比完整44.1/22.8。p31检索次数1.8/2.4（Hotpot/MuSiQue），耗时7.9/10.5s；少于CoAT19.5/28.0s但高于Hotpot RAT5.3s。分母不跨表合并。

**与A**：正常多步证据组合/图路径保留是效用邻域；已读范围不研究单真实长源经未知chunker形成的恶意互补双块及固定四格必要性。

**与B**：直接限制“实体关系检查+谱结构可靠度+选择性核验+保留多跳”整体首次的宽主张。SEC为证据图拉普拉斯平滑性，区别于B冻结query–chunk嵌入的尾谱马氏；生成中多轮反馈且需log-prob，并非B生成前至多一次批量核验。没有独立clean-query最大风险分位或最终OR删块误报控制的同一证据。

**局限/当前推断**：外部来源间独立性未认证；高结构一致性不能认证真值。已读主实验无主动投毒、同源来源预算或安全FPR评测；平衡筛选限制总体效度。p22解释可选ReGAT训练，不能把全部组件都写免训练。p33未来工作主要压缩推理/证据；附录案例及期刊终版未完整阅读，不能把所读版本的范围扩大到全部版本。

### IR01-author-text

- **书目来源**：[原始页面](https://oro.open.ac.uk/110775/)
- **DOI / arXiv**：10.1145/3827609 / 未核实 / 未提取
- **本地PDF**：[打开PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Decomposition, Think, and Action_ Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph.pdf>)
- **原始PDF链接**：[机构仓储PDF（复查受限）](https://oro.open.ac.uk/110775/9/110775.pdf)
- **实际阅读**：作者接受稿正文物理p3–33逐页阅读（L3），附录物理p37的算法1已读；p1–2为机构封面，参考文献仅浏览，附录案例p38–43及出版终版未完整阅读。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [Decomposition, Think, and Action: Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Decomposition, Think, and Action_ Alleviating Hallucinations of Large Language Models with Reasoning–Evidence Interactive Augmented Graph.pdf>)
<!-- PDF_LIBRARY_END -->
