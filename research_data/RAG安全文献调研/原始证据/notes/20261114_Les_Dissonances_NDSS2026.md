# Les Dissonances：NDSS 2026 全文阅读笔记

## 书目信息与版本

- **作者顺序**：Zichuan Li；Jian Cui；Xiaojing Liao；Luyi Xing。
- **正式出处**：Network and Distributed System Security (NDSS) Symposium 2026；DOI [10.14722/ndss.2026.240577](https://doi.org/10.14722/ndss.2026.240577)。按第七版CCF目录为CCF-A。
- **官方来源**：[NDSS论文页](https://www.ndss-symposium.org/ndss-paper/les-dissonances-cross-tool-harvesting-and-polluting-in-pool-of-tools-empowered-llm-agents/)；[NDSS正式PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-f577-paper.pdf)。
- **本地PDF**：[论文库文件](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Les Dissonances_ Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents.pdf>)，20个物理页，1,107,604 bytes，SHA-256 `D436F730E97409294C55B50637E97C3082C0F98A7508B81D76A1BED7CE2FDAAE`；与NDSS正式PDF核对题名和DOI。
- **代码**：论文公开动态扫描工具Chord的[GitHub仓库](https://github.com/systemsecurity-uiuc/Chord)及artifact说明；仓库/制品未审查或复现。运行完整实验需要与第三方工具及模型API交互，不据此声称可无密钥复现全部评估。
- **阅读范围**：正式PDF物理页1–20全文阅读；未运行Chord，未逐条审计参考文献。

## 问题与攻击机制

论文考察多个工具共享一个agent并共同参与任务时，工具之间的控制流与依赖关系如何被利用。作者提出Cross-Tool Harvesting and Polluting（XTHP），由Chord对真实工具进行动态扫描并构造端到端攻击。核心不是单个恶意工具孤立地返回有害文本，而是借助工具描述、前驱/后继调用关系或错误处理流程改变任务控制流，继而跨工具读取敏感上下文，或影响后续工具输出。

评估覆盖LangChain和LlamaIndex生态中的66个工具。作者确认50/66（75%）存在控制流劫持风险，48/66（72%）可被用于跨工具数据收集，45/66（68%）可被用于结果污染。三个比例对应不同攻击能力，不应合并成一个通用“成功率”。论文案例包含名为`search_and_retrieve_documents`的检索工具；这是agent工具池里的工具对象，不代表对持久RAG索引或知识文档的攻击。

## 对开题方向的关系

- **A方向**：这是Agentic RAG/Pool-of-Tools环境的强边界近邻。若RAG系统把搜索、检索和后处理封装为可组合工具，跨工具调用链可成为检索后泄露或结果污染的风险面。
- **不能等同于A**：论文不要求向持久知识库写入恶意文档，也不研究同一长源经受害者未知chunker形成的块、共同Top-K召回、逐块删除必要性或RAG答案攻击成功率。
- **B方向**：工具调用控制流与Top-K文本净化不是同一检测位置。Chord检测工具链配置/行为，不提供检索文档事实性判断、query级过滤或正常证据保留率。
- **适用结论**：报告应把“工具池/工作流污染”列为相邻攻击面，并明确与“检索语料/索引投毒”分层；不能仅以论文出现检索工具便判作直接RAG撞题。

## 证据定位与复现边界

| 主张 | PDF位置 |
|---|---|
| XTHP定义、工具池威胁及Chord | Abstract；§I–III |
| 控制流劫持、跨工具收集与污染攻击 | §IV |
| 66个工具及50/48/45项结果 | §V及Table III |
| 缓解讨论、artifact与局限 | 后续评估/讨论及artifact附录 |

完整记录见[证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261114-ndss26-les-dissonances)及[元数据表](../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261114-ndss26-les-dissonances)。
