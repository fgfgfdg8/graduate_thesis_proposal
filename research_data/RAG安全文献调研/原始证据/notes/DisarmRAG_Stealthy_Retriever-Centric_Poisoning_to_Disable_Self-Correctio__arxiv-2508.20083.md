---
tags: [rag-security-evidence, conf-paper-recommend]
study_id: arxiv-2508.20083
reading_level: L3
checked_date: 2026-11-15
---
# DisarmRAG：检索器供应链投毒与自纠错抑制

**版本与阅读范围。** 阅读[arXiv v2扩展版PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DisarmRAG_ Stealthy Retriever-Centric Poisoning to Disable Self-Correction in Retrieval-Augmented Generation (Extended Version).pdf>)的正文第1–13页和附录O.2第21页；PDF共21页，SHA-256 `fe09f987d19f7ca553f875b3b96051aeae6269776dbe2f8d585193c33265fbb9`。L3仅表示上述版本正文已读，会议版及其他附录未据此算作已读。

- **作者**：Yanbo Dai、Zhenlan Ji、Zongjie Li、Kuan Li、Shuai Wang。
- **会议版**：*DisarmRAG: Stealthy Retriever Poisoning to Disable Self-Correction in Retrieval-Augmented Generation*，ACM CCS 2026主研究轨道，CCF-A，pp. 4627–4641，[DOI 10.1145/3830454.3832598](https://doi.org/10.1145/3830454.3832598)。[会议录用目录](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)与[Crossref登记](https://api.crossref.org/works/10.1145/3830454.3832598)均使用这一正式题名。
- **所读预印本**：*DisarmRAG: Stealthy Retriever-Centric Poisoning to Disable Self-Correction in Retrieval-Augmented Generation (Extended Version)*，[arXiv:2508.20083v2](https://arxiv.org/abs/2508.20083)。其首页同时写了会议DOI和扩展版题名，不能据此把21页扩展内容或扩展标题直接当成正式会议录条目；版本结果未逐项对照。
- **代码**：[作者仓库](https://github.com/ybdai7/DisarmRAG-poisoning-attack)，扩展版p13公布；2026-11-15入口HTTP 200，未运行、未核最新release。
- **引用量与优先级**：见[元数据汇总](<../../../../docs/RAG安全文献补查元数据_20261102.md>)；未观测值不填零。

## 威胁模型与方法

攻击者知道或选定目标问题，能够在部署前白盒编辑并分发受污染的检索器，同时向将被索引的语料贡献攻击文档；不能任意修改存量知识、查看受害系统提示词或查询受害部署的LLM（pp5–7）。攻击者通过辅助超网络将梯度映射为低秩更新，使用对比损失与查询邻域表示约束，使目标查询召回指令而尽量保留良性检索；多目标使用PCGrad处理目标间冲突。另一部分在模拟防御提示池与攻击提示池间迭代选出抑制自纠错的指令，之后与伪事实文档一同进入知识库（pp7–9）。这是**模型供应链与文档注入联合权限**，不属于仅修改一个源文档的黑盒威胁。

## 实验及可复用结果

- §7称每个数据集随机取100个封闭式问题；默认Contriever、Top-5、GPT-4o mini，另含HotpotQA、MS MARCO和其他模型。ASR要求回答包含攻击者答案且不含正确答案，以精确字符串匹配判定；指令召回率与恶意上下文F1是不同指标（p9）。
- Table 5对NQ、Contriever、GPT-4o mini报告ASR **94.00%±0.82%**，PoisonedRAG(W) **48.33%±0.58%**，BI Recall@5为100%、MC F1为78%；表注称三次评价的均值和标准差。相同表中Qwen-Max为80.33%，不能将摘要“超过90%”泛化到所有设置（p10）。
- 同时针对25个目标查询时，Table 6报告NQ和HotpotQA的ASR均为78%，MS MARCO为83%；目标数、查询构造和更新方式应与单目标设置分开（p10）。
- 对TrustRAG，原始指令平均ASR为21.83%；作者称适配后平均为71.67%，Table 13三数据集分别为75%、62%、78%。这不是未经适配的防御对照。对重排器的参数编辑只报告可行性检查，未完成端到端研究（p12）。
- Table 10的单目标NQ Recall@100下降1.13个百分点，25目标HotpotQA MRR@100下降5.15个百分点；Table 11的GTE Recall@100下降3.54个百分点。因此作者有关各指标差异均低于1%的概括不能覆盖这些表格；附录O.2仅比较特定层的谱统计，不能证明不可检测（pp11、21）。
- §7的每数据集100题及Table 5的三次评价，与部分数值如94.75%存在口径待解释：若三次各以100题等权、各次命中数为整数，该均值不可能由简单平均得到。可能存在文中未说明的汇总方式；不反推每次分母或独立样本数。

## 与开题的关系

- **A攻击方向**：检索器权重控制、目标查询和攻击文档是更强权限；该研究不证明未知分块器下单个真实长源形成同源角色块、实际共同召回及逐块共同必要性。
- **B防御方向**：提醒比较系统提示词、自纠错与检索器可信前提，并可将权重投毒作为额外扩展威胁。它没有证明开题的跨块异常检测及clean-query最终误删率控制已被实现；其自纠错与防御结果依赖具体模型、提示和攻击适配。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-64b35c347fa1218b>) · [技术总结报告](<../../../../docs/RAG安全文献攻防技术手段总结报告.md>)
