# TIFS 2026 第21卷：14条目录增量（2026-11-19）

核查日期：2026-11-19（Asia/Shanghai）。TIFS为年度连续卷，官方卷页不提供月issue；本记录以IEEE Xplore Volume 21的年度卷页和导出CSV为目录单位。

## 来源与集合闭合

- 官方入口：[IEEE Xplore TIFS Volume 21](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=11313711&punumber=10206)；页面显示`Showing 1-25 of 689`，并可按`Export → Download`导出年度CSV。
- 原始CSV：[本地副本](../catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.18-12.03.04.csv)，2,102,891 bytes，UTF-8 BOM；SHA-256 `aa9f78b9d2505f144fedd9b0e31c336e140d30bc8f350185a678c1e70390d745`。该CSV含摘要，按既有策略保留在本机原始证据目录，不把摘要原文复制进主报告。
- 集合差：2026-11-15的675条（650旧快照＋25条增量）对2026-11-19的689条，新增14、移出0；689个DOI均唯一。
- 14条均逐一阅读官方CSV摘要，阅读等级为L1；没有下载PDF、没有全文阅读、没有复现实验，也没有查询引用数。
- 14条题名/摘要未出现直接RAG、GraphRAG、检索语料投毒、恶意块检测或query级误删方案。6条列为M2跨域方法边界，其余为排除；M2不升级为RAG安全候选。
- 机器可读精简元数据：[14条JSONL](./TIFS2026_volume21_increment14_20261119.jsonl)，不含摘要原文；SHA-256 见下方。

## 14条逐项筛查

|#|DOI与题名|TIFS身份、摘要与判断|
|---:|---|---|
|1|[10.1109/tifs.2026.3744624](https://doi.org/10.1109/tifs.2026.3744624)，*Information-Theoretic Side-Channel Analysis of LWE-Based Cryptosystems Using the Replica Method*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9966–9981；L1摘要。**排除**：LWE密码体制的副本法信息论侧信道分析；不是检索证据。|
|2|[10.1109/tifs.2026.3744634](https://doi.org/10.1109/tifs.2026.3744634)，*Taming the Shapeshifter: A Dynamic Framework for Detecting and Defending Against Self-Evolving Automated Jailbreak Attacks*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.10041–10056；L1摘要。**M2 方法边界**：用轻量语义嵌入和向量数据库检测自适应演化越狱查询；向量近邻用于恶意query识别，不是证据块检测或正常多跳保留。|
|3|[10.1109/tifs.2026.3750687](https://doi.org/10.1109/tifs.2026.3750687)，*Shared Features Are Not Enough: Injecting Modality-Specific Cues Into Unsupervised Visible-Infrared Person Re-Identification*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9890–9903；L1摘要。**排除**：无监督可见光—红外行人重识别；处理跨模态伪标签噪声，不是检索证据安全。|
|4|[10.1109/tifs.2026.3750688](https://doi.org/10.1109/tifs.2026.3750688)，*Differentially Private Distribution Release of Gaussian Mixture Models via KL-Divergence Minimization*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9904–9919；L1摘要。**排除**：GMM参数发布的差分隐私与KL效用优化；不是检索或生成安全。|
|5|[10.1109/tifs.2026.3750725](https://doi.org/10.1109/tifs.2026.3750725)，*Adaptive Spatial-Directional Guidance for Safe Text-to-Image Diffusion Model*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.10089–10103；L1摘要。**M2 方法边界**：文本到图像扩散的轨迹级风险判定、空间局部安全引导；是生成模型安全，不是外部文档检索。|
|6|[10.1109/tifs.2026.3750734](https://doi.org/10.1109/tifs.2026.3750734)，*AuditCT: Decentralized and Efficient Identity Traceability Scheme for Monero Transactions*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9874–9889；L1摘要。**排除**：Monero交易的身份可追踪性与分层群签名；对象是区块链隐私与合规。|
|7|[10.1109/tifs.2026.3751567](https://doi.org/10.1109/tifs.2026.3751567)，*ELSA: Efficient Lightweight Graph Modeling With LLM-Enhanced Supervision for Ethereum Attack Transaction Detection*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9997–10008；L1摘要。**M2 方法边界**：以函数调用轨迹构轻量交易图，并用LLM精炼注释提供监督检测Ethereum攻击交易；图关系监督可作类比，但不是文本知识库或检索块净化。|
|8|[10.1109/tifs.2026.3751571](https://doi.org/10.1109/tifs.2026.3751571)，*Uncovering and Measuring Privacy Leakage in Mobile Remote Logging at Scale*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.10009–10024；L1摘要。**排除**：移动应用远程日志隐私泄漏测量；对象是日志，不是RAG文档。|
|9|[10.1109/tifs.2026.3751572](https://doi.org/10.1109/tifs.2026.3751572)，*Toward Interpreting and Boosting Adversarial Transferability via Transferability Error Minimization*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.10057–10072；L1摘要。**排除**：图像分类模型的迁移对抗样本与理论误差界；不是RAG语料/块。|
|10|[10.1109/tifs.2026.3751575](https://doi.org/10.1109/tifs.2026.3751575)，*Bridging Semantic Logic Gaps: A Cognition-Inspired Multimodal Boundary Preserving Network for Image Manipulation Localization*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9936–9950；L1摘要。**M2 方法边界**：用LLM文本补偿图像篡改定位，并以图文中心歧义模块降低不可靠文本影响；可作不可靠辅助证据加权参考，不是RAG检索。|
|11|[10.1109/tifs.2026.3751580](https://doi.org/10.1109/tifs.2026.3751580)，*Pixel-Adaptive Purification: From Uniform to Spatially Heterogeneous Noise Injection*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.10073–10088；L1摘要。**M2 方法边界**：测试时图像对抗净化，按SNR/内容复杂度做空间异质噪声并自动停止；与B的“强度—语义保留”权衡有远类比，对象是像素不是RAG块。|
|12|[10.1109/tifs.2026.3751582](https://doi.org/10.1109/tifs.2026.3751582)，*Intelligent Wiretap Code Design: Exploiting Wireless Endogenous Security via Information Theory and Deep Learning Integration*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9982–9996；L1摘要。**排除**：无线窃听码设计与物理层安全；不涉及LLM或检索。|
|13|[10.1109/tifs.2026.3751583](https://doi.org/10.1109/tifs.2026.3751583)，*DxG-Fuse: Description-Guided Fusion for Multimodal Fake News Detection via MLLMs*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9920–9935；L1摘要。**M2 方法边界**：多模态假新闻检测融合多视角描述、图文一致性与伪造视觉线索；是内容真实性判断，不是检索器投毒或最终答案校准。|
|14|[10.1109/tifs.2026.3751584](https://doi.org/10.1109/tifs.2026.3751584)，*Robust Physical-Layer Authentication via Active Time-Varying RIS: A Multi-Domain Protection Framework*|TIFS 2026，21卷，CCF-A；Date Added To Xplore `17 Nov 2026`；pp.9951–9965；L1摘要。**排除**：RIS辅助物理层认证与重放攻击防护；对象是无线信道。|

## 证据边界

本批只覆盖2026-11-19导出快照的14条新增记录；2026年仍未结束，689条不是最终年终总数。2024/2025卷的734/930条官方CSV已另行对账；2026-11-15的675条快照及其25条增量仍按原审计保留，不重复阅读。TIFS为连续卷，不把空白Issue字段伪造成月度issue。所有判断限于摘要，不等于全文排除。

JSONL SHA-256：`b0847ec33ca72a33015fd988c27e1e63bb12782bd9eb60211abadc3fb72d6fcd`。
