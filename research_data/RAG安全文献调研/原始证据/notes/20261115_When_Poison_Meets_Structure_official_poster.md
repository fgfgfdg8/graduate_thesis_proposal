# When Poison Meets Structure：NeurIPS官方海报核读

## 身份与证据范围

Qizhi Chen、Junhao Wen、Shuang Liang、Jiakai Li、Yizhuo Ma、Rongzheng Wang、Ke Qin；[NeurIPS 2026官方Poster #152350](https://neurips.cc/virtual/2026/poster/152350)。会场具体submission track尚未核实，不能仅凭poster标记给论文赋主会CCF等级。

2026-11-15核读[官方海报原图](https://neurips.cc/media/PosterPDFs/NeurIPS%202026/152350.png)，PNG为5120×2880像素，SHA-256 `0e85e95e7e5614d1011314b3ea2b35ca88f6bae2b8b459dfc568289f1ba0bcee`；这是海报哈希，不是论文PDF哈希。[OpenReview论坛](https://openreview.net/forum?id=TirVWlIdjG)当次提示登录，[PDF端点](https://openreview.net/pdf?id=TirVWlIdjG)匿名访问返回403；没有取得论文全文或可核自有代码。以下仅为海报图表和文字，**不能计入论文正文精读，论文阅读等级仍为L1摘要加海报**。

## 方法与开题的交叉

海报以有限投毒预算下的经验/策略假设为动机：攻击者倾向于伪造与查询直接相关的事实，较少补造背景，使污染子图呈稀疏星形，而正常子图有更多交叉支撑。这不是对所有攻击和干净子图的普遍证明，也不排除攻击者主动补造关联支持。

海报Method图显示：LGA-DPO先分离冲突证据；Topology-Responsive Prompting（TRP）重新检索候选证据的邻域，使用冻结GNN和可学习特征提示，对两个候选子图的拓扑可信度排序，随后移除被判污染的证据；作者宣称预训练一次后可迁移。训练数据、损失、阈值、攻击权限和在线成本均无法由海报充分核实。

这与开题B中从Top-K文本块构建实体—命题关系图、审查跨块桥接及命题冲突后复核的目标有直接重叠，不宜再宽泛宣称“首次使用结构或关系净化RAG检索证据”。目前可见区别是TDP对GraphRAG的冲突候选子图重检索邻域并排序；开题设计还提出记录源文档标识与块偏移、识别同源远距/低频桥接和特定命题冲突，并结合异源参照复核。海报不足以确定全文是否涉及同源分块、来源独立性、最终误删控制或相同消融；不同文档也不必然对应相互独立的信息源。

## 海报结果与限制

海报“Main results under GRAG-Poison”表将数值标为GraphRAG结果，均值、单位为百分比：

| 数据集 | TDP攻击成功率ASR↓ | ACC↑ | DASR↑ | ACCexpect↑ |
|---|---:|---:|---:|---:|
| 2WikiMultiHopQA | 27.0 | 65.5 | 60.4 | 88.3 |
| MuSiQue | 30.5 | 42.4 | 59.2 | 74.8 |
| PubMedQA | 29.4 | 45.5 | 68.6 | 70.3 |

海报另给HippoRAG迁移ASR/ACC：2Wiki 27.2/54.4、MuSiQue 24.0/49.8、PubMedQA 21.3/63.0。海报脚注将DASR解释为针对成功攻击的防御率，ACCexpect为干净答案保留；样本量、分母、训练/测试划分及不确定性均未在海报中充分披露。ACCexpect不能直接等同独立干净query集上的最终误删率，海报也不能验证延迟和广泛泛化声明。

已有[HoG-GRAG证据记录](<../../../../docs/RAG安全证据地图_20261102.md#src-fa5309b8c3b158d1>)讨论逐跳不一致检查及选择性子图修复；其是否被TDP全文比较未知。[KEPo记录](<../../../../docs/RAG安全证据地图_20261102.md#src-20261111-kepo>)包含连接攻击子图的策略，适合作为对稀疏结构假设的候选压力测试；这只是实验建议，不能据此声称KEPo已经绕过TDP。

取得全文后优先核查冲突候选形成、预训练与提示学习、适应性攻击、干净稀疏图与桥接证据误删、分母和端到端延迟。

[返回证据地图](<../../../../docs/RAG安全证据地图_20261102.md#src-20261108-when-poison-structure>) · [元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md#src-fe1fdb661d031149-h4>)
