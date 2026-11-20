---
tags: [rag-security-evidence, neural-ranking, black-box, full-paper]
reading_level: L3
checked_date: 2026-11-15
---
# Multi-granular Adversarial Attacks against Black-box Neural Ranking Models

## 身份、来源与阅读范围

- **完整作者**：Yu-An Liu；Ruqing Zhang；Jiafeng Guo；Maarten de Rijke；Yixing Fan；Xueqi Cheng。与 2023 年 Topic-oriented 论文不同，本篇作者名单中没有 Wei Chen。
- **正式出版**：SIGIR 2024，第 47 届 International ACM SIGIR Conference on Research and Development in Information Retrieval，主会 Full Paper，pp. 1391–1400，DOI [10.1145/3626772.3657704](https://doi.org/10.1145/3626772.3657704)。作者、会议及正式页码由[ACM 注册的 Crossref 记录](https://api.crossref.org/works/10.1145/3626772.3657704)核验。官方[录用论文页](https://sigir-2024.github.io/program_papers.html)的数据源[原始 JSONL](https://sigir-2024.github.io/infofiles/sigir2024-papers.updated.v3.jsonl)列有该文 `submssion_id: fp1227`；页面脚本将 `fp` 对应 Full Papers。会议[正式论文集目录](https://sigir-2024.github.io/proceedings.html)亦列出本篇。CCF 官方[数据库/数据挖掘/内容检索目录](https://www.ccf.org.cn/Academic_Evaluation/DM_CS/)将 SIGIR 列为 A 类。
- **实际阅读版本**：作者所在阿姆斯特丹大学信息检索实验室公开的[作者版 PDF](https://irlab.science.uva.nl/wp-content/papercite-data/pdf/liu-2024-multi-granular.pdf)，本地[按题名保存的 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Multi-granular Adversarial Attacks against Black-box Neural Ranking Models.pdf>)；SHA-256 `493f39670dfb56d8a46c0067de492d677a4ac37040cc60782b06d6dc7737c18c`。论文首页标明 CC BY 4.0；另有[作者预印本页面](https://arxiv.org/abs/2404.01574)。本地文件共 10 页，已阅读正文 PDF 第 1–9 页，第 10 页为参考文献。**此作者版未印正式会议页码**：下文一律采用本 PDF 的物理页码，正式论文集范围 1391–1400 仅作书目元数据，不把推算页码冒充已验证的印刷页码。
- **查重**：本次对三份 RAG 主文档和 `research_data` 按完整题名、DOI、arXiv 号、RL-MARA 等方法名检索，未发现本研究既有逐篇精读笔记；已有 Topic-FlipRAG 局部笔记属于另一篇研究。

## 问题、能力和对象

- **任务与目标**：对一个给定查询—目标文档对，选择词、短语、句子粒度的扰动，使修改后的文档在神经排序结果中高于原文，同时限制修改预算并追求语义/语法相似。称为多粒度排名攻击 MARA，提出的强化学习方法为 **RL-MARA**（§2，PDF 第 2–3 页）。
- **黑盒能力**：仅可查询目标神经排序器并观察部分结果的排名，不获得目标相关性分数和内部参数；用目标输出训练本地代理模型，代理分数及梯度提供优化信号。因此这是**可获得排名反馈的排序黑盒**。开题 A 明确目标接口不提供检索得分或 logprob、优化仅使用影子系统得分，但是否披露检索条目及顺序未明确，不能据此断言开题只有生成接口（§2、§4.2–4.3，PDF 第 2、4–5 页）。
- **目标系统边界**：Anserini/BM25 取 Top-100 后，攻击 BERT、PROP、RankLLM 这三种神经排序器。RankLLM 在本文是从 ChatGPT 排序能力蒸馏到 DeBERTa-large 的模型，不是直接攻击 ChatGPT 作为排名器；论文结论明确把直接攻击 LLM 排序器列为未来工作（§5.3–5.4、§8，PDF 第 6、9 页）。
- **修改位置和预算**：在同一文档内可组合词、短语、句子级修改；实验统一词项修改预算 ε=25，三种跨度分别为 1、2–5、6–10 个词。方法允许某个例子只用一种或部分粒度，并非每个例子都必须同时包含三种粒度（§1、§5.4，PDF 第 2、6 页）。

## 方法及对 Topic-FlipRAG 的关系

- 强化学习框架中的子代理标注不同粒度的脆弱文本位置，元代理从候选扰动中顺序选择操作；词级采用 PRADA 式同义词替换，短语级借鉴 PLAT/BART，句级采用 PAT 式触发替换。各操作及最终组合针对的是同一个查询—文档对（§3–4，PDF 第 3–5 页）。
- 虚拟环境同时包含代理排序器和 ChatGPT：前者提供相关性变化，后者评价扰动文档相对原文的语义相似度与流畅度，作为自然度奖励。**ChatGPT 在这里是攻击构造的自然度评分器，不是受害 RAG 的答案生成器**；奖励分数也不构成真实读者无法察觉的保证（§4.2、图 3，PDF 第 4 页）。
- [Topic-FlipRAG 正式版](https://www.usenix.org/system/files/usenixsecurity25-gong-yuyang.pdf) §4.2.2 将本篇列为参考文献 [29] 并称其多粒度编辑受到启发，位置为其 PDF 第 5 页、印刷 p.3810；它把这一方法思想用于话题知识编辑与立场控制。引用关系不意味着本篇 2024 年实验已经评估 RAG 生成偏向或观点操纵。
- 论文列出的代码为 [Davion-Liu/MARA](https://github.com/Davion-Liu/MARA)；本次未运行，也未核实每项实验与仓库当前版本的对应关系（§4，PDF 第 3 页）。

## 实验与可复核结果

- **数据与候选**：MS MARCO Document Ranking 随机抽取 1,000 个开发查询；ClueWeb09 使用 TREC Web Track 2012 的 242 个查询。每个查询的 Easy 文档从目标排序中第 30–60 位抽取 5 个，Hard 文档取末尾 5 个；另有从两者混合抽取的 Mixture。文档均从 BM25 预取的候选中选取，不能据此推出语料库外新文档的首阶段召回率（§5.1、§5.4，PDF 第 6 页）。
- **数值实例，限 MS MARCO、BERT、Hard 条件**：表 1 中 RL-MARA 的 ASR=98.9%、平均提升 88.1 位、T10R=36.9%、T5R=9.9%；IDEM 基线依次为 90.2%、69.6 位、25.8%、7.2%。ASR 定义为排名获得提升的目标文档比例，不是 Top-5 命中率，更不是 RAG 生成成功率；同表 Easy 文档的 ASR 已有多个方法达到 100.0%，不能仅凭 ASR 判断更深的排名改善（§5.2、表 1，PDF 第 6–7 页）。
- **组合消融**：表 1 同时给出固定单粒度、强制三粒度和贪心策略；在所测设置中完整 RL-MARA 的组合方式优于这些变体。它支持同一文档内扰动组合的观察，不能说明 RAG 中两个检索块具有协同必要性（§5.3、§6.1，PDF 第 6–8 页）。
- **自然度与检测**：在 MS MARCO 的 RankLLM / Mixture 条件下，5 名标注者对每种方法随机抽取 32 个对抗例进行评分；原文与 RL-MARA 的不可察觉性分数分别为 0.90、0.87，流畅度为 4.57、3.90。以 OSD 阈值 0.04 为例，对 RL-MARA 的检测率为 20.2%；人评样本、阈值和检测器均有限，不能外推成普遍隐蔽或绕过开题 B（表 3–4、§6.3，PDF 第 8–9 页）。
- **泛化限制**：论文明确称策略网络训练结束后在同一完整数据集再跑一轮测试，不能把其作为独立未见查询和文档上的泛化证明（§5.4，PDF 第 6 页）。作者另用 Natural Questions 查询训练代理做 OOD 对比，图 5 中各攻击指标下降；这是代理训练分布变化的补充实验，并不能消除策略训练/测试复用或证明对不同 RAG 管线的迁移（§6.2、图 5，PDF 第 8 页）。

## 与开题 A/B 的比较和可整合判断

开题原始定义见 [section3_content.tex](../../../../partitions/section3_content.tex)：A 为单篇源文档经受害者分块后的同源双块联合召回与预设错误答案；B 为检索后、生成前结合统计/语义特征、跨块关系和异源参照的净化。

- **A 的相似处**：对同一篇已有文档做位置和语言质量受约束的改写，用本地代理指导提高排名，可作为单文档攻击及自然文本构造的检索侧近邻。
- **A 的关键差异**：本文目标侧暴露排序位置，优化单个查询的整篇候选文档排名；开题对目标排名是否可见未作明确约定；不涉及受害者真实分块、两个同源角色块的完整性、联合 Top-K、互补命题或预设错误答案。**词/短语/句子的多粒度不等于多个检索文本块协同**。若作基线，需另行适配受害管线，并做单块、双块和共同召回消融及答案评估。
- **B 的相似处与边界**：LLM 自然度奖励及 OSD 结果表明，流畅性和词面反垃圾过滤不能替代对不同攻击策略的实测。该文没有运行 B 的查询—块特征、跨块检查或异源事实核验，不能称已绕过 B；应将其改写样本在明示标签和数据分布的前提下作为候选测试，并报告检测、误报和最终问答效用。
