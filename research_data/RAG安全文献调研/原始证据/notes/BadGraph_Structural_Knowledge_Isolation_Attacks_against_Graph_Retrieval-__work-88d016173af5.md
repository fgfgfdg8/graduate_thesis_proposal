---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-88d016173af5
reading_level: L3
checked_date: 2026-11-14
---
# BadGraph: Structural Knowledge Isolation Attacks against Graph Retrieval-Augmented Generation

**阅读状态：L3。** 本记录对应USENIX Security 2026正式PDF；正文及附录A–C已全文阅读。L3不表示独立复现、代码审计或参考文献逐条核验。

- **作者**：["Leiming Yan", "Xinlong Xu", "Ziqiang Li"]
- **机构**：未核实
- **年份 / 会议 / track**：2026 / USENIX Security / main research paper，pp. 4741–4760
- **发表状态**：正式proceedings
- **CCF**：A（按第七版目录）
- **DOI**：USENIX正式页面未列DOI，不补造
- **代码与制品**：论文提及Zenodo DOI `10.5281/zenodo.20398798`；解析器未能确认目标制品，未审计或运行，不将其记作已验证代码。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **本地正式版PDF**：[科研数据库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/BadGraph_ Structural Knowledge Isolation Attacks against Graph Retrieval-Augmented Generation.pdf>)；SHA-256：`B72907C1E7B4D63861A05646941587D93FD9459F24CCC92636F30A4FC99B44E3`。

## 方法与证据

BadGraph向GraphRAG语料注入语义中性的linker documents，以改变持久图的拓扑、中心性排序、社区划分和随机游走，使目标证据更难被检索。攻击目标是证据可用性/隔离，不是强制生成预设错误答案。

威胁模型仅要求攻击者知道目标查询和系统采用持久图索引；攻击者不需要观察真实图拓扑、完整良性语料或模型参数（正式PDF物理页5，§3.1）。附录表C.1给出的FastGraphRAG评测配置为chunk size 800、overlap 100；这描述目标系统实验设置，不能推断攻击者已知具体分块参数。

论文评估两个数据集与三种GraphRAG系统。在报告的0.5%注入预算设置中，HotpotQA使用49篇注入文档、2Wiki使用30篇。HotpotQA的MS-GraphRAG结果中，作者的Top-20 source-recall审计由88.75%降至0.00%，QA F1由17.31%降至7.26%。Top-20来源审计口径不等同系统原生生成上下文中的实际召回，也不能将QA F1下降解释为定向误答ASR。

## 与开题的关系

**A：** 这是GraphRAG图拓扑可用性攻击，注入的是多篇linker documents；它不是由一份真实长源经受害者未知chunker生成的同源块。论文未证明同一正常query在真实索引中共同召回这些同源块，也未用逐块及联合删除确认块级共同必要。因此它压缩“图结构操纵能隔离证据”的宽泛新颖性，不闭合开题A的联合协议。

**B：** 论文没有提出或评测恶意块检测器、clean-query误删校准或最终OR删块后的QA效用。若研究范围扩展到GraphRAG，单纯检查内容语义是否正确不足以覆盖结构操纵；这只是威胁边界提示，不等同于B方向既有防御。

## 局限与可比性

- 威胁模型使用已知目标query；不能直接推及未知查询分布。
- 作者指出，较大或稠密语料可能需要更高注入量；当前报告的预算和结果不构成跨规模保证。
- Source Recall来自Top-20来源审计，与GraphRAG系统原生提供给生成器的上下文不是同一测量对象。
- 与文档级RAG投毒的攻击单位、索引结构和终点不同，不合并ASR或召回率作横向排名。

阅读范围：正式PDF共21个物理页，物理页1为封面；正文和附录A–C位于物理页2–21。附录末页的提示模板与表C.1已核读；未独立运行artifact。跨研究逐query重叠未知，不合并样本或数值。

## 来源与追溯

[USENIX正式论文页](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-leiming) · [正式PDF](https://www.usenix.org/system/files/usenixsecurity26-yan-leiming.pdf)

详见[证据地图记录](../../../../docs/RAG安全证据地图_20261102.md#src-fd8c244446b6b79c)与[开题近邻分析](../../../../docs/RAG安全文献攻防技术手段总结报告.md#十一rag安全近邻工作与开题定位)。目录、筛选范围及引用观测见[补查元数据](../../../../docs/RAG安全文献补查元数据_20261102.md)。
