# TOIS 2024–2026 目录覆盖与近邻筛查

审计截止日按任务要求为 **2026-11-10**；本地状态核对及 EMPRA 作者稿 hash 比对在 **2026-11-11** 完成。2026-11-11 对 ACM 正式 PDF 直链另作浏览器可达性检查时出现 Cloudflare 安全验证页，未尝试解决验证，也未取得该 PDF。范围为 ACM Transactions on Information Systems (TOIS) 第42–44卷、2024–2026年。这里报告可复核的 Crossref 全年卷期快照、历史 ACM DOM 证据、DBLP差额、候选筛查及阅读边界；不把目录筛查冒称全卷出版社逐篇闭合，也不声称不存在撞题工作。

## 数据源、检索式与计数

主清单为 Crossref ISSN `1046-8188` Works API 响应快照：`catalog_tois_2024-2026_sources/crossref_issn_1046-8188_2023-2026_response_20261110.json`；筛出第42–44卷、日期为2024–2026的登记记录为 `catalog_tois_2024-2026_sources/crossref_tois_volumes_42-44_2024-2026_20261110.jsonl`。后者SHA-256：`AC2463BBFC68254D5F06BA25183725C106E79EDA9D6F520FDBF645C8BDD66D9D`。

筛查先按标题信号 `RAG`、`RAGnRoll`、`retrieval-augmented` 及 `poisoning / attack / adversarial / security / privacy / malicious / backdoor / injection / vulnerability / robustness` 建立候选；再对标题含 retrieval/ranking/search/RAG/question-answer/information-retrieval 的记录扩展相同风险词摘要筛查。共35条标题触发、20条摘要触发，去重后50个候选（逐篇列于下表）。这是透明的发现式筛选式，不是语义完备检索式；特别是未命中词表的隐式安全贡献仍可能漏检。

实际使用的大小写不敏感正则如下；标题候选为 `title_rag OR title_security`，摘要扩展为 `abstract_domain AND abstract_risk`，最终按DOI去重：

```text
title_rag      = (?i)\bRAG\b|RAGnRoll|retrieval[- ]augmented
title_security = (?i)\b(poison(?:ing)?|attacks?|adversarial|security|privacy|malicious|backdoor|injection|vulnerab|robustness)\b
abstract_domain = (?i)retriev|rank|search|RAG|question answer|information retrieval
abstract_risk   = (?i)\bpoison(?:ing)?\b|\battacks?\b|\badversarial\b|\bsecurity\b|\bprivacy\b|\bmalicious\b|\bbackdoor\b|\binjection\b|\bintegrity\b|\brobust(?:ness)?\b|\bcontaminat\w*|data leak\w*|vulnerabilit\w*
```

| 卷期 | Crossref记录数 |
|---|---:|
| 42(1)–42(6) | 32, 30, 25, 25, 28, 27；合计167 |
| 43(1)–43(6) | 26, 29, 28, 27, 31, 27；合计168 |
| 44(1)–44(8) | 29, 26, 24, 26, 25, 24, 21, 10；合计185 |
| **总计** | **20期，520个唯一DOI、520个唯一题名** |

520条 Crossref 记录的 `type` 均为 `journal-article`，但这不等于520篇原创研究。快照中按标题可识别出12条前置/更正类记录：42(5) *Special Section on Efficiency in Neural Information Retrieval*；43(2)、43(5) 两篇 *Pre-Trained Models for Search and Recommendation* 专刊导言；43(6) 因果表示专刊导言；44(6) QPP专刊导言；以及44(1)、44(2)、44(3)两条、44(4)、44(5)、44(7)的 Erratum/Corrigendum。DBLP/出版方书目中有些更正记录页码格式不同，故不把它们删除出原始目录分母。未发现独立“reviewer list”标题记录；由于未取得当日全量ACM期页，不能据此证明出版社目录没有此类前置内容。

520条中有516条带 Crossref摘要；无摘要的4条是上述42(5)专栏标题、43(2)/43(5)专刊导言和43(6)专刊导言。这4条只能标题筛查。历史交接摘要曾报告“520题名已人工筛、72篇摘要已读”，但没有找到与这两个数字一一对应的持久化逐篇日志；本记录只确认输入数据计数和本表50候选筛查，**不把未留档的72篇升级为本轮可审计的阅读数**。

## 独立目录交叉核验与缺口

- **DBLP**：卷页可访问，按当前搜索/API观察得到卷级总数42卷167、43卷168、44卷154，合计489，与Crossref 520相差31。DBLP卷页： [42](https://dblp.org/db/journals/tois/tois42.html)、[43](https://dblp.org/db/journals/tois/tois43.html)、[44](https://dblp.org/db/journals/tois/tois44.html)。2026-11-11直接机器API请求返回 HTTP 202 “Making sure you're not a bot”验证页；按访问规则停止，不绕过。当前无法逐DOI匹配、分期计数或解释31条差额，因此不能宣称Crossref/DBLP目录身份闭合。
- **ACM DL**：既有 `catalog_tois_browser.md` 记录的是2026-11-02对TOIS 44(1)–44(8)的DOM集合快照，共185条，8期逐期集合与当时Crossref目录相符；该材料明确“标题主题筛查0、摘要阅读0”，且不是2026-11-10刷新。当前没有42卷或43卷全期官方DOM快照。2026-11-11非浏览器直接请求ACM PDF端点返回403；同日 Edge 打开同一正式 PDF 直链后显示 Cloudflare 安全验证页。本轮未操作该验证或绕过访问控制，正式 PDF 仍未取得。检索到的 [Paperity条目](https://paperity.org/p/376513499/invisible-black-box-backdoor-attack-against-deep-cross-modal-hashing-retrieval)标明是远程PDF预览，下载入口仍指向ACM；没有取得独立作者稿文件，不将网页预览记为PDF阅读。
- **44(8)状态**：2026-11-10 Crossref快照含10条，在线日期均为2026-10-21、print日期为2026-11-30；截至审计日该期仍属在编/未来印刷期，不把10条称为最终封卷数量。旧ACM DOM证据同样把44(8)标作 Issue-in-Progress，但观察日是11月2日。
- **完整性结论**：Crossref 20期/520 DOI是可核验的主数据快照；DBLP卷总数差31未逐条调和；ACM只有44卷历史快照；reviewer/front matter无法由未访问的期页排除。不得表述为“2024–2026 TOIS官方全卷逐篇完全闭合”或“零漏检”。

### 2026-11-11增量核验

- **ACM第42、43卷官方目录**：对官方 TOC 页 [TOIS 42(1)](https://dl.acm.org/toc/tois/2024/42/1) 的一次正常页面请求返回 HTTP 403。依照访问限制，收到403后停止，没有继续请求42(2)–42(6)或43(1)–43(6)，也没有改用代理或其他方式绕过。故本次成功取得的官方逐期TOC为 **0/12**；此前“未取得42、43卷官方全期快照”的缺口仍在。
- **DBLP差额**：既有DBLP卷级观察仍为42卷167、43卷168、44卷154，合计489；本轮直接请求DBLP公开搜索API时返回HTML而非JSON，不能取得逐条记录；此前对该API的HTTP 202验证拦截也已记录。遵循停止规则，不再尝试其他DBLP入口或替代访问方式。逐DOI差集因此仍**无法闭合**。
- **可核验的期数算术**：Crossref基线中44(1)–44(6)合计154，44(7)为21，44(8)为10。31条卷级差额恰等于44(7)+44(8)的条数，而DBLP 44卷总数154恰等于Crossref 44(1)–44(6)合计。这个吻合支持“当前DBLP卷级观察可能尚未收录44(7)–44(8)”的解释，但不构成逐DOI缺失证明；这31条不能逐篇标成DBLP缺项或已调和。待核对的Crossref DOI仍可从既有 `catalog_tois_2024-2026_sources/crossref_tois_volumes_42-44_2024-2026_20261110.jsonl` 按volume=44、issue=7/8提取，无需复制另建差异清单。
- **44卷时效性**：2026-11-11从 [Crossref REST API](https://api.crossref.org/journals/1046-8188/works?filter=from-pub-date%3A2026-01-01%2Cuntil-pub-date%3A2026-12-31&rows=1000) 取得HTTP 200响应。该查询按2026年出版日期过滤，端点共返回172条，其中volume 44为143条；它不是完整的44卷目录，不能用143替换185。44(7)仍为21条，44(8)仍为10条；两期 DOI 集合与11月10日Crossref快照比较均为新增0、移除0。44(7)印刷日期为2026-09-30；44(8)十篇的在线日期为2026-10-21、印刷日期均为2026-11-30。44(8)的最新官方DOM证据仍是11月2日的历史观察（标为Issue-in-Progress）；本轮因ACM访问403，无法确认11月11日官方期页状态，故仍应标为在编/待印刷，不称最终封卷。
- **增量结论**：42–43卷官方逐期目录未能补齐；31条差额已缩小到“数量上对应44(7)与44(8)”的解释，但逐DOI仍待DBLP无验证访问恢复后核对；44(8)截至11月11日的Crossref登记无新增，官方实时状态未核实。以上不改变“目录完整性尚未闭合”的总判断。

## 标题与摘要候选逐篇筛查

类别：`D` = RAG安全直接工作；`M1` = 强方法近邻；`M2` = 方法/安全边界邻近但不构成直接撞题；`R` = RAG系统/评测/综述相关但摘要未显示安全贡献；`X` = 领域或任务不符。来源以本目录Crossref摘要为准；除已存在的父任务正式笔记外，本表不等同逐篇全文阅读。

| 卷期 / DOI | 题名 | 类别与筛查理由 |
|---|---|---|
| 42(1) / 10.1145/3589000 | Training Robust Deep Collaborative Filtering Models via Adversarial Noise Propagation | X：协同过滤的扰动鲁棒性，不处理检索语料或RAG上下文。 |
| 42(2) / 10.1145/3617825 | DA-DAN: A Dual Adversarial Domain Adaption Network for Unsupervised Non-overlapping Cross-domain Recommendation | X：跨域推荐训练方法，不是检索攻击/防御。 |
| 42(2) / 10.1145/3617892 | Person-action Instance Search in Story Videos: An Experimental Study | X：视频实例搜索评测，摘要无对抗安全机制。 |
| 42(3) / 10.1145/3632524 | Cross-domain Recommendation via Dual Adversarial Adaptation | X：对抗域适配用于推荐，不含恶意语料或RAG。 |
| 42(3) / 10.1145/3633202 | Privacy-Preserving Individual-Level COVID-19 Infection Prediction via Federated Graph Learning | X：隐私保护疾病预测，与RAG检索安全无直接关系。 |
| 42(4) / 10.1145/3643131 | Can Perturbations Help Reduce Investment Risks? Risk-aware Stock Recommendation via Split Variational Adversarial Training | X：金融推荐的风险/训练扰动，不是检索语料攻击。 |
| 42(4) / 10.1145/3650205 | Invisible Black-Box Backdoor Attack against Deep Cross-Modal Hashing Retrieval | M2：检索模型训练期跨模态后门，威胁对象是hash模型而非RAG文档库；仅摘要筛查，未全文精读。 |
| 42(5) / 10.1145/3634911 | Data Augmentation for Sample Efficient and Robust Document Ranking | M2：文档排序鲁棒性/数据增强可作背景，但摘要不是投毒威胁或RAG防御。 |
| 42(5) / 10.1145/3652853 | Discrete Federated Multi-behavior Recommendation for Privacy-Preserving Heterogeneous One-Class Collaborative Filtering | X：联邦推荐和用户隐私，不是RAG安全。 |
| 42(5) / 10.1145/3653448 | Privacy-preserving Cross-domain Recommendation with Federated Graph Learning | X：跨域推荐的隐私学习，不是检索增强系统。 |
| 42(6) / 10.1145/3681784 | A Self-Distilled Learning to Rank Model for Ad Hoc Retrieval | X：常规排序模型提升，摘要无攻击/防御。 |
| 42(6) / 10.1145/3666088 | Adversarial Item Promotion on Visually-Aware Recommender Systems by Guided Diffusion | M2：目标项目推广攻击与排序操纵有类比，但攻击面是视觉推荐模型/项目。 |
| 42(6) / 10.1145/3665324 | Bridging Dense and Sparse Maximum Inner Product Search | X：检索算法，不含安全目标。 |
| 43(1) / 10.1145/3694783 | Distributed Recommendation Systems: Survey and Research Directions | X：分布式推荐综述，不是RAG安全。 |
| 43(1) / 10.1145/3698876 | Meta-Learning to Rank for Sparsely Supervised Queries | X：稀疏监督排序，未见安全威胁。 |
| 43(1) / 10.1145/3696105 | Multi-Agent Attacks for Black-Box Social Recommendations | M2：黑盒多智能体攻击，但目标为社交推荐而非RAG语料检索。 |
| 43(2) / 10.1145/3695868 | Building a Coding Assistant via the Retrieval-Augmented Language Model | R：检索增强代码助手应用，摘要未显示安全攻击/防御。 |
| 43(2) / 10.1145/3701228 | CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models | R：RAG基准可作评测背景，摘要聚焦一般质量评测而非安全。 |
| 43(2) / 10.1145/3708884 | Decoy Effect in Search Interaction: Understanding User Behavior and Measuring System Vulnerability | M2：搜索结果对decoy效应的易感性属于交互层排序风险，不是恶意检索投毒/RAG。 |
| 43(2) / 10.1145/3676957 | FIT-RAG: Black-Box RAG with Factual Information and Token Reduction | R：黑盒RAG框架，但摘要目标是事实信息利用和token压缩，无安全攻击/防御。 |
| 43(2) / 10.1145/3707204 | Privacy-Preserving Sequential Recommendation with Collaborative Confusion | X：推荐隐私保护，不是RAG检索安全。 |
| 43(4) / 10.1145/3728359 | Federated Semantic Learning for Privacy-preserving Cross-domain Recommendation | X：联邦跨域推荐，不涉及RAG安全。 |
| 43(5) / 10.1145/3745025 | Interaction Privacy Vulnerability in Federated Recommendation and Lossless Countermeasure | X：联邦推荐交互隐私，威胁和防护目标与知识检索不同。 |
| 43(6) / 10.1145/3759453 | A Survey of Conversational Search | X：对话搜索综述，摘要没有安全贡献。 |
| 43(6) / 10.1145/3749099 | Agent4Ranking: Semantic Robust Ranking via Personalized Query Rewriting Using Multi-Agent LLMs | M2：查询改写与群体差异下排名鲁棒性可作边界背景，但不是投毒/攻击防御。 |
| 43(6) / 10.1145/3757059 | DuAda: Adaptive Targeted Model Poisoning Attack Framework via Dummy User Simulation on Federated Recommendation | M2：推荐模型/梯度投毒，不是RAG外部文档或检索索引投毒。 |
| 44(1) / 10.1145/3762182 | LLM4DSR: Leveraging Large Language Model for Denoising Sequential Recommendation | X：清理用户交互噪声的推荐方法，不是RAG知识源净化。 |
| 44(1) / 10.1145/3765617 | Projection-Displacement-Based Query Performance Prediction for Embedded Space of Dense Retrievers | X：密集检索QPP方法，非安全检测/攻击。 |
| 44(1) / 10.1145/3768153 | Robust Neural Information Retrieval: An Adversarial and Out-of-Distribution Perspective | M2：神经IR对抗/OOD鲁棒性综述，值得背景引用；不是RAG直接先例，未全文阅读。 |
| 44(2) / 10.1145/3777378 | Graph Retrieval-Augmented Generation: A Survey | R：GraphRAG综述，摘要为一般架构/知识增强综述，未显示安全专章证据。 |
| 44(3) / 10.1145/3787468 | FedHoG: Federated Homogeneous Graph Neural Network for Privacy-Preserving Recommendation | X：联邦推荐，不是RAG。 |
| 44(3) / 10.1145/3786609 | U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-in-a-Haystack | R：RAG/长上下文评测，不是攻击或防御工作。 |
| 44(4) / 10.1145/3800948 | Push and Pull: Defending against Retrieval Poisoning Attacks via Embedding Space Reshaping | D：直接针对RAG检索投毒防御。父任务已有正式VOR PDF与L2选页笔记 `notes/ShieldRAG_Safeguarding_Retrieval-Augmented_Generation_from_Untrusted_Kno__work-31cb317e5ccd.md`；本增量去重，不重复下载/阅读/建笔记。 |
| 44(4) / 10.1145/3802586 | A Survey of Personalization: From RAG to Agent | R：RAG到Agent的个性化综述，摘要没有检索安全机制。 |
| 44(4) / 10.1145/3797026 | Balancing Imperceptible and Aggressive Poisoning Attack for Recommender Systems: A Simple Multinomial Diffusion Model | M2：推荐训练数据投毒与隐蔽性，但不是知识文档/检索器投毒。 |
| 44(4) / 10.1145/3795527 | Direct Retrieval-augmented Optimization: Synergizing Knowledge Selection and Language Models | R：优化RAG知识选择与LM协同，摘要未显示攻击/安全评估。 |
| 44(4) / 10.1145/3801943 | EMPRA: Embedding Perturbation Rank Attack against Neural Ranking Models | M1：单文档文本增补操纵黑盒NRM排序，最强排序攻击方法近邻；本轮已读作者稿正文pp.1–38并另存逐篇笔记。 |
| 44(4) / 10.1145/3800961 | MetaRAG: Identifying Website Owner Using Meta-Path-Guided Dynamic Graph Retrieval-Augmented Generation | R：用RAG做网站所有者识别/来源关联；安全是应用背景，摘要未显示对抗/防御问题。 |
| 44(4) / 10.1145/3803545 | Privacy Matters: Data Attack to Make User Preferences Unlearnable in Recommendation | X：用户隐私/推荐训练数据攻击，不是RAG语料攻击。 |
| 44(4) / 10.1145/3795521 | Retrieval-Augmented Purifier for Robust LLM-Empowered Recommendation | M2：检索协同图用于净化被投毒/扰动的推荐交互；与知识源净化有方法类比。父任务已有PDF及L2笔记 `notes/Retrieval-Augmented_Purifier_for_Robust_LLM-Empowered_Recommendation__work-e666e15f7afd.md`，本增量不重复。 |
| 44(4) / 10.1145/3801969 | Statistical Filtering for Fair Item Ranking | X：公平排序过滤，不是安全攻击或RAG防御。 |
| 44(6) / 10.1145/3827605 | Adaptive Query Performance Prediction for Retrieval-Augmented Generation: Bridging Retrieval Quality and Generation Relevance | R：RAG检索质量预测，摘要面向查询评估/选择性处理，未显示安全威胁。 |
| 44(6) / 10.1145/3815198 | RAQG-QPP: Query Performance Prediction with Retrieved Query Variants and Retrieval-Augmented Query Generation | R：RAG-QPP/查询变体方法，不是安全机制。 |
| 44(6) / 10.1145/3790102 | Reversing the Retrieval Engine: Query Performance Prediction as an Inverse Learning Task | X：通用QPP建模，无安全目标。 |
| 44(6) / 10.1145/3818621 | TeaRAG: A Token-Efficient Agentic Retrieval-Augmented Generation Framework | R：Agentic RAG效率框架，摘要无攻击/防御。 |
| 44(7) / 10.1145/3841465 | GenTREC: The First Test Collection Generated by Large Language Models for Evaluating Information Retrieval Systems | X：IR基准/测试集生成，不是安全研究。 |
| 44(7) / 10.1145/3831683 | Dynamic Uncertainty Learning with Noisy Correspondence for Text-based Person Retrieval | X：图文行人检索噪声鲁棒性，不是RAG/对抗安全。 |
| 44(7) / 10.1145/3837856 | Modular RAG: Transforming RAG Systems into LEGO-like Reconfigurable Frameworks | R：模块化RAG架构，摘要无安全攻击/防御。 |
| 44(7) / 10.1145/3831679 | RAGnRoll: Learning to Iteratively Retrieve and Generate Attributable Answer Snippets | R：检索与生成归因片段，可能作溯源背景；摘要未呈现恶意检索攻击或安全防御。 |
| 44(8) / 10.1145/3833415 | A Survey on Knowledge-Oriented Retrieval-Augmented Generation | R：知识型RAG综述；截至本快照未确认其目录状态以外的安全专门贡献。 |

## 已读论文与制品状态

|论文|筛查结论|PDF与阅读证据|代码制品|
|---|---|---|---|
|EMPRA (DOI 10.1145/3801943)|M1强方法近邻；TOIS 44(4)，CCF-A|上述论文库PDF；41页作者稿；SHA-256 `D3639BE76C016DFA9321FCF067B0268CACA2684035031E4CD1397C613169AF10`；实读作者稿物理pp.1–38；VOR未取得，ACM PDF 403|作者论文p14给出的 [aminbigdeli/EMPRA](https://github.com/aminbigdeli/EMPRA)；未运行|
|Push and Pull / ShieldRAG (DOI 10.1145/3800948)|D直接工作；CCF-A；父任务已有记录|已有正式VOR PDF及选页L2笔记；本轮不重复。既有笔记记录31页PDF SHA-256 `d1b98b9698907c42f7c965f2455ae8d7f387738655b42e9988d900776a219460`|已有记录未核实代码链接|
|Retrieval-Augmented Purifier (DOI 10.1145/3795521)|M2方法邻近；CCF-A；父任务已有记录|已有42页PDF及L2笔记；本轮不重复|本轮不核代码|
|其余47个候选|依上表标为M2/R/X；未据标题/摘要声称全文阅读|仅做标题/摘要筛查；没有新下载PDF|未逐篇核代码|

本轮新增逐篇阅读记录仅EMPRA；没有下载新PDF（作者稿早已在指定论文库，且与作者公开URL字节一致），没有运行代码，没有查询引用数或计算优先级。`Push and Pull`与`Retrieval-Augmented Purifier`的既有笔记已去重，不作覆盖性复述。

## 下一步与不能声称的结论

1. 若DBLP API恢复无验证访问，按DOI逐期对账Crossref 520与DBLP 489，解释卷44的31条差额，并重新区分更正/专刊导言/研究文章。
2. 取得42、43卷和44卷最新ACM全期TOC快照后，核验当前期页、分页及reviewer/front matter；44(8)应在2026-11-30印刷日后再更新。
3. `Invisible Black-Box Backdoor Attack against Deep Cross-Modal Hashing Retrieval`是保留的摘要级检索后门邻近项，但威胁对象不同且本轮未取得其正式全文；2026-11-11 ACM PDF 直链在浏览器触发 Cloudflare 安全验证，尚无可用的本地 PDF。后续仅在正式页面可正常访问或找到合法作者/机构稿时继续全文核验。

当前证据支持“TOIS已有一篇直接RAG检索投毒防御工作（Push and Pull），另有EMPRA这篇文档注入式排序攻击强方法近邻”；不支持“全部TOIS目录已出版社逐篇闭合”“所有近邻全文均已读”或“开题不存在其他潜在撞车工作”。
