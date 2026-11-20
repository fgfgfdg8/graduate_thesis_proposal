---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-31cb317e5ccd
reading_level: L3
checked_date: 2026-11-07
link_audited: 2026-11-16
---
# ShieldRAG: Safeguarding Retrieval-Augmented Generation from Untrusted Knowledge Bases

**结论：方向 B 的直接近邻。** 论文训练兼顾相关性与内容安全的检索器，并评价投毒下的检索和生成；“加入 RAG 安全筛选”“同时考虑安全与效用”或“考虑未知不安全内容”本身不能作为独占创新。论文的实证对象和指标与开题 A 的同源互补块共同必要性、B 的干净 query 误删校准仍不相同，不能因此把这些问题视为已被完整覆盖。

## 身份、来源与阅读边界

- **作者顺序**：Peiru Yang、Haoran Zheng、Yi Luo、Xinyi Liu、Jinrui Wang、Huili Wang、Xintian Li、Yongfeng Huang、Tao Qi。
- **正式出处**：AAAI 2026，AAAI Technical Track on Natural Language Processing V，*Proceedings of the AAAI Conference on Artificial Intelligence*，40(40): 34286–34294。DOI：`10.1609/aaai.v40i40.40725`，正式页面所列发布日期为 2026-03-14。作者、卷期和页码与 [Crossref 登记](https://api.crossref.org/works/10.1609/aaai.v40i40.40725)一致；分轨见 [AAAI 论文页](https://ojs.aaai.org/index.php/AAAI/article/view/40725)。
- **CCF**：A 类；用户提供的第七版目录物理第 57 页将 AAAI 列为人工智能会议 A 类。[CCF 官方目录 PDF](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F)与该本地目录文件在 2026-11-16 的 SHA-256 对比中逐字节一致。
- **实际阅读版本**：AAAI 正式会议 PDF，582,316 字节，9 个物理页；SHA-256 `8e241987a841090a47f9cc592266e7d6c7025e776ccfc1452638fd921a10cdfc`。[论文库 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/ShieldRAG_ Safeguarding Retrieval-Augmented Generation from Untrusted Knowledge Bases.pdf>)位于本仓库之外；该相对路径仅在保留现有目录关系时可用，单独克隆仓库不会获得 PDF。
- **L3 的准确范围**：既有记录记载 2026-11-07 完整阅读正文物理 p1–7，目视核对 p4–7 的公式、表 1–3 及图 3–6；p8–9 致谢和参考文献仅浏览，未逐条认证引文。2026-11-16 仅就来源、哈希以及 p2、p4–7 的相关公式、指标和表图作定点复核，没有扩大阅读范围。独立补充材料及作者稿版本匹配情况未知。
- **在线来源状态**：2026-11-16 普通请求访问 AAAI 论文页和[官方 PDF 地址](https://ojs.aaai.org/index.php/AAAI/article/download/40725/44686)时，虽然返回 HTTP 200，但内容是机器人验证 HTML，未据此声称在线 PDF 可直接下载，也不将其判为失效。页面的正式书目信息以可核索引及 Crossref 登记交叉核对。
- **代码与引用量**：PDF 物理 p2 印有 [ypr17/ShieldRAG](https://github.com/ypr17/ShieldRAG)，该公开仓库页面于 2026-11-16 可访问；本次只核对链接和页面身份，未审查实现、运行或复现实验，论文与具体提交的对应关系未知。Google Scholar 引用数未核，保持未知。
- **消歧**：本文不同于 TOIS 论文 *Push and Pull: Defending against Retrieval Poisoning Attacks via Embedding Space Reshaping*（DOI `10.1145/3800948`）中同名方法；不合并作者、模型、实验或引用。

## 方法与威胁对象

论文针对不可信知识源中的有害内容和检索语料投毒：被检索内容可能使回答复述有害信息、拒答或质量下降（p1–2）。有害内容、事实错误、恶意指令与攻击意图不是同一标签；无害讨论也可能引用有害内容，不能仅凭毒性代替全部安全终点。

方法用有限标注和合成对抗数据学习安全评分，让安全判断与相关性共用可训练的检索表征，并用初始化检索器的候选排名分布作 KL 参照（p3–4）。论文使用 Contriever 作为检索骨干，使用 BeaverTails 标注数据，并在离线数据准备中使用本地与商业 LLM（p5）。这些训练资源和权限应计入比较。

具体而言，p4 式 (2) 的相关性分数 `uθ(q,d)` 使用 query 与文档表示，安全头 `sθ(d)` 只以文档表示为输入。因此联合排名依赖 query，不等于安全头能够基于 query 判断证据角色。排名 KL 约束也不等于逐个保留正常支持块，更不直接给出 query 级误删或生成安全保证。

## 正式 PDF 中的符号与文字疑点

以下均限定于已核对的正式 PDF 物理 p4（印刷页 34289），不代替实现核验：

1. 式 (6) 将 `E[y log sθ(d) + (1-y) log(1-sθ(d))]` 称为二元交叉熵，并写总目标 `L = Lrank + Lsafety`。若按通常的损失最小化约定理解，打印表达式缺少负号；正文没有给出足以闭合该疑点的另一套符号或优化约定。
2. 同页定义 `y=1` 为安全、`sθ(d)` 为安全概率，推断排名又写作 `S(q,d)=uθ(q,d)+λsθ(d)`；文字同时说超过毒性阈值的 `sθ(d)` 被丢弃，并将相应项称作减法惩罚。安全概率、毒性阈值、加号及惩罚方向在打印文本中未统一，`λ` 的符号也不足以消解全部歧义。
3. 前面的对抗共训使用毒性置信度，向后续安全概率的方向转换没有清晰展开。需在统一标签与分数方向后核对实现；上述疑点**不是**作者代码错误的证据。

## 实验终点、结果与限制

- **指标分母（p4–5）**：retrieval ASR 是 Top-k 至少出现一篇投毒文档的 query 占比；Recall@k 是至少命中一篇 ground-truth 文档的 query 占比，不是多跳完整支持集合召回。generation ASR 将有害输出与被注入内容触发的拒答合并；正常问题误拒与对有害请求的合理拒绝应分开。论文主文未充分展开评分 judge、细分错误及完整样本分母，不能由百分数反推这些口径。
- **表 1（p5）**：四个问答数据集在表列 Top-1/3/5 下的 ShieldRAG retrieval ASR 均为 0；三个 targeted 数据集的表列最高值为 3.21%。这是所列设置中的经验结果。对比无攻击 Vanilla，SQuAD Top-1 Recall 为 23.76 对 24.75，AdvBench 为 65.31 对 69.39，不能概括为所有召回均无损。
- **表 2（p6）**：caption 写六个数据集，表中实际有七行。SQuAD 和 HotpotQA 的 4o-mini 列中，ShieldRAG generation ASR 均为 1.98，TrustRAG 均为 0；所以不能把作者的整体优势概括为每个单元格严格胜出。AdvBench 的 Llama3 结果 2.08 与表 1 的 2.04 属于不同阶段，不自行合并或判为排版错误。
- **表 3（p6）**：generation accuracy 是四个数据集的平均值。无攻击与 ShieldRAG 分别为 Llama3 的 42.20 与 42.08、4o-mini 的 60.77 与 59.66；平均值接近不意味着每个 query 或正常证据块均无损。
- **效率与消融（p6–7）**：图 3 所列 ShieldRAG 检索阶段时间为 0.005 秒，但主文未给足硬件、batch、候选数、缓存/索引及离线训练成本，不得改称端到端 RAG 时延或零成本。图 4 是有限污染比例下的经验测试；图 5 侧重数据准备和共训变体。图 6 的 ASR@1 在 6k 标注量最低，Recall@1 在 8k 最高，不能声称标注越多始终越安全或无需标注。

这些指标、实验设置及有限证据不能推出对任意未知攻击、低 FPR 或完整支持集合保留的保证。表内未见可直接用于逐 query 风险校准的显著性或误差报告；训练/验证源隔离、阈值选择和完整超参数仍需进一步核对。

## 与开题 A/B 的逐项关系

| 开题要素 | 已有直接关联 | 尚不能从本文推出的结论 |
| --- | --- | --- |
| B：检索后安全与效用 | 论文联合相关性与安全性，使用训练后的安全头、重排和阈值过滤，并评价检索与生成。 | 宽泛的安全筛选或安全—效用权衡不是独占创新；须在相同攻击、候选预算和数据资源下比较具体机制。 |
| B：固定四统计与离线 RF | 双方都利用检索表征识别风险；本文训练共享编码器和安全头。 | 不能先验断定固定编码器更强、更新或更省全链成本；应分别比较统计增益、标注与离线训练成本。 |
| B：干净 query 与 OR 误删 | 本文 Recall@k 只要求至少命中一篇 gold 文档。 | 它没有给出开题所需的单块 FPR、干净 query 中至少一块被误删的概率、完整支持集合保留率或该最终 OR 决策的校准保证。 |
| B：未见攻击与域外 | 论文测试多数据集、两种投毒策略和有限污染比例。 | 未见普遍未知攻击保证；应独立检查训练/验证/测试源隔离、阈值选择、正常域外误删及未见攻击。 |
| A：单一真实源与共同必要性 | 实验包含投毒文档及 HotpotQA；retrieval ASR 关注至少一篇投毒文档进入 Top-k。 | 已读正文未展示单一真实源经未知受害分块器形成同源互补块、同 query 共同召回，并通过逐块及联合删除证明共同必要性的完整链条；这不排除其他未读材料或其他论文。 |

若将其作为 B 的候选基线，应先确认公开实现的论文对应版本、分数方向和阈值，再统一检索器与资源预算，分别报告单块误报、query 级误删、完整支持集合保留、最终回答/拒答及离线和在线成本。本笔记提出的是比较要求，不声称该基线已经复现。
