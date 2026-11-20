---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2308.09861
reading_level: L3
checked_date: 2026-11-16
---
# Black-box Adversarial Attacks against Dense Retrieval Models: A Multi-view Contrastive Learning Method

**阅读范围：L3。** 实际阅读作者托管的十页会议排版稿物理第 1–9 页正文；第 10 页参考文献用于追踪，未声称逐条精读。未运行实现或复现实验。本文通过已读 AGGD 的参考文献追溯纳入。

- **作者：** Yu-An Liu、Ruqing Zhang、Jiafeng Guo、Maarten de Rijke、Wei Chen、Yixing Fan、Xueqi Cheng。
- **正式书目：** CIKM 2023，1647–1656；[ACM 出版者 Crossref 登记](https://api.crossref.org/works/10.1145/3583780.3614793)及[DOI](https://doi.org/10.1145/3583780.3614793)；会议在用户提供的 CCF 第七版目录物理第 36 页属 B 类，具体 Full/Regular track 尚未独立核实。
- **阅读版本：** [作者托管 PDF](https://jiafengguo.github.io/2023/CIKM2023-MCARA.pdf)与[论文库 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Black-box Adversarial Attacks against Dense Retrieval Models_ A Multi-view Contrastive Learning Method.pdf>)的 SHA-256 均为 `2a23d86270321fe30bcd4e9b2cd6ac54eef5669f7f97bfd8eab04ba836a25192`（2026-11-16 核对）。[arXiv:2308.09861v1](https://arxiv.org/abs/2308.09861v1)为同题同作者的另一公开版本，其 PDF SHA-256 为 `4f8cadd0e0b944241540e1bd6e973dc3f7e43941ec84d2917cfc3a1f30821073`，与本地稿不同；未逐字对照 ACM 最终 PDF。
- **制品：** 论文 p.5 给出[作者代码仓库](https://github.com/ict-bigdatalab/AREA)；[固定提交 `74da2326`](https://github.com/ict-bigdatalab/AREA/tree/74da2326b3ece4b3874aae83d0e0b42eb361942b)可见代码目录。静态检查其 [blackbox_attack.py](https://github.com/ict-bigdatalab/AREA/blob/74da2326b3ece4b3874aae83d0e0b42eb361942b/blackbox_attack.py#L147) 第 147 行调用 `run_parse_args()`，该文件未见同名定义或导入；未执行该路径，尚不据此断言完整项目不可复现。数据完整性、许可及运行条件待核。
- **引用与优先级：** 论文内容和资源优先；Google Scholar 引用数未观察，保留未知，其他评分维度见[元数据汇总](<../../../../docs/RAG安全文献补查元数据_20261102.md#src-5b36637cbea9998b>)。

## 问题、威胁模型与方法

论文提出 AREA 任务：针对已知查询，通过修改原来位于初始候选集合之外的目标文档，使它进入稠密检索候选集。攻击者使用目标系统输出，不直接取得目标稠密检索器参数；论文用“检索后重排”的黑盒管线给出排序反馈，并训练双编码器代理（pp. 2–4）。该权限与只拥有一个真实源文件、面对未知分块器和实际 RAG 检索结果的约束不能直接等同。

MCARA 对已召回文档聚类构造多视角参照，在代理表征空间中把目标文档各视角拉近相应参照、推离周边非候选文档，再按重要性作受约束词语替换并限制文本流畅性（pp. 4–5）。多视角针对**单个文档的表示**，不是把攻击拆成同源互补的多个检索块，也不是逐块必要性试验。

## 实验口径与结果

- **数据与目标：** MS MARCO Document（约 321 万文档）和 Passage（约 884 万 passage）；每个数据集随机选 500 条开发集查询。每个查询分别选 Easy、Middle、Hard 不同初始排名目标，再从原有 30 项目标随机抽 10 项组成 Mixture（pp. 5–6）。
- **模型：** 黑盒管线以 coCondenser 作目标稠密检索器、PROP 作重排器，使用 BERT-base 双编码器代理；Document 的候选集 `K=100`，Passage 的 `K=1000`（p. 6）。这是具体测试配置，不是任意真实 RAG 环境。
- **结果：** Table 1（p. 7）的 Mixture 条件下，MCARA 对 Document 的 `SRR@100=69.9%`、对 Passage 的 `SRR@1000=60.5%`。SRR 是被改写目标进入对应检索集合的比例；两项不能解释为生成端答案攻击成功率。对照直接关键词堆砌同列分别为 61.1% 和 52.0%。
- **自然性评价：** Table 3（p. 8）由 5 名标注者对每种攻击随机抽取的 32 个 Mixture 样本评分；MCARA 的流畅性均分 3.81/5，原文档 4.32/5。样本量有限，不能据此断言对所有读者或部署场景不可察觉。
- **重排与黑盒：** Table 4 的重排测试只在已成功进入候选集的对抗文本上进行；不能把该条件下排名比例当作总体端到端成功率。Table 6（p. 9）比较了具体代理和模拟白盒配置，不保证其他检索器下迁移。

## 对开题 A/B 的约束

**A：** AREA 与 MCARA 是单目标文档初始召回攻击的明确前身，限制“首次针对稠密检索、黑盒目标文档召回”的宽泛叙述；其未评测 RAG 生成、真实长源经未知分块后两块共同召回，以及固定背景下逐块和联合删除的共同必要性。

**B：** 论文测试垃圾文本检测及流畅性，而非检索后的恶意证据识别、跨块关系核验或正常查询级误删与 QA 效用校准。相近度优化及自然性约束是攻击适应性评测的参考，不是现成防御效果。

[证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-cikm2023-mcara>) · [攻防总结](<../../../../docs/RAG安全文献攻防技术手段总结报告.md#src-fb1682dc8e7f28a5-h119>)
