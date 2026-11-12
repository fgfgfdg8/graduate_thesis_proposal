---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-9b0b01b9275a
reading_level: L3
checked_date: 2026-11-13
---
# Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention

**阅读状态：L3。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录或正式版。

- **作者**：Jongbin Won；Sung Geun An；Jay-Yoon Lee（正式PDF署名；Anthology HTML另显示“SungGeun AN”）
- **机构**：Graduate School of Data Science, Seoul National University（正式PDF作者栏）
- **年份 / 会议 / track**：2026 / Findings of EMNLP，pp. 50655–50674 / Findings
- **发表状态**：ACL Anthology正式记录与PDF已核；DOI 10.18653/2026.findings-emnlp.2356。arXiv:2609.35794v1为同题名、同作者顺序的预印本版本，归属同一study，不重复计研究。
- **CCF**：Findings未单独评级，不继承EMNLP主会等级。
- **引用量**：见[元数据汇总](../../RAG安全文献补查元数据_20261102.md)。
- **代码 / 制品**：[公开GitHub项目页](https://github.com/Jongbin-kr/sieve-and-sage-demo)是React静态论文演示，不运行模型或推理；其源文件引用的研究代码仓库[当前返回404](https://github.com/Jongbin-kr/Sieve-and-Sage)，未核实到可用研究代码或其许可证。
- **关联标题**：["Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention"]

## 一句话总结与核心贡献

集合级轻量前筛+LLM直接近邻；微调/整集合弃答、效用负例、恢复预算与最终风险边界需联立。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 受控混合和候选排名不等真实单源未知切块/实际共召回/每实际块必要。

**B：** 两阶段架构直接相关；微调整集合弃答非冻结四统计20维RF，单SieveFPR非最终query OR删除保证。

## 局限、可比性与不确定性

指定正式报告主文L3，限主文p1–10、附录A–H p12–16与J p19–20；p17–18构造模板不授完整审读。受控检索集合与噪声不代表自然检索或A联合条件；单Sieve集合FPR与子集恢复不授最终query OR删块风险或统一预算保证。Table15 NQ-wiki .638与计数复算.673仍未对账；Table10部分对偶展示不合一，保留原值而不归因实现。作者实现/模型未访问或运行；不同版本不继承。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### R97-SieveAndSage-official-L3-20261105

- **书目来源**：[原始页面](https://aclanthology.org/2026.findings-emnlp.2356/)
- **DOI / arXiv**：[10.18653/2026.findings-emnlp.2356](https://doi.org/10.18653/2026.findings-emnlp.2356) / [2609.35794v1](https://arxiv.org/abs/2609.35794)
- **本地PDF**：[打开PDF](../pdf/Sieve_and_Sage__Efficient_Distraction_Filtering___81352aba5b2e.pdf)
- **原始PDF链接**：[公开PDF](https://aclanthology.org/2026.findings-emnlp.2356.pdf)
- **实际阅读**：L3仅对应ACL Anthology正式版20页PDF：主文p1–10至Limitations/Acknowledgments全部；Appendix A–H p12–16与J p19–20正文/表格已读；p19 Table14正常QA接口已核。p10–12参考仅部分，I中p17–18构造模板未完整逐行审读，不整理构造步骤。实际目视p1/5/19/20；p8/9/15/16已渲染未授目视信用。arXiv v1仅核身份，未另行阅读；作者实现/模型未运行。

#### 方法、结果与适用条件

**论文题名：** Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention

- 官方Findings EMNLP2026，pp50655–50674，20物理页；Findings不继承主会CCF等级。PDF作者Jongbin Won / Sung Geun An / Jay-Yoon Lee*，首尔国立大学Graduate School of Data Science，星号明确通讯作者。当前HTML第二作者SungGeun AN与PDF来源变体并列，不静默覆盖。
- 官方HTML DOI为`10.18653/2026.findings-emnlp.2356`，正式版页码50655–50674；主文PDF SHA `81352aba5b2e1563e7ae5eba38dc50f7b9a05204c64def0bccad9f3d1f28ccf4`。arXiv v1题名与三位作者顺序匹配，视为同一研究的另一报告；阅读信用仍只计正式版。
- 制品核查（2026-11-13）：公开的`sieve-and-sage-demo`是静态交互页面，明确不运行后端/GPU模型，输入只触发预置演示。其`src/data.ts`指向`Jongbin-kr/Sieve-and-Sage`及研究提交`7c03d99aa8cfb3d97bf62888462e349e21b80adf`，但目标仓库当前返回404；实际研究代码、模型固定版本及许可证未能独立核实。
- 2026-11-05实际完整阅读主文p1–10与A–H p12–16、J p19–20。参考仅部分，I的p17–18未完整逐行审读；p19正常QA接口已核。实际目视p1/5/19/20。仅论文阅读，未访问/运行实现、模型或当天Scholar。

##### 与开题A/B的关系

**B的“轻量前筛＋昂贵LLM”宽泛架构已有直接先例。** p4–5 Sieve输入query及整个检索文档集合，先二分类有无干扰；命中则整集合立即弃答并跳过Sage，未命中再由Sage生成或因缺证弃答。默认Longformer和Sage均经任务微调；小量专家域监督与分布适配仍必要。它不是冻结完整ModernBERT的单块恰好四统计/20维RF，也没有独立正常query TopK-max校准、最终G/R/F OR删块风险保证。不能用主干名不同排除架构撞车，也不能把本工作说成已复现B全部联合条件。

输入单位和决策事件尤须分开：set-level distracted分类与最终query弃答，不是单文档标签或逐块删文档；Sage缺证判断进一步影响最终行为，单Sieve FPR不自动代表完整链。p9可选恢复会对不同留一子集重复Sieve，再将清理集合交给Sage；文章没有在本轮可核范围给出所有删块合并规则、恢复后正常证据保留风险及统一最坏调用上界。主流程省调用不代表恢复流程固定一次，也不能与B“一次批LLM”自动等同。

A的真实单长源、未知chunker、角色分离、实际共同召回及每实际块共同必要没有在同一实验联立。原文给定检索集合并构造/混合干扰；附录reranker排名检验的是候选可见性和语义接近，不是端到端自然检索共召回或块必要性。多文档混合不能直接证明或排除A的联合假设。

##### 标签、训练与真实正常多跳（p4/6/13–16）

标签使用答案词与NLI对参考句的关系，是离线数据构造/评估条件，不推断线上模型可获得真值。answerable状态定义为至少一篇可支持答案且无干扰，unanswerable为全部无支持；干扰状态含至少一篇支持和一篇干扰。该taxonomy没有给正常互补多跳证据的all-required测试，不能将跨文档差异都作为恶意。

Table1列5一般域、3专家域；各数据来源/构造程度不同，表中星号表示沿用前作。两模块不同监督对象、验证选模型，专家域Sieve仍需监督。训练标签、微调代价与在线前筛耗时分开；t-SNE可视化、少样本跨域趋势不证明全新域免训练或特征因果性。AppendixC称至少两随机种子、主文报告均值；没有逐格方差/CI，不由同一query多个状态或模型格增加独立研究数。

##### 实测收益与重要负例（p8/15–16/19–20）

Table15 NQ-google：DTA-chatQA vs Sieve-and-Sage系统Acc .230→.796，latency756.341→379.574ms；约1.993倍来自这个比较，不是对vanilla。vanilla仅74.204ms，因而Sieve并非最快；摘要69.4百分点来自.796−.102，Macro-F1 55.2百分点来自.731−.179，均需写比较对象。

MedQA系统Acc .297→.682、MacroF1 .367→.766（对DTA-chatQA），同时answerable coverage .914→.862，selective accuracy .509→.460。全状态incorrect responses319→140、correct abstentions108→289；前者是计数，不是独立正常query误删率。正文把coverage/selective下降换取更少错误，效用代价不能省略。

反例：NQ-wiki主设置Sage-only系统Acc .792高于Sieve-and-Sage .638，MacroF1 .730高于.632；RAG-Bench亦.397高于.368。BioASQ本文方法正确答案0、selectiveAcc0，虽MacroF1 .552高于对照，也不支持普遍更好回答质量。Table16 DPR/NQ-wiki Sage-only .812/.779优于本文.641/.641；Table17 Gemma/NQ-wiki .843/.747优于.600/.608。跨主干/检索器“稳健”须保留这些格，不能写每项胜出。

Table7由K5改K3或7两数据均退化，训练K固定解释可迁移限制；不是所有K的参数无关保证。Table10 AstroQA单Sieve默认阈值binary MacroF1 .947、FPR .037，描述的是冲突/非冲突集合分类；不是最终G/R/F OR删除事件的query FPR或独立校准保证。中间阈值的TPR/FNR等展示对偶未完全相加为1，保留原表，不自行修正。

##### 成本、恢复和指标可复算边界

Table8作者报告Sieve149M/0.56GB/15.01TFLOPs，对Sage8B/15.91GB/217.52TFLOPs。这是组件资源口径，不能直接用54倍参数差当端到端加速。单NVIDIA Pro6000 96GB环境、未用vLLM/量化，换部署不自动继承时延；主文“最多1.99x”不是Table16/17全部模型对比的全局最大值。

Table2仅在Sieve已检出的113 NQ-google、71 RealtimeQA子集报告恢复accuracy：无恢复.247/.380、筛文档.867/.943、agent.716/.774。不能推广成全体query最终收益，agent的模型/总调用和恢复总耗时未完整核定。动态补检索是建议路径，不计本轮已有端到端实验。

Table15 NQ-wiki本文方法(592正确答+1627正确弃答)/3297=.673，与系统Acc .638不直接重合；表注称系统Acc为ternary而response counts覆盖全状态，是否由弃答类型、运行平均或其他统计口径造成尚未建立。这里只保留复算不一致的待核问题，不宣称实现错误。K变化、neutral加入、可视化和多seed不是独立研究/完整风险校准证据。

##### 待核

主要噪声是受控构造，作者Limitations明确自然噪声、动态知识与zero-shot外部有效性待核。没有本次可验证的A五项联合控制或B完整风险预算。可访问制品限于静态演示；研究代码链接当前404，模型/数据发布条件与许可证未能独立核实，不把演示当可复现实验实现。References未逐条追踪，arXiv版本未单独精读，Scholar观察待按原始记录核验。

### 2026.findings-emnlp.2356-official-cached-abstract

- **书目来源**：[原始页面](https://aclanthology.org/2026.findings-emnlp.2356/)
- **DOI / arXiv**：未核实 / 未提取 / 未核实 / 未提取
- **本地PDF**：该摘要报告未关联PDF；已读全文见本笔记其他报告。
- **原始PDF链接**：[公开PDF](https://aclanthology.org/2026.findings-emnlp.2356.pdf)
- **实际阅读**：L1；Official cached complete abstract; catalog_emnlp_sources/articles.jsonl line 11340; no PDF, methods, experiments, or appendix read in this route.

#### 方法、结果与适用条件

### N460｜2026.findings-emnlp.2356｜Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention

**相关性：** 优先全文：轻量集合前筛加LLM直接工程近邻。

全部作者（官方缓存）：Jongbin Won; SungGeun AN; Jay-Yoon Lee。

身份：2026；Findings of EMNLP；track=findings；CCF=null（Findings不继承主会）；publication_status=official_catalogue_cache_entry; not_revalidated_online_in_this_route；DOI=null；arXiv=null。

作者摘要声称：Sieve and Sage区分缺所需证据的不可回答与混有冲突/否定/对抗信息的干扰状态，由轻量Sieve先筛文档集合，再调用Sage生成或弃答，测一般和专家域准确及成本。

A审读判断：集合内混合证据相邻，摘要未证明恶意同源未知分块或双块共同必要。

B审读判断：轻量前筛加昂贵LLM、误证与缺证区分非常接近B分层架构；特征、来源关系、保正常多跳和最大分位校准仍须全文，不能凭架构直接判完全撞车。

关键原文（该官方缓存摘要源合计不超过25英文词）：“screens retrieved document sets for distracting evidence before invoking a costly LLM”

原文实际范围：articles.jsonl第11340行完整摘要；正文、实验、附录未读；物理页=[]；本地PDF=null；PDF版号=null。官方证据：https://aclanthology.org/2026.findings-emnlp.2356/；远端PDF链接（非下载）：https://aclanthology.org/2026.findings-emnlp.2356.pdf。

## 待核事项与追溯

未读版本、章节、代码及样本依赖按上文所列范围保留待核。

[返回证据地图](../../RAG安全证据地图_20261102.md) · [全部逐篇笔记](../README.md)

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Sieve and Sage_ Efficient Distraction Filtering for Reliable RALM Abstention.pdf>)
<!-- PDF_LIBRARY_END -->
