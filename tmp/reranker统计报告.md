# reranker 涉及情况统计报告

**统计日期**：2026-10-06（第二版，覆盖最新文献集）
**统计脚本**：`tmp/scan_reranker.py`（全文扫描）、`tmp/check_reranker_context.py`（边界复核）、`tmp/dump_ctx2.py` / `tmp/dump_ctx3.py`（命中上下文导出）、`tmp/judge_hits.py` / `tmp/judge_regent.py`（边界判定）
**原始输出**：`tmp/reranker_scan.txt`、`tmp/reranker_context_check.txt`、`tmp/reranker_ctx2.txt`、`tmp/reranker_ctx3.txt`、`tmp/reranker_judge.txt`、`tmp/regent_ctx.txt`

---

## 一、统计口径

| 项目 | 说明 |
|------|------|
| **匹配模式** | `\bre[\s-]?rank`（覆盖 rerank / re-rank / reranker / reranking），附加 `cross-encoder` 作为强相关信号；中文侧附加 `重排`、`重排序`、`二次排序` |
| **判定方式** | **全文扫描**（非仅摘要），逐 PDF 提取文本后正则匹配，再对全部命中做**上下文复核** |
| **A 组** | `RAG安全文献` 目录下 **83 个 PDF** → 去重后 **81 篇独立文献**（剔除 2 个附录工件：*Topic-FlipRAG_appendix* 与 *[With Appendix]PoisonedRAG*，重复副本已清理） |
| **B 组** | 三篇综述联网补充的 **20 篇**原文 |
| **去重后总范围** | **100 篇独立文献**（A 组 81 篇 + B 组 20 篇，其中 1 篇与 A 组重叠 → 19 篇新增） |

> **正则修正说明**：初版 `re[\s-]?rank` 会把 "a**re rank**ed"（如 "documents are ranked by similarity"）误判为命中，产生 3 篇假阳性。加入前置词界 `\b` 后修正。

---

## 二、统计结果概览

| 结果 | A 组（83 个 PDF） | B 组（20 篇原文） | 去重合计 |
|------|------------------|------------------|----------|
| **命中 reranker** | 37 个文件（→ **37 篇**） | 5 篇（→ **4 篇新增**） | **41 篇** |
| **未命中** | 46 个文件（→ **44 篇**，另 2 个为附录工件） | 15 篇 | — |
| **其中"实质涉及"** | 32 篇 | 4 篇 | **36 篇** |
| **仅参考文献/背景提及（不计）** | 5 篇 | 0 篇 | 5 篇 |

**结论**：在当前统计范围 **100 篇文献**中，有 **41 篇**出现 reranker 相关表述，其中 **36 篇**为实质涉及。

> 与上一版（62 篇范围 / 26 篇命中 / 24 篇实质涉及）相比，覆盖面扩大约 61%，命中数由 26 增至 41——**新增命中主要来自 2025–2026 年新入库的文献**，说明"重排"在近一年的工作里已从可选环节变为常规评测项。

---

## 三、分级明细

### 第 1 级｜以 reranker 为核心对象（4 篇）

> 攻击专门针对重排器，或防御以重排器为主要作用点。

| # | 文献 | 类型 | 命中 | reranker 的角色 |
|---|------|------|------|-----------------|
| 1 | **Reranker Helps, but Not Enough (P3A)** | 攻击 | 99 | 论文主体：针对**重排器盲点**设计提示扰动，注入约 1% 字符级扰动以提升毒文本重排排名 |
| 2 | **When Poison Fails After Retrieval (CRCP)** | 攻击 | 90 | 论文主体：提出**分块感知、重排一致**投毒（Chunk-aware and Rerank-Consistent），解决"重排后攻击失效"问题 |
| 3 | **GRADA: Graph-based Reranking** | 防御 | 74 | 论文主体：**基于图的重排**，用文档间相似度图抑制毒段落（对比 HLATR、BGE-reranker） |
| 4 | **Defending RAG … Cross-Encoder Activation (CEG-RAG)** | 防御 | 69 | 论文主体：利用**交叉编码器重排器的内部激活**做多示例学习检测（cross-encoder 出现 18 次） |

### 第 2 级｜将 reranker 纳入攻防评估或流水线（17 篇）

> reranker 是论文评估、防御设计或多阶段流水线中的实质组成，但非唯一核心。

| # | 文献 | 类型 | 命中 | reranker 的角色 |
|---|------|------|------|-----------------|
| 5 | **SilentRetrieval** | 攻击 | 40 | 在匹配的 MiniLM-L6-v2 重排器设置下评估；讨论重排作为防御（cross-encoder 15 次） |
| 6 | **BEIR** | 基准 | 23 | 检索基准把 **re-ranking** 列为四类检索系统之一（与 lexical / sparse / dense / late-interaction 并列），并系统比较其**性能与计算成本**（*"computationally expensive models, like re-ranking models"*，cross-encoder 3 次） |
| 7 | **CamoDocs** | 攻击 | 16 | 把 **cross-encoder reranking** 列为 7 种受测防御之一，并给出关键结论：**重排对抗"查询包含"类攻击效果有限、对不含查询的 CamoDocs 更弱**（cross-encoder 4 次）；论文自身也用**连贯性重排**筛选替换 token |
| 8 | **TrustRAG** | 防御 | 15 | 报告"重排阶段后的真实投毒率"作为评估指标 |
| 9 | **SafeRAG** | 基准 | 14 | 把 **Hybrid-Rerank（bge-reranker-base）**作为 14 个受测 RAG 组件之一，发现其对某些攻击更脆弱 |
| 10 | **Topic-FlipRAG**（2 个副本） | 攻击 | 14 | 将**重排作为缓解机制**纳入考察，结论重排增强整体鲁棒性但不足以防御；并分析"引入独立重排器"对攻击的影响 |
| 11 | **RADE** | 防御 | 11 | 防御第一层即"**可靠性感知重排**（reliability-aware reranking）" |
| 12 | **Poison-RAG** | 攻击 | 10 | 把**重排后的攻击一致性**设为独立研究问题（*"RQ2: Consistency of Attacks Before and After Reranking"*），并在 cutoff=10 下报告重排前后效果 |
| 13 | **RAG Paradox（PARADOX）** | 攻击 | 9 | 把 **ListT5 重排**列为两种代表防御之一，实测本方法仍为降幅最大者——毒文档**仍被重排器判为相关** |
| 14 | **MIRAGE** | 攻击 | 8 | 将 **cross-encoder re-ranking** 作为额外检索设置复核（*"decrease in Fact-Level RSR@5 under Re-ranking"*），用于说明结论在重排下依旧成立（cross-encoder 2 次） |
| 15 | **SIREN** | 攻击 | 4 | 编辑内容需**通过检索与重排**才能生效；引文涉及"误导检索器、重排器与 LLM 评判" |
| 16 | **Overcoming the Retrieval Barrier (IPI)** | 攻击 | 3 | 评估**重排机制作为防御**，发现不足以阻止恶意文本被检索 |
| 17 | **RAGPart & RAGMask** | 防御 | 3 | 描述含 re-rank 步骤的检索流水线，防御作用在检索（重排前）阶段 |
| 18 | **RAGRank** | 防御 | 3 | **按权威度二次重排**是其核心机制（*"re-ranking by authority"*）——把 PageRank 类来源可信度直接用于重排阶段 |
| 19 | **TRIS** | 防御 | 2 | L1 层以**单一学习式信任分重排**（*"re-ranks via a single learned trust score"*），并与可选 L3 一致性重排串联 |
| 20 | **ReGENT（The Silent Saboteur）** | 攻击 | 2 | 讨论包含 **co-condenser 重排**的检索配置（*"BM25 + co-condenser reranking"*），并把"重排器"与过滤器并列为其扰动需穿越的关卡 |
| 21 | **Semantic Chameleon** | 攻防 | 1 | 混合检索组件"按精确词重叠**重排**文档" |

### 第 3 级｜综述中设有重排阶段/章节（7 篇）

| # | 文献 | 命中 | reranker 的角色 |
|---|------|------|-----------------|
| 22 | **Retrieved But Not Reliable**（综述） | 25 | 防御分类的四阶段之一**"重排阶段（rerank-stage）"**，独立成节 |
| 23 | **Towards Secure RAG**（综述） | 22 | 把"检索 → **重排**"列为流水线独立环节，并按"重排-stage"组织防御讨论（含对 GRADA 图重排的引用） |
| 24 | **Towards Trustworthy RAG**（综述） | 8 | 公平性章节讨论**重排方法**缓解检索偏差；含 LLM+LoRA 重排 |
| 25 | **大语言模型检索增强生成优化技术研究综述** | 8 | 讨论 bge-reranker 重排序、Filter-Reranker 范式、图重排 |
| 26 | **Securing RAG / SLOT**（综述） | 5 | 六阶段知识访问流水线中"**检索与重排**"为独立阶段 |
| 27 | **基于大型语言模型的检索增强生成综述（刘雪颖）** | 5 | 讨论"Filter-Reranker"范式、面向难样本的 reranker |
| 28 | **A Systematic Survey of Claim Verification**（跨域综述） | 3 | 事实验证管线中的**多阶段重排**（*"multi-stage reranking"*）与联合重排+真实性预测 |

### 第 4 级｜顺带提及（4 篇）

| # | 文献 | 命中 | 说明 |
|---|------|------|------|
| 29 | **GASLITE** | 2 | 仅提及"text re-rankers"作为检索后端之后的阶段 |
| 30 | **MS MARCO** | 2 | 数据集论文，其任务之一为"passage re-ranking" |
| 31 | **CatPoison** | 1 | 讨论缓解手段时指出"**多模型重排**可显著削弱攻击影响" |
| 32 | **Influence Factors on RAG Poisoning** | 1 | 在列举使攻击更难的因素时提到"**重排阶段**" |

### 补充｜综述联网补充文献中的新增（4 篇）

| # | 文献 | 命中 | reranker 的角色 |
|---|------|------|-----------------|
| 33 | **ProGRank** | 32 | 论文主体：**探针梯度重排**（Probe-Gradient Reranking），用检索器梯度的信噪比识别并压低毒段落 |
| 34 | **Cordon-MAS** | 2 | 信息流控制防御；讨论重排作为预处理变换会被绕过 |
| 35 | **RAGShield** | 1 | 三层纵深防御含"**信任加权重排**（Trust-weighted re-ranking，~2ms/query）" |
| 36 | **MemoryGraft** | 1 | 提出密码学溯源 + "**Constitutional Consistency Reranking**"作为缓解方向 |

---

## 四、判定为"不实质涉及"而排除的 5 篇

| 文献 | 命中 | 排除理由（经上下文复核） |
|------|------|--------------------------|
| **On the Vulnerability of RAG in Knowledge-Intensive Domains** | 1 | 唯一命中出现在**参考文献列表**（"Passage re-ranking with BERT"），正文无重排相关论述 |
| **GMTP** | 1 | 命中为**背景章节**介绍检索器类型时提及 cross-encoder（"The cross-encoder, proposed by Nogueira and Cho (2019)…"），以及参考文献；GMTP 本体基于检索器相似度梯度，不使用重排器 |
| **TrojanRAG** | 1 | 唯一命中在**参考文献列表**（"Passage re-ranking with bert"），正文未涉及重排阶段 |
| **After Retrieval, Before Generation (BRIDGE)** | 2 | 两处均为**引用/综述性罗列**（"Re2G: Retrieve, rerank, generate." 与相关工作中的 "passage rerank-"），**BRIDGE 本体不设重排模块** |
| **Astute RAG** | 2 | 两处均为**相关工作引用**（"passage reranking (Yu et al., 2024)"、"Re2g: Retrieve, rerank, generate."），正文机制不涉及重排 |

> 注：**TrojanRAG / BRIDGE / Astute RAG** 为第二版新增的排除项——三者的命中全部落在参考文献或相关工作罗列中，与正文机制无关。

---

## 五、简要观察

1. **reranker 是攻防博弈的活跃战场，且对峙已从"1 对 1"扩展为"一对多"**：第 1 级的 4 篇仍构成完整对峙——**2 篇攻**（P3A、CRCP 专攻重排器）与 **2 篇守**（GRADA、CEG-RAG 依托重排器）。但随着文献集扩大，第 2 级新增了 **5 篇把重排作为独立评测维度**的工作（BEIR、CamoDocs、Poison-RAG、RAG Paradox、MIRAGE），说明"**重排器既是防御资产也是新的攻击面**"这一双向性已被更广泛地独立确认。

2. **"把重排当防御"已成为标准做法，而"攻击者是否仍能穿透"成为新的比较维度**：CamoDocs / RAG Paradox / MIRAGE / Topic-FlipRAG / IPI 五篇**均为攻击类**，却都把重排写进了防御评估——前三者的结论一致：**重排能压低"查询包含"类攻击，但对不含查询、措辞自然的毒文档效果有限**（RAG Paradox：*"still ranked as relevant by the reranker"*；CamoDocs：*"cross-encoder reranking is less effective against…"*）。这恰好与 §5.2 缺口 3 的"信号错配"同源。

3. **中文/综述文献的重排认知普遍存在**：7 篇综述均把"重排"列为独立流水线阶段（第 3 级），其中 **Towards Secure RAG**（22 次）与 **Retrieved But Not Reliable**（25 次）更把"rerank-stage"作为**防御分类的一级轴**——说明重排已被公认为 RAG 的标准环节。

4. **防御侧存在一条"自我重排"的独立路线**：**RAGRank**（按权威度重排）、**TRIS**（学习式信任分重排）、**RADE**（可靠性感知重排）、**RAGShield**（信任加权重排）、**MemoryGraft**（一致性重排）共 5 篇**把重排器本身改造成防御组件**，而不是在重排之外再加一层检测。这条路线在上一版中仅有 2 篇（RADE、RAGShield），**本版显著扩张**。

5. **有多篇"基准"与"实用性"导向的工作完全未涉重排（值得注意）**：
   - **PoisonedRAG** —— **原始投毒奠基工作**（含 *[With Appendix]* 版本），正文完全不含重排
   - **Benchmarking Poisoning Attacks against RAG**（44 页，148K 字符）
   - **Practical Poisoning Attacks against RAG**（12 页）
   - **Certifiably Robust RAG（RobustRAG）** —— **主要防御之一，却完全不涉及重排阶段**
   - **SeCon-RAG / ToxicRAG / InceptionRAG / AdversarialCoT / DenialRAG / FlippedRAG / RAGForensics**（含 2025–2026 新入库的若干重要工作）
   
   这恰好印证了 CRCP 所指的 **"现实性鸿沟"（realism gap）**——即当前相当一部分投毒评测仍在**简化流水线**（无重排）下进行，与真实部署存在差距。值得注意的是：**本轮新增命中的文献中仅 CamoDocs、MIRAGE、RAG Paradox 三篇把重排纳入评估**，而同属新入库的 DenialRAG、AdversarialCoT、FlippedRAG、ToxicRAG、RAGForensics 等**均未涉及**——说明"补齐重排环节"仍未成为普遍惯例。

6. **统计边界提示**：`Anti-Knowledge Corruption` 为 1 页海报，仅提取到 1761 字符，其"未命中"结论的可靠性弱于其他全文论文。

---

*数据来源：全文提取 + 正则扫描，所有命中均有原始句子可溯源（见 `tmp/reranker_scan.txt`）。*

---

## 附：两次统计的口径对照

| 项目 | 第一版（2026-09-29） | 第二版（2026-10-06） |
|------|---------------------|---------------------|
| A 组 PDF 数 | 46 | **83** |
| A 组独立文献 | 43 | **81** |
| B 组原文 | 20 | 20 |
| 去重后总范围 | 约 62 篇 | **100 篇** |
| 命中 reranker | 26 篇 | **41 篇** |
| 实质涉及 | 24 篇 | **36 篇** |
| 排除（仅参考文献/背景） | 2 篇 | **5 篇** |
| 第 1 级（核心对象） | 4 篇 | 4 篇 |

> 第二版新增命中的来源可分三类：① **新入库文献**（CamoDocs、RAG Paradox、MIRAGE、BEIR、Towards Secure RAG 等）；② **既有文献的更严格复核**（Poison-RAG、RAGRank、TRIS、ReGENT、CatPoison、Influence Factors 等此前未单独列出的条目）；③ **排除项同步扩容**（TrojanRAG、BRIDGE、Astute RAG 三篇经复核确认命中全在参考文献中）。
