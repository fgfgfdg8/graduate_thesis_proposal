# A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models

## 书目、版本与文件

- 作者：Jiayi Wen、Tianxin Chen、Zhirun Zheng、Cheng Huang；PDF首页机构为复旦大学、Ajou University。
- 版本：arXiv:2508.04276v2，cs.CL；首次提交于2025-08-06，v2于2025-08-12更新。2026-11-11复核官方arXiv API，v2仍是最新版本。
- 正式发表与CCF：本次未在官方arXiv记录及精确题名检索中核到期刊/会议出版信息或DOI；现按arXiv预印本登记，CCF不适用，不把它标为顶会/CCF-A论文。
- 本地PDF：[A Few Words Can Distort Graphs_ Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models.pdf](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/A Few Words Can Distort Graphs_ Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models.pdf>)；9页，5,287,335 bytes；SHA-256 425BD532556BEF9E11E0D03C90B80CF582DFAD843158B13C3196DDE3FDC0E24D。文件已存在，本次未重复下载。
- 官方入口：[arXiv记录](https://arxiv.org/abs/2508.04276v2)、[PDF](https://arxiv.org/pdf/2508.04276v2)。
- 代码/数据制品：PDF中未发现作者代码、数据或权重发布链接；GitHub精确题名仓库检索返回0项。没有确认可用的作者制品，但这不等同于穷尽所有可能仓库。评测输入包含《小王子》及Wikipedia长文；作者生成并人工复核的QA数据未见独立发布链接。
- 引用与优先级：Google Scholar引用数未观测，待相关性筛选完成后与全库统一核查。按报告现有评分方法，venue输入属于预印本；引用速度、归一化引用项、统一日期下的时间项、开源因子及总分暂不计算。

## 全文阅读与证据定位

已逐页读取本地arXiv v2的物理页1–9，含参考文献；未运行代码或独立复现实验。

| 页码 | 阅读证据 |
|---|---|
| p.1 | 题名、作者、摘要及Introduction开头；论文将其定位为对已有源文本做少量修改，而非向语料新增毒文档。 |
| p.2 | Figure 1及贡献概述；TKPA操纵指定问题答案，UKPA通过改变指代链破坏全局图结构。 |
| p.3 | Figure 2、GraphRAG管线、攻击模型；TKPA的VCL、ego-subgraph及chunk scoring定义。 |
| p.4 | Figure 3、TKPA后续步骤和UKPA动机；分别用局部图结构信号选块、用语言指代扰动破坏实体合并。 |
| p.5 | UKPA候选生成与结构影响分数；数据、问题生成、模型参数和攻击/防御基线。 |
| p.6 | Tables 1–3及指标定义；TKPA逐语料ASR/QASD、UKPA图结构变化与QA准确率。 |
| p.7 | Tables 4–5、Figures 4–5及消融；检测器结果、修改预算、Top-K与编辑距离分析。 |
| pp.8–9 | 完整参考文献定位；直接关联GraphRAG的引用包括GraphRAG under Fire（arXiv:2501.14050）、PoisonedRAG等。 |

## 方法、威胁与实验

- **攻击面和威胁模型（pp.1–3）**：攻击者修改可信源（例为Wikipedia）中的少量文字，不新加文档、不访问模型参数。GraphRAG把源文本分块、抽取实体关系、合并知识图、检测社区并生成社区摘要；查询检索的是相关社区摘要。TKPA针对特定问题/答案，UKPA以很少的编辑普遍破坏实体链接与图连通性。
- **TKPA（pp.3–4，Eq.1–2）**：先从query抽取目标实体；以(1 + degree)(1 + betweenness) / log(1 + summary length)给包含目标实体的社区评分，选出脆弱社区并提取一跳ego-subgraph，再从相关源chunks中按图中心性、query语义相关性和情感倾向评分，最后改写高分块。默认权重为(0.5, 0.3, 0.2)。Fig.4报告仅改写Top-1/Top-2/Top-3块时，TKPA ASR依次为55.8%/81.3%/91.2%。
- **UKPA（pp.4–5，Eq.3）**：逐chunk用LLM识别代词、名词短语和共指链，生成保持局部语义和流畅度的微小改写候选；分数为实体集合变化、关系集合变化与语义相似度下降的加权和，默认权重(0.25, 0.25, 0.5)；选择最高分改写并写回原语料，以此累积破坏跨chunk实体合并。
- **威胁模型缺口**：p.3称攻击者不能访问构造后的图。但TKPA需要社区划分、degree/betweenness centrality和ego-subgraph来定位与评分候选块；正文未说明在不读取目标图的情况下如何取得这些结构量、是否依赖本地影子图或额外oracle。UKPA则明确不需图结构细节。故TKPA的实际图可见性/代理获取假设未闭合，不能仅凭“gray-box”标签推断为可部署黑盒攻击。
- **数据与系统（p.5）**：TKPA测试《小王子》（LP）、2007–08金融危机（FC08）、日本资产泡沫（JAPB）；UKPA测试LP与俄乌战争（RUW）。作者为每份文档生成20–30个多跳QA对并人工检查；GraphRAG用GPT-4o-mini构图、BGE-M3嵌入；GPT-4o用于TKPA改写/攻击结果核验及UKPA语言分析、候选改写和结构抽取。系统为Microsoft GraphRAG与LightRAG。
- **基线（p.5）**：TKPA比较PoisonedRAG和Naive Swap；UKPA比较TextFooler-style Perturbation。防御比较PPL Filter（GPT-2）、few-shot LLMDet、Semantic Closeness Checking；另讨论query paraphrasing。
- **指标及分母（p.6）**：TKPA报告ASR与QASD；UKPA报告节点/边保留率、Jaccard及下游QA accuracy。文中披露每文档生成20–30个问题，但未给各实验单元的实际N、整数分母、置信区间或多次运行波动；不能据百分数反推精确成功概率。

## 结果与边界

- **TKPA（p.6 Table 1）**：ASR为LP 93.10%、FC08 89.50%、JAPB 91.20%，表内三集平均91.27%；摘要的93.1%对应LP，不是该表跨集平均。QASD为0.85、0.81、0.83，平均0.83。图4的Top-3 91.2%与JAPB值相同，但不是全表的91.27%平均。
- **UKPA（p.6 Tables 2–3）**：Microsoft GraphRAG QA accuracy从95%降至50%，LightRAG从90%降至45%；TextFooler两者均为85%。微软GraphRAG在LP/RUW的节点Jaccard分别0.4255/0.4100，边Jaccard分别0.2121/0.1581；LightRAG节点Jaccard为0.2783/0.2899，边Jaccard为0.1362/0.0789。部分图的边数在攻击后增加，结果是结构重组/碎裂，不宜简化成单纯节点或关系删除。
- **修改预算（p.7 Table 5）**：TKPA的LP为48/155词（最小/平均，0.055%/0.164%），FC08为76/325词（0.18%/0.807%），JAPB为113/334词（0.254%/0.751%）；UKPA的LP/RUW分别修改32/60词，占0.033%/0.045%。因此“少于0.05%”应限定于UKPA两项数据，不能概括TKPA全部设置。
- **检测器与消融（p.7 Tables 4–5）**：TKPA的PF、LLMDet、SCC F1分别0.07/0.13/0.07；UKPA仅列PF与LLMDet，F1为0.04/0.11，未列UKPA-SCC结果。表中未报告FPR；“防御无效”不能泛化到所有检测器。消融指出TKPA图结构项单独ASR 65.3%、语义项58.2%、态度项51.7%；联合优化91.2%。UKPA调权可使accuracy降至0.50，但单项结果为0.70–0.75。样本规模与运行波动缺失限制了结果解释。

## 与开题及近邻工作的关系

- 这是A方向的**强直接部分近邻**：在长源文本中就地改写多个块，利用图结构影响定向QA；UKPA则通过小改动制造跨块/跨实体的结构性后果。不能再声称“首个对长源现存文本做多块GraphRAG投毒”“GraphRAG图构建投毒”或“少量改写造成图级影响”。
- 当前原文没有验证受害系统未知chunker下的真实切分，也未用源chunk ID展示同一正常query实际共同召回了哪些原始块，更未以逐块/联合删除证明每个实际块对终端错误答案共同必要。其检索上下文是社区摘要，不能直接等同于普通RAG top-k原始chunk。开题A若保留窄贡献，需把这些缺失协议设为实证对象，并将TKPA作为直接基线/生态位冲突项。
- 与GraphRAG under Fire和KEPo均属图构建/图知识投毒，但机制有别：本文是就地改写源文、图中心性定向选块或共指破坏；GraphRAG under Fire覆盖关系增强/跨chunk抽取；KEPo以新增伪造知识演化叙事与关系为主。不可将三者的分数横向合并，也不可将其分别覆盖的机制简单当作同一方法。
- B方向上，本篇只有通用检测器对比，没有来源鉴真、正常query最终OR误删校准或真实多跳效用控制，不能作为这些能力已被解决的证据。
