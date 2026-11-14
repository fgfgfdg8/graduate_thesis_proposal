# Prompt Injection Attack to Tool Selection in LLM Agents：全文阅读笔记

## 书目信息与版本

- **方法名**：ToolHijacker。
- **作者顺序**：Jiawen Shi；Zenghui Yuan；Guiyao Tie；Pan Zhou；Neil Zhenqiang Gong；Lichao Sun。
- **正式出处**：Network and Distributed System Security (NDSS) Symposium 2026；DOI [10.14722/ndss.2026.230675](https://doi.org/10.14722/ndss.2026.230675)。按第七版CCF目录为CCF-A。
- **官方来源**：[NDSS论文页](https://www.ndss-symposium.org/ndss-paper/prompt-injection-attack-to-tool-selection-in-llm-agents/)；[NDSS正式PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s675-paper.pdf)。
- **本地PDF**：[论文库文件](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Prompt Injection Attack to Tool Selection in LLM Agents.pdf>)，18个物理页，757,058 bytes，SHA-256 `1749EFA3DBB7D90D32CE1B48C7B122C069048CE389BC1BE8D7DAC4BF86467967`；与NDSS正式PDF核对题名和DOI。
- **代码**：NDSS论文页及正式论文未列出公开代码仓库；此结论仅表示本次来源中未定位到代码链接，不断言作者从未发布实现。未审代码或复现。
- **阅读范围**：正式PDF物理页1–18全文阅读；未逐条审计参考文献。

## 威胁模型与方法

研究对象是LLM agent的工具选择链，而不是传统RAG回答生成本身。常见流程分两步：检索器先从工具库取回top-k工具说明，LLM再从中选出工具。攻击者把一份恶意工具说明注入工具库，在不知目标检索器、提示及内部参数的no-box设定下，同时操纵“被检索到”和“被LLM选中”。

ToolHijacker把工具描述优化拆成检索目标R和选择目标S，并采用两阶段优化。作者构造shadow task descriptions、shadow retriever、shadow LLM及shadow tool library，分别优化恶意说明进入候选集合及影响最终选择的能力；评估同时包含gradient-free和gradient-based方案。论文使用两个基准、8个LLM和4种retriever，并比较预防式及检测式防御。

## 结果及生态位影响

论文报告ToolHijacker在MetaTool上的检索攻击命中率达到100%；在StruQ配置下，gradient-free方案成功率为99.6%。known-answer detection未能识别其恶意工具说明；DataSentinel、PPL和windowed-PPL检测只能识别部分样本。上述数字分别对应检索命中、特定攻击/防御配置和检测结果，不能混称为同一ASR。

论文明确把PoisonedRAG作为RAG语料投毒相关基线，并指出其目标是将恶意文本写入知识库以影响回答；ToolHijacker则直接攻击工具库文档与工具选择。因此它直接约束“检索候选+下游LLM选择可被一份优化文档联合操纵”的宽泛新颖性，但两者的资产、任务目标和成功判据不同。

## 对开题方向的关系

- **A方向**：强邻近工作。它证明“单份恶意说明被检索并被下游模型采纳”不是全新抽象；但恶意对象是工具目录条目，不是RAG知识库中的事实性文档，也未研究真实长源、未知chunker、同源分块共同召回或逐块共同必要性。
- **B方向**：没有提出RAG检索后文档风险过滤器，也未评估clean-query最终OR误删风险、事实性/来源验证或证据效用保持。
- **创新边界**：不能将本课题贡献概括为“首次联合攻击检索与LLM选择”；可将区别限定在持久知识库、受害者真实分块及RAG答案层面的威胁与检测问题，并用直接RAG基线实证比较。

## 证据定位

| 主张 | PDF位置 |
|---|---|
| 两阶段工具检索/选择与no-box威胁模型 | Abstract；§I–III |
| R/S目标与两阶段优化 | 方法章节 |
| 8个LLM、4个retriever及攻击/防御结果 | Evaluation章节、Table I及后续防御结果 |
| 与PoisonedRAG的资产及目标区别 | Introduction/Related Work及本笔记范围分析 |

完整记录见[证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261114-ndss26-toolhijacker)及[元数据表](../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261114-ndss26-toolhijacker)。
