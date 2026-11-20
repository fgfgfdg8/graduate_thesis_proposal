---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2608.06947
reading_level: L3
checked_date: 2026-11-12
---
# When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse

**阅读状态：L3。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Yingtao Ren", "Ziyi Zhao", "Yiwei Fu", "Xiao Luo", "Yu-Cheng Chang", "Chin-Teng Lin"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / SIGIR '26 proceedings，pp. 4080–4086；DBLP目录归入“Short Papers”，这是目录分类，不据此认定独立评审轨道。
- **发表状态**：ACM向Crossref登记的正式proceedings article元数据已核；DOI 10.1145/3805712.3809904。arXiv记录与正式版题名、作者一致。
- **CCF**：SIGIR按用户提供的第七版目录为A类（会议级）；不对Short Papers目录分类另赋等级。
- **引用量**：见[元数据汇总](../../RAG安全文献补查元数据_20261102.md)。
- **代码**：代码：PDF第1页明确 https://github.com/yingtaoren/D-Scan.git 。
- **关联标题**：["When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse"]

## 一句话总结与核心贡献

方法：生成时提取token及document注意力熵、方差、密度，按文档长度归一化注意力，再训练线性分类器。与B共享“低维统计+小分类器”和跨文档分配信号；不是B的检索器embedding异常，也不需要B命题图。依赖能读取生成器注意力，部署阶段和黑盒适用性与B不同。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 限防御分工；已读范围未专门验证未知分块下同源互补双块威胁。

**B：** 直接机制近邻：D-SCAN从生成器提取token/document级注意力熵、方差、密度并训练线性分类器，故“轻量注意力统计+线性检测”不能单独作为新颖性主张。它依赖生成时可访问模型注意力；B需明确区分信号对象、检测阶段、来源/命题关系和clean-query校准，并在同等误报与正常多跳保留口径下验证增量。

## 局限、可比性与不确定性

局限：高注意力集中也可出现在正常答案证据上；目前已读实验没有覆盖全部自然集中/更新/互补场景。论文将注意力统计当机制线索，相关性不自动构成因果解释。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### arXiv v1：2608.06947v1

- **书目来源**：[原始页面](https://arxiv.org/abs/2608.06947v1)
- **正式版本**：ACM登记为SIGIR '26 proceedings article，pp. 4080–4086；在线出版日期2026-07-19。Crossref所载作者、题名与arXiv一致。[DOI记录](https://doi.org/10.1145/3805712.3809904)；[arXiv v1](https://arxiv.org/abs/2608.06947v1)；[DBLP SIGIR 2026目录](https://dblp.org/db/conf/sigir/sigir2026.html)。
- **DOI / arXiv**：10.1145/3805712.3809904 / 2608.06947
- **本地PDF**：[打开PDF](../pdf/D07__dscan__arxiv2608.06947v1__f31025a245__f31025a24531.pdf)
- **原始PDF链接**：[公开PDF](https://arxiv.org/pdf/2608.06947v1)
- **实际阅读**：L3仅对应arXiv v1；已读PDF正文第1–5页全部，§1–2、§3.1–3.3、§4.1–4.4/Table 1–3、§5；第6页参考文献未系统核验。正式proceedings版本未另行阅读，无附录正文信用。

#### 方法、结果与适用条件

### D07. D-SCAN — 生成器注意力统计+线性检测（中撞车，L3）

- 标题：When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse。
- 全部作者：Yingtao Ren; Ziyi Zhao; Yiwei Fu; Xiao Luo; Yu-Cheng Chang; Chin-Teng Lin。
- 发表身份：ACM向Crossref登记为SIGIR '26正式proceedings article，pp.4080–4086，在线出版日期2026-07-19；DOI为10.1145/3805712.3809904。DBLP目录将条目置于“Short Papers”栏目；这只确认目录组织方式，未证明独立评审track。SIGIR依所给第七版CCF目录为A，按会议级记录。
- arXiv:2608.06947v1，2026-08-07；正式版：[DOI记录](https://doi.org/10.1145/3805712.3809904)；[arXiv记录](https://arxiv.org/abs/2608.06947v1)；[DBLP SIGIR 2026目录](https://dblp.org/db/conf/sigir/sigir2026.html)。本地阅读PDF为arXiv v1，非另行下载/阅读的ACM版本。
- 代码：PDF第1页明确 https://github.com/yingtaoren/D-Scan.git 。
- 原报告按题名/缩写/ID检索未命中；现已并入报告第11.4节，不另设增量章节。
- 已读：PDF正文第1–5页全部，§1–2、§3.1–3.3、§4.1–4.4/Table 1–3、§5；第6页参考文献未系统核验。无附录正文，L3。
- 方法：生成时提取token及document注意力熵、方差、密度，按文档长度归一化注意力，再训练线性分类器。与B共享“低维统计+小分类器”和跨文档分配信号；不是B的检索器embedding异常，也不需要B命题图。依赖能读取生成器注意力，部署阶段和黑盒适用性与B不同。
- 多跳证据：HotpotQA、2Wiki、MuSiQue；top5中替换两块而非真实未知分块下摄入。主要是检测AUC/F1，不是净化后的正常桥接保留或低query-FPR证明。Table 1主结果10次采样，Table 2单次仍有AUC>0.8；不能把主结果成本写成单次生成。
- 局限：高注意力集中也可出现在正常答案证据上；目前已读实验没有覆盖全部自然集中/更新/互补场景。论文将注意力统计当机制线索，相关性不自动构成因果解释。
- 关键原文（第4页，19词）：“we train a linear classifier using attention distribution metrics at both the token-level and document-level as features”。
- 记录核对：arXiv v1、ACM向Crossref登记的DOI元数据、DBLP目录；未决：目录“Short Papers”是否对应会内独立评审轨道、正式版与arXiv版的细微版本差异。和NPAS/AV Filter的机制差异仍应并排比较。

<a id="D08"></a>

## 待核事项与追溯

正式发表元数据与会议级CCF身份已核；正式proceedings版未另行阅读，L3仍只代表arXiv v1正文范围。DBLP目录分类不等于已证实的独立track；未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../RAG安全证据地图_20261102.md) · [全部逐篇笔记](../README.md)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/When Context Bites_ Detecting RAG Poisoning via Document-Level Attention Collapse.pdf>)
<!-- PDF_LIBRARY_END -->
