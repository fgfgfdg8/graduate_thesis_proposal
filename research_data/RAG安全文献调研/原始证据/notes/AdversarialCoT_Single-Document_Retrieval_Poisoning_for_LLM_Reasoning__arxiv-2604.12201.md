---
tags: [rag-security-evidence, knowledge-poisoning, reasoning]
study_id: arxiv-2604.12201
reading_level: L3
checked_date: 2026-11-15
---
# AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning

## 身份、版本和阅读范围

- **作者**：Hongru Song、Yu-An Liu、Ruqing Zhang、Jiafeng Guo、Maarten de Rijke、Yixing Fan、Xueqi Cheng。
- **正式发表**：[SIGIR 2026 Short Papers](https://sigir2026.org/en-AU/pages/program/accepted-papers)，会议级别为CCF-A，依据用户提供的第七版目录[第35页文字层](<../catalogs/local_bib_round63_sources/CCF/p35.txt>)；ACM会议论文集pp.4145–4150，DOI [10.1145/3805712.3809838](https://doi.org/10.1145/3805712.3809838)。Crossref登记线上出版日期为2026-07-19。
- **实际阅读**：[arXiv v1作者稿](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/AdversarialCoT_ Single-Document Retrieval Poisoning for LLM Reasoning.pdf>)，2026-04-14，物理p1–5正文及p6参考文献全部阅读；L3仅对应该版本，不声称与ACM出版社排版版逐字一致。PDF共6页，SHA-256 `5d2ed7810f94d1677de9ca632a1021e64fef6cd35f452457ca12377c48b6338c`。
- **BibTeX**：沿用现有 `song2026adversarialcot`；[作者案例仓库](https://github.com/ruyisy/AdversarialCoT_case)当前主分支为说明和案例图，未见完整实验代码或release，未复现。Google Scholar引用数待统一核验。

## 设定与方法

作者研究查询特定的语料投毒。攻击者为每个目标查询和目标答案生成一份对抗文档，把所有目标查询对应的文档集合加入语料；因此“单文档”是**每目标查询**的载荷预算，而不必然是全实验只有一个投毒文档。攻击者能添加新文档，但不能修改或删除原有良性文档。受害系统是单轮检索、推理和回答的管线。作者称为决策式黑盒，具体接口返回**模型推理过程、最终答案和被检索文档集合**；不能把它归类为仅返回最终答案的黑盒（p2）。

攻击者先观察模型推理，将其粗粒度组织概括为启动、检视与转换证据、综合结论三个阶段，再借KIMI-K2构造支持指定答案的伪推理文档。若载荷未被检索，优化其查询相关性；若载荷已被检索而未能诱导答案，则参考模型拒绝的证据和推理轨迹改写说服链。实验最多三轮交互，不保证每次都收敛（p3–4）。

## 关键结果和可比性

| 位置 | 可核证据 | 限制 |
|---|---|---|
| p3–4 | MS-MARCO、Natural Questions、HotpotQA各随机抽取100查询；Co-Condenser检索top-5；目标模型为DeepSeek-R1、Qwen3、GLM4.5。 | 仅一个检索器；该样本与设定不代表其它语料或检索器。 |
| p4表2 | 作者列出的迭代ASR范围为52%–80%；将ASR定义为检索成功率ASRᵣ乘以已检索条件下的攻击成功率ASRᵍ。 | GLM4.5/MS-MARCO一项列92%、56.5%、59%；前两者相乘为51.98%，明显不同于59%，无法判定具体哪一列有误，须保留原文疑点。 |
| p4表3 | 表3中Qwen-7B-R1-distilled的迭代版ASR为74%、PoisonedRAG为51%，差23个百分点。 | 作者称对比实验主要关注MS-MARCO，但表3未单独标明数据集。只有AdversarialCoT进行了迭代，作者也明确把基线迭代扩展列为未来工作；该差值不是等攻击预算的独立因果效应。 |
| p4–5图3–4 | 作者报告0–3轮的攻击效果变化、随交互与上下文增长的成本趋势，以及跨模型迁移变化；图4既有下降也有少数上升。 | 未给可复核的完整成本明细；图中相对变化的归一化口径不明，不直接改写为百分点。 |
| p5–6 | 作者提出利用攻击轨迹定位推理缺陷，并把agentic RAG多轮检索/动态规划作为未来方向；参考文献[25]与[26]重复列出The Silent Saboteur。 | 文中没有完成可量化评估的防御器；重复文献是同一研究，不能重复计数。 |

## 对开题的约束

该文已经覆盖“每查询一篇投毒文档＋伪推理链＋反馈优化”的直接近邻，不能将这组宽泛能力称为首创。它与开题拟研究的区别是：原文不允许修改真实来源文档，未研究未知受害分块器把同一长源切成多个载荷，也未在固定其余上下文时分别删除多个同源块来验证同查共同召回和共同必要。是否能在不暴露推理轨迹和检索集合时迁移，原文也未验证。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-e62be27b5bcd2329>) · [元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md>)
