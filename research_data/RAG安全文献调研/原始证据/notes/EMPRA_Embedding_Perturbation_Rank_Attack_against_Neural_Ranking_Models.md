# EMPRA: Embedding Perturbation Rank Attack against Neural Ranking Models

## 书目信息与证据身份

- 作者：Amin Bigdeli、Negar Arabzadeh、Ebrahim Bagheri、Charles L. A. Clarke。
- 正式 venue：ACM Transactions on Information Systems (TOIS), 44(4), 2026；Crossref 注册页码 1–42，DOI `10.1145/3801943`；online 2026-05-11，print 2026-05-31。
- CCF：A 类。核对《第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）》PDF 第32页“数据库/数据挖掘/内容检索”A类，第2项 TOIS。
- 目录身份源：本地 2026-11-10 Crossref ISSN 1046-8188 快照 `../audit/catalog_tois_2024-2026_sources/crossref_tois_volumes_42-44_2024-2026_20261110.jsonl`。
- 本地 PDF：`D:\学在东南\科研数据库\20_Research\Papers\RAG安全文献\EMPRA_ Embedding Perturbation Rank Attack against Neural Ranking Models.pdf`；652,289 bytes，41个物理页；SHA-256 `D3639BE76C016DFA9321FCF067B0268CACA2684035031E4CD1397C613169AF10`。
- 版本：PDF 来自作者机构公开稿 [Toronto Metropolitan University LS3 PDF](https://ls3.rnet.torontomu.ca/wp-content/uploads/2026/02/ABigdeli___EMPRA___TOIS___2026___CR_compressed.pdf)。2026-11-11 对该公开文件与论文库副本逐字节 SHA-256 比对一致。它是作者稿，不是已核实的 ACM VOR：扉页写有“Manuscript submitted to ACM”，刊头 DOI 仍是占位符 `10.1145/nnnnnnn.nnnnnnn`；ACM DOI PDF 直接请求返回 HTTP 403，未尝试绕过。正式 DOI、卷期及页码据 DOI 注册记录，不从占位符推断。
- 代码：论文 p14 给出作者仓库 [aminbigdeli/EMPRA](https://github.com/aminbigdeli/EMPRA)。本次未克隆、未运行，也未独立评估仓库与论文版本一致性。

## 阅读范围

精读作者稿物理页1–38，覆盖摘要、引言、相关工作、威胁模型、方法、实验设置、主要结果、质量评估、复杂度、案例及结论。物理页38之后为参考文献，未逐条核验；没有运行代码或复现实验。本文的逐页事实以下列物理页为锚点，不把未读参考文献计作阅读。

## 内容与威胁模型

EMPRA 研究对抗性操纵神经排序模型（NRM）的文档排序：攻击者选择一个目标文档，并通过插入生成文本提高它对查询的排序位置。攻击者不掌握受害排序器的梯度、结构或训练数据；方法生成阶段不依赖专门训练的 surrogate。论文仍允许攻击流程从受害模型返回的排序列表取得目标文档和当前 top-ranked 文档，因此“black-box”不等于完全零查询（pp.8–9）。

方法先把目标文档分句，在句向量空间沿查询、top document 及其中语义匹配句子的方向寻找相关文本；再把候选向量重建为文本，并将文本插入目标文档不同句间位置。候选选择用通用 NRM 的 query-document 相关性与 BERT Next Sentence Prediction 的局部连贯性加权（pp.10–14）。这属于单文档文本注入以操纵检索排序，不是 RAG 生成器提示注入，也不是恶意文档投毒后对知识库多文档证据的端到端研究。

## 主要实验证据

- 数据：MS MARCO V1 Passage Collection、TREC DL 2019、TREC DL 2020；使用不同 victim NRMs、ID surrogate 和 OOD generic NRMs（pp.14–20）。
- 目标分层：MS MARCO Dev 从原排名51–100选 Easy-5、从996–1000选 Hard-5；TREC DL 2019/2020各用200个测试 query（p.15）。
- 作者报告：MS MARCO Dev 上，ID 设置的 Easy-5 目标文档有95.6%被推入top-10，Hard-5为64.9%；使用其最佳 generic OOD ranker 时分别为74.3%和35.1%（Table 4, p.22）。TREC数据集也报告高成功率（Tables 5–6, pp.24–25）。这些是作者的基准实验结果，不是 RAG answer correctness 或真实部署成功率。
- 质量评估包含 LOR、BERTScore、反向蕴含逻辑一致性、perplexity、可读性、语言可接受性及人工判断（pp.16–18, 31–33）。人工评估为两名非计算机专业背景标注者的 Mixture 子集，不应泛化为真实用户检测率（pp.17–18）。
- 论文分析指出构造阶段对每个文本候选遍历可能插入位置，给出每批总复杂度 `O(Q·D·S^2)`；并报告1,000个 query-document 对的单GPU耗时（pp.34–35）。未在本次独立复算。
- p38提出输入阶段伪迹过滤、检索阶段多排序器一致性/交叉编码器复核、异常文档检测及对抗训练等防御方向；这些是讨论建议，不是本文经实验验证的防御方法。

## 与 RAG 安全主题的关系

**强方法近邻，不是同题直接先例。** 它表明攻击者可通过可读的内容增补操纵神经排序，把低位文档推入高曝光位置；这与 RAG 系统的检索上下文选择有明确接口关系。它会占据“文本级文档注入/排序操纵”相关工作位，适合作为威胁基线和差异化依据。

边界也很明确：论文没有评估 RAG 检索器加生成器的完整链路、恶意知识库摄入、chunk边界变化、多来源/多跳证据、最终答案事实错误或来源追溯；其 top-10 rank gain 不能代替 RAG ASR、错误答案率或正常证据误删率。对开题工作的直接启示是需要把 RAG 的证据单元、检索后生成影响及防御误伤另行实证，而不能把 NRM 排名提升结果写成 RAG 投毒已被证明。

## 未核实项

- ACM VOR PDF 因 HTTP 403 未取得；作者稿与 VOR 的最终排版/页码差异未核实。
- 未运行作者代码；未审计训练数据、随机种子、作者仓库当前状态或跨版本复现性。
- 只读论文主体，不核参考文献中每条相关工作；不报告引用数或优先级。
