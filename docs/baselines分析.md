# RAG 攻防 Baseline 统一复现：可行性审定与计算资源评估

> **审定对象**：`/home/shadowx/mnt/sdc2/New_Future/GraduationDesign/SEU_Graduation_Design`（ChunkTrojan 现役代码库）
> **输入依据**：`docs/RAG安全文献攻防技术手段总结报告.md`（**81 篇独立文献**，攻击 A1–A17 / 防御 D1–D18；实验设计与开销统计见其 §7，优先级评定见 §8，综述补充的攻防文献见 §9，跨域借鉴文献见其 §6.7，低优先级邻域文献见其 §6.8）
> **审定日期**：2026-10-02
> **结论口径**：本文所有资产数字均为**本机实测**；所有计算量估算均标注为**估算**并给出推导依据。未实测处不冒充实测。

---

## 0. 结论摘要

**可以复用，且复用价值高于重新搭建。** 但"可复用"集中在**数据层与检索层**，**攻击/防御的适配与调度层需要新建**。

| 判定项 | 结论 | 一句话依据 |
|---|---|---|
| 300-query PoC 数据 | ✅ **直接可用** | 3 数据集 × 100 抽样题，含 qrels、gold alias、语义分层配额，已冻结 |
| 12 套分块索引（4 档 × 3 数据集） | ✅ **可直接可用** | 604 GB，全覆盖验收完成，`manifest.json` 状态 `complete` |
| 检索背景缓存（top-1000 精确排名） | ✅ **核心复用资产** | `screening.jsonl` 已存每题每档 1000 深度的精确排名 |
| query 向量缓存 | ✅ **核心复用资产** | 768 维 FP32，精确复算所需 |
| 生成评测协议（prompt / 判分 / 日志） | ✅ **可直接可用** | 固定 system/user prompt、EM+alias 判分、全量 API 记录 |
| 攻击载荷注入 → 索引重建 | ⚠️ **需新建（但成本极低）** | 现有管线只索引原始语料；append-only 注入走增量路径即可 |
| 重排器阶段（reranker） | ❌ **缺失** | 现役协议 `reranker: false`；CEG-RAG/P3A/GRADA 类方法需要 |
| 多阶段拦截框架（检索→重排→生成） | ❌ **缺失** | 现有管线是单链路，防御需可插拔拦截点 |
| 攻击/防御适配层 | ❌ **缺失** | `src/attack/` 仅占位 docstring，`src/defense/` 为空目录 |
| 磁盘余量 | ⚠️ **紧张** | `/mnt/sdb1` 3.7 T 已用 97%，仅剩 138 GB |
| 本机算力 | ❌ **不可用于编码/生成** | 本机仅 1×Tesla M40 12 GB + 15 GB RAM；编码与 27B 生成实际在 dancher-01/03 远端完成 |

**关键结论（详见 §3）**：对**绝大多数攻击族**（凡"向语料追加新文档"者），**检索结果可被精确、近乎零成本地复算**——因为追加文档不改变既有文档与 query 的向量，新排名 = 旧排名与新分值的归并。这意味着统一复现**不需要重跑 604 GB 全库检索**，单格（100 题 × 1 档）检索复算 < 1 秒。

**瓶颈不在受害者侧生成**（100 题仅需约 1.1 分钟），而在**攻击载荷构造所需的迭代式 LLM/受害者调用**（InceptionRAG 的 ZOSO、SIREN 的 PAIR 循环、ReGENT 的 RL 循环可达每问数十至数百次调用），以及**多阶段防御的成倍生成**（RobustRAG 类隔离-聚合为 5–6 倍）。

---

## 1. 现有资产盘点（全部本机实测）

### 1.1 语料与索引

`data/datasets/{hotpotqa_official,nq_v2,ms-macro_official}/.../poc/`，索引实体落在 `/mnt/sdb1/ragshield_protocol_v2/`（符号链接接入）。

| 数据集 | 文档数 | 语料 content tokens | @64 块数 | @128 | @256 | @512 | 分片数 | 索引体积（四档合计） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HotpotQA fullwiki | 5,486,212 | 2,592,266,659 | 43,286,268 | 23,210,636 | 13,400,704 | 8,739,565 | 649 | **417 GB** |
| MS MARCO doc dev | 401,855 | 1,206,689,861 | 19,052,437 | 9,626,657 | 4,913,542 | 2,565,965 | 303 | **170 GB** |
| NQ validation | 7,378 | 59,387,781 | 931,554 | 467,590 | 235,618 | 120,160 | 15 | **8.3 GB** |
| **合计** | 5,895,445 | 3.858 B | 63.27 M | 33.30 M | 18.55 M | 11.43 M | 967 | **≈ 595 GB**（含 corpus 副本共 604 GB） |

- 协议 `contriever-cls-sep-v2`：FP16 模型、FP32 masked mean pooling、L2 归一化、FAISS `IndexFlatIP`，overlap=0，内容容量 64/128/256/**510**（512 档为 CLS/SEP 各留 1 位）。
- 分片粒度：**每片 4,000,000 content tokens**，边界只落在文档之间（`shard_tokens: 4000000`）；已实测单片 @512 构建 27.6 s、占盘 56.7 MB。
- 全部 `manifest.json` 状态 `complete`，向量有限性与 L2 范数已验收。

### 1.2 问题集

| 集合 | 规模 | 位置 | 说明 |
|---|---:|---|---|
| **300-query PoC（分层抽样）** | **300**（100 × 3） | 各 `poc/queries.jsonl` | InceptionRAG 五类语义配额（TIME/PERSON/LOCATION/QUANTITY/IDENTITY），类内长度降序；`fill_seed=20260924` |
| 全量池 | 7,405 / 4,462 / 5,169 | 各 `poc/queries_all.jsonl` | answer-bearing 全量 |
| 全量 clean 评测集 | **20,428** | `results/full_clean_top5_20260927/*/queries.jsonl` | 三集合原始 validation/dev 全部 query |

- 每题含 `answers`（gold alias 集）、`positive_sources`（正相关文档 ID）、`metadata.stratum`。
- 抽样有硬门槛：**至少一篇正相关 gold 载体 > 512 Contriever tokens**，因此 300 题**天然适配四档中 ≥256 的档位**（64 档对部分题的下游块过短）。

### 1.3 检索缓存（**核心复用资产**）

| 资产 | 位置 | 实测规格 |
|---|---|---|
| 精确排名背景 | `results/contriever_protocol_v2_20260925/clean_{hotpot,nq,ms}/screening.jsonl` | 每数据集 **400 行**（100 题 × 4 档），每行 `top` 为 **1000 深度精确排名** `[chunk_id, score]`，另有 `top20` |
| query 向量 | 同名 `query_vectors.npy` | `(100, 768) float32`（hotpot）、`(200, 768)`（nm=nq+ms）、`(7830/7405/5193, 768)`（full_clean） |
| 分片检索前缀 | `clean_nm/search/d01,d03/`、`full_clean_top5_20260927/*/search/` | 每语料分片一份 npz（649 + 303 + 15 文件；hotpotqa 277 MB、msmarco 92 MB、nq 6.8 MB） |
| 正相关载体 | `clean_*/positive_documents.jsonl`、`positive_chunks.jsonl` | 按数据集与块档索引 |
| 逐题 Top-5 完整记录 | `results/full_clean_top5_20260927/*/retrieval.jsonl` | 含 `chunk_id`、`score`、`rank`、`text`、`start_token`/`end_token`、`chunk_size`、`protocol` |

`screening.jsonl` 字段：`answer_alias_match, clean_valid, dataset, first_positive_rank_top1000, full_corpus_vectors, instance, positive_minus_top10_boundary, positive_source_best_chunk_score, shard_count, short_chunk_counts, size, source_recall, top, top20`。

**这些字段本身已经覆盖了文献报告 §7.5 要求的多种统计口径**：检索侧命中（`source_recall` 在 10/20/50/100/500/1000 六档）、排序位次（`first_positive_rank_top1000`）、clean 有效性（`clean_valid`）。即统一复现所需的"检索侧 ASR/Hit"分母**已经预计算完毕**。

### 1.4 管线代码

| 模块 | 作用 | 复用价值 |
|---|---|---|
| `src/common/encoding_protocol.py` | CLS/SEP v2 容量与块数计算（`content_capacity`、`chunk_count`） | 必复用：保证注入文档与语料同协议编码 |
| `src/common/indexing.py` | `ContrieverEncoder`（FP16、长度感知合批）、`build_index`、`load_index` | 必复用 |
| `src/common/shards.py` | `document_shards`、`build_shards`、`retrieve_shards` | 必复用：注入分片按同一分片规则生成 |
| `tests/experiments/cached_retrieval.py` | `cached_background()`：返回**字节保真的 query 向量 + 精确 Top-100 背景 + 覆盖校验**，供调用方"对新文档向量打分" | **核心复用**：这正是注入式攻击所需的接口 |
| `tests/experiments/full_clean.py` | 可续跑的全分片精确检索与生成；`prepare/retrieve/generate/report/summarize/diagnose` | 复用其判分与报告生成 |
| `tests/experiments/chat.py` | `ChatClient`：进程级令牌桶限速（`RPM_PARALLEL`）、全量 usage 日志、指数退避重试 | 必复用：统一 LLM 出口 |
| `tests/experiments/answers.py` | alias 归一化匹配（EM / contains） | 必复用 |
| `tests/experiments/documents.py` | `_chunk_document`、`_token_spans` | 复用：注入文档的分块与偏移 |
| `src/attack/` | 仅 `"""Reserved for future supported attacks…"""` | **占位，需新建** |
| `src/defense/` | 空目录 | **需新建** |
| `baselines/` | 38 个 submodule + 3 个源码快照，分 `attacks/`、`defenses/`、`benchmarks/`、`tools/`、`misc/` 五类（§1.7） | 上游实现载体已就位 |

### 1.5 模型动物园（本地 `/mnt/sdc2/models`，实测存在）

| 类别 | 已下载模型 | 对应可复现方法 |
|---|---|---|
| 稠密检索器 | `contriever`(837 M)、`contriever-msmarco`(419 M)、`ance-firstp`(4.6 G) | PoisonedRAG/GASLITE/corpus-poisoning/HijackRAG/SilentRetrieval（白盒检索器） |
| 其他嵌入 | `bge-base-en`、`bge-m3`、`gte-modernbert-base`、`jina-embeddings-v5`、`multilingual-e5-base`、`nomic-embed-text-v1.5`、`Qwen3-Embedding-0.6B` | AgentPoison 式跨嵌入器迁移、Influence Factors 的检索器因子实验 |
| 重排器 / 交叉编码器 | `bge-reranker-v2-m3`、`gte-reranker-modernbert-base`、`jina-reranker-v3.5`、`Qwen3-Reranker-0.6B`、`ms-marco-MiniLM-L6-v2` | **CEG-RAG、P3A、CRCP、GRADA、ProGRank**（重排相关） |
| MLM（掩码概率检测） | `electra-base-discriminator`(1.7 G)、`gpt2`(5.3 G) | **GMTP**（梯度掩码 + MLM 概率） |
| 注入防护 | `PIGuard`(714 M) | 提示注入检测类对照 |

> 这是本次审定中价值最高的**意外发现**：文献中大量防御（GMTP 的 MLM、CEG-RAG/P3A 的 cross-encoder）所需的**具体模型已本地就绪**，无需再申请下载。

### 1.6 硬件与算力（实测）

| 位置 | 配置 | 可用性 |
|---|---|---|
| **本机**（wfy-desktop-home） | 1× Tesla M40 11.5 GB（Maxwell，无 FP16/BF16 张量核）、12 核、15 GB RAM | ❌ 不足以跑 Contriever FP16 编码，也不足以跑 27B 生成；**仅适合做调度、打分、报告** |
| 远端 dancher-01 | A6000 48 GB | 编码（batch=128，2 进程）与 vLLM 27B 生成 |
| 远端 dancher-03 | RTX 4090 24 GB | 编码（batch=256，2 进程） |
| 磁盘 `/mnt/sdb1` | 3.7 T，**已用 97%，剩 138 GB** | ⚠️ 索引主盘 |
| 磁盘 `/mnt/sdc2` | 932 G，已用 85%，剩 143 GB | 模型与数据 |
| 磁盘 `/` | 278 G，已用 61%，剩 106 GB | 系统 |

**已实测吞吐**（关键成本参数）：

| 指标 | dancher-01 | dancher-03 | 来源 |
|---|---:|---:|---|
| 文档分片吞吐（2 进程，含四档） | **63.18 份/小时** | **75.34 份/小时** | `throughput_tuning.md` |
| 单进程吞吐 | 46.14 份/小时 | 43.28 份/小时 | 同上 |
| 单片墙钟（四档合计） | 117.4 s | 76.0 s | `throughput_rebalance.json` |
| 折算编码速率 | ≈ 70 K tok/s | ≈ 84 K tok/s | 4 M tok/片 ÷ 3600 |

生成侧（`backend.json` + `progress.json`）：vLLM `qwen3.8-27b`（W8A8 INT8 + DFlash 投机解码，`max_model_len=65536`、`max_num_seqs=8`），客户端 **100 RPM / 8 workers**；实测 MS MARCO 5,193 题 56.6 min、HotpotQA 7,405 题 76.2 min → **≈ 95 题/分钟**（已贴近限速上限，**瓶颈是客户端配额而非 GPU**）。

### 1.7 上游 baseline 清单（`baselines/`）

`baselines/` 按性质分为五类，共 **41 个项目目录**（38 个 Git submodule + 3 个源码快照），另含 `patches/` 本地适配补丁。

| 类别 | 数量 | 项目 |
|---|---:|---|
| `attacks/` | 14（11 submodule + `OTRB`、`p3a`、`FlippedRAG` 源码快照） | InceptionRAG、PoisonedRAG、corpus-poisoning、GASLITE、GARAG、robust-rag、Topic-FlipRAG、TrojanRAG、Open-Prompt-Injection、MIRAGE、CamoDocs、OTRB、p3a、FlippedRAG |
| `defenses/` | 16 | CEG-RAG、GMTP、GRADA、PIShield、RAGDefender、RobustRAG、TrustRAG、indirect-pia-detection、HijackRAG、Joint-GCG、PRA-RAG、RAG-Responsibility-Attribution、ReliabilityRAG、Secon-Rag、Stealthy_Attacks_Against_RAG、tris |
| `benchmarks/` | 3 | BIPIA、SafeRAG、SecRAG |
| `tools/` | 2 | evaluate、gector |
| `misc/` | 6 | EMNLP2025-Claim-Verification-Survey、Fact-checking-via-Raw-Evidence、llm-misinformation-survey、TRACER、DEO-negation-aware-retrieval、AdversarialCoT_case |

- **进入统一复现矩阵的是 `attacks/` 与 `defenses/` 两类，共 30 个项目**（27 submodule + `OTRB`、`p3a`、`FlippedRAG`）；它们对应 §4 G6 的适配工作量与 §6 的资源评估。（另 `misc/AdversarialCoT_case` 为 A17 的案例制品，不含实现代码，不入矩阵。）
- **本地载体与文献方法清单的高度对齐，但仍非一一对应**：本次相对上一版新增的 3 篇（`#79`–`#81`）与本地载体的对应关系如下；仍需按原论文新建适配器的是 **`#66 MedMisBench`（A16）、`#70 Estimating Embedding Vectors`、`#73 ToxicRAG`、`#76 RAGForensics`、`#80 DenialRAG`，以及仅在 §9 综述补充中出现的约 20 篇**。因此适配工作量应按**并集**而非交集估算（§4 G6）。

| 文献报告条目 | 报告内类别 | 本地载体 | 备注 |
|---|---|---|---|
| `#64` TRIS | 防御（**D18** 三层检索完整性筛） | `baselines/defenses/tris` | 补齐"检索期纵深校验"空白；L1/L2 廉价、L3 昂贵（§6.3、§6.4） |
| `#65` Toward Robust RALMs | 基准/实证 | `baselines/attacks/robust-rag` | 提供 **GenADV**（A16 攻击）与 **RAD** 指标；报告把它归入基准/实证类，本地按"含对抗样例构造"置于攻击侧 |
| `#66` MedMisBench | 基准（**A16** 认知韧性） | — | 未本地化；A16 的"误导上下文注入"需据此自建适配 |
| `#67` DEO | 基础方法 | `baselines/misc/DEO-negation-aware-retrieval` | 否定感知检索（§5.2 缺口 13） |
| `#68` Combating Misinformation | 跨域（§6.7） | `baselines/misc/llm-misinformation-survey` | 虚假信息治理综述 |
| `#69` Complex Claim Verification | 跨域（§6.7） | `baselines/misc/Fact-checking-via-Raw-Evidence` | 时间约束证据（§7.1 的"时间轴"、E11） |
| `#70` Estimating Embedding Vectors | 跨域（§6.7） | — | 未本地化；查询嵌入估计的理论根基 |
| `#71` The Missing Parts（TRACER） | 跨域（§6.7） | `baselines/misc/TRACER` | 遗漏型误导/半真检测（§5.2 缺口 13） |
| `#72` A Systematic Survey of Claim Verification | 跨域（§6.7） | `baselines/misc/EMNLP2025-Claim-Verification-Survey` | 标注一致性（IAA）作为 ACC 口径上限（§7.5、E9） |
| `#73` ToxicRAG | 攻击（**A13** 单文档叙事投毒） | — | 未本地化；"知识已被更新"式因果叙事 + 答案导向自校验（§6.2） |
| `#74` FlippedRAG | 攻击（**A9** 黑盒观点操纵） | `baselines/attacks/FlippedRAG`（源码快照） | 上下文泄露反推黑盒检索器 + 触发器优化；模仿训练开销需自建（§6.2） |
| `#75` MIRAGE | 攻击（**A6** 严格黑盒·查询无关） | `baselines/attacks/MIRAGE` | 合成查询分布 + 语义锚定 + 对抗 TPO；原文全部实验在单张 H200（§6.2、§6.4） |
| `#76` RAGForensics | 防御（**D12** 投毒追溯） | — | 未本地化；"检索—判定—剔除"迭代取证（§6.3） |
| `#77` FilterRAG | 低优先级（其 §6.8） | — | 多模态 VQA 去幻觉，**不进入复现矩阵** |
| `#78` 检索增强生成综述:方法与应用 | 综述（其 §6.3） | — | 中文综述，技术底座参照的第二来源 |
| `#79` CamoDocs | 攻击（**A6** 嵌入分散·抗聚类投毒） | `baselines/attacks/CamoDocs` | 良性/对抗子文档分别切块 + 分散 token 替换 + 连贯性重排；同时躲开查询检测与聚类检测（§6.2、§6.4） |
| `#80` DenialRAG | 攻击（**A13** 单文档·嵌入式否认） | — | 未本地化；显式点名正确答案并当场否决（§6.2） |
| `#81` AdversarialCoT | 攻击（**A17** 推理链污染） | `baselines/misc/AdversarialCoT_case`（案例制品，**无实现代码**） | 伪推理链 + 观察/反馈/再优化回路；只可读回输出的决策式黑盒（§6.2） |

- `benchmarks/` 提供评测协议与载荷集合，`tools/` 提供指标与文本扰动能力；两者按需被前两类适配器调用，不单独作为对比方法。
- `misc/` 是与 RAG 安全相邻、但不属投毒/注入攻防的资料：声明验证、事实核查、半真检测与否定感知检索。**它们不进入统一复现矩阵**，其语料与标签体系与 RAG 投毒任务不可直接混用；若后续需要纳入，须先单独说明口径差异。逐项定位与上游地址见 [baselines/README.md](../baselines/README.md)。
- 版本固定方式：每个 submodule 在主仓库以 gitlink 锁定提交，`git submodule update --init` 即可复现；`attacks/OTRB`、`attacks/p3a` 与 `attacks/FlippedRAG` 为源码快照，随主仓库提交（FlippedRAG 仅跟踪代码与小型元数据，其余约 2.6 GB 复现产物按 `.gitignore` 排除）。

---

## 2. 复用性判定：逐环节

| 环节 | 现役实现 | 可否复用 | 需要做的改动 |
|---|---|---|---|
| 语料与 gold | `poc/corpus.jsonl`、`qrels.tsv`、alias | ✅ 直接 | 无 |
| 问题集 | 300 抽样 / 20,428 全量，已冻结 | ✅ 直接 | 攻击若需 held-out 划分，需另行按 `instance` 切分 |
| 分块与编码 | `encoding_protocol` + `indexing.ContrieverEncoder` | ✅ 直接 | 注入文档按同协议编码 |
| 语料索引 | 12 套，`complete` | ✅ 直接 | 攻击只追加时**不需重建**（见 §3） |
| 精确检索 | `full_clean.retrieve`（全分片 FAISS，按片缓存 npz） | ✅ 直接 | 只对"修改既有文档"的攻击需要局部重算 |
| 检索背景复用 | `cached_retrieval.cached_background` + `screening.jsonl` | ✅ 直接 | 这正是注入式攻击的接入点 |
| 重排 | **无** | ❌ 新建 | 引入 cross-encoder（本地已有 5 个候选模型） |
| 上下文组装 | `CONTEXT: {ctx}\nQUESTION: {q}`，两空行连 5 块 | ⚠️ 可配置化 | 各 baseline 的 prompt/上下文格式不同，需抽象 |
| 受害者生成 | `ChatClient` + vLLM 27B | ✅ 直接 | 可换模型后端以复现跨 LLM 迁移 |
| 判分 | `answers.answer_matches`（归一化 EM / contains） | ✅ 直接 | 报告 §7.5 建议的 **LLM-judge 口径需新增** |
| 调度 | `poc <cmd> --stage` | ⚠️ 部分 | 需要"攻击→检索→防御→生成→判分"的矩阵编排 |
| 攻击/防御实现 | 空 | ❌ 新建 | 从 `baselines/attacks` 与 `baselines/defenses` 的 32 个项目适配（§1.7） |

**结论**：数据、索引、编码、检索、生成、判分这几层可**零改动或极小改动直接复用**——这已覆盖统一复现 80% 以上的工程量。缺口集中在**重排阶段、可插拔拦截、矩阵编排、以及 32 个攻击/防御项目的适配层**。

---

## 3. 关键判定：检索可精确复用（本节为复用可行性的技术核心）

### 3.1 命题

设干净语料文档集 $C$，查询 $q$ 已编码为 $v_q$（L2 归一化），语料向量 $v_d$。排名函数为余弦内积：

$$
r_q(d) = \langle v_q, v_d \rangle
$$

攻击注入文档集 $P$（$P \cap C = \varnothing$）。则对任意 $d \in C$，$r_q(d)$ **不变**；新排名为

$$
\mathrm{TopK}\big(\{r_q(d)\}_{d \in C \cup P}\big) = \mathrm{TopK}\Big(\underbrace{\{r_q(d)\}_{d\in C}}_{\text{已缓存的 } top\text{-}1000} \cup \underbrace{\{r_q(p)\}_{p\in P}}_{\text{只需 } |P| \text{ 次内积}}\Big)
$$

**只要缓存的干净排名深度 $K_{cache} \ge K_{need} + |P|$，结果与全库重算逐位相同。**

本仓库现状：$K_{cache} = 1000$，$K_{need} = 5$，典型 $|P| \le 50$。**余量充足**。

### 3.2 适用范围

| 攻击族 | 是否改变既有向量 | 可否走缓存路径 | 说明 |
|---|---|---|---|
| 追加新文档（PoisonedRAG、corpus-poisoning、GASLITE、OTRB、Phantom、CatPoison、AuthChain、CorruptRAG、HijackRAG、SilentRetrieval、BadRAG、Micro-Collaborative、ReGENT 注入、**CamoDocs**、**DenialRAG**、**AdversarialCoT**，**以及 Joint-GCG**） | 否 | ✅ **精确且近零成本** | 主流攻击族。Joint-GCG 虽需白盒梯度**构造**载荷，但最终只是往**未改动的**检索器里注入文本，故评估期仍可走缓存；A17 的 AdversarialCoT 虽需多轮反馈优化，但载荷仍是“追加文档”，评估期同样可走缓存 |
| **A16 干扰/不可答诱导**（Toward Robust RALMs 的 GenADV、MedMisBench 的误导上下文注入） | 否（仅追加干扰文档） | ✅ **精确且近零成本** | 载荷目标是"让模型在不该作答时作答"，不伪造具体答案；构造期只在本地生成上下文，评估期同样走缓存 |
| **改写既有文档**（GARAG 拼写扰动、P3A 字符扰动、CRCP、Human-Imperceptible） | 是 | ✅ **仍可精确**（局部重算） | 只需重编码**被改写的那几篇**文档（通常 1 篇/题），再用其新向量替换旧向量参与归并 |
| **改变检索器本身**（TrojanRAG：训练并分发检索器） | 是（模型变） | ❌ **必须重算** | 检索器一变，$v_q$ 与全部 $v_d$ 都变；受害者安装的是攻击者训练过的检索器 |
| 多向量/混合检索（Semantic Chameleon 的 BM25 混合） | 需稀疏通道 | ⚠️ 需新增 | 缓存只覆盖稠密通道 |

**只有第 3 类（改变检索器本身）需要重跑全库检索。** 其余均可由缓存精确复算。需要区分的是：**构造期的白盒开销**（Joint-GCG 的 27B 反向）与**评估期的索引重算**（TrojanRAG 的重建）是两件不同的事。

### 3.3 成本对比（估算）

单格 = 100 题 × 1 档。

| 路径 | 计算量 | 估算耗时 |
|---|---|---|
| 全库重检索（HotpotQA @256） | 13.40 M 向量 × 768 维 × 100 题；FP16 向量体积 ≈ 20.6 GB/题，需读 ≈ 2.06 TB | 数小时～十余小时（依是否命中 page cache） |
| **缓存路径（本文推荐）** | 53 篇载荷 × 100 题 = 5,300 次 768 维内积 ≈ 0.008 GFLOP | **< 1 秒** |

> 缓存路径**不仅是"够用"，而是"更精确"**：全库重检索会引入 FAISS 分片级 tie-break 与浮点累积顺序差异（现役记录的最大重算差异为 2.38×10⁻⁷），而缓存归并只需一次确定性的 `lexsort`（`full_clean.merge_top5` 已实现该确定性 tie-break）。

---

## 4. 缺口清单与需新建组件

| 编号 | 缺口 | 影响的方法 | 工作量 |
|---|---|---|---|
| G1 | **注入语料的可插拔索引层**：现有索引是"原始语料"的固定产物，无"干净 + 注入"合并检索的正式入口 | 全部攻击 | 中：`cached_retrieval` 已提供一半，需补"注入文档编码 → 与缓存归并 → 输出 top-k（含 provenance）" |
| G2 | **重排阶段** | CEG-RAG、P3A、CRCP、GRADA、ProGRank | 中：接入 cross-encoder，本地模型已就绪 |
| G3 | **防御拦截点抽象**（检索前 / 检索后 / 重排后 / 生成前 / 生成后） | 全部防御 | 中：定义 `pre_retrieval / post_retrieval / pre_generation / post_generation` 四个钩子 |
| G4 | **多阶段/多轮编排**（防御可能多次调用 LLM，或不调用 LLM 直接改检索结果） | RobustRAG、PRA-RAG、Astute RAG、CARE-RAG、RAGOrigin、RAGForensics、Cordon-MAS | 大：需要 DAG 式执行器与调用预算记账 |
| G5 | **LLM-judge 判分口径** | 文献报告 §7.5 建议双口径 | 小：新增 judge prompt + 解析 |
| G6 | **攻击/防御适配层** | 全部 | 大：`baselines/attacks` 与 `baselines/defenses` 共 32 个项目的 API 各异（详见 §6） |
| G7 | **held-out 划分机制** | 通用/可迁移类攻击（GASLITE、corpus-poisoning、GCG） | 小：按 `instance` 切分并冻结 |
| G8 | **磁盘与索引重建预算** | 需重建索引的方法 | 大：见 §7 |
| G9 | **多检索器/多生成器矩阵** | Influence Factors 类因子实验、跨模型迁移 | 中：检索器可切换，需重编码 |

---

## 5. 建议的统一复现框架

```
src/
├── common/                     # 现有，基本不动
├── attack/                     # 新建：统一攻击接口
│   ├── base.py                 # AttackAdapter: build_payloads() -> list[InjectedDoc]
│   ├── index_overlay.py        # 干净索引 + 注入文档的合并检索（走 §3 缓存路径）
│   └── adapters/               # 每个 baseline 一个适配器
├── defense/                    # 新建：统一防御接口
│   ├── base.py                 # DefenseAdapter: pre_retrieval/post_retrieval/pre_generation
│   └── adapters/
└── harness/                    # 新建：矩阵编排
    ├── matrix.py               # (attack × defense × dataset × size) 笛卡尔积
    ├── budget.py               # LLM 调用记账与限速（复用 ChatClient 令牌桶）
    └── report.py               # 汇总为统一指标表

tests/experiments/
└── baseline_repro.py           # 新 CLI: poc baseline-repro --stage ...
```

**统一接口（草案）**

```python
@dataclass(frozen=True)
class InjectedDoc:
    doc_id: str                  # 攻击专用命名空间，如 "payload:nq:0:3"
    text: str                    # 完整文档正文（由受害者 chunker 决定分块）
    target_query_ids: tuple[str, ...]
    malicious_answer: str | None

class AttackAdapter(Protocol):
    def build(self, queries, clean_background, *, budget) -> list[InjectedDoc]: ...

class DefenseAdapter(Protocol):
    def post_retrieval(self, query, hits, *, budget) -> list[RetrievalHit]: ...
```

**评测四元指标（对齐文献报告 §10 第 4 条建议）**：`攻击成功率 ASR` + `检索成功率 / 命中率` + `干净精度 ACC 损失` + `额外开销（LLM 调用数 / 延迟）`。

---

## 6. 各方法计算资源估算

> **本节口径**：按文献报告的**核心集**——攻击族 A1–A17（对应 31 篇）与防御族 D1–D18（对应 22 篇）——逐项估算，共 53 个方法（§6.5）。除核心集外，§9 综述补充的约 20 篇方法（ProGRank、CleanBase、RAGuard、Cordon-MAS、RAGSieve、ContextCite、TracLLM、AttnTrace、SDAG、RAGShield、AV Filter 等）为**扩展集**，其在 `baselines/` 中的载体见 §1.7；§6.2–§6.3 的“调用次数 / 开销等级”为**依机理推算的估算**，§6.4 另列出文献报告 §7.7 已**实测**的原文开销作为实证参照。

### 6.1 统一成本模型

| 成本项 | 单位 | 实测/估算依据 |
|---|---|---|
| **检索复算**（缓存路径） | < 1 s / 格（100 题） | §3.3 |
| **检索重算**（全库） | HotpotQA @256 ≈ 2.06 TB 读/100 题 | §3.3 |
| **载荷编码** | ≈ 70–84 K tok/s/机 | §1.6 |
| **受害者生成** | **≈ 95 题/分钟**（100 RPM 上限） | §1.6 |
| **LLM 载荷构造** | 按方法，1–数百次/题 | 见下表 |
| **GPU 梯度优化** | 按方法，白盒检索器前向/反向 | 见下表 |
| **重排打分** | cross-encoder ≈ 10³–10⁴ 对/分钟（GPU） | 估算 |

### 6.2 攻击方法资源表

单位：下表按**对 300 题（100/数据集）执行一轮**给出调用量级。表中"LLM 调用"仅指**攻击构造侧额外调用**，不含受害者生成（后者统一为 300 次/轮）。

| 方法 | 载荷构造机理 | 攻击构造侧额外 LLM 调用（300 题） | GPU 开销 | 检索路径 | 磁盘增量 |
|---|---|---:|---|---|---|
| **corpus-poisoning** | 梯度 + HotFlip，本地优化 | 0 | 中（梯度迭代，百～千次前向） | 缓存 ✅ | < 1 MB |
| **GASLITE** | 梯度候选 + 搜索，本地 | 0 | 中高 | 缓存 ✅ | < 1 MB |
| **OTRB** | CEM 采样迭代，本地 | 0 | 中 | 缓存 ✅ | < 1 MB |
| **Phantom** | 本地 HotFlip（Contriever，16 epochs） | 0 | 中（文档记录为 MS MARCO 16 epochs） | 缓存 ✅ | < 1 MB |
| **HijackRAG** | HotFlip 启发的梯度优化 | 0 | 中 | 缓存 ✅ | < 1 MB |
| **GARAG** | 遗传算法 + 词替换 | 低（词替换可离线查表） | 中 | 局部重算 ✅ | 忽略 |
| **Joint-GCG** | **双白盒梯度**（检索器 + 生成器）**构造**载荷 | 0 | **高**（27B 反向） | 缓存 ✅ | 忽略 |
| **TrojanRAG** | 教师 LLM 生成 + **训练并分发检索器**（对比学习） | 中 | **高（训练）** | ❌ 需重建索引 | 模型权重 |
| **SilentRetrieval** | CBS 束搜索 + CATG 触发词 | 0（本地模型） | 中高 | 缓存 ✅ | < 1 MB |
| **P3A** | p2a：LLM 生成伪证据；p3a：字符扰动 | ≈ 300（1/题） | 低 | 局部重算 ✅ | 忽略 |
| **CorruptRAG** | LLM 生成单篇伪证据 | ≈ 300 | 低 | 缓存 ✅ | < 1 MB |
| **PoisonedRAG** | LLM 生成 N 篇伪证据（黑盒）/ HotFlip 前缀（白盒） | **≈ 1,500**（5/题） | 中（白盒） | 缓存 ✅ | < 1 MB |
| **AuthChain** | LLM 抽取实体-意图-关系并构造权威链 | ≈ 900–1,500（3–5/题） | 低 | 缓存 ✅ | < 1 MB |
| **Topic-FlipRAG** | LLM 语义级扰动 + 对抗排名 | ≈ 900（3/题） | 中 | 缓存 ✅ | < 1 MB |
| **MIRAGE** | 合成查询分布 + 语义锚定 + **对抗 TPO 偏好优化**（严格黑盒、查询无关） | 中（合成查询簇，无受害者反馈；TPO 迭代用代理信号） | 中高（偏好优化，原文全部实验在**单张 H200**） | 缓存 ✅ | < 1 MB |
| **FlippedRAG** | 上下文泄露**模仿黑盒检索器**（枚举查询/候选 + 对比学习）+ 触发器成对损失优化 | 中（模仿训练需在黑盒系统上枚举查询与候选） | 中（对比学习训练替代检索器） | 缓存 ✅ | < 1 MB |
| **ToxicRAG** | 四阶段叙事构造（参考答案→目标答案→叙事要素→文档修订）+ **答案导向自校验循环** | ≈ 600–1,200（2–4/题，含自校验多轮） | 低 | 缓存 ✅ | < 1 MB |
| **CatPoison** | 黑盒优化（按类别，非按题） | 按类别数，**远少于按题** | 中 | 缓存 ✅ | < 1 MB |
| **Human-Imperceptible** | LLM 生成"正确但误导"文档 | ≈ 300 | 低 | 局部重算 ✅ | 忽略 |
| **Poison-RAG** | LLM 生成 item tag（推荐场景） | 按 item 数 | 低 | 需新检索器 | 忽略 |
| **BadRAG** | 复用既有文档 + 语义触发器 | **0** | 低 | 缓存 ✅ | < 1 MB |
| **Micro-Collaborative** | 弱信号分散注入 | 低 | 低 | 缓存 ✅ | < 1 MB |
| **InceptionRAG** | **ZOSO 零阶优化**：需**受害者响应反馈**迭代 | **≈ 5,000–20,000**（50–200/题） | 中 | 缓存 ✅ | < 1 MB |
| **SIREN** | **PAIR 越狱循环** + 活体 web 回放 | **≈ 2,500–7,500**（含 124 次试验协议） | 低 | 需活体检索 | — |
| **ReGENT** | **强化学习循环**（相关性-生成-自然度奖励） | **高（RL 采样）** | 中 | 局部重算 ✅ | 忽略 |
| **A16・GenADV**（Toward Robust RALMs） | 用生成模型批量构造**引开注意力**的对抗文档 | ≈ 300–900（1–3/题） | 低 | 缓存 ✅ | < 1 MB |
| **A16・MedMisBench** | 生成**形式化规则式**误导上下文（不伪造具体答案） | ≈ 300（1/题） | 低 | 缓存 ✅ | < 1 MB |
| **CamoDocs** | 良性/对抗子文档**分别切块** + 梯度引导的**分散 token** 替换 + 困惑度（连贯性）重排 | 中（每目标需合成器 LLM 生成草稿；离线构造） | 中（原文用 **1× A6000 48 GB**；**每篇 ≈ 3.22 min**，每目标 β=10 篇） | 缓存 ✅ | 约 1,000 篇/目标（正文档） |
| **DenialRAG** | 两阶段内容构造（特征抽取 → 四段式段落：断言 Y → 织入实体 → **否定 X 并给理由** → 收尾权威）+ 表层词校验 | **≈ 600**（2/题，无迭代反馈） | 低 | 缓存 ✅ | < 1 MB（每目标 1 篇 ≤100 词） |
| **AdversarialCoT（A17）** | 攻方智能体读回模型输出与推理轨迹，据此改写**伪推理链**；相关性/说服力双维度反馈优化 | **中高（需读回受害者输出）**：每查询最多 **3 轮**交互（每轮 1 次受害调用 + 若干攻方调用） | 低（无梯度；成本在 API/交互轮次） | 缓存 ✅ | < 1 MB（单篇） |

**看要点**：

1. **"零额外 LLM 调用"的方法占比过半**（梯度/HotFlip/CEM/遗传类），它们的成本是**本地 GPU 前向**，可控。
2. **迭代式攻击是唯一的量级杀手**：InceptionRAG（ZOSO）、SIREN（PAIR）、ReGENT（RL）每题的 LLM/受害者调用是普通方法的 **50–200 倍**。按 95 题/分钟计，20,000 次调用 ≈ **3.5 小时**（单进程）；若按题串行无并行，规模更大。
3. **MIRAGE 与 FlippedRAG 属另一类**：它们**不依赖受害者查询反馈**，但需在本地做**偏好优化 / 对比学习训练**（MIRAGE 原文全部实验在**单张 H200** 上完成，并把“TPO 迭代的高计算成本”列为第一项局限；FlippedRAG 需先黑盒模仿出替代检索器）。因此二者**不吃 100 RPM 的生成配额，瓶颈在 GPU 而非 API**。
4. **PoisonedRAG 类“每问 N 篇”的构造是次要量级**：1,500 次调用 ≈ **16 分钟**。
5. **新增的 A17 与 CamoDocs 各代表一种新开销形态**：**CamoDocs** 是**离线几何优化**（单卡 A6000，每篇 ≈ 3.22 min，不增加受害者推理延迟）；**AdversarialCoT** 是**决策式黑盒的多轮交互**（每查询最多 3 轮），成本以**受害者/攻方调用次数**计，而非 GPU —— 两者都**不吃本地 GPU 梯度预算**。

### 6.3 防御方法资源表

单位同上（300 题/轮）。"额外生成"= 受害者 LLM 的**倍增系数**（1.0 = 与干净基线相同）。

| 方法 | 防线阶段 | 额外 LLM 生成（倍数） | 额外 GPU/模型（**本地是否已具备**） | 备注 |
|---|---|---:|---|---|
| **GMTP** | 检索后 | **1.0** | MLM 推理：**✅ `electra-base` / `gpt2` 已有** | 需检索器相似度梯度 |
| **CEG-RAG** | 检索后 | **1.0** | cross-encoder：**✅ 5 个候选已有** | 多示例学习检测 + 定位 |
| **RAGDefender** | 检索后 | **1.0** | 轻量 ML：✅ | 无需额外训练 |
| **GRADA** | 检索中 | **1.0** | 图重排：✅ 仅 embedding | 需良性文档弱相似性信号 |
| **ShieldRAG** | 检索中 | **1.0** | ✅ | 嵌入空间重塑 |
| **RAGPart / RAGMask** | 检索期 | **1.0** | ✅ 仅检索器 | 分片稀释 + 掩码偏移 |
| **ProGRank** | 检索期 | **1.0** | ✅ 仅检索器梯度 | 探针梯度信噪比 |
| **CleanBase** | 检索后 | **1.0** | ⚠️ 需 kNN 图（FAISS ✅） | 团检测 |
| **RAGRank** | 检索前/中 | **1.0** | ✅ | PageRank 类来源可信度图 |
| **AttnTrace** | 溯源 | **1.0** | ⚠️ 需注意力输出 | 需白盒 LLM |
| **ContextCite** | 溯源 | **1.0** | ✅ | 多次消融采样（推理期开销高） |
| **TracLLM** | 溯源 | **1.0** | ✅ | 贡献分数集成 |
| **TrustRAG** | 检索前 | **2.0** | ✅ | 自评估多一次生成 |
| **SeCon-RAG** | 检索期 | **2.0** | EIRE 抽取器（需 LLM） | 两阶段过滤 |
| **AV Filter** | 生成前 | **1.0** | ⚠️ 需段落级注意力方差 | 上游 `Stealthy_Attacks_Against_RAG` 已就位 |
| **SDAG** | 生成时 | **1.0** | ⚠️ 需改注意力实现 | 稀疏文档注意力 |
| **RAGSieve** | 溯源/检测 | **1.5** | ✅ | 查询期 + 语料期双对照 |
| **BRIDGE** | 生成前 | **2.0** | ✅ | 决策树选择策略 |
| **CARE-RAG** | 生成前 | **2.0** | 蒸馏 3B 模型（需下载） | 冲突驱动摘要 |
| **Astute RAG** | 生成前 | **2–3** | ✅ | 内外部知识迭代整合 |
| **RAGuard** | 生成后 | **2.0** | ✅ | LOO 分层 + ZKIP 过滤 |
| **Cordon-MAS** | 生成后 | **2.0** | ✅ | Auditor + Gate |
| **RAGOrigin** | 溯源 | **5–20** | ✅ | 迭代聚类剪枝 |
| **RAGForensics** | 溯源（后验取证） | **5–20** | ✅ | 迭代"检索—判定—剔除"，逐条定位毒文本并交服务方处置；DACC **97.4–99.6%**、FPR **0.4–2.7%**（WWW 2025，本地未收录） |
| **RobustRAG** | 生成时 | **5–6** | ✅ | 隔离-聚合（k′ 组 + 聚合） |
| **PRA-RAG** | 生成时 | **5–6** | ✅ | 鲁棒子集采样 + 聚合 |
| **ReliabilityRAG** | 生成时 | **5–6** | ✅ | 同族可证明聚合 |
| **PIShield** | 输入侧 | **1.0** | 需指令微调 LLM 前向（残差流） | 线性分类器，不生成 |
| **indirect-pia-detection** | 输入侧 | **1.0** | ✅ 已训练分类器 | 上游已 clone |
| **TRIS** | 检索期（三层纵深） | **1.0**（L3 另需一次 LLM 一致性校验，非生成） | ✅ 独立判官嵌入模型（本地已有多个）+ 结构过滤；L3 需 LLM | 上游 `defenses/tris` 已就位；**L1 ≈13 ms、L2 ≈8 ms、默认 L1+L2 ≈0.35 s/查询；L3 ≈16–19 s/查询**（原文 §6.7 实测） |
| **DeRAG** | 架构层 | **1.0** | ⚠️ 需区块链/DHT 环境 | 吞吐 78 k qps（论文值） |

**看要点**：

1. **防御侧的分层特征**：**多数防御不增加生成次数**（检测/过滤/重排/溯源类，含 GMTP、CEG-RAG、RAGDefender、GRADA、ShieldRAG、RAGPart、ProGRank、CleanBase、RAGRank、TRIS 等），成本集中在一次额外前向或一次 cross-encoder 打分——**计算量小，且所需模型基本已在本地**（§1.5）。
2. **可证明鲁棒族（RobustRAG / PRA-RAG / ReliabilityRAG）是生成侧最贵的**：5–6 倍生成。300 题 × 4 档 × 3 数据集的单轮，从 3,600 次生成膨胀到 18,000–21,600 次 → 约 **3.2–3.8 小时**（按 95 题/分钟）。
3. **溯源族（RAGOrigin / RAGForensics）是迭代最贵的**：5–20 倍。这正对应文献报告 §5.2 缺口 6 的判断——"RAGOrigin 是少数事后溯源工作，但仍是黑盒启发式，缺乏理论保障"：**当前用迭代聚类换取精度，代价是线性增长的 LLM 预算**，这也是该方向可出增量贡献的地方。

### 6.4 文献侧已实测开销（引自文献报告 §7.7）

文献报告 §7.7 汇总了各原文**自报**的开销。下表只摘录可直接用于本复现排期的条目，用于**校验 §6.2–§6.3 估算的量级**；这些数值来自各自论文的语料与设定，**不可直接换算到本仓库**。表中每一行已回到 `docs/papers/` 的**原文 PDF 逐条核对**（数值均为原文自报）。

| 类型 | 方法 | 原文实测开销 | 对本方案的含义 |
|---|---|---|---|
| 训练 | **BRIDGE** | **8×H100（80 GB）** 训 Llama3-8B-Instruct（LoRA r=16, α=32） | 训练类方法（BRIDGE、TrojanRAG）无法在 dancher-01/03 上复现，须改用预训练或蒸馏产物 |
| 优化 | **PoisonedRAG** | 白盒**每毒文本 ≈26 s**（NQ 26.12 / HotpotQA 26.01 / MS-MARCO 25.88）；黑盒启发式 **≈1.45×10⁻⁶ s** | 与 §6.2「每问 5 篇」自洽：300 题 × 5 × 26 s ≈ **10.8 h**（单机） |
| 优化 | **InceptionRAG** | **ZOSO 234.1 min** vs 穷举 **6,621.5 min**（**28.3× 加速**） | 印证 §6.2 中 ZOSO 是主要成本项；若无此加速，复现不可行 |
| 优化 | **MIRAGE** | 全部实验跑在**单张 H200**；每数据集 **1,000 次独立试验**、每次仅注入 **1 篇**；作者把“TPO 迭代的高计算成本”列为第一项局限 | 与 §6.2「MIRAGE 瓶颈在 GPU 而非 API」一致；H200 不可得时需用 H100/A100 外推 |
| 优化 | **FlippedRAG** | 平均攻击成功率较基线 **+16.7**、观点极性**方向性偏移约 50%**、**约 20% 受试用户认知被带动** | 需先在黑盒系统上枚举查询/候选训练替代检索器；复现成本主要在**模仿阶段** |
| 优化 | **CamoDocs** | 每篇对抗文档 **≈3.22 min**（单卡 **A6000 48 GB**）；β=**10 篇/目标查询**、投毒率 **0.019% / 0.037% / 0.011%**（HotpotQA/NQ/MS-MARCO）；**不增加受害者推理延迟** | 与 MIRAGE 同为“离线几何优化”型（GPU 主导）；**每目标 10 篇 × 3.22 min 使构造成本随目标数线性放大** |
| 优化 | **DenialRAG** | 离线**2 次 LLM 调用**产出 1 篇 **≤100 词**文档（无反馈迭代）；Mistral-7B 上三集 ASR **89 / 94 / 86%**；消融去掉“否认”降 **17.1 pp**、成本档→前沿档降 **−30.3 pp（83.5%→53.2%）** | 属“最轻构造”端（与 CorruptRAG 同量级），适合放第一批 |
| 交互 | **AdversarialCoT** | 每查询最多 **3 轮**黑盒交互（攻方智能体 **KIMI-K2**）；MS-MARCO/NQ/HotpotQA 各 **100 查询**、top-5、Co-Condenser；迭代后 ASR **59–80%**，较基线**最高提升 23%** | 成本以**交互轮次数**计而非 GPU；属§6.2“需读回输出者”一类 |
| 推理延迟 | **TRIS** | **L1 ≈13 ms、L2 ≈8 ms/查询**（默认 L1+L2 ≈**0.35 s**/查询）；**L3 使延迟升至 ≈16–19 s/查询**（always-on ≈15 s） | L1+L2 可全量常开；L3 必须按需触发（自适应模式只在 L1/L2 分歧时点火，约占 HotpotQA 查询的 21%） |
| 推理延迟 | **SilentRetrieval** | 组合防御 **6×** 延迟（ASR-LLM 25.6%）、最强防御 **11×**（21.3%） | 与 §6.3 的倍增假设同量级 |
| 推理延迟 | **RADE** | **3.9×** 延迟（顺序单卡 **3.91 s** vs Vanilla RAG **1.00 s**；双卡调度降至 3.24 s） | 属 §6.3「生成倍增族」的轻端 |
| 推理延迟 | **GMTP** | 比**生成期**防御基线**低约 80% 平均延迟**（另比 PPL 低约 20%） | 支持"检测类优先、生成类靠后"的批次划分（§8.1） |
| 端到端 | **RAGDefender** | **仅 CPU** | 无需 GPU，在本机（§1.6，无可用 GPU）仍可跑 |
| 推理延迟 | **RobustRAG** | 原文 Table III（Mistral-7B，k=10，ω=1，单卡 A100）：**1.16–3.65×** vanilla RAG 单问延迟 | 隔离-聚合的**相对**开销可用原文实测值锚定（远低于 ×k） |
| 端到端 | **SeCon-RAG / TrustRAG / Astute RAG** | SeCon-RAG 论文报告 NQ + 100% 投毒下单问 **1.06 min**，较 TrustRAG **0.67**、AstuteRAG **0.70** 仅慢约 10 s；SeCon-RAG 自身批运行 **1.21–1.45 min** | 冲突感知族之间成本接近（同为一次以上额外生成） |
| 成本对照 | **RAGDefender（对比 ROBUSTRAG）** | RAGDefender 论文的对照表：**ROBUSTRAG 每问成本 $1.22（Vicuna-7B）～ $59.00（GPT-4o）** | 可证明鲁棒族与轻量检测族的成本差可达两个数量级；**注**：此 `$` 值为 RAGDefender 论文的对照值，非 RobustRAG 原文自报 |
| API 费用 | **Benchmarking (RSB)** | NQ 跑一次 BPRAG ≈**$10**（GPT-4o-mini）/ **$390**（GPT-4）；15 数据集合计 ≈**$150** vs **$5,850**（GPT-4）/ **$1,440**（GPT-4.1） | 与 §6.5「LLM 调用数为主要瓶颈」一致；预算需按判定模型分档 |
| 系统吞吐 | **DeRAG** | 节点 100→10,000 时延迟 **52→256 ms**，报告 **78,000 qps** | 架构类方法，本方案仅做概念对照（§7） |

> **与 §6.5 的分工**：本节是**原文自报值**，§6.5 是**在本仓库 300 题 × 12 格设定下的推算**；两者不可混用。排期以 §6.5 为准，本节用于**校验量级**——例如 InceptionRAG 单次优化 234 min 与 §6.5「迭代式攻击 10–25 h」同量级。

### 6.5 全量矩阵的单轮总量估算

**矩阵定义**：文献报告核心集为 17 个攻击族（A1–A17，对应 31 篇）+ 18 个防御族（D1–D18，对应 22 篇），共 **53 个方法**；连同 §9 综述补充的扩展集，适配项合计约 56 条。按每方法覆盖 **3 数据集 × 4 档 = 12 格**、每格 **100 题**计：

| 成本项 | 计算 | 估算 |
|---|---|---|
| 受害者生成（干净基线） | 12 格 × 100 题 = 1,200 次 | ≈ 13 min |
| 受害者生成（31 个攻击，1.0×） | 31 × 12 × 100 = 37,200 次 | **≈ 6.5 h** |
| 受害者生成（22 个防御，平均 1.8×） | 22 × 12 × 100 × 1.8 = 47,520 次 | **≈ 8.3 h** |
| **受害者生成小计** | **≈ 85,920 次**（95 题/min） | **≈ 15.1 h** |
| 攻击构造侧 LLM（迭代式 4 个方法主导） | InceptionRAG + SIREN + ReGENT + **AdversarialCoT** | **≈ 10–25 h** |
| 攻击构造侧 GPU（无受害者反馈的训练类） | MIRAGE（对抗 TPO）、FlippedRAG（模仿训练）、**CamoDocs（分散 token 优化）** | **≈ 15–40 h（单卡 H200/A6000）** |
| 载荷编码 | 53 方法 × 300 题 × 5 篇 × 300 tok ≈ 23.9 M tok | **≈ 5 min**（70 K tok/s） |
| 检索复算（缓存路径） | 53 × 12 格 × < 1 s | **< 10 min** |
| 重排打分（重排相关约 8 个方法） | 8 × 12 × 100 题 × 100 候选 = 96 万对 | **≈ 0.5–2 h（GPU）** |
| **索引重建（仅 TrojanRAG）** | 1 方法 × 3 数据集 全库重编码 | **≈ 10 h（双机）** |
| **载荷构造白盒开销（Joint-GCG）** | 27B 检索器+生成器双阶段反向 | **≈ 5–15 h（GPU）** |

**读法**：

- 排除迭代式攻击与索引重建，全矩阵**单轮约 17–22 小时**，其中 **受害者生成占 15.1 小时且完全受 100 RPM 客户端配额支配**（GPU 远未饱和）。提高 `RPM_PARALLEL` 或并行多端点可近似线性压缩这 15.1 小时。
- **迭代式攻击（4 个）与需索引重建/双白盒/本地训练的方法（TrojanRAG + Joint-GCG + MIRAGE + FlippedRAG + CamoDocs）合计 30–60 小时**，占总量 60% 以上——这正是 §8.1 建议把它们放入第三批的原因。

---

## 7. 瓶颈、风险与不适用项

| 编号 | 风险 | 严重度 | 依据与缓解 |
|---|---|---|---|
| R1 | **磁盘余量仅 138 GB**，HotpotQA 四档重建需 417 GB | 🔴 高 | 走 §3 增量路径（注入分片 < 1 MB）；若必须重建，需先归档或降档（如只保留 256/512） |
| R2 | **本机无可用 GPU**（M40 12 GB 且无 FP16 张量核） | 🔴 高 | 编码/生成必须走 dancher-01/03；本机仅做调度与报告 |
| R3 | **生成受 100 RPM 客户端限速**，非 GPU 限速 | 🟡 中 | 迭代式攻击（InceptionRAG/SIREN/ReGENT）的总时长由该配额决定；可提高 `RPM_PARALLEL` 或用多端点 |
| R4 | 现役协议 **无 reranker**，与 CRCP/P3A/CEG-RAG 的设定不符 | 🟡 中 | 需补重排阶段（本地已有 5 个 cross-encoder 候选） |
| R5 | **语料来源差异**导致跨文献 ASR 不可直接比较（文献 §7.1：同一攻击在 Security SE 38%、FEVER 0%） | 🟡 中 | 统一复现恰好解决此问题——这正是本方案的价值所在；报告须固定语料层与分母 |
| R6 | 定向投毒**不区分优化集与测试集**（文献 §7.3 E3，81 篇中仅 6 篇严格隔离） | 🟡 中 | 复现时对每方法标注"是否 held-out"，避免把 ASR 解读为泛化能力（ToxicRAG、FlippedRAG、CamoDocs、DenialRAG、AdversarialCoT 均未隔离） |
| R7 | **投毒率分母不统一**（文献 E6：500 段落 ～ 2,101 万段落） | 🟡 中 | 统一以"占 `manifest.document_count` 比例"报告 |
| R8 | TrojanRAG **需训练并重建检索器**；Joint-GCG **需双白盒梯度**（构造期） | 🟡 中 | 两者性质不同：前者是索引重建，后者是构造开销；均单独排期，不与增量路径混跑 |
| R9 | 部分方法依赖**外部 API**（GPT-4o 判分、活体 web） | 🟢 低 | 文献 §7.2 已指出多数"白盒"实为本地影子系统；本地 27B 可替代大部分 |
| R10 | **本机 15 GB RAM**：缓存 `screening.jsonl`（约 30 MB）与向量可放下；但 top-1000 归并需注意驻留 | 🟢 低 | 按题流式处理 |

**明确不适用/需降级的项**：

- **活体网络类**（SIREN 的 Claude web tools）：无法在封闭语料上复现，需降级为离线快照或排除。
- **推荐系统类**（Poison-RAG，MovieLens）：语料与任务均不同，需独立小规模环境。
- **架构级去中心化**（DeRAG）：需区块链/DHT 环境，建议只做概念对照而非性能复现。
- **多模态 RAG**：现役索引仅文本，不覆盖。

---

## 8. 实施建议

### 8.1 分三批推进

| 批次 | 范围 | 方法数 | 理由 | 预估 |
|---|---|---:|---|---|
| **第一批** | 追加式攻击（corpus-poisoning、GASLITE、OTRB、Phantom、HijackRAG、BadRAG、PoisonedRAG、CorruptRAG、AuthChain、CatPoison、Topic-FlipRAG、Micro-Collaborative、ToxicRAG、**DenialRAG**、**A16 的 GenADV 与 MedMisBench**）× 过滤/检测式防御（GMTP、CEG-RAG、RAGDefender、GRADA、ShieldRAG、RAGRank、TrustRAG、CleanBase、RAGPart/RAGMask、ProGRank、**TRIS（L1+L2）**） | **≈ 27** | 全部走 §3 缓存路径，无索引重建；防御侧不增生成或仅增 1 次 | 以编排框架 + 适配层为主，**单轮 ≈ 5 h** |
| **第二批** | 需重排阶段的方法（P3A、CRCP、SilentRetrieval、GARAG、Human-Imperceptible） + 生成倍增族（RobustRAG、PRA-RAG、ReliabilityRAG、Astute RAG、CARE-RAG、BRIDGE、RAGuard、Cordon-MAS） + 溯源族（RAGOrigin、RAGForensics、ContextCite、TracLLM、AttnTrace、RAGSieve） | **≈ 19** | 需补 G2 重排阶段与 G4 多阶段编排 | **单轮 ≈ 8–10 h**（生成倍增主导） |
| **第三批** | 迭代式攻击（InceptionRAG、SIREN、ReGENT、**AdversarialCoT**） + 需重建检索器者（TrojanRAG） + 需双白盒梯度者（Joint-GCG） + 严格黑盒但需本地偏好/模仿/几何优化者（**MIRAGE、FlippedRAG、CamoDocs**） | **≈ 9** | 成本量级最高（GPU/交互轮次主导，非批量 API 主导），需独立预算与排期 | **单轮 ≈ 35–60 h** |

> 批次划分依据是**单轮成本量级**而非难度：第一批 27 个方法的合计成本低于第三批任一个迭代式攻击。§9 综述补充的扩展集方法（ProGRank、CleanBase、RAGuard、Cordon-MAS、RAGSieve、ContextCite、TracLLM、AttnTrace、SDAG、RAGShield、AV Filter 等）已按相同口径并入上述批次。

### 8.2 八条硬性记录要求（直接采用文献报告 §10 第 5 条的"实验设计自查项"）

1. 语料必须交代到物理形态（原始 dump / BEIR 加工版 / 扩展版）与**分母段落数**；
2. "白盒"必须说明是目标系统还是本地影子系统，并报**跨检索器迁移率**；
3. 明确优化集与测试集**是否隔离**；
4. 报告问题集确定方式与筛选条件（含随机种子 / 置信区间）；
5. **同时报告字符串匹配与 LLM-judge 两套 ASR**，并区分检索侧命中率与生成侧采纳率；
6. 防御须报 **ACC + ASR 成对结果**并给出延迟/开销，以体现效用—安全—成本三方权衡；
7. 报告 **ACC 须声明三个口径**：① 是攻击条件还是干净条件（ACC vs CACC）；② 分母是全部查询还是仅目标查询；③ 分子是子串包含还是须校验证据。并建议额外报告 **$1-(ACC+ASR)$ 缺口率**，以区分"被攻击成功"与"过度过滤导致答不出"；
8. 报告 **ASR 须声明四个口径**：① 判定协议（substring / LLM-judge / ASR-LLM / 关键词占比 / 排序）；② 分母（全部查询 / 仅目标查询 / 排除性净增益 / 非查询单位）；③ 立场（攻方 raw ASR / 守方 residual ASR）；④ 同时给出 baseline 与 defended 的**绝对值**（否则"降幅 88.8%"无法复算）。

> **补充（针对新增的 A17 与几何规避类）**：对**推理模型类**攻击（A17 AdversarialCoT）须额外声明 **① 推理侧是否纳入判定**（原文用 $\mathrm{ASR}_r \times \mathrm{ASR}_g = \mathrm{ASR}$，即检索侧与生成侧分别计后再合取）、**② 交互预算**（最多几轮、每轮代价）、**③ 是否逐条人工核验**（原文对全部结果人工核验成败）；对**多信号规避类**（CamoDocs）须额外声明 **④ 被规避的防御信号清单**及其阈值（原文扫描了 7 种防御、并给出 TrustRAG 阈值 0.10→0.99 的全扫描），以及 **⑤ 规避的效用代价**（原文报告 TrustRAG 剔除 **91.48%** 检索文档、干净准确率 **29.13%→5.79%**）。

### 8.3 立即可做的三件事

1. **固化缓存清单**：为 `screening.jsonl` / `query_vectors.npy` / `search/*.npz` 生成 SHA256 清单（`protocol.json` 已有部分），防止后续实验误改分母。
2. **写 `src/attack/index_overlay.py`**：实现 §3 的"缓存背景 + 注入向量归并"，这是解锁第一批 27 个方法的最小可用组件。
3. **补 LLM-judge 判分**（G5）：文献 §7.5 明确指出单一判定口径会带来偏差，且实现量小。

---

## 附录 A：本报告全部实测数据来源

| 数据 | 来源文件 |
|---|---|
| 索引体积、块数、分片数 | `/mnt/sdb1/ragshield_protocol_v2/*/documents_*/`、各 `poc/manifest.json` |
| 抽样题数、五类分层配额 | 各 `poc/queries.jsonl`、`poc/sampling.json` |
| screening 400 行 × 1000 深度 | `results/contriever_protocol_v2_20260925/clean_*/screening.jsonl` |
| query 向量形状 | 各 `query_vectors.npy`（`np.load(mmap_mode='r')`） |
| Top-5 记录字段 | `results/full_clean_top5_20260927/nq/retrieval.jsonl` |
| 编码吞吐 | `results/contriever_protocol_v2_20260925/throughput_tuning.md`、`throughput_update_20260926.md`、`eta_update_latest.md`、`results/full_dev_20260924/throughput_rebalance.json` |
| 分片规格（4 M tokens/片、@512 27.6 s、56.7 MB） | `/mnt/sdb1/ragshield_protocol_v2/hotpotqa/documents_512/shards.json` |
| 生成吞吐与最终 ACC | `results/full_clean_top5_20260927/progress.json`、`report.md`、`nq/generation_protocol.json`、`backend.json` |
| 硬件与磁盘 | `nvidia-smi`、`nproc`、`free -g`、`df -h` |
| 本地模型清单 | `/mnt/sdc2/models`（`du -sh`） |
| baselines 清单与版本 | `.gitmodules`、各 submodule 的 gitlink 与 HEAD、`baselines/README.md` |
| 文献侧开销实测（§6.4） | `docs/RAG安全文献攻防技术手段总结报告.md` §7.7（逐篇原文自报值，已在 `docs/papers/` 原文 PDF 逐条核对） |

**估算声明**：本报告的数字分三层，不可混用——①**本机实测**：§1 全部资产、§6.1 的检索/编码/生成吞吐；②**文献原文自报**：§6.4 全部数据（引自文献报告 §7.7 并经 `docs/papers/` 原文 PDF 逐条核对，非本机实测，不可直接换算到本仓库语料）；③**基于机理的估算**：§6.2 / §6.3 的"额外 LLM 调用次数""GPU 开销等级""重排打分耗时"，以及 §6.5 的总量（其中干净基线生成、受害者生成、载荷编码、检索复算四项**基于 ① 的实测吞吐推算**）。所有涉及具体方法的机理描述引自 `docs/RAG安全文献攻防技术手段总结报告.md` 第二、三、六章，口径与统计定义（ACC/ASR 分子分母、机理实验分布、设置与开销）见其 §7，优先级评定见其 §8，综述补充文献见其 §9，低优先级邻域文献见其 §6.8。

---

*报告生成：基于 SEU_Graduation_Design 现役代码与数据的静态盘点（12 套索引、967 个分片、300 抽样题、400×4 条 screening 记录、模型动物园 18 个本地模型）+ 已归档吞吐记录的再计算。未执行任何对现有索引的写操作；未运行任何攻防实验。*
