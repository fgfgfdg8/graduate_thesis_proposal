---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-a020b4dd2358
reading_level: L3
checked_date: 2026-11-12
---
# Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence

**阅读状态：L3。** 正式版正文及附录共12页已逐页阅读；参考文献未逐条核验。

- **作者**：["Ruihua Zhou", "Hao Huang", "Yijie Zheng", "JiaTang Luo", "Yunpeng Li", "Yuling Liu", "Dan Du"]
- **机构**：中国科学院信息工程研究所；中国科学院大学网络空间安全学院；中国科学院大学交叉科学学院；中国科学院计算技术研究所
- **年份 / 会议 / track**：2026 / EMNLP Main / pp. 11682-11693
- **发表状态**：ACL Anthology正式条目；DOI `10.18653/2026.emnlp-main.509`
- **CCF**：EMNLP主会按第七版目录为CCF-B。
- **引用量**：尚未核查，见[元数据汇总](../../RAG安全文献补查元数据_20261102.md)。
- **代码**：[作者公开仓库](https://github.com/zrh233/Evidence-Laundering)；未独立运行。
- **本地PDF**：[正式版PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Evidence Laundering_ Deep Research Agents Mistake Correlated Sources for Independent Evidence.pdf>)；12页；SHA-256 `63e4060458e39fbe40b6f715defeff110617a775ce3de2b0ec9d3158225c0442`
- **关联标题**：["Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence"]

## 一句话总结与核心贡献

论文把同一虚假主张跨同源页面改写、链接并包装成多来源佐证定义为evidence laundering，以匹配语料控制内容和检索暴露，检验深度研究agent是否区分页面重复与来源独立；另提出基于masked writing skeleton的检索后来源门控。

## 与开题逐项比较

**A：** 攻击同样利用多个页面对同一虚假主张形成表面佐证，但不是单一真实长源经未知chunker产生的互补块；未检验块级拆分、各块单独不足及联合必要性。

**B：** 直接来源依赖/来源独立性近邻。应将来源分组和重复证据折扣纳入基线与威胁模型；本篇不识别恶意RAG块、不判断事实真伪，也不控制clean-query上的最终OR误删率。

## 方法与结果

- **威胁模型与设计**（pp. 11683-11685）：攻击者可控制普通页面正文、表面媒体/作者/日期/标题及页面链接，不能控制agent或检索器；测试时没有真实作者身份、真实来源血缘或真值标签。确定性matched corpus含100个虚构实体主张，A为单条虚假页面，C为k=5同源改写页，F为表面独立来源对照，E为真实事实控制；同一命题池、干扰项和检索暴露保持匹配。按无检索先验剔除高置信项目，主模型gpt-5.4保留90条。
- **主攻击结果**（pp. 11685-11687）：gpt-5.4对A/C/F的false-publish率为0.71/0.83/0.82，C-A增加0.12（n=90）；C-A置信对数优势增加0.81，DDI=1.00，95% bootstrap区间[0.75,1.22]；C-F差值+0.08，落入预设±0.15 TOST等效界。8种模型设置的C-A置信增量均为正，DDI范围0.71-1.01。k从1增至3时增量至+0.78，k=3/5/7/10估计在+0.78至+0.81间，未随页数稳定上升。
- **检索暴露与反证**（pp. 11686-11687）：普通top-5下C/F的5个集群页面均进入候选，agent平均打开约4.07/4.10页。加入5个独立正确页面后，A/C/F false-publish为0/0.76/0.72，C-A置信差+1.28、DDI=0.68；改为top-12并要求打开8页时三条件false-publish均为0。结果依赖检索窗口内正反证据的实际曝光。
- **来源门控**（pp. 11688-11689）：BM25先取M=15候选，按fingerprint Jaccard连通分量去重并保留最高排名代表，输出K=5。词shingle在C/F/E保留有效来源数1.00/2.00/2.00，DDI=0.15；masked skeleton为1.03/4.94/5.00，DDI=-0.39。自然新闻元数据标签分类中，masked skeleton precision/recall为0.949/0.359，word shingle为0.900/0.350；低召回意味着仅能识别一部分同源对。
- **自适应改写**（p. 11689）：独立模型调用生成的85页中，masked skeleton对C/F平均保留4.41/4.88个来源，precision=0.867、recall=0.0765、false-merge=0.0118；17个有效集群中11个完全未被折叠。静态写作骨架信号对独立改写攻击明显脆弱。
- **限制**（pp. 11690, 11693）：主攻击是虚构实体和合成页面的本地sandbox；自然新闻部分只做基于媒体/作者/署名等元数据的来源分类，不是端到端agent实测，且无人工血缘标签。作者明确指出自适应改写会消除静态特征、counter-evidence结论依赖检索暴露。没有线上网页发布或检索操纵实验，不构成真实网络或RAG安全保证。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### 正式出版与阅读凭据

- **书目来源**：[原始页面](https://aclanthology.org/2026.emnlp-main.509/)
- **DOI / arXiv**：`10.18653/2026.emnlp-main.509` / 未发现arXiv版本
- **本地PDF**：[正式版PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Evidence Laundering_ Deep Research Agents Mistake Correlated Sources for Independent Evidence.pdf>)
- **原始PDF链接**：[公开PDF](https://aclanthology.org/2026.emnlp-main.509.pdf)
- **实际阅读**：L3；官方正式PDF逐页阅读，物理页1-12，印刷页11682-11693，含附录A；参考文献未逐条审计。
- **SHA-256**：`63e4060458e39fbe40b6f715defeff110617a775ce3de2b0ec9d3158225c0442`

## 待核事项与追溯

引用数与代码复现未核；论文页眉没有区分单篇long/short类别。参考文献未逐条审计；跨研究样本重叠未知，不数值合并。

[返回证据地图](../../RAG安全证据地图_20261102.md) · [全部逐篇笔记](../README.md)
