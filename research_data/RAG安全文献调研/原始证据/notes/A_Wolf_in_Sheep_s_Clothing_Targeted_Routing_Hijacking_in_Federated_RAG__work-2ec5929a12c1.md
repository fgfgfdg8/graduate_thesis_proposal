---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-2ec5929a12c1
reading_level: L3
checked_date: 2026-11-19
venue: "EMNLP 2026 Main"
ccf: "B"
doi: "10.18653/2026.emnlp-main.668"
pdf_sha256: "a49111085ee4114797439c6b7ee6509907f7a7e34c242ee30f14e95bfe0ae582"
pdf_pages: 24
---
# A Wolf in Sheep’s Clothing: Targeted Routing Hijacking in Federated RAG

**阅读状态：L3（正文全文）+ 附录定向阅读。** 已读正式EMNLP 2026 PDF正文pp.1–10及附录A–J的关键方法、实验、防御与限制（pp.12–24）；参考文献pp.11未逐条核对，未把附录中的全部表格逐项复算。阅读对象是ACL Anthology正式版，不是预印本替代。

## 正式身份

- **作者/机构**：Junjie Mu（Politecnico di Milano）；Qiongxiu Li（Aalborg University，通讯作者）。
- **年份/会议/track**：2026 / EMNLP 2026 Main / main_research；正式主会论文，不是Findings、Industry或Workshop。
- **CCF**：第七版目录中EMNLP主会为CCF-B；本文按正式主会记B，不把Findings等级外推。
- **正式出版信息**：Proceedings of EMNLP 2026, pp.15388–15411；[ACL Anthology](https://aclanthology.org/2026.emnlp-main.668/)；[DOI](https://doi.org/10.18653/2026.emnlp-main.668)；[BibTeX](https://aclanthology.org/2026.emnlp-main.668.bib)。
- **版本关系**：仓库README标注arXiv:2605.28112；[arXiv页面](https://arxiv.org/abs/2605.28112)题名与正式版一致。本文的科学判断以正式EMNLP PDF为准；arXiv只作版本线索，不把两版字段等同。
- **本地PDF**：[正式EMNLP PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/A Wolf in Sheep’s Clothing_ Targeted Routing Hijacking in Federated RAG.pdf>)，24物理页，4,029,216 bytes，SHA-256 `a49111085ee4114797439c6b7ee6509907f7a7e34c242ee30f14e95bfe0ae582`。
- **代码**：[官方仓库](https://github.com/Junjie-Mu/routing-hijacking-fedrag)，HEAD `56319576268fcfa97458d62d4f4e6ce02344c2ef`；只读核验了仓库入口与README，未克隆、未安装、未运行或复现。

## 一句话总结

FedRAG中客户端只用语义profile向服务器声明本地语料，服务器无法核验profile与真实语料的一致性；恶意客户端可用目标域proxy伪造profile，在预检索路由阶段劫持query，再返回有害、缺失或被投毒的evidence。论文提出TASR，用返回evidence的查询相关性、profile一致性和跨客户端一致性做在线信任重加权，降低重复query上的持续劫持，但不能识别语义相关且profile自洽的虚假证据。

## 方法

### 1. FedRAG路由与威胁模型

系统有客户端集合 `C`，每个客户端持有私有语料 `D_i`，服务器不能直接读取语料。客户端上传语义profile：

`P_i = Φ(D_i)`

服务器按query `q` 计算路由分数 `S_i(q)=R(q,P_i)`，选择Top-K客户端集合 `T_K(q)`；只有被选中的客户端返回证据。攻击者控制客户端集合 `C_adv`，可伪造上传的profile，并控制被选中后返回的证据；不读取诚实客户端语料、不修改服务器router、不破坏隐私机制。成功劫持的一阶条件是：

`T_K(q) ∩ C_adv ≠ ∅`

这是**预检索访问控制失败**，不是检索块的语义投毒；下游失败只有在获得路由访问后才测量。

### 2. 三类router与攻击实例

- **embedding-based routing**：把目标域proxy文本嵌入后取均值或K-Means centroid；单向量余弦路由下，目标query embedding的归一化centroid方向最大化总相似度（Proposition 1，附录B）。
- **neural routing / RAGRoute**：伪造同一个目标域centroid-style profile，但攻击效果经学习到的query–client MLP打分器过滤；论文没有把centroid最优性无条件搬到神经router。
- **LLM-based routing / ReSLLM**：伪造自然语言的“通用能力”来源描述，夸大目标域覆盖；157个合法源加3个恶意源时，HR@1为73%、HR@3为97%。

攻击者只需要目标域proxy，主要是公开文本或目标query分布样本；不需要诚实客户端的私有语料。

### 3. TASR

TASR不替换router，而是在未来query的路由分数上乘客户端信任权重：

`Ŝ_i(q) = S_i(q) τ_i`

其中

`τ_i = s_i (u_i^rel)^α_r g_c(u_i^cons) g_a(u_i^agr)`

- `u_i^rel`：返回证据与query的检索相关性；
- `u_i^cons`：返回证据与已注册profile的一致性；
- `u_i^agr`：与其它足够相关客户端的跨客户端一致性；
- `s_i`：冷启动因子，随反馈累积从 `s_0` 趋向1；
- `g_c,g_a`：profile一致性和跨客户端一致性的软门控。

信任按反馈中位数更新：低于阈值则乘以衰减 `γ`，高于阈值则按 `γ_rec` 恢复；受 `u_min` 限制。TASR在获得反馈后才更新，因此不阻止第一次劫持，目标是重复客户端/重复query流上的后续抑制。

## 主要实验与结果

### 路由级劫持

| Router/setting | Malicious clients | HR@1 | HR@3 |
|---|---:|---:|---:|
| Embedding, Gaming/GIS/Physics (multi-domain K-Means) | 1 | 16–27% | 70–91% |
| Embedding, 同上 | 3 | 47–58% | 86–95% |
| RAGRoute neural router | 1 | 2.3% | 21.7% |
| RAGRoute neural router | 3 | 7.3% | 32.0% |
| ReSLLM universal description | 3 | 73% | 97% |

这里的HR是目标query的top-K集合中至少有一个恶意客户端的比例。embedding与neural的数值不能直接作鲁棒性排名，因为各router按原生设置评估。

### 下游生成

- harmful-content injection：K=1时，成功劫持后触发拒答的比例为embedding 96.3%、RAGRoute 100%；这是可用性破坏，不等同于事实错误。
- data poisoning：成功劫持后错误答案为embedding 83.3%、RAGRoute 83.4%；在K=3时条件错误率下降，但全query口径的暴露变化需分别报告。
- missing-information：embedding/RAGRoute在K=1的拒答/幻觉表现不同，不能把条件于劫持的分母当全query失败率。

### 医学压力测试

MedQA-USMLE的受控路由压力测试中，3个恶意客户端、100条医疗proxy passages时：

- 医疗profile HR@1为32.3%、HR@3为75.1%；
- 有诚实医疗客户端时的MedAcc@1从100%降到67.7%；
- 随机profile不进入top-K；非医疗profile可进入top-5但不进入top-1/top-3。

生成侧使用伪造医疗证据时，五种模型的ASR（Poisoned+Sycophancy+Conflated）为：Qwen3-4B 68%、Qwen3-8B 74%、MedGemma-1.5-4B 76%、Llama-3.1-8B 82%、Qwen3-30B-A3B 44%。这是**poisoned-context压力测试**，不是完整临床FedRAG部署，也不能把ASR全归因于routing。

### TASR与负结果

500-query在线流中，无防御的HR@1为35.6%（1个恶意客户端）和64.9%（3个）；Full TASR为3.5%和5.7%，post-warmup HR@1为0%，Acc@1约93.5%–95.2%。RAGRoute上HR@3从96.8%降到49.7%，Acc@3从92.1%升到97.6%，仍有残余top-K暴露。

最重要的负结果是**semantically relevant false evidence**：当错误证据保留完整问题、选项和医疗概念，只替换正确选项时，正确与虚假证据的relevance/consistency/agreement分数几乎相同；TASR不但不能抑制，1个恶意客户端时HR@3由51.8%升到87.1%，3个时由70.0%升到99.4%。因此TASR检测的是可观察的检索/画像不一致和重复路由，不是事实真值，也不是单query内部的恶意块证明。

### 既有防御为何不闭合

- HE routing保护profile和相似度计算机密性，但不改变被攻击的排序；plaintext与encrypted HR完全相同。
- Krum、Median、Trimmed Mean是针对FL模型更新聚合的Byzantine规则，不适配异构语义profile；自适应混合攻击下Krum在α约0.5时失效，Median/Trimmed Mean在多个混合比例下与无防御接近甚至更差。
- TASR是post-routing、按返回证据反馈的行为信任机制，不是来源真实性证书、不是块级恶意检测，也不是最终query级误删控制。

## 与开题A/B的关系

### A方向

**不同但相邻。** 本文攻击预算主要是客户端上传的routing profile；恶意客户端不需要控制一份真实长源并经未知chunker产生同源块，也不需要证明多个块在同一query中共同必要。其“恶意客户端进入检索路径”是比开题A更早的访问控制层。

**可直接借鉴的约束**：如果开题A把FedRAG、客户端选择或跨源路由纳入范围，必须把“profile-to-corpus一致性”列为独立威胁面；否则只测文档块内容会漏掉路由阶段的抢占。

### B方向

**强方法近邻，但不是完整撞车。** TASR把query-evidence相关性、profile一致性和跨客户端一致性作为公开可观测信号，这与B的来源/实体/命题关系信号和跨块一致性相邻。其关键限制是：语义相关的错误证据可以同时通过三种信号，且多个恶意客户端能互相支持，导致TASR在MedQA false-evidence设置中反而提高恶意top-K暴露。

**对B的具体约束**：

1. 不能只以“相关性+来源一致性+跨客户端一致性”证明事实真值；必须区分**支持关系**、**来源独立性**和**命题真实性**。
2. 不能把top-K客户端信任加权直接当作块级过滤；必须在单query内做块级/证据组合核验，并报告最终query级误删。
3. TASR的false-evidence负结果应作为B的消融/杀门禁：构造语义相关但事实错误的证据，检查检测器是否因relevance、profile consistency或agreement被误导。
4. 需要报告clean-query正常效用、跨客户端串谋和重复query/首次query的差异；TASR只覆盖重复query流，不保证首次攻击或单次query。

## 局限与证据边界

- 论文的医学实验是受控MedQA压力测试，不是临床部署；模型ASR不能直接外推到真实医院数据。
- TASR依赖返回证据和feedback exploration；不阻止首次恶意路由，也不保证将恶意客户端从top-K彻底移除。
- 语义相关、profile一致的虚假证据可使TASR失效；论文明确报告反而升高的HR@3。
- 代码仓库已有入口，但本次未运行、未复现、未审阅所有依赖和制品；开放源码不等于实验可复现。
- Google Scholar引用数未查询；本笔记不写0、不做优先级最终排名。
- 正文和附录已读，但未逐表重算、未逐条核对参考文献。

## 来源、阅读范围与追溯

- 正式PDF：[ACL Anthology PDF](https://aclanthology.org/2026.emnlp-main.668.pdf)，本地路径与SHA见上。
- 实际阅读：正式PDF正文pp.1–10（L3），附录A–J的选定页pp.12–24；参考文献pp.11未逐条核对。页数按PDF物理页计，正式文章页为15388–15411。
- 历史L1事件：2026-11-02曾只读官方缓存摘要，未取得PDF；该旧事件保留为历史，不覆盖本笔记的L3结论。
- [返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-09555a8efae68b6f)
- [全部逐篇笔记](../README.md)
