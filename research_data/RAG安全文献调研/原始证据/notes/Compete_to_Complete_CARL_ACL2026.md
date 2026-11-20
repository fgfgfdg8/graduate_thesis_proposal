---
tags: [rag-security-evidence, acl2026, rag-robustness]
study_id: acl:2026.acl-long.258
report_id: 2026.acl-long.258
reading_level: L3
checked_date: 2026-11-12
---

# Compete to Complete: Co-opetition Adversarial Learning for Retrieval-Augmented Generation

**阅读状态：L3。** ACL Anthology正式PDF物理页1–16逐页阅读，覆盖正文、结果表、局限、附录和参考文献文字；未运行代码、复现或逐图视觉审阅。

## 身份与来源

- **作者**：Xin Liu；Yu-An Liu；Ruqing Zhang；Yixing Fan；Lixin Su；Jiafeng Guo；Xueqi Cheng。
- **正式版本**：ACL 2026 Main Conference, Volume 1: Long Papers，pp. 5710–5725；DOI `10.18653/v1/2026.acl-long.258`。按用户提供的第七版CCF目录，ACL为CCF-A。
- **官方记录**：[ACL Anthology论文页](https://aclanthology.org/2026.acl-long.258/)；[DOI](https://doi.org/10.18653/v1/2026.acl-long.258)。
- **本地PDF**：[Compete to Complete_ Co-opetition Adversarial Learning for Retrieval-Augmented Generation.pdf](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Compete to Complete_ Co-opetition Adversarial Learning for Retrieval-Augmented Generation.pdf>)；16页，365,790 bytes；SHA-256 `CD96A8CB8D215BFD618298062989FB87E7EB36A291756DECAFB648CAC39D4D7D`。

## 方法与实验

CARL（Co-opetition AdveRsarial Learning）把retriever与generator联合训练表述为minimax交替优化：先分别warm-up，再由retriever从当前分布采样困难文档、重建索引，generator在相关文档与hard negatives中学习选择正确证据。方法还将生成的答案作为pseudo-documents注入检索池以形成困难负例。训练语料为2018 Wikipedia；主实验覆盖NQ、HotpotQA、TriviaQA、FEVER、T-REx、zsRE和Wizard of Wikipedia七个数据集，默认生成器Qwen2-7B、检索器DPR。

Table 1报告CARL在四项数据集上取得最高值；作者报告七数据集加权平均64.7，高于ATLAS的61.6和RAAT的62.0。该平均跨Exact Match、Accuracy与F1等异质指标，作者在Limitations中承认加权聚合可能遮蔽任务差异。附录Table 9还展示CARL被主题相关但事实错误的hard negative误导、给出错误答案；因此其鲁棒性不是对误导证据的普遍保证。附录统计检验说明先称未做多重比较校正，后又称Bonferroni校正后仍显著，表述存在内部不一致。

## 与开题A/B的关系

这是训练期retriever–generator协同优化和检索噪声鲁棒性的CCF-A方法近邻，可作为误导/无用检索内容下的系统效用比较背景。它不构造语料投毒或攻击者控制的恶意来源，不测试真实长源经未知chunker生成的同源互补块及其共同必要性；也不提供冻结的检索块检测器、来源真实性判别、clean-query最终OR误删率或运行时过滤策略。不能把对抗训练等同于安全检测，也不能据其一般QA指标推出投毒防御效果。

## 制品与优先级输入

- 论文首页列出[作者CARL仓库](https://github.com/Peter0701/CARL)；本轮`git ls-remote`确认远端可访问，默认分支HEAD为`6241c972758164357586499caaac2ad6767447d0`，未审计仓库内容、许可或复现性，未运行代码。
- 类别=`method_reference / retrieval-noise robustness training`；venue=`ACL 2026 Main Long Papers`；CCF=`A`；公开日期=`2026-07-02`（会议起始日）；Google Scholar引用数=`null`/`not_observed`（截至2026-11-12未查询）；代码因子与总优先级未计算，留待全库候选池闭合后统一处理。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261112-carl)
