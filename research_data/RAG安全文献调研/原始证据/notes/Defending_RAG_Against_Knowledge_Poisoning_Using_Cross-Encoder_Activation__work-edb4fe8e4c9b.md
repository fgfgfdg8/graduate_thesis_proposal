---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-edb4fe8e4c9b
reading_level: L3
checked_date: 2026-11-02
---
# Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals

**阅读状态：L3。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Razieh Moradi", "Havva Alizadeh Noughabi", "Fattane Zarrinkalam", "Ali Dehghantanha"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / Canadian AI / Main conference
- **发表状态**：published
- **CCF**：正式身份已核等级 未核实 / 未提取；作者声称或关联venue等级 未核实 / 未提取。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **代码**：代码：PDF第1页明确给出 https://github.com/CyberScienceLab/CEG-RAG ，含代码和数据声明；本次未运行。
- **关联标题**：["Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals"]

## 一句话总结与核心贡献

方法证据：query–passage末层重排器表示构成矩阵；共享投影+Set Transformer显式建模同组chunk交互；attention MIL做bag级检测，chunk head定位；分组概率取最大值，双阈值触发过滤与按原重排顺序补齐。只用上下文标签弱监督。不能把它概括成“单块检测、完全没有跨块交互”。
补全文：Set Transformer交互限每K块bag内部，各bag独立处理后max作query/context gate；只有context过τdet才按chunk τloc过滤/补齐。不是跨所有bag的显式关系图，也没有干净query共形校准。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 限防御分工；已读范围未专门验证未知分块下同源互补双块威胁。

**B：** 与B重合：冻结/现成重排编码器的联合表示作为安全信号、低成本监督头、上下文级判别与chunk定位、过滤后保持证据预算。B的RF与四统计替代MIL并非天然创新，必须有同一编码器/同一划分下的消融和成本比较。
差异（限已读）：B增加干净query最大分位校准及显式来源/偏移/实体/命题关系，采用选择性LLM；本篇为隐式集合交互而非上述物理来源图。未见其评估同源互补前提与未知分块变化。
正文补全后：CEG-RAG同样先context gate再做chunk过滤，故干净query最终删块事件包含于context flag，但其FPR仅实测，未给分位/共形控制。B若加入关系OR绕过统计gate，需要另说明最终误删保证。本文交互范围每K块bag内；来源/偏移/实体/条件命题图和LLM复核正文未实现。

## 局限、可比性与不确定性

证据评价：三QA集，仅一个主要投毒族；HotpotQA Table 1中ASR 16.28%、ACC 13.95%，不能用ASR低推断多跳效用保留。第5页MS-MARCO块级FPR=0.1125，正文摘要“very low FPR”不适用于全部配置。§3.1未清楚交代查询/源文档训练测试隔离，需作者/代码补证。
作者§4 p8明确三项边界：单一PoisonedRAG威胁、必须访问内部reranker激活、固定retriever/generator；虽测多个reranker，不能当跨检索器/生成器验证。Table3 HotpotQA CEG ACC13.95 vs TrustRAG46.40，NQ41.06 vs59.35，低ASR不代表效用最优。RAGuard [26]为Kolhe等NeurIPS2025 workshop版本，不是D24 Cheng的BigData RAGuard。p5把该baseline的leave-one-out描述为incorrect→correct翻转，其测试实现如何判正确/是否可部署尚未核，不能忽略接口公平性。正文仍未明确query/source级train-test隔离或阈值校准单位，未审代码。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### pmlr318-moradi26a

- **书目来源**：[原始页面](https://proceedings.mlr.press/v318/moradi26a.html)
- **DOI / arXiv**：未核实 / 未提取 / 未核实 / 未提取
- **本地PDF**：[打开PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals.pdf>)
- **原始PDF链接**：[公开PDF](https://raw.githubusercontent.com/mlresearch/v318/main/assets/moradi26a/moradi26a.pdf)
- **实际阅读**：L3；正式PDF p1–9正文全部；本次补读p8 Table3/§4 Limitations/§5、p9 §6 Conclusion/披露，浏览p9–11参考文献但未逐条外部核验；再核p3–5方法/设置。此11页正式PDF未含附录。

#### 方法、结果与适用条件

### D01. CEG-RAG — 重排器表示+集合交互（高撞车，L3正文）

- 标题：Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals。
- 全部作者（正式PDF）：Razieh Moradi; Havva Alizadeh Noughabi; Fattane Zarrinkalam; Ali Dehghantanha。本次正式网页、BibTeX与PDF第二作者均为Noughabi；不沿用旧记录中的作者拼写疑点。
- 正式发表：The 39th Canadian Conference on Artificial Intelligence，2026，PMLR 318；官网给出事件日期2026-05-25至29。CCF：所给目录未列Canadian AI，不借用AAAI等级。
- 官方页：https://proceedings.mlr.press/v318/moradi26a.html 。正式PDF：https://raw.githubusercontent.com/mlresearch/v318/main/assets/moradi26a/moradi26a.pdf 。未见DOI/arXiv号，勿编造。
- 代码：PDF第1页明确给出 https://github.com/CyberScienceLab/CEG-RAG ，含代码和数据声明；本次未运行。
- 现有报告：已覆盖，CEG-RAG/CEGRAG字符串多处命中（例第43、59、1466行）。覆盖不代表已正确比较集合交互。
- 已读：正式PDF第1–9页正文全部；本次补读第8页Table3/§4 Limitations/§5、第9页§6 Conclusion/披露，并浏览第9–11页参考文献（未逐条外部核验）；再核第3–5页方法/设置。此11页正式PDF没有附录，L3正文。
- 方法证据：query–passage末层重排器表示构成矩阵；共享投影+Set Transformer显式建模同组chunk交互；attention MIL做bag级检测，chunk head定位；分组概率取最大值，双阈值触发过滤与按原重排顺序补齐。只用上下文标签弱监督。不能把它概括成“单块检测、完全没有跨块交互”。
- 与B重合：冻结/现成重排编码器的联合表示作为安全信号、低成本监督头、上下文级判别与chunk定位、过滤后保持证据预算。B的RF与四统计替代MIL并非天然创新，必须有同一编码器/同一划分下的消融和成本比较。
- 差异（正文已读完）：B增加干净query最大分位校准及显式来源/偏移/实体/命题关系，采用选择性LLM；本篇为隐式集合交互而非上述物理来源图。未见其评估同源互补前提与未知分块变化。
- 证据评价：三QA集，仅一个主要投毒族；HotpotQA Table 1中ASR 16.28%、ACC 13.95%，不能用ASR低推断多跳效用保留。第5页MS-MARCO块级FPR=0.1125，正文摘要“very low FPR”不适用于全部配置。§3.1未清楚交代查询/源文档训练测试隔离，需作者/代码补证。
- 关键原文（PDF第3页）：“apply a Set Transformer [19] encoder to model interactions among the K chunks”。
- 检索："CEG-RAG"；"Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals"。状态：正式发表已核；PMLR页码366–376。

- 本次正文补全核准（p3–5、8–9）：Set Transformer建模**同一固定K块bag内部**的交互，各bag独立，之后max作context级flag；不能把它说成逐块互不相关，也不能反过来当成跨整个候选集任意关系均已建模。只有context gate通过才按chunk阈值删除/补齐，未给clean-query有限样本分位或共形保证；对全clean query，至少一次删除包含于context flag，但这里只报告实测FPR。B独立关系OR可绕过统计初筛，两者保证入口并不相同。
- 作者明确局限（p8 §4）：只评单一PoisonedRAG；需访问cross-encoder内部激活，黑盒/专有重排服务未必可用；固定retriever/generator，虽测三reranker也不能外推其他检索/生成模型。正文未给未知分块/同源互补双块实验，未明确query/源文档级train-test隔离和阈值校准单位；这些仍为代码/作者待证，不伪装成已核。
- 结果与公平性边界（p8 Table3，p5设置）：MS-MARCO CEG ACC50.00/ASR11.20；NQ41.06/6.30，相对TrustRAG59.35/16.26；HotpotQA13.95/16.28，相对TrustRAG46.40/23.60。因此不能只按更低ASR称全面更优，尤其正常多跳效用未由HotpotQA参测自动证明。参考[26]是Kolhe等NeurIPS2025 workshop RAGuard，**不是D24 Cheng BigData RAGuard**。正文对其leave-one-out基线的描述依赖incorrect→correct翻转，如何判正确及部署可观测性需另核实现；本次未据描述断言基线就是oracle或错误复现。

<a id="D02"></a>

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Defending RAG Against Knowledge Poisoning Using Cross-Encoder Activation Signals.pdf>)
<!-- PDF_LIBRARY_END -->
