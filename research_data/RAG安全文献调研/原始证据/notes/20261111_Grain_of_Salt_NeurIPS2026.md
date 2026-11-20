# Can LLMs Take Retrieved Information with a Grain of Salt?

## 书目身份与版本

- 作者：Behzad Shayegh、Mohamed Osama Ahmed、Fred Tung、Leo Feng（RBC Borealis）。
- 录用身份：NeurIPS 2026论文。arXiv官方记录注明“Accepted by The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS 2026)”，NeurIPS 2026官方Downloads目录列出同题；按用户提供的第七版CCF目录，NeurIPS为CCF-A。未核独立会议DOI，`10.48550/arXiv.2605.06919`是arXiv-issued DOI。
- 版本：arXiv:2605.06919v2，2026-11-06修订；v1提交于2026-05-07。官方入口：[arXiv v2](https://arxiv.org/abs/2605.06919v2)、[NeurIPS 2026 Downloads](https://neurips.cc/Downloads/2026)。
- 本地PDF：[打开全文](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Can LLMs Take Retrieved Information with a Grain of Salt_.pdf>)；32页，1,342,597 bytes；SHA-256 `c9490503bb2965b7c6606e221976bf4d7bb38076b2835a5d218bc78a5edda172`。文件名中的问号按Windows规则替换为下划线。
- 代码/数据：论文正文与附录未见作者项目仓库或独立代码/数据制品链接；本次未核实到作者指定实现，不据此断言制品不存在。实验使用ClashEval与MIRAGE。

## 全文阅读范围

本地arXiv v2 PDF物理pp.1–32逐页阅读，含正文、参考文献、限制、Broader Impact及完整prompt表格，L3；未运行代码或复现。下述数值均为论文报告。

| 定位 | 阅读记录 |
|---|---|
| pp.1–3 | 问题定义及指标。给定上下文置信度`c`与上下文答案`a`，理想输出分布为`(1-c)π+cδ_a`；以该分布和模型实际输出分布的total variation distance对`c∈[0,1]`积分，定义context-certainty obedience error。单头近似只沿一个上下文答案展开token前缀分布，是较紧多头估计的下界；实际实验使用0/20/40/60/80/100%六档置信度。指标衡量对外部置信值的遵从，不是答案准确率。 |
| pp.4–5 | 方法和设置。八个开权重模型：Gemma 3 1B/4B/12B/27B、Llama 3.2 3B、Llama 3.3 70B、Qwen 3 4B、Qwen 2.5 72B；关闭reasoning模式。ClashEval五类共9,377条样本；主分析仅保留八个模型都能从上下文取出答案的1,280条。 |
| pp.6–10 | 主实验、消融与相关工作。方法由三部分组成：将模型自身context-free答案作为prior reminder；用模型级recalibration map校准输入置信值（需访问输出概率并在部署域拟合）；抽取并简化上下文以减少复杂度偏置。ClashEval平均误差由0.52降至0.39（约25%）；few-shot和rubric基线均约0.51。MIRAGE平均误差由0.52降至0.43，但从ClashEval拟合的recalibration映射不能良好迁移至MIRAGE。 |
| pp.11–13 | 全部参考文献。直接近邻包括ClashEval、参数知识与检索上下文冲突/信任方法、context-aware decoding、FaithfulRAG及检索可信度估计；已存在的ClashEval、BRIDGE和FaithfulRAG记录不重复重读。 |
| pp.14–22 | 统计检验、数据过滤影响、类别/上下文正确性分解、置信映射、自信度与单头/多头误差近似。MIRAGE含7,560条，主过滤后1,588条。作者还在未过滤数据上报告了相似方向结果，但主指标仍依赖受限样本和短答案任务。 |
| pp.23–32 | 局限、计算成本、Broader Impact及完整system/user prompts。作者指出置信值操纵可能被用于传播错误信息，建议监测并保留人工监督；同时讨论仅两数据集、短答案、logit访问、API模型和域迁移限制。 |

## 方法与证据边界

- `c`被当作可信、未失真的外部有效概率；上下文表达一个确定答案。论文不从文档内容估计来源真实性，也不设恶意检索文档、投毒者或对抗预算。
- Prior reminder和context simplification在ClashEval对部分模型改善不一；完整三组件平均收益显著，但小模型仍有较高残差。MIRAGE上从ClashEval迁移的校准映射失败，部署到新域需要重新拟合。
- 主分析筛掉模型取不出上下文答案的样本；作者另报未过滤结果，但其构念仍是短答案场景下的置信遵从，而非受污染RAG中的误检、漏检或误删控制。
- 论文在Broader Impact中承认certainty score manipulation风险，但未提出攻击检测或信号来源认证方案。
- PDF p.18 Appendix E.4称唯一评价指标`ε_obey`“uses signed averaging”；这与pp.2–3由total variation的绝对L1距离定义的指标表述存在口径张力，引用时应以正式公式和逐样本定义为准，并保留该文字不一致。

## 对开题的关系

- 分类为B方向的可靠性/交互设计方法参照，不是RAG安全攻击或安全检测器。
- 它限制“首次研究LLM如何按外部检索置信信号调整参数知识与上下文权重”这类宽泛表述；可作为信号校准、上下文复杂度干预及效用基线的参考。
- 与开题B的关键差异：论文假设外部置信度可用且诚实，不判断信号是否遭操纵、不检测恶意来源或事实投毒、不隔离检索块，也没有clean-query误删率、攻击检出率或来源真实性指标。不得把25%的obedience-error改善表述成安全攻击防御收益。
- ClashEval及BRIDGE等已存近邻应与本篇区分：本篇显式研究给定置信度的遵从和校准，不等同于自动推断上下文可靠度或来源治理。

## 优先级输入

- 类别=`method_reference / context-certainty calibration`；venue=`NeurIPS 2026`；按第七版目录CCF=`A`；v1日期=`2026-05-07`。
- Google Scholar引用数=`null`/`not_observed`（截至2026-11-11未查）；公开代码因子未确认；总优先级与全局排序未计算，待所有相关文献内容和制品核验完成后统一处理。
- 证据地图：[本篇条目](../../../../docs/RAG安全证据地图_20261102.md#src-20261111-neurips26-grain-of-salt)。
