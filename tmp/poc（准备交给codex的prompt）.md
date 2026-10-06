# ChunkTrojan — Single-Document Cross-Chunk Compositional Poisoning PoC

## 1. Objective

验证 ChunkTrojan 的核心安全假设：

> 在更现实的 RAG 投毒场景下，攻击者只能控制或修改一个 source document（例如一个 Wikipedia 词条），不能直接注入多个独立 poisoned documents/passages。该 document 经过 victim RAG 的正常 chunking 后产生多个 retrieval chunks。攻击者构造一个单一 poisoned document，使其中多个同源 chunks 分别携带互补的恶意语义；这些 chunks 单独不足以稳定诱导目标错误答案，但能够针对同一 query 被联合召回，并通过跨 chunk 的语义组合诱导 LLM 输出攻击者指定的错误答案。

核心机制：

```text
                 attacker controls ONE document
                              |
                              v
                     poisoned document D_adv
                              |
                         victim chunker
                              |
                    +---------+---------+
                    |                   |
                    v                   v
                   cA                  cB
             weak individually   weak individually
                    |                   |
                    +---------+---------+
                              |
                              v
                       joint co-retrieval
                              |
                              v
                  cross-chunk composition
                              |
                              v
                    LLM generation
                              |
                              v
                       target false answer
```

本 PoC 的核心不是 prompt injection，而是：

```text
single-document injection
        ->
victim-controlled chunking
        ->
same-source multiple chunks
        ->
joint retrieval
        ->
non-additive generation effect
```

本 PoC 不研究 reranker。

核心 RAG pipeline：

```text
source document
  -> victim chunking
  -> embedding retrieval
  -> retrieved context composition
  -> LLM generation
```

优先使用 LlamaIndex 等成熟库，以保持代码简洁、pipeline 可复现，并避免自行实现不必要的 RAG 基础设施。

---

## 2. Research Question

ChunkTrojan 只回答一个核心问题：

> **当攻击者的控制粒度是 source-document，而 RAG 的检索粒度是 chunk 时，攻击者能否利用二者之间的粒度差异，将一次文档级控制转化为多个能够联合检索、并产生非加性攻击效果的 retrieval units？**

需要严格区分：

### InceptionRAG

攻击者直接控制多个独立 passages：

```text
attacker
   |
   +---- malicious passage A
   |
   +---- malicious passage B
```

### ChunkTrojan

攻击者只控制：

```text
attacker
   |
   +---- malicious source document
                |
                v
          victim chunker
                |
           +----+----+
           |         |
           v         v
          cA        cB
```

因此 ChunkTrojan 的关键约束是：

```text
number of attacker-controlled source documents = 1
```

而不是简单地将多个 independently injected passages 称为多个 chunks。

---

## 3. Core Hypotheses

### H1 — Single-Document Multi-Chunk Decomposition

攻击者控制一个 source document：

```text
D_adv
```

攻击者不能直接指定最终 chunk boundary。

经过 victim chunker 后：

```text
D_adv -> {c1, c2, ..., cn}
```

其中至少存在两个目标 chunks：

```text
cA
cB
```

分别承担不同的恶意语义角色。

推荐初始角色：

```text
cA = retrieval anchor + partial target-related evidence

cB = complementary evidence + semantic completion / target conclusion cue
```

重要约束：

* cA 和 cB 必须来自同一个 `D_adv`；
* 不允许直接注入两个独立 poisoned documents；
* 不允许依赖固定 chunk ID；
* 不允许依赖 victim context 中的固定 chunk 顺序；
* 不允许在 chunk 中显式声明“另一个 chunk”；
* 不允许依赖特定 chunk 的存在位置。

目标是验证：

> victim chunking 是否能够自然产生多个可联合利用的 retrieval units。

---

### H2 — Individual Weakness

将目标 chunks 单独提供给 LLM 时，不应稳定产生目标错误答案：

```text
ASR_A ~= low
ASR_B ~= low
```

即：

```text
ASR_A ≈ 0
ASR_B ≈ 0
```

这是区分 ChunkTrojan 与普通 single-chunk poisoning 的必要条件。

如果某一个 chunk 单独已经具有较高 ASR，则：

```text
cA + cB
```

产生的攻击效果不能归因于 compositional mechanism。

---

### H3 — Same-Source Co-Retrieval

两个目标 chunks 必须针对同一个 target query：

```text
q
```

同时进入 retrieval Top-K：

```text
cA ∈ TopK(q)
cB ∈ TopK(q)
```

记录：

```text
rank(cA)
rank(cB)

score(cA)
score(cB)

cA ∈ TopK
cB ∈ TopK

co-retrieval indicator
```

核心指标：

```text
CoRecall@K =
1[cA ∈ TopK(q) AND cB ∈ TopK(q)]
```

该指标用于证明：

> 两个同源 chunks 不是分别有效，而是能够在同一 query 下同时进入 RAG context。

---

### H4 — Non-Additive Generation Effect

当两个 chunks 同时进入 LLM context 时，应产生明显强于任意单 chunk 的攻击效果：

```text
ASR_AB > max(ASR_A, ASR_B)
```

定义：

```text
Synergy =
ASR_AB - max(ASR_A, ASR_B)
```

PoC 最重要的 GO signal：

```text
ASR_A ≈ 0
ASR_B ≈ 0
ASR_AB > 0
```

更理想的结果：

```text
ASR_A ≈ 0
ASR_B ≈ 0

ASR_AB >> ASR_A
ASR_AB >> ASR_B

Synergy > 0
```

这里的核心不是追求最高 ASR，而是证明：

> 两个 individually weak 的同源 chunks 之间存在可观测的非加性攻击效应。

---

### H5 — Compositional Interaction Rather Than Simple Redundancy

必须排除以下解释：

> 两个 chunks 只是因为包含更多相似信息，所以共同出现时自然更容易影响 LLM。

因此需要加入 retrieval-relevance matched 的 control。

至少构造：

```text
(cA, cB)
    = complementary pair

(cA, cB_random)
    = retrieval-relevant but semantically incompatible pair
```

要求：

```text
ASR(cA,cB) > ASR(cA,cB_random)
```

如果资源允许，再构造：

```text
(cA, cB_shuffled)
```

使 cB 的语义关系被破坏，同时尽量保持：

```text
length
retrieval relevance
surface form
```

基本不变。

---

### H6 — Victim Chunking Is Part of the Attack Surface

如果攻击效果随着 chunk size 改变而发生系统性变化：

```text
chunk size
    ->
chunk boundary
    ->
co-retrieval
    ->
joint generation
```

则支持以下机制解释：

> ChunkTrojan 的攻击能力并非单纯来自 poisoned document 本身，而与 source-document 到 retrieval-chunk 的 victim-side transformation 有关。

因此重点记录：

```text
CoRecall@20(chunk_size)
ASR_AB(chunk_size)
Synergy(chunk_size)
```

不预先假设某一种 chunk size 最优。

---

## 4. Dataset

使用三个数据集：

```text
NQ
MS-MARCO
HotpotQA
```

数据集位于：

```text
/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/data/datasets
```

每个数据集随机抽取：

```text
100 target queries
```

总计：

```text
300 target queries
```

每个 selected target query 必须存在可用于构造 attack instance 的 source document，并具有明确的 target answer，以支持：

```text
ACC
ASR
EM
```

计算。

记录：

```text
dataset
query_id
document_id
document_token_length
query
answer
```

Target query 在 threat model 中视为攻击者已知。

---

## 5. Source Document Selection

ChunkTrojan 的基本攻击单位是：

```text
ONE source document
```

而不是 BEIR-style 已经切好的 retrieval passage。

对于每个 target query，选择一个能够作为 attack carrier 的 source document：

```text
D_adv
```

该 source document 应具有足够长度，使 victim chunker 能够产生至少两个 retrieval chunks，
并让两个来自同一 `D_adv` 的角色片段落入不同 chunk。

当前 PoC 要求：

```text
document length > 512 Contriever tokens
```

长度必须使用实际 victim tokenizer 计算。

该条件是 PoC 的实验设计约束，而不是声称所有现实 RAG document 都必须超过 512 tokens。
不要求 `D_adv > 1024`，也不要求至少产生三块；`D_adv > 512` 配合实际 chunk size
只需保证 A/B 能够落入两个不同 victim chunks。

原因：

1. 确保 document 不退化为单 chunk poisoning；
2. 支持 `64/128/256/512` chunk size 下的 boundary-aware 检验；
3. 保留短于 1024 tokens 但仍能产生有效 cross-chunk 的真实样本。

如果某 dataset 无法提供足够数量的满足条件的 source documents，应优先降低 query 数量，而不是放宽：

```text
number of poisoned documents = 1
```

这一核心约束。

---

## 6. Chunking

测试四种 chunk size：

```text
64
128
256
512
```

PoC 默认：

```text
chunk_size = N
overlap = 0
```

除非现有 RAG pipeline 已有固定 overlap，否则第一轮不要引入 overlap 变量。

必须使用同一个 tokenizer 计算：

```text
document length
chunk boundaries
```

对每个 source document 保存：

```text
document_id
chunk_id
start_token
end_token
chunk_text
```

并记录目标 chunks：

```text
cA_position
cB_position
```

以及：

```text
cA_start_token
cA_end_token

cB_start_token
cB_end_token
```

特别记录：

```text
distance(cA, cB)
```

即两个目标 chunks 在原始 document 中的 token 距离。

该信息用于分析：

> 攻击效果是否依赖两个 chunks 在 source document 中的物理邻近程度。

第一阶段不主动优化 chunk position。

---

## 7. Threat Model

攻击者：

* 已知 target query；
* 可以控制或修改一个 source document；
* 可以离线访问 surrogate retriever；
* 知道或可以合理推测 victim chunk size；
* 可以对 poisoned document 进行离线构造和优化；
* 不控制 victim retrieval implementation；
* 不控制最终 LLM；
* 不控制 Top-K；
* 不需要 online gradient access；
* 不需要修改多个 corpus documents。

攻击者不能：

```text
inject document A
inject document B
```

然后将它们称为两个 attack chunks。

必须满足：

```text
D_adv
  |
  +---- cA
  |
  +---- cB
```

即：

```text
source(cA) == source(cB) == D_adv
```

PoC 中：

```text
number of poisoned documents = 1
```

攻击者控制对象：

```text
single source document payload
```

而不是：

```text
corpus-wide poisoning
```

---

## 8. Retriever

使用 Contriever：

```text
/home/shadowx/mnt/sdc2/models/contriever
```

第一阶段：

```text
document
   ->
victim chunker
   ->
chunks
   ->
Contriever embedding
   ->
cosine similarity
   ->
Top-K
```

不要加入 reranker。

固定并记录：

```text
Contriever model/version
embedding normalization
similarity metric
K
```

建议：

```text
K = 5
K = 10
K = 20
```

其中：

```text
K = 10
```

作为主要 generation evaluation context retrieval setting。

同时：

```text
K = 20
```

作为主要 CoRecall 指标。

---

## 9. Payload Construction

ChunkTrojan 的 payload 必须首先被构造成：

```text
ONE poisoned document
```

而不是两个独立 payload passages。

基本结构：

```text
D_adv
 |
 +---- semantic region A
 |
 +---- semantic region B
```

经过 victim chunker：

```text
D_adv
 |
 +---- cA
 |
 +---- cB
```

cA 与 cB 可以分别承担：

```text
cA:
    retrieval anchor
    partial evidence

cB:
    complementary evidence
    semantic completion
    target conclusion cue
```

但二者之间不得存在显式程序化引用。

禁止：

```text
"see chunk B"
"the next section proves..."
"combine this with chunk 2"
```

禁止：

```text
chunk IDs
special cross-chunk markers
fixed positional references
```

禁止明显的：

```text
"ignore previous instructions"
"system prompt"
"developer message"
```

等 prompt injection。

目标是测试：

```text
retrieval-mediated compositional poisoning
```

而不是：

```text
prompt injection
```

---

## 10. InceptionRAG Relation

PoC 阶段允许复用 InceptionRAG 的：

```text
payload semantic decomposition
seed generation
offline optimization
```

代码位于：

```text
/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/InceptionRAG
```

未修改部分的优化算法和超参数按照现有实现继承。

但是必须修改其攻击抽象：

### InceptionRAG-style abstraction

```text
multiple attacker-controlled passages
        ->
joint retrieval
        ->
compositional generation
```

### ChunkTrojan abstraction

```text
ONE attacker-controlled source document
        ->
victim chunking
        ->
multiple same-source chunks
        ->
joint retrieval
        ->
compositional generation
```

因此 PoC 不要求重新设计复杂 optimizer。

第一阶段只验证：

> InceptionRAG 的 distributed/compositional semantic mechanism 是否能够迁移到由 victim chunking 自动产生的 same-source chunks，并产生 non-additive cross-chunk poisoning effect。

算法设计可参考下面讨论稿：
```markdown
可以。基于 CRCP 的“显式建模 victim chunking”思想和 InceptionRAG 的“把攻击语义拆成多个 individually benign / jointly effective fragments”思想，我认为 ChunkTrojan 最自然的算法不是简单地把 InceptionRAG 的两个 passage 拼成长文档，而是做成一个“先生成语义角色，再在 victim chunking 环中联合优化 source document”的算法。

CRCP 的关键启发是：攻击优化必须经过 `document → chunk → retrieval` 这个真实变换，否则优化出来的 payload 很可能在实际 chunking 后失效。([arXiv][1]) InceptionRAG 的关键启发则是：攻击目标可以从“单个 passage 完整表达恶意结论”变成“多个 dormant fragments 被共同检索后，由 LLM 自行完成恶意推理”。([arXiv][2])

因此我建议先设计下面这个版本。

## 1. 核心思想：Joint Chunk-Aware Payload Construction

定义：

$$
D_{adv}=G(z_A,z_B,q,y^*)
$$

其中：

* \(q\)：目标 query；
* \(y^*\)：攻击者希望 LLM 输出的错误答案；
* \(z_A,z_B\)：两个不同的语义角色；
* \(G\)：payload document generator。

然后不是直接优化 \(c_A,c_B\)，而是：

$$
D_{adv}
\xrightarrow{\text{victim chunker}}
C(D_{adv})=\{c_1,\ldots,c_n\}
$$

从中寻找两个目标 chunks：

$$
c_A,c_B\in C(D_{adv})
$$

整个攻击闭环：

```text
             target query q
                    │
                    ▼
             target answer y*
                    │
          ┌─────────┴─────────┐
          │ semantic roles    │
          │                   │
          ▼                   ▼
      z_A: anchor         z_B: completion
          │                   │
          └─────────┬─────────┘
                    ▼
          generate ONE document
                    │
                    ▼
                  D_adv
                    │
             victim chunker
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
         c_A                 c_B
          │                   │
          └─────────┬─────────┘
                    ▼
              Contriever
                    │
                    ▼
              Top-K(q)
                    │
                    ▼
              c_A + c_B
                    │
                    ▼
                 LLM
                    │
                    ▼
                  y*
```

这里真正的新东西是：

> **optimization loop 中间插入 victim chunker，并且优化目标是“同源 chunks 的联合召回 + 单 chunk 弱攻击性 + pair compositionality”。**

这比单纯的 chunk-aware poisoning 更贴近你的科学问题。

---

# 2. Payload 不应该简单设计成“两段恶意文字”

我建议第一版把 payload 抽象成两个 semantic roles。

### Chunk A：Anchor / Evidence Fragment

它负责：

$$
q\rightarrow e_A
$$

即让 embedding retriever 觉得它与 query 有关，同时提供部分支持信息。

例如抽象成：

```text
Entity X
    +
property / event / relation fragment
```

但不完整给出攻击结论。

### Chunk B：Completion / Conclusion Fragment

它负责：

$$
e_A+e_B\rightarrow y^*
$$

提供：

```text
relation
+
attribute
+
semantic completion
```

但单独拿出来时不应该足以诱导模型输出 \(y^*\)。

所以：

$$
P(y^*|q,c_A)\approx low
$$

$$
P(y^*|q,c_B)\approx low
$$

而：

$$
P(y^*|q,c_A,c_B)\gg low
$$

这实际上把 InceptionRAG 的 dormant semantic fragments 改造成了**同源 chunk pair**。InceptionRAG 本身的核心就是让分散的 fragments 在联合 retrieval 后由模型完成隐含推理，而不是让单个 passage 显式携带完整恶意 payload。([arXiv][2])

---

# 3. 关键：不要先生成 cA/cB，再拼接

这是我认为算法里最容易犯的错误。

错误方案：

```text
generate cA
generate cB

D_adv = cA + cB
```

然后：

```text
chunk(D_adv)
```

这样会出现一个问题：

> cA 和 cB 本身就是攻击者控制的 retrieval units。

那审稿人完全可以说：

> 这不就是 InceptionRAG 的两个 malicious passages 拼在一个 document 里吗？

所以正确方向应该是：

```text
semantic seed
      ↓
document generator
      ↓
D_adv
      ↓
victim chunker
      ↓
candidates
      ↓
select cA,cB
      ↓
evaluate
      ↓
modify D_adv
```

即：

> **chunk 是优化过程产生的中间状态，而不是攻击者直接指定的最终对象。**

这正是你与 InceptionRAG 最重要的 threat-model 差异。

---

# 4. 可以设计一个非常简单的 Algorithm 1

我建议暂时叫：

**ChunkTrojan: Chunk-Aware Compositional Payload Optimization**

伪代码可以是：

```text
Algorithm 1: ChunkTrojan Payload Optimization

Input:
    target query q
    target answer y*
    clean corpus D
    victim chunker C
    surrogate retriever R
    generator L
    K
    optimization budget B

Output:
    poisoned document D_adv

1:  Initialize semantic roles zA, zB
2:  D_adv ← GenerateDocument(q, y*, zA, zB)

3:  for t = 1 ... B do

4:      C_adv ← C(D_adv)

5:      S ← Retrieve(R, q, C_adv, K')

6:      Identify candidate pair (cA, cB)
        from same D_adv

7:      Compute:
            rA = rank(cA)
            rB = rank(cB)
            Ico = 1[cA,cB ∈ TopK]

8:      Evaluate individual weakness:
            A_A = ASR(q, cA)
            A_B = ASR(q, cB)

9:      Evaluate pair:
            A_AB = ASR(q, cA,cB)

10:     Score:
            J =
                λ1 · CoRecall(cA,cB)
              + λ2 · PairGain(cA,cB)
              - λ3 · max(A_A,A_B)

11:     Generate candidate modification:
            D'_adv ← ModifyDocument(D_adv, q, y*, zA, zB)

12:     If J(D'_adv) > J(D_adv):
            D_adv ← D'_adv

13: return D_adv
```

但这里有一个重要的成本问题：

**不要真的在每个 optimization iteration 调一次 Qwen。**

否则你的 PoC 很快重新变成你之前 SkillHijacker 那种 API 成本黑洞。

所以实际上应该把这个算法拆成两个阶段。

---

# 5. 第一阶段：Retriever-only optimization

CRCP 给你的最大启发其实在这里。

CRCP 的核心思想就是显式模拟：

$$
D\rightarrow C(D)\rightarrow retrieval
$$

而不是优化 document-level score 后再希望 chunking 不会破坏它。([arXiv][1])

ChunkTrojan 可以进一步定义：

$$
J_{ret}(D)
=
S(c_A,q)+S(c_B,q)
+\lambda C_{AB}
$$

其中：

$$
C_{AB}
=
\mathbf{1}[c_A,c_B\in TopK(q)]
$$

但是我建议不要简单最大化两个 score。

因为那会产生：

```text
cA = highly relevant
cB = highly relevant
```

然后两个 chunks 各自已经能够攻击。

这与 H2 冲突。

所以可以加入一个“individual weakness” penalty：

$$
J_{ret}
=
\lambda_1 C_{AB}
+\lambda_2(S_A+S_B)
-\lambda_3\max(S_A,S_B)
$$

但这里仍然不够好，因为 retrieval score 和 ASR 没有直接关系。

因此 PoC 第一版甚至可以更简单：

$$
J_{ret}
=
C_{AB}
$$

然后在每个候选 payload 上单独做：

```text
A-only
B-only
A+B
```

过滤。

即：

```text
Retriever optimization
       ↓
candidate D_adv
       ↓
individual ASR filter
       ↓
pair generation test
```

这样成本低很多。

---

# 6. 更关键的优化：Joint Retrieval Margin

我认为这个比单纯 `CoRecall` 更适合成为论文算法。

定义：

$$
s_A = sim(q,c_A)
$$

$$
s_B = sim(q,c_B)
$$

然后定义两个 chunk 的最低安全 retrieval margin：

$$
M_{joint}
=
\min(s_A,s_B)-s_{K}
$$

其中 \(s_K\) 是 Top-K 边界分数。

如果：

$$
M_{joint}>0
$$

则两个 chunks 都进入 Top-K。

这给你一个完全 offline 的 objective：

$$
J_{joint}
=
\min(s_A,s_B)-s_K
$$

优化：

$$
\max_D J_{joint}(D)
$$

这非常适合你现有的 3090 环境，因为：

**不需要 LLM query。**

只需要：

```text
Contriever embedding
+
cosine similarity
```

---

# 7. 但还需要一个“同源约束”

这是 ChunkTrojan 算法与普通 distributed poisoning 的核心。

候选集合：

$$
C_D=\{c_i\mid source(c_i)=D_{adv}\}
$$

然后：

$$
(c_A,c_B)
=
\arg\max_{c_i,c_j\in C_D}
J_{joint}(c_i,c_j)
$$

明确要求：

$$
source(c_A)=source(c_B)
$$

这样算法天然保证：

```text
ONE document
       ↓
same-source pair
```

而不是：

```text
D1 → cA
D2 → cB
```

---

# 8. 如何生成 D_adv？

这里我建议借鉴 InceptionRAG 的 seed generation，但不要直接照搬它的 payload。

可以定义一个非常简单的模板：

```text
Target:
    q
    y*

Semantic role A:
    target-related entity/property/evidence

Semantic role B:
    complementary relation/conclusion evidence
```

然后让 Qwen 生成一个自然 source document：

```text
D_adv =
    natural contextual content
    +
    semantic fragment A
    +
    natural contextual content
    +
    semantic fragment B
    +
    natural contextual content
```

这里有一个非常重要的设计：

**A/B 最好不要紧贴在一起。**

例如：

```text
paragraph 1
paragraph 2
semantic A
paragraph 4
paragraph 5
semantic B
paragraph 7
```

这样：

```text
D_adv
    ↓
chunker
    ↓
cA ≠ adjacent cB
```

更能证明：

> 这是 cross-chunk composition，而不是两个相邻句子恰好被拆开。

但第一版不要主动追求非常远的距离。先测试：

```text
distance = 1 chunk
distance = 2 chunks
distance = 4 chunks
```

即可。

---

# 9. 真正有意思的地方：Boundary-aware regeneration

这里可以得到一个很漂亮、而且与 CRCP 有明显继承关系的机制。

假设第一次生成：

```text
D_adv
```

经过 chunker：

```text
c1
c2
c3
c4
c5
```

结果：

```text
cA = c2
cB = c5
```

但：

```text
cA
```

被切坏了：

```text
semantic anchor
     ↓
chunk boundary
     ↓
剩余信息
```

那么不要直接修改 cA。

而是反馈：

```text
cA fragmented
```

给 document generator：

```text
Move anchor semantics
        ↓
modify D_adv
        ↓
rechunk
        ↓
evaluate again
```

也就是：

$$
D^{(t)}
\rightarrow C(D^{(t)})
\rightarrow evaluate
\rightarrow D^{(t+1)}
$$

这就是我认为最值得借 CRCP 的东西：

> **把 victim chunker 放进 attack optimization loop。**

CRCP 是为了让一个 adversarial passage 在不同 chunk boundary 下保持有效；ChunkTrojan 则进一步利用这个 loop 寻找能够形成**两个互补 retrieval units**的 document layout。([arXiv][1])

---

# 10. 因此最终算法可以拆成三层

我建议论文算法最终就保持这么简单：

### Stage 1 — Semantic Fragment Generation

借鉴 InceptionRAG：

$$
(q,y^*)\rightarrow(z_A,z_B)
$$

生成：

```text
anchor fragment
+
complementary fragment
```

目标：

```text
individually incomplete
jointly meaningful
```

---

### Stage 2 — Chunk-Aware Document Construction

借鉴 CRCP：

$$
(z_A,z_B)\rightarrow D_{adv}
$$

不断：

```text
generate
↓
chunk
↓
retrieve
↓
evaluate
```

寻找：

$$
c_A,c_B\in C(D_{adv})
$$

满足：

$$
source(c_A)=source(c_B)
$$

且：

$$
c_A,c_B\in TopK(q)
$$

---

### Stage 3 — Compositional Validation

最后才调用 Qwen：

```text
cA
cB
cA+cB
cA+random-B
```

检查：

$$
ASR_A\approx0
$$

$$
ASR_B\approx0
$$

$$
ASR_{AB}\gg ASR_A,ASR_B
$$

以及：

$$
ASR_{AB}>ASR_{random}
$$

这样 LLM API 只承担最终验证，而不是承担每一步搜索。

---

# 11. 一个更完整的目标函数

如果以后确实需要论文级算法，可以把它写成：

$$
\boxed{
J(D)=
\lambda_1 J_{\mathrm{co-ret}}
+
\lambda_2 J_{\mathrm{margin}}
+
\lambda_3 J_{\mathrm{sep}}
-
\lambda_4 J_{\mathrm{ind}}
}
$$

其中：

### Joint retrieval

$$
J_{\mathrm{co-ret}}
=
\mathbf{1}[c_A,c_B\in TopK(q)]
$$

或者用 soft version：

$$
J_{\mathrm{co-ret}}
=
\sigma(s_A-s_K)
+
\sigma(s_B-s_K)
$$

### Retrieval margin

$$
J_{\mathrm{margin}}
=
\min(s_A,s_B)-s_K
$$

### Pair separation

防止两个 chunk 过度相似：

$$
J_{\mathrm{sep}}
=
1-\cos(e_A,e_B)
$$

但这一项要谨慎。

因为如果两个 chunks 语义差异太大，它们可能无法共同完成推理。

所以更合理的是让它落在一个区间：

$$
\tau_l
<
\cos(e_A,e_B)
<
\tau_h
$$

即：

> 相关，但不是简单重复。

这恰好对应你的 H5。

### Individual attack penalty

严格意义上的：

$$
J_{\mathrm{ind}}
=
ASR_A+ASR_B
$$

但由于 ASR 需要 LLM evaluation，**PoC 不建议把它放进 inner-loop。**

实际工程上应该：

```text
offline retrieval objective
          ↓
candidate filtering
          ↓
limited LLM evaluation
```

---

# 12. 我反而不建议现在加入“LLM 生成 reward”

你之前考虑过类似：

```text
CoT reward
semantic reward
joint generation reward
```

现在我建议全部不要。

原因很简单：

你的核心科学问题是：

> **retrieval chunks 是否形成 compositional poisoning？**

而不是：

> 怎么用一个 LLM optimizer 把 ASR 最大化？

如果一开始就：

```text
LLM generation reward
+
ZOSO
+
chunk optimization
+
semantic reward
```

最后很容易重新变成一个复杂的 optimization paper，而且你又会掉回之前 SkillHijacker 的成本/风险陷阱。

**第一版甚至可以完全没有 optimizer。**

手工生成：

```text
D_adv
```

然后验证：

```text
chunk
→ retrieval
→ pair
→ generation
```

如果这个 mechanism 都不存在，优化器再漂亮也没有意义。

---

# 13. 我认为真正值得论文贡献的算法，是这个闭环

最终可以把 ChunkTrojan 的方法压缩成一句：

> **Unlike conventional poisoning attacks that optimize a document or InceptionRAG that directly distributes payloads across attacker-controlled passages, ChunkTrojan optimizes a single source document through the victim's own chunking transformation, searching for a same-source pair of retrieval units that are individually weak but jointly retrievable and compositional.**

形式化为：

$$
\boxed{
D^*
=
\arg\max_D
\;
J_{\mathrm{co-retrieval}}
\left(
C_{\mathrm{victim}}(D),q
\right)
}
$$

subject to：

$$
|D_{\mathrm{poison}}|=1
$$

$$
source(c_A)=source(c_B)=D
$$

$$
ASR(c_A),ASR(c_B)\le\epsilon
$$

并最终要求：

$$
ASR(c_A,c_B)
-
\max(ASR(c_A),ASR(c_B))
> \delta.
$$

这四个约束实际上就是 ChunkTrojan 的“数学指纹”。

---

## 14. 最后给你一个很重要的 GO/NO-GO

在你真正写 optimizer 前，我建议只做下面这个实验：

```text
10 NQ
10 HotpotQA
10 MS-MARCO

× 4 chunk sizes

手工/LLM生成 1 个 D_adv/query
```

然后只看：

$$
ASR_A,\quad ASR_B,\quad ASR_{AB}
$$

和：

$$
CoRecall@20
$$

如果出现：

```text
             ASR
A             0
B             0
A+B          30%+
random       ~0
```

同时：

```text
CoRecall@20 > 0
```

那就值得做 Stage-2 的 optimizer。

如果出现：

```text
A       20%
B       15%
A+B     25%
```

那么 ChunkTrojan 的 compositional claim 基本不成立，因为只是普通 single-chunk poisoning。

如果：

```text
A       0%
B       0%
A+B     0%
```

则直接 NO-GO。

这也是我认为目前最适合你的路线：**先证明“机制存在”，再证明“算法能稳定制造机制”，最后才讨论 ASR 和隐蔽性。** CRCP 为你提供 chunk-aware optimization 的基础框架，InceptionRAG 为你提供 compositional semantic payload 的基础机制，但 ChunkTrojan 自己真正需要贡献的是两者之间这个新的闭环：**single-document control × victim chunking × same-source co-retrieval × non-additive generation**。

[1]: https://arxiv.org/abs/2606.11265?utm_source=chatgpt.com "When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines"
[2]: https://arxiv.org/abs/2609.16818?utm_source=chatgpt.com "InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation"

```

---

## 11. Optimization Objective

如果 Phase 1 手工 PoC 成功，再进行离线 payload optimization。

优化对象：

```text
D_adv
```

而不是直接独立优化：

```text
cA
cB
```

因为最终：

```text
cA
cB
```

必须由 victim chunker 从同一个：

```text
D_adv
```

产生。

优化目标首先考虑：

```text
maximize joint co-retrieval(cA,cB)
```

即：

```text
cA ∈ TopK(q)
AND
cB ∈ TopK(q)
```

同时约束：

```text
ASR_A low
ASR_B low
```

最终 objective 可以抽象为：

```text
maximize:
    CoRecall(cA,cB)

subject to:
    ASR_A ≈ low
    ASR_B ≈ low
```

PoC 阶段不要加入复杂的：

```text
multi-objective Pareto optimization
adaptive topology
large-scale search
LLM-as-judge
```

目标不是首先得到 SOTA attack，而是验证：

```text
single-document
        ->
same-source multi-chunk
        ->
joint retrieval
        ->
compositional attack
```

这一机制是否存在。

---

## 12. LLM

使用：

```text
/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/.env
```

中指定的：

```text
MODEL_NAME=qwen3.8-27b
TEMPERATURE=0
RPM_PARALLEL=100
```

其中：

```text
RPM_PARALLEL=100
```

表示允许整个实验进程同时发起的 OpenAI client 调用 RPM 限制，使用 token bucket 进行限速。

LLM 用于：

1. payload seed generation；
2. 最终 RAG attack evaluation。

每次 API 调用必须记录：

```text
timestamp
dataset
query_id
stage
prompt_tokens
completion_tokens
total_tokens
```

至少区分：

```text
seed_generation_cost
optimization_cost
evaluation_cost
```

禁止只统计最终 evaluation cost。

最终报告：

```text
Total API tokens
Input tokens
Output tokens
Number of API calls
Token cost / attack instance
Token cost / successful attack
```

---

## 13. Experimental Conditions

每个 target query 至少运行以下条件。

### C0 — Clean RAG

使用：

```text
original corpus
query q
```

记录：

```text
clean answer
clean ACC
```

该条件用于确定正常 RAG 的 baseline behavior。

---

### C1 — Chunk A Only

向 LLM 提供：

```text
q + cA
```

测：

```text
ASR_A
```

该实验用于验证 cA 是否 individually weak。

---

### C2 — Chunk B Only

向 LLM 提供：

```text
q + cB
```

测：

```text
ASR_B
```

该实验用于验证 cB 是否 individually weak。

---

### C3 — Joint Same-Source Pair

向 LLM 提供：

```text
q + cA + cB
```

测：

```text
ASR_AB
```

这是 ChunkTrojan 的核心 condition。

---

### C4 — Retrieval-Relevance Matched Random Control

将 cB 替换为：

```text
cB_random
```

要求其：

```text
retrieval relevance
```

尽量接近原始 cB，但不具有与 cA 的目标语义互补关系。

测：

```text
ASR_A_random
```

核心比较：

```text
ASR_AB
    vs.
ASR_A_random
```

---

### C5 — Semantic-Destroyed Control

如果成本允许：

```text
cB
    ->
semantic relation destroyed
```

同时尽量保持：

```text
length
retrieval score
surface characteristics
```

测：

```text
ASR_A_shuffled
```

该 condition 用于进一步验证：

> 攻击增益来自 semantic composition，而不是简单增加 context information。

---

## 14. Retrieval Metrics

每个：

```text
dataset
query
chunk_size
attack instance
```

记录：

```text
Admission@5(cA)
Admission@5(cB)

Admission@10(cA)
Admission@10(cB)

Admission@20(cA)
Admission@20(cB)

CoRecall@5
CoRecall@10
CoRecall@20

rank(cA)
rank(cB)

retrieval_score(cA)
retrieval_score(cB)

score_margin
```

核心指标：

```text
CoRecall@20
```

定义：

```text
CoRecall@20 =
# queries where cA and cB both appear in Top20
/
# attack queries
```

同时记录：

```text
cA-only retrieval
cB-only retrieval
joint retrieval
```

用于区分：

```text
individual retrieval success
```

和：

```text
joint retrieval success
```

---

## 15. Generation Metrics

核心：

```text
ASR_A
ASR_B
ASR_AB
ASR_random
```

定义：

```text
ASR_X =
# queries where LLM outputs attacker target answer under condition X
/
# evaluated queries
```

主要机制指标：

```text
Synergy =
ASR_AB - max(ASR_A, ASR_B)
```

同时计算：

```text
Pair Gain =
ASR_AB - mean(ASR_A, ASR_B)
```

但：

```text
Synergy
```

作为主要 compositionality 指标。

---

## 16. Conditional Attack Success

为了区分 retrieval failure 与 generation failure，计算：

```text
Conditional ASR_AB
```

定义：

```text
Conditional ASR_AB =
P(target answer |
  cA ∈ TopK
  AND
  cB ∈ TopK)
```

因此：

```text
overall ASR
```

回答：

> 整个攻击 pipeline 是否成功？

而：

```text
Conditional ASR
```

回答：

> 在两个 chunks 已经成功共同进入 context 的情况下，LLM 是否表现出组合攻击效应？

这两个指标必须分开报告。

---

## 17. Answer Evaluation

所有 ASR 指标采用与 clean ACC 一致的 answer matching protocol。

PoC 默认：

```text
首句 exact match / EM
```

即：

1. 获取 LLM 输出；
2. 提取首句；
3. 与 target answer 进行 exact match；
4. 记录 binary success。

同步报告：

```text
Clean ACC
ASR_A
ASR_B
ASR_AB
ASR_random
```

不得仅报告 ASR 而不报告 clean baseline。

如果 target answer 存在多个规范表达形式，应预先建立：

```text
acceptable_answers
```

并在整个实验中使用相同 matching protocol。

---

## 18. Primary Success Criterion

PoC 不要求达到论文级 SOTA ASR。

只要求证明以下机制：

```text
1. attacker controls only one source document
2. victim chunker produces multiple attack chunks
3. cA alone has low ASR
4. cB alone has low ASR
5. cA and cB can be jointly retrieved
6. cA+cB has substantially higher ASR
7. random/non-complementary control does not reproduce the gain
```

理想结果：

```text
ASR_A ≈ 0
ASR_B ≈ 0

CoRecall@20 > baseline

ASR_AB >> ASR_A
ASR_AB >> ASR_B

ASR_AB > ASR_random

Synergy > 0
```

其中最重要的不是：

```text
ASR_AB 最大
```

而是：

```text
ASR_A low
ASR_B low
ASR_AB high
```

即：

> individually weak + jointly effective。

---

## 19. Chunk-Size Analysis

分别运行：

```text
64
128
256
512
```

分析：

```text
chunk size
    ->
number of chunks
    ->
chunk boundary
    ->
retrieval score
    ->
co-retrieval
    ->
joint ASR
```

重点观察：

```text
CoRecall@20(chunk_size)

ASR_AB(chunk_size)

Synergy(chunk_size)
```

并记录：

```text
cA_position
cB_position
distance(cA,cB)
```

如果攻击效果明显依赖：

```text
chunk size
```

或者：

```text
chunk boundary
```

则可作为支持以下机制的证据：

> ChunkTrojan exploits the document-to-chunk transformation performed by the victim RAG pipeline.

---

## 20. Same-Source Constraint Ablation

必须验证：

```text
same-source
```

确实是实验约束，而不是偶然结果。

至少比较：

```text
Condition A:
cA + cB
where source(cA) == source(cB)

Condition B:
cA + cB_external
where source(cA) != source(cB)
```

Condition B 不作为主要攻击方法，而作为 mechanism/reference control。

其目的不是证明 same-source 一定优于 multiple-source，而是确认：

> ChunkTrojan 的核心贡献是 single-document constraint 下仍然能够形成 compositional attack。

---

## 21. Ablation

最低限度：

```text
A only
B only
A+B
A+random B
```

建议增加：

```text
A+B with semantic-destroyed B
```

如果资源允许：

```text
A+B with independently optimized B
```

以及：

```text
same-source pair
vs.
cross-source pair
```

其中 independent optimization 实验用于分析：

> 是否需要显式联合优化才能形成 compositional attack。

---

## 22. Artifact and Logging Requirements

所有实验必须保留：

```text
source document
victim chunks
payload
query
retrieval result
LLM input
LLM output
evaluation result
token cost
```

每个 attack instance 至少记录：

```json
{
  "dataset": "...",
  "query_id": "...",
  "document_id": "...",
  "document_token_length": 0,
  "chunk_size": 128,
  "chunk_a_id": "...",
  "chunk_b_id": "...",
  "chunk_a_start": 0,
  "chunk_a_end": 0,
  "chunk_b_start": 0,
  "chunk_b_end": 0,
  "chunk_distance": 0,
  "rank_a": 3,
  "rank_b": 7,
  "retrieval_score_a": 0.0,
  "retrieval_score_b": 0.0,
  "co_retrieved": true,
  "asr_a": false,
  "asr_b": false,
  "asr_ab": true,
  "asr_random": false,
  "input_tokens": 0,
  "output_tokens": 0,
  "total_tokens": 0
}
```

---

## 23. Data and Artifact Directory

继承现有项目路径：

```text
/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/
```

数据集：

```text
data/
    datasets/
```

建议 PoC artifact：

```text
data/
    datasets/
        poc_dataset/
            clean_corpus.jsonl
            clean_corpus_chunk_64.*
            clean_corpus_chunk_128.*
            clean_corpus_chunk_256.*
            clean_corpus_chunk_512.*
            poisoned_corpus.jsonl
            poisoned_corpus_chunk_64.*
            poisoned_corpus_chunk_128.*
            poisoned_corpus_chunk_256.*
            poisoned_corpus_chunk_512.*
            queries.jsonl
```

其中 embedding/index 文件后缀以 LlamaIndex 实际支持格式为准。

注意：

```text
chunk
```

统一使用正确拼写。

不要再使用：

```text
chunck
```

作为新的文件名或变量名。

结果：

```text
results/
    poc/
        retrieval/
            query_{}.jsonl
        generation/
            query_{}.jsonl
        results_overview.json
        report.md
```

代码：

```text
main.py
common/
    models.py
```

如果现有项目实际使用：

```text
commom/
```

则继承现有目录，不在 PoC 阶段为了重命名目录增加无关修改。

---

## 24. Execution Order

严格按照以下顺序执行。

目标：

> 在核心机制未验证之前，不进行大规模 payload optimization 和 API evaluation。

---

### Phase 0 — Pipeline Sanity Check

在不生成 poison 的情况下确认：

```text
dataset
    ->
source document
    ->
victim chunker
    ->
Contriever
    ->
TopK
    ->
Qwen RAG generation
```

确认：

```text
chunking 正常
embedding 正常
retrieval 正常
LLM generation 正常
answer evaluation 正常
token logging 正常
```

---

### Phase 1 — Manual Same-Source PoC

手工构造少量：

```text
ONE D_adv
```

使其经 victim chunker 后产生：

```text
cA
cB
```

每个 dataset 先测试约：

```text
10 queries
```

至少运行：

```text
A
B
A+B
random B
```

确认：

```text
A-only low
B-only low
A+B > A/B
A+B > random
```

如果 Phase 1 无明显 compositional signal：

```text
STOP
```

不要进入大规模优化。

---

### Phase 2 — InceptionRAG Seed Adaptation

只有 Phase 1 出现正向信号后，才使用：

```text
InceptionRAG
```

现有代码：

```text
/home/shadowx/mnt/sdc2/New_Future/ChunkTrojan/baselines/attacks/InceptionRAG
```

生成 payload seed。

注意：

> seed generation 输出必须最终合并为一个 source document，而不能产生多个独立 poisoned documents。

---

### Phase 3 — Single-Document Offline Optimization

将现有 InceptionRAG optimization pipeline 适配为：

```text
ONE source document
        ->
victim chunking
        ->
cA + cB
        ->
joint retrieval objective
```

主要目标：

```text
maximize joint co-retrieval(cA,cB)
```

约束：

```text
single source document
low individual ASR
```

第一阶段不加入：

```text
reranker
Agent execution
multi-document poisoning
large-scale LLM optimization
complex Pareto optimization
```

---

### Phase 4 — 300-Query Evaluation

如果 Phase 3 成功，运行：

```text
3 datasets
×
100 queries
×
4 chunk sizes
```

即：

```text
NQ
MS-MARCO
HotpotQA

64
128
256
512
```

完整统计：

```text
retrieval
co-retrieval
generation
Synergy
Conditional ASR
clean ACC
token cost
```

---

## 25. GO / NO-GO Decision

### GO

满足以下核心条件：

```text
G1:
攻击者始终只控制一个 source document。

G2:
victim chunker 能够产生多个攻击相关 chunks。

G3:
cA alone 的 ASR 较低。

G4:
cB alone 的 ASR 较低。

G5:
cA 与 cB 能够针对同一 query 联合进入 Top-K。

G6:
cA+cB 的 ASR 明显高于任一单 chunk。

G7:
complementary pair 的效果高于 retrieval-relevance matched random/non-complementary pair。

G8:
现象至少在多个 chunk size 或多个 dataset 上具有一定重复性。
```

最关键的 GO signal：

```text
ASR_A ≈ low
ASR_B ≈ low

CoRecall@20 > 0

ASR_AB >> max(ASR_A, ASR_B)

Synergy > 0

ASR_AB > ASR_random
```

如果同时满足：

```text
Conditional ASR_AB high
```

则进一步支持：

> 攻击成功主要发生在两个 malicious chunks 已经共同进入 context 后，而不是单纯由 retrieval failure 或某一个 chunk 单独造成。

---

### STRONG GO

如果进一步观察到：

```text
same-source
    ->
multiple chunks
    ->
joint retrieval
    ->
non-additive ASR
```

并且：

```text
chunk size / boundary
```

会系统性影响：

```text
CoRecall
Synergy
ASR_AB
```

则可以开始进入论文级实验设计。

---

### NO-GO

出现以下情况时，不继续复杂化：

```text
1. cA 或 cB 单独已经获得较高 ASR；

2. cA+cB 的提升无法超过 random/non-complementary pair；

3. 两个 same-source chunks 无法稳定 co-retrieve；

4. joint ASR 主要来自 cA 或 cB 单独的攻击能力；

5. 攻击必须依赖显式 chunk reference；

6. 攻击必须依赖 prompt injection；

7. 攻击必须依赖固定 chunk ID 或固定 chunk order；

8. 只有某一个 dataset、某一个 chunk size 出现现象；

9. 结果无法与普通 single-document poisoning 区分；

10. 最终只能证明“一个长 poisoned document 本身有效”，而无法证明 cross-chunk compositional effect。
```

NO-GO 后：

```text
不要继续增加 optimizer；
不要加入 reranker；
不要加入 Agent execution；
不要扩大到大规模 corpus；
不要通过增加更多 poisoned documents 修复结果。
```

---

## 26. Minimal Scientific Claim

如果最终只能获得 PoC 级结果，论文 claim 应严格限制为：

> **ChunkTrojan demonstrates that a single attacker-controlled source document can, after victim-side chunking, produce multiple individually weak retrieval chunks whose joint retrieval can induce a stronger target misinformation effect than either chunk alone.**

对应中文：

> **ChunkTrojan 证明：在攻击者只能控制单一源文档的条件下，受害 RAG 的文档分块过程可以产生多个单独攻击能力较弱但能够联合召回的恶意 chunk；这些同源 chunks 的联合出现能够产生强于任一单独 chunk 的目标错误生成效果。**

不要在 PoC 阶段宣称：

```text
universal RAG vulnerability
```

或者：

```text
all chunkers are vulnerable
```

也不要宣称：

```text
InceptionRAG fails under chunking
```

ChunkTrojan 的核心 claim 只是：

```text
single-document constraint
        +
victim-side chunking
        +
same-source co-retrieval
        +
non-additive generation
```

是否构成一个独立的攻击机制。


---

结合你前面整个思路、现在已有的实验资产，以及我刚核对的 CamoDocs / CRCP / InceptionRAG / TRIS 原文，我现在会把这两个问题定得更窄一些：

**ChunkTrojan 不应该被形式化成“更强的投毒优化器”，而应该被形式化成一个 constrained compositional poisoning problem；防御也不应该被形式化成“更强的 embedding anomaly detector”，而应该被形式化成 retrieval-context set 的风险重排问题。**

这样工程上才可控，而且攻防两边形成一个很漂亮的对偶。

---

# 1. 先定义一个统一 RAG 模型

令攻击者控制一个 source document：

\[
D\in\mathcal D.
\]

受害者的实际处理流程：

\[
D
\xrightarrow{\phi}
\mathcal C(D)=\{c_1,\ldots,c_n\}
\xrightarrow{E_r}
\{e_1,\ldots,e_n\}
\xrightarrow{\operatorname{TopK}}
C_q
\xrightarrow{G}
y.
\]

其中：

\[
\phi=\text{victim chunker},
\]

\[
E_r=\text{victim retriever encoder},
\]

\[
G=\text{generator}.
\]

CRCP 已经非常明确地指出：现实 RAG 的关键问题是 document-level optimization 与实际 chunk-level retrieval / reranking 之间存在 granularity mismatch，因此它显式优化 chunk relevance、reranker consistency 和 boundary robustness。[arXiv](https://arxiv.org/html/2606.11265v1)

而 CamoDocs 虽然也使用 chunking，但它明确把 chunking 当作后续 token manipulation 和 merging 的工具，而不是研究“多个 chunk 联合攻击”；它真正优化的是 dispersion loss，使 poisoned-document embeddings 分散。[arXiv](https://arxiv.org/abs/2608.28389)

这正好给 ChunkTrojan 留出了一个不同的目标。

---

# 2. ChunkTrojan 应该形式化成什么

按照你现在已经确定的约束：

\[
\boxed{\text{一个 source document}}
\]

\[
\boxed{\text{恰好两个 adversarial chunks}}
\]

\[
\boxed{\text{target query 已知}}
\]

\[
\boxed{\text{victim chunker / encoder / retriever 不受攻击者控制}}
\]

令这个 document 经过 victim chunker 后得到两个真正承载攻击语义的 chunk：

\[
c_a,\;c_b.
\]

其它 chunks 只是正常/掩护内容。

核心要求不是：

\[
Attack(c_a)>0,\quad Attack(c_b)>0.
\]

而是：

\[
\boxed{
Attack(c_a)\approx0,\quad
Attack(c_b)\approx0
}
\]

但是：

\[
\boxed{
Attack(c_a,c_b)\gg0
}
\]

这就是整个 ChunkTrojan 最重要的 formal property。

---

# 3. 第一项：联合检索目标

你现在已经有完整 Top-1000 背景缓存，这是非常适合这个目标的。

设干净背景下第 \(K\) 名分数为：

\[
\tau_K(q).
\]

两个 adversarial chunks 的 dense retrieval score：

\[
s_a=s_r(q,c_a),\qquad
s_b=s_r(q,c_b).
\]

可以定义 retrieval margin：

\[
m_i=s_i-\tau_K(q).
\]

于是 exact CoRecall@K：

\[
\operatorname{CoRecall}@K
=
\mathbf 1[
m_a\ge0\land m_b\ge0
].
\]

这个指标比单纯 Recall@K 更符合 ChunkTrojan。

用于优化时，不要直接最大化一个离散 indicator，而采用平滑 surrogate：

\[
h_i=
\sigma\left(\frac{m_i}{T}\right),
\]

然后：

\[
\boxed{
J_{\mathrm{co-ret}}
=
h_a h_b
}
\]

或者更保守地：

\[
J_{\mathrm{co-ret}}
=
\min(h_a,h_b).
\]

我更喜欢后一个。

因为它迫使两个 chunk 都过线，而不是让一个 chunk 得分极高、另一个勉强存在。

---

# 4. 第二项才是 ChunkTrojan 的真正创新：composition objective

这里不要简单采用：

\[
J_{\mathrm{gen}}(q,c_a,c_b).
\]

否则它和 InceptionRAG 没有本质区别。

应该明确优化：

\[
\boxed{
\text{pair-only gain}
}
\]

定义某个目标错误答案 \(a^*\) 的支持得分：

\[
g(q,C,a^*).
\]

它可以由一个冻结的 local surrogate reader / NLI model / small cross-encoder 提供。

然后：

\[
J_{\mathrm{single}}
=
\max\{g(q,c_a,a^*),g(q,c_b,a^*)\}
\]

而：

\[
J_{\mathrm{pair}}
=
g(q,c_a\oplus c_b,a^*).
\]

定义：

\[
\boxed{
J_{\mathrm{comp}}
=
J_{\mathrm{pair}}-J_{\mathrm{single}}
}
\]

这才真正表达：

> 单块自己不能完成攻击，两个块联合以后才产生额外攻击能力。

最终你甚至可以定义论文里的核心指标：

\[
\boxed{
\operatorname{Composition\ Gain}
=
ASR(c_a,c_b)
-
\max[ASR(c_a),ASR(c_b)]
}
\]

如果实验得到：

\[
ASR(c_a)\approx0,\quad
ASR(c_b)\approx0,\quad
ASR(c_a,c_b)\gg0,
\]

那么你证明的是**一种攻击现象**，而不仅仅是一个新优化器。

这点很重要。

---

# 5. 第三项：CamoDocs 应该怎么进入 ChunkTrojan

这里我建议你**不要直接照抄 CamoDocs 的 dispersion loss**。

因为 CamoDocs 的：

\[
L_{disp}
=
\frac1\beta\sum_j\|e_j-c\|
\]

本质上是在把多个 poisoned-document representations 往不同方向推，使它们不再形成紧簇。[arXiv](https://arxiv.org/abs/2608.28389)

对 ChunkTrojan 而言，如果你直接：

\[
\max \|e_a-e_b\|,
\]

可能把两个 chunk 推得过远，反而降低：

\[
P(c_a,c_b\in TopK).
\]

所以更合理的是把 CamoDocs 的思想从：

> **dispersion**

改成：

> **local normality / footprint minimization**。

定义一个基于 clean corpus 的 embedding anomaly：

\[
A(e)
\]

例如局部 Mahalanobis / kNN density / robust distance。

然后：

\[
\boxed{
J_{\mathrm{stealth}}
=
A(e_a)+A(e_b)
}
\]

优化目标变成：

\[
\min J_{\mathrm{stealth}}.
\]

这比“让两个 chunk 彼此离得远”更加适合 ChunkTrojan。

所以从算法继承关系看：

\[
\text{CamoDocs}
\rightarrow
\text{candidate generation / token substitution machinery}
\]

而：

\[
\boxed{
\text{ChunkTrojan 自己定义新的 objective}
}
\]

这就避免了单纯缝合。

CamoDocs 的原文明确是 gradient-guided token replacement，并先用 dispersion 候选，再用 lightweight coherence model 做过滤。[arXiv](https://arxiv.org/abs/2608.28389)

---

# 6. 第四项：文本自然度

保留一个简单的：

\[
J_{\mathrm{fluency}}
\]

例如 frozen lightweight LM PPL。

然后：

\[
\min J_{\mathrm{fluency}}.
\]

这部分完全可以照搬 CamoDocs 的 coherence filtering 思想；它已经证明这是一条工程上合理的廉价约束。[arXiv](https://arxiv.org/abs/2608.28389)

---

# 7. 所以 ChunkTrojan 的完整优化目标

我会最终写成：

\[
\boxed{
\max_D
\;
\lambda_r J_{\mathrm{co-ret}}
+
\lambda_c J_{\mathrm{comp}}
-
\lambda_s J_{\mathrm{stealth}}
-
\lambda_f J_{\mathrm{fluency}}
}
\]

如果考虑 victim chunking 不确定性：

\[
\boxed{
\max_D
\;
\mathbb E_{\phi\sim\Phi}
[
\lambda_r J_{\mathrm{co-ret}}^\phi
+
\lambda_c J_{\mathrm{comp}}^\phi
-
\lambda_s J_{\mathrm{stealth}}^\phi
-
\lambda_f J_{\mathrm{fluency}}^\phi
]
}
\]

这和 CRCP 有一个非常漂亮的区别。

CRCP 明确鼓励：

\[
\boxed{
c_i\text{ individually self-contained}
}
\]

它希望每个 chunk 自己就有 query relevance、answer-bearing semantics 和 adversarial guidance。[arXiv](https://arxiv.org/html/2606.11265v1)

ChunkTrojan 则应该刻意优化：

\[
\boxed{
c_i\text{ individually insufficient}
}
\]

同时：

\[
\boxed{
(c_a,c_b)\text{ jointly sufficient}
}
\]

所以可以把两者概括为：

\[
\text{CRCP}: \quad
\text{local sufficiency}
\]

\[
\text{ChunkTrojan}: \quad
\text{compositional sufficiency}.
\]

这是目前我认为最有价值的理论分界。

---

# 8. 但这里有一个重要工程现实：不要一开始优化“完整生成器”

这是整个 ChunkTrojan 最大的工程风险。

如果直接：

\[
\nabla_D
P_G(a^*|q,c_a,c_b)
\]

你马上进入 InceptionRAG / Joint-GCG 那种高成本路线。

你当前资源和硕士目标都不适合。

所以建议两层：

### 优化阶段

用冻结 surrogate：

\[
g_\psi(q,C,a^*)
\]

提供 composition signal。

例如：

- small NLI model；
- cross-encoder；
- local small reader。

### 最终验证阶段

再用你的本地 Qwen 27B 做真实 RAG generation。

这样：

\[
\text{optimization}
\neq
\text{LLM generation loop}.
\]

这会大幅降低成本。

你已经明确倾向于离线、静态和低 API 成本路线，而现有本地检索缓存也已经能直接支持“对新注入 chunk 与固定 clean Top-1000 背景重新打分”的实验路径。

---

# 9. 真正的攻击算法应该怎么落地

我不建议你直接复制 CamoDocs 的 1500-step 全词表搜索。

应该是：

\[
\text{LLM draft}
\rightarrow
\text{victim chunk}
\rightarrow
\text{确定两个 adversarial chunks}
\rightarrow
\text{候选 token proposal}
\rightarrow
\text{精确 post-chunk evaluation}
\rightarrow
\text{保留最优}
\]

也就是：

**CamoDocs 负责“提候选”，ChunkTrojan objective 负责“选候选”。**

这点非常重要。

因为 CamoDocs 当前的 HotFlip 候选方向优化的是：

\[
L_{disp}.
\]

ChunkTrojan 应该把 candidate selection 改成：

\[
\boxed{
J_{CT}
=
J_{co-ret}
+
J_{comp}
-
J_{stealth}
-
J_{fluency}
}
\]

这样算法上才真正属于 ChunkTrojan。

---

# 10. 最大的工程风险不是算力，而是“两个 chunk 根本无法同时出现”

这是 No.1 风险。

定义：

\[
P_{\mathrm{co}}(K)
=
P(
rank(c_a)\le K
\land
rank(c_b)\le K
).
\]

如果这个概率本身非常低，那么无论优化器多漂亮都没用。

因此第一个 PoC 根本不应该做大规模攻击。

先测：

\[
\boxed{
\max_D CoRecall@K
}
\]

在：

\[
K=5,10,20,50
\]

和：

\[
chunk\ size=64,128,256,512
\]

下测。

如果 2-chunk CoRecall 本身接近 0：

**立即停止。**

这就是你现在最重要的 GO/NO-GO gate。

你已有 4 档 chunk 索引和完整 Top-1000 检索缓存，这个实验成本非常低。

---

# 11. 第二个风险：两个 chunk 一起出现，但其实每一个都已经能攻击

这种实验非常危险。

例如：

\[
ASR(c_a)=75\%
\]

\[
ASR(c_b)=63\%
\]

然后：

\[
ASR(c_a,c_b)=80\%.
\]

这不能叫 compositional attack。

必须要求：

\[
ASR(c_a)\ll ASR(c_a,c_b)
\]

\[
ASR(c_b)\ll ASR(c_a,c_b).
\]

所以你的最核心实验 matrix 应该是：

| Context | Retrieval | Generation |
|---|---:|---:|
| clean | — | baseline |
| \(c_a\) | Recall@K | ASR |
| \(c_b\) | Recall@K | ASR |
| \(c_a+c_b\) | **CoRecall@K** | **Joint ASR** |
| unrelated \(c_x+c_y\) | control | control |

最好再增加：

\[
c_a+\text{unrelated}
\]

和：

\[
c_b+\text{unrelated}.
\]

这样可以证明不是“多放一篇文本就增强攻击”。

---

# 12. 第三个风险：victim chunker 不知道怎么办

这里我建议你**不要把“完全未知 chunker”设成主要优化约束**。

这是一个非常容易把项目搞死的地方。

CRCP 自己也采用了一组 chunking policies：

\[
\Phi=\{\phi_1,\ldots,\phi_M\}
\]

并优化：

\[
E_{\phi\sim\Phi}[L_{\mathrm{attack}}].
\] :chatgpt-content-reference{index="8"}


你也可以这样做，但分两个层次：

第一阶段：

\[
\phi=\text{固定代表性 chunker}
\]

验证 phenomenon。

第二阶段：

\[
\phi\in\{64,128,256,512\}
\]

做 transfer evaluation。

不要一开始就要求：

> attacker 完全不知道任何 chunking，而且必须一次性跨所有 chunking 成功。

那会把一个硕士问题变成一个非常重的 black-box optimization 问题。

---

# 13. 现在说 RAGShield

我现在不建议你的防御优化目标是：

\[
\min \text{embedding anomaly}.
\]

TRIS、TrustRAG、CleanBase、PRA-RAG 等已经把这个方向覆盖得比较充分。报告也明确把“cluster / embedding geometry”列为现有防御主线，并指出新攻击正在使这种 semantic-outlier 假设失配。gptchat gptchat

你应该把对象改变成：

\[
\boxed{
C_q=\{c_1,\ldots,c_K\}
}
\]

而不是单个：

\[
c_i.
\]

---

# 14. RAGShield 的核心优化问题

给每个 chunk：

\[
s_i=s_r(q,c_i)
\]

embedding：

\[
e_i=E(c_i)
\]

source：

\[
z_i=source(c_i).
\]

构造一个 context-level feature representation：

\[
F_q=\Psi(q,C_q).
\]

目标：

\[
\boxed{
\min_{\theta}
\;
\mathbb E[
L_{\mathrm{security}}
+
\lambda L_{\mathrm{utility}}
+
\mu L_{\mathrm{latency}}
]
}
\]

同时：

\[
FPR\le \epsilon
\]

\[
CACC_{\mathrm{def}}
\ge CACC_{\mathrm{clean}}-\delta.
\]

这实际上就是一个 safety–utility–cost optimization。

你报告本身已经指出现有文献很少系统报告三者权衡，这反而适合作为你的实验设计要求。gptchat

---

# 15. RAGShield 不应该检测“一个点”，而应该检测“一个关系”

我建议最终使用四组信号。

### A. Point signal

传统攻击：

\[
A_i
\]

例如：

- local density
- Mahalanobis
- query similarity abnormality
- rank anomaly

用来处理 PoisonedRAG/CamoDocs 一类。

---

### B. Provenance signal

：

\[
S_{ij}=1[z_i=z_j].
\]

但不能简单：

\[
same\ source\Rightarrow poison.
\]

应该计算：

\[
P(\text{co-retrieval}\mid same\ source,q)
\]

相对于 clean baseline 是否异常。

这个非常重要。

---

### C. Relational signal

：

\[
R_{ij}=f(e_i,e_j,s_i,s_j).
\]

比如：

\[
\cos(e_i,e_j)
\]

\[
|s_i-s_j|
\]

\[
rank_i,rank_j
\]

以及一个很有价值的量：

\[
\boxed{
\text{Joint Retrieval Amplification}
}
\]

也就是 pair 在 context 中的联合效应是否异常集中。

---

### D. Conflict / consistency signal

这里你提出的：

> 良性和恶性文档共同存在时，会不会有 entity-level contradiction？

**值得做，但不能把它当成理论根源。**

因为这不是必然成立。

例如：

> “X was born in 1980.”

和：

> “A newly discovered archive reveals X was actually born in 1983.”

两者事实上冲突，但恶意文本可以包装成“knowledge update”。

而另一些 ChunkTrojan 可以制造：

\[
A\rightarrow B
\]

\[
B\rightarrow C
\]

\[
A\rightarrow C
\]

这种新的错误推理关系，可能根本不存在一个直接 contradiction edge。

所以：

\[
\boxed{
Conflict\ is\ a\ signal,\ not\ the\ root\ invariant.
}
\]

---

# 16. 你提出的“小于 1B SLM 做微型 KG”应该怎么改

我认为：

**不要让 SLM 生成 KG。**

这个设计容易产生：

\[
text
\rightarrow
LLM
\rightarrow
JSON
\rightarrow
KG
\]

一串新的不稳定性。

你担心它的：

- 格式不稳定；
- relation extraction 错误；
- 小模型理解不足；

都是实际问题。

更好的用法是：

\[
\boxed{\text{SLM 只输出固定维度 logits}}
\]

例如 NLI。

`cross-encoder/nli-deberta-v3-base` 直接输出：

\[
P(\text{contradiction}),
P(\text{entailment}),
P(\text{neutral}),
\]

而不是输出自由文本。其模型基于 DeBERTa-v3-base，参数量约 183M，模型卡报告 MNLI mismatched accuracy 90.04%。[Hugging Face](https://huggingface.co/cross-encoder/nli-deberta-v3-base/blob/main/README.md?utm_source=chatgpt.com)

所以：

\[
(c_i,c_j)
\rightarrow
\text{NLI}
\rightarrow
(p_c,p_e,p_n)
\]

会比：

\[
(c_i,c_j)
\rightarrow
\text{SLM}
\rightarrow
JSON\ KG
\]

稳定得多。

---

# 17. 甚至可以不做完整 KG

我建议只保留：

\[
\text{NER}
+
\text{NLI}
\]

例如：

chunk \(i\) 中实体：

\[
E_i
\]

chunk \(j\) 中：

\[
E_j.
\]

共享实体：

\[
E_{ij}=E_i\cap E_j.
\]

然后只有在：

\[
|E_{ij}|>0
\]

的时候才调用 NLI。

得到：

\[
P_{ij}^{contra}.
\]

定义：

\[
C_{ij}
=
|E_{ij}|
\cdot P_{ij}^{contra}.
\]

这就是一个非常便宜的 entity-conditioned contradiction score。

而且可以限制：

\[
\text{只检查 top-3 suspicious pairs}.
\]

这样就不会产生：

\[
O(K^2)
\]

次 NLI 全量开销。

---

# 18. 真正适合你的 RAGShield，我反而建议做“轻量 pairwise reranker”

这是我现在最喜欢的版本。

首先产生每个 chunk 的 point risk：

\[
r_i.
\]

然后产生 pair risk：

\[
r_{ij}.
\]

然后不是直接：

\[
delete(c_i).
\]

而是优化最终 context：

\[
\boxed{
C^*
=
\arg\max_{C:|C|=m}
\left[
\sum_{i\in C}s_i
-
\lambda\sum_{i<j}r_{ij}
\right]
}
\]

这实际上是一个：

\[
\boxed{
risk-aware evidence set selection
}
\]

而不是普通 anomaly filter。

它有非常重要的优势：

正常情况下：

\[
r_{ij}\approx0
\]

所以不会破坏普通 RAG。

ChunkTrojan 情况：

\[
r_{ab}\gg0
\]

即使：

\[
r_a\approx0,\quad r_b\approx0,
\]

最终也会降低：

\[
(c_a,c_b)
\]

同时进入 context 的概率。

这正好针对你的核心攻击。

---

# 19. 这个设计甚至能解释 TRIS 的缺点

TRIS：

\[
\text{point / structure / generation}
\]

是：

\[
AND
\]

式防御。

你的 RAGShield：

\[
\text{evidence-set risk}
\]

是：

\[
\text{pairwise / relational}
\]

它针对的是：

\[
Attack(c_a,c_b)
\]

而不是：

\[
Attack(c_a)
\]

这就是一个明确区别。

TRIS 当前的论文定位是跨 embedding clustering + trigger-payload structure + LLM consistency 三层；它确实取得了很强的单文档 poisoning 降幅，但 Layer 3 会引入约 16–19 秒/query 的额外延迟。[arXiv](https://arxiv.org/abs/2609.00470?utm_source=chatgpt.com)

你可以追求：

\[
\boxed{
no generation-time LLM judge
}
\]

而把大量工作放在：

\[
\text{retrieval-context numerical features}.
\]

---

# 20. 防御具体到工程实现，可以压成三层

### 第一层：纯数值、always-on

每个 query：

\[
K=20\text{ or }50
\]

直接计算：

- query relevance
- local density
- rank margin
- source concentration
- pairwise cosine
- same-source pair count

全部来自已有 embedding 和 retrieval metadata。

**几乎可以 CPU 跑。**

---

### 第二层：小模型、conditional

只有当：

\[
R_{pair}>\tau
\]

时，对前 1–3 个 pair 做：

\[
NER+NLI.
\]

不调用外部 LLM。

183M NLI encoder 本身就是固定分类器，不需要自由生成。[Hugging Face](https://huggingface.co/cross-encoder/nli-deberta-v3-base/blob/main/README.md?utm_source=chatgpt.com)

---

### 第三层：pairwise reranking

最后：

\[
s_i'
=
s_i-\lambda r_i
\]

以及：

\[
s_{ij}'=
s_i+s_j-\gamma r_{ij}.
\]

做一个轻量 greedy selection。

这样整个 online path 都不需要 GPT judge。

---

# 21. 防御模型应该怎么训练？

我不建议直接训练一个：

\[
MLP(e_i)\rightarrow\{clean,poison\}.
\]

太容易回到 TRIS / RAGDEFENDER。

应该训练：

\[
\boxed{
f_\theta(F_q)\rightarrow R(C_q)
}
\]

其中输入是整个 context 的统计摘要。

例如 15–30 个 scalar features。

然后：

\[
f_\theta
=
\text{Logistic Regression / XGBoost / tiny MLP}.
\]

其实甚至 XGBoost 都够。

这就是非常低成本的：

\[
\text{feature engineering}
+
\text{lightweight learner}.
\]

---

# 22. 最重要的训练集设计

防御不能只用：

\[
PoisonedRAG.
\]

至少需要：

\[
\{
PoisonedRAG,\;
CamoDocs,\;
CRCP,\;
InceptionRAG,\;
ChunkTrojan
\}.
\]

然后最好：

\[
Train:
\{PoisonedRAG,CamoDocs,CRCP\}
\]

\[
Test:
\{InceptionRAG,ChunkTrojan\}
\]

再反过来一次。

这样才能回答：

> 这个 detector 学的是“攻击家族”，还是学到了真正的 retrieval-context footprint？

---

# 23. 你提出的“冲突是根源”需要稍微修改

我会把你的直觉改成：

> **投毒的根源不是“信息冲突”，而是“检索到的 evidence set 与真实证据结构之间的不一致”。**

然后：

\[
\text{conflict}
\]

只是 evidence inconsistency 的一种。

其它 inconsistency 可以是：

\[
\text{source concentration}
\]

\[
\text{abnormal co-retrieval}
\]

\[
\text{redundancy}
\]

\[
\text{unsupported bridge}
\]

\[
\text{query-context mismatch}
\]

\[
\text{joint influence concentration}.
\]

这样一来，防御理论就不会被“必须存在 contradiction”卡死。

---

# 24. 我认为最漂亮的攻防对偶其实是这个

ChunkTrojan：

\[
\boxed{
\begin{aligned}
&\text{minimize individual risk}\\
&\text{maximize pair retrieval}\\
&\text{maximize pair attack gain}
\end{aligned}
}
\]

RAGShield：

\[
\boxed{
\begin{aligned}
&\text{estimate individual risk}\\
&\text{estimate pair risk}\\
&\text{minimize risky evidence composition}
\end{aligned}
}
\]

所以：

\[
\boxed{
\text{Attack: compositionality}
\quad\leftrightarrow\quad
\text{Defense: composition integrity}
}
\]

这是比“攻击 + 一个 unrelated detector”更完整的 thesis。

---

# 25. 最后做一次工程风险审计

| 项目 | 风险 | 我的判断 | 解决方案 |
|---|---|---|---|
| 两 chunk 同时 Top-K | 高 | 最大风险 | 先做 CoRecall PoC |
| 两 chunk 联合才产生攻击 | 高 | 必须证明 | single vs pair 对照 |
| unknown chunker | 高 | 全黑盒很难 | 固定 chunker 做主实验，多 chunk size 做 transfer |
| CamoDocs 优化太慢 | 中高 | 不能照搬 1500-step | 用 CamoDocs proposal + exact post-chunk scoring |
| generation objective | 高 | 直接优化 LLM 太贵 | local surrogate，最终 Qwen 验证 |
| embedding camouflage | 中 | 已被 CamoDocs 占据 | 只作为 constraint，不作为 novelty |
| chunk-aware attack | 中高 | CRCP 已做 | 强调 compositional sufficiency vs local sufficiency |
| InceptionRAG overlap | 中高 | 必须处理 | 强调 single-source/victim-induced chunks |
| RAGShield embedding detection overlap | 高 | 必须避开 | pair/set-level representation |
| entity contradiction | 中 | 有用但非必然 | 作为 conditional feature |
| sub-1B KG | 高 | 容易不稳定 | 不生成 KG，使用 fixed-output NLI |
| clean multi-hop false positive | 高 | 很现实 | clean multi-hop calibration + soft rerank |
| adaptive attack | 高 | 论文审稿重点 | held-out CamoDocs/Inception/ChunkTrojan |
| 计算成本 | 低到中 | 可控 | 检索缓存 + 小模型 + CPU feature learner |

---

# 26. 所以我的最终建议已经比较明确

**ChunkTrojan：先不要追求“强”。先证明一个现象。**

第一阶段只回答三个问题：

\[
\boxed{
CoRecall@K>0?
}
\]

\[
\boxed{
ASR(c_1),ASR(c_2)\ll ASR(c_1,c_2)?
}
\]

\[
\boxed{
c_1,c_2\text{ individually look normal?}
}
\]

三个都成立，ChunkTrojan 就基本站住了。

然后才加入 CamoDocs-inspired stealth optimization 和 CRCP-inspired chunk robustness。

---

**RAGShield：不要做 KG detector，也不要做第五种 clustering。**

我建议把核心收敛成：

\[
\boxed{
\text{Lightweight Source- and Pair-Aware Retrieval-Context Integrity Reranking}
}
\]

底层：

\[
\text{embedding/rank/provenance}
\]

中层：

\[
\text{pairwise structural features}
\]

可选：

\[
\text{small NLI logits}
\]

最终：

\[
\boxed{
\max_{\text{context}}
\sum relevance
-
\lambda\sum pairwise\ risk
}
\]

整个 online 防御不调用外部 LLM。

这条路线的最大优点是：**ChunkTrojan 如果成功，它自动提供了 RAGShield 最需要的 adversarial training/evaluation case；RAGShield 反过来又能验证 ChunkTrojan 是否真的绕开了现有单点检测。**

而且你目前已经具备固定 4 档 chunk 索引、Top-1000 精确背景、query vector、source/chunk retrieval 元数据，以及本地 GPU 做最终生成验证的基础设施，所以这个方案并不要求你重新搭一个大型系统。

我会把整个项目的真正核心假说压缩成一句话：

\[
\boxed{
\textbf{RAG poisoning can hide at the individual-chunk level while remaining detectable at the evidence-composition level.}
}
\]

**这句话同时是 ChunkTrojan 的攻击命题，也是 RAGShield 的防御命题。**