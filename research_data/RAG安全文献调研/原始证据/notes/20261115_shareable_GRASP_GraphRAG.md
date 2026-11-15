# GRASP：Graph RAG 子图重构攻击（整理笔记）

核对日期：2026-11-15。本文是按既有阅读记录和公开一手来源重新撰写的中文分析，不复制论文摘要或正文。

## 论文身份与阅读范围

- Minkyoo Song 等，**Graphs Don’t Stay Secret: Practical Subgraph Reconstruction Attacks on Defended Graph RAG**。arXiv:2602.06495v2，2026-06-17。v1 使用题名 *Subgraph Reconstruction Attacks on Graph RAG Deployments with Practical Defenses*；两者是同一 arXiv 记录的不同版本。
- DataCite 将 10.48550/arXiv.2602.06495 登记为 arXiv 预印本 DOI，不是已核实的期刊或会议出版 DOI。作者主页将本篇标为 Under Review；本次未找到足够证据确认正式发表 venue 或 track。作者主页相邻的 IEICE 条目属于另一篇工作，不能据此将 IEICE 归给 GRASP。
- **既有阅读记录**：L3，按 arXiv v2 PDF 物理第 1–19 页逐页阅读，包括正文、附录和参考文献。本轮核验本地 PDF 哈希、首页及下列代表性结果，没有重新逐页审读，也没有复现。

## 方法、结果与适用边界

- 攻击者通过查询接口访问 Graph RAG，目标是对已知目标实体重构一跳实体关系及其类型；论文的黑盒设定不授予知识库写权限。它研究知识结构和机密性泄露，而不是注入恶意文档或检索投毒。
- 按 v2 物理第 9 页和表 II：每个图谱随机选取 50 个度至少为 5 的目标，默认每目标至多 10 次查询。Enron、Claude Haiku 4.5 条件下，关系类型匹配的目标级宏平均 F1 最高为 82.9。这个值不是整张图的抽取比例，也不能替换其他模型或数据集的结果。
- 评估基于受控语料构建的 Graph RAG 实例；论文还讨论减轻抽取的措施。结果不能直接证明真实企业在线服务的整体泄漏率，也不能证明投毒攻击成功或污染块检测能力。该工作适合作为 Graph RAG 隐私威胁近邻。
- 既有检索未找到作者发布的 GRASP 官方实现；这不证明代码不存在。本轮没有运行实验，目标采样、数据构图及逐目标预测仍需可用工件才能独立复核。

## 来源与携带性

- [arXiv v2 记录](https://arxiv.org/abs/2602.06495v2)；[arXiv v2 正文](https://arxiv.org/html/2602.06495v2)；[DataCite 预印本登记](https://api.datacite.org/dois/10.48550/arXiv.2602.06495)；[作者发表页面](https://minkyoo9.github.io/)。
- [证据地图](../../../../docs/RAG安全证据地图_20261102.md)：项目内相对路径，目标文件已被 Git 跟踪；本次核验使用工作区内容。
- [本机文库 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Subgraph Reconstruction Attacks on Graph RAG Deployments with Practical Defenses.pdf>)：**仓库外、仅本机路径，不随 Git 携带**。现存文件 19 页，SHA-256：a512502b92161cc4d08789b25c845d7fb293ce33401ea1453574adf578c3e2e8。既有记录称其与当时 arXiv v2 PDF 字节一致；本轮未重新下载比对。
