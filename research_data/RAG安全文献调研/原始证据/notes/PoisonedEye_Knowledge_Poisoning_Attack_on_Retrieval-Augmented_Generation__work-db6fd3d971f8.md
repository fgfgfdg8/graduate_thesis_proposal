---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-db6fd3d971f8
reading_level: L3
checked_date: 2026-11-16
---
# PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models

> **2026-11-15链接复核范围：** 此前仅核对本地PDF首末页、版本标识、页数、已有哈希和可验证链接；那次核验未扩大阅读记录。

**阅读状态：L3（正文）。** 既有2026-11-15核读记录覆盖本笔记所列、哈希匹配的PMLR版PDF物理pp.1–9正文文字和p.10影响声明；2026-11-16本次只补读物理pp.13–20附录A–K的文字与表格，并对pp.18–20的图5–7作整体目视核对。本次未重读正文；p.10参考文献部分及pp.11–12未在本次核验，不能据此声称这些页面已逐项阅读。未运行代码或独立复现。

**2026-11-15正文补读定位（物理页）：**

- pp.1–2：问题、图文知识投毒和三种攻击的总体定位。
- pp.3–4：多模态检索流程、单样本攻击条件及黑盒/白盒区别。
- pp.5–6：单查询与类别查询优化、实验设置及检索/生成指标。
- pp.7–8：主实验结果，以及检索数、投毒样本数和类别图像数的消融。
- pp.9–10：防御对照、结论及影响声明；p.10其余为参考文献，当时未逐条核实。

**2026-11-16附录补核定位（PDF物理页）：**

- p.13：附录A参数消融、表5；B攻击耗时、表6；C的纯文本检索讨论。
- p.14：C的纯图像检索讨论；D五种预设问题和表7；E实验设定。
- p.15：E三种改写问题及表8；F数据集说明；G单查询目标实验设置和样本数。
- p.16：G表9；H查询文本及I推理提示模板。
- p.17：J的五类目标回答；K案例部分标题。
- pp.18–20：K的图5–7分别展示B、S、C的一例攻击；本次只作整体目视和图中文字核对，不据示例推定总体成功率。

- **作者**：["Chenyang Zhang", "Xiaoyu Zhang", "Jian Lou", "Kai Wu", "Zilong Wang", "Xiaofeng Chen"]
- **机构**：State Key Laboratory of ISN, Xidian University；Key Laboratory of Data and Intelligent System Security, Ministry of Education；School of Software Engineering, Sun Yat-sen University；School of Artificial Intelligence, Xidian University（按论文脚注）
- **年份 / 会议 / track**：2025 / ICML 2025 / main
- **发表状态**：official_proceedings
- **CCF**：正式身份已核等级 ["A"]；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)；本轮未查询Google Scholar，暂不核引用数。
- **代码**：[PMLR官方页面所链接的GitHub仓库](https://github.com/123000001212/PoisonedEye)；未运行或复现。
- **关联标题**：["PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models"]

## 一句话总结与核心贡献

面向vision-language RAG的单个图文知识样本投毒：PoisonedEye-B为不改图像的文本基线，PoisonedEye-S优化毒图以攻击单query，PoisonedEye-C面向类别query；主文将白盒检索器假设用于S/C优化变体。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 单个图文样本预算及类别query泛化是部分近邻。附录D（物理p.14）针对目标类别图像，构造一个图文毒样本，并将5种预设问题全部写入毒文本；表7的平均PSR 84.47%是5种问题对应百分比的算术平均。附录E（pp.14–15）报告3种语义改写问题的PSR分别为70.13%、57.80%、58.08%；作者称构造使用初始问题及4种相似问题，但未列全后者，也未明确表8的3个测试问题是否与构造文本重叠，不能认定这些改写均为未见问题。这些结果限制“单样本无法跨query生效”的宽泛说法，但不涉及一份真实长文本源经未知受害chunker生成的同源块共同召回或逐块必要性。

**B：** 论文区分毒样本检索成功（RSR）与目标回答子串出现率（PSR），可作攻击终点拆分的参照；没有提出检索块检测器、来源认证或clean-query误删率。附录C（物理pp.13–14）讨论仅检索文本时可使用既有PoisonedRAG式文本投毒；该处是可行性讨论，未给出对应的独立纯文本实验结果，不构成本研究的文本chunk级防御先例。

## 局限、可比性与不确定性

主实验使用类别query、2M OVEN-Wiki子集、3个分类数据集（每类10图）、2种retriever、2种LVLM及top-3检索；优化变体要求白盒retriever，不能将S/C泛称为黑盒攻击。类别query设置中B/S/C平均RSR-1分别为49.69%/75.62%/86.91%，RSR-K为58.20%/82.79%/92.41%；K=8时单/双毒样本PSR为51.78%/85.20%。PSR按目标答案子串出现率计算，不能与RSR混称。防御表中随机裁剪后的PSR为45.20%，RoCLIP对原始攻击报告0%、对增强攻击仍为54.52%；只代表论文设定，不能外推为文本块检测或clean-query误删性能。

附录D表7在ImageNet-1k、Siglip-so400m和LLaVA-1.6设定下，5种预设问题的平均RSR-1/RSR-K为95.39%/97.93%，逐问题PSR为42.30%–98.28%；平均数均为5行等权算术平均，掩盖问题间异质性。附录D/E没有明确写出表7/表8每一行的评估样本数，不能把问题数当成样本分母。附录G（物理pp.15–16）称在InfoSeek、Flickr30K及OVEN-Wiki各随机攻击1,000个目标样本；表9使用两个检索器与三个数据集的6行设置，B/S平均PSR为86.40%/87.87%，RSR-1为89.77%/96.60%，RSR-K为99.32%/99.72%，分别是这6行百分比的等权平均。论文此处没有说明不同检索器条件的样本是否完全独立或复用，不能将6行直接解释为6,000个互不重叠样本，也不能推定一个毒样本覆盖所有目标。这些是作者报告结果，未独立复现或作跨论文数值合并。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### pmlr267:zhang25da

- **书目来源**：[原始页面](https://proceedings.mlr.press/v267/zhang25da.html)
- **DOI / arXiv**：PMLR官方记录未列DOI或arXiv；本轮未确认独立arXiv版本。PMLR元数据的publication date为2025-10-06。
- **本地PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/PoisonedEye_ Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models.pdf>)；20页；SHA-256 `13D385038702464A33AD0EE9901E5B815D21181DBF36BF293DE4619E48E852A1`
- **原始PDF链接**：[公开PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25da/zhang25da.pdf)
- **阅读记录**：旧汇总曾声称覆盖PDF物理pp.1–20，但旧局部审计仅列p.1择读及pp.3–6部分章节，不能独立支撑旧记录的全部覆盖范围。2026-11-15已有记录补读正文pp.1–9及p.10影响声明；2026-11-16本次实际补读附录pp.13–20，定位见上。本次没有补核p.10参考文献部分或pp.11–12，也未重读已确认正文。

#### 方法、结果与适用条件

### 22｜PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models — L3

- **study_id / report_id**：pmlr:267:zhang25da / pmlr267:zhang25da。
- **全作者**：Chenyang Zhang, Xiaoyu Zhang, Jian Lou, Kai Wu, Zilong Wang, Xiaofeng Chen。
- **身份**：ICML 2025 / main；official_proceedings；CCF A；DOI None。
- **证据入口**：见上方PMLR官方页面及公开PDF链接；2026-11-15对PDF直链的HEAD请求曾返回200、也曾超时，之后一次HEAD检查返回200；本次未下载远端PDF。
- **早期局部阅读记录**：PDF p.1的摘要和引言为择读；pp.3–6涉及§3威胁模型、§4.1–4.3及§5.1设置，未覆盖§5.2全部结果。该旧记录与累计记录的历史衔接仍无法独立确认；2026-11-15已补读上述正文范围。
- **作者结论**：多模态RAG单个image-text pair投毒；baseline、single-query image optimization和class-query image optimization分属不同攻击设置。
- **我们的A比较**：单样本预算近邻但样本为图文对；不是一真实文本源经未知chunker的两块组合。
- **我们的B比较**：检索及生成条件分列，强调模态对齐；当前B纯文本统计不能直接声称覆盖。
- **限制/未决**：主实验类别query设置、2M OVEN-Wiki子集、3分类基准每类10图、2 retriever/2 LVLM、top-3；S/C优化为白盒retriever。PSR是目标答案子串发生率，与召回RSR分开。未测真实长文本源、受害者未知chunker、文本同源块共同召回/必要性或clean-query最终OR误删率。
- **早期代码记录**：先前记为None；PMLR官方页面现列出上方代码仓库，未审查或运行。
- **评估口径**：pp.4–6：黑盒只baseline；单query与classquery优化均白盒。Query文本固定而类别图像变化不等于实例/topic均未知。
- **论文假设（PDF p.4，归纳）**：单查询与类别查询优化均以检索器白盒访问为前提。
- **代码制品**：PMLR官方论文页直接链接上方仓库；仓库内容、可复现性及运行结果未核。
- **正式身份**：ICML 2025主会，PMLR 267:76811–76830；按第七版CCF目录为A。PMLR官方页未列DOI。

## 待核事项与追溯

仍待核：p.10参考文献部分及pp.11–12的逐项阅读、表7/表8每行样本数及表8测试改写与构造问题是否重叠、表9不同检索器条件是否复用目标样本、PMLR未链接的独立预印本版本、代码内容/运行与复现、跨研究query级样本重叠。L3由既有正文核读支持；附录结果以上述2026-11-16逐页补核为依据。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md)。截至2026-11-15，本笔记尚未纳入版本控制。

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/PoisonedEye_ Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models.pdf>)
<!-- PDF_LIBRARY_END -->
