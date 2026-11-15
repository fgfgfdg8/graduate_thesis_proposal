---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-aae524a6944d
reading_level: L1
checked_date: 2026-11-03
---
# Toward Faithful Class-Level Self-Explainability in Graph Neural Networks by Subgraph Dependencies

**书目核对：**2026-11-15 [Crossref登记](https://api.crossref.org/works/10.1109%2FTKDE.2026.3730527)和IEEE目录均记为标题首词 *Toward*；[arXiv:2508.11513v1](https://arxiv.org/abs/2508.11513v1)的预印本题名使用 *Towards*，与期刊版按版本分别登记。

**阅读状态：L1。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Fanzhen Liu", "Xiaoxiao Ma", "Jian Yang", "Alsharif Abuadbba", "Kristen Moore", "Surya Nepal", "Cecile Paris", "Quan Z. Sheng", "Jia Wu"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / IEEE Transactions on Knowledge and Data Engineering / Journal research article
- **发表状态**：2026-09-04在线发表；IEEE与Crossref登记于2026年12月38(12), 8542–8555，截至2026-11-15该期次尚在未来。
- **CCF**：正式身份已核等级 ["A"]；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **代码**：未核实 / 未提取
- **关联标题**：["Toward Faithful Class-Level Self-Explainability in Graph Neural Networks by Subgraph Dependencies"]

## 一句话总结与核心贡献

GraphOracle联合学GNN分类器和稀疏类别子图，建图—子图—预测依赖，并以mask评价类级faithfulness；熵正则选择和随机游走减开销。

L1条目的方法、效应及撞车关系保持待核，不由题名或下载行为推定。

## 与开题逐项比较

**A：** 摘要未建立A的全部联合约束；正常检索、分散证据或删子结构的意义仅以本条判断为限，不据此排除全文。

**B：** A必要性对照与B删块保留的组件近邻：子结构mask依赖和类别解释已有。GNN训练及类级faithfulness不等RAG单源互补块共同必要；移除分布变化、稳定性及条件前提仍待全文。

## 局限、可比性与不确定性

- 仅摘要L1；正文方法、保证前提、实验实际N及成本未读。
- 样本重叠unknown；摘要未列不等全文没有。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### IRJ06-publisher-abstract-main-20261103

- **书目来源**：[原始页面](https://ieeexplore.ieee.org/document/11679062/)
- **DOI / arXiv**：10.1109/tkde.2026.3730527 / 未核实 / 未提取
- **本地PDF**：缺PDF，保留证据缺口
- **原始PDF链接**：未核
- **实际阅读**：L1；完整官方原摘要；正文0页。

#### 方法、结果与适用条件

# IRJ06 — Toward Faithful Class-Level Self-Explainability in Graph Neural Networks by Subgraph Dependencies

DOI `10.1109/tkde.2026.3730527`；IEEE Transactions on Knowledge and Data Engineering；2026-09-04在线；登记2026年12月38(12), 8542–8555，为截至2026-11-15的未来期次。

[IEEE主源](https://ieeexplore.ieee.org/document/11679062/)；原摘要曾在本地快照阅读，当前网页可用性另行核实。

**作者摘要主张**：GraphOracle联合学GNN分类器和稀疏类别子图，建图—子图—预测依赖，并以mask评价类级faithfulness；熵正则选择和随机游走减开销。

**开题关系与待核**：A必要性对照与B删块保留的组件近邻：子结构mask依赖和类别解释已有。GNN训练及类级faithfulness不等RAG单源互补块共同必要；移除分布变化、稳定性及条件前提仍待全文。

摘要L1；无PDF正文阅读信用。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-eb904e08e2f6d721) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes)
