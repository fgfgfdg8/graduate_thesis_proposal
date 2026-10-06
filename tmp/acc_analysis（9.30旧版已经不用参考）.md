**建议参考 SecRAG 的指标实现：短答案问答同时报告 EM、答案包含匹配 ACC、token F1；事实核查使用标签 ACC。Ground Truth 优先从本地 metadata 提取，缺失部分再回原始数据集补齐。**

本次检查的是你新指定的 `New_Future/ChunkTrojan`。本文为早期源码与数据检查记录；当时代码图MCP不可用。2026-09-28已修复并重建索引；官方来源通过直接访问项目仓库核对。

**1. 其他 baseline 有没有可用的 ACC？**

有，但**同名 ACC 的判定规则和统计方式并不统一**。

| Baseline | 实际计算方式 | 是否适合参考 |
|---|---|---|
| **SecRAG / FlashRAG** | 将预测和参考答案规范化；任一参考答案是预测的子串就记 1，最终求平均。另外独立提供 EM、token F1 | **最适合作为统一实现的参考** |
| **RobustRAG** | 任一正确答案经 `clean_str` 后包含在回答中，就记正确；默认还加入 GPT 生成的 `expanded answer` | 可以复现其 ACC，但应区分原始答案和生成的别名 |
| **GARAG** | `norm_acc` 使用规范化后的子串匹配，`EM` 使用完全相等 | 评分函数可参考；汇总函数有额外条件，不能直接当通用 ACC |
| **RAGDefender / artifacts** | 正确答案包含于回答，**或回答包含于正确答案**，均算正确 | 判定偏宽，不建议直接复用 |
| **p3a / evalutate.py** | 单题采用正确答案子串匹配 | 汇总公式存在运算顺序问题 |
| **GMTP** | 用 GPT 判断回答正确与否，再统计解析出的 `yes` 比例 | 属于 LLM 判分，不能与字符串 ACC 混用 |
| **SafeRAG** | `retrieval_accuracy = (recall_gc + 1 - recall_ac) / 2` | 衡量检索结果组成，不是问答 ACC |

对应代码：

- SecRAG：[ACC / Sub_ExactMatch](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/evaluator/metrics.py:178)、[EM](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/evaluator/metrics.py:134)。规范化包括小写化、去英文标点和冠词、合并空白。
- RobustRAG：[正确性判定](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/RobustRAG/src/dataset_utils.py:42)、[扩展答案加入位置](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/RobustRAG/src/dataset_utils.py:19)。
- GARAG：[评分函数](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/GARAG/src/util.py:156)、[汇总逻辑](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/GARAG/src/task.py:14)。汇总时，仅部分满足攻击条件的样本实际评分，其余分支直接加 1。
- RAGDefender：[双向包含判定](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/RAGDefender/artifacts/main.py:332)。例如标准答案为 `New York City`，输出 `York` 也可能被算正确。
- p3a：[汇总公式](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/p3a/evalutate.py:333) 写成 `count / repeat_times * M`；若要除以总问题数，应为 `count / (repeat_times * M)`。

GMTP 的判分汇总见 [evaluation.py](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/GMTP/src/evaluation.py:98)，SafeRAG 见 [nctd_attack.py](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SafeRAG/tasks/nctd_attack.py:67)。

因此建议明确命名，避免只写一个含义不清的 `ACC`。设 \(G_i\) 为第 \(i\) 题的参考答案集合，\(y_i\) 为预测，\(n(\cdot)\) 为规范化：

\[
\mathrm{ACC_{contains}}
=\frac1N\sum_i\mathbf1[\exists g\in G_i:n(g)\text{ 是 }n(y_i)\text{ 的子串}]
\]

\[
\mathrm{EM}
=\frac1N\sum_i\mathbf1[\exists g\in G_i:n(g)=n(y_i)]
\]

事实核查则使用：

\[
\mathrm{LabelACC}
=\frac{\#\{\text{预测标签与参考标签相同}\}}{N}
\]

包含匹配容易把否定句也判对；标签任务应先解析成固定类别，再比较标签。

**2. 本地 BEIR 已经有哪些 Ground Truth？**

需要分开两类：**检索 GT 是相关文档，生成 GT 是答案或标签**。BEIR 官方加载接口返回 `corpus、queries、qrels`，检索评估使用 qrels 计算 nDCG、MAP、Recall 等，不能直接把相关文档当作短答案。[官方说明](https://github.com/beir-cellar/beir)

对你本地数据的检查结果如下：

| 数据集 | 本地可用 GT | 获取或补齐方式 |
|---|---|---|
| **hotpotqa** | 全部 97,852 条 query 的 `metadata.answer` 和 `supporting_facts` 均存在；test 为 7,405 条 | **直接提取即可** |
| **fever** | 全部 123,142 条 query 的 `metadata.label`、`evidence` 均存在；test 为 6,666 条 | **直接提取标签和证据** |
| **scifact** | 1,109 条 query 中，693 条 metadata 非空；test 300 条中有 188 条保留证据标签 | 与官方 claims 标注合并，区分有证据与无证据 |
| **nq / nq-train** | query metadata 为空；分别有 3,452 / 132,803 条 query | 回原始 NQ 或 DPR 的带答案版本匹配 |
| **msmarco** | query metadata 为空，有检索 qrels | 回 MS MARCO QA 数据，按 `query_id` 匹配 `answers` |
| **fiqa** | 有相关回答文档及 qrels | 可用相关回答全文作长答案参考，但不宜按短答案 EM 解释 |
| **arguana、quora、nfcorpus、scidocs、trec-covid** | 主要是相关性标注 | 优先保留各自检索任务，不能统一套短答案 ACC |

本地文件可直接查看：[HotpotQA queries](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/data/datasets/hotpotqa/queries.jsonl)、[FEVER queries](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/data/datasets/fever/queries.jsonl)、[SciFact queries](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/data/datasets/scifact/queries.jsonl)。

**注意 split：**`queries.jsonl` 可能包含多个 split。评估 test 时，应以 `qrels/test.tsv` 中的 query ID 筛选，不能直接评估全部 query。提取正相关文档时过滤 `score > 0`；本地 MS MARCO test 中存在 score 为 0 的行。

**3. 缺失 GT 的具体获取方案**

1. **HotpotQA、FEVER：直接从本地生成答案索引。**

   推荐记录结构：

   ```json
   {
     "query_id": "...",
     "split": "test",
     "gold_answers": ["..."],
     "gold_label": null,
     "gold_doc_ids": ["..."],
     "source": "queries.metadata",
     "annotation_type": "original"
   }
   ```

   HotpotQA 填 `gold_answers`，FEVER 填 `gold_label`；二者的证据另行保留。`gold_doc_ids` 从当前 split 的正相关 qrels 获取。

2. **SciFact：下载官方 claims，按 ID 合并。**

   来源：[SciFact 官方仓库](https://github.com/allenai/scifact)、[官方数据包](https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz)。

   **已实测：本地 `qrels/test.tsv` 的 300 个 query ID，与官方 `claims_dev.jsonl` 的 300 个 ID 全部匹配。**其中 112 条 `evidence` 为空，与本地 metadata 为空的 test 样本数量一致。

   从 `evidence[doc_id][...].label` 提取 `SUPPORT / CONTRADICT`。空证据样本按原始 SciFact 的无证据任务定义处理，不能根据“qrels 存在相关文档”就标为 SUPPORT。若你要构建三分类 ACC，需要显式规定无证据类别及标签映射。

3. **NQ：先匹配带答案版本，再补未匹配项。**

   可用来源：[DPR 官方下载配置](https://github.com/facebookresearch/DPR/blob/main/dpr/data/download_data.py)、[NQ test QA 文件](https://dl.fbaipublicfiles.com/dpr/data/retriever/nq-test.qa.csv)、[原始 Natural Questions](https://github.com/google-research-datasets/natural-questions)。

   **实际匹配结果：**DPR test QA 有 3,610 条；按问题文本精确匹配，本地 NQ 命中 **2,065 / 3,452**；进行 Unicode、大小写和标点空白归一后，命中 **2,255 / 3,452**。因此，DPR 不能直接当作本地 NQ 的完整答案集，也不能按行号对应。

   剩余项回原始 NQ 的 `question_text` 和 annotations 匹配：使用 `short_answers` 的 token span 提取答案，保留 `yes_no_answer`；`long_answer` 作为证据单独保存。`nq-train` 同样需要重新核对覆盖率。最终记录匹配成功、冲突、未匹配数量，未匹配项不能静默记错或用模型生成答案顶替。

4. **MS MARCO：按 query ID 回接 QA 标注。**

   来源：[Microsoft 官方 QA 数据说明](https://github.com/microsoft/MSMARCO-Question-Answering)。

   将本地 `_id` 与 QA 数据的 `query_id` 统一为字符串，提取人工标注的 `answers`，需要长答案时另存 `wellFormedAnswers`。官方 QA test 的正确答案不公开，所以**不能假定 BEIR 的每个 split 都能取得完整 QA 答案**；应逐 split 核对匹配覆盖率，并明确处理 `No Answer Present.`。

5. **其余检索数据集：保留检索 GT，单独设计生成任务。**

   直接从 `qrels/<split>.tsv` 获取相关文档，报告 Recall@k、nDCG@k 等。若确实需要生成质量评估，可以在原始人工回答可用时使用长答案评分；缺乏答案标注时，需要新增人工标注。LLM 根据相关文档生成的答案应标为 **synthetic / silver reference**，不能与原始人工 GT 混在一起作为“标准 ACC”。

**下一步：先打开 [HotpotQA queries.jsonl](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/data/datasets/hotpotqa/queries.jsonl)，确认 `metadata.answer`；它是目前最容易直接建立答案级 EM / ACC / F1 评估的数据集。**

**比较这些方法时，先看“植入位置”：本地实现分为新增文档入库、加入检索候选重排、直接替换上下文三类。** 它们对应的攻击能力不同，不能全部视为修改了 corpus。

以下依据当前 `New_Future/ChunkTrojan/baselines` 的代码；`attacks/`、`defenses/`、`benchmarks/`、`tools/` 为按性质划分的四类，分类依据见 [baselines/README.md](../baselines/README.md)。

| Baseline / 方法 | 对抗性载荷如何生成 | 如何植入 RAG | 主要攻击目标 |
|---|---|---|---|
| **PoisonedRAG** | LLM 生成错误答案及支持它的伪证据；黑盒模式在文段前拼接问题，白盒模式用 **HotFlip 优化检索前缀** | 将投毒文段编码，与原始 top-k 候选按相似度合并排序；主流程不改写原始 corpus 文件 | 让伪证据被检索，并诱导指定错误答案。[生成](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/PoisonedRAG/src/attack.py:81) / [植入](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/PoisonedRAG/main.py:145) |
| **corpus-poisoning** | 对训练查询做 K-means 分组，用梯度与 HotFlip 优化少量 token 序列，提高其对一组查询的相似度 | 保存对抗文段，评估时计算其分数并与干净检索结果比较，模拟新增文档 | **占据检索排名**，不直接优化指定错误答案。[实现](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/corpus-poisoning/src/attack_poison.py:114) |
| **GASLITE** | 面向查询集合或聚类中心优化通用文段；使用梯度候选 token、搜索与字符串级校验，可配置流畅度约束 | 将对抗文段的向量分数加入缓存的检索结果 | 提升少量投毒文档对大量查询的覆盖率。[生成](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/GASLITE/src/attacks/gaslite.py:15) / [植入](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/GASLITE/src/evaluate/evaluate_beir_online.py:59) |
| **OTRB** | 用 **交叉熵方法 CEM** 搜索离散 token 前缀或后缀；反复采样、按相似度选精英候选、更新采样分布；与配置的载荷正文拼接 | 生成独立 `poisoned_added_corpus.json`，检索投毒文档，再与干净结果合并评估 | 用优化后的文本提高载荷的可检索性。[生成](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/OTRB/attack.py:22) / [植入](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/OTRB/main.py:128) |
| **GARAG** | 对原本能支持正确回答的文档做拼写扰动，可加入词替换；通过遗传算法的变异、交叉、选择，联合检索与生成指标搜索 | 修改样本中的原始 context，并直接评估扰动文档；主攻击入口保存攻击结果，没有统一写回全库 | 用细微文本噪声破坏检索与回答，属于**原文篡改**。[实现](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/GARAG/src/attacker.py:376) |
| **p3a** | `p2a.py` 用 LLM 生成肯定错误答案的短段落；`p3a.py` 再用字符插入、删除、替换及 beam search，提高 **cross-encoder 重排分数** | 加载 `adv_texts`，加入检索候选，随后进入重排与生成流程 | 让伪证据同时通过检索和重排。[生成](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/p3a/p3a.py:40) / [植入](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/p3a/evalutate.py:173) |
| **GMTP 中的攻击集** | 主实验加载预生成的 **PoisonedRAG、Phantom、Adversarial Decoding** 载荷；GMTP 本身是检测方法 | 将 `poisoned_docs` 转成带独立 ID 的 corpus JSONL，单独建索引，再把干净与投毒向量合入 FAISS | **实际文档/索引级投毒**，用于验证检测效果。[文档转换](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/GMTP/convert_poisoned_dataset_to_jsonl.py:27) / [索引合并](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/GMTP/merge_index.py:18) |
| **RAGDefender / artifacts** | 复用 PoisonedRAG 式生成段落和检索优化攻击 | 将投毒候选加入 `topk_results`，按相似度排序，结合防御流程评估 | 防御实验中的攻击实现，不是另一套独立载荷生成算法。[入口](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/RAGDefender/artifacts/main.py:154) |
| **RobustRAG** | `Poison` 重复已有错误证据；`PIA` 使用指定输出的指令模板；`PIALONG` 使用较长的伪指令/对话结构 | 按前部、后部或随机位置，**直接替换 top-k 上下文槽位**；无需载荷赢得检索排名 | 检验生成器对已进入上下文的恶意文档是否稳健。[实现](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/RobustRAG/src/attack.py:1) |
| **SafeRAG** | 主流程读取预制的 SN、ICC、SA、WDoS 攻击文本，即 `enhanced_<任务>_contexts` | 两条路径：①追加到复制出的文档库并建索引；②直接前插到检索结果并截取 top-k | 分别测试知识库投毒与下游上下文注入。[实现](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SafeRAG/retrievers/base.py:109) |

**SecRAG 另实现了五类载荷，共用真实的 corpus / 索引追加入口：**

| SecRAG 攻击类 | 载荷生成方式 |
|---|---|
| **PoisonedRAGAttack** | 用 LLM 生成支持目标错误答案的伪证据段落。[代码](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/attack/poisoned_rag.py:97) |
| **PromptInjectionAttack** | 将问题、目标答案填入多种指令注入模板，生成独立恶意文档。[代码](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/attack/prompt_injection.py:23) |
| **CorruptRAGAttack** | AS 模式拼接问题、否定正确答案的“过时信息”声明和目标答案；AK 模式进一步用 LLM 改写。[代码](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/attack/corrupt_rag.py:117) |
| **CPARAGAttack** | LLM 初始化多个伪证据，再迭代进行面向检索器的改写，按相似度及生成条件筛选；当前交叉模型优化步骤被注释。[代码](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/attack/cpa_rag.py:227) |
| **AuthChainAttack** | 提取问题实体、意图与关系，生成支持目标答案的证据链和权威声明，再拼接成文档。[代码](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/attack/authchain_attack.py:52) |

这五类都会产生 `poisoned_docs`，由 benchmark 调用 `retriever.update_corpus()`，编码新文档、追加 FAISS 向量并更新 corpus。[调用入口](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/benchmark/poison_benchmark.py:548) / [更新实现](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/SecRAG/flashrag/retriever/retriever.py:428)

另外，**BIPIA** 将预设攻击文本插入外部 context 的开头、中间或结尾；**indirect-pia-detection** 也在输入文本中插入指令，属于间接提示注入样本构造，不经过 corpus 检索竞争。[BIPIA](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/benchmarks/BIPIA/bipia/data/base.py:90) / [indirect-pia-detection](/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/defenses/indirect-pia-detection/instruction_attack_defense_tools.py:46)

本地 **TrustRAG** 是通用 RAG 框架（归类为 `defenses/`）；`evaluate`、`gector` 是配套工具（归类为 `tools/`），不宜作为独立投毒方法列入对比。

**若用于统一实验，至少分开报告“需要通过检索的投毒”和“直接进入上下文的注入”：后者的成功率不包含检索失败这一环。**