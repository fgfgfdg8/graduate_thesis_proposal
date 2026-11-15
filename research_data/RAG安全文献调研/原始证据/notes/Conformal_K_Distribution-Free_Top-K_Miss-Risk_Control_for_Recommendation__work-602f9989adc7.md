---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-602f9989adc7
reading_level: L2
checked_date: 2026-11-15
---
# Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees

**阅读状态：L2。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Guangrui Fan", "DanDan Liu", "Lihu Pan"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2026 / ACM Transactions on Information Systems / Journal article; regular/special-issue classification not independently verified
- **发表状态**：journal_version_of_record_volume_issue_assigned
- **CCF**：正式身份已核等级 ["A"]；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **代码**：No paper implementation repository confirmed. PDF github literal belongs to a cited data-set,not this paper code;not proof of absence.
- **关联标题**：["Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees"]

## 一句话总结与核心贡献

Held-out query calibration of monotone retrieval/list budgets for zero-relevant-item miss;fractional overlapping cohorts,strict-split survivor-conditional rerank calibration and direct2D/IW/windowed/LTT variants. Recall-loss extensions are also stated. Direct calibration neighbor;author claims and observed table values separated from identified proof/definition gaps.

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** At-least-one relevant hit and expected Recall-loss statements do not establish joint retrieval/necessity of complementary blocks from one real source under unknown chunking,or robustness across chunking changes.No payload/construction/reproduction produced.

**B：** Independent query/TopK calibration is prior-art neighborhood. No frozenModernBERT PCA16+four-statistic20D RF,source/entity/proposition conditions,heterosource reference or one-batchLLM structure is instantiated. Numeric query-max only covers its own event;relation OR that merely escalates calls differs from a relation-only path enabling deletion. Final deletion inherits a max-event bound only if the deletion event is contained in it;otherwise final policy risk needs coverage.

## 局限、可比性与不确定性

- 正式版物理p1–32及p35–42已作定向阅读；p4–5和p12–13算法框已核，部分图内细节和证明未逐项核，整体保留L2。
- ObservedY relevance differs from latent truth and all-support retention.
- Exact per-table/fold/seed query counts,stage2 survivor denominator,group raw counts and CI pooling unknown.
- Group/IW proof invokes false finite self-normalized expectation identity;group implication gap verified;not a blanket conformal-method rejection.
- FixedK/Recall loss directions conflict with displayed set definitions;cannot borrow truncation or all-support guarantee.
- 2D order/cross-fit/conditional rank/BH high-probability upgrade require extra conditions.
- POI cap/table means,group mapping,Figure4 scale and rank-preserving refinement effects unresolved;no table splicing.
- No empirical algorithm reproduction,code/preprint unconfirmed,sample reuse unknown,no ASR pooling.
- 独立原页复核及精确有理数计算给显示overlap-group选择器一个无条件边际风险超过alpha的反例；不能将该组定理作为B证明。普通split边际思想不因该反例被否定，作者实现未知。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### conformal-at-k-local-vor-L2-20261102

- **书目来源**：[原始页面](https://dl.acm.org/doi/10.1145/3828550)
- **DOI / arXiv**：10.1145/3828550 / 未核实 / 未提取
- **本地PDF**：[打开PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Conformal@K_ Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees.pdf>)
- **原始PDF链接**：[公开PDF](https://dl.acm.org/doi/pdf/10.1145/3828550)
- **实际阅读**：L2；正式版物理p1–32、35–42定向阅读；p12–13算法框已通过页面渲染核对，p33–34参考文献未逐条核，Fig1/2细节与Fig3格点未逐值核。不将定向阅读写成完整正文逐页精读，也不声称全部证明验证。

#### 方法、结果与适用条件

# LCK01 — Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees

<a id="lck01"></a>

## 结论与版本边界

它是B在“既有scorer后接独立query校准、有限样本风险约束、分组与多阶段端点”上的直接方法近邻；并未覆盖B的四统计、冻结ModernBERT→PCA16与20维RF，也没有来源/实体/条件命题检查或批量LLM核验。论文的零相关项miss、B的正常query最终误删、以及多跳所需全部证据保留是三个不同事件，不能互换。正式身份和可见表值已核，但部分证明/推论有可定位问题；不能把标题中的distribution-free、group或two-stage guarantees当作B最终决策的现成证明。

<a id="identity"></a>

## 正式身份、来源与本地文件

- 完整题名：Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees。
- 全作者：**Guangrui Fan；DanDan Liu；Lihu Pan**，顺序/大小写按首页ACM reference。第一/第三作者Taiyuan University of Science and Technology，第二作者Universiti Malaya；与官方Crossref缓存一致。
- **ACM Transactions on Information Systems，44(6)，Article 138，42 pages，2026**。期刊论文；regular/special issue细分未核。PDF印记August2026；物理p1即article138:p1，没有封面偏移。首页正式ACM reference、DOI、页脚及CC BY4.0支持排版VOR身份。
- DOI `10.1145/3828550`；[官方DOI页面](https://dl.acm.org/doi/10.1145/3828550)；[官方PDF](https://dl.acm.org/doi/pdf/10.1145/3828550)。
- CCF **A**：用户提供的CCF第七版目录中，数据库／数据挖掘／内容检索期刊A类列有TOIS。
- 本地PDF：[论文库正式版](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Conformal@K_ Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees.pdf>)；42物理页。
- p42日期：received2025-11-09、revised2026-03-08、accepted2026-06-21；PDF印记August2026。旧publisher-deposited Crossref缓存online2026-08-11、print/issued2026-07-31；分别保留，不静默统一。PDF创建时间不当出版日期。
- 当前原综述Conformal@K字面命中2152行，完整题名/DOI未命中。只说明当前已提及该名，不是历史首次发现或全文已覆盖；精确记录存`metadata/old_coverage_literal.json`。

## 实际阅读范围（L2，不是L3）

**38个不同物理页有定向阅读：pp1–3、6–32、35–42。** p32只读§9，p35从Appendices起；References不计。pp4–5未读，pp33–34为未读参考文献页。方法§3–5、实验§6、主结果§7、讨论/局限§8及相关附录A–C的文本已读；pp12–13 Algorithms1–5框内未读，Fig1/2图内细节及Fig3格点未逐值核验，因此不声称完整正文通读、全部算法/图/证明已验证。

原版页图另核p1、11、19、20、24、26、27、29、35、36、38、42。Fig4坐标数量级亦已视觉对照。逐页scope见`reading_scope.json`；12条reading evidence见`reading_evidence.jsonl`；全文提取见`text/conformalk.txt`、`text/conformalk.pages.json`。下载、渲染和全文提取不等同阅读。

<a id="risk-unit"></a>

## 随机单位、标签与分母

作者定义（pp6–9，§3）：随机单位是**query/user-session context X**，不是物品或独立文档块。R(X)为相关项集合；实际保证针对用于构造miss的观测标签Y，潜在真实相关r与Y不同。§6.7的PU敏感性分析不能直接把这个边界消除。

| 端点 | 作者定义/分母 | 对B的限定 |
|---|---|---|
| retrieve-miss | R(X)∩C1(X)为空的query概率，Eq3.3 | 候选池零命中，不是误删 |
| final/budgeted miss | R(X)∩C2(X)为空的query概率，Eq3.5 | 至少一个相关项即可成功，不保多跳全部support |
| fixed-K miss | reranked固定TopK零命中，Eq3.4 | 不能与校准可变长列表直接替换 |
| group risk | E[w_g(X)·miss]/E[w_g(X)]，Eq3.6 | 分母为query权重质量，group不是语义/来源关系 |
| B最终误删（审阅比较事件） | 正常query的TopK中，至少一个正常块被最终策略误删 | 打分、关系OR升级和LLM后的最终删除须按实际决策定义；块级FPR不能替代 |

作者§5.7/Theorem5.13（pp19、42）还声称可校准ℓ_U=1−Recall，分母为该query的相关集合大小；这是平均未召回比例，也不等于“任一必要support被删”的概率。当前读了该扩展声明和证明，没有独立核证全部拓展。

本文主要通过扩大列表降低“一个也没命中”的风险。B删疑似污染块并保正常证据，目标、标签、损失方向不同。剩余至少一个块、答案ACC或任意块级accuracy都不等于B最终query误删率。

<a id="single-stage"></a>

## 单阶段阈值与有限样本条件

作者方法（pp9–11、16–17）：固定已训练scorer/候选生成器和检索预算L1，对每个校准query定义相关项首次进入reranked前缀的critical K；在预设单调族上选满足 **(1+校准miss数)/(n_cal+1)≤α** 的最小K。n_cal是校准query数，不是query×chunk数。p35 LemmaA.2给分位位置ceil((1−α)(n_cal+1))。即便零miss，也要求α≥1/(n_cal+1)，不能略去有限样本粒度。

Theorem5.1要求单调族、校准与新query交换性、固定L1，且校准内有可行K≤Kmax。无可行K则回退Kmax，报告feasible/risk_at_cap/gap，**不宣称该界**。经验gap不等于精确人口gap，POI不可行不等于依然达到α。

期望以校准样本和新query的随机性计（p35附录开头），是边际层面。p35 LemmaA.1/p36 A.2使用给定校准集后的rank/概率说法，不能据此升级成任意已实现校准集的条件风险≤α或逐query保证。本审阅保留标准单调分位校准概念，但不把本文条件化证明视为已独立核证。

<a id="groups"></a>

## overlapping-group：条件与证明边界

作者条件（pp7–8、11–12、17–18、37–39）：w_g只依赖X，可重叠/分数权重，不必和为1；不得依赖Y、相关性、scorer或事后选择特征；权重有界且E[w_g]>0。degree/community/time/region cohorts不是来源真实性认证，也不是跨命题一致性。

记S_g=Σw_g·miss、T_g=Σw_g、上界W_g。Eq4.5/A.1统计为 **(η+S_g+(1−α)W_g)/(η/α+T_g+W_g)**；每组取最小可行K_g，query返回活跃组K_g的max。η也不是普通+1伪样本：在该统计≤α的选择不等式中，η在两侧代数抵消，不能仅因η>0就当新增有限样本保险。只有各组选择器先有效时，扩大列表的单调性才保各组；这不是误删分支OR的自动保证。ESS_g=(Σw_g)^2/Σw_g²不是独立样本数；默认ESS<50合并/池化，原始小群和合并群的风险目标须分开。

**算法框与正文公式不一致（正式版物理p11–13）**：p12 Algorithm 2 的组风险统计为 `(η+S)/(η/α+T)`，而p11式4.5另在分子加`(1−α)W`、分母加`W`，p12式4.6前文字又要求按式4.5选择。比如`α=0.05、η=W=1、S=T=0`时，算法框值为0.05并满足`≤α`，式4.5值为`1.95/21≈0.09286`而不满足。两者是显示规则的差异；原文另述低ESS组先合并，不能用此例断言作者实现或实验代码实际发生该情形。p13 Algorithm 3也未在框内展示下文Protocol A要求的两个互斥校准池。

**作者声称**Theorems5.4/5.7/A.4给有限样本组风险≤α；**审阅判断**该具体证明有缺口，不能直接当已证：

1. p36 A.4用不含W_g margin的另一统计，与Eq4.5不是同一选择器。
2. p38先得到≤α+αW_g/(η/α+T_g+W_g)，随后断言≤α，一般推不出。确切算术：α=1/20、η=1、T_g=38、S_g=1、W_g=1满足其A.4前提等号，但新点w=1,z=1时比值3/59>1/20。只审计论文代数，没有攻击/实证复现。
3. p35 LemmaA.3把总体加权均值与有限样本自归一化均值的期望等同，一般不成立：N=1、等概率类型(w,z)=(1,0)/(2,1)，两侧2/3与7/12。此恒等式被组和IW证明调用。
4. degree/community如何映射成仅X可测的query membership、合并后是否仍逐一保护原始小群，细节不足；不因此直接断言标签泄漏。

以上仅审计这篇具体证明，不否定所有group-conformal方法，也不扩展其他论文。

<a id="two-stage"></a>

## two-stage：条件化与survivor分母

作者ProtocolA（pp13–14、17–18，§4.4–4.5/5.3）：D_cal,1只选检索预算；独立D_cal,2中**只保留检索已命中**的survivors以校准重排K。第二阶段平滑分母为survivor数量m+1，不是全量n_cal+1或被检索块数。需固定scorer、相应交换性、两阶段可行；只拆开相关时间日志不自动提供独立性。

设A为检索漏，B为在检索未漏时的重排漏。作者以P(A)≤α1、P(B|A^c)≤α2得到最终漏 **α1+(1−α1)α2**。两者各.05对应.0975，不是.05；若总目标.05，对称预算约各.02532。Table12实测final=.049是实测值，不能倒推理论上界.05，也不把Final-miss列改称survivor条件风险。

两校准池大小/实际survivor m未随Table12公布；MSLR总cal2k不能自行分配成每池1k。Stage2不可行仍撤回界。cross-fitting取median不能仅凭单调性继承strict-split证明，其LTT升级还需有效p值与多重选择控制。

<a id="selection-confidence"></a>

## 2D选择、α与δ

§4.6/Theorem5.8声称在(L1,K) product-order网格找最小可行pair直接控最终miss，区别于阶段组合。普通重排扩大候选可改变固定TopK成员，两维嵌套是实质条件；偏序可有互不支配极小点，最小pair与一维rank证明如何适用仍缺条件。B的RF和关系两个分支不是此处的retrieval/rerank两阶段。

§4.8/5.8、附录C：α是风险，δ_HP是校准选择失败概率，不能混同。候选/组/折的多重选择须计入。§4.8谈独立校准点和Bonferroni；§5.8/附录C却把BH/FDR选项也归入1−δ高概率风险句子。FDR不自动给FWER或单个所选策略无效概率；本次不把该说法视为验证过的升级。附录A.8的Bonferroni全(组,aggregator)校正是另一声明，仍依赖p值有效性。

<a id="shift-dependence"></a>

## 漂移与依赖的附加条件

§4.7/5.4要求真实query密度比有支持overlap、正下界和有限上界；估计/裁剪有Δ_w项，裁剪比对应的目标与未裁剪test分布不能混同。本文IW证明还调用上面的LemmaA.3，不能由当前认定具体严格界成立。

§5.5依赖版要求严格平稳β-mixing，带Ξ_dep=(2ceil(W/b)−1)β(b)，不是任意漂移流量的精确保证；附录A.9还提block浓度项。实验2周窗口、每周更新、6小时block，但对应主表没有给出实际β(b)/slack。稳定曲线不等于这些未知项已验证为零。

<a id="settings-denominators"></a>

## 实验设置与实际分母

| 数据/设置 | 作者报告（pp20–23，Tables2–4） | 已知与未知 |
|---|---|---|
| MSLR-WEB10K | 10,000 query、约1.2M query-doc pairs、136特征；5折，每折train6k/cal2k/test2k；LambdaMART | 主表怎样池化折和5 seeds计算Clopper–Pearson CI不明确；不能自行乘成50k/10k独立query |
| Gowalla | 18,737 users、32,510 items、1,278,274 interactions；temporal70/10/20%；next-POI window10 | users不是test query数，interaction不是session；n_cal/n_test/组原始分子未知 |
| Foursquare | 24,941 users、28,593 items、1,196,248 interactions；同类temporal划分 | 同上，不按比例反推精确query数 |
| POI协议 | 全item all-ranking，Kmax50，无city限制/小负采样；LightGCN/SR-GNN/SASRec | 主要α目标不可行；POI未穷尽two-stage sweep |
| 分组/校准 | 独立train/cal/test；24 time bins、8 regions、degree deciles、20 communities；ESS阈值50 | stage2 survivors、各原始cohort分母、设计选择的实际校正族规模未给 |
| 不确定性 | 作者称5 seeds固定splits；miss用95% Clopper–Pearson，utility用1000 paired bootstraps | 无逐seed/fold原始miss counts，重复test不当新独立query |
| 漂移/流式 | hour×region weight clip[.5,2]；12周流；Table14展示六窗 | ESS3900是权重有效量而非test N；不推未展示周值或总体率 |

§6.7称PU重权使miss变化+0.3至+1.2个百分点，无逐数据集明细主表，不当潜在真实相关控制已证。实现用PyTorch/LightGBM/FAISS，24-core CPU+RTX4090；当前没有运行论文算法或复现实验。

<a id="main-results"></a>

## 主结果：逐表独立保留

以下均为**作者表值**，非复现或合并结果；结构化记录见`table_evidence.json`。

| 定位/条件 | 作者表值 | 可据此作出的有限判断 |
|---|---|---|
| Table5 p23，global α=.05 | MSLR .052 [.048,.056]，平均C2=19；Gowalla .662 [.650,.674]，C2=45；Foursquare .523 [.508,.538]，C2=42 | MSLR接近目标，两个POI在cap下不可行；有限test点估计略高于α不单独否定边际定理，也不等于严格经验≤α |
| Table6 p24，MSLR | FixedK20 miss=.083；CRC global=.054；Conformal global=.052/overlap=.051；后两者NDCG20=.458/.459 | 限同表比较；作者Meets-target Yes列原样保留，不推出逐群/每次校准都达标 |
| Table8 p24 | MSLR overlap worst=.056、p95=.053；Gowalla .710/.680，CRC-global .740/.710 | 群组风险改善，但MSLR点估计仍>.05且没有逐组CI/原始分母；不拼接Table9 |
| Table12 p26，MSLR (.05,.05) | joint ret=.048/final=.049，平均C1=200/C2=19，NDCG20=.458；naive ret=.049/final=.061 | 实测端点与.0975理论界分开，不是B误删或核验成功率 |
| Table13 p26，shifted Gowalla | unweighted .760；IW-CRC .720；IW-Conformal .710 [.697,.723]，ESS3900/clip12% | 风险下降但仍不可行；与无shift Table5不净收益相加 |
| Table14 p26，Foursquare六窗 | windowed [.521,.520,.512,.521,.522,.531]；无重校准[.580,.600,.620,.640,.660,.680] | 这些窗较稳定，不证明任意漂移≤.05，不以Fig4替换表值 |

对应关系缺口：Table8 Gowalla最坏群.710低于Table9所列deg-tail .800，未说明cohort集合如何对应；p27 Fig4轴约.05，Tables13/14同名任务约.71/.52，未见独立协议解释。POI文字说不可行回cap50，而Table5平均45/42也待解释。各项分别保留，不替作者修值，不把不同表/图拼成一个实验。

<a id="ablations"></a>

## 消融、成本与定义核对

Table15 p27的三个**独立比较块**，不累计收益：

- Mondrian→overlap：tail miss .820→.800，night .780→.760，列表46.0→46.2，latency15.0→15.1ms。
- λ0→.25：列表45→40，但tail miss .710→.730、HR20 .20→.19。
- refinement off→on：列表45→43.2，tail miss .710→.702。若只是§4.10严格递增逐query分数变换，则排序和critical K不变，不能单独解释这些变化；额外机制未知。

Table19 p29，MSLR由miss改τ=.1/.2，作者报列表19→16.2/14.1，binary miss .052→.067/.081。**审阅判断**：τ>0时{Recall=0}包含于{Recall<τ}，阈值损失≥binary miss，不是Remark5.14写的≤；字面τ=0时<0事件恒空，也不等于binary miss。不能把这张表当已核的“更弱Recall目标缩短列表”推导，表值只作作者报告。

Table17 p27同表成本：MSLR p50/p95/p99=9.8/12.4/14.1ms；Gowalla15.8/19.6/22.3ms，窗口更新均值1.2min/p95 1.5min。其推荐模型/硬件/列表成本不是B的RF+一次批量LLM端到端成本，不和Table18另一个均值口径拼接。

<a id="proof-audit"></a>

## 影响开题引用的数学问题

- **已视觉核对的固定K方向错误**：Prop5.12 p19/A.10 p42写TopK⊆C2、|C2|≥K，却推出fixed-K miss≤budgeted miss。较小集合更易零命中，应为fixed-K miss≥budgeted miss；相关项仅在长列表第K+1位即可区分。不能据此保证截断TopK或全部多跳support。
- **已视觉核对的Recall方向错误**：Remark5.14 pp19–20/Table19 p29，详见消融。不接受作者较大τ更宽松的推导。
- **已核期望/代数缺口**：p35 LemmaA.3两侧2/3≠7/12；pp36–38群组证明有3/59>1/20的已满足前提反例，详见group节。精确有理数核对存`metadata/reviewer_algebra_checks.json`，不是攻击/算法复现。
- **待补条件**：2D偏序最小性、cross-fit median继承、给定已实现校准集的条件rank、BH到高概率选择控制。严格split/固定单调族/边际分位校准的概念，不因这些具体写法被一概否定。
- **协议/机制对应未知**：cap回退与表内平均值、cohort集合、Fig4尺度、rank-preserving refinement额外作用。不是已确证的实现bug，也不据此推断研究不真实。

作者声明与审阅判断分开存`theory_audit.json`，不跨表合并任何风险率。

<a id="limitations"></a>

## 作者局限、审阅判断与未知

**作者承认**（pp11/17/22/30–31）：cap可不可行；小群保守/噪声大；无支持overlap区域不能由IW保护；裁剪偏差、依赖有slack；反馈循环改变行为/exposure；POI未穷尽two-stage。miss-risk和exposure公平不是同一目标。

**审阅判断**：可作风险校准近邻，不能作B整个RF+关系+LLM策略的有限样本证书。即使不考虑本文具体证明缺口，相关命中不认证来源真值，不保全部support，不控任意攻击分布安全性。

**未知**：各表/seed/fold原始query分母、survivor人数、未池化群体分母、候选校正族、实际Δ_w/β-mixing slack、实现/代码/样本重用、refinement与图表差异解释、预印本关系。均不猜；sample_overlap=unknown。正文pp4–5、算法框和部分图细节未读，固定L2。

## 对开题A/B的限定比较

| 维度 | 本文实际邻域 | B的不同与保证边界 |
|---|---|---|
| 表示/训练 | 已训练scorer后held-out校准，model-agnostic | B冻结ModernBERT不代表整体无训练，PCA/RF/校准角色应分开；本文不实例化PCA16+四统计→RF20维 |
| 统计量 | rank/critical K、binary miss | 不覆盖尾谱马氏、BM25/SVD残差、query正交平行比、首尾一致性四统计或语义融合 |
| 校准单位 | query/会话 | B独立clean query TopK max同属query级；同query块间相关无需假装独立；query校准本身不是宽首创 |
| 分组 | X可测有界fractional cohort，max扩列表 | 不是同/异源、实体、命题适用性；max扩列表不是删除分支OR |
| 多阶段 | retrieval miss+survivor条件rerank miss，独立池 | RF分支和关系OR升级不是这里的阶段定义；不能借其组合界 |
| 最终误删 | 本文未定义 | 若B最终误删事件严格包含于已校准max越阈事件，可依事件包含继承；若关系-only触发LLM能另行删块，该路径需覆盖。关系OR若只增加核验调用、不增加删除则另论，不笼统判其破坏保证 |
| 异源参照/LLM | 未实例化 | 至多一次批量LLM仅约束调用预算，不自动控误删；异源证据真假与适用性仍需定义 |
| 正常多跳/A | 至少一项相关命中 | 不保多个互补块共同检索、共同必要性、单源真实文档或未知分块稳健；全部/充分support保留不能由零命中miss推出 |

B应把新颖性收窄到具体统计表示、关系核验如何保正常证据、以及**最终query误删端点**的有效控制，不能以冻结模型/TopK/query校准/两阶段本身区别前作。本文的证明问题也不能反向证明B新颖或有效。

## 文件与完成边界

- `reading_evidence.jsonl`：12条独立reading evidence；`reading_scope.json`：38页逐页范围。
- `table_evidence.json`逐表；`theory_audit.json`区分作者/审阅；全文提取保留，不当全文已读。

## 独立理论复核后的引用限制

[独立局部审查](<../audit/local_conformalk_independent_review.md>)进一步检查显示式4.5/4.6：其选择条件等价于 `S <= alpha*T+(2*alpha-1)*W`，eta抵消。常数组权重1、8个校准query、alpha=1/5、Kmax=50、独立均匀critical rank下，该规则选择第7顺序统计量；新query零命中风险的精确边际值为 `82899363866669/390625000000000 = 0.21222237149867265 > 0.20`。原页公式及有理数算术相符；这针对显示规则的普遍组保证，不是论文代码复现或对所有共形方法的否定。ESS=53的变体也保留在审查中。

另须区分：普通split分位的无条件边际保证，与给定全部校准结果后的条件人口保证；样本可行与人口cap可行；至少一个相关项与全部多跳support保留。显示组式及条件rank证明不能直接作为B的风险证书。两阶段.05/.05的组合界仍为.0975；固定K截断与正Recall阈值损失的包含方向须按独立审查收窄。原表实测值保留，代码是否额外约束、原始分母及图表口径仍未知。

### conformal-at-k-acm-vor-3828550

此节仅记录出版社元数据和作者网页作为独立来源的L1阅读；当前论文阅读范围以本笔记前述正式版记录为准。

- **书目来源**：[原始页面](https://dl.acm.org/doi/10.1145/3828550)
- **DOI / arXiv**：10.1145/3828550 / 未核实 / 未提取
- **本地PDF**：该摘要报告未关联PDF；已读全文见本笔记其他报告。
- **原始PDF链接**：[公开PDF](https://dl.acm.org/doi/pdf/10.1145/3828550)
- **实际阅读**：L1；L1：publisher-deposited Crossref metadata及摘要；补看官方ACM检索索引片段，但未取得连续HTML或PDF，不能算方法/实验全文。物理页码：无（未读任何PDF页）；书目1–31/1–42不等于阅读范围。Conformal作者publication网页已完整读，只有accepted/forthcoming身份描述，无方法全文/PDF入口。

#### 方法、结果与适用条件

## IRP02 — Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees

### 身份、版本与旧覆盖

- `study_id`: **conformal-at-k**；`report_id`: **conformal-at-k-acm-vor-3828550**。
- 全作者（publisher-deposited Crossref）：**Guangrui Fan; DanDan Liu; Lihu Pan**。保留 `DanDan` 原字段大小写；PDF 未核，不自行改名。
- **ACM Transactions on Information Systems 44(6), 2026, 1–42；CCF-A**。文章号 `null`；会议 track 不适用，专刊身份未核。
- DOI：**10.1145/3828550**；正式入口：https://dl.acm.org/doi/10.1145/3828550 ；publisher-deposited 元数据：https://api.crossref.org/works/10.1145/3828550 。本地 `catalog_ir_priority_sources/conformal_crossref.json`。
- Crossref `published-print`/`issued` 为 **2026-07-31**，`published-online` 为 **2026-08-11**。保留先印后 online 的登记字段，不自行调换。还登记 VOR 的 CC-BY 4.0 许可；**403 不能据此解释为付费或未公开**。
- **状态差异明确保留：** 作者主页 https://gerryfan0706.github.io/publication/2026-tois-conformal-k （网站标最后更新 **2026-09-18**）仍写 accepted/forthcoming；ACM 登记到 Crossref 的记录已有上述卷期/出版日期。以“publisher-registered publication metadata；作者页仍 accepted/forthcoming；未直接取得最终 PDF”描述，不无解释地同时写已出版/未录用。
- 作者页只提供身份、短述和推荐引用，未观察到 PDF 超链接。已全文读的是这张**简短作者网页**，不是论文正文。
- arXiv：**未确认**；只登记一个正式报告元数据 report，不凭无关 conformal 检索结果造预印本关联。

### 阅读等级及 PDF 获取边界

**该报告为L1。** 已读 Crossref 元数据/摘要及完整短作者网页；**没有 PDF 或连续方法/定理/实验正文**，没有 PDF 物理页，`local_pdf=null`、`physical_pages_read=[]`。书目 1–42 不等于实际阅读范围。

### 作者披露的机制、设置和结论（仅摘要层）

摘要称其是与模型无关的校准层，在任意 retrieval/reranking scorer 上选取单调预算，控制返回 Top-K 中**没有相关项**的 miss-risk。作者还声称支持重叠群体、两阶段 retrieve-miss/final miss@K、importance-weighted/windowed 漂移扩展；参数不可行时报告 best-effort gap。**定理概率层级、alpha 与置信参数的关系、损失/单调性、交换性/漂移假设、群体估计条件和严格有限样本界均未核原文，不把 distribution-free 解读为无假设。**

摘要列 MSLR-WEB10K、Gowalla、Foursquare，并指出显示上限 Kmax=50 下的小 alpha 可能不可行。完整划分协议、群体样本量、基线、表中数值、方差及局限章节未读。这里只保存摘要层主张，不认证其保证、结果或可复现性。

> distribution-free, finite-sample control of

证据：https://api.crossref.org/works/10.1145/3828550 ，`message.abstract`。另作者网页身份短引（独立 source，2 词）：

> Accepted (forthcoming).

证据：https://gerryfan0706.github.io/publication/2026-tois-conformal-k ，推荐引用。**该短引是出版状态证据，不是方法证据。**

### 我们对 A/B 的比较与证据评价

**A：** 至少一个相关项进入 Top-K 与多个互补前提块共同进入、共同必要是不同事件。即便前者成立，也不能推出后者成立。当前没有未知分块、同源互补前提或组合投毒相关全文证据，不能将它列作 A 已有攻击方法。

**B 的几何维度：** 摘要披露的是任意评分器外的预算校准层。尚不能确认与尾谱马氏/SVD 残差/query 正交比/块内一致性在正文有无组件交集；不凭摘要作不存在断言。

**B 的校准维度（强邻域）：** Conformal@K 的风险标签是“没有相关项”，决策量涉及检索/显示预算；B 的干净 query 最大分位校准面向“正常查询下最大的疑似恶意风险/误报”。**校准单位、坏事件、分母和控制目标不同**；不能直接拿其 miss-risk 保证给 B 的恶意块误报控制背书。可作为目标区分、群体/双阶段可行性诊断的重要方法学近邻；是否已有 B 同型分位数校准，必须读公式再判断。

**B 的正常多跳/来源关系维度：** “至少一项相关”不能保证保留回答所需的**全部**互补证据，也不等于审计来源、实体或命题关系。群体可能重叠同样不自动等于证据块之间存在语义关系。对正常多跳链的联合遗漏事件、跨来源异质性和检测后证据保留，仍需另设匹配的评价事件。此为我们的目标比较，不是该文实验结论。

**综合判断：** 对 B 的风险校准叙事是强相关新候选；现阶段只能确定身份和摘要披露目标，不能认证定理假设、证明正确性或 B 的创新边界。

### 尚未解决

1. 合法本地 PDF、最终文章号/作者排版、真实物理页；方法/定理、设置、主要表、局限至少 L2。
2. 核区分边际/群体/同时两阶段保证、交换性/漂移条件、重叠群体分母及平滑、可行性边界；不可行时的 best-effort 不能冒充原目标保证。
3. 核 Crossref 出版登记与作者页 accepted/forthcoming 状态差异；不猜隐藏出版进度。
4. 预印本、代码、样本复用：均未由论文正文确认；`arxiv_id=null`、`code_url=null`、`sample_overlap="unknown"`。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md) · [全部逐篇笔记](../../../../docs/RAG安全证据地图_20261102.md#paper-notes)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [Conformal@K: Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Conformal@K_ Distribution-Free Top-K Miss-Risk Control for Recommendation with Overlapping-Group and Two-Stage Guarantees.pdf>)
<!-- PDF_LIBRARY_END -->
