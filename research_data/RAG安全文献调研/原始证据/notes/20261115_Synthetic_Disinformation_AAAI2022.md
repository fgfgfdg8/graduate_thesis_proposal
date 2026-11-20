---
tags: [rag-security-evidence, fact-verification, poisoning, ccf-a]
reading_level: L3
checked_date: 2026-11-15
---
# Synthetic Disinformation Attacks on Automated Fact Verification Systems

## 身份、文件与阅读范围

- **作者与正式身份：** Yibing Du、Antoine Bosselut、Christopher D. Manning；[AAAI 2022 Technical Track on Speech and Natural Language Processing](https://ojs.aaai.org/index.php/AAAI/article/view/21302)，CCF-A；*Proceedings of the AAAI Conference on Artificial Intelligence* 36(10):10581–10589，2022-06-28，DOI [10.1609/aaai.v36i10.21302](https://doi.org/10.1609/aaai.v36i10.21302)。
- **实际阅读：** [arXiv:2202.09381v1](https://arxiv.org/abs/2202.09381v1) 的[本地作者版PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Synthetic Disinformation Attacks on Automated Fact Verification Systems.pdf>)物理p1–12全部逐页阅读，包括参考文献及附录A–D；阅读等级L3仅代表该作者版，未逐字比对出版社版。文件1,479,879字节，SHA-256 `24db35023ebc6f50f41f4e0b36592bcd11fec3c885d1b5d6f37dc688033f78e8`。
- **版本区别：** AAAI论文页面确认正式卷期和题名；本机请求出版社下载地址返回HTTP 200但实际为HTML，故未将其当作出版社PDF。作者版页面标示CC BY 4.0；出版社版与作者版的内容差异未逐项核查。
- **去重：** 以完整标题、DOI和arXiv ID检索三份主文档、BibTeX、现有笔记及原始证据文本；另在主文档、BibTeX和笔记中核查作者组合及方法别名；命中其他论文的参考文献或提及，不等同于本论文已有逐篇阅读记录。指定文献库标题文件名未见已有文件。
- **制品：** 原文p2/p12链接的[作者代码库](https://github.com/Yibing-Du/adversarial-factcheck)可打开，仓库README与原文身份一致；未运行、未验证数据完整性或结果复现。Google Scholar引用数和评分待统一核查。

## 研究问题与攻击模型

论文研究自动事实核验中，攻击者污染检索证据来源后对声明分类的影响。系统先检索文档及句子，再预测支持（SUP）、反驳（REF）或信息不足（NEI）；此处核验模型和检索器不能等同于现代生成式LLM-RAG（p1–2）。

- **ADVADD：** 面向待核验声明生成合成文档，将文档作为可检索证据加入库中；每个声明生成10篇文章后按段落组织（p3）。FEVER文档层检索以命名实体和关联Wikipedia页面的重合模拟合成文档可召回，而非实证攻击者能修改线上Wikipedia（p4、p7）。SCIFACT使用统计检索，不能把FEVER的实体模拟一概套用。
- **ADVMOD：** 在与声明相关的已有证据文档中添加合成句；比较意图保留声明语义的改写、关键词替换以及直接加入原声明的oracle（p6–7）。这是在已有来源上的修改先例，但论文没有声称单篇真实长文经过未知分块器得到两种互补角色块，更没有逐块/联合干预证明它们共同必要。

## 实验与适用边界

| 位置 | 证据及限制 |
|---|---|
| p3–4，Table 2 | FEVER开发集仅使用REF/NEI：CorefBERT原准确率73.05%，ADVADD-min单条对抗句34.80%，ADVADD-full 28.59%；各值是准确率，非攻击成功率。论文p3给全开发集19,998条，但表中未直接写所用REF/NEI总分母，不擅自补数。 |
| p4，Table 3 | 作为检索语料规模，FEVERDB 5,416,537篇、GROVER段落995,829条；不能把这些语料规模当作独立评测声明数或有效攻击数。 |
| p5、p10 | 随机证据替换对照中，KGAT的REF准确率降幅为6.63个百分点，对抗证据为30.05个百分点；NEI分别为7.73和53.42个百分点。它支持污染内容带来额外影响，但不是同源多块共同必要的消融。 |
| p5–6，Table 5 | SCIFACT使用300个开发声明；VeriSci的abstract-label由51.03降至25.57，报告为原表任务指标，不换称ASR。 |
| p6 | COVIDFACT测试使用271个REF声明；Top-1/Top-5准确率原文均报告83.8%至69.4%，不得推广到所有类别。 |
| p6–7，Table 6 | FEVER CorefBERT的ADVMOD-paraphrase准确率为32.62%，原值73.05%；NEI下KGAT对关键词替换更敏感，不能写成改写攻击在所有设置都更强。 |
| p7、p11–12 | 作者明确FEVER实体召回为模拟，并指出攻击生成时使用确切声明；约20%的声明可能被生成文本直接复制。SUP未进入FEVER/COVIDFACT主结果：SUP自动反声明的KGAT准确率从86.2%升至87.5%，100个手写反声明子集由92%升至93%。失败案例限制了覆盖面。 |
| p12 | 原文称每个确定性设置只运行一次，未提供多次随机重复；不能赋予跨种子稳定性或置信区间。 |

## 与开题及近邻的关系

本文比[Fact2Fiction](20261115_Fact2Fiction_AAAI2026.md)更早给出目标条件化证据污染和已有证据文档修改的先例；Fact2Fiction进一步处理基于判定解释的代理子问题规划。两者均不应被描述为已经验证真实长源、未知分块、同一查询同源块共召回以及在固定背景下逐块/联合删除证明共同必要的完整交集。本文不评估开题的四统计防御或最终query级误删。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-20261115-synthetic-disinformation>) · [元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md>)
