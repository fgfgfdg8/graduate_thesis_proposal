---
tags: [llm-generated, rag-security-evidence, privacy]
study_id: doi-10.1007-s11432-024-4441-4
reading_level: L3
checked_date: 2026-11-13
---
# RAG-leaks: Difficulty-Calibrated Membership Inference Attacks on Retrieval-Augmented Generation

**阅读状态：L3。** 出版者正式刊载版18页全文文本已逐页核读；本机未能保存PDF，不代表复现或对其他版本的核查。

- **作者**：Guangshuo Wang；Jiajun He；Hao Li；Min Zhang；Dengguo Feng
- **正式出处**：*Science China Information Sciences*, 2025, 68(6), article 160102, pp. 160102:1-160102:18；Version of Record于2025-05-21发布
- **DOI**：[10.1007/s11432-024-4441-4](https://doi.org/10.1007/s11432-024-4441-4)
- **CCF**：第七版目录第67页将该刊列于交叉/综合/新兴期刊A类
- **全文状态**：出版社文章页标记订阅限制；通过出版社CDN取得18页全文文本并逐页阅读。本机直连CDN发生DNS解析失败，未落盘PDF；未绕过访问控制
- **引用与优先级**：Google Scholar未观测；优先级未计算
- **代码**：未核实

## 方法与结果

DC-MIA推断候选文本是否属于RAG检索知识库。攻击者通过黑盒输出查询，但使用生成器、检索器和数据分布先验、辅助样本及16个参考RAG；参考系统用于估计难度条件下成员/非成员得分分布，再做似然比判定。因此不是零先验API-only攻击。主要实验使用HealthCareMagic-100k和AGNews，默认top-k=4；目标与shadow库各抽8,000条，评估各用1,000条成员及1,000条非成员，并另用100+100条辅助样本。

Mistral + AGNews的AUC为0.809，对比S-MIA的0.650；TPR@1% FPR为4.129%对2.011%。Mistral + HealthCareMagic的正文AUC报告0.662，而Table 1为0.661；保留此0.001差异，不静默统一。结果范围受所用模型、数据与较强先验设定约束。

## 与开题的关系

这是检索数据库成员隐私近邻，不是知识库投毒、恶意块识别、来源鉴真或完整性防御。成员推断回答“候选文本是否入库”，不能推出该文本为真、为毒或有攻击意图；反向也成立。若开题使用广义RAG安全表述，应在相关工作中纳入并分开定义机密性和完整性威胁。

## 来源与追溯

[出版社正式记录与全文入口](https://doi.org/10.1007/s11432-024-4441-4)。精读页码按出版社全文文本阅读器计，共18页。引用数未核，未运行代码或复现。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-rag-leaks) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
