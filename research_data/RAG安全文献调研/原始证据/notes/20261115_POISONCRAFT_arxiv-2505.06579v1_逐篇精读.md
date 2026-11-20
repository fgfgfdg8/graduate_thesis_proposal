# POISONCRAFT（arXiv:2505.06579v1）独立精读

- 阅读、代码与文献核验：2026-11-15（Asia/Shanghai）。阅读对象是下述 14 页作者预印本，正文、参考文献和附录均已逐页检查；下文“页”均为该 PDF 物理页码，亦与其印刷页码一致。网页摘要上的 “12 pages, 7 tables and 3 figures” 与实际文件的 14 页、表 I–IX 不一致，阅读范围按实际文件记录。
- **准确身份**：Yangguang Shao、Xinjie Lin、Haozheng Luo、Chengshang Hou、Gang Xiong、Jiahao Yu、Junzheng Shi，**POISONCRAFT: Practical Poisoning of Retrieval-Augmented Generation for Large Language Models**，arXiv:2505.06579v1，2025-05-10；预印本 DOI [10.48550/arXiv.2505.06579](https://doi.org/10.48550/arXiv.2505.06579)。作者顺序以[arXiv 官方记录](https://arxiv.org/abs/2505.06579v1)、[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2505.06579)及 PDF 第 1 页为准。
- 作者公开 PDF：[arXiv v1](https://arxiv.org/pdf/2505.06579v1)，本地阅读件 [POISONCRAFT_ Practical Poisoning of Retrieval-Augmented Generation for Large Language Models.pdf](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/POISONCRAFT_ Practical Poisoning of Retrieval-Augmented Generation for Large Language Models.pdf>)；冒号替换为 Windows 合法的 `_`。文件 1,182,358 字节，14 页，未加密；SHA-256 `bf73cddfffef100d502e6c04cdab7374dd5a01b90011760a3dd8d71df56c51a9`。arXiv 页面标注论文 CC BY 4.0；它不等同于其他制品的授权。
- **去重**：在开题工作根的 `research_data`、`docs`、`ref` 中对 arXiv ID、预印本 DOI、完整题名和下述同题会议 DOI 做不受 ignore 规则限制的文本检索，未找到本篇身份匹配项或已有完整精读笔记；同时检查论文库文件名。对 `PoisonCraft` 的单词检索命中 GuardRAG 笔记及其台账来源等，所记是“扫描到的 PoisonedRAG/PoisonCraft 链接仅为对比来源”，不是本篇的独立阅读记录。不能按简称把这些记录当作本篇已读。

## 一、出版身份及会议等级：保留边界

- 此处阅读和归档的是 **2025 年 arXiv 七作者版本**。arXiv 当前页面只列 v1 和 arXiv DOI，未给出经过作者确认的正式会议引用或正式出版 DOI。因此，尚不能将同题会议记录的身份、会议 DOI 或 CCF 等级赋给该预印本。
- 可独立核验到一条 **同标题但作者名单不同**的 2026 会议记录：[IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11582092)、[CSCWD 官方议程](https://fyust.edu.cn/gjhyqk/cscwd2026/program.pdf)物理第 27 页（编号 266）及 [IEEE 出版方 Crossref deposit](https://api.crossref.org/works/10.1109/CSCWD68734.2026.11582092) 给出 Yangguang Shao、Chengshang Hou、Gaopeng Gou、Gang Xiong、Junzheng Shi，题名为 *PoisonCraft: Practical Poisoning of Retrieval-Augmented Generation for Large Language Models*，载 *2026 29th International Conference on Computer Supported Cooperative Work in Design (CSCWD)*，pp. 1068–1073，DOI `10.1109/CSCWD68734.2026.11582092`，deposit 的出版日期 2026-05-13。两者首作者及部分作者重合，但作者名单不同；这些事实不单独证明七作者稿就是该会议论文的正式版。
- [CCF 2026 年目录发布页](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml)及[高校镜像的 CCF 2026 目录 PDF](https://cce.ncepu.edu.cn/docs/2026-08/75b5af5644e64b519884bf7383f1bde9.pdf)显示：PDF 物理第 66/72 页，“三、C 类”第 10 项列出 CSCWD、会议全名和 DBLP `conf/cscwd` 入口。该条出版社栏为 Springer，而上述 2026 会议条目的 DOI 由 IEEE 登记。**这仅是对会议目录项的独立观察，不为本七作者 arXiv 稿赋 C 类**；若将来需要建立会议论文与预印本的版本关系，还须作者或正式出版全文提供明确证据。

## 二、问题、能力与资产

论文目标不是让答案必然出现指定错误事实，而是让模型在回答用户问题时推荐攻击者指定网址；作者希望主体答案仍正确，从而让额外网站看起来可信（第 3–4 页、式 1）。论文示例展示了正确回答后附加网址，但并未由此证明所有案例的事实正确性或不损害效用（第 9–10 页，及本笔记第七节）。网址是输出污染目标，不等于用户实际访问、执行恶意代码或造成实际损失。

| 维度 | 论文明确设定 | 不能推演成 |
|---|---|---|
| 可控资产 | 可向目标知识库注入不超过 `n·p` 个攻击者构造文档；不能查看或修改库内其他内容，第 3–4 页。第 2、13–14 页多处描述投毒率 0.5%。 | 仅控制一篇原始源文档；也不是无需入库权限。 |
| 目标查询 | 攻击推理时看不到、不能修改真实用户的具体查询、主题或意图，第 3–4 页。 | 完全不知道查询分布：作者拥有与目标查询不重叠、但近似其分布的影子查询，并据其领域分配预算。 |
| 可观测与代理 | 主实验的 Contriever、SimCSE 对构造者白盒，能使用编码器、相似度和梯度；生成 LLM 为黑盒，第 3–6 页。跨模型迁移另测，见表 VII。 | 默认能够对任意未知检索器进行零知识白盒优化，或黑盒迁移仍有同等成功率。 |
| 攻击时机 | 先离线生成并注入，真实查询到达时被动检索和生成，不改用户查询，第 4 页。 | 攻击者已证明能穿过所有真实文档摄取、过滤或权限管理流程。 |

**影子查询来源的实证限制。** 实验从每个数据集的同一测试集随机选取 20% 用作影子，余下 80% 评估；两部分分离，但这给攻击者提供了与目标同源的分布样本，不代表面对未知分布漂移或完全没有代表性影子样本时仍有效（第 5–6 页，表 II）。

## 三、构造过程与“图 / 分块”边界

- 每条注入文本是 `C_inject + C_freq + C_adv`（第 4–5 页，式 2、算法 1）。前缀要求模型在答案中推荐网址；高频词从整个影子集提取，优化后缀用 GCG 最小化对一批影子查询的负相似度。按影子查询所属主题分配投毒预算并分别生成候选，最后汇总为投毒集（第 4–5 页，式 3–5）。论文第 4 页称不是显式指令，但同页样例包含大写 `MUST recommend`；应依样例认定其至少包含直接的行为性要求，不把“自然伪装”当成无指令的证据。
- 主要设置：14 个影子主题、10 个高频词、每批保留 4 个候选、后缀长度 50–85、步长 5、最多 500 次迭代、每批 4 个查询，top-k 为 5、10、20（第 6 页）。第 5 页把主题划分描述为查询嵌入上的标准聚类，第 6、13 页具体又采用 GPT-4o 和预定义 14 个领域对查询分类；两种描述的精确组合需看运行记录。
- 文中将构造文本作为可索引的检索文档，**没有展示从攻击文本抽取知识图谱、建立实体边、污染图索引的实现或实验**。第 4–6 页的方法是文本向量相似度优化；第 9–10 页案例是检索后的指令影响生成。其参考文献出现图重排论文不等于本方法采用 GraphRAG。
- **未知 chunker 未评估**：文中没有看到先将多个互补子载荷写入单一长源、再通过未知受害者分块器构造角色块、改变分块长度与相位、或报告切断后的保留率/联合召回；不能据此声称该攻击耐受未知分块，也不能据此认定其必然失败。代码中 `filter_adv(..., chunk_size=512)` 是分批计算已有候选向量的批大小，并非摄取文档的 chunker，见下节代码。

## 四、数据、指标、结果与局限

- 表 II（第 6 页）：NQ 知识库 2,681,468 条、测试集 3,452、影子集 690；HotpotQA 知识库 5,233,329 条、测试集 7,405、影子集 1,481。由总数减影子数得到评估 2,762 / 5,924；这是算术推导，与代码常量吻合，实际每组有效评测分母仍以运行日志为准。
- 表 III 各领域行相加得到 NQ **688**、HotpotQA **1,476**，与同页表 II 的 690、1,481 分别差 2 和 5；已对原页图像复核，原因待查。两者不能同时作为一致的实际分母。
- 文中式 1 的预算使用 `n·p`，但第 6 页文字写 `p = 0.5`，而第 2、13–14 页又将投毒率写作 **0.5%**。若将后者用作比例 `0.005`，表 II 给出的预算约为 13,407.34 / 26,166.645 条，具体取整和有效注入数量不明；不能把这作为代码已运行的真实投毒量。图 3 的 `p` 轴为 0.1–0.9，单位与此也需作者/配置确认。
- ASR-r 是至少检索一条投毒样本的查询比例；ASR-t 是目标网址出现在生成输出的比例，第 6 页。主报告分别测检索和生成；网址命中不等于错误事实命中，也不等于成功欺骗用户。
- 主表 IV/V，第 7 页，均为作者报告、非本次复现。例如 NQ / Contriever / GPT-4o-mini：top-5 ASR-r 37.65%、ASR-t 31.88%；top-10 为 47.07%、31.92%；top-20 为 56.88%、31.12%。检索率提高而目标输出率不必提高。HotpotQA / Contriever / GPT-4o-mini top-5 分别为 97.57%、96.41%，不能泛化成全部数据集、检索器或投毒预算的成功率。
- 对照是为推荐同一网址而**改造的** Prompt Injection、PoisonedRAG、Corpus Poisoning；Corpus Poisoning 额外获得部分知识库访问，第 6、13–14 页。结果比较的是这些改造及各自权限条件，不能直接归因于原论文方法的原始完整设置。
- 消融表 VI（第 8 页）在 NQ / Contriever / top-5 中，完整方案 37.65% / 31.88%；移除高频词为 34.29% / 26.29%；移除对抗后缀为 0% / 0%。这支持该表配置下后缀的重要性，不证明前缀或后缀能跨未知分块保持完整。
- 迁移表 VII（第 9 页）报告的是 NQ、**ASR-r@50**，不是端到端 ASR-t。Contriever 代理迁到 OpenAI ada-002 / 3-small / 3-large 分别为 4.13% / 3.15% / 5.36%；不能说这些黑盒检索器的目标回答攻击率就是这些数字。
- 防御表 VIII（第 10–11 页）分别考察查询改写 PD、完全一致去重 DTF、BGE 重排后取 top-3 的 RF。NQ / Contriever 原 ASR-t 31.88%，PD 33.19%，RF 25.14%；精确哈希去重的表值不变。RF 列的 ASR-r 与原始检索值完全相同，未能确认它是否在重排后重新统计，因此不能用它推导毒样本在 top-3 的保留率。三项为各自测试，表中没有联合部署后的实证值。
- 附录第 14 页写 PD **仅用于 NQ 评估查询**，但表 VIII 同时列出了 HotpotQA 的 PD 值；如何得到这些值待核。表 IV/V 的一些相同检索器 ASR-r 数值又随后端 LLM 行变化，例如 NQ / SimCSE / Corpus Poisoning top-5 为 7.32% 与 6.32%，需随机种子、投毒集与计算日志解释，不预设为排版错误。
- 第 9–10 页 DeepSeek 案例展示模型输出的推理文本及最终回答，说明在该示例中指令被叙述为有用建议；它不能单独证明模型内部真实因果机制或推理能力越强就越不安全。作者本人也将高难数据、跨检索器迁移及从问答扩展到其他应用列为限制（第 11 页）。

## 五、与本开题 A / B 的关系

开题依据：[section3_content.tex](../../../../partitions/section3_content.tex) 第 15–31、43、308–337 行及相关上下文；这是当前方案，不代表已有实验结果。

| 对照 | 开题方案 | 本文 | 判断 |
|---|---|---|---|
| A：资产 | 已知 `q` 和正确答案，只能改一篇源文档，再经受害者侧分块得到同源角色块；目标是指定且与真值互斥的答案。 | 可加入多篇投毒文档；推理时未知目标查询；目标是在回答中加入网址。 | 两者都优化检索和生成，但权限、攻击目标与评估单元不同；本研究不能声称首先研究了 query-agnostic 或多文档检索投毒。 |
| A：构造 | 两个互补核心载荷须在单块/双块及 matched unrelated context 等对照下验证组合效果，且考虑未知分块器的载荷保留和共同召回。 | 一个投毒文档内拼接指令、频词和对抗后缀；优化平均查询相似度，指标为至少一条毒文档入选。 | 本文没有证明互补子载荷缺一不可，也没有测同源两个角色块的联合召回；不要把多条候选或后缀拼接误称为 A 的跨块协同。 |
| A：检索器知识 | 目标系统黑盒，离线使用影子检索器和影子分块器。 | 主实验目标 retriever 白盒，另外测试从白盒代理向不同 retriever 的 ASR-r@50 迁移。 | 可作为检索优化和迁移基线/威胁模型对照，但迁移结果不能直接当作开题的未知分块端到端结果。 |
| B：实体与边 | 对检索候选抽取实体和带极性、时间/条件的 OpenIE 命题边，结合来源、桥接和冲突信号，升级复核并考虑异源参照。 | 无图抽取、边构造或图投毒，攻击样本可含明确网址指令和不规则后缀。 | 应将其作为单块 URL 推荐注入及检索操控的外部测试；这些文本可能生成稀疏或不可靠的命题边，但是否漏检必须实测，不能仅凭结构推断。单块统计/语义分支及 LLM 复核可能识别，也不得预设一定成功。 |
| B：评估 | 比较安全性、正常问答效用、误删及开销，结构关系仅是送审信号。 | PD、精确去重和重排是单独防御；未评估 B 的分类、图检查、异源证据或完整净化策略。 | 不能引用本论文证明 B 有效或失效。若纳入后续实验，应同预算记录入库粒度、单块检出、送审原因、最终 URL ASR、正常引用误删及运行成本。 |

具体实验建议属于本次分析而非论文已完成结果：同时保留“原论文多文档/同分布影子查询”设置与“单源文档 + 受害者实际分块”的新设置，分开报告有效预算和不可行样本；对 `C_inject` 及 `C_adv` 分别测被切断、丢失及召回情况；对 B 记录 OpenIE 可抽取率、边正确性、结构分支是否触发以及单块分支是否已告警，并以正常网址推荐/引用为干净对照。

## 六、公开代码核对（静态审查，未运行）

- 第 1 页脚注与摘要明确指向 [AndyShaw01/PoisonCraft](https://github.com/AndyShaw01/PoisonCraft)。公开 `main` 的 [Atom 历史](https://github.com/AndyShaw01/PoisonCraft/commits/main.atom)所见最新提交为 `879246eef12490ef8e541a7b9b592871e83be546`，时间 2025-05-10 08:39:16 UTC；以下链接固定该提交，不等于已在本机复现。GitHub API 返回 403/限流，使用公开 Atom 与原始文件核验。
- [README](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/README.md) 列数据准备、词频、毒文本优化、检索/目标评估脚本及 MIT 代码许可。尚未验证模型权重、依赖及全部论文图表的生成过程。
- [target_attack.py 第 214–237 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/experiments/target_attack.py#L214-L237)实际对 `attack_info[:1000]` 计算向量；[retrieval_attack.py 第 126–145 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/experiments/retrieval_attack.py#L126-L145)同样处理 `all_list[:1000]`。这与按表 II 和 0.5% 推算的千以上预算存在待解释差异；代码是否与论文表格运行版本完全一致未知，不能断言论文实际实验只使用 1,000 条。
- [target_attack.py 第 21–38、162–194 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/experiments/target_attack.py#L162-L194)先与预存干净检索结果比较再合并候选，未召回毒文本的查询记 0 并跳过 LLM；其中 `chunk_size` 是向量批处理。`top_k+1` 与默认 `top_k=4` 的关系应在复现时核对，不能把变量名直接等同论文 top-k。
- [src/utils.py 第 78–96 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/src/utils.py#L78-L96)的 `MatchPredictor` 对目标域名做不区分大小写的正则文本匹配；它不核验回答的事实正确性，也不验证用户是否点击。[同文件第 198–226 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/src/utils.py#L198-L226)从各领域、各长度的结果文件装载候选。
- [prepare_datasets.py 第 54–83 行](https://github.com/AndyShaw01/PoisonCraft/blob/879246eef12490ef8e541a7b9b592871e83be546/experiments/prepare_datasets.py#L54-L83)调用 `random.shuffle` 后按 2:8 划分；该脚本中未见固定随机种子，NQ 分支复制完整 queries 文件，而另一些分支按 qrels 选择。不同已生成数据文件和实验运行路径可能影响实际分母，须以原始划分文件与日志核对。
- 本次仅读取公开代码，不下载模型、运行攻击或声称完成复现。原始文件 UTF-8 响应 SHA-256：`target_attack.py` = `4931e0ef3f0c19e22e7e258f2cc165b6a7cc2d75cad7e1f99b9737feb10837d4`；`src/utils.py` = `c2631e9076323f3c8c6168b28706970ceb1ab018e2110d107132d6879c013521`。

## 七、逐页索引

| 页 | 核对内容 |
|---:|---|
| 1 | 七作者、题名、v1 日期、摘要、作者公开代码脚注。 |
| 2 | 图 1、影子查询、三段投毒文本及攻击声称。 |
| 3 | 表 I、目标网址、攻击预算、知识与权限。 |
| 4 | 威胁模型余项、算法 1、投毒文本结构与指令前缀。 |
| 5 | GCG 目标与频词、按主题分配预算、数据集划分开始。 |
| 6 | 表 II/III、数据分母、检索器、LLM、改造基线、参数与指标。 |
| 7 | 表 IV/V 主结果、top-k 与检索和生成差异。 |
| 8 | 表 VI 消融、图 2 领域差异、图 3 参数敏感性。 |
| 9 | 表 VII 跨检索器 ASR-r@50、敏感性与具体案例。 |
| 10 | 案例续、PD/DTF/RF 设置及结果解释。 |
| 11 | 表 VIII/IX、各防御结果、结论与作者列出的局限。 |
| 12 | 参考文献、伦理声明及附录开始。 |
| 13 | RAG 提示、实验环境、14 领域分类、基线改造。 |
| 14 | PoisonedRAG / Corpus Poisoning 改造与 PD 实现说明。 |

## 八、最后查询的引用数与待核事实

- 2026-11-15 13:35 左右（Asia/Shanghai）最后查询 [DataCite 预印本 DOI](https://api.datacite.org/dois/10.48550/arxiv.2505.06579)：其 `citationCount` 为 **0**；这是该数据库该字段的覆盖结果，不能说论文在所有来源中零引用。
- 同时用预印本 DOI 和会议 DOI 分别查询 [OpenAlex](https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2505.06579)，均返回同一 work `W4417513116`，主 DOI 为会议 DOI、作者为五人，`locations` 同时含两 DOI，`cited_by_count` 为 **14**，记录 `updated_date` 为 2026-11-14T11:04:58.165337。**这是数据库合并记录的计数，不能当作七作者预印本独立引用数，也不能据此单独认定正式版关系。** Semantic Scholar API 对 arXiv 精确查询返回 HTTP 429，无法复核；上述数字均会变化。
- 待核：作者确认的七作者预印本与五作者同题会议论文的关系；若确需正式出版身份，应检查出版全文及作者说明。还需核对表 III 分母、`p` 的百分数与小数写法、表 VIII / 附录 PD 的数据集冲突、重排后 ASR-r 口径、代码前 1,000 条限制与论文运行版本/实际预算、随机划分文件、答案质量指标，以及未知 chunker 和 B 图抽取/防御的实测结果。