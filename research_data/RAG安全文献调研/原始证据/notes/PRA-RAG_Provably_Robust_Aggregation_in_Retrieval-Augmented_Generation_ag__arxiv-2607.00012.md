---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2607.00012
report_id: arxiv-2607.00012--33b844d71174
reading_level: L3
checked_date: 2026-11-18
---
# PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption

**PRA-RAG是B的组合几何与鲁棒子集选择近邻。它给出的表示中心偏移界、干净子集选择和最终回答安全是不同的结论；组合严格多数、几何可分和采样误差的条件必须分别检查。** 正式全文及附录已读，公开同名仓库已静态核查，尚未运行或复现。

## 身份、版本与作者冲突

- 正式发表：Findings of the Association for Computational Linguistics: ACL 2026，pp.36002–36017，2026年7月；DOI `10.18653/v1/2026.findings-acl.1794`。Findings未在用户给定的第七版CCF目录单列，不能直接继承ACL主会A类。
- 正式PDF顺序：Xue Tan、Yi Zheng、Chang Huo、Yunruo Zhang、Yu Liu、Hao Luan、Zhuyang Yu、Xiaoyan Sun、Ping Chen、Jun Dai；机构为复旦大学的School of Computer Science、Institute of Big Data及Worcester Polytechnic Institute的Department of Computer Science。
- 2026-11-18实际读取的ACL网页及BibTeX末三位为 **Jun Dai、Xiaoyan Sun、Ping Chen**，正式PDF为 **Xiaoyan Sun、Ping Chen、Jun Dai**。arXiv题名页与正式PDF顺序一致。保留来源冲突，不把网页、导出书目和PDF称为完全一致；现有Bib key `tan2026prarag`保留，本次未改BibTeX。
- 官方PDF下载响应200，4,065,287字节、16物理页，SHA-256 `33b844d71174ee19ed35fcbc6f4b17de590879a658e1de395c542accadb00fa6`，与科研数据库既有文件逐字节一致。

## 实际阅读范围

阅读等级L3：正文p1–9及声明已读；p11附录A.1–A.2、p12–13附录A.3–A.5和B、p14–16附录B.3及C.1–C.3已读。p9–11参考文献浏览，未逐条跟读。p6算法2、p12采样界、p13几何假设和p15表9另经渲染目视核对。本次填补的是既有L2尚缺的p2及附录；独立研究数不增加。旧PDF版本只做过题名核对，不因正式版补读自动获得同样等级。

## 方法、访问权限与部署接口

p3–4 §3允许向外部语料注入毒段，检索结果Top-K中最多ε段被改变；攻击者知道检索器，不知道生成器权重或解码。p4 §4把每个大小n的段落组合表示为按原顺序拼接的嵌入，在所有 `L=C(K,n)` 个组合中，寻找覆盖严格多数的最小角距离球，其中心对应待选子集；随后按query相似度对所选段落表示加权。

论文区分组合选择和生成器输入：p13 B.1称开放模型可用embedding层，黑盒模型经Llama3-8B抽取/解码聚合表示再作为上下文，但没有给出足以完全重建该黑盒解码过程的细节。下述候选仓库仅含Mistral源码，不能据此补齐论文所有模型的接口。

## 定理、干净多数与几何假设

p5 §5及p11 A.1通过同一组合全集中的两个严格多数球必有交点、再用角距离三角不等式，推出精确中心间偏移不超过2R；β近似版本推得 `(1+β)Rhat`，论文用β=2。R的定义本身要求对所有预算内扰动满足多数覆盖；定理陈述不等于已经证明任何经验半径都能替代R。p6式9–10使用F，p11 A.2证明使用Fhat，近似与精确符号未完全一致，保留实现映射未决。

p12–13 A.4通过 `Ladv=L−C(K−ε,n)` 和零基索引 `k=floor(L/2)+Ladv`，给出该半径球内至少 `floor(L/2)+1` 个干净组合的计数。其前提是 `C(K−ε,n)>C(K,n)/2`；球内有多数干净组合，不自动说明中心对应的子集干净。

p13 A.5另外要求：干净组合集中于某个半径Rc的球，所有含毒组合处在Rc+Δ之外，Δ>0。作者明确说明Δ=0时不能由几何信息保证选出全干净子集。因此主文p4“不假设严格几何可分”的说法，不能覆盖附录用可分条件连接到干净选择的主张；中心稳定、干净选择和答案正确须分开。上述界也没有直接覆盖query级最终删块误报或正常多跳关键证据保留。

## Monte Carlo保证和实验参数的算术核查

p12 A.3的结论是：固定最优球在总体中的覆盖比例满足 `q>0.5+τ`，且 `m≥log(2/η)/(2τ²)` 时，以至少1−η概率有 **样本多数球半径R*≤总体半径R**。它表明采样可能低估半径，不能推出拿R*作保守认证上界。作者也明确没有仅由均匀采样得到 `R≤(1+τ)R*` 的确定性保证。普通严格多数只要求略高于1/2，不保证任意指定的τ裕量；`m=200, τ=0.1` 对应失败概率上界约0.0366，不能外推所有参数。

下面只运行组合计数算术，没有运行论文模型。ε按p13 B.1所述投毒比例向下取整；表9注明K=20、20%投毒，因此ε=4。

| 论文设置 | 总组合L | 完全干净组合C | C/L | 严格多数 | 认证索引k / 最大合法索引 |
|---|---:|---:|---:|---|---|
| 默认K=8、ε=1、n=3 | 56 | 35 | 62.50% | 满足 | 49 / 55 |
| 表9 K=20、ε=4、n=3 | 1140 | 560 | 49.12% | 不满足 | 1150 / 1139 |
| 表9 K=20、ε=4、n=4 | 4845 | 1820 | 37.56% | 不满足 | 5447 / 4844 |
| 表9 K=20、ε=4、n=5 | 15504 | 4368 | 28.17% | 不满足 | 18888 / 15503 |

表9参数超出算法2的严格多数前提，不能用其中低ASR/PAD宣称该条件定理已覆盖更大污染；这不是预算内定理的反例，也不抹去其经验结果。作者所述采样PAD偏差通常约3%是实验观察，不是上述缺失的反向界。

## 结果、效用与成本

| 正式PDF位置 | 可核对的同配置结果 | 解释范围 |
|---|---|---|
| p8 Table2，MS-MARCO/Mistral-7B，K=8、20%、PoisonedRAG | PRA-RAG clean ACC0.57、攻击ACC0.63、ASR0.01；Vanilla clean0.58 | 是63%/1%的配对，不能替换成摘要的71%/1%。p7正文同设置称62%，与表1/2的63%保留差异。 |
| 同表，MS-MARCO/Vicuna-7B | PRA-RAG clean0.63、攻击0.68、ASR0.01；Vanilla clean0.73 | 68%/1%并伴clean ACC下降10个百分点，不能声称所有设置效用无损。 |
| p1摘要与p2引言 | 作者概括ACC71%/ASR1% | 本次已读主表未将这两个数对齐为同一明确配置，按作者概括记录，不替代可核表格。 |
| p8 Table2，HotpotQA/Mistral | PRA-RAG clean0.49、攻击0.37、ASR0.03；Vanilla clean0.55；RobustRAG攻击0.56/ASR0.24 | 安全与正确率存在权衡；HotpotQA参测本身不证明全部必要桥接块被保留。p7 Table1的同方法clean0.38与Table2的0.49亦未闭合。 |
| p9 Table3，100 queries | NQ/MS-MARCO/HotpotQA响应5.98/6.20/6.17秒 | 特定环境端到端测量；p13列出四张80GB A100，不能与B单项特征毫秒成本跨硬件直接比较。 |
| p15–16 Table10–11 | Vicuna/NQ K16 n3的64.93→9.23秒；K12 n5的116.09→7.17秒 | 采样减少枚举开销；K8 n3仅56组合，未触发m=200采样，不是每个配置都有同样收益。 |

## 公开仓库：可访问性、实现差异与完整性

正式PDF p9只承诺以后发布代码，全文超链接和arXiv题名页均未指向下述仓库。此前报告提供的 `simpleaday/PRA-RAG` 当前网页200、README与方法同名，固定commit为 `7889536fe904d0eecbbb3a3114b7758b161900d6`；这是**已核公开候选实现**，作者官方归属仍待进一步证据，不能仅因同名就写为已确认作者制品。

已静态读取README、主流程、Mistral实现、模型导入和工具路径。未安装依赖、执行仓库或推理。API请求曾因速率限制403，随后网页/固定ZIP可访问；403不是仓库失效证据。ZIP包SHA-256 `fb098fefca0ef1722fedaeba139b2da4791641238969a942fde372b03be374da`。

| 固定commit路径与行号 | 读到的实现 | 与论文/复现的关系 |
|---|---|---|
| `main.py:171–193` | 固定选择`int(top_k*poison_ratio)`个本query毒段，补齐正常段；传入已知毒段数量 | 是控制Top-K污染比例的评估入口，不能凭它宣称完成语料注入后自然检索成功的端到端实验；已知ε仅参与PAD计算，不把此路径说成中心选择本身读取标签。 |
| `src/models/Mistral.py:147–166` | 先把组合文本拼接，再用Contriever编码 | 不同于p4把每篇表示按位置拼接为nd维向量的描述；组合几何/定理对象不能直接视作同一实现。 |
| 同文件174–200 | 角距离多数邻域选中心；PAD索引越界时截到最后一项，然后乘3 | 截断避免程序索引错误，不恢复不满足严格多数时的认证前提。所读文件没有Monte Carlo采样路径。 |
| 同文件99–138、21–50 | token embedding插值对齐、检索分数softmax权重，`inputs_embeds`送Mistral生成 | 提供开放Mistral的具体融合参考；与论文按query相似度原始归一化权重的式4存在差别，未验证黑盒路径。 |
| `main.py:213–248` | 分子要求judge判目标答案且所选子集仍保留毒段；最终除以全部M个query | 是“目标判定且保留毒段”的联合事件，不能混同只看最终目标答案的ASR，尚未核影响大小。 |
| 仓库清单、README及导入语句 | 未见`requirements.txt`、LICENSE/COPYING、`src/models/Model.py`、四个被导入的模型源码和`src/contriever_src`；主脚本调用`save_results`但所读utils未定义；两项可视化函数被调用却未在所读源码定义或导入；有若干pyc | 当前公开包缺少必要源码/入口依赖和许可，不是已核完整可运行复现包；没有通过反编译pyc补造阅读或执行信用。 |

`Mistral.py` SHA-256 `27ef0b54deead129ecd521ede8e41eeccdd0bce5bafa88b50679f2bf8b968220`；`main.py` SHA-256 `0b0cdaa4957fd0ee867f96557ba18c212edd255e242442c0eeb905b1ccfef127`。仓库默认K=5、n=3不满足论文算法1的2n<K；即使改为论文默认值，也不能据静态核查称完成复现。

## 与开题A/B的关系

**B的直接近邻：** 检索后组合嵌入几何、多数邻域选择及效用/ASR联合评价均已有；冻结表示或“有理论保证”本身不能作为B的空白。可比较四统计/RF与其组合选择在相同检索器、污染预算和clean-query最终动作误报下的增益；来源/偏移、桥接实体和时态/作用域命题关系对正常多跳保留的实际贡献仍需实证。PRA-RAG的中心偏移认证不同于B所需的最终删块误报控制。

**A的边界：** 论文以Top-K段落替换/投毒为威胁模型，没有验证单份真实长源、未知chunker、同源互补块共同必要的完整交集。提高n可稀释单块影响，也会降低完全干净组合的比例；任何攻击比较应先核算严格多数前提，超出参数域不能声称推翻其定理。不能由本篇未测完整交集推断整个文献域没有近邻。

## 来源、文件与待核事项

- [正式页面](https://aclanthology.org/2026.findings-acl.1794/)；[官方BibTeX](https://aclanthology.org/2026.findings-acl.1794.bib)；[正式PDF](https://aclanthology.org/2026.findings-acl.1794.pdf)；[arXiv题名页](https://arxiv.org/abs/2607.00012)。题名/发表信息已核，作者顺序冲突如上。
- [公开候选仓库固定commit](https://github.com/simpleaday/PRA-RAG/tree/7889536fe904d0eecbbb3a3114b7758b161900d6)。作者官方关联、完整发布包及许可证待核。
- [科研数据库正式PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/PRA-RAG_ Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption.pdf>)；同题旧版[PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/版本/286c23f4ebe9/PRA-RAG_ Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption.pdf>)仅保持既有L1题名核对，不授正式版L3。
- [证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-18ff50f3b5d89921>)；[元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md>)；[技术报告](<../../../../docs/RAG安全文献攻防技术手段总结报告.md>)。

<a id="D03"></a>
Google Scholar引用数仍未核，留待正文与制品工作后统一处理；优先级未重算。逐query结果、理论量到经验PAD的完整对应、黑盒聚合路径、作者冲突和仓库官方归属仍待核实。
