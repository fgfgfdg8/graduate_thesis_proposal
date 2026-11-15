---
tags: [rag-security-evidence, arxiv-preprint]
study_id: arxiv:2505.23828
report_id: arxiv:2505.23828
bibkey: Yu-2025-SpaVLM
reading_level: L3
checked_date: 2026-11-12
---

# Spa-VLM: Stealthy Poisoning Attacks on RAG-based VLM

**阅读状态：L3。** 官方arXiv v1 PDF共14页；逐页阅读正文、表格文字、参考文献和附录A–F。未运行代码、复现实验或逐图视觉审读。

## 身份与来源

- **作者**：Lei Yu；Yechao Zhang；Ziqi Zhou；Yang Wu；Wei Wan；Minghui Li；Shengshan Hu；Pei Xiaobing；Jing Wang。
- **版本**：arXiv:2505.23828v1，2025-05-28提交，分类cs.CR；arXiv-issued DOI为`10.48550/arXiv.2505.23828`。DBLP记录为CoRR/arXiv；截至2026-11-12未核实正式会议或期刊版本，因此不赋CCF等级。
- **原文**：[arXiv记录](https://arxiv.org/abs/2505.23828)；[DBLP CoRR记录](https://dblp.org/rec/journals/corr/abs-2505-23828.html)。
- **本地PDF**：[Spa-VLM_ Stealthy Poisoning Attacks on RAG-based VLM.pdf](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Spa-VLM_ Stealthy Poisoning Attacks on RAG-based VLM.pdf>)；14页，5,457,764 bytes；SHA-256 `CB91EBF7B226F14B253B47901FF0CF315D63B1D5937CD84DFEABCF82ACBDFE76`。

## 威胁模型与方法

目标系统是图像与文本联合查询的多模态RAG-VLM：视觉检索先取Top-5知识条目，再由Q-Former重排并向回答模型提供Top-5文本。攻击者按目标问题向知识库注入图文配对条目；论文假设攻击者可访问视觉检索器和文本重排器参数。视觉侧用同类别图像簇中心近似未知目标图像嵌入，以PGD迭代40步并将像素扰动限制在ε=0.05；文本侧由VLM按目标问题/答案生成，再优化与图文融合查询的嵌入相似度并迭代改写至目标答案命中。默认每个目标问题注入N=5个图文条目。

## 结果与证据边界

- **数据与分母**：Encyclopedic-VQA知识库约2M条，InfoSeek知识库约100K条。附录称每数据集每轮抽取200个封闭式目标问题，重复10轮且不复用问题，共2,000个独立目标问题；没有明确说明攻击载荷构造/优化问题与最终ASR评测问题及图像之间是否严格隔离。
- **主结果**（Table I，PDF p.6）：E-VQA的ASR/Precision为0.87/0.85，InfoSeek为0.83/0.84；对应PoisonedRAG基线为0.02/0.03和0.01/0.01。Precision指最终Top-k文本中恶意文本所占比例，不等同于答案正确性或端到端安全率。
- **防御结果**（Table V，PDF p.8）：输入图像随机缩放/填充后的ASR为0.88/0.86；问题改写后的ASR为0.83/0.85；SHA-256精确重复文本过滤后为0.87/0.83。作者报告这三种设置均未有效阻断攻击；数值仅对应本文数据、组件和协议。
- **方法核对点**：式(6)定义损失为负余弦相似度，式(7)却写成沿`+sign(∇L)`更新，同时文字称提高余弦相似度。按通常梯度符号约定，公式与目标方向表述看似不一致；在代码未核实前保留为待澄清的复现风险，不据此断言实验实现错误。
- 论文限制包括对视觉检索器及文本重排器参数的白盒访问、只评估两个Wikipedia来源数据集；防御仅覆盖三种基础方法。正文没有提供可确认的作者代码仓库链接，本轮未运行或复现。

## 与开题方向比较

该工作直接占据“多模态RAG外部知识库图文联合投毒”这一邻近生态位，故不能把多模态RAG投毒笼统表述为尚未研究。它与开题A的核心设置仍不同：开题攻击者只改写一份长文本源，经受害系统未知分块后形成同源互补角色块；Spa-VLM面向含图像查询的VLM，并注入多个独立图文条目，没有测试未知文本chunker、同一源文档的角色块共同召回或逐块/联合删除的组合必要性。它也不是开题B的检索上下文文本块检测器：随机图像预处理、query改写和精确重复过滤均未处理文本块关系、来源血缘或clean-query最终OR误删率。

## 制品与优先级输入

- 论文和arXiv记录未提供可确认的作者代码仓库或独立生成数据下载地址；使用的底层E-VQA/InfoSeek知识库不等于该文作者发布的攻击制品。
- 类别=`attack / multimodal RAG corpus poisoning`；venue=`arXiv/CoRR preprint`；CCF=`不适用，正式venue未核`；首次公开=`2025-05-28`。Google Scholar引用数=`null`、`not_observed`（截至2026-11-12未查询）；代码因子及总优先级/排序暂不计算，留待相关候选池闭合后统一处理。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261112-spa-vlm) · [元数据](../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261112-spa-vlm)
