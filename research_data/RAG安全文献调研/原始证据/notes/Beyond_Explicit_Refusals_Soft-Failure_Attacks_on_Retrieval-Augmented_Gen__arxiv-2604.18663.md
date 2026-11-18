---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2604.18663
reading_level: L3
checked_date: 2026-11-18
---
# Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation

**阅读状态：L3。** 已逐页阅读正式 ACL 2026 PDF 全文 22 页：正文与伦理声明 pp.1–10、参考文献 pp.11–12、附录 A–C pp.12–22；这里的 L3 表示正文和附录均已读，不代表运行作者代码或复现全部实验。

- **作者**：Wentao Zhang；Yan Zhuang；Zhuhang Zheng；Mingfei Zhang；Jiawen Deng；Fuji Ren
- **年份 / 会议 / track**：2026 / ACL 2026 / Volume 1 Long Papers，main
- **作者拼写差异**：正式页元数据作“ZhuHang Zheng”，PDF首页作“Zhuhang Zheng”；两处来源大小写不同，元数据表保留正式页写法。
- **发表状态**：official proceedings；正式页码 30281–30302
- **CCF**：ACL 按第七版目录为 A；Findings、Industry、Workshop 等 track 不自动继承主会等级
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
- **代码**：正文和正式页面未确认自有代码链接；不据此断言闭源

## 一句话总结

DEJA（Deceptive Evolutionary Jamming Attack）研究一种**软失败可用性攻击**：攻击文档被检索并诱导模型生成流畅、相关但信息贫乏的回答，避免显式拒答和明显错误，从而隐蔽地降低 RAG 的有效效用。

## 威胁模型与攻击机制

- 攻击者拥有知识库写入权限，但不访问检索器参数、LLM 参数、梯度或内部嵌入；每个目标 query 注入一篇文档。
- 文档结构为 `query ⊕ retrieval hook ⊕ payload`：hook 提升检索排名并充当语义桥，payload 通过六类软失败策略诱导含糊、冲突、复杂度升级、信息碎片化、上下文敏感等输出。
- 进化搜索以 Answer Utility Score（AUS）为适应度：目标软失败区间为 `[2.0, 3.5]`，硬失败区间为 `[1.0, 2.0)`；正文设置 `τ_soft=3.0`，最多 10 代、种群 5、保留 3 个父代并使用早停。
- 作者把“检索成功”和“回答软失败”分开测量：RSR/Top-1 描述攻击文档进入上下文，SASR 描述软失败，HASR 描述硬失败，`MAD_τ` 描述效用偏离；这些指标不能直接改称事实投毒 ASR、错误答案率或来源真实性检测率。

## 实验、结果与边界

- 数据集为 NQ、FiQA、HotpotQA；检索器为 GTR-base 与 Contriever；主要生成模型为 Llama-2 7B/13B、Mistral-7B，并测试 GPT-4.1 mini、Gemini 2.5 Flash、Claude 3.5 Haiku 的迁移。
- 每个数据集先从干净 RAG 能产生高效用回答的 query 中保留 100 个评测样本；这是有效性所需的筛选，也限制了对低效用/难 query 的外推。
- GTR-base 下，攻击文档 RSR 通常超过 94%，Top-1 为 72.5%–100%；DEJA 的 SASR 在 NQ、FiQA、HotpotQA 上分别约为 81.76%–92.27%、94.39%–98.47%、79.91%–82.13%。扩大检索窗口 `k=4→10`、做 query 改写和跨模型迁移后，软失败仍明显存在。
- 去掉逐字 query anchor 后，DEJA 仍报告 74.36% SASR 和 71.00% RSR；这说明方法不完全依赖复制 query，但仍不能推出对所有检索器和语料的普适性。
- 困惑度检测不能稳定识别攻击：NQ AUC 0.548，HotpotQA AUC 0.760 但伴随误报，FiQA AUC 0.197；SelfRAG、CoVe、Citation Checking 等语义防御在作者设置下仍保留较高 SASR。
- 消融、跨模型、人工一致性和高级语义防御均在附录 A–C 中给出；人工验证为小规模专家评估，不能替代跨数据集人工金标准，也不能把评判器一致性当作安全保证。

## 与开题逐项比较

**A：** DEJA 是单篇注入文档，并把检索可见性与生成效用退化联合优化；它没有建立“同一真实长源经受害者未知 chunker 后形成同源多块、同 query 共同召回、逐块与联合删除均必要”的四格协议，因此不直接占据 A 的核心交集。

**B：** DEJA 直接占据“软失败、流畅非信息回答、可用性退化”生态位。B 的评测不能只报告错误答案和显式拒答，还应分别报告正常回答效用、信息完整性、软失败识别、干净 query 的证据保留与误删；SASR/HASR 不应与这些终点混用。

## 可比性与局限

- 论文的攻击权限是知识库写入，且每个 query 注入一篇文档；这与修改真实长源、控制分块边界、跨块协调等权限不同。
- 100 个高效用干净 query 的筛选影响外推；跨论文 query 重叠未知，不与其它工作的 ASR/SASR 数值合并。
- 论文证明的是作者给定数据、检索器、模型、AUS 判定和预算下的软失败风险，不是所有 RAG 部署均会发生的普遍上界，也不是防御失效定理。

## 来源与实际阅读范围

- **正式页面**：[ACL Anthology](https://aclanthology.org/2026.acl-long.1397/)
- **正式 PDF**：[公开 PDF](https://aclanthology.org/2026.acl-long.1397.pdf)
- **DOI**：[10.18653/v1/2026.acl-long.1397](https://doi.org/10.18653/v1/2026.acl-long.1397)
- **arXiv**：[2604.18663](https://arxiv.org/abs/2604.18663)
- **本地证据副本**：[原始 PDF](<../pdf/2026.acl-long.1397__3b9041111cdd.pdf>)；SHA-256 `3B9041111CDD134061FAD36C54456F367A665B9AF06B7DE8D7BB681C826F8A93`

<!-- PDF_LIBRARY_START -->
## 科研数据库 PDF（按实际文件题名归集）

- [Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Beyond Explicit Refusals_ Soft-Failure Attacks on Retrieval-Augmented Generation.pdf>)
<!-- PDF_LIBRARY_END -->

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md) · [全部逐篇笔记](../README.md)
