# When Does Graph Retrieval Become Answer-Supporting Evidence?：官方海报与公开结果核验

## 身份与阅读范围

Chenghua Duan、Zhuo Wang、Boheng Liu、Ziyu Li、Qing Li、Xiuxing Li、Zhong Zhang、Xia Wu；[NeurIPS 2026 Poster #139414](https://neurips.cc/virtual/2026/poster/139414)。官方海报左上角标注 **Evaluations & Datasets**；NeurIPS会议在所给第七版CCF目录中为A类，但不据此推断该轨道每篇论文的CCF-A认定，论文级评级仍待核实。

已阅读官方摘要及[官方海报](https://neurips.cc/media/PosterPDFs/NeurIPS%202026/139414.png)，并静态核对海报展示结果与作者仓库固定提交的说明和CSV。海报PNG SHA-256：`bf79ba1646057b67d516b92643c3711efc51ebf1a224e0c18a731d0cb1903c3e`。OpenReview PDF端点当次返回403，未取得论文PDF；因此阅读状态仍为**L1摘要＋海报＋公开结果文件核验**，不能算论文正文精读或推断正文未展示的实验细节。

[作者仓库固定提交](https://github.com/Wonderdch/When-Does-Graph-Retrieval-Become-Answer-Supporting-Evidence/tree/db637d51170c838f16fef9c3615ef4dc1baaa23d)由官方页面的Project Page链接；项目自有代码和文档声明MIT，使用和再分发其他软件、数据及权重须另查仓库说明。本次没有运行作者代码、模型或完整复现实验。

## 问题、方法和适用边界

作者沿候选证据可用、选择、生成上下文、答案及评价五个阶段审计证据到答案的转化，并提示在每阶段核对来源、token预算和成本。海报结果覆盖GraphRAG-Benchmark的Medical与Novel共400个问题；仓库[复现说明](https://github.com/Wonderdch/When-Does-Graph-Retrieval-Become-Answer-Supporting-Evidence/blob/db637d51170c838f16fef9c3615ef4dc1baaa23d/docs/reproducibility.md)称该样本按2个领域×4种问题类型×50题分层，7个逻辑方法标签对应5条独立检索流水线。仓库还说明其评价器经过本地兼容补丁，faithfulness提示和解析器发生变化；这些结果应限定于所用生成器、评价器和数据，不能表述成跨系统结论。

海报建议同时报告检索、证据支持、答案和成本，并通过gold证据、上下文位置等干预区分证据选择、组织和生成使用的失败。它是开题B评估**过滤后正常证据能否支持最终回答**的近邻；海报未提出恶意块检测、来源真实性判定或对正常query最终OR删块概率的校准，不能当成上述任务的同义工作。

## 可复核的分母与数值

以下为作者结果，非本地模型复现。固定提交的[主结果表](https://github.com/Wonderdch/When-Does-Graph-Retrieval-Become-Answer-Supporting-Evidence/blob/db637d51170c838f16fef9c3615ef4dc1baaa23d/results/paper_results/main_table_400q.csv)、[配对bootstrap表](https://github.com/Wonderdch/When-Does-Graph-Retrieval-Become-Answer-Supporting-Evidence/blob/db637d51170c838f16fef9c3615ef4dc1baaa23d/results/paper_results/bootstrap_main_claims.csv)和[逐题数值](https://github.com/Wonderdch/When-Does-Graph-Retrieval-Become-Answer-Supporting-Evidence/blob/db637d51170c838f16fef9c3615ef4dc1baaa23d/results/reproduction_inputs/per_query_metrics_400q_scores.csv)之间可直接对账。逐题CSV共2,800行，其下载字节SHA-256为`56741fca85ef324118d3e78467b09dd108f5065581b10e4ceda64313137a6f7c`；本次自行读取逐题文件，按同一问题ID取两方法均非空的数值，计算均值与配对差，未重新运行bootstrap。

| 对照及指标 | 海报/仓库配对结果 | 有效配对数及核验 |
|---|---|---|
| Dense-rerank相对BasicRAG：evidence recall | +0.0357 | 400；配对bootstrap 95%区间约[+0.0069, +0.0650]。 |
| 同一对照：answer correctness | +0.0001 | 400；实际均差约+0.0000748，95%区间约[-0.000426, +0.000569]。跨零不等于证明两法完全等效。 |
| 同一对照：coverage | 海报+0.0250；README +0.0251 | 200；逐题配对均差+0.02504679，按常规四位小数为+0.0250；README高一末位的原因未核实。 |
| LightRAG相对BasicRAG：context relevancy | 海报-0.1663；README -0.1662 | 400；逐题配对均差-0.16625，末位与取舍方式有关，具体生成流程未核。 |
| LightRAG相对BasicRAG：faithfulness | 海报配对差-0.2297；README -0.2355 | 仓库bootstrap表和逐题内连接均为99个有效配对，均差-0.2297118；主表BasicRAG均值使用100个非空值，LightRAG均值使用99个非空值，两者均值直接相减为-0.2355306。数值差异对应配对与非配对分母，不能混用。 |

仓库复现说明称全部7×400结果中evidence recall、context relevancy和answer correctness各有2,800个非空值；ROUGE与coverage各1,400个，faithfulness共699个。上述指标分母不同，“400题”不是每个指标都用了400对样本。海报还报告gold-only相对最优检索上下文的answer correctness +0.0047、ROUGE +0.2939、coverage +0.1799、faithfulness +0.2662；在未取得正文和完整干预算子定义前，将其作为海报展示的诊断结果，不外推为部署效果。

## 后续核验

若合法公开全文可取得，下载到指定论文库并按完整题名命名，再核查生成器和评价器、干预分母、特征与数据划分、显著性及效用/成本；确认全文后才可调整正文阅读等级。引用数统一留待Google Scholar集中核验，未知不记为零。

[证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-20261108-graph-evidence-support>) · [元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md#src-20261108-graph-evidence-support>)
