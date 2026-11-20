---
study_id: acl:2024.acl-short.2
reading_level: L3
checked_date: 2026-11-16
---
# FanOutQA: A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models

本笔记为 2026-11-16 的独立全文审读记录。L3 在此仅表示下列 **ACL 正式版 PDF 的正文和附带附录均已逐页阅读**；不表示复现实验、审查完整数据集或逐条验证论文引用。

## 一、结论与去重

**FanOutQA 是正常多文档、多跳问答及检索评测的强近邻，并非本次读到的 A/B 直接撞车。** 它有明确的跨文章任务设计、人工问题分解和一定反捷径过滤，可供研究正常证据保留；但其设计要求和标注不能证明每个检索块都对回答必要，也不能代替对攻击载荷的逐块消融。论文未构造攻击者控制的同源长文与协同投毒，也未给出 B 的污染检测、异源安全复核或独立干净查询最终误删校准。本文中“必要证据”等名称指作者任务和标注意义，不是对每个块的因果必要性证明。见 PDF 物理页 2–5、11、17–20。

审读前对 `docs/`、`research_data/RAG安全文献调研/原始证据/` 和 `ref/` 的可检索文件，以完整题名、`FanOutQA`／`FanOut QA`、`2024.acl-short.2`、DOI `10.18653/v1/2024.acl-short.2`、arXiv `2402.14116` 检索；仅发现 [ACL 2024 Short 摘要筛查记录](<../audit/ACL2024_Short_1-11_13-21_逐篇官方摘要筛查_20261116.md>)和官方卷目录缓存，前者只登记摘要，后者是目录材料，均不是既有逐篇全文阅读。指定论文库检索只发现本任务取得的这份 PDF。该结论仅覆盖检索到的记录和别名，不能排除未登记的阅读。此处增加的是对同一篇论文的一次全文审读，不把原摘要记录另算为新论文。

## 二、出处、版本、许可与阅读范围

- **作者及正式出处**：Andrew Zhu、Alyssa Hwang、Liam Dugan、Chris Callison-Burch。*Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*，ACL 2024，Bangkok，印刷页 18–37；ACL Anthology ID `2024.acl-short.2`，DOI `10.18653/v1/2024.acl-short.2`。见[官方文章页](https://aclanthology.org/2024.acl-short.2/)及[官方 PDF](https://aclanthology.org/2024.acl-short.2.pdf)。
- **关联版本**：同题名、同作者的 [arXiv:2402.14116](https://arxiv.org/abs/2402.14116) 为预印本；其页面列 v1 为 2024-02-21、v2 为 2024-06-06。本次实际阅读、页码与哈希均指 ACL 正式版，而非预印本。
- **本地文件**：[按完整题名保存的 ACL PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf>)；Windows 文件名不能使用题名中的冒号，故替换为 `_`，其余题名保留。官方 PDF 在本任务中获取时返回 HTTP 200；本地文件 353,446 字节，20 个物理页；SHA-256 `2ecf7dc40f9694d555695577c5fc675c91436ab9de4ae5b55344a78ff8582c32`。PDF 物理页 N 对应印刷页 N+17。
- **实际阅读**：物理页 1–5 是主文、结论、伦理和局限；6–7 为参考文献；8–20 为附录 A–H。主文与所有附录逐页读取，参考文献页也逐页查看；对图 1、图 2、表 1–4 及第 10 页实例作了本地图像视觉核验。下表按每一物理页记录阅读结果。
- **许可**：ACL Anthology 文章页页脚称 2016 年及之后的 ACL 材料采用 CC BY 4.0，PDF 首页列 © 2024 ACL；本任务从 ACL 官方公开地址获取，供本地研究。论文物理页 5 单独声明**数据集 CC BY-SA 4.0、Python 包 MIT**；不得把数据的 ShareAlike 条款混同为代码许可。维基百科内容、代码及数据再利用应按相应许可归属与条件处理。
- **核验范围**：官方网页、PDF 和作者公开仓库均已查看；本次未安装代码、运行检索、下载整库维基百科或重跑基准。所引数字是论文报告，而非本次独立测得。

## 三、数据构建与“多文档共同支持”

论文让 379 名修读 AI/NLP 课程的学生写信息检索题，要求顶层题至少需要五篇英文维基百科文章，并将问题拆成由单篇文章回答的子问题。1,418 个初稿经筛选后保留 1,034 个顶层问题、7,305 个子问题、4,121 篇不同文章；作者报告平均每题约七篇证据文章、总计约 172k 证据 token。这里的证据长度是数据/文章规模，**不意味着所有这些内容都实际进入每次模型输入**。[PDF 物理页 2／印刷页 19](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=2>)。

论文声明数据写作截至 2023-11-20，并保存该日期的维基百科快照；开发集 310、测试集 724，约 30%／70%。开发集公开问题、人工分解和答案；测试集公开顶层问题及人工分解所用文章列表，答案用于隐藏评测。论文在这些页面没有说明按来源文章隔离划分，也没有给出跨划分文章不重叠的证明；不能把问题数量划分解读为来源不重叠。论文未声称另有训练集。见物理页 2；当前仓库的发布方式及后续数据更新另见第六节。

附录 A 展示先确定实体列表再查各实体属性的扇出型分解，也展示较长的链式例子；附录 G 的标注说明明确允许一题有多种可行策略。分解可提供有用的**文章级人工参考路径**，但不同文章可能包含相同事实，模型也可能利用参数知识或其他来源；同一文章切成的不同块还可能重复或互相替代。因此，文章标注、多篇共同输入、甚至答对，分别都不足以证明“给定竞争背景和替代来源时，移除任一指定片段都会使正确回答失败”。[PDF 物理页 8–10](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=8>)；[物理页 17／印刷页 34](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=17>)。

## 四、过滤、捷径与验证边界

附录 C 的流程先用启发式**标记**顶层答案不由子答案组成、多个子问题复用同篇文章等潜在问题，经过人工复核，并检查子答案是否出现在其标注文章。然后，以顶层问题和维基文章标题的 `text-embedding-3-small` 表示检索最相近 30 篇文章；若其中一篇含所有子问题答案，则删除整个样本。作者还用 GPT-4 辅助标出主观性、语法与单位问题并人工复查；相似问题以嵌入余弦相似度 0.9 为候选阈值，人工选择保留项。[PDF 物理页 11／印刷页 28，附录 C](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=11>)。

论文物理页 5 另称利用 Wikipedia backlinks API 查看与人工证据关联的文章。上述检查加强了任务设计，但“前 30 篇中没有某一单篇含全部子答案”不排除其他文章、多个替代文章或参数知识形成捷径；backlinks 的描述也没有给出逐片反事实实验。论文未对每个检索块实施逐一删除、等量回填及所有真子集的系统必要性检验。标注写作者的至少五篇要求，是任务意图，不是这些强结论的实验证明。

## 五、检索、问答指标及实验结果

| 条目 | 论文做法及限制 |
|---|---|
| 三种设置 | Closed Book 仅给顶层问题；Open Book 用 Wikipedia 检索工具多轮查找；Evidence Provided 给出人工分解所用文章，但具体实验仍按同一检索方案截取能放入上下文的块，不能当作“全部完整证据都被模型看见”。物理页 3–4。 |
| 检索流程 | Open Book 用 Kani 调用 Wikipedia 搜索：将每篇取回的文章切成约 **1,024 字符**的块，优先段落／句子边界，再以 **BM25+** 对块排序；每篇最多提供模型上下文长度一半的 token。这里是字符分块及每篇上限，不是固定 1,024 token，也不是全局固定 Top-k。物理页 3–4。 |
| 检索指标 | 论文主要报告顶层回答效果；在所读正文与附录中未见逐块 Recall@k、标注支持集完整召回率或恶意检索召回等安全指标。文章级证据名单不能自动当作块级金标。 |
| Loose / Strict | 将参考答案和生成文本词形归一、去停用词和标点后，Loose 是参考答案字符串出现在生成文本中的比例，再对题目求均值；Strict 是该题全部参考字符串均命中的指示量，再对题目求均值。它们更偏向回答字符串覆盖，不校验证据来源或安全。物理页 3，式 1–2。 |
| 其他评分 | 报告 ROUGE-1/2/L F1、BLEURT 和 GPT-4-0613 judge。附录 H 的评判模板把与参考答案一致的超集、相同内容或事实等价分别计 1，将子集、冲突与无效回答等计 0；模型裁判不是来源真实性验证。物理页 3、18–19。 |
| 代表性结果 | 论文表 2：闭卷 Mixtral-8x7B Loose **0.470**；开卷 GPT-4-turbo **0.470**、Claude 2.1 **0.471**；给定证据 Claude 2.1 的 Loose **0.653**、Strict **0.215**、GPT judge **0.470**。这些是正常问答得分，并非攻击成功率或防御安全率。物理页 12，表 2。 |
| 人类与模型比较 | 作者让 14 名志愿者各回答 10 题，给 Wikipedia 检索权限；报告人类 Loose 0.685、模型裁判 0.452，人工复核为 0.847。论文称后者估计人类表现上限；这不是所有人类或所有设置的数学上界。物理页 4、17–18。 |
| 上下文实验 | 作者报告不同模型的上下文长度与开卷、给证据条件下得分分别存在相关性（r²=0.558／0.782），不同模型本身等因素仍可能混杂，不能仅凭相关性认定上下文长度的因果效应。附录 F 将模型上下文统一为 4,096 token，并测试每轮重复原题：GPT-4 在后者有 33.1% 题目超时，另两模型未见显著提升（p>0.2）。这些实验涉及信息保留和检索成本，不是污染防御。物理页 4、13。 |

表中出处：[PDF 物理页 3／印刷页 20](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=3>)；[物理页 4／印刷页 21](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=4>)；[物理页 12–13／印刷页 29–30](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=12>)；[物理页 19／印刷页 36](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=19>)。

## 六、数据、代码与版本差异

截至 2026-11-16，论文指向的[作者仓库](https://github.com/zhudotexe/fanoutqa)可浏览；仓库首页称包含数据加载、Wikipedia 检索和论文指标实现。[数据目录](https://github.com/zhudotexe/fanoutqa/tree/main/fanoutqa/data)列出 `fanout-final-dev.json`、`fanout-final-test.json` 和对应的 `-nov23.json` 文件及数据许可；`fanout-final-dev-nov23.json` 的网页内容实际可读。README 说明开发集可用于本地评价，测试集不公开答案；作者提供提交隐藏测试结果的流程。未尝试下载完整快照或验证测试集评分服务当前能否运行。

当前仓库的 [pyproject.toml](https://github.com/zhudotexe/fanoutqa/blob/main/pyproject.toml) 标版本 `1.3.0`；[utils.py](https://github.com/zhudotexe/fanoutqa/blob/main/fanoutqa/utils.py) 的 `load_dev()`／`load_test()` 默认读取**不带 `-nov23` 后缀**的两个文件，允许通过参数指定文件。README 及 [2026 年数据更新提交](https://github.com/zhudotexe/fanoutqa/commit/1d59846d8cf4c29e6c91e9febce2278dcda86cdd)称 2026 年 7 月更新了 dev／test 的部分答案以适配本地 2023 年 9 月 Wikipedia ZIM，建议使用 `fanoutqa>=1.3.0`。这与论文所述 2023-11-20 快照不能直接视为同一知识环境；仓库同时描述另一份 2023-11-20 快照，但本次未下载验证该大文件。复现时应固定具体数据文件、代码提交、语料及其摘要，不应仅写 `FanOutQA` 或 `latest`。

**可复核的具体不一致**：论文附录 A 的 Ann Arbor 面积示例在[物理页 10／印刷页 27](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=10>)写 **73.35 平方公里**；仓库当前 [dev-nov23 数据](https://github.com/zhudotexe/fanoutqa/blob/main/fanoutqa/data/fanout-final-dev-nov23.json)中同一问题、ID `498337828f5896d3` 的答案为 **75.35 平方公里**。2026 年 7 月更新之前的[父提交开发数据](https://github.com/zhudotexe/fanoutqa/blob/4e254877c0d28378e800171ab92781dbba893718/fanoutqa/data/fanout-final-dev.json)里同一 ID 也写 75.35。因此，这一差异不能归因于 2026 年更新；其成因和哪一个面积在对应证据口径下正确，本次未确认。`-nov23` 后缀也不能单凭名称证明该文件与论文实验所用文件逐字节一致。

## 七、与开题 A/B 的比较和可用方式

依据本项目 [研究点正文](<../../../../partitions/section3_content.tex>)，A 为单一源文档改写、受害者侧切块及同源角色块协同投毒；B 为统计与语义筛选、跨块关系检查及结合异源参照的有限 LLM 复核。本文比较以所读论文和上述当前开题内容为限。

- **A：环境近邻，非攻击机制重合。** FanOutQA 的正常任务体现“一个问题需要整合多个文章中实体／属性”的复杂性；但多个 Wikipedia 来源并不等于攻击者控制的同一长源，不存在本文展示的双角色恶意载荷、未知切块迁移、自然 Top-k 共同召回或固定背景的双块／单块／空块对照。若用于 A 的干净背景，仍需另行构造和验证威胁模型、配对移除／回填及攻击块共同必要性。
- **B：正常多证据保留和效用近邻，非安全防御。** 人工文章路径和开卷／给定证据设置可作为正常任务压力测试，观察过滤前后检索及问答变化。使用前需将文章级标注映射到实际片段，检查替代证据、时点与答案正确性；宜分别测量支持覆盖、最终回答、正常查询的误删和调用成本。本文没有给出 B 的污染识别或独立干净查询上的最终 OR 误删率，也未证明统计告警阈值自然控制最终 LLM 误删。
- **不能直接外推**：该数据只覆盖英语 Wikipedia 的事实信息收集；题目来源、标注、快照与 2026 更新会影响复现。作者没有评价模型分解与人工分解是否一致（物理页 5），故成功回答本身不表明模型实际使用了全部人工路径。

## 八、逐页阅读索引

下列“P”均为本地 PDF **物理页**；印刷页 = P+17。每行的链接直达该页。

| 页码 | 本页阅读内容 |
|---|---|
| [P1／18](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=1>) | 摘要、引言、图 1：扇出式问题分解及三种设置示意。 |
| [P2／19](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=2>) | 相关工作；任务、人工构造、样本量、2023-11-20 快照与 dev/test 划分。 |
| [P3／20](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=3>) | 三种评测设置、模型、Loose／Strict 和其他指标；开卷分块、BM25+ 及每篇上下文上限。 |
| [P4／21](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=4>) | 图 2，开卷与给证据结果、模型上下文相关性、人类实验和结论。 |
| [P5／22](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=5>) | 未按人工路径评估模型分解；伦理、数据与代码许可、指标和英文维基百科局限；backlinks 的描述。 |
| [P6／23](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=6>) | 参考文献起始，逐页查看。 |
| [P7／24](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=7>) | 参考文献续页，逐页查看。 |
| [P8／25](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=8>) | 附录 A：歌曲榜单与人物年龄例子；快照日期说明。 |
| [P9／26](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=9>) | 附录 A：漫画主角、学校基金和长链问题的分解。 |
| [P10／27](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=10>) | 附录 A：Ann Arbor 面积及葡萄品种；附录 B 的主题标注方法。 |
| [P11／28](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=11>) | 表 1 主题分布；附录 C 过滤、30 篇候选及人工复核；附录 D 模型信息开始。 |
| [P12／29](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=12>) | 附录 D 模型及贪心解码；附录 E 表 2 完整结果；附录 F 附加实验开始。 |
| [P13／30](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=13>) | 附录 F 统一 4,096 token 的表 3 与重复问题的表 4；附录 G 开始。 |
| [P14／31](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=14>) | 附录 G：题目编写说明及独立子问题的示例。 |
| [P15／32](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=15>) | 附录 G：先找列表再依赖列表分解，以及更复杂示例的开头。 |
| [P16／33](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=16>) | 附录 G：多层递归策略、证据页与答案的样例续篇。 |
| [P17／34](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=17>) | 附录 G：至少五文章、多个可能策略的写题要求；人类问答说明。 |
| [P18／35](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=18>) | 人类实验说明续；附录 H 的主观性与语法／单位提示词。 |
| [P19／36](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=19>) | GPT 评判 A–F 类及计分规则；闭卷、开卷与给证据提示词。 |
| [P20／37](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/FanOutQA_ A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models.pdf#page=20>) | 给证据提示词末尾，确认附录与论文结束。 |
