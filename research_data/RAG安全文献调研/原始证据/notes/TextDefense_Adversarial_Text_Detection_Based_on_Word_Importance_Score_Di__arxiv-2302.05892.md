---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2302.05892
reading_level: L3
reading_scope: "2025 IEEE journal main text and 2023 arXiv v1 main text; appendices scoped below"
checked_date: 2026-11-16
---
# TextDefense: Adversarial Text Detection Based on Word Importance Score Dispersion

## 研究结论与阅读范围

**结论先行。** TextDefense 是分类器输入的词重要性分布检测，与 B 的单块统计筛查在方法动机上是近邻；它没有在 RAG 检索块、同源跨块组合投毒或多跳问答证据保留上给出实验。其数值不能直接用于主张 B 的检出率、跨块关系有效性或正常问答误删率。以下期刊版页码均为印刷页码，并附 PDF 页码；作者版的页码另标明。

- **先前已读：L2，2026-11-02。** 旧记录实际读过 arXiv v1 的 PDF p1、p4–6、p7 局部、p11 局部、p12 局部和 p13 局部；正式版当时未取得。旧记录正文保留于文末历史折叠区，原顶部元数据已按本次阅读范围更新。这是同一研究的既有阅读，不新增一篇、不重复计入旧页的阅读工作。
- **本次新增：2025 正式版正文 L3。** 逐页读 IEEE PDF p1–13，即印刷 pp.4671–4683 的摘要、§I–VIII 正文及结论；逐图核读 Table I–X；PDF p14 / p4684 为参考文献尾部及作者简介，已检查。该 PDF 不含其正文所称的在线补充材料；没有把该材料冒充已读。
- **本次新增：2023 作者版正文补齐至 L3。** 结合旧记录，现已逐页阅读 arXiv v1 PDF p1–13 的正文。附录按主题查读 PDF p16–21，涉及 A–I 的文字和相关表格；Fig. 7 的 ROC 曲线未逐点数字化。p14–16 的参考文献只做定位。作者版附录不能自动视作 2025 年在线补充材料的完全同版。
- **来源关系已加强，但不合并版本。** 浙江大学 NESA 作者团队的[正式论文列表](https://nesa.zju.edu.cn/webpage/pubyear.html)在 2025 正式题名下直接链接 arXiv 2302.05892；已直接比对两版的威胁模型、公式和主要实验。2023 稿 7 名作者，2025 稿 8 名作者、成员与顺序有变化；期刊论文新增了 WISD 命名、更加明确的自适应约束和对正常文本误报的讨论。不得据此断言所有实验、样本和在线附录逐项完全相同，也不得作为独立研究重复计权。

## 一手来源、版本与本地文件

1. **正式版：** Lujia Shen, Yuwen Pu, Xuhong Zhang, Chunpeng Ge, Xing Yang, Hao Peng, Wei Wang, Shouling Ji, *TextDefense: Adversarial Text Detection Based on Word Importance Score Dispersion*, IEEE TDSC 22(5), 4671–4684, 2025, DOI `10.1109/TDSC.2025.3551162`。以[IEEE 论文页面](https://ieeexplore.ieee.org/document/10924677/)和[出版方经 Crossref 注册的书目](https://api.crossref.org/works/10.1109/TDSC.2025.3551162)核对身份；[IEEE PDF 接口](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10924677)于本机返回真实 PDF。首页明确 DOI，文件共 14 页，PDF 页码 + 4670 = 期刊印刷页码。本次按实际正式题名归档：[本地正式 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/TextDefense_ Adversarial Text Detection Based on Word Importance Score Dispersion.pdf>)；2,132,735 字节；SHA-256 `07247F5E584E848685EA3D9074083CB82DFCE98826221874A22064E63173406F`。文件载有东南大学机构许可水印，属于本机机构许可访问，**不是可自由再分发的开放获取版本**。
2. **公开作者版：** [arXiv 页面](https://arxiv.org/abs/2302.05892)，[2023-02-12 v1 PDF](https://arxiv.org/pdf/2302.05892v1)，题名为 *TextDefense: Adversarial Text Detection based on Word Importance Entropy*。复用已存在的[本地作者版 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/TextDefense_ Adversarial Text Detection based on Word Importance Entropy.pdf>)；21 页、748,865 字节，SHA-256 `CB2024AED8A531904388E5676B8673C8CA2E6CB9A8DCAEC4576110348AA26717`。本次从 arXiv 获取的字节哈希与现存文件一致，没有重复下载入库。

## 威胁模型与检测机制

**攻击对象与能力。** 正式版 §III-A，p4673 / PDF p3，攻击者操纵单条输入文本，使原本真实类别为 `y` 的文本被目标分类器分到其他类；可以是黑盒或白盒访问。§IV-D，p4676 / PDF p6 的主要攻击为 TextBugger、TextFooler、PWWS，分别涉及字符及词语扰动、同义词替换等，目标是小扰动的非定向误分类。这里的“黑盒”仍要求防御端能够查询目标分类器并取得类别置信分数，而非只有最终文本答案或标签；§V-F 排除了对 logits 做后处理的 API（p4681 / PDF p11）。论文本身不是针对第三方知识库插入、检索操纵、提示注入或多块组合载荷的实验。

**词级删除与 WISD。** 正式版 §III-C，p4674–4675 / PDF p4–5，定义固定参考类别 `y` 的单词重要性：

\[
s_i=F_y(x)-F_y(x\setminus w_i),\qquad
\mathrm{WISD}(x)=-\sum_{i=1}^{n}|s_i|\log |s_i|.
\]

其中 `F_y` 为分类器对类别 `y` 的置信分数，`x \setminus w_i` 是删除第 `i` 个单词后的输入。对数的零值按极限处理。其绝对重要性分数未被归一化为概率，故 WISD 是借鉴熵形式的统计量，不是该词重要性概率分布的标准 Shannon 熵；它受文本长度、采样数、分类模型和具体对数/实现约定影响。原文对真实标签、目标标签和预测标签的称呼并不完全一致，未找到足以确定无标签线上部署时 `y` 究竟如何选取的实现说明，复现时必须明确并核验。

较高 WISD 判为对抗文本。作者认为它反映了模型对不相关词的敏感性与文本不连贯；这是一种基于观察的解释，而不是“语义事实冲突”或恶意意图的证明。`-|s|log|s|` 对单个 `|s|` 在整个 `[0,1]` 上也不是单调递增：它在 0 和 1 处均为 0。因此既不能把任意高重要性都等同于高 WISD，也不能把高 WISD 必然解释为异常。

**阈值与查询开销。** 正式版 p4675、p4677 / PDF p5、p7：使用少量本地干净文本及由攻击算法生成的对应对抗样本，选择 F1 最高的阈值；§V-A 描述 100 条对抗样本及其干净文本。论文没有在这些段落中充分交代该本地阈值集与 500 条测试集之间的全部去重细节，不能自行假定其划分已经闭合。WISD 对每词删除需再次执行模型，若采样 `m` 个词且不复用结果，单文本约需 `1+m` 次模型前向；批处理会改变请求次数但不消除相应计算。作者版 p13 指出采样 2 词仍需 3 次查询；其附录 F、PDF p18 的 Amazon 实验报告采样 2/10 词约 7.4/27.2 ms、全词 222.7 ms，仅为该作者版及其实验环境的数据，不是 RAG 延迟保证。

## 实验与结果：明确条件、误报和矛盾

- **模型与数据。** 正式版 §IV-A/B，p4675–4676 / PDF p5–6：BERT、LSTM 文本分类，二分类为 Amazon、Yelp、IMDb、Twitter、Jigsaw，多分类为 Emotion、AG News；训练集按类平衡抽取 50,000 条，每个数据集随机抽取 500 条不在训练集中的测试文本，再生成对抗文本。§IV-C 的指标为 ASR、AUC、TPR/FPR、词扰动比例 PW、句向量余弦 SIM 和 CoLA 模型的语言可接受率 LA。SIM/LA 都是代理指标，不足以单独证实语义和真实标签未变。
- **常规检测与误报。** 正式版 Table I，p4677 / PDF p7：BERT + Amazon + TextBugger，阈值 0.06 时 AUC 0.9750、TPR 0.96、FPR 0.12；该 FPR 是所测正常分类文本的误告警率，不是 RAG 问答证据的误删率。正文宣称平均 AUC 0.9698，而表 I 的 Amazon/BERT 三种攻击 AUC 为 0.9750、0.9839、0.9764，简单均值约 0.9784；正文的 TextBugger ASR 写 85.65%，表 I 对应行写 83.90%。论文未在该处说明这些数值为何不同，不能悄然互换。
- **阈值方向的正文错误。** 正式版 p4677 正文写阈值提高会使 TPR 和 FPR 提高，但 §III-C 规定分数**高于**阈值才告警，Table VIII 的 FPR 也随阈值从 0.04 到 0.07 由 0.17 降至 0.09。按定义和表格方向分析，不能照搬 p4677 该句。
- **对照并非逐项都胜出。** 正式版 Table III，p4678 / PDF p8：Amazon + TextBugger 的 TextShield AUC 0.9846、F1 0.9680，TextDefense 分别为 0.9681、0.9249；Yelp + TextBugger 的 TextShield AUC 0.9761 也高于 TextDefense 0.9555。因此作者概括性的“优于其他方法”不能理解为每个数据集、攻击和指标均最优。TextShield 是该文用 10k TextBugger/TextFooler 样本微调 T5 的重实现，并非所有基线原始实现的直接对照。
- **在线 API 的选择条件。** 正式版 Table VII、§V-F，p4681 / PDF p11：三种分类 API 在给定转移攻击下 AUC 为 0.8244–0.9471，但只选择攻击成功的样本及其对应原始文本做检测评价，且排除了有 logits 后处理的 API；这不是全部请求上无条件的安全率，更非生成式 LLM 接口可直接部署的证据。
- **自适应攻击是有条件经验结果。** 正式版 §VI-A 与 Table VIII，p4681–4682 / PDF p11–12：攻击者知道检测器和阈值，维持原攻击的搜索/变换方式，同时约束误分类、扰动不超过 20% 和 `WISD(x')<阈值`；作者测试九种攻击。阈值 0.04 时，本地 FPR 0.17，TextBugger ASR 7.50%，九攻击经验鲁棒率 75%；阈值 0.07 时 FPR 0.09、TextBugger ASR 34.17%、经验鲁棒率 45%。鲁棒率只表示九种受限搜索均未成功的测试样本比例，不是对所有攻击的认证保证。正式版 Table VIII 没有显示 TPR/F1 列，不能把作者版同号阈值的 TPR/F1 自动记为期刊表的结果。
- **正式版两张表的 ASR 对不上。** p4681–4682 的正文说对抗训练比较采用阈值 0.06 的自适应攻击，但 Table VIII 中 TextBugger/TextFooler/PWWS 为 26.25%/30.83%/23.33%，而 Table IX 的 TextDefense 行为 54.24%/59.53%/45.76%。目前未在正文定位足以统一两表分母或实验条件的说明，应按各表单独报告并保留疑点。
- **高置信绕过与样本有效性。** 正式版 §VI-C、Table X，p4682–4683 / PDF p12–13：将真实类别目标分数压至 0.02 时，三种攻击的 AUC 分别为 0.6013、0.6624、0.6710，均值 0.6449；相应攻击成功率、PW 和 LA 亦应一同看，不能只报 AUC。作者指出部分替换改变真实语义/标签；正式版 §VII-B 还指出部分干净文本因低分类置信度而被误报。作者版附录 G/I 的具体例子位于 PDF p19–21；仅凭作者列出的例子，不能断言所有漏检均由标签改变造成。

## 对 B 的逐项相关性与边界

**单块检测：方法近邻，但输入和观测量不同。** 两者都以单文本内部的低维统计信号筛查异常，TextDefense 先于本方案讨论词删除导致的分类分数分布与所谓连贯性，不能将“使用统计异常识别或块内一致性本身”作为 B 的首创性。B 在当前 `partitions/section3_content.tex` 的 §3.2 中拟结合尾谱马氏距离、BM25 主子空间残差、查询条件的相对几何、首尾子窗表示差异和冻结 ModernBERT 查询—块联合表示，并以随机森林拟合干净/投毒样本；TextDefense 则依赖分类器对逐词删除的类别置信变化，不等于这些统计特征。B 的拟合集含干净和投毒样本、独立校准集是干净查询；不要把它误写成完全无攻击样本的方法。

**跨块关系：没有直接覆盖。** TextDefense 的一个分数对应一段分类输入，并未构建来源、跨块实体—命题、时间条件或互补载荷关系图，也没有测同源远距块对协同攻击。B 拟对候选块进行实体/命题关系与来源检查，再将可疑块对送审；两者对象不同。但“TextDefense 未研究”只针对本篇两版的已读内容，不等于全领域没有跨块防御。

**正常问答与误删：证据缺口。** TextDefense 的 FPR 说明正常分类文本会被错误告警，特别提醒不能把单块统计异常直接等同恶意；该论文未测正常问答答案准确率、关键证据保留、正常多跳桥接块被删除的比例，也没有 B 的 LLM 复核链路。B 以干净查询 Top-K 最大风险校准统计分支阈值；即使交换性等条件满足，其查询级统计告警控制也不自动控制跨块关系分支、LLM 最终删块或正常答案准确率。正常长文档中的同源远距和低频桥接实体可能合理，关系告警不能直接等于删除。

**可操作的比较建议，不代表已完成实验。** 若把 TextDefense 作为 B 的探索性基线，必须先明确针对 `(q,c)` 或 `c` 的受保护分类器、可用的逐类置信分数、线上参考标签、删除采样和长度截断；将重排序分数或生成概率代入属于新的适配版本，不是原论文开箱即用实现。在相同 Top-K、计算预算与独立的查询/源文档划分下，分别报告：块级 AUROC/AUPRC 与固定低 FPR 的 TPR；干净查询级任一块告警率和跨块分支告警率；必要证据完整保留率/误删率、正常多跳 QA 的 EM/F1 或任务相符指标；攻击成功率、跨块配对覆盖以及实际模型前向次数和端到端延迟。再按攻击方法、块长、来源、正常桥接类型与单块/组合载荷分层；只有该等实验可回答迁移是否成立。

## 代码来源与复现状态

- 检查了两版 PDF 的全文 URL、正式 PDF 可点击链接、作者团队论文列表及 GitHub 仓库名/描述搜索；未找到可证实由本论文作者发布的 TextDefense 实现或其固定版本。GitHub 同名 `FYNIXnlpGroupIIE/Textdefense` 页面显示仓库创建于 2021 年且没有任何文件，与 2023/2025 本论文无可核的实现关联，不能作为其代码。仓库搜索无法穷尽所有代码；**当前结论是作者实现未验证，不是证明代码不存在**。
- 没有运行论文代码、复现数值或核验训练/测试样本、线上参考标签选择、采样随机种子及自适应攻击的实现细节。正式版在线附录、实验数据与具体代码来源仍待作者或正式补充材料确认。
<details>
<summary>2026-11-02 原始 L2 记录（历史留存；与本次直接核验有差异时以上文为准）</summary>
# TextDefense: Adversarial Text Detection Based on Word Importance Score Dispersion

**阅读状态：L2。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：["Lujia Shen", "Yuwen Pu", "Xuhong Zhang", "Chunpeng Ge", "Xing Yang", "Hao Peng", "Wei Wang", "Shouling Ji"]
- **机构**：未核实 / 未提取
- **年份 / 会议 / track**：2025 / IEEE Transactions on Dependable and Secure Computing / Journal, volume22 issue5, pp.4671–4684
- **发表状态**：2025 journal identity confirmed by IEEE-deposited Crossref and DBLP; methods read in 2023 author precursor only
- **CCF**：正式身份已核等级 未核实 / 未提取；作者声称或关联venue等级 ["A"]。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](<../../../../docs/RAG安全文献补查元数据_20261102.md>)。
- **代码**：未核实 / 未提取
- **关联标题**：["TextDefense: Adversarial Text Detection Based on Word Importance Score Dispersion"]

## 一句话总结与核心贡献

作者版以目标分类模型删除单词前后的类别置信变化表征词重要性，再将其分布聚合为绝对分数的entropy式离散度；用少量正常/对抗样本选择F1最大阈值，无额外检测网络。实测BERT/LSTM、评论情感/毒性、Emotion和AGNews；每数据集500原样本及对应对抗样本。支持仅输出置信度的黑盒分类API，依赖目标模型泛化能力。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 未研究RAG来源、未知分块、互补块或双块联合检索，不直接撞A。

**B：** 高方法邻域：使用文本内部低维统计区分异常，并且明确与文本连贯性/无关词依赖关联，B不能把统计异常识别或块内一致性本身宣称首创。对象是目标分类器对删除词的输出反应，B对象为检索几何/词项残差及独立冻结语义编码；作者版阈值用含对抗样本的F1最大化，非干净query最大块分数分位校准。没有跨源实体命题关系或正常多跳证据保持评价。

## 局限、可比性与不确定性

2023作者版题名Word Importance Entropy、7作者；2025正式题名Word Importance Score Dispersion、8作者，且作者成员/顺序不同，不能据旧版断言最终方法完全一致。arXiv abs未见明确DOI/journal-ref对齐字段，当前按同名TextDefense及共同首作者记录潜在前身关系，report_relation为provisional，不将样本视为已证实相同。作者版§6.2高置信错误情境AUC均值降至0.6449；API AUC范围0.8244–0.9471。Table6低阈值FPR可达0.17，不是低FPR部署保证；每文本多次模型查询。部分样本语义标签已经变化，作者承认会混淆所谓假阴性。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### arxiv:2302.05892v1+TDSC.2025.3551162

- **书目来源**：[原始页面1](https://ieeexplore.ieee.org/document/10924677/) / [原始页面2](https://api.crossref.org/works/10.1109/TDSC.2025.3551162) / [原始页面3](https://arxiv.org/abs/2302.05892) / [原始页面4](https://www.computer.org/csdl/api/v1/graphql)
- **DOI / arXiv**：10.1109/TDSC.2025.3551162 / 2302.05892
- **本地PDF**：[打开作者版 PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/TextDefense_ Adversarial Text Detection based on Word Importance Entropy.pdf>)
- **原始PDF链接**：[公开PDF](https://arxiv.org/pdf/2302.05892v1)
- **实际阅读**：L2；2023-02-12 arXiv v1，共21页：实读PDF p1身份/摘要，p4–5 §3方法，p5–6数据/指标，p7 §5.1局部，p11 §5.5/5.6与§6.1局部，p12 §6.2与p13 §7.2/7.3局限。未通读正文和附录；2025正式期刊PDF获取418，不能将作者版阅读范围写成期刊页码。

#### 方法、结果与适用条件

### C07 TextDefense: Adversarial Text Detection Based on Word Importance Score Dispersion

- study_id：doi:10.1109/tdsc.2025.3551162。
- report_id：arxiv:2302.05892v1+TDSC.2025.3551162。
- 全部作者：["Lujia Shen", "Yuwen Pu", "Xuhong Zhang", "Chunpeng Ge", "Xing Yang", "Hao Peng", "Wei Wang", "Shouling Ji"]。
- 年份：2025。
- 正式venue：IEEE Transactions on Dependable and Secure Computing。
- track/卷期页：Journal, volume22 issue5, pp.4671–4684。
- 出版状态：2025 journal identity confirmed by IEEE-deposited Crossref and DBLP; methods read in 2023 author precursor only。
- CCF：A（用户第七版）。
- DOI：10.1109/TDSC.2025.3551162。
- arXiv/版本：2302.05892v1。
- 官方及作者主源：["https://ieeexplore.ieee.org/document/10924677/", "https://api.crossref.org/works/10.1109/TDSC.2025.3551162", "https://arxiv.org/abs/2302.05892"]。
- PDF源：https://arxiv.org/pdf/2302.05892v1。
- 本地PDF：D:/学在东南/毕业论文/开题/硕论开题报告/tmp/rag_gap_20261102/catalog_security_journals_sources/textdefense_pdf.pdf。
- 本地文本：D:/学在东南/毕业论文/开题/硕论开题报告/tmp/rag_gap_20261102/catalog_security_journals_sources/textdefense_pdf.txt。
- 阅读等级：L2。
- 实际阅读页码/章节：2023-02-12 arXiv v1，共21页：实读PDF p1身份/摘要，p4–5 §3方法，p5–6数据/指标，p7 §5.1局部，p11 §5.5/5.6与§6.1局部，p12 §6.2与p13 §7.2/7.3局限。未通读正文和附录；2025正式期刊PDF获取418，不能将作者版阅读范围写成期刊页码。
- 作者方法/实验陈述：作者版以目标分类模型删除单词前后的类别置信变化表征词重要性，再将其分布聚合为绝对分数的entropy式离散度；用少量正常/对抗样本选择F1最大阈值，无额外检测网络。实测BERT/LSTM、评论情感/毒性、Emotion和AGNews；每数据集500原样本及对应对抗样本。支持仅输出置信度的黑盒分类API，依赖目标模型泛化能力。
- 我们综合判断A：未研究RAG来源、未知分块、互补块或双块联合检索，不直接撞A。
- 我们综合判断B：高方法邻域：使用文本内部低维统计区分异常，并且明确与文本连贯性/无关词依赖关联，B不能把统计异常识别或块内一致性本身宣称首创。对象是目标分类器对删除词的输出反应，B对象为检索几何/词项残差及独立冻结语义编码；作者版阈值用含对抗样本的F1最大化，非干净query最大块分数分位校准。没有跨源实体命题关系或正常多跳证据保持评价。
- 局限：2023作者版题名Word Importance Entropy、7作者；2025正式题名Word Importance Score Dispersion、8作者，且作者成员/顺序不同，不能据旧版断言最终方法完全一致。arXiv abs未见明确DOI/journal-ref对齐字段，当前按同名TextDefense及共同首作者记录潜在前身关系，report_relation为provisional，不将样本视为已证实相同。作者版§6.2高置信错误情境AUC均值降至0.6449；API AUC范围0.8244–0.9471。Table6低阈值FPR可达0.17，不是低FPR部署保证；每文本多次模型查询。部分样本语义标签已经变化，作者承认会混淆所谓假阴性。
- 原文摘录<=25词/源：“TextDefense has to query the model multiple times.” (arXiv PDF p13, <=25 English words)。
- 原文确认代码：null（未核）。
- 样本复用：unknown；不跨study汇总ASR。

- CSDL补核说明：正式卷期目录的完整摘要、正式作者顺序已实读确认；官方接口及本地record见同ID metadata的official_abstract_confirmation。仅补身份与摘要，不消除作者前身与期刊最终PDF的版本差异。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md>) · [全部逐篇笔记](<../../../../docs/RAG安全证据地图_20261102.md#paper-notes>)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [TextDefense: Adversarial Text Detection based on Word Importance Entropy](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/TextDefense_ Adversarial Text Detection based on Word Importance Entropy.pdf>)
<!-- PDF_LIBRARY_END -->

</details>
