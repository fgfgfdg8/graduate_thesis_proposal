# PaperNotes 与 AI Safety Daily 补查（2026-11-08）

> 本记录是本轮唯一新建的 Markdown 文件。范围仅限 PaperNotes 的 NeurIPS/ECCV 2026 更新、AI Safety Daily 小红书公开主页，以及为确认候选正式身份而查阅的官方目录/论文页。引用数与优先级计算未做。

## 课题边界与判定

- **A（攻击）**：攻击者仅能控制一份真实外部长源文档；受害系统分块器及参数未知；由该源生成的同源块依托不同检索触发器，在同一正常查询下共同召回并联合诱导错误答案。关键验证包括逐块必要性、chunker迁移和真实生成端点。
- **B（防御）**：融合低成本检索统计、冻结文本语义、跨块实体/命题关系和异源参照；在有限LLM复核预算下检出污染，同时保留正常多跳证据；用独立clean-query校准最终query级OR误删风险。
- **威胁模型不合并**：持久语料投毒、运行时网页/搜索注入、Agent历史记忆投毒、普通间接提示注入、知识冲突、检索错实体分别记录。没有把相邻机制直接算成A撞车。

## 检索与目录覆盖

### PaperNotes

- 来源：[PaperNotes主页](https://papernotes.org/)、[NeurIPS 2026信息检索/RAG](https://papernotes.org/NeurIPS2026/information_retrieval/)、[ECCV 2026信息检索/RAG](https://papernotes.org/ECCV2026/information_retrieval/)及公开sitemap。sitemap检查日期为2026-11-08。
- sitemap列出NeurIPS 2026 **4,077个论文页URL、54个方向页**；ECCV 2026 **2,900个论文页URL、48个方向页**。这是站点URL/分类页计数，不声称等于去重后的会议论文总数。
- 信息检索/RAG分类页分别标示NeurIPS **18篇**、ECCV **8篇**。两页逐条读取标题/链接；其余方向页按论文页URL标题slug做广泛词面扫描。广泛词组为 `RAG / retrieval / poisoning / security / evidence / trust / robustness / memory / grounding / injection / entity / agent`，匹配 **1,140个页面URL**（NeurIPS 723、ECCV 417）；较窄的 `RAG / retrieval / poison / security / injection` 匹配 **189个URL**（113、76）。URL词面命中只用于发现，不代表读过这些页面的论文全文。
- 站点目录中提取并逐条对照正式来源的PaperNotes候选为：Deceptive Grounding、BayesRAG、MG2-RAG、MMAgent-R2、Evidence Triangulation。Evidence Triangulation由广义`evidence`词命中，其题名不含窄检索词。
- NeurIPS官方目录中另发现When Poison Meets Structure、When Does Graph Retrieval Become Answer-Supporting Evidence；本轮可见PaperNotes sitemap未定位到这两个标题的独立笔记URL。此结论仅表示本次sitemap检索未定位，不表示论文或站点其他入口不存在。

### 官方目录与筛选计数

- CCF第七版正式目录：本地PDF第57页将NeurIPS列为A类；第58页将ECCV列为B类。
- [NeurIPS 2026官方目录](https://neurips.cc/Downloads/2026)：读取 **9,145个唯一poster ID/标题行**。同一标题词组的广泛筛选命中1,567行；窄筛选 `RAG / retrieval-augmented / poisoning / Agent memory / graph retrieval / entity attribution / prompt injection` 命中89行。标题筛选后仅将本文件内4篇NeurIPS候选列为正式候选；其余命中不提升为本轮候选，不代表已全文排除。
- [ECCV 2026官方Accepted Papers目录](https://eccv.ecva.net/Conferences/2026/AcceptedPapers)：检查 **2,852个poster链接/论文行**。同一广泛筛选命中429行；窄筛选命中6行。本文件内3篇ECCV候选进入正式候选记录。
- PaperNotes与官方目录彼此重叠，计数不相加。广义词面命中中未提升为正式候选的数量：PaperNotes 1,135个URL，官方目录1,989行；这些只是标题层级未提升的数量，不将其写成“已证明无关”或“论文不存在”。
- 变体覆盖了用户指定的`RAG`、`retrieval`、`poisoning`、`security`、`evidence`、`trust`、`robustness`、`agent memory`，另加`grounding`、`entity`、`injection`以定位实体归因和运行时注入边界。标题/URL扫描不是全文筛查；正式候选才回到官方论文页和原文核验。

### 小红书公开主页

- 来源：[AI Safety Daily公开主页](https://www.xiaohongshu.com/user/profile/699b43930000000021008dbe)，检查日2026-11-08。
- 主页公开渲染出11张笔记卡片；卡片可见标题依次为：`大模型与智能体安全前沿论坛，成都见！`、`密文检索，7128项只需5.168秒！`、`签名的是W，运行的却是Q。`、`105个逻辑漏洞，不靠崩溃发现！`、`假弹窗，能把Agent带偏吗？`、`补丁挡住原PoV，漏洞还在！`、`漏报压到1%，为何91.8%要上报？`、`改写轨迹，监控器会漏看。`、`41,824条轨迹，注入藏在哪！`、`MIG隔离，还能偷偷传数据？`、`三个正常Skill，拼出98%攻击！`。
- 公开页面没有呈现这些卡片的发布日期；“登录即可查看Ta的笔记”遮挡正文。标题未出现明确RAG/语料投毒命中；“假弹窗”“轨迹注入”“Skill组合”等只作可能的Agent/运行时安全线索，不能由标题推断其具体威胁模型，未提升为论文候选。未登录、未点验证、未尝试验证码。

## 正式候选与原文核验

阅读级别：**L1**=仅书目/官方页面级；**L2**=已注明页码的选择性原文阅读；**L3**=正文全文逐页阅读。截至本轮复核，Deceptive Grounding为L3，其余候选保持各条记录所示等级。PDF路径均位于`D:\学在东南\科研数据库\20_Research\Papers\RAG安全文献`；Windows文件名中的冒号以`_`替换。

### 1. Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation

- **作者**：Cedric Caruzzo、Donggeun Yoo、Tae Soo Kim。**正式身份**：NeurIPS 2026官方Poster #152927（官方页面记载NeurIPS 2026；未公开更细track）；第七版CCF-A。官方页：[Poster #152927](https://neurips.cc/virtual/2026/poster/152927)；[NeurIPS 2026论文目录](https://neurips.cc/Downloads/2026)；原文：[arXiv:2607.09349v1](https://arxiv.org/abs/2607.09349)；arXiv-issued DOI：`10.48550/arXiv.2607.09349`；会议论文DOI未独立确认。
- **发现入口**：[PaperNotes医疗NLP条目](https://papernotes.org/NeurIPS2026/medical_nlp/deceptive_grounding_entity_attribution_failure_in_clinical_retrieval-augmented_g/)。PaperNotes只作发现入口，身份与方法以下列官方页和PDF为准。
- **PDF**：`Deceptive Grounding_ Entity Attribution Failure in Clinical Retrieval-Augmented Generation.pdf`；24页；SHA-256 `1946B73CF1D393A32D56DCD292CFF4F30BE62E8F1CEDB002C6E3307805C599E1`。此前不存在同名文件，本轮从arXiv公开PDF下载；未覆盖其他文件。
- **阅读证据**：L3，PDF物理页1–24逐页阅读，含参考文献及附录；方法/设置覆盖264个drug-disease-alternate-drug triples、15个检索条件、两种工具schema、13个模型；结果、裁判偏差/盲点、合成刺激构造、附录机制实验、制品与limitations均已核读。此等级仅表示该固定arXiv v1 PDF已逐页阅读，不代表独立复现。
- **主要结果与限制**：论文定义“Deceptive Grounding”为模型忠实复述检索文档中真实实体Y的证据、却归因给查询实体X。作者报告13模型对抗条件峰值8.0%–86.7%，另在临床部署740对中测得7.8%（新批准药物13.6%）；二者分别是合成对抗基准与部署测量，不可混作同一估计。实体归因验证(EAV)按claim核对支持文档的主实体与查询实体，在IPW调整的人类gold标准n=88上报告97.0% precision、98.7% EAF recall；EAF有效样本约18例、recall区间较宽。EAV对Entity Substitution按定义输出PASS，须配合另一个ES检测组件。合成刺激与特定临床实体构造不等于恶意持久语料投毒。
- **对A/B的关系**：不构成A攻击撞车；它没有攻击者控制的文档、未知chunker、同源多块共同召回或逐块必要性。对B是高价值实体归因检查参考：提醒“文本被检索内容蕴含”不等于“证据实体匹配”。但它不验证跨块联合污染、正常多跳保留、有限LLM复核预算，也没有独立clean-query上的最终OR误删校准。
- **Artifact核验**：官方poster链接的作者博客HEAD 200；论文未列专属代码/数据仓库。文中模型页于2026-11-08检查：L1-16B-A3B、OpenBioLLM-Llama3-70B、Gemma4-31B-it为HTTP 200；Gemma4-27B-it返回401，视为受限，未登录或绕过。没有将401模型页当作可访问artifact。
- **新增判断**：证据地图未找到同题名条目，属于本轮新增候选；PDF为新增入库。

### 2. When Poison Meets Structure: Topology-based Defense against Poisoning Attack on Graph-based Retrieval-Augmented Generation

- **作者**：Qizhi Chen、Junhao Wen、Shuang Liang、Jiakai Li、Yizhuo Ma、Rongzheng Wang、Ke Qin。**正式身份**：NeurIPS 2026官方Poster #152350；第七版CCF-A；细分track未由当前官方页面确认。官方页：[Poster #152350](https://neurips.cc/virtual/2026/poster/152350)；[OpenReview论坛](https://openreview.net/forum?id=TirVWlIdjG)；DOI/arXiv：本轮未核实。
- **原文状态**：L1。对OpenReview官方PDF端点的匿名GET/HEAD均返回403；官方OpenReview API亦返回403。官方poster上的图片不是论文PDF。遵守访问限制，未登录、未换端点绕过或用验证码访问；未找到可公开合法全文。无本地PDF、无页数/hash、无方法/结果/限制全文证据。
- **对A/B的关系**：题名直接落在Graph-RAG投毒防御，是B最应闭合的直接近邻；但在取得原文前，不推测其拓扑特征、攻击者能力、数据设置或效果，也不据题名判定撞车或差异。
- **新增判断**：证据地图已存在同题名L1未闭合记录（`src-20261108-when-poison-structure`）；本轮只复核官方poster和403状态，不重复下载、不重复计为新全文候选。

### 3. When Does Graph Retrieval Become Answer-Supporting Evidence? A Diagnostic Audit of GraphRAG

- **作者**：Chenghua Duan、Zhuo Wang、Boheng Liu、Ziyu Li、Qing Li、Xiuxing Li、Zhong Zhang、Xia Wu。**正式身份**：NeurIPS 2026官方Poster #139414；第七版CCF-A；细分track未由当前官方页面确认。官方页：[Poster #139414](https://neurips.cc/virtual/2026/poster/139414)；[OpenReview论坛](https://openreview.net/forum?id=S9CWPfaHOm)；arXiv/DOI：本次未确认。
- **原文状态**：L1。官方OpenReview PDF端点返回403；未下载、无本地PDF、无方法/结果页码。PaperNotes sitemap本轮未定位到独立题名页，故此条来自NeurIPS官方目录标题扫描；不据题名补造内容。
- **对A/B的关系**：题名指向GraphRAG检索结果何时成为答案支持证据，可能影响B“保留正常多跳证据”的基线选择；在全文可读前只登记为潜在方法参考，不声称具体技术或结果。
- **新增判断**：证据地图未找到同题名条目；待原文闭合。

### 4. MG2-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation

- **作者**：Sijun Dai、Qiang Huang、Xiaoxing You、Jun Yu。**正式身份**：ECCV 2026 Accepted Papers官方目录/Poster #3411（Poster location #117）；第七版CCF-B。官方目录：[ECCV Accepted Papers](https://eccv.ecva.net/Conferences/2026/AcceptedPapers)；[官方poster](https://eccv.ecva.net/virtual/2026/poster/3411)；[PaperNotes图学习条目](https://papernotes.org/ECCV2026/graph_learning/mg2-rag_multi-granularity_graph_for_multimodal_retrieval-augmented_generation/)；[arXiv:2604.04969v2](https://arxiv.org/abs/2604.04969)。DOI：本次未确认。
- **PDF**：`MG²-RAG_ Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation.pdf`；34页；SHA-256 `334DCA05B566CA41D2BF7C81BEBD0B5793540FAC3AAA5483ACB5366AF054F060`。文件此前已在论文库，未重复下载。
- **阅读证据**：L2，主文物理页1–15；后续主文/附录未逐页核读，不是L3。方法涉及多粒度多模态图、实体/命题关联及图上检索/随机游走，适合作为B的结构关系与正常跨证据检索参考。
- **对A/B的关系**：不是投毒论文，没有验证攻击者控制外部长源、受害者未知chunker或联合攻击块必要性。它的多模态图结构不能直接等同于文本块污染检测；也没有query级OR删块校准。价值在于给B提供“实体/关系结构如何服务正常证据检索”的强基线。
- **Artifact核验**：ECCV官方poster指向项目页，项目页和[作者GitHub仓库](https://github.com/Daboolu/MG2-RAG)于2026-11-08均HTTP 200；未发现论文固定commit/tag，记录为当前可访问仓库而非可复现固定版本。
- **新增判断**：证据地图未找到同题名条目；论文PDF已存在库中，本轮新增的是正式候选与比较记录，不是新PDF。

### 5. BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation

- **作者显示差异**：NeurIPS官方Poster #154974列Xuan Li、Yining Wang、Haocai Luo、Shengping Liu、Jiaen Liang、Ying Fu、Wei Huang、Jun Yu、Junnan Zhu；本地arXiv v1 PDF首页对应位置显示Jerry Liang、Weihuang。未静默合并为同一写法，书目冲突保留待作者/正式版确认。**正式身份**：NeurIPS 2026官方poster #154974；第七版CCF-A；细分track未公开确认。官方页：[Poster #154974](https://neurips.cc/virtual/2026/poster/154974)；[OpenReview论坛](https://openreview.net/forum?id=9Vk5e1o3lU)；[arXiv:2601.07329v1](https://arxiv.org/abs/2601.07329)。DOI：本次未确认。
- **PDF**：`BayesRAG_ Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation.pdf`；17页；SHA-256 `3959F6C54864FEDA6C1919810D78BD0246F584101B10E17D451BC96AEAD60062`。此前已存在，未重复下载。
- **阅读证据**：L2，主文物理页1–9；非全文/附录精读。核心是对多模态检索证据作概率/DS证据融合，并结合图结构或版面先验处理模态冲突。
- **对A/B的关系**：对B的异源证据融合有参考价值；但研究的是多模态证据互证，不是恶意语料投毒/污染检测，也未给出块级因果必要性、有限LLM复核策略或query级OR风险校准。不能把“证据互相支持”直接当作来源可信证明。
- **Artifact核验**：NeurIPS官方poster链接[代码仓库](https://github.com/TioeAre/BayesRAG)，仓库网页HEAD 200；GitHub API版本查询遇到403 rate limit，未取得commit SHA/tag，故只确认仓库页可达，不声称固定版本。文中HuggingFace组织页可达，但非具体checkpoint。
- **新增判断**：证据地图未找到同题名条目；PDF此前已存在。

### 6. Evidence Triangulation for Multimodal Fact-Checking in the Wild

- **作者**：Stefanos-Iordanis Papadopoulos、Zacharias Chrysidis、Christos Koutlis、Symeon Papadopoulos、Panagiotis C. Petrantonakis（ECCV名单省略中间名首字母）。**正式身份**：ECCV 2026 Accepted Papers官方目录/Poster #4874（Poster location #416）；第七版CCF-B。官方目录：[ECCV Accepted Papers](https://eccv.ecva.net/Conferences/2026/AcceptedPapers)；[官方poster](https://eccv.ecva.net/virtual/2026/poster/4874)；[PaperNotes社会计算条目](https://papernotes.org/ECCV2026/social_computing/evidence_triangulation_for_multimodal_fact-checking_in_the_wild/)；[arXiv:2606.31367v1](https://arxiv.org/abs/2606.31367)。DOI：本次未确认。
- **PDF**：`Evidence Triangulation for Multimodal Fact-Checking in the Wild.pdf`；14页；SHA-256 `ABF0B8AFF1A6ECD5A1C1593B23759B9CA93A2BBCF097EC39A4C8954FE7D5A04A`。此前已存在。
- **阅读证据**：L2，主文物理页1–10；非全文/附录精读。工作以开放网页/社交内容做运行时多模态事实核查，结合来源筛选和跨源关系核验；其攻击/数据对象不是持续写入受害RAG知识库的外部长源文档。
- **对A/B的关系**：可为B的异源参照、跨来源蕴含/矛盾关系特征提供方法参照；不能作为持久语料投毒检测或chunker迁移证据，也没有最终query级OR误删校准。明确归类为运行时网页证据核查的邻近方法，而非RAG投毒防御。
- **Artifact核验**：[作者代码/数据仓库](https://github.com/stevejpapad/evidence-triangulation)于2026-11-08 HTTP 200；[gte-Qwen1.5-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct)与[MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6)模型页HTTP 200。仓库说明X-POSE数据需要机构邮箱验证；未申请访问、未提供邮箱、未绕过门槛。代码页可达不等于受限数据可达。
- **新增判断**：证据地图未找到同题名条目；PDF此前已存在。

### 7. MMAgent-R2: Learning to Rerank and Reject for Agentic mRAG

- **作者**：Tao Zhang、Ziqi Zhang、Zongyang Ma、Yuxin Yang、Bing Li、Chunfeng Yuan、Kang Rong、Fengyun Rao、Jing Lyu、Weiming Hu。**正式身份**：ECCV 2026 Accepted Papers官方目录/Poster #4250（Poster location #164）；第七版CCF-B。官方目录：[ECCV Accepted Papers](https://eccv.ecva.net/Conferences/2026/AcceptedPapers)；[官方poster](https://eccv.ecva.net/virtual/2026/poster/4250)；[PaperNotes信息检索条目](https://papernotes.org/ECCV2026/information_retrieval/mmagent-r2_learning_to_rerank_and_reject_for_agentic_mrag/)；arXiv:2607.07383。DOI：本次未确认。
- **PDF**：`MMAgent-R2_ Learning to Rerank and Reject for Agentic mRAG.pdf`；17页；SHA-256 `F4DFCB85DD2170931F1F43FD755FFE309C988F1A6347F4DCD7A782787D1FF5AE`。此前已存在。
- **阅读证据**：L2，正文物理页1–15；参考文献及全部附录未逐项核读，不是L3。方法以视觉重排序和主动拒绝为Agentic mRAG候选校验，并使用GRPO/步级验证奖励。
- **对A/B的关系**：对B的候选级筛选/拒绝可作系统基线；不是恶意投毒检测，不能将拒绝效用等同于正常clean-query删块风险控制，也未验证A的同源块必要性。
- **Artifact核验**：所查ECCV官方poster页与PDF文本未发现作者代码/数据仓库链接；不据此断言全网不存在。官方poster PDF页可达，但不是代码artifact。
- **新增判断**：证据地图已有L2记录（`src-20261108-mmagent`），论文库也已存在；本轮仅纳入PaperNotes扫描与比较状态，不重复建档。

## 小结、排除与未闭合项

- 本轮正式记录7篇：4篇NeurIPS、3篇ECCV；其中5篇有公开可读PDF并完成`pdfinfo`页数、SHA-256及逐篇阅读记录：**L3 1篇**（Deceptive Grounding，物理页1–24），L2 4篇；2篇（When Poison Meets Structure、When Does Graph Retrieval Become Answer-Supporting Evidence）官方OpenReview PDF均403，保持L1。5个PDF中1份是本轮新增下载，4份已在论文库；未覆盖已有PDF。
- 标题筛选中未提升为候选的主题主要包括非RAG视觉/向量检索、模型/预训练数据投毒、视觉模型后门、运行时间接提示注入、Agent记忆/多用户记忆投毒、知识冲突和一般RAG工程。它们分别计入词面筛选未提升数，不与持久语料投毒混为一类；没有声称这些方向不存在或已逐篇精读。
- 最重要未闭合项仍是When Poison Meets Structure全文；其次是GraphRAG答案支持证据审计全文。未找到受限PDF的替代合法公开版本；没有绕过403、登录或验证码。
- XHS页面登录遮挡导致11条笔记的正文、发布时间和附件均不可核。当前不能判断其中是否有未公开卡片、正文提到的RAG论文或新发现；不以标题猜测为事实。
- **未做**引用数核实与优先级计算；未写入或修改`docs`、证据地图、BibTeX、合并台账、`.gitignore`或他人输出；没有创建逐论文/逐查询临时文件。
