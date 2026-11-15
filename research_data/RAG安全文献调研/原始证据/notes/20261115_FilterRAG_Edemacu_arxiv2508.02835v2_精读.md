# FilterRAG 与 ML-FilterRAG：检索投毒防御逐篇阅读

## 身份、版本和阅读范围

- **题名与作者稿**：Kennedy Edemacu、Vinay M. Shashidhar、Micheal Tuape、Dan Abudu、Beakcheol Jang、Jong Wook Kim，*Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation*。[arXiv:2508.02835v2](https://arxiv.org/abs/2508.02835v2) 于 2026-03-27 提交，v1 为 2025-08-04。此文的 FilterRAG 是知识投毒防御方法，不能与同名的视觉问答幻觉缓解论文 arXiv:2502.18536 混同。
- **会议登记与作者顺序冲突**：[Crossref 中 IEEE 登记的会议条目](https://api.crossref.org/works/10.1109/IRI69576.2026.00091)题名及六名作者集合匹配，载于 *2026 IEEE International Conference on Information Reuse and Integration for Data Science*（IRI 2026），2026 年 7 月，pp. 460–465，DOI `10.1109/IRI69576.2026.00091`；该登记顺序第三、四位为 Dan Abudu、Micheal Tuape，与 arXiv v2 首页相反。IEEE Xplore 文献页本次请求返回 HTTP 202 且无正文，未取得或阅读六页会议版，因而不声称两版内容相同，也不擅自消解作者顺序差异。
- **CCF**：对[第七版正式目录](<../catalogs/local_bib_round63_sources/CCF/第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）.pdf>)全文检索会议全称、`Information Reuse` 和独立词 `IRI` 均未检出；暂记“目录未检出，不赋 CCF 等级”，不以 IEEE 出版身份推定为 A 类。
- **实际阅读对象**：[本地 arXiv v2 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation.pdf>)，10 个物理页，SHA-256 `e1a9acf7c6a79ed8a78310d124f7f5d9122a677acff0e06b43f5fd3ea038cc33`。2026-11-15 阅读物理 pp.1–9 全部正文和局限、p.10 附录 A–D；参考文献列表已浏览，未逐条追溯。表格数值按 PDF 提取文字与表头核对，未复现或逐格审计全部表图；这是作者稿 L3，不等于会议正式 PDF 已读。
- **代码和引用**：arXiv 页和已读 PDF 未见此方法的作者实现地址；GitHub repository 搜索三个与题名/方法名相关的条件均无命中，不足以证明不存在。Google Scholar 引用数未观察，记未知；不把无数据填为零。

## 威胁模型与方法

- **攻击者与输入（pp.2–3）**：沿用 PoisonedRAG，攻击者预先选择目标问答并可向知识库插入每题多条投毒文本；分别研究无法访问或查询目标检索器的黑盒，以及可访问检索器参数的白盒。受害者直接检索已插入的文本；文中没有报告单份真实长源经未知受害分块后产生同源块及共同必要性的实验。
- **阈值型 FilterRAG（pp.3–4，式3–5、算法1）**：每个 query–候选段落对先调用小语言模型生成临时答案，将 query 与该答案结合，统计与段落语义相似的词在段落中的频率，再按段落不同词数归一为 Freq-Density；高于阈值的候选被排除，保留的候选中选择 top-k 用于生成。语义相似词匹配阈值默认 0.6，Freq-Density 阈值默认 0.2。逐候选调用 SLM，不是只做一次轻量分类器前向。
- **ML-FilterRAG（pp.4–5，算法2）**：除 Freq-Density 外还利用困惑度、SLM 答案联合对数概率和相关词频等特征，对标注的候选训练监督分类器。NQ 使用 XGBoost，HotpotQA、MS-MARCO 使用随机森林，且每数据集单独训练模型；论文没有明确给出与开题一致的来源级、query 级隔离协议，不能据此认定无跨 query/模板泄漏。

## 结果和限制

- **样本与人为平衡（pp.5–6）**：沿用 NQ、HotpotQA、MS-MARCO 每个数据集 100 个目标问答，每个问题注入 5 条对抗文本；ML 实验另用 GPT-4o 构造相似毒文供训练。实验将候选 top-s 固定为 4，**有意取相同数量的毒与干净候选**，再选 top-k=2；m=10 的实验重复 10 次覆盖问题。该平衡条件不能视为自然检索下无标签、未知污染率的检出与误删评估。
- **黑盒例子（p.7 Table I）**：NQ、GPT-3.5 下，PoisonedRAG 的 ASR/Accuracy 分别为 88.0%/10.8%，FilterRAG 为 3.0%/75.6%，ML-FilterRAG 为 2.0%/81.1%，而 CleanRAG 的 Accuracy 为 83.1%。ASR 与准确率都采用答案子串匹配；结果只能按文中受控实验条件解释。
- **效用及参数边界（pp.7–8 Tables I、II、IV）**：HotpotQA、LLaMA-3 的 CleanRAG Accuracy 为 66.5%，FilterRAG 为 53.6%，相差 12.9 个百分点；不能把结论中的“与原系统至多相差 0.2%”当作所有配置的统一保证。MS-MARCO/GPT-4 的阈值 ε=0.1 时 Accuracy 62.4%，ε=0.2 时 84.0%；更激进过滤可能牺牲效用。两者是攻击配置下答案准确率，均不是 clean-query 最终误删概率。
- **范围和成本（pp.8–10）**：作者明确说明主要测试 PoisonedRAG、未测试其他攻击且新增计算需求有待分析。部署段仅作定性成本讨论，未给端到端时间或调用预算；未见面向 Freq-Density/监督分类器的自适应攻击、来源独立性核验、query 级形式化误删控制或正常多跳前提保留评测。

## 对开题的约束

- **A（单源多块组合攻击）**：直接插入多条面向已知目标问答的毒文本，不构成受害侧未知 chunker、同源双块共同召回及逐块共同必要性的验证；不能据此否认或证明 A 的完整约束交集。
- **B（检索后净化）**：已有逐块 SLM 输出衍生统计量、监督随机森林/XGBoost 和阈值过滤的直接先例，因此不能宽泛宣称首次用统计特征或轻量监督模型识别毒块。B 仍需在一致预算与攻击/数据划分下，比较具体检索几何、来源—实体—命题关系、正常多跳证据保留及独立 clean-query 最大风险分位门控；本文没有给出这些组合的效果或可证明错误率。
- **关联入口**：[证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-20261115-edemacu-filterrag>)；[技术总结](<../../../../docs/RAG安全文献攻防技术手段总结报告.md>)；[元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261115-edemacu-filterrag-meta>)。
