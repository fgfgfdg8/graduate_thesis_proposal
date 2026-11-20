---
tags: [rag-security-evidence, acl-paper]
study_id: doi:10.18653/v1/2026.acl-long.1558
report_id: 2026.acl-long.1558
bibkey: Ha-2026-MM-PoisonRAG
reading_level: L3
checked_date: 2026-11-12
---

# MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks

**阅读状态：L3。** 23页ACL正式PDF物理p1–23逐页阅读，包括正文、附录A–F与参考文献。p2–12此前已读；本次补读p1和p13–23。表格文字已核；未做逐图视觉分析、代码执行或复现实验。

## 身份与来源

- **作者**：Hyeonjeong Ha; Qiusi Zhan; Jeonghwan Kim; Dimitrios Bralios; Saikrishna Sanniboina; Nanyun Peng; Kai-Wei Chang; Daniel Kang; Heng Ji。
- **正式来源**：ACL 2026主会Long Papers，CCF-A；ACL ID `2026.acl-long.1558`；DOI `10.18653/v1/2026.acl-long.1558`；页33804–33826。
- **原文**：[ACL Anthology正式页](https://aclanthology.org/2026.acl-long.1558/)；[本地PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/MM-PoisonRAG_ Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks.pdf>)；23页；SHA-256 `666c5a8daaee0f75e1be25baf84a8758a8a1b5834ef0033e3a1a32b7a26514f9`。

## 研究问题与方法

论文评估多模态RAG系统如何受到外部知识库投毒。LPA以目标query为条件，构造错误答案与匹配图像/caption以操纵局部回答；GPA用一条不定向注入影响更广的query。实验覆盖多模态问答、不同retriever及对抗者可见程度，并研究改写、困惑度和对抗图像检测等防御。

## 结果与证据边界

- 摘要报告：受限访问下LPA攻击成功率最高56%，并可迁移至四种retriever；GPA单条污染内容可令生成准确率降至0%。这些数值来自论文的多模态设置。
- 附录C.1，Table 7（物理p15）：文本单独污染对照在所测管线中基本不改变正常检索与生成；LPA-Rt联合处理图像和caption，在MMQA、N=1时污染内容检索率为88.8%，攻击目标答案准确率为56.8%。该表中各列代表不同检索/重排配置，不应把单格结果当成所有配置的整体水平。
- 附录C.2，Table 8（物理p17）：在LLaVA reranker与Qwen-VL-Chat generator异构配置中，部分攻击效果减弱；攻击有效性受模型组件与优化设定影响。
- 附录C.3，Table 10（物理p19）：使用干净样本最大值阈值时，两种检测器对攻击样本检出均为0%；改用平均值阈值后，干净样本被标记比例达到perplexity 31.2–32.8%、对抗图像检测44.0–45.6%。这是指定数据和阈值上的检测/误报权衡，不证明普遍防御失效。
- 附录D补充了弱caption生成器、替代通用caption、降采样步数和DALL·E 3设置。弱caption生成下LPA仍有效但指标下降；这些结果仍受数据集、检索栈和实验配置限制。

## 与开题方向比较

该工作直接占据持久外部多模态RAG语料投毒和单条载荷广泛影响的攻击生态位，可用作多模态污染压力基线。论文没有测试真实单一长文本经受害者未知chunker产生的同源互补块、同query共同召回与逐块共同必要性，也没有提出文本块冻结检测器或评估独立clean-query上的最终OR误删率。因此它压缩多模态投毒的新颖性，但不等于文本同源chunk攻击或防御已被验证。

## 制品

- **作者仓库**：[HyeonjeongHa/MM-PoisonRAG](https://github.com/HyeonjeongHa/MM-PoisonRAG)。2026-11-12 `git ls-remote` 得到`main` SHA `e40f76a148d0dac081bde22e8e420ec3d0fb8e06`。
- 仓库README给出运行步骤并链接WebQA与MultimodalQA基准；作者生成的LPA/GPA对抗知识样本仍标为待发布。仓库可访问不代表完整生成数据或一次性复现实验包已发布。
- **复现状态**：未安装依赖、未运行代码、未下载模型权重或生成样本。

## 优先级输入（未评分）

- 类别=`attack / multimodal corpus poisoning`；分组=`ATTACK`；venue=`ACL 2026 main Long Papers / CCF-A`；`V_i=1.00`。
- 发表时间输入暂记`2026-07`（正式卷/月）；精确首次公开日期未核。Google Scholar引用数=`null`，状态=`not_observed`（截至2026-11-12未查询）。
- 引用速度、领域先验、归一化引用项、时间项、开源因子及最终优先级/名次未计算；全局候选池未闭合。代码可达及仓库SHA已记录；自有对抗样本待发布，权重与社区活跃度未核。`ready=false`。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261108-mm-poisonrag) · [元数据](../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261108-mm-poisonrag)
