---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2603.23293
reading_level: L3
checked_date: 2026-11-12
---
# TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning

**阅读状态：L3。** 已逐页读取正式Findings PDF物理页1–15，覆盖正文、局限、参考文献及附录A–C文字；不表示逐图视觉审读、代码运行、独立复现或预印本逐版复核。

- **作者**：["Muhaimin Bin Munir", "Akib Jawad Ononto", "Nazia Shehnaz Joynab", "Bhavani Thuraisingham", "Latifur Khan"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / EMNLP / Findings
- **发表状态**：published
- **CCF**：EMNLP在CCF第七版目录列为B类会议（目录PDF第58页）；本文正式track为Findings，目录未单独列出该track等级，按项目口径不将主会等级赋给Findings单篇，记为“Findings，未单独评级”。
- **引用量**：见[元数据汇总](../../RAG安全文献补查元数据_20261102.md)。
- **代码**：代码：正式PDF第2页脚注确认 https://github.com/akibjawad14/tris 。
- **关联标题**：["TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning"]

## 一句话总结与核心贡献

方法：独立嵌入空间多数簇过滤，query前缀结构/词项重叠筛查，再由LLM以无上下文内部答案为参照逐文档验证；不确定/调用失败保留；推荐前两层意见不一致时自适应调用第三层。后者直接覆盖“便宜初筛+按需LLM复核”架构，不能再把该级联本身列成空白。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 限防御分工；已读范围未专门验证未知分块下同源互补双块威胁。

**B：** B差异：四统计+冻结ModernBERT/RF/clean-query分位校准；显式源文档偏移、桥接实体、带时态条件命题图；异源外部参照；一次批量核验。TRIS主要逐文档相对参数知识，未见上述来源图与query级误报控制。

## 局限、可比性与不确定性

证据评价：正式版§6.2已撤回对公平配置TrustRAG的自适应ASR优势。附录B.3的独立几何消融也未显示显著收益：NQ中MiniLM/Contriever的ASR为32%/33%（p=.88），HotpotQA为44%/53%（p=.20）；作者据此把实测收益主要归于Layer 2，而非Layer 1使用独立嵌入空间。不能沿旧版用“三层独立必然更强”叙述。

**补读结果与边界：**

- Table 5的live-retrieval配对实验（k=50，n=100）中，启用Layer 3后NQ的ASR/CleanAcc由32%/43%变为15%/61%，HotpotQA由44%/34%变为31%/45%；这只支持本文设置下的改善，不等于总体误删率保证。
- 附录B.2强制将毒文档置顶时，完整系统ASR为33%，高于live-retrieval主结果；附录B.4将注入数扩到6–20篇的结果仅来自NQ子样本n=25。附录B.5显示k=5时ASR为85–93%、CleanAcc为9–17%，k≥10后才在该扫描中稳定于3–4% ASR；不可概括为对检索深度不敏感。
- 附录C的HotpotQA两跳失败例中，毒文档仿写真实Wikipedia段落、仅替换答案实体，绕过前两层；因替代实体本身合理，Layer 3信号也弱。作者将这类模仿归因于大部分残余14% HotpotQA ASR，且多跳任务只需破坏一跳即可成功。
- 正文Limitations明确：没有实测judge-aware或完整white-box攻击；实验来自NQ、HotpotQA、MS-MARCO各100条问题子集而非全语料；部分比较为n=30单次运行；没有形式化鲁棒保证。Layer 3依赖验证模型的参数知识，10条模型知识缺失的post-cutoff问题上其全部弃答（fail-open），但该切片中Layer 1–2移除30/30毒项且未误删50条干净文档。作者报告Layer 3约2.9秒/查询，live retrieval下附加成本约16–19秒/查询。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### emnlp2026-findings2122

- **书目来源**：[原始页面](https://aclanthology.org/2026.findings-emnlp.2122/)
- **DOI / arXiv**：10.18653/v1/2026.findings-emnlp.2122 / 2603.23293
- **本地PDF**：[打开PDF](../pdf/D03__tris__emnlp2026-findings2122__e78fa9ed54__e78fa9ed54f9.pdf)
- **原始PDF链接**：[公开PDF](https://aclanthology.org/2026.findings-emnlp.2122.pdf)
- **实际阅读**：L3；正式PDF物理页1–15完整读取，覆盖§1–8、Limitations、参考文献及附录A–C；包括Table 5–10和Appendix C案例。SHA-256 `e78fa9ed54f9a52f3920c7824a6c6ac263459841468e1c4aab5a36ef518d6106`；未逐图视觉审读、运行代码或独立复现。

#### 方法、结果与适用条件

### D03. TRIS — 多信号级联+自适应LLM（高撞车，L3）

- 标题：TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning。
- 全部作者：Muhaimin Bin Munir; Akib Jawad Ononto; Nazia Shehnaz Joynab; Bhavani Thuraisingham; Latifur Khan。
- 正式发表已核：Findings of EMNLP 2026，45250–45264，会议2026-10-24至29。不是仅arXiv，也不是EMNLP主会。CCF：EMNLP整体为B；第七版目录未单列Findings track等级，按项目口径不赋主会等级给本文。
- DOI：https://doi.org/10.18653/v1/2026.findings-emnlp.2122 。官方页/PDF：https://aclanthology.org/2026.findings-emnlp.2122/ 、https://aclanthology.org/2026.findings-emnlp.2122.pdf 。预印本：arXiv:2603.23293。
- 代码：正式PDF第2页脚注确认 https://github.com/akibjawad14/tris 。
- 现有报告：正式Findings身份已核，DOI与官方PDF见上。
- 已读：正式PDF物理页1–15完整读取，正文、局限、参考文献及附录A–C；L3。未逐图视觉审读、运行代码或独立复现。
- 方法：独立嵌入空间多数簇过滤，query前缀结构/词项重叠筛查，再由LLM以无上下文内部答案为参照逐文档验证；不确定/调用失败保留；推荐前两层意见不一致时自适应调用第三层。后者直接覆盖“便宜初筛+按需LLM复核”架构，不能再把该级联本身列成空白。
- B差异：四统计+冻结ModernBERT/RF/clean-query分位校准；显式源文档偏移、桥接实体、带时态条件命题图；异源外部参照；一次批量核验。TRIS主要逐文档相对参数知识，未见上述来源图与query级误报控制。
- 证据评价：正式版§6.2已撤回对公平配置TrustRAG的自适应ASR优势；Appendix B.3显示独立嵌入空间替换无显著差异（NQ p=.88；HotpotQA p=.20）。Table 5 live retrieval中Layer 3改善ASR与CleanAcc，但HotpotQA仍有多跳模仿失败；Appendix B.5在k=5时显著失稳。§6.5自适应L3仅在21% HotpotQA查询触发；Layer 3约2.9秒/查询，live-retrieval下附加成本约16–19秒/查询。部分基线比较n=30单次运行，不能分辨几百分点差异；论文不提供形式化鲁棒保证。
- 关键原文（第4页，12词）：“adaptive, invoked only when Layers 1 and 2 disagree”。
- 检索："TRIS" "Retrieval Integrity"。仍未解决：与B在同一预算下的来源关系检测及多跳桥接保留直接比较；代码未运行。

<a id="D04"></a>

### LIB058-preexisting-PDF-title-20261102

- **书目来源**：未核
- **DOI / arXiv**：未核实 / 未提取 / 2603.23293
- **本地PDF**：[打开PDF](../pdf/0cfb36b28844d919ea79b967e1bbacda9d6a38d5e5a51768__0cfb36b28844.pdf)
- **原始PDF链接**：未核
- **实际阅读**：L1；仅既存PDF前两页中完整题名、版式及poster/附录提示核对；不声称完整摘要阅读，方法/设置/结果/局限未在本次题名核对中阅读。

#### 方法、结果与适用条件

### LIB058 — TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning

L1：仅既存PDF前两页中完整题名、版式及poster/附录提示核对；不声称完整摘要阅读，方法/设置/结果/局限未在本次题名核对中阅读。

本地归档PDF：[PDF_version_unverified](../pdf/0cfb36b28844d919ea79b967e1bbacda9d6a38d5e5a51768__0cfb36b28844.pdf)
原库文件名：`TRIS- A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning.pdf`；同研究关联：`arxiv-2603.23293`。正式书目、PDF版本与方法判断以独立原文报告为准。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../RAG安全证据地图_20261102.md) · [全部逐篇笔记](../README.md)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/TRIS_ A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning.pdf>)
- [TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/版本/0cfb36b28844/TRIS_ A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning.pdf>)
<!-- PDF_LIBRARY_END -->
