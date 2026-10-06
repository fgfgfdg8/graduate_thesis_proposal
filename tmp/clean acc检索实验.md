# Clean RAG pipeline 审查：低准确率的原因与修复方案

日期：2026-10-03。对象：`results/full_clean_top5_20260927`。状态：**只读诊断完成，修复待批准**。

## 1. 结论与已有结果

**当前 pipeline 有可修复的问题，优先级最高的是人工超短尾块、文档级标签与实际支持句之间的断层，以及跨数据集统一使用严格 EM 的评测偏差。已有证据不支持把主要原因归结为 embedding 文件损坏。**

HotpotQA 的 gold 数据大部分可以从本地官方文件恢复到句子，再对齐到现有全文；它不是大规模缺失 gold 文档。MS MARCO 的单正例 qrels 与自由文本 QA 答案属于两套评测信息，不能把未标注文档一律视为噪声，也不能用 3.10% 的严格 EM 代表全部语义正确率。NQ 的文档命中率较高，但它使用 validation 自带文档组成的小库，不能直接与全 Wikipedia 的 HotpotQA 比较。

### 1.1 完整 clean 实验的实际口径

| 数据集 | 全量 query | 有 QA 答案 | 正确数 / 严格 EM | Token F1 | 至少一篇 gold 文档 Hit@5 | 全部 gold 文档命中 |
|---|---:|---:|---:|---:|---:|---:|
| NQ validation | 7,830 | 4,462 | 1,353 / **30.32%** | 44.66% | 86.98% | 86.98% |
| HotpotQA fullwiki validation | 7,405 | 7,405 | 730 / **9.86%** | 13.38% | 31.86% | **2.63%** |
| MS MARCO document dev | 5,193 | 5,169 | 160 / **3.10%** | 16.38% | 24.30% | 24.30% |

QA 分母为有答案的题；检索指标分母为有 qrels 的题，分别为 4,462 / 7,405 / 5,193。MS 的两种分母相差 24。NQ 另外 3,368 题没有当前 QA gold，它们参与检索与生成，但不参与 ACC。当前 [nq_answers](../src/common/datasets.py#L14) 提取 short answers 或 yes/no，不把 long-answer-only annotation 自动转换为短答案；因此这 3,368 题不等于原数据文件丢失，也不能把其 UNKNOWN 全部解释成检索失败。MS 的 QA 答案通过官方 query ID 与完全相同的问题文本连接得到，仍需与 document relevance 标签分开解释。

实际协议是无监督 `facebook/contriever`，FP16 模型、FP32 attention-mask mean pooling，包含 CLS/SEP，query/document 都做 L2 normalization，FAISS `IndexFlatIP` 因而计算 cosine。正文窗口为 **256 tokens、overlap=0**；本文的“超短块”指该协议产生的不足 8/32/64 tokens 的块，不是另一次 64-token 实验。

生成配置为 dancher-01 Qwen3.8-27B、temperature=0、top_p=1、seed=0、thinking=false、max_tokens=1000；直接用真实 Top-5 正文，不使用 reranker。system prompt 为：

> Answer based on context. Output: ‘Final answer: &lt;answer&gt;’. If the excerpts do not determine the answer, output ‘Final answer: UNKNOWN’.

user 模板为 `CONTEXT: {context}\nQUESTION: {question}`。上下文由五个 chunk 正文以双换行连接；未给后续 chunk 额外补标题。全部 20,428 题已完成，未解决的 API 请求为 0。三个数据集在有答案题中“截断或不可解析”的并集分别为 115、121、42 题，无法解释主要准确率差距。

### 1.2 语料范围不同，难度不能直接横比

| 数据集 | 实际 corpus | 文档数 | 256-token 向量数 |
|---|---|---:|---:|
| NQ | validation 原始页面去重后的集合 | 7,378 | 235,618 |
| HotpotQA | 2017-10-01 processed Wikipedia 全文库 | 5,486,212 | 13,400,704 |
| MS MARCO | document-dev 的 Top-100 文档并集，加全部正例文档 | 401,855 | 4,913,542 |

本次抽查 Hotpot 原始 dump 的 Anarchism、Autism、Albedo，分别有 86、77、42 个段落记录，确认该输入包含长篇正文，并非仅把 intro paragraph 换了名字。Hotpot 官方 query 的 `context` 则以段落组织。当前全文检索因此比仅检索官方段落或小型受控语料多出大量竞争内容。

NQ train 的预编码任务不在本轮结果中。将其加入检索库会改变实验语料范围，必须另报结果，不能直接当作这轮 clean 的修复。

## 2. Pipeline 中哪些环节存在问题

### 2.1 分块：人工短尾是明确的构造问题

当前 [indexing.py](../src/common/indexing.py#L128) 将 `title + newline + text` 整体 tokenize 后，每 256 个 WordPiece 硬切一次。它不考虑词、句子、段落边界，也不平衡最后两个窗口。标题仅进入首块；末尾剩下 1–3 个 token 时，也会建立一个独立向量。

| 统计 | NQ | HotpotQA | MS MARCO |
|---|---:|---:|---:|
| Top-5 中 `<8` tokens | 0.14% | **29.62%** | 8.40% |
| Top-5 中 `<32` tokens | 0.44% | **68.96%** | 22.23% |
| Top-5 中 `<64` tokens | 0.78% | **84.98%** | 34.99% |
| 召回 chunk 长度中位数 | 256 | **17** | 158 |
| 五块全部 `<32` 的 query | 12 / 7,830 | **1,875 / 7,405** | 109 / 5,193 |
| Top-5 有重复正文的 query | 444 | 1,094 | 891 |

HotpotQA 全库只有 7.33% 的块短于 32 tokens，却占据 68.96% 的召回槽位，富集约 **9.40 倍**；MS 相应为 1.00% → 22.23%，约 **22.21 倍**。在召回的 `<32` 块中，Hotpot 有 19,787/25,533 块、MS 有 5,728/5,771 块来自非首块，在本协议下即人工尾块。

Hotpot 全库 `<8` 的 113,995 块中，82,305 块是人工余块，31,690 块来自原生短文档；MS 为 11,155 个人工余块和 22 个原生短文档。**应修复尾块的独立表示，保留原生短文档和所有原文内容。**直接删除所有短文本既违背已有全量保留约束，也会误删简短但有效的证据。

具体实例：query `5a8b57f25542995d1e6f1371` 问 Scott Derrickson 和 Ed Wood 是否同一国籍。Top-1 为 `wiki-2766149:256`，来源是 Robert H. Waterman Jr.，正文仅 `##son.`，cosine=0.438307；原文共 258 tokens，前 256 tokens 留在另一个块。Top-2/3 也是其它文档的同一尾词。Top-4 是 `, wayne wood,`，Top-5 是 `different nationalities.`。这组上下文没有提供回答所需的两个人物国籍，模型输出 UNKNOWN 符合其提示词。

重编码能复现该尾块高分，说明这是现有表示与语料竞争产生的真实检索结果。短尾与低质量检索的关联已经明确；修复能提升多少 ACC 仍须配对消融，不能把富集倍数直接解释为因果贡献。

### 2.2 Encoder 与索引：有协议差异，没有发现本轮系统性损坏

当前 [encoder](../src/common/indexing.py#L43) 保留原始 token ID 窗口，再加 CLS/SEP；不是先 decode 再重新 tokenize 后编码。保存给生成器的文本来自 `tokenizer.decode`，会改变大小写、空格，切在子词中间还会出现 `##`。这损害文本可读性与上下文连续性，但不等于向量与其原始窗口错位。

已有 [index audit](../results/full_clean_top5_20260927/diagnostics/index_audit.json) 覆盖 18 个分散文档向量、2 个定向短尾及 6 个 query 向量，复核了原文 token slice、节点映射、向量与分数。已有 [Top-100 probe](../results/full_clean_top5_20260927/diagnostics/retrieval_probe.json) 对 H/MS 各 100 题重新执行全库精确检索：200/200 的 Top-5 集合相同，最大分数差约 `2.38e-7`。这足以排除抽查范围内的错位、漏搜分片等解释；本次没有重新逐向量重编码整个库。

特殊 token 不能直接删掉。PoisonedRAG 携带的 Contriever 实现同样对包含 CLS/SEP 的非 padding 位置平均。既有 v2 协议已经修复旧版 query/document 特殊 token 不一致的问题；[历史重校验](chunk_trojan_contriever_protocol_revalidation.md) 显示修复后 NQ/MS 召回明显恢复。本轮使用的就是 v2，不能重复归因为旧 bug。

两正文 token 的窗口有一半位置是 CLS/SEP，特殊位置对极短文本的 pooled direction 影响较大。已有同一次 forward 的诊断中，`##son.` 使用全位置池化得分约 0.43830，只池化正文 hidden states 得分约 0.34554。这个局部诊断说明长度与池化值得消融，**不证明去掉特殊 token 是正确修复**。

当前 cosine 与 PoisonedRAG 默认 raw dot 不同：

\[
s_{\rm cos}(q,d)=\frac{q^\top d}{\|q\|\|d\|},\qquad
s_{\rm dot}(q,d)=\|q\|\|d\|\,s_{\rm cos}(q,d).
\]

对固定 query，raw dot 会引入 document 向量范数的排序影响。InceptionRAG、CEG-RAG 的所查路径也使用归一化向量，因此 cosine 不是普遍意义上的实现错误。其与短尾竞争的交互尚需实验。**当前库只保存归一化向量，不能通过切换 FAISS 参数还原 raw dot**；需要重新编码，或重新计算并保存原始范数。

容量方面，[encoding_protocol.py](../src/common/encoding_protocol.py#L8) 的逻辑 64/128/256/512 档分别容纳 64/128/256/510 个正文 token，再加 2 个特殊 token。当前 256 档没有 512-position 溢出。另发现 [PoC `_chunk_document`](../tests/experiments/documents.py#L22) 仍按传入 size 直接切片，512 档存在与基础设施 510 正文容量不一致的风险；它不在本次 clean 路径上，不是本轮低分原因，后续恢复 PoC 前应统一。

### 2.3 清洗与标题：保留了全文，也保留了无效检索材料

| 数据集 | 当前实现 | 判断及修复方向 |
|---|---|---|
| NQ | [datasets.py](../src/common/datasets.py#L123) 删除标为 HTML 的 token，再连接其余 token | 导航、编辑提示、参考文献等仍可能保留；原始 HTML 结构与 answer span 的字符映射没有贯通到 chunk。需在保留原文的前提下构造正文视图，并验证答案 span 不丢失。 |
| HotpotQA | [wikipedia.py](../src/common/wikipedia.py#L34) 去 HTML tag、unescape、连接全文段落 | 文本主要内容存在，但丢失句子与原始段落坐标；15 条支持事实仅因残留 markup 的清洗口径不同，首次定位失败。可以统一映射，无须下载新语料。 |
| MS MARCO | [datasets.py](../src/common/datasets.py#L197) 直接使用官方 doc TSV 的 title/text | 这不是完整保留 HTML tag 的原网页，却仍含网站模板、FAQ 列表和其它 boilerplate；例如一个页面连续列举多个支付问题，容易凭关键词被召回但不回答当前问题。不能将全库低分全部归因于 HTML。 |

标题只加一次尤其影响中后段：一个独立召回块可能只剩代词、年份或列表，无法识别主语。改为每个检索单元携带标题需要重新计入 token 预算；仅在生成 prompt 里补标题与重新编码带标题是两个不同消融。

保留 `raw_text`、正文视图、字符/token offset、source ID 与清洗版本，可以同时支持检索改进和 ChunkTrojan 的单源文档追踪。正文清洗是否提高召回，目前没有直接因果实验；不应进行不可逆的全库删行或删除短文档。

### 2.4 召回深度和多跳：exact Top-5 正确执行，但证据预算不足

[full_clean.py](../tests/experiments/full_clean.py#L92) 每个分片取 Top-5，再按得分合并。一个严格高于全局第 5 名的向量必定位于本分片前 5，因此该流程能得到 exact 全局 Top-5；等分边界按既定 tie order 处理。低召回不能简单解释成“只搜了部分分片”或 ANN 近似误差。

已有各 100 个等间隔 query 的 probe 显示：

| 数据集 | 任一 gold Hit@5 / @20 / @100 | 全部 gold @5 / @20 / @100 |
|---|---|---|
| HotpotQA | 35% / 57% / 73% | **2% / 11% / 20%** |
| MS MARCO | 25% / 45% / 71% | 25% / 45% / 71% |

这是固定诊断样本，不是全量结果或随机抽样置信区间。增大候选深度有空间，但单纯取 Top-100 再用同一分数选前 5，结果不会改善。需要明确增加的机制，如重复文本去重、同源证据合并、尾部重构、词法融合或多跳检索；它们应分别消融。

source 去重也不够：同一 probe 中，把 Top-100 按 source 去重再取 5，H 的 Hit@5 仍为 35%，MS 只从 25% 到 28%。而 `##son.` 可以来自不同 source，source 去重无法消除这种重复。反过来，强制每个 source 最多一个 chunk 会消灭研究对象中的 same-source A/B 共召回，因此不宜设为 ChunkTrojan 的默认 victim 配置。

Hotpot 的 bridge 问题还可能需要先找到一跳实体，再检索第二篇。单轮 query embedding + 五个独立块没有保证两跳完整性的机制。应先修复短尾与标签，再判断单轮 dense retrieval 的剩余能力边界。

## 3. 与本地 baseline 实现的对照

本节核对与检索、输入语料和判分直接相关的代码路径；不把目录中的每个项目都视为同一实验协议。无可调用的 codebase-memory 图工具，本轮结构检索按源码回退核验。

### 3.1 攻击 baseline

| 项目及源码 | 实际实现 | 对当前诊断的意义 |
|---|---|---|
| PoisonedRAG：[main.py:35](../baselines/attacks/PoisonedRAG/main.py#L35)、[beir_utils.py:24](../baselines/attacks/PoisonedRAG/src/contriever_src/beir_utils.py#L24)、[contriever.py:46](../baselines/attacks/PoisonedRAG/src/contriever_src/contriever.py#L46) | 默认 `dot`；`norm_query=False, norm_doc=False`；masked mean 含特殊 token；BEIR 每个 corpus unit 拼接 title/text，最长截断到 512 输入 token | 当前 full-document 全覆盖硬切、归一化 cosine 与之不同。差异有真实影响，但不能为了复现它而把全文尾部全部截掉。 |
| InceptionRAG：[build_corpus_cache.py:84](../baselines/attacks/InceptionRAG/scripts/build_corpus_cache.py#L84)、[run_attack.py:176](../baselines/attacks/InceptionRAG/run_attack.py#L176) | 无 padding 单条编码、截断 512、mean 后 L2 normalize；两阶段均使用 Contriever cosine | 支持“cosine 是一种已有选择”。这里的第二阶段不是 cross-encoder reranker，不能误读为额外强检索器。 |

InceptionRAG 的另一个 [build_corpus_index.py:77](../baselines/attacks/InceptionRAG/data/build_corpus_index.py#L77) 在 padding batch 上直接 `.mean(dim=1)`，没有排除 padding hidden states，存在随 batch 长度变化的表示风险。它不能成为当前 encoder 的照搬模板；当前 masked mean 在这一点上更正确。分层抽样规则与该 encoder 实现是不同事项，不需要捆绑采用。

PoisonedRAG 的 [load_beir_datasets](../baselines/attacks/PoisonedRAG/src/utils.py#L55) 还将 MS MARCO split 固定为 `train`。其 BEIR corpus unit 与当前 document-dev 全文集合不是同一输入，不能仅因名称都叫 MS MARCO 就直接比较 ACC。

### 3.2 防御 baseline

| 项目及源码 | 实际实现 | 不能直接比较的原因 |
|---|---|---|
| Secon-Rag：[main.py:249](../baselines/defenses/Secon-Rag/main.py#L249) | 使用 BEIR 检索路径；`use_truth=True` 分支直接把 gold text 作为 context | 比较其 clean 数值必须区分真实召回与 oracle context。 |
| RobustRAG：[dataset_utils.py:14](../baselines/defenses/RobustRAG/src/dataset_utils.py#L14) | 消费已准备好的 `context[:top_k]`；默认附标题、加入 expanded answers；`eval_response` 按答案是否包含于整段响应判对 | 不构成当前全文索引正确性的证明；其包含式判分比当前 Final-answer EM 宽。 |
| CEG-RAG：[DefenseMechanism:45](<../baselines/defenses/CEG-RAG/code/DefenseMechanism by Utilizing MIL Model#L45>)、[同文件:458](<../baselines/defenses/CEG-RAG/code/DefenseMechanism by Utilizing MIL Model#L458>) | 归一化 Contriever 检索 Top-50，再用 `bge-reranker-large` 和 MIL；所查代码 `NEED_CTX=2`，另有语义 QA judge | README 的 top-3 描述与当前代码不完全一致；其受控知识库、候选深度、reranker、judge 均不同，不能把其结果当作无 reranker 的全wiki Top-5 预期。 |
| GMTP：[get_avg_mask_probs.py:19](../baselines/defenses/GMTP/get_avg_mask_probs.py#L19) | 名称为 contriever 的分支加载 `facebook/contriever-msmarco` | 使用了监督微调 checkpoint，不能与当前无监督 Contriever 混为一谈。 |
| 当前 TrustRAG：[README](../baselines/defenses/TrustRAG/README.md)、[chunk.py:135](../baselines/defenses/TrustRAG/trustrag/modules/document/chunk.py#L135) | `.gitmodules` 指向 `gomate-community/TrustRAG`，是通用 RAG 框架；chunker 按句子组织，超长句另切 | 可参考其保留句子边界的工程思路；不能把目录名称当作已核实的同名安全论文实现。 |

CEG-RAG README 还说明以 4,000 queries 及相关语料构造知识库、以攻击成功数据训练检测器。该任务范围和选择过程不同于当前完整 eval/dev。**“与主流对齐”应拆成 checkpoint、corpus unit、编码、召回深度、上下文和评分六项协议，不存在一个可以整套照搬的统一实现。**

### 3.3 评测口径确实拉低了部分 ACC

当前 [full_clean_eval.py:54](../tests/experiments/full_clean_eval.py#L54) 对解析出的 Final answer 做 normalized exact match。它保留了一个严格且可复算的指标，但不是全部数据集共同的官方语义正确率。

例如 MS query `54544`：gold 为 `Hepatitis B, Hepatitis C and HIV.`，输出为 `hiv, hepatitis b and hepatitis c`。已有日志中 F1=1、EM=0，且 gold source 命中。NQ query `-5347529046899875616` 的 gold 为 `85 (SD) 585 (HD)`，输出为 `585 (hd) 85 (sd)`，同样 F1=1、EM=0。这些实例证明存在排序/表达误判，不代表所有低 F1 输出都应改判正确。

MS 官方本地 [ms_marco_eval.py:104](../data/dataset_code/MSMARCO-Question-Answering/Evaluation/ms_marco_eval.py#L104) 计算 BLEU 与 ROUGE-L；document ranking 则是另一套检索评测。建议保留旧 EM/F1，同时补数据集适配指标与盲审语义正确率，不能删除旧数值后只报告更高的 judge 分数。

命中 gold source 后，有答案题的 ACC 仍仅为 NQ 33.19%、H 22.09%、MS 5.34%；因此提高 source hit 本身不足以完成修复。应同时核对答案/支持句是否位于该 chunk、上下文能否作答，以及最终答案的评分规则。

## 4. HotpotQA 的 gold 稀疏问题：可恢复部分与真实检索缺口

### 4.1 本次新增的全量离线核验

按 query ID 核对 fullwiki/distractor validation 的 question、answer、supporting facts，7,405 题全部一致。全量扫描 canonical corpus，13,783 个独立 gold 文档全部找到。随后将官方支持句对齐到 `title + text` 的 Contriever token 区间，再与已有 Top-5 区间比较。

| 检查 | 结果 |
|---|---:|
| 官方支持事实总数，按 query 计 | 18,005 |
| fullwiki 自带 context 能取出的支持句 | 10,298；全部句子齐全的 query 仅 2,088 |
| 同 query 的 distractor context 能取出的支持句 | **18,004；完整 query 7,404** |
| 直接 token 匹配到 canonical 全文 | 17,988 |
| 使用与 canonical 相同的去 tag/unescape 后额外匹配 | 15 |
| 最终可定位的支持事实 / 完整可定位 query | **18,003 / 7,403** |
| Top-5 覆盖至少一条完整支持句 | 1,890 题 |
| Top-5 覆盖全部支持句 | **80 题** |

原始 fullwiki 文件中的 context 本来就是官方 IR 取出的段落，并不保证 gold 在内；本地 [Hotpot README:31](../data/dataset_code/hotpot/README.md#L31) 明确说明这一点。使用同一 validation 的 distractor 文件恢复**评测标签**，不会改变自然检索输入，更不需要改用 train/test 或把 gold 强行注入上下文。

剩余两条应单列人工审查：`5ae61bfd5542992663a4f261` 的 Jimmy Butler 支持句索引为 902，在两份 context 中均无法取到；`5abaee665542992ccd8e7e5f` 的 Benedict of Nursia 支持句含破损 HTML，统一清洗后仍未精确定位。不能自动猜测句子编号，也不能把“未定位”直接算为检索失败。

### 4.2 文档命中显著高估了实际证据齐全程度

两篇 gold source 都在 Top-5 的共有 195 题，其中只有 **80/195=41.03%** 完整覆盖官方支持句。其余 115 题虽然命中文档，召回位置没有覆盖全部支持事实。

全部支持句覆盖率为 **80/7,403=1.08%**（仅完整可对齐题作分母）；相对于全部 7,405 题，已确认覆盖的下界也约为 1.08%。80 题中 53 题回答正确，**ACC=66.25%**，UNKNOWN 仅 2 题；195 题 source 齐全组的 ACC 为 44.10%。这组差异是观测关联，说明证据粒度值得优先修复，不是恢复标签就能把全量 ACC 自动变成 66.25%。

本次定位是完整支持句的 token 覆盖，可能比回答所需的最小短语更严格；query 的替代有效证据也可能在其它文档。因此它应与 source hit、答案证据与 QA 指标并列。两个未对齐 query 保持 unknown alignment 状态，旧 EM 分母不变。

### 4.3 “稀疏”应区分三件事

1. **缺少 canonical gold 文档：**本轮未发现，13,783 篇全部存在。
2. **文档级 qrels 没有细化到 chunk：**可用现有官方支持句与 token/字符坐标补齐；本轮已证明 7,403 题可完整定位。`sent_id` 是官方 context 段落内编号，不能直接当作全文句子编号。
3. **全库可替代证据没有穷尽标注：**确实不能由两篇 gold 覆盖全部。需候选池标注或人审，并记录新增正例来源；不能仅凭答案词出现、模型自称能答，或某检索器恰好召回来扩充 gold。

MS 每题恰好一个 positive 的稀疏性更明显。现有日志里出现同一有效内容位于另一文档的实例，非 gold 不等于无关。补标签能改进测量，只有改善召回到的证据才会提升真实 QA。

## 5. 待批准的修复顺序与验收

推荐先批准 **P0 + P1**。本次只生成报告及离线审计附件，尚未执行以下修复。

### P0：先建立可诊断的标签与指标，不重建向量库

1. 将支持句到 canonical source/chunk 的映射纳入评测元数据；保留官方 qrels，另建 sentence/chunk support 标签及映射状态。两个 Hotpot 异常保留原记录、单列审计。
2. 增加 SourceHit、AllSupportSource、SupportSentenceRecall、AllSupportCovered、有效上下文 tokens、人工尾块占比、重复正文率；QA 同时报旧 EM/F1、MS 适配指标及少量盲审，分清证据缺失与答案表达差异。
3. 固定 query、model、prompt、Top-5 与语料版本，保留旧结果。全量 clean 不按 `>512 tokens` 或 clean 成功与否删题；后续 PoC 才单列 `gold 文档 >512 tokens + clean 可答` 的合格子集。

预计工程与核验约 **1–2 小时**，无需新的 embedding/API 生成。验收要求：完整复算旧 EM、保持 query 分母、所有新增正例可追溯，且支持句索引错误不会被静默改写。

### P1：先隔离人工短尾的影响，保持现有 victim 其它配置

| 条件 | 唯一主要变化 | 是否重编码 |
|---|---|---|
| S0 | 当前 256、overlap=0、cosine、全库 Top-5 | 复用旧库及结果 |
| S1 | 当人工末尾不足 32 tokens 时，重平衡同文档最后两个窗口；所有内容保留，窗口均不超容量；优先词/句边界 | 仅重编码边界改变的窗口 |

32 tokens 是待验证的工程阈值，不是“短文本都无效”的判断。原生全文短于阈值的文档仍正常编码与检索；标题、checkpoint、pooling、prompt、最终 Top-5 不同时修改。若尾部需要句子跨界，保留明确跨度，不能让 chunker 产生隐藏截断。

按现有 corpus 统计，H/MS 分别有 354,310 / 49,051 个 `<32` 人工尾块。固定窗口下每篇至多一个尾块，主要重编码量约为其两倍，无须先重建四个尺寸全库。实现可采用不可变旧库加替换节点 overlay：旧边界的两个节点必须从检索候选中排除，新节点加入；每个分片应取得足够的未屏蔽候选，以保证合并后仍是完整语料的 exact Top-5。不能只往旧库追加新窗口，也不能仅重排旧 Top-100 就宣称完成全库对照。

先锁定每数据集 100 题的分层验证名单，覆盖答案类型，Hotpot 另覆盖 bridge/comparison；名单不按攻击成功或 clean 成功筛选。S0/S1 使用相同题、完整 canonical corpus、同一生成配置。对固定子集的改善只报子集结论，决定推广前另做独立验收，避免用同一批题反复选阈值再报收益。

验收同时检查内容守恒、短尾减少、真正支持句召回和配对 clean ACC；不能只看 gold source hit 上升。若 S1 未提升证据召回，停止继续微调该阈值，进入下一组原因的受控验证。预计实现与测试约 **2–4 小时**；编码和全库 exact search 的 ETA 需用当时双机吞吐与本地磁盘速度实测，不在本报告虚报完成时刻。

### P2：根据 P1 结果，再分别审批其它协议变化

| 候选修复 | 要回答的问题 | 重建范围与注意事项 |
|---|---|---|
| 句子/词边界、每块标题、原文 span 展示 | 是否减少语义被切断、缺主语和 decode 损失 | 编码内容/边界改变需重编码；仅生成侧补标题不必重编码，但要单独报告 prompt 改动。 |
| raw dot vs cosine | 短尾竞争是否受到归一化放大 | 保持文本和 checkpoint；需获取全部待比较文档的未归一化表示。旧 cosine Top-100 不能代表 raw-dot 全局候选。 |
| Contriever vs Contriever-MSMARCO | 监督检索训练能补多少能力差距 | query/doc 同时换 checkpoint 并重编码；披露训练与评测集合关系，避免把模型变化写成索引修复。 |
| 更深候选、词法融合、两跳召回 | 相关文档排名低或 bridge 第二跳缺失能否缓解 | 仍报告最终五块；扩大候选但不改变选择规则不会改变 Top-5。逐项对照，reranker 不属于本次默认批准范围。 |
| 正文清洗与等价证据标签 | 模板噪声、重复页面、非穷尽 qrels 的影响 | 保留原文和 offset；标签扩充需独立审计，清洗改编码内容时重编码。 |

小型候选池可先用来检查排序机制与编码正确性，但不能用它的召回提升替代完整 corpus 的验收。与 BEIR baseline 的严格复现可单列一条协议；ChunkTrojan 的主线仍保留原始 source document、victim chunking 与 same-source 多块威胁模型，不用截断到单 passage 的基准替代。

### 对后续 ChunkTrojan 研究的判断

现有数据足以支持**有 clean 证据门槛的手工机制探索**，但 Hotpot 当前仅约 1% 的 query 完整召回官方支持句，MS 的 qrels/QA 指标又有明显口径差异，不适合作为无需筛查即可直接进行大规模攻防比较的稳定 victim baseline。既有成功 PoC 的证据应保留；全量 clean 的低分不能据此否定跨 chunk composition，也不能把 UNKNOWN 变为错误答案直接当作可靠攻击收益。

P0/P1 的目标是先建立能正确回答、证据可追踪的 victim 配置。随后恢复手工 PoC，继续分别报告 clean QA validity、same-source cross-chunk validity、自然 CoRecall@5 和 A/B/AB/BA 的非加和效果；筛选后的攻击结果明确属于条件样本，不外推为整个 eval/dev 的成功率。

## 审计材料与复现边界

本次新增结果位于 [clean_pipeline_audit_20261003](../results/clean_pipeline_audit_20261003/README.md)：`log_reanalysis.json` 为三集合全量 Top-5 离线重算，`hotpot_support_alignment.json` 为支持句核验汇总，`hotpot_support_alignment.jsonl` 保存逐题 source、原句、token 区间及覆盖情况；`audit_checks.json` 记录计数一致性检查与输入/产物 SHA256。没有发起新的 LLM 请求或 GPU 检索，没有改动旧结果或 canonical corpus/index。

旧结果依据 [results_overview.json](../results/full_clean_top5_20260927/results_overview.json)、[annotation_audit.json](../results/full_clean_top5_20260927/diagnostics/annotation_audit.json)、[index_audit.json](../results/full_clean_top5_20260927/diagnostics/index_audit.json) 和 [retrieval_probe.json](../results/full_clean_top5_20260927/diagnostics/retrieval_probe.json)。本报告没有混入此前错误 special-token 协议的低召回结果。

源码审查基于主仓库 `c2e520d34211a1c56fde6a965b66e72688eb60bf`。子模块版本：PoisonedRAG `f660d721`、InceptionRAG `f2ab9b25`、Secon-Rag `0bfeeca3`、RobustRAG `9bc35b2f`、CEG-RAG `9ce03688`、GMTP `15b48d15`、TrustRAG `a2bf14a6`。PoisonedRAG 的 `prepare_dataset.py` 已有本地修改，本轮未修改它；本文引用的 encoder/default-score 路径不在该差异文件中。

旧 README 中 `src/main.py full-clean` 命令及 `ragshield` 绝对路径反映历史目录布局；当前统一入口为 `python src/main.py poc full-clean`。这属于复现说明待修订项，不是历史检索低分的证据。报告中的索引一致性结论以列明的审计范围为限；新诊断与修复收益没有混写。

# 全量 Clean Top-5 检索与问答实验

状态：全部完成。

## 实验范围与协议

全部原始 validation/dev 问题，无 query 抽样、长度过滤或 clean 成功筛选。检索使用现有 Contriever FP16 CLS/SEP v2 向量库、256 content tokens、overlap=0，遍历全部分片以单位向量内积实现 cosine，精确检索 Top-5，不做来源去重或 reranking。

dancher-01 的 qwen3.8-27b；temperature=0、top_p=1、seed=0、max_tokens={'nq': 1000, 'hotpotqa': 1000, 'msmarco': 1000}、enable_thinking=false。只对传输错误重试，首次成功返回（含截断）固定为结果；未使用格式提醒。

System prompt：`Answer based on context. Output: ‘Final answer: <answer>’. If the excerpts do not determine the answer, output ‘Final answer: UNKNOWN’.`

User prompt：`CONTEXT: {context}\nQUESTION: {question}`；context按排名用两个换行连接5个chunk正文。

|数据集|完整query|QA gold|corpus文档|256向量|状态|
|---|---:|---:|---:|---:|---|
|nq|7830|4462|7378|235618|complete|
|hotpotqa|7405|7405|5486212|13400704|complete|
|msmarco|5193|5169|401855|4913542|complete|

## Clean QA 与检索诊断

|数据集|全文正确/QA gold|Clean ACC|严格 EM 正确数（严格 EM）|Token F1|qrel Hit@5|qrel Recall@5|MRR@5|全部qrel命中|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|nq|1955/4462|43.81%|1356（30.39%）|44.52%|87.05%|87.05%|74.30%|87.05%|
|hotpotqa|1161/7405|15.68%|922（12.45%）|16.61%|42.30%|23.27%|29.36%|4.25%|
|msmarco|292/5169|5.65%|159（3.08%）|17.68%|27.25%|27.25%|16.43%|27.25%|

|数据集|UNKNOWN|无Final answer|输出token上限截断|未完成/传输失败|source 命中条件严格 EM|重复来源比例|
|---|---:|---:|---:|---:|---:|---:|
|nq|3149|208|210|0|33.11%|45.43%|
|hotpotqa|5332|168|169|0|24.07%|3.20%|
|msmarco|1859|34|34|0|4.91%|11.11%|

本轮主ACC检查完整响应中的规范化gold词组；旧Final-answer严格EM并列报告。该指标不是语义判分，也不是各数据集官方leaderboard指标。分母固定为具有QA gold的全部问题，UNKNOWN/无Final answer/截断不剔除；缺少gold单列。Token F1用于观察答案表述差异。截断与无Final answer可能重叠，不可相加。qrel Recall为逐query已命中positive文档比例的平均；HotpotQA全部support命中更适合多跳诊断，MS-MARCO多个相关文档不代表必须全部召回才能作答。

## 数据质量与研究适用性

NQ原始7830题中3368题缺少当前可用short/yes-no gold；这不等于corpus中无答案，不能用UNKNOWN给这些题判对，也不能把它们当作攻击失败。NQ多标注者/多span答案采用现有alias口径，不是官方NQ评分器。

HotpotQA使用7405条带答案validation问题，在完整wiki索引中检索。多跳问题的单个support命中不能证明上下文已支持答案。

MS-MARCO检索库范围是dev top100文档并集加positive qrels，不是整个约320万文档库。QA答案通过官方Microsoft QA validation的query ID及问题文本精确关联；24题未匹配QA gold。相关性标注和QA答案来自不同标注任务，长句参考答案也会使严格EM低于语义正确率。

nq有2题gold含UNKNOWN/N/A等歧义值，保持原标注、未静默重标：
- `5209763379196124426`：who's opening for foo fighters at fenway；gold=['N/A']。
- `-4663296615598634791`：who was allowed to vote in the roman republic；gold=['citizens', 'unknown']。
UNKNOWN按本轮拒答标记处理，即使出现在参考alias中也不算正确；这些题需独立标注复核。
- **nq**：未在索引中找到的已映射positive source为0个；qrel Hit@5=87.05%；答案词面出现代理=56.39%；截断210题；clean EM正确且至少召回一个positive source的候选为1286题。
- **hotpotqa**：未在索引中找到的已映射positive source为0个；qrel Hit@5=42.30%；答案词面出现代理=22.76%；截断169题；clean EM正确且至少召回一个positive source的候选为754题。
- **msmarco**：未在索引中找到的已映射positive source为0个；qrel Hit@5=27.25%；答案词面出现代理=9.25%；截断34题；clean EM正确且至少召回一个positive source的候选为69题。

本轮基线可用于区分语料/标注覆盖、检索遗漏和生成协议失败。低Clean ACC本身不能否定ChunkTrojan机制；截断或格式失败属于当前问答协议的限制，相关文档未召回属于检索限制，不能直接归因于数据损坏。后续手工PoC应从clean可回答且证据支持的候选中复核选择，并继续要求gold载体>512 tokens。上述候选计数尚未施加载体长度或证据蕴含复核，不能直接当作可攻击样本数。Clean实验本身不提供组合效应或自然A/B共同召回证据。

## 逐题记录与复现

各数据集子目录：`queries.jsonl`保存原始query与gold；`retrieval.jsonl`保存每题5个chunk的document_id/chunk_id、rank、retriever score、token边界与正文；`generation_attempts.jsonl`保存请求prompt、输出、模型、finish_reason和usage；`query_results.jsonl`保存逐题诊断；`protocol.json`、`generation_protocol.json`固定配置。

运行/恢复命令见根目录 `README.md`；`run_generation.sh`按NQ、MS-MARCO、HotpotQA顺序生成并自动汇总。

## P0/P1 修复诊断

保持cosine；人工尾部1–31 tokens与前块重平衡，内容无损且每块≤256正文tokens。原生短文档保留；检索在内存中移除两个旧窗口，加入两个新窗口，仍遍历全库exact Top-5。

|数据集|全文ACC|旧严格EM|上下文tokens均值|去重正文tokens均值|人工短尾比例|重复正文比例|支持句Recall|全部支持句覆盖|MS ROUGE-L|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|nq|43.81%|30.39%|1263.4|1246.7|0.00%|1.44%|—|—|—|
|hotpotqa|15.68%|12.45%|353.7|353.6|0.00%|0.15%|18.19%|1.81%|—|
|msmarco|5.65%|3.08%|898.6|863.3|0.00%|3.64%|—|—|16.10%|

支持句覆盖使用同source的召回token区间并集；2个Hotpot问题有无法定位的事实，不进入全部支持句覆盖率分母，QA分母仍保留。支持句Recall为逐题可定位事实覆盖比例的均值。去重正文tokens仅衡量非空、去重复上下文预算，不代表这些tokens都支持答案。主ACC保留显式UNKNOWN判失败规则；原始全文词面命中另存。其它解释中或被否定的gold仍可能命中，不能替代语义审计；MS ROUGE-L采用规范化token LCS、beta=1.2，本地诊断不等于官方leaderboard评分。

## 完成后的对比分析

详见[同口径收益、失败原因及修复建议](post_run_analysis/report.md)。HotpotQA 全文 ACC 提升 3.34 个百分点，NQ 基本持平，MS MARCO 提升 0.27 个百分点；需分别处理证据召回不足与词面评分偏差。

# P0/P1 Clean RAG 完成结果分析与修复建议

更新日期：2026-10-06。范围：NQ validation、HotpotQA fullwiki validation、MS MARCO document dev。第 2–8 节保留 P0/P1 分析；第 9 节新增同 chunk 池 BM25 全量对照，第 10 节记录原始 BEIR 语料上的固定 300 题 baseline 对照。

## 1. 结论

**同 chunk 池的 BM25 对照把 HotpotQA ACC 从 15.68% 提高到 36.52%，证明当前 Contriever 排序是其主要瓶颈之一；仅修复分块仍不足以建立强基线。** HotpotQA 有明确改善，剩余主要瓶颈是多跳证据召回；NQ 基本持平，主要需要提高答案片段覆盖和核验答案评分；MS MARCO 的低分同时受证据召回与长答案词面评分影响。现有记录不支持把索引损坏视为主要原因。

三个集合共 20,428 个 query 已全部完成，API 错误与未解决传输失败均为 0。运行完整不等于答案正确。低 clean ACC 也不构成 ChunkTrojan 核心设想的否定证据：它限制的是后续攻击实验的可解释性和可用样本量。

## 2. 同口径比较：真正提升了多少

S0 是旧运行的原始输出按新指标离线复算，S1 是本轮 P0/P1 修复后重新生成。两者均以完整响应中的规范化 gold 词组匹配作为主 ACC，保留 Final answer 严格 EM。不能拿旧严格 EM 与新全文 ACC 比较后宣称修复收益。

|数据集|query 总数 / QA gold 数|全文 ACC：S0 → S1|差值（百分点）|严格 EM：S0 → S1|任一 gold source Hit@5：S0 → S1|
|---|---:|---:|---:|---:|---:|
|NQ|7,830 / 4,462|43.93% → 43.81%|−0.11|30.32% → 30.39%|86.98% → 87.05%|
|HotpotQA|7,405 / 7,405|12.34% → 15.68%|+3.34|9.86% → 12.45%|31.86% → 42.30%|
|MS MARCO|5,193 / 5,169|5.38% → 5.65%|+0.27|3.10% → 3.08%|24.30% → 27.25%|

本轮全文正确数分别为 1,955、1,161、292；严格 EM 正确数分别为 1,356、922、159。NQ 的 3,368 题和 MS 的 24 题没有当前可用 QA gold，不参与 QA 准确率分母，不自动按错误或 UNKNOWN 正确处理。检索指标的标签分母也应单列，不能一律使用全部 query 数。

|配对变化|NQ|HotpotQA|MS MARCO|
|---|---:|---:|---:|
|旧错 → 新对|55|405|45|
|旧对 → 新错|60|158|31|
|净增正确题数|−5|+247|+14|
|有序 Top-5 正文完全相同的 query|7,468|686|1,608|
|其中输出文本发生变化|3,402|272|506|
|相同上下文、有标签样本：旧错 → 新对 / 旧对 → 新错|52 / 55|10 / 5|4 / 4|

S0/S1 保存的生成协议只有 retrieval 文件哈希不同；模型、prompt、max_tokens=1000、temperature=0、top_p=1、seed=0 等一致。但固定参数不保证跨运行输出逐字一致，日志不足以确定漂移来自服务后端、批处理数值还是其它运行因素。NQ 的微小 ACC 变化主要发生在检索上下文未变的样本，不能解释为分块策略导致退化。Hotpot 的证据覆盖和检索命中改善是直接可见的；生成收益仍是单次重跑结果，不应当成完全隔离生成波动的因果估计。

## 3. HotpotQA：修复人工短尾后，仍缺少第二跳和足够的证据正文

|证据指标|S0|S1|
|---|---:|---:|
|全部 gold source 命中|2.63%|4.25%（315/7,405）|
|支持句 Recall（逐题宏平均）|13.45%|18.19%|
|全部标注支持句覆盖|1.08%|1.81%（134/7,403）|
|Top-5 正文 tokens 均值|202.49|353.74|
|UNKNOWN 数|5,658|5,332|

18,005 条支持事实中已有 18,003 条定位到语料，7,403 题的全部事实可定位。**此次低分不能主要归因于官方支持事实无法映射。** 官方支持事实仍非所有有效替代证据的穷尽标注，所以全部支持句覆盖率是诊断指标，不是可回答率的绝对上限。补标签改善测量，不能自动改善检索。

本轮 37,025 个召回位置中，10,585 个块不足 32 tokens，占 28.59%；这些块全部从 source 的 token 0 开始，人工短尾计数为 0。低于 256 tokens 的块占 89.32%。平均每块仅 70.75 tokens，五块总计 353.74 tokens，仅相当于 5×256 正文容量的 27.64%。容量使用不足本身不证明错误，但结合证据低覆盖表明仅控制 chunk 数不能保证足够信息。

频繁出现的短块包括 `who ' s no. 1?`（132 个召回位置）、`how ethical is australia?`（69）、`list of places in new york : i`（48）、`=? =? may refer to :`（48）。这是标题式条目、列表或消歧入口占据排名的直接证据；不能据此把所有短文档都判为无用，也不能断言这些短源一定由清洗错误造成。需回查原始 wiki 对象，区分原本简短的正文、抽取丢失和源格式异常。

最有区分力的条件统计是：

|本轮证据条件|题数|全文 ACC|严格 EM|UNKNOWN|
|---|---:|---:|---:|---:|
|至少一个 gold source 命中|3,132|30.84%|24.07%|1,513|
|全部 gold source 命中|315|62.22%|48.25%|48|
|全部标注支持句覆盖|134|82.84%（111/134）|66.42%|3|
|支持句未全部覆盖，且事实可定位|7,269|14.44%|11.46%|5,327|

这些是自然检索后不同难度样本的条件统计，不能把 82.84% 外推成全量 oracle ACC。不过，它强烈支持优先修复证据获取，而不是先更换生成模型。例：`5adbf0a255429947ff17385a` 问两处建筑是否在同一街区，召回里有 Laleli Mosque 信息却没有 Esma Sultan Mansion 位置，模型明确据此输出 UNKNOWN。source 命中不等于两跳证据齐全。

## 4. NQ 与 MS MARCO：source 命中、答案支持、语义正确是三个层次

### NQ

NQ 任一 gold source Hit@5 已达 87.05%，但排除 yes/no 后，答案词面在上下文出现的比例只有 56.39%（分母 4,288）。同一长 wiki 文档中的目录、导航、列表及相关但不含答案的段落也会被记为 source 命中。样本正文里确实出现了这类内容，但本轮未全量测量其占比，不能将全部失败归因于清洗。

命中 gold source 的 3,884 题全文 ACC 为 47.73%；上下文有 gold 词面的 2,418 题全文 ACC 为 71.01%。后一指标同样不是语义支持判定。原生短文本在这里不是首要问题：Top-5 平均已有 1,263.38 tokens，未出现不足 32 tokens 的召回块。

评分也有可确认的假阴性案例：`8678345068092193884` 的 gold 是 `Jean-Paul Valley (a.k.a. Azrael)`，模型答 `Jean-Paul Valley`，全文完整词组未命中；`-3632974700795137148` 回答 `dai yongge and dai xiuli`，gold 的连接词/括号限定写法不同，同样失败。应规范别名、可选限定语与多 span 结构，不能简单把任意答案子串都当正确。

### MS MARCO

任一 positive source Hit@5 从 24.30% 提升到 27.25%，但命中的 1,405 题全文 ACC 仍只有 10.75%，严格 EM 4.91%。原因不能只用“未召回文档”解释：还需要核验命中的具体块是否支持答案，以及 QA 答案与文档排名标签是否语义一致。

MS 的最短 gold 词数中位数为 12（NQ 和 Hotpot 均为 2），完整参考答案串在上下文的出现率仅 9.25%。这不是“只有 9.25% 有正确证据”的证明：长答案通常可以释义，词组匹配会漏掉正确表达。

具体例子：

|query ID|参考答案 / 实际输出|诊断|
|---|---|---|
|54544|`Hepatitis B, Hepatitis C and HIV.` / `hiv, hepatitis b and hepatitis c`|枚举顺序不同，Token F1=1，全文 ACC 却失败|
|1090270|带 `The definition of botulinum is ...` 的定义 / 同一定义正文另加括号内菌名|模板前缀和表述差异，F1=0.8667|
|1090110|`Tax planning is the exercise minimizing liability using all deductions available.` / `exercise minimizing liability using all deductions available`|省略主语模板，F1=0.8235|

MS 有 64 个全文 ACC 失败样本的 F1≥0.8，342 个≥0.5；这只是待审计集合，不是可直接补算的正确数。高 F1 也可能把关键实体答错：NQ 的 Third/Fourth Five-Year Plan 案例就有 F1=0.6667，但目标年代实质错误。本轮 ROUGE-L 从 14.97% 提升到 16.10%，F1 从 16.38% 提升到 17.68%，支持表达质量有小幅改善，但不能证明语义准确率已经很高。

MS 单一 positive qrel 不穷尽所有相关文档；QA gold 来自另一标注任务的精确 query 关联。缺标签会低估 source 指标，长答案会低估词面指标，但两者都不能免除检索内容审计。语料范围为 dev top100 文档并集加 positive qrels（401,855 文档），不是完整约 320 万文档集；NQ 也只检索当前 validation 源文档库，三集合难度与主流公开 leaderboard 并不直接可比。

## 5. 哪些故障已排查，哪些仍需验证

P0/P1 主线运行协议是 Contriever、FP16、256 正文 tokens、cosine、全库精确 Top-5、无 reranker。底层单位向量内积实现 cosine，不是本轮改用了未归一化 dot。P1 只把人工 1–31-token 尾块与前块重平衡，保留全部原文及原生短文档。

已有 checkpoint 文件校验、替换向量回传 SHA 校验、分片完整搜索和旧窗口排除检查；三集合 808,520 个替换向量已校验。检索覆盖 NQ/MS/Hotpot 的 15/303/649 个 base shards；已映射 positive source 缺失数均为 0，人工短尾召回均为 0。相关记录见父目录 `checkpoint_verification.json`、`retrieval_integrity_checks.json`、`implementation_report.md`。这些检查反对“回传缺失或部分分片未搜索是主因”的解释，但不能证明每个向量与正文的语义对应都绝对正确；若还需进一步排除，可抽样重新编码验证向量和排名。

|因素|本轮判断|下一步区分方法|
|---|---|---|
|人工短尾占据 Top-5|已修复，Hotpot 收益明显|保留当前 S1 作为对照|
|原生短源、导航/列表噪声|有直接案例；全量成因未定|回查原始正文及抽取路径，核验源本来就短还是清洗丢失|
|多跳证据召回不足|Hotpot 的主要实证瓶颈|诊断更深候选池与桥接证据位置|
|评分假阴性、qrel 稀疏|确认存在；总体影响未定|盲审失败样本和 source miss 样本，单独扩充评估标签|
|生成与格式问题|存在，但不是唯一瓶颈|小样本固定 oracle 证据对照，区分证据不足与生成失败|

全部 query 的截断数 NQ/Hotpot/MS 为 210/169/34，占 2.68%/2.28%/0.65%；其中有 QA gold 的截断为 105/169/33。即便只把这些有标签截断全部修成正确，全文 ACC 最多增加约 2.35/2.28/0.64 个百分点，无法单独填补当前差距。UNKNOWN 也不能统一解释为模型故障：当前 prompt 要求缺乏证据时拒答。

全文 ACC 还可能假阳性：解释段落提到了 gold、最后却否定或答了别的内容，词面仍可命中。显式 UNKNOWN 和截断失败规则减少一部分风险，但不能替代语义审计，尤其是 yes/no。

## 6. 修复顺序与验收标准

1. **先分离评分与证据问题。** 保留现有全文 ACC、严格 EM、F1/ROUGE-L，在固定小型开发集上盲审正确性与上下文支持性；MS 优先检查释义/枚举，NQ 检查别名和多 span。输出假阴性/假阳性及标签不完备比例。不要用 F1 阈值直接替代正确性，也不要把补充 qrel 注入自然生成上下文。
2. **做独立的 gold/support-context 对照。** 同一 query、同一模型和 prompt，比自然 Top-5 与人工核验的充分证据，分别记录语义正确、词面指标、UNKNOWN、截断。该条件只诊断生成和评分，不混入 natural ACC。它能判断下一步应优先改检索还是 prompt。
3. **修复检索呈现与语料结构。** 保持 cosine 和原始内容完整入库；按抽取审计结果处理导航模板，在独立检索视图里比较标题加完整句、邻接窗口或 parent-child 正文扩展。原生短文不应直接按长度删掉；同源 chunk 也不应硬去重，否则破坏 same-source A/B 研究对象。改变视图后重新验证 token 边界、答案覆盖及向量对应关系，并固定上下文预算。
4. **针对 Hotpot 补足多跳候选。** 先看 Top-20/100 是否已有缺失支持句，再决定桥接检索或覆盖感知选取；单纯扩大候选后按原相似度再取 Top-5，不会改变最终结果。对最终五个块及总 tokens 分别约束，记录任一 source、全部 source、全部支持句覆盖和 clean QA，避免靠扩大预算冒充算法收益。MS 则优先定位 positive 文档内答案所在段落及正文噪声。
5. **再做模型或生成协议消融。** 若充分证据下仍低分，再测试先输出 Final answer 或结构化短答案；监督检索 checkpoint、混合检索、reranker 是后续独立对照，不归入本轮 P0/P1 收益。当前 cosine 不变。固定开发集和独立确认集，避免反复在全 validation/dev 上调参后把其结果当无偏泛化指标。

原建议之后已完成同 chunk 池 BM25 全量对照（第 9 节），并开始固定小样本的上游原语料对照（第 10 节）。充分证据对照与语义盲审仍用于进一步区分生成、评分和召回瓶颈。

## 7. 对后续 ChunkTrojan 研究的含义

可以继续做经核验的手工 PoC，但不能把全部 query 作为攻击成功率分母。已有严格 EM 正确且至少命中一个 positive source 的候选数为 NQ 1,286、Hotpot 754、MS 69；这些计数未检查完整证据、gold 载体 >512 tokens、A/B 独立性或自然共同召回，不能直接称为合格攻击样本。

主实验应先锁定 clean 回答正确且确有证据支持、gold 载体 >512 tokens 的 query。报告筛选率与被排除原因，分别展示自然召回结果和 forced-context 组合机制。修复 clean pipeline 是为了建立可解释的 victim 基线；本轮并未测试或否定 cross-chunk 非加和攻击机制。

## 8. 可审计产物与口径说明

- [离线全量统计](analysis.json)：按 query ID 配对的准确率转换、相同上下文输出变化、证据分组、失败类型及长度桶。
- [定性案例](examples.json)：定向选择的失败样本，含 gold、模型全文、Top-5 正文/分数/排名；不是随机盲审样本。
- [输入哈希](input_hashes.json)：固定本次离线统计输入。
- [本轮主报告](../report.md)与 [S0 同口径复算](../baseline_rescore/report.md)；[此前 pipeline 对齐审计](../../../reports/clean_pipeline_baseline_alignment_audit_20261003.md)。

主报告原来把“严格 EM 正确数”与“全文 Clean ACC”放在同一行而未并列明确分子；本次已明确区分，条件指标也改称“source 命中条件严格 EM”。原启动快照只记录启动验收，不代表目前进度；全部完成状态以本轮结果总表为准。

## 9. BM25 同 chunk 池完整对照：检索器影响与剩余瓶颈

### 9.1 对照成立的范围

本轮使用修复后的全部 256-token chunks、Top-5、原样正文、同一 Qwen3.8-27B 服务与 system/user prompt；temperature=0、top_p=1、seed=0、max_tokens=1000，无 reranker。BM25 为 SQLite FTS5 `porter unicode61`，k1=1.2、b=0.75，query 去英文停用词后 OR 查询；这是此次实测的词法实现，Lucene/Pyserini 的分词与排序不必与其逐位相同。

NQ/HotpotQA/MS MARCO 索引分别为 235,618 / 13,400,704 / 4,913,542 个 chunk，FTS 完整性检查通过；原 Contriever 的 39,150 / 37,025 / 25,965 个召回位置均与 BM25 索引中的正文对齐。两轮生成协议除输入文件哈希外一致。BM25 完成 20,428/20,428 题，未解决 API 错误为 0，输入截断为 0。完整运行见 [BM25 报告](../../full_clean_bm25_chunks_20261005/report.md)。

### 9.2 全量准确率与配对差异

|数据集|QA gold 分母|Contriever 正确 / ACC|BM25 正确 / ACC|差值（百分点）|严格 EM：Contriever → BM25|
|---|---:|---:|---:|---:|---:|
|NQ|4,462|1,955 / 43.81%|1,952 / 43.75%|−0.07|30.39% → 31.13%|
|HotpotQA|7,405|1,161 / 15.68%|2,704 / 36.52%|+20.84|12.45% → 28.93%|
|MS MARCO|5,169|292 / 5.65%|385 / 7.45%|+1.80|3.08% → 3.71%|

|数据集|仅 BM25 正确|仅 Contriever 正确|两者正确|两者失败|配对差值 95% 近似区间（百分点）|McNemar 精确双侧 p|
|---|---:|---:|---:|---:|---:|---:|
|NQ|456|459|1,496|2,051|[−1.40, +1.26]|0.947|
|HotpotQA|1,782|239|922|4,462|[+19.75, +21.93]|2.60×10⁻²⁹¹|
|MS MARCO|176|83|209|4,701|[+1.19, +2.41]|7.57×10⁻⁹|

区间按 query 级配对差值的正态近似计算，p 值对不一致题数做二项精确检验；它们描述这两个固定运行的逐题差异，未覆盖服务重跑波动。HotpotQA 的效果量大，并伴随检索证据改善；NQ 结果相当，但两检索器各有约 450 题独有正确答案，存在互补空间。不能用总 ACC 持平推断两者返回了相同证据。

### 9.3 检索效能：HotpotQA 的短文竞争和多跳覆盖

|指标|Contriever|BM25|
|---|---:|---:|
|HotpotQA 任一 gold source Hit@5|42.30%|81.16%|
|HotpotQA 全部 gold source Hit@5|4.25%|23.55%|
|HotpotQA 全部标注支持句覆盖|1.81%（134/7,403）|18.38%（1,361/7,403）|
|HotpotQA 支持句 Recall，逐题宏平均|18.19%|49.21%|
|HotpotQA Top-5 正文 token 均值|353.74|1,011.62|
|HotpotQA 原生短块 <32 tokens 占召回位置|28.59%|1.48%|
|HotpotQA 人工短尾 <32 tokens|0|0|
|HotpotQA UNKNOWN，全量题数|5,332|3,123|
|NQ gold source Hit@5，有 qrel 题|87.05%|85.03%|
|MS MARCO gold source Hit@5，有 qrel 题|27.25%|35.66%|

**相同 chunk 池可以取得明显更高的证据覆盖。** BM25 没有恢复额外语料、修改边界或补充标签，就把 HotpotQA 的短块占比降到 1.48%，增加两跳来源与支持句覆盖。这直接定位了当前无监督 Contriever + cosine + 全文竞争池组合的排序局限。它不等价于 Contriever 在所有语料或 raw dot 配置下都弱；更换 cosine、checkpoint、语料单位的效果需要独立对照。

BM25 仍有 6,042/7,403 题未覆盖全部支持句。其 ACC 为 27.01%，而全部支持句覆盖的 1,361 题 ACC 为 **78.69%（1,071/1,361）**，UNKNOWN 仅 17 题。当前主要剩余损失仍与证据缺失相关；gold source 命中 81.16% 并不表示 81.16% 的题已有充分答案依据。原文标题只在首块、硬 token 边界、邻接句缺失及单轮 Top-5 的多跳预算都可能造成这个差距。

“全部支持句覆盖”来自官方标注，是可审计的充分证据诊断之一。支持句未全覆盖的正确回答仍有 1,632 题，说明替代证据与模型已有知识也会发挥作用；不能将该覆盖率直接当作最高可达 ACC。

### 9.4 NQ 与 MS MARCO：仅换检索器为何不够

|数据集 / 条件|Contriever 题数 / ACC|BM25 题数 / ACC|
|---|---:|---:|
|NQ，gold source 命中|3,884 / 47.73%|3,794 / 49.29%|
|NQ，上下文含 gold 词组|2,418 / 71.01%|2,343 / 72.77%|
|MS MARCO，gold source 命中|1,405 / 10.75%|1,844 / 11.44%|
|MS MARCO，上下文含 gold 词组|468 / 42.31%|622 / 43.89%|

NQ 两检索器的 gold source 命中都在 85% 以上，答案词组覆盖仍仅约 55%。完整页面中“取到同一来源”比“取到正确段落”容易，下一步应定位 gold answer span 与召回窗口，而不是继续只优化 source Hit@5。上下文出现答案词组时仍有约 27% 未得分，需细分歧义、别名评分、回答格式及生成错误。

MS MARCO 存在双重瓶颈：检索命中改善了，但命中条件 ACC 仍约 11%；参考答案通常较长，且 QA 标注与 document-ranking qrels 是不同任务的标签。BM25 有 **391** 个 ACC 失败样本的 F1≥0.5，其中 **51** 个≥0.8，提示需要逐题核验释义评分；这些数字不是额外正确题数。把召回失败和评分假阴性分开，才能估计真实增益。

BM25 在有 QA gold 的 NQ/HotpotQA/MS 上输出截断分别为 **84 / 430 / 82**。即便把这些题全部修为正确，ACC 上界增量也只有 **1.88 / 5.81 / 1.59** 个百分点。HotpotQA 相比 Contriever 的截断增多，需审计困难证据下是否出现冗长输出；但它不能解释全部低分。当前没有输入截断，扩大输入上下文上限不会直接解决本轮问题。

### 9.5 是否主要因为与 baseline pipeline 未对齐

**与 baseline 不同解释了“为什么不能横比论文 ACC”；本轮直接证据指向的是排序与证据获取，而不是统一的 pipeline 损坏。** 分开看有四层：

|层次|当前 pipeline 与上游的差异|本轮证据与归因|
|---|---|---|
|语料和 split|当前 NQ validation 完整页、Hotpot 全文、MS document-dev；上游常用 BEIR passage、MS dev 或 train 小样本|改变竞争文档、相关证据单位与问题难度；不能用论文数字作为当前 ACC 的验收线|
|检索表示|当前 256-token 硬分块、CLS/SEP mean pooling、FP16 cosine；PoisonedRAG 系通常原 BEIR 文本 + raw dot|Hotpot 同池 BM25 显著改善，定位到表示/打分/语料交互；尚未用 raw dot 消融归因给单一参数|
|上下文和 prompt|当前严格缺证拒答、Final answer 格式；上游有短答案、不强制拒答、带标题等差异|生成与词面评分的拒答率会变；小样本固定上下文、切换原生 prompt 可单独检查|
|标签与评分|完整来源 qrel 与片段支持不同；MS 长答案、NQ 多 span/别名；上游可能压缩答案或 substring|假阴性已有实例，影响绝对 ACC；统一 QA aliases 与评分后才能比较小样本结果|

还有实现本身的差异：SeCon-RAG 发布代码中 GPT-RE 部分是占位，RAGDefender 的论文 Stella、旧研究脚本 paraphrase-MiniLM 与公开 API all-MiniLM 默认值并不相同。复用仓库名称不能替代版本和运行路径核验。

**RAGDefender 还存在决定性的证据可用性差异。** `artifacts/main.py:181–193` 从正 qrels 取 gold，NQ 扩展为同标题段落；`:229–235` 将这些文本直接追加到待防御上下文。`run_poisonedrag.py` 对 Hotpot/MS 设 Top-2，并非本次 Top-5。这种受控 gold-context 实验预先提供正确证据，无法用来证明自然 Top-5 也应有同等 clean ACC。原代码另有 `use_truth=True` 的纯 gold 生成分支，应归为 oracle 诊断。此次小对比以自然缓存召回作为统一输入，并明确标为公开防御代码在 clean Top-5 上的适配实验。

审计锚点：PoisonedRAG `src/contriever_src/beir_utils.py:85–115`（标题拼接、截断及编码），`main.py:118–166`（缓存 Top-K 与正文输入）；CamoDocs `src/prompts.py`（简短回答模板）；SeCon-RAG `main.py:79–125`（过滤与 GPT-RE 占位）、`:315–330`（substring 指标）；RAGDefender `ragdefender/embedders.py:1–20`（模型版本差异）；SecRAG `flashrag/prompt/base_prompt.py:7–12,217–228`（标题格式及回答模板）。

**修复优先级：**先保留 BM25 作为强词法对照，逐题测量答案/支持句所在窗口；在固定开发集上比较标题补充与邻接证据扩展，保持总 token 预算可比；随后分别消融 Contriever checkpoint 和 dot/cosine，避免同时换语料、分块与模型后无法解释提升。MS 优先审计语义正确性与 QA/document 标签关联，NQ 优先审计正确来源内的答案定位。原始全文和全部短文继续保留，检索视图调整单独版本化。

逐题条件统计与配对区间见 [BM25 对比分析](bm25_comparison_analysis.json)，输入 SHA256 见 [输入指纹](bm25_comparison_hashes.json)。

## 10. 原始语料上的固定 300 题 baseline 对照

三个数据集各冻结上游预选的 100 题，五条 clean 路径共用题单。本次不再按 clean 正确率或长度筛选；其结果描述固定 cohort，不外推为完整 eval 的均值。选取 PoisonedRAG（攻击 S）、CamoDocs（攻击 A）、CorruptRAG/SecRAG（攻击 S、第三方实现）、RAGDefender（防御第 8，B）与 SeCon-RAG（防御第 9，B）。更高优先级 RobustRAG 的原始 Google snippets 资产未覆盖这三个共同语料，本轮选择具有共同 BEIR 资产的上述路径。

固定统一 Qwen 服务与 Top-5，读取原始 BEIR corpus 的上游 scored retrieval cache，逐条保留排名、分数和正文。各仓库导入原生 prompt；RAGDefender、SeCon-RAG 加跑发布代码可执行的 clean 防御分支。另设“同原始上下文 + 当前 prompt”条件以区分生成模板的影响。同一 messages 哈希的条件共享一次调用，属于路径一致性验证，不作为独立统计重复。

这组对照是统一 victim 下的原语料 clean 路径复现：CamoDocs 改用共同题单与显式传入的原始语料缓存；CorruptRAG 使用 SecRAG clean 模板；RAGDefender 启用分支使用公开 API 的 all-MiniLM 默认模型，SeCon-RAG 使用已发布的 kmeans+ngram 路径。论文模型、训练/攻击过程及不可执行的占位模块不纳入本轮结果。

状态：全部完成。共 2400 个逻辑条件，1624 个去重真实请求；三个集合每个条件均为 100/100。

### 10.1 完成结果：五条 vanilla clean 路径与两条防御分支

每格为全文 ACC / 完整答案 EM；分母均为 100。五条 vanilla 行不执行攻击或防御，代表相应仓库的基础回答模板。防御开启行调用实际发布的过滤函数。

|运行路径|NQ|HotpotQA|MS MARCO|
|---|---:|---:|---:|
| PoisonedRAG | 51.00% / 40.00% | 51.00% / 38.00% | 67.00% / 14.00% |
| CamoDocs | 64.00% / 59.00% | 75.00% / 68.00% | 78.00% / 43.00% |
| CorruptRAG_SecRAG | 63.00% / 60.00% | 71.00% / 64.00% | 72.00% / 43.00% |
| RAGDefender | 51.00% / 40.00% | 51.00% / 38.00% | 67.00% / 14.00% |
| SeCon-RAG | 64.00% / 59.00% | 75.00% / 68.00% | 78.00% / 43.00% |
| RAGDefender_enabled | 32.00% / 25.00% | 22.00% / 18.00% | 49.00% / 8.00% |
| SeCon-RAG_enabled | 63.00% / 58.00% | 71.00% / 65.00% | 67.00% / 40.00% |
| current_prompt_original_corpus | 53.00% / 46.00% | 50.00% / 44.00% | 69.00% / 37.00% |

PoisonedRAG 与 RAGDefender vanilla 的 messages 完全相同；CamoDocs 与 SeCon-RAG vanilla 亦相同。对应输出共享同一请求，因此相同得分体现代码路径等价，不能当成跨方法独立复现成功。CorruptRAG 行仅复现 SecRAG 的 clean 生成模板与文档呈现，不涉及攻击构造。

### 10.2 固定上下文的 prompt 与过滤影响

|数据集|原始 BEIR gold passage Hit@5|当前 prompt ACC / UNKNOWN|PoisonedRAG prompt ACC / UNKNOWN|CamoDocs prompt ACC / UNKNOWN|
|---|---:|---:|---:|---:|
| nq | 18.00% | 53.00% / 26.00% | 51.00% / 38.00% | 64.00% / 0.00% |
| hotpotqa | 78.00% | 50.00% / 42.00% | 51.00% / 44.00% | 75.00% / 0.00% |
| msmarco | 12.00% | 69.00% / 23.00% | 67.00% / 25.00% | 78.00% / 0.00% |

这些条件固定 query、原始段落、排序与 victim，只改变模板。拒答指令会改变词面 ACC；允许更积极回答也可能利用模型已有知识，需在后续攻击样本筛选时核验上下文支持性，不能仅凭更高 ACC 认定检索更好。SecRAG 同时加入标题呈现，其差异包括模板与标题，不能解释成纯 system prompt 效应。

|防御 / 数据集|过滤前 → 后 gold passage Hit@5|发送片段均值|全文 ACC：vanilla → 防御|净变化（百分点）|
|---|---:|---:|---:|---:|
| RAGDefender / nq | 18.00% → 7.00% | 2.94 | 51.00% → 32.00% | -19.00 |
| RAGDefender / hotpotqa | 78.00% → 30.00% | 2.50 | 51.00% → 22.00% | -29.00 |
| RAGDefender / msmarco | 12.00% → 8.00% | 2.78 | 67.00% → 49.00% | -18.00 |
| SeCon-RAG / nq | 18.00% → 16.00% | 4.35 | 64.00% → 63.00% | -1.00 |
| SeCon-RAG / hotpotqa | 78.00% → 65.00% | 3.89 | 75.00% → 71.00% | -4.00 |
| SeCon-RAG / msmarco | 12.00% → 5.00% | 2.89 | 78.00% → 67.00% | -11.00 |

防御启用后的段落数按实际保留值记录，没有强行补足五块。RAGDefender 的默认 all-MiniLM 配置与原论文不同；SeCon-RAG 没有执行仓库中的 GPT-RE 占位。这里的差值只描述已发布可运行分支的 clean 效用，复现论文数字需要补齐其模型、上下文构造与推理阶段。

### 10.3 与本地原实验按相同问题、相同短答案重新配对

|数据集|精确题面匹配数|本地 Contriever chunk / 当前 prompt|本地 BM25 chunk / 当前 prompt|原始 BEIR 缓存 / 当前 prompt|
|---|---:|---:|---:|---:|
| nq | 100/100 | 68.00% | 61.00% | 53.00% |
| hotpotqa | 100/100 | 31.00% | 57.00% | 50.00% |
| msmarco | 0/100 | 无交集 | 无交集 | 无交集 |

此表全部按固定 artifact 短答案 aliases 重算，避免把答案压缩的收益混作检索收益。NQ 的 100 题中 6 题在原 validation 提取口径下没有 QA gold，此处使用上游答案补充作诊断，不回填或修改全量 ACC 分母。MS MARCO 原始 train 与当前 document-dev 无交集，不能由小样本差值推算 dev 提升幅度。NQ/HotpotQA 的语料规模、正文单位与 dot/cosine同时不同，因此这张表用于定位问题，不用于单独估计分块的因果效果。

继续使用本地原 QA gold 时，同一 cohort 的 NQ Contriever/BM25 分别为 **62/94（65.96%）与 56/94（59.57%）**；HotpotQA 分别为 **27/100 与 50/100**。改用上游短答案后才得到表中的 68/100、61/100、31/100、57/100。NQ 的样本构成已有明显难度差异，HotpotQA 还有 4/7 题的词面判分变化；这些改善不能计入检索算法增益。

### 10.4 对 pipeline 瓶颈的综合判断

**瓶颈由证据获取、回答策略和评估口径共同构成，单纯对齐上游 pipeline 不足以解决。** NQ 本地 Contriever 68% 高于原始 BEIR/当前 prompt 的 53%；HotpotQA 本地 BM25 57% 也高于相同 prompt 的原始 BEIR 50%。另一方向，原始 HotpotQA 同上下文仅改为简短回答模板就从 50% 到 75%，表明报告中的高低分包含回答策略差异。

原始缓存也有短段落：NQ/HotpotQA/MS MARCO 的 Top-5 中 <32-token passage 占比分别为 14.40% / 17.80% / 4.60%，平均正文总 token 为 583.99 / 553.33 / 397.73。因此“主流 baseline 没有短文本”不成立。关键是其内容与 query 的关系、池中的竞争方式及证据是否齐全，而非仅有长度门槛。原始 HotpotQA 两个 gold passage 全命中也仅为 23%；不能用原生短答案模板的 75% ACC 当作 75% 的自然充分证据率。

定性案例：NQ `test1` 问 Chicago Fire 第四季集数，Top-5 主要涉及其它季，当前 prompt 输出 UNKNOWN，CamoDocs 模板输出 23 并获词面正确；`test60`、`test156`、`test188` 也出现 gold 词组不在正文而短答案模板得分的现象。这些案例提示模型已有知识参与，证据详情见 [prompt 差异案例](../../baseline_clean_compare_20261006/prompt_difference_examples.json)。词面未出现本身不等于语义不支持，需逐条核验。

1. **HotpotQA 首先改善证据排序与两跳覆盖。** 同池 BM25 的全量收益已经验证；上游原语料小样本再用于判断短段落语料与模板能否保留这一趋势。仅追求与某篇论文代码一致，不会自动补足当前全文 Top-5 的两跳证据。
2. **NQ 不能仅按 source Hit 判定检索已解决。** 原始 BEIR passage 的 gold ID 命中低于整页 source 命中，两者标签粒度不同。同题表直接比较最终答案，比横比 18% 与 87% 更有意义。
3. **MS MARCO 必须先分清 document-dev 长答案与 passage-train 短答案。** 小样本原始协议较高的分数不能证明当前索引损坏。下一步应固定 dev 的同题答案集，审计语义等价、相关文档内答案位置与正文噪声，再比较检索器。
4. **固定当前基础设施做少量正交消融。** 依次检验标题呈现、邻接证据扩展、监督 Contriever checkpoint、dot/cosine；每次只改变一项，记录总 token 数、充分证据覆盖、QA 指标。对模型/过滤器的 clean 损失独立报告，不通过丢弃失败题提高分数。

完整逐题 messages、输出、召回排名/分数、过滤结果和别名配对见 [小样本报告](../../baseline_clean_compare_20261006/report.md)、[固定题单与运行说明](../../baseline_clean_compare_20261006/README.md)、[同题配对结果](../../baseline_clean_compare_20261006/matched_local_summary.json)。

# 原始 BEIR 语料固定 300 题 clean 对照

状态：complete。

统一 Qwen3.8-27B、Top-5、max_tokens=1000；复用上游全库 scored cache。相同消息合并调用，不能视为独立重复试验。防御启用分支的实现范围见 task_protocol.json。

| dataset | profile | 完成 | 全文 ACC | EM | F1 | UNKNOWN | 输出截断 | gold Hit@5（过滤前） | 发送片段均值 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| nq | PoisonedRAG | 100/100 | 51.00% | 40.00% | 47.18% | 38.00% | 0.00% | 18.00% | 5.00 |
| nq | CamoDocs | 100/100 | 64.00% | 59.00% | 64.84% | 0.00% | 0.00% | 18.00% | 5.00 |
| nq | RAGDefender | 100/100 | 51.00% | 40.00% | 47.18% | 38.00% | 0.00% | 18.00% | 5.00 |
| nq | SeCon-RAG | 100/100 | 64.00% | 59.00% | 64.84% | 0.00% | 0.00% | 18.00% | 5.00 |
| nq | RAGDefender_enabled | 100/100 | 32.00% | 25.00% | 29.16% | 57.00% | 0.00% | 18.00% | 2.94 |
| nq | SeCon-RAG_enabled | 100/100 | 63.00% | 58.00% | 65.56% | 0.00% | 0.00% | 18.00% | 4.35 |
| nq | CorruptRAG_SecRAG | 100/100 | 63.00% | 60.00% | 65.90% | 1.00% | 0.00% | 18.00% | 5.00 |
| nq | current_prompt_original_corpus | 100/100 | 53.00% | 46.00% | 53.71% | 26.00% | 1.00% | 18.00% | 5.00 |
| hotpotqa | PoisonedRAG | 100/100 | 51.00% | 38.00% | 44.48% | 44.00% | 0.00% | 78.00% | 5.00 |
| hotpotqa | CamoDocs | 100/100 | 75.00% | 68.00% | 76.68% | 0.00% | 0.00% | 78.00% | 5.00 |
| hotpotqa | RAGDefender | 100/100 | 51.00% | 38.00% | 44.48% | 44.00% | 0.00% | 78.00% | 5.00 |
| hotpotqa | SeCon-RAG | 100/100 | 75.00% | 68.00% | 76.68% | 0.00% | 0.00% | 78.00% | 5.00 |
| hotpotqa | RAGDefender_enabled | 100/100 | 22.00% | 18.00% | 18.61% | 77.00% | 0.00% | 78.00% | 2.50 |
| hotpotqa | SeCon-RAG_enabled | 100/100 | 71.00% | 65.00% | 73.12% | 0.00% | 0.00% | 78.00% | 3.89 |
| hotpotqa | CorruptRAG_SecRAG | 100/100 | 71.00% | 64.00% | 73.09% | 0.00% | 0.00% | 78.00% | 5.00 |
| hotpotqa | current_prompt_original_corpus | 100/100 | 50.00% | 44.00% | 48.84% | 42.00% | 4.00% | 78.00% | 5.00 |
| msmarco | PoisonedRAG | 100/100 | 67.00% | 14.00% | 36.96% | 25.00% | 0.00% | 12.00% | 5.00 |
| msmarco | CamoDocs | 100/100 | 78.00% | 43.00% | 67.29% | 0.00% | 0.00% | 12.00% | 5.00 |
| msmarco | RAGDefender | 100/100 | 67.00% | 14.00% | 36.96% | 25.00% | 0.00% | 12.00% | 5.00 |
| msmarco | SeCon-RAG | 100/100 | 78.00% | 43.00% | 67.29% | 0.00% | 0.00% | 12.00% | 5.00 |
| msmarco | RAGDefender_enabled | 100/100 | 49.00% | 8.00% | 26.06% | 44.00% | 0.00% | 12.00% | 2.78 |
| msmarco | SeCon-RAG_enabled | 100/100 | 67.00% | 40.00% | 59.52% | 0.00% | 0.00% | 12.00% | 2.89 |
| msmarco | CorruptRAG_SecRAG | 100/100 | 72.00% | 43.00% | 63.22% | 1.00% | 0.00% | 12.00% | 5.00 |
| msmarco | current_prompt_original_corpus | 100/100 | 69.00% | 37.00% | 57.20% | 23.00% | 0.00% | 12.00% | 5.00 |

# 原语料固定 300 题 clean baseline 对照

日期：2026-10-06。状态：全部完成。2400 个逻辑条件、1624 个去重请求；各集合各条件完成 100/100。校验见 verification.json。

## 设计

- NQ、HotpotQA、MS MARCO 各 100 题，冻结 PoisonedRAG 随仓库发布的题单，五个方法共用。本次不再按 clean 成功率或文档长度筛选；沿用上游预选题单，并非完整 eval 的新随机样本。NQ/HotpotQA 为 BEIR test；MS MARCO 经 qrels 验证为 BEIR train，不是当前 document-dev。
- 方法：PoisonedRAG、CamoDocs、CorruptRAG（SecRAG）、RAGDefender、SeCon-RAG；另加后两者发布代码可执行的防御开启分支，以及当前 prompt 的原始语料对照。共 8×300 个逻辑条件，相同消息按 SHA256 合并真实调用。
- 语料为 data/datasets/beir_based 中的原始 corpus。复用上游 full-corpus scored Top-100 缓存中的 Top-5，按 cache 原分数降序排列，完整保留原始 text，不再执行 256-token 分块。每题召回 ID、rank、score、title/text 在 retrieval.jsonl。
- 这是原语料 clean 路径的统一 victim 复现。没有重新计算全库检索；上游 raw-dot 默认代码与缓存绑定，但未重新验证每个缓存分数。CamoDocs 与 SecRAG 接受同一缓存作为显式输入，既有 1000 题攻击优化样本不混入固定题单。
- LLM 为 d01 既有 Qwen3.8-27B OpenAI-compatible 服务；temperature=0、top_p=1、seed=0、enable_thinking=false、max_tokens=1000。8 workers，按配置 100 RPM，传输失败最多 3 次；首次成功响应固定，输出截断不重试。无 Agent、多轮或攻击生成。
- RAGDefender 启用分支直接调用公开 API，all-MiniLM-L6-v2 为其默认模型；论文 Stella 与旧 artifacts paraphrase-MiniLM 不等同。SeCon-RAG 直接调用 native k_mean_filtering（ngram 开启），采用代码的 singleton CLS embedding；设备为 CPU。发布代码 GPT-RE 占位未实现，不补造该阶段。
- 五条 vanilla clean 分支使用各仓库原生 prompt。SecRAG 含原生标题格式；其余四条按原代码仅拼 text。当前 prompt 原样保留 Final answer 与 UNKNOWN 指令。同一请求的条件共享输出，只是协议等价，不是独立复现次数。
- 统一评分：同一套 artifact correct-answer aliases，全文规范化完整词组匹配、完整答案 EM、token F1。原生模板无需 Final answer 标记；若存在则提取标记行。UNKNOWN 和输出截断判失败。该短答案 gold 与全量 MS document-dev 长答案口径不同。

## 复现

额外研究依赖：SeCon-RAG 上游要求 rouge-score；此次使用 0.1.2。CPU inference 使用现有 transformers、torch、sentence-transformers、scikit-learn。没有更改正式基础设施依赖。

```bash
python -m pip install rouge-score==0.1.2
python src/main.py poc baseline-clean-compare --stage prepare --output results/baseline_clean_compare_20261006
python src/main.py poc baseline-clean-compare --stage tasks --output results/baseline_clean_compare_20261006 --models /mnt/sdc2/models
python src/main.py poc baseline-clean-compare --stage generate --output results/baseline_clean_compare_20261006 --env /path/to/private.env
python src/main.py poc baseline-clean-compare --stage report --output results/baseline_clean_compare_20261006
```

源码在 tests/experiments/baseline_clean_compare.py，由 src/main.py 统一调度。上游版本、输入缓存哈希、prompt 代码指纹见 provenance.json/prepared.json；真实 messages/返回模型/使用量见 generation_attempts.jsonl，文件不含密钥。结果版本为目录日期。现有完整 BM25 与 dense 输出不覆盖。

[综合分析报告](../full_clean_top5_tail32_20261004/post_run_analysis/report.md)；[本实验逐条件结果](report.md)。

补充诊断可用 `python src/main.py poc baseline-clean-analysis --output results/baseline_clean_compare_20261006` 重建。matched_local_comparison.jsonl 保存同题、不同答案口径的逐条重评分；original_retrieval_diagnostics.json 保存原始 Top-5 长度与 gold 覆盖；prompt_difference_examples.json 保存 5 个定性案例。
