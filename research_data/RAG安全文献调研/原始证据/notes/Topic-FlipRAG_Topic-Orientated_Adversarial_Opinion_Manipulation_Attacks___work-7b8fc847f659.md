---
tags: [rag-security-evidence, opinion-manipulation]
study_id: work-7b8fc847f659
reading_level: L3
checked_date: 2026-11-15
---
# Topic-FlipRAG: Topic-Orientated Adversarial Opinion Manipulation Attacks to Retrieval-Augmented Generation Models

**正式身份**：Yuyang Gong、Zhuo Chen、Jiawei Liu、Miaokun Chen、Fengchang Yu、Wei Lu、XiaoFeng Wang、Xiaozhong Liu；USENIX Security 2025，主研究论文，3807–3826，CCF-A。[会议页面](https://www.usenix.org/conference/usenixsecurity25/presentation/gong-yuyang)；[arXiv 2502.01386](https://arxiv.org/abs/2502.01386)。正式会议页面未列论文DOI；[Zenodo 10.5281/zenodo.15523435](https://doi.org/10.5281/zenodo.15523435)标识代码/数据归档。机构：武汉大学、南洋理工大学、伍斯特理工学院。

**版本与阅读范围**：正式[会议PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Topic-FlipRAG_ Topic-Orientated Adversarial Opinion Manipulation Attacks to Retrieval-Augmented Generation Models.pdf>) SHA-256 `2d995962ef88f008ce54619159c8f95140fc92453eb94b7573ea2d1a7420bce1`。L3：物理第2–16页正文与伦理说明；另读第19–21页附录A.1–A.5。第17–18页参考文献只按需检查。另有同研究[独立附录版本](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/版本/f62e487e5f37/Topic-FlipRAG_ Topic-Orientated Adversarial Opinion Manipulation Attacks to Retrieval-Augmented Generation Models.pdf>)，仅核过前两页，不将其计为全文阅读。

## 目标、攻击面与方法

攻击目标是让同一话题的一组相关查询持续倾向目标观点，而非对一个事实查询制造唯一错误答案。目标RAG为黑盒，但攻击者可查询并获得候选参考文档；可修改并注入目标文档。先用LLM引导的知识攻击改变文档立场，约束编辑距离和语义相似度；再利用开源替代神经排序模型的梯度及beam search生成跨查询的10 token触发器。默认编辑距离上限0.2、相似度下限0.85、迭代5次；PROCON默认选该话题下5篇低相关目标文档，top-k=3（正文§3–5，物理第4–9页）。

## 设置、指标与结果

- 数据：MS MARCO用于检索排序；PROCON包含80余争议话题，作者用GPT-4o生成候选子查询并做多样性过滤。RAG模型包括Contriever、ANCE、DPR与Llama-3.1-8B、Qwen2.5-7B的组合；模型输出立场由Qwen2.5-72B判别（物理第7–10页）。
- RASR用于衡量目标观点文档在Top-K中的占比是否上升，不能等同事实问答ASR；top3-v是投毒前后目标观点文档在Top-3中的比例差。表2中PROCON、Contriever黑盒检索器的CON／PRO RASR为51.90%／49.20%，top3-v为25.57／21.55个百分点（物理第10页）。
- ASV计算受操纵和原输出离散立场分数的绝对差，ΔASV减去干净条件下的基线变化。表3中的ASV量纲为立场分数，不是受试者改变比例；随机遮挡、困惑度、改写与重排只在文中配置下测试（§5–7，物理第8–15页）。
- 附录A.1对500条回答由3名标注者标注；模型与多数投票的一致性报告κ=0.8110、准确率0.8760。该验证不自动消除人机判别偏差（物理第19页）。

## 用户研究与可比性

54名18–25岁大学生随机分成两组，各27人；每人对两个话题各使用3个预设查询，交互前后填7点量表，归一化至[0,1]。事后均值：素食干净组0.45、投毒组0.61；太空殖民干净组0.76、投毒组0.59。附录A.3报告两个事后独立样本检验 $p=0.0454$、$p=0.0017$（§6.3，物理第11页；附录A.3，物理第19–20页）。这是组均值及组间比较，不是改变观点的受试者比例。前后测题干不完全相同；基线检验未拒绝差异并不证明等价。FlippedRAG同样报告54人/27人两组并有共同作者，样本是否重合未知，不可假定独立合并。

## 与开题的关系

A方向的自然文档改写、话题级多查询和检索排序均有直接参考价值；本文并未验证同一源文档经未知分块得到两块、二者共同被检索且共同必要。B方向应区分观点分歧与事实矛盾，对多视角有用证据的误删率须单独评估；作者的防御实验不足以覆盖所有事实冲突检测与自适应攻击。

## 制品与追溯

[GitHub](https://github.com/LauJames/Topic-FlipRAG)页面可访问；[Zenodo归档](https://zenodo.org/records/15523435)的API返回匹配题名及代码和数据清单，网页受访问限制。未运行制品。引用计数见[元数据](../../../../docs/RAG安全文献补查元数据_20261102.md)；[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-9ba15e3f0c9e5fb6)。
