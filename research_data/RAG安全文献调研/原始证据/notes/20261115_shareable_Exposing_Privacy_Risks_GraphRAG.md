# Exposing Privacy Risks in Graph Retrieval-Augmented Generation（整理笔记）

核对日期：2026-11-15。本文是按既有阅读记录和公开一手来源重新撰写的中文分析，不复制论文摘要或正文。

## 论文身份与阅读范围

- Jiale Liu、Jiahao Zhang、Suhang Wang，**Exposing Privacy Risks in Graph Retrieval-Augmented Generation**。正式载体为 *Findings of the Association for Computational Linguistics: ACL 2026*，第 18073–18093 页，DOI 10.18653/v1/2026.findings-acl.899。它是 Findings 论文，不应标成 ACL 主会 Long/Short 论文。
- **既有阅读记录**：L3，按 ACL Anthology 正式 PDF 的物理第 1–21 页逐页阅读，包括正文、参考文献和附录。本轮核验本地 PDF 哈希、首页与代表性表格数值；未重新逐页审读，也未复现实验。

## 方法、结果与适用边界

- 论文考察黑盒查询导致的 Graph RAG 隐私外泄。攻击者观察回答并尝试取得源文本、实体、关系及描述；其威胁模型不需要向知识库写入恶意内容。实验比较 Naive RAG、GraphRAG 与 LightRAG，并使用 Enron 和 HealthCareMagic 样本。
- 正式 PDF 物理第 4–5 页、表 1：每个表中设置使用 250 次查询。Qwen-Turbo 与 GraphRAG 条件下，HealthCare 的实体/关系泄漏为 68.6% / 72.3%，Enron 为 73.6% / 74.0%。作者先以单次查询的检索实体或关系为分母计算比例，再对查询求平均；不能称为全图唯一实体或关系泄漏率。
- 提示限制、相似度阈值和摘要等防御实验展示隐私与效用的权衡，但不构成形式化隐私保证。该论文不直接评估知识库投毒成功率、恶意块识别率或正常查询误删率，不能把隐私泄漏指标移作这些指标。

## 尚待核实

- 表 1 中 Enron / GraphRAG / Qwen-Turbo 的 Target Information 为 727。固定代码快照中，位于 healthcare 目录的评估脚本最多处理 250 条、每轮最多给该计数加一；但本轮未确认此脚本就是生成 Enron 该表格单元的脚本，也未排除不同计数口径，故不能单凭两者认定论文数据错误。需要作者提供对应数据、脚本和表格生成过程。
- 既有记录包含静态代码审阅；本轮未运行代码、下载索引资产或验证端到端结果。API 模型版本、数据与上游依赖的匹配仍待核验。

## 来源与携带性

- [ACL Anthology 正式记录](https://aclanthology.org/2026.findings-acl.899/)；[正式 PDF](https://aclanthology.org/2026.findings-acl.899.pdf)；[作者仓库](https://github.com/liule66/ACL26-GraphRAG-Privacy)；[固定版本 healthcare 评估脚本](https://github.com/liule66/ACL26-GraphRAG-Privacy/blob/3d707ee0763c5e4a3ad6b7fffc6e3138f9973595/graphrag-main/healthcare/target_attack_eval.py)。
- [证据地图](../../../../docs/RAG安全证据地图_20261102.md)：项目内相对路径，目标文件已被 Git 跟踪；本次核验使用工作区内容。
- [本机文库 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Exposing Privacy Risks in Graph Retrieval-Augmented Generation.pdf>)：**仓库外、仅本机路径，不随 Git 携带**。现存文件 21 页，SHA-256：47fd8a321b07fee5547956a5e052950312cd2c1e2f57851e6993e3c6e4e558bd。本轮未重新下载官方 PDF 以进行字节比对。
