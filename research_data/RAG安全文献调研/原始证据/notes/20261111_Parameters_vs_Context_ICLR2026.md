# Parameters vs. Context: Fine-Grained Control of Knowledge Reliance in Language Models

## 核查结论

- **精读等级：L3。** 本次以 ICLR 2026 正式论文版为准，逐页阅读 23 页，覆盖正文、参考文献和附录 A–E；不是仅依据摘要判断。
- **既有记录检查：** 在论文库文件名、调研笔记、`调研记录.jsonl`、`归并记录.json` 中检索完整题名、`CK-PLUG`、arXiv ID `2503.15888` 及作者名，没有找到本论文既有 PDF、笔记或元数据记录，故此前没有可复用的 L3。本地确有同作者的 Context-DPO、Beyond Black-Box Interventions 等独立论文笔记，不是本论文。
- **正式身份：** Baolong Bi, Shenghua Liu, Yiwei Wang, Yilong Xu, Junfeng Fang, Lingrui Mei, Xueqi Cheng. *Parameters vs. Context: Fine-Grained Control of Knowledge Reliance in Language Models*. ICLR 2026 正式会议论文。按所给《第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）》第 57 页“人工智能”会议 A 类第 7 项，ICLR 为 CCF-A。
- **版本：** arXiv `2503.15888v1`，2025-03-20 提交；arXiv API 的 published 与 updated 时间均为 `2025-03-20T06:26:28Z`。本次阅读及入库的是 ICLR proceedings 正式版，而不是将预印本冒充正式版。官方 proceedings 标注 “Published as a conference paper at ICLR 2026”。
- **官方证据：** [ICLR proceedings 记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ae82a60c5ce50b5c4d18cfe3214eb684-Abstract-Conference.html) · [ICLR 正式 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/ae82a60c5ce50b5c4d18cfe3214eb684-Paper-Conference.pdf) · [arXiv 2503.15888v1 版本记录](https://arxiv.org/abs/2503.15888v1)。OpenReview 网页未作为下载或阅读前提，未尝试绕过访问控制或验证码。
- **本地正式版：** [ICLR 正式 PDF（相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Parameters vs. Context_ Fine-Grained Control of Knowledge Reliance in Language Models.pdf>)
- **SHA-256：** `7AB3497AAD66CE9D552FA09051C22DF67D2E1AA941B2AFEEB0AE324526769EE4`
- **文件核验：** Poppler `pdfinfo` 报告 23 页、Letter 页面、PDF 1.5；本地逐页文本提取覆盖第 1–23 页，首面题名与 ICLR proceedings 记录一致。PDF 元数据 Title 字段为空，因此身份以正式 proceedings 记录和首页为准。2026-11-15 重新计算的本地 SHA-256 与 ICLR 官方正式 PDF 的 SHA-256 相同；此项核验不改变既有阅读范围。

## 逐页阅读位置

| PDF 页 | 阅读内容与证据位置 |
|---|---|
| 1 | 正式标题、作者、摘要、引言开头；提出 CK-PLUG、Confidence Gain 与可调知识依赖。 |
| 2 | 引言及图 1；明确目标是在过时参数知识与不可靠/对抗检索上下文之间可双向调节；方法概览。 |
| 3 | 预备知识、熵定义；第 3.1 节开始，区分 query-only 参数分布与 query+retrieval 分布。 |
| 4 | 图 2、3；熵变化观察及 `CG = H(p(x|Xq)) - H(p(x|Xr+Xq))`，用负值指示上下文引入后置信度下降的候选冲突 token。 |
| 5 | 图 4、式 (5)–(9)；参数感知与上下文感知分数、top-k 候选词并集及 α 调节公式。 |
| 6 | 表 1：NQ、ConFiQA、MQuAKE 上四个模型的显式控制结果；第 3.3 节自适应 α 式 (10)；实验设置与反事实上下文构造。 |
| 7 | 表 2：六项 KILT RAG 任务；ConR、ParR、MR 指标与适应性增强结果；第 5.1 节结果解释。 |
| 8 | 图 5 的 α-MR 曲线、表 3 的冲突检测消融；去除冲突检测时命中率在极端 α 下明显退化；开始 token-level 深入分析。 |
| 9 | 图 6、7：参数/上下文 token 概率与分布随 α 的变化；案例研究说明及结论。 |
| 10 | 表 4 案例；致谢、伦理与可复现性陈述；参考文献从 Achiam 开始。 |
| 11 | 参考文献：Bi、DOLA、数据集、RAG 调查、检索与幻觉工作等。 |
| 12 | 参考文献：检索、知识编辑、事实性、context-faithfulness 等。 |
| 13 | 参考文献：KILT、熵、内部状态、RAG/上下文解码及知识冲突等。 |
| 14 | 参考文献：事实性、RAG、数据集与 hallucination 相关工作。 |
| 15 | 参考文献收尾；随后为附录。 |
| 16 | 附录 A Related Work；附录 B Confidence Gain 的支持上下文示例及阈值化式 (11)。 |
| 17 | ε 的模型专属设置；附录 C.1 反事实 NQ、ConFiQA、MQuAKE 的构造与数据来源，以及一般任务数据集说明。 |
| 18 | 六类 KILT 数据集、Wikipedia 2019-08-01 语料、分段与 BGE 检索配置；指标定义、提示词设置。 |
| 19 | 各任务提示模板与表 5；附录 D 知识敏感 token 捕获算法说明开始。 |
| 20 | Algorithm 1；在生成期间查找参数答案/上下文答案 token 或其子串并抓取分布；附录 E 案例研究开始。 |
| 21 | 表 6、7：LLaMA2 与 LLaMA3 的反事实上下文案例。 |
| 22 | 表 8：Mistral 的反事实上下文案例。 |
| 23 | 表 9：Qwen 的反事实上下文案例，全文结束。 |

## 方法与实验

CK-PLUG 是无需改权重的解码时插件。对每步 next-token 分布分别计算参数知识 `p(x|Xq)` 与 RAG 分布 `p(x|Xr+Xq)` 的熵差。作者将 `CG < 0`（附录中使用带模型专属 ε 的条件）视作潜在知识冲突 token；只对此类 token 干预，其他 token 保留原 RAG 分布。参数分数定义为 `q_para = log p(x|Xq)`，所谓 context-aware 分数定义为 `q_cont = log[p(x|Xr+Xq)/p(x|Xq)]`。在联合 top-k 词集合上，对 `α q_para + (1-α) q_cont` 做 softmax；α 越大越偏参数知识，越小越偏上下文。自动模式设 `α = H_cont / (H_para + H_cont)`，以两个条件分布的熵调节偏好。

显式控制实验在含反事实检索内容的 NQ、ConFiQA、MQuAKE 上使用 LLaMA2-7B、LLaMA3-8B、Mistral-v0.3-7B、Qwen2.5-7B；指标为上下文一致率 ConR、参数一致率 ParR 与 `MR = ParR/(ParR+ConR)`。自适应实验评估 NQ、HotpotQA、FEVER、T-REX、ELI5、WoW；语料为 2019-08-01 Wikipedia dump，作者称切分后约 28,773,800 段，使用 BGE-base-en-v1.5、top-10 检索；每项任务随机抽 1,000 条，输出长度上限 64、生成 top-k=100。

- **显式控制结果：** 表 1 中 LLaMA3-8B 的 NQ MR 从 α=0 的 9.9% 到 α=1 的 71.9%；α=0.5 为 42.1%，表中 baseline 为 43.5%。其余模型与任务也显示 α 能改变对反事实上下文或参数答案的偏向。
- **自适应结果：** 表 2 报告四个模型在六任务平均值上相对标准 RAG 有小幅提升：LLaMA2 36.4→38.3、LLaMA3 42.3→43.5、Mistral 45.1→45.7、Qwen 45.4→45.9。分任务并非全都提升，例如 Qwen 的 T-REX 从 61.6 降至 60.2，LLaMA3 的 FEVER 从 86.4 降至 86.1。
- **消融：** 表 3 的 hit rate 将输出包含参数真值或反事实上下文答案都视为命中，说明冲突筛选能避免粗暴调节造成的文本/答案退化；该指标本身不等同于攻击成功率、防御检出率或事实安全率。

## 局限与核验问题

1. **冲突信号不等于恶意性。** `CG < 0` 表示上下文加入后 token 熵升高，不是来源真实性或投毒检测。若误导上下文让模型对错误答案变得更确信，熵可能下降，负 CG 规则未必触发。这是由判据推导出的安全风险，本文没有报告此类攻击压力测试。
2. **context-aware 项是似然比。** 式 (6) 定义 `q_cont` 为 `log p_RAG - log p_para`，不是 `log p_RAG`。因此按式 (8)，α=0 时 softmax 的对象是参数与 RAG 的 log-likelihood ratio，并非通常意义上直接采用检索条件分布；α 混合也不是两个归一化概率分布的凸组合。该实现含义应在复现时核实，不应把 α=0 无条件解释为“直接照抄检索上下文”。
3. **论文内部基线数字不一致。** 摘要页 1 写 LLaMA3-8B NQ 的 baseline MR 为 42.1%，页 2 写 42.09%；但表 1 页 6 baseline 列为 43.5%，42.1% 对应 α=0.5 行。后续引用数值应以表格并注明该差异，不要混写成同一个 baseline。
4. **阈值需按模型调节。** 附录 B 给出的 ε 分别为 LLaMA2 -2、LLaMA3 -1、Mistral -1、Qwen -3；未证明跨模型统一阈值或迁移校准。自适应 α 也依赖熵能代表可靠性的启发式假设。
5. **部署开销证据不足。** 参数分布需 query-only 条件，RAG 分布需 query+context 条件；方法还对 token 分布、联合 top-k 与熵作逐步操作。论文称 plug-and-play，但未报告相对普通 RAG 的端到端延迟、吞吐或显存开销，B 的在线预算比较不能直接借用其“轻量”描述。
6. **安全评估范围有限。** 反事实上下文是知识冲突压力测试，但正文没有对单源语料投毒、检索器污染、提示注入、攻击者知识/能力、未知 chunker 或分布式同源互补块作威胁建模；也未报告 ASR、clean-query 误删率、precision/recall 等毒块检测指标。
7. **可复现信息有一处不一致。** 首页给出公开 GitHub `byronBBL/CK-PLUG`，可复现性陈述页 10 又称 anonymous 4open.science repository。本文笔记未核验代码与补充物，不能据此宣称代码实现已经验证。

## 对开题 A/B 的关系

这里的 A/B 按[开题研究内容源文件](<../../../../partitions/section3_content.tex>)定义：A 是仅改写单一源文档、由受害系统未知分块后形成同源互补角色块并共同进入 Top-K 的投毒攻击；B 是检索后、生成前，结合检索统计/语义特征、跨块关系、异源参照和选择性 LLM 复核的上下文净化。

- **A：间接相关，不是直接攻击撞车。** 论文不构造或优化投毒载荷，不研究未知分块、单一源文档预算、同源角色块共同召回/共同必要性，也没有 A 的攻击成功协议。它提供了“错误检索上下文与参数知识冲突时，生成器如何偏向哪一边”的可调机制，可作为 A 端到端生成器层压力测试或下游对照，但不能替代 A 攻击。
- **B：强近邻与直接 claim-narrowing，控制层不同。** 本文直指 RAG 中参数知识与上下文冲突、可按场景调节 reliance，故会压缩“首次提出适应不可靠上下文、平衡参数/外部知识”的宽泛表述。它在解码时调 token 分布，不识别或删除恶意块，不建模来源/跨块关系，不做 clean-query query-level 误报校准，也不以正常多跳桥接证据保留为目标。B 的检索后净化与此生成时控制不是同一方法；可将 CK-PLUG 作为后续可组合/对照的生成层方法，并实测是否互补及额外延迟。
- **建议定位：** 在相关工作中明确其为 ICLR 2026 CCF-A 的参数—上下文知识依赖控制近邻；将 B 的贡献边界写成“检索阶段恶意上下文识别与选择性净化、跨块同源/命题关系及干净查询校准”，避免将一般的参数/上下文偏好调节表述为本课题首创。

## 引用信息

Bi, Baolong, Shenghua Liu, Yiwei Wang, Yilong Xu, Junfeng Fang, Lingrui Mei, and Xueqi Cheng. “Parameters vs. Context: Fine-Grained Control of Knowledge Reliance in Language Models.” *Proceedings of the International Conference on Learning Representations (ICLR)*, 2026. arXiv:2503.15888v1 (2025).

[返回证据地图对应条目](../../../../docs/RAG安全证据地图_20261102.md#src-20261111-parameters-vs-context)
