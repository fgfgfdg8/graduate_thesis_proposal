---
tags: [rag-security-evidence, ccs-2025, l3-full-text]
study_id: ccs-2025-flippedrag
checked_date: 2026-11-20
reading_level: L3
---

# FlippedRAG: Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models

**阅读状态：L3。** 已读 ACM CCS 2025 正式 PDF 物理 pp.1–13（摘要、方法、实验、用户研究、防御、消融、伦理与结论）；pp.14–15 主要为参考文献，未逐条审计。作者 arXiv v7 为 21 页，仅用于补充用户研究附录信息，不作为正式版页码来源。

## 正式身份

- **作者**：Zhuo Chen；Yuyang Gong；Jiawei Liu；Miaokun Chen；Haotan Liu；Qikai Cheng；Fan Zhang；Wei Lu；Xiaozhong Liu。
- **会议 / 页码**：ACM CCS 2025 主会，CCF-A；pp.4109–4123。
- **DOI**：[10.1145/3719027.3765023](https://doi.org/10.1145/3719027.3765023)。
- **正式 PDF**：[论文库正式版](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/版本/f9e61441f781/FlippedRAG_ Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models.pdf>)，15页，SHA-256 `f9e61441f7813576bb44a88715b2c9617486dbcedb4924caae5e99654cd84e2f`。
- **作者稿**：[arXiv v7](https://arxiv.org/abs/2501.02968v7)，21页；本地文件 SHA-256 `5e964e5686100fac73e7885f3909372ab5f2a116cadb98a4a0b57dd2ed77f092`。
- **代码**：[DavidAilesChen/FlippedRAG](https://github.com/DavidAilesChen/FlippedRAG)，固定 HEAD `fe3a899c5397c4ae210e320d82e63cadaf94daa4`；BSD-3-Clause；README 称包含代码、数据、环境与实验脚本。未克隆/运行。
- **归档入口**：[Zenodo 17036325](https://zenodo.org/records/17036325)；2026-11-20 DNS 解析失败，本轮保留为未验证入口，不据此否认归档存在。

## 一句话总结

FlippedRAG 先诱导黑盒 RAG 复述其检索上下文，用（query, candidate）对比样本训练替代 retriever；再以 PAT 生成触发词并把少量同立场文档推入 top-3，从而在争议话题上把 RAG 输出转向指定 Pro/Con 立场，并用用户实验测量认知变化。

## 威胁模型

- 攻击者能无限次查询目标 RAG，并能在公开可编辑语料中修改最多 `N` 份文档。
- 目标 corpus、retriever、LLM 参数和 prompt template 均不可见、不可改。
- 攻击者预先知道要操纵的争议话题和目标立场；这一点与开题 A 的 query-agnostic 设定不同。
- 防御脚本直接针对数据、检索和生成三个阶段。

## 方法

1. **黑盒 retriever imitation**：用指令要求 RAG “完整复制被检索到的 context”。返回文本与可访问语料对应后，以 relevants 为 `d+`、低排名/随机文档为 `d-`，训练 pairwise/contrastive surrogate retriever。
2. **Trigger generation**：在 surrogate 上用 PAT 优化触发词，同时约束检索相关性、语言流畅性和目标文档的 next-sentence consistency。
3. **Retrieval manipulation**：把 trigger 置于目标立场文档前，向目标 corpus 注入这些被修改的文档；默认 top-k=3，poison 数 `N=3–10`。
4. **Generation/user effect**：偷换 top-3 的立场比例后，依赖 Llama-3、Vicuna 或 Mixtral 的 context-following 产生定向立场；再用 7 点 Likert 量表做用户实验。

## 实验设置

- MS MARCO Passages Ranking 子集：约 500 queries、500,000 docs；ProCon.org 约 80 个争议话题、30 个被抽样用于攻击。
- Retriever：Contriever、Co-Condenser、ANCE、Qwen3-Embedding-4b；surrogate 为 NBoost/pt-bert-base-uncased-msmarco。
- LLM：Llama-3-8B-Instruct、Vicuna-13b-v1.5、Mixtral-8x7B-Instruct-v0.1。
- 用户研究：3 个争议话题、control/experimental 两组；v7 附录称共 54 人、每组 27 人。

## 关键结果

- **RQ1 retriever imitation**：Contriever/Co-Condenser/ANCE/Qwen3 的 surrogate/target NDCG@10 分别为 69.96/67.71、67.98/68.16、66.49/67.84、70.97/72.15；`Inter@10` 为 62.55/61.86/56.74/60.23。
- **RQ2 LLM 输出**：Table 4 的 OMSR 覆盖约 33.33–56.66%，ASV 约 0.23–0.70；Llama-3、Mixtral、Vicuna 的结果随 surrogate 和立场而变，并非所有组合均高于所有基线。
- **Table 6 baseline comparison**：FlippedRAG 的 Pro/Con OMSR 为 63.33/53.33%，PoisonedRAG 为 56.67/66.67%；即 FlippedRAG 在一个方向更高、另一个方向更低，“平均提高 16.7%”不能改写成每个 cell 均胜。
- **用户研究**：Table 7 的组均值分别为 GMO Pro 4.88→5.55、企业所得税 Con 3.59→2.70、临终医疗援助 Con 4.70→2.66；三次独立样本 t 检验均 `p<0.05`。这不是“20%受试者翻转”，也不能与模型 OMSR 相加。
- **防御**：TF-IDF spamicity 大多数阈值仍低于 clean 的 1 倍左右但并非零检出；PPL 与 clean 分布接近；keyword-density 与 clean 接近；query paraphrase 把 OMSR 63.3→40.0；RobustRAG 下仍约 40–46.7%；随机 mask 在低 mask rate 下不降反升，>50% 才明显下降。
- **消融**：poison 数从 1→10、top-k=3 时，3 份已可占满多数上下文；corpus 从 2k→100k 时效果先降后趋稳，但不能据此推出对任意 100k 语料均有效。

## 内部一致性问题

- Table 3/4 对 **Contriever + Llama-3、Target=Pro** 的 FlippedRAG `OMSR` 均为 **53.33%**；Table 6 同一 retriever/LLM/主题的对应行却印 **63.33%**。正文没有解释这两个评估集合是否不同。
- 因此优先保留分表口径，不把 Table 6 的 63.33 与 Table 4 的 53.33 相加/平均；跨方法排序只用同一张表内的 cell。
- 正式 main paper 说明附录按篇幅移至 arXiv；因此仅在 v7 附录看到的样本量另注为“作者附录”，不冒充正式 PDF 正文。

## 与开题 A/B 的关系

**A：强近邻，但不是直接撞车。**

- 重合：黑盒 retriever/LLM、允许修改少量公开文档、检索阶段触发、把目标立场文档推入 top-k、只靠生成端自然指令跟随。
- 不同：攻击者已知目标争议话题及目标立场，不是 query-agnostic；不是从一份良性真实长源派生；不控制内容管理员/受害者 chunker；没有把同源文本切成两个互补块；没有逐块 `00/10/01/11` 检查，也没有证明每块单独无效而联合必要。
- 它的触发器是附加在已有同立场文档前的 token/prompt 片段，和 A 的“真实源文档内语义互补触发”不同。
- 对系统级防御的启示：如果 RAG 允许用户诱导复述完整检索上下文，黑盒 retriever 可被近似；B 可把上下文最小披露作为门控前置条件，但这不等于块级风险检测。

**B：中等近邻，不能直接迁移。**

- 反 PPL、SEO、keyword density 的证据表明 B 不能只靠文档自然度/kw 密度。
- RobustRAG 在 factoid 上是强基线，但对 opinion-level poisoning 只有约 40% 削弱；说明 B 需要按证据语义/立场覆盖而非只数恶意 passages。
- 没有 clean-query 最终 OR 误删、独立阈值校准、正常多跳保留或人工验证成本；因此不能把它写成 B 的方案完成。

## 结论

FlippedRAG 是 A 的重要前邻：它把“黑盒检索器模仿 + 少量文档排名操纵 + 观点影响”证明得很完整；但它的攻击权限包含已知争议 topic、可修改多份已有立场文档、上下文泄露查询，并且没有同源未知 chunker/双块共同必要。开题若把 A 的创新点从“黑盒/少量文档”移走，仍可保留“单真实源覆盖、未知 chunker 迁移、同源互补块共同必要、B 的 clean-query 最终 OR 风险”这一组合。

## 来源

- [ACM DOI](https://doi.org/10.1145/3719027.3765023)
- [Crossref 记录](https://api.crossref.org/works/10.1145/3719027.3765023)
- [CCS 2025 accepted-papers](https://www.sigsac.org/ccs/CCS2025/assets/accepted-papers.json)
- [arXiv v7](https://arxiv.org/abs/2501.02968v7)
- [代码仓库](https://github.com/DavidAilesChen/FlippedRAG)
- [Zenodo 归档](https://zenodo.org/records/17036325)

[返回证据地图](../../RAG安全证据地图_20261102.md)
