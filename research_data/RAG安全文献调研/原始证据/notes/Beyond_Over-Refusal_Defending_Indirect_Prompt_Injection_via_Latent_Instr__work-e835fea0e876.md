---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-e835fea0e876
report_id: work-e835fea0e876--0e9895258e2e
reading_level: L3
checked_date: 2026-11-18
---
# Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

**AEGIS利用生成器隐藏状态的指令敏感方向和多层投票检测间接提示注入，是开题B的表示检测、经验分位和多信号融合近邻。** 正式PDF表1的FPR为0.0290，即2.9%；正文0.29%和摘要低于1%的表述与表格存在冲突，暂不选择其中一个作为统一结果。

## 正式身份与实际阅读

- 作者及顺序：Jiahao Chen、Rui Yin、Xinfeng Li、Qianli Ma、Tianyu Du、Zhihui Fu、Jun Wang、Zhaoxiang Wang、Shouling Ji；正式PDF与ACL导出书目相同。
- 机构：浙江大学、香港理工大学、中国科学技术大学、OPPO Research Institute；按正式PDF首页编号对应。
- 发表：Findings of the Association for Computational Linguistics: EMNLP 2026，pp.3995–4001，2026年10月；DOI `10.18653/2026.findings-emnlp.188`。Findings为独立track，不继承EMNLP主会CCF-B；第七版CCF目录未对该track单列评级。
- 实际阅读：正式7页PDF的正文p1–5、p6的Limitations/Ethical Considerations/LLM Usage均已读；p6–7参考文献浏览，未逐篇跟读；本PDF无独立附录。p3公式和p4表1另已目视核对。阅读等级L3，不代表代码结果复现。
- 核验日期：2026-11-18。同一study由既有L1摘要升级，新增独立研究数为0；不把正式版、作者稿和本次阅读重复计为不同研究。

## 威胁模型、方法与代价

p2 §3.1的攻击者只能在外部数据段中注入恶意指令，不能访问权重、系统提示或用户query；防御者能读取生成器内部隐藏状态并知道外部数据边界。研究对象是IPI检测，没有实验覆盖一份真实长源经未知chunker形成同源双块并共同必要的攻击链。

p2–3 §3.2–3.3把隐藏表示建模为知识成分与指令成分之和。用带类别标签的数据估计指令/知识均值和指令协方差，经Ledoit–Wolf收缩后得到方向 `w ∝ Σ_I^(-1)(μ_I−μ_K)`；投影强调指令类方差较小、两类均值分离的方向。这里的协方差来自指令/恶意类；开题B的尾谱马氏统计以干净query–chunk分布为参照，统计对象和矩阵不同。

随后用良性投影分位设置单层边界，并在多个层上做hard或soft aggregation。p4默认估计使用200良性+200恶意样本，Qwen3-4B投3层、Llama模型投7层，从网络50%深度开始；默认soft voting，作者称结果为5个随机种子平均。其“training-free”指免梯度更新生成器，仍要带标签拟合检测方向和阈值。正文没有给出独立拟合/校准/测试的全部逐实例隔离证明。

p5报告约120 ms附加延迟；Figure3标AEGIS约0.52 GB。正文没有列出足以在相同硬件、输入长度和检索块数下复算该点的完整测量设置。它读取生成器隐藏状态，不能与B仅运行独立编码器的特征开销直接相减，也没有提供正常多跳关键证据保留或最终回答效用的完整实验。

## 定量结果与冲突

| 原文位置 | 已读结果 | 解释范围 |
|---|---|---|
| p3–4 §4.1、Table1 | OpenPromptInjection，7个任务，各100 instruction–data对；8种攻击、10项基线；默认Qwen3-4B，另测Llama3/3.1-8B | 各任务、攻击或seed不能不经去重合并为独立query总数。报告的ACC是检测分类准确率。 |
| p4 Table1 | AEGIS八行ACC 0.9847–0.9855，FPR均0.0290（NeuralExec排版为0.029），FNR 0–0.0021 | FPR为2.9%。Combined行 `(1−0.0290+1−0.0014)/2=0.9848` 与平衡分类ACC吻合；这只是算术核对。 |
| p1 Abstract、p4 §4.2 | 摘要写FPR <1%，正文写0.29%，而表1为2.9% | 存在10倍单位/数值冲突；代码README也复述0.29%，不是独立证据。未经作者澄清不改表值、不宣传统一低于1%。 |
| p5 Figure6及正文 | 三模型ACC >97%、FPR <5% | 与“所有模型低于1%”不同；图中未打印各点原始值，未从曲线造精确数字。 |
| p5 Figure7及正文 | 作者称约100 calibration samples已趋于稳定，图轴为40–400样本 | 数据量指检测拟合/校准预算，不能理解为无样本检测或对分布漂移的保证。 |

## 统计主张与公式边界

p3 Eq4把 `b` 写为良性投影上分位数的负值，随后hard rule却写原始投影 `s>b_l`；两者把截距与原始分数阈值混用。下面固定代码的实现是 `score = projection − quantile`、`score>0`，可解释一种一致阈值用法，但不能据此悄悄修订印刷公式。

p3 Eq6的Hoeffding界针对hard votes，并假设非相邻层近似独立；p6 Limitations承认它可能是过于乐观的上界。普通层间“近似独立”没有给出依赖误差项；默认soft voting也不自动受hard-vote推导覆盖。良性经验分位及其拟合集上的误报占比，尚不足以得到新query上分布无关的有限样本保证，尤其当方向和分位共享良性拟合样本时。此处应区分需要何种独立性/交换性、有限样本分位修正和最终告警单位。

同页的鲁棒半径是直接隐藏状态扰动、单位投影下的margin论证；文本编辑到多层隐藏状态扰动的对应、各层扰动范数及其共享约束没有完整说明。该半径不能直接变成对未知chunker、词级投毒或最终RAG删块动作的认证。

## 公开代码与实现对应

正式PDF p1的Github超链接指向作者仓库；本次核验固定commit `f0ab67fd374cf88e4f6e0a788c6bdb62345242e2`，公开可读。已静态读取README、pyproject、`steer.py`中核心类、训练与多层评估相关路径，并核对打包JSON规模；未执行模型推理或重现实验。

| 对应路径与行号（固定commit） | 实际实现或资源 | 对论文主张的影响 |
|---|---|---|
| `inststeer/utils/steer.py:154–215` | `CalibratedAsymmetricLDA`用恶意类LedoitWolf precision拟合方向，取相同拟合良性集的经验分位作负截距，`projection+intercept>0`判恶意 | 有标签拟合、经验分位先例；不等独立clean-query校准或生成器无需访问。 |
| 同文件272–346 | 多层类重复拟合检测器；hard为严格多数，soft为各层带截距分数的算术平均再与默认0比较 | soft路径没有实现论文p3逐层标准化 `(s−μ_b)/σ_b`；实现差异未通过运行解释。 |
| `train.py:123–125`、`steer.py:427–465` | 单层训练入口用`AsymmetricLDA`的两类均值中点截距；多层评估入口另用校准类 | 单层训练入口与多层校准入口不能当作同一阈值算法。 |
| `eval_multilayer_voting.py:746–757` | 参数默认起始深度2/3、5层、per-layer FPR0.05；用户可改参数 | 默认命令与论文50%深度、3/7层不同；复现须明确配置。 |
| 打包数据和README | 校准演示100条（50+50），测试演示40条（20+20），1个clean/malicious配对；README明确演示不等论文结果；完整论文模型权重/hidden states未附 | 可作实现参考；不能称完整基准包或已复现论文。 |
| 仓库49个ZIP条目与README许可段 | 未发现LICENSE/COPYING，README称license将补；含实际核心代码 | 公开可读与明确开源许可分列。 |

固定commit ZIP SHA-256：`ba941fbc934879919fc41c444aa0cb02aa42d28696be7f59e5237b26f080093c`；`steer.py` SHA-256：`4889e2a530a0de3dff1645aef2b01f561380cf277923725135ffd883ae9b472e`。ZIP仅在内存检查，未另留临时副本。

## 与开题的关系

**B的直接组件近邻：** 已有低方差指令方向、冻结生成器隐藏表示、经验良性分位和多层共识检测；这些机制各自不能作为B的宽泛创新。B的差异需落在独立query–chunk编码接口、四统计与监督RF的实际增益、物理来源/实体/条件关系对正常多跳保留的贡献，以及最终query级动作校准。应在相同访问权限、攻击集合、输入长度、误报和调用预算下比较；AEGIS的分类ACC、2.9%表格FPR或隐藏半径均不等于最终query误删率。

**A的攻击面参考：** 它检测恶意指令，不验证事实/规则的适用性或同源互补事实的共同必要性。当前已读实验没有直接占据A的单真实源—未知分块—同源双块共同必要这一完整交集；该结论限定于已读正式7页和所核代码路径。

进一步区分两种解释需要新增证据：①0.0290与0.29%可能是排版或记录错误，应取作者更正/逐seed混淆矩阵；②聚合收益可能依赖共享校准数据或层间相关，应取得独立校准/测试划分、相关性统计及同一最终动作的误报，而不是由“层多”推出无条件保证。

## 来源与文件

- [正式页面](https://aclanthology.org/2026.findings-emnlp.188/)；[正式BibTeX](https://aclanthology.org/2026.findings-emnlp.188.bib)；[正式PDF](https://aclanthology.org/2026.findings-emnlp.188.pdf)。三者题名、作者、页码已核。
- [作者代码固定commit](https://github.com/xaddwell/AEGIS/tree/f0ab67fd374cf88e4f6e0a788c6bdb62345242e2)。README关联arXiv `2608.22248`；该作者稿正文未另读，不据此重复授予L3。
- [本地PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/Beyond Over-Refusal_ Defending Indirect Prompt Injection via Latent Instruction Manifolds.pdf>)；7物理页、842098字节；SHA-256 `bdb65828e9e86f429d272965a5a85e5e0ccbcd0bfdc3af3e68cd5237688b211a`。
- [证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-7c01fe422b49e736>)；[元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md>)；[技术总结](<../../../../docs/RAG安全文献攻防技术手段总结报告.md>)。

Google Scholar引用数保持未核；按任务次序留待内容与制品核查完成后统一处理。代码完整性能复现、作者数值澄清、共享样本与独立校准边界仍未完成。
