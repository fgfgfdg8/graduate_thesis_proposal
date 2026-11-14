# Approximate Nearest Neighbor Search Over Temporal Vector Data

## 身份、版本与阅读范围

- **作者**：Yuxiang Wang、Ziyuan He、Yongxin Tong、Zimu Zhou、Zijie Ma、Yiman Zhong。
- **正式出版信息**：IEEE Transactions on Knowledge and Data Engineering，2026，38(11):7291–7303；[DOI 10.1109/TKDE.2026.3722749](https://doi.org/10.1109/TKDE.2026.3722749)；[IEEE Xplore记录](https://ieeexplore.ieee.org/document/11647349/)，文献编号11647349。IEEE记录的发表日期为2026-08-10，期次为2026年11月；[CSDL期次](https://www.computer.org/csdl/journal/tk/2026/11)及[Crossref出版者登记](https://api.crossref.org/works/10.1109/TKDE.2026.3722749)与作者、期次、页码相符。
- **CCF**：期刊A类；[第七版推荐目录](<../../../../../../../../Downloads/第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）.pdf#page=32>)物理p32的“数据库/数据挖掘/内容检索”期刊表列有TKDE。
- **实际读取版本**：作者主页直接提供的[14个物理页PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Approximate Nearest Neighbor Search Over Temporal Vector Data.pdf>)，SHA-256 `b2a69a1c271c43e7be3b49915a8d396b4eb7f131bc560183329a99c437e5a613`；[作者出版物页](https://zhouzimu.github.io/publication.html)将此PDF链接到本题名和DOI。正式期刊登记页码7291–7303共13页，未逐页核对正式出版版与作者PDF是否一致，不能把作者稿14页当成出版版页数。
- **实际阅读**：作者PDF p1–11正文与方法、实验、结论逐页阅读；p11–12参考文献扫描；p13–14全部附录文字阅读。L3仅授上述作者PDF；图中曲线的精确数据未数字化，方法和证明未独立复现。
- **引用数**：Google Scholar当前引用数未核；留待统一核验，不以空值或零值代替。

## 研究问题与机制

论文研究带时间有效性的近似最近邻检索，并以RAG的时效性作为应用动机。每个向量有开始、结束时刻；**TANNS**要求候选在查询时间点有效，**IANNS**要求候选有效区间与查询区间相交。论文假设离散时间、每个时间戳恰有一个向量生效或失效；ANN召回率以当期有效向量上的精确kNN为参照（p1–3）。

Timestamp Graph复用相邻时间点的索引，仅更新变化向量的局部邻居并保存历史邻接表；为应对点过期造成的图连通性下降，它另外维护备用邻居。Historic Neighbor Tree压缩历史邻接表；面向区间查询时预计算大子树代表邻居，避免随区间长度反复扫描（p4–8，Algorithms 3–7）。作者给出的空间量级从时间戳图的 `O(M²N)` 降到压缩图的 `O(MN)`，区间查询量级写为 `O(M log²N)`，其中N是向量数、M是每点邻居数（p2、p7–8、p13–14）。这些是论文设定下的索引复杂度，附录对检索访问节点、重建邻居规模等使用了既有近似检索假设和实验观察；不能据此声称对任意对抗语料存在最坏情况下的安全保证。

## 实验、结果和限制

- **实验对象与预算**：SIFT、GIST、GloVe各100万向量并附合成时间模式；TWiki约150万文本向量、MIND约23.1万新闻向量使用真实时间信息。查询返回k=10；默认M=16、候选邻居数200、树叶参数8（p8–9）。
- **比较与指标**：预过滤、HNSW后过滤、ACORN、SeRF、DIGRA及iRangeGraph；以QPS–recall权衡、索引更新吞吐和内存比较，不评估恶意文本识别、ASR或正常查询误删（p9–10）。
- **作者报告**：在95% recall固定点，TANNS的QPS相对比较方法提升4.4–138.1倍；部分IANNS设置下时间戳图较最佳基线提升3.4–27.6倍。作者另报告其方法在所测数据和工作负载可达到99%以上recall；不可把95% recall处的速度倍数当作99% recall处的结果（p9–10）。
- **规模与内存**：DEEP扩展实验在200万至1000万向量上展开；作者报告1000万向量时，M=16压缩图以约46.7 GB内存处理，时间戳图在99% recall时约857 QPS（p14）。不同索引、参数和数据上的两个数不应拼接为同一配置的端到端结果。
- **边界**：没有构造投毒者、攻击预算、恶意来源、语义欺骗、检索后过滤或生成器问答实验；时间戳本身的真伪和攻击者是否可操纵时间信息未被作为安全问题检验。时间相交只能表示输入元数据满足时效条件，不验证内容真实或来源可信。

## 对开题A/B的关系

对A，它是共享时间范围、真实索引与多块被召回条件的基础设施参照；不研究同源恶意文本经未知chunker分割、多个必要前提或协同投毒。对B，它提示建立过期事实和正常多时态证据的效用对照：对时间不相交的块做筛选与识别恶意块是不同决策。不能把有效期筛选、相似性或邻接结构当作内容真实性、恶意性或clean-query误删率保证，也不能据此推导开题方案已有直接安全方法撞车。

## 资源与参考文献线索

- [团队TimestampGraph仓库](https://github.com/BUAA-BDA/TimestampGraph)在2026-11-14核到master的HEAD为`0e8b0aeb334cde61a81688f194cf64b7d230dd84`。仓库包含相关C++实现，但README未明确绑定本篇2026年期刊题名或DOI；完整代码、数据和版本对应关系未证实，未执行或复现。
- 论文参考文献中的TemporalWiki、Temporal Blind Spots、SeRF、ACORN及iRangeGraph用于时效知识或向量检索背景，未见直接等价的RAG知识库投毒/检测先例（p11–12）；是否属于本项目其他已登记研究需按题名和DOI另行去重。
