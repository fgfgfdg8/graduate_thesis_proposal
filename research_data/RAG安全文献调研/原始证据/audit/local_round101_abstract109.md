# 科学101：Findings ACL2024八篇PDF首页完整摘要

本发布来源登记8项L1研究/报告/阅读事件，关联8个不同SHA官方PDF。PDF全文取得不等于全文已读；本轮范围仅第1物理页的完整Abstract及身份。正文、实验、附录、实现和别版均不继承阅读信用；0claims/effects，不构成L3或实验复现。

阅读日2026-11-05（Asia/Shanghai）；原始获取UTC及阅读记录UTC逐项保留。Findings不继承ACL主会CCF；Scholar/引用数均未核null。原T109零信用准备封包独立保留。

## R101-Muffin

**论文题名：** Muffin: Mitigating Unhelpfulness in Emotional Support Conversations with Multifaceted AI Feedback

- 作者（官方XML顺序）：Jiashuo Wang / Chunpu Xu / Chak Tou Leong / Wenjie Li / Jing Li
- 版本：正式Findings ACL2024；567-585；DOI 10.18653/v1/2024.findings-acl.31
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共19物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Muffin_ Mitigating Unhelpfulness in Emotional Support Conversations with Multifaceted AI Feedback.pdf>)
- PDF SHA256：`aa469d8ec87687c6ab91e18e4444d848fa444c435f9612e08d8205d870787e0b`

**摘要机制：** 情绪支持对话的多面AI反馈先评估帮助性，再用对比学习降低无帮助回复的似然；摘要称改善流畅性与相关性。

**A边界：** 所读摘要未显示检索投毒、单源未知切块或互补恶意块；情绪支持失败不等于A。

**B边界：** 多面反馈与对比学习用于生成模型训练；摘要未建立冻结编码器几何检测、正常query误删校准或检索块删除路径。

**后续：** L1非直接A/B；保留训练型反馈背景，不据摘要作全文排除。

**训练与调用预算：** 明确使用对比学习；反馈模块调用数、训练与在线成本未在摘要量化。

**摘要数字：** []

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-MORE

**论文题名：** MORE: Multi-mOdal REtrieval Augmented Generative Commonsense Reasoning

- 作者（官方XML顺序）：Wanqing Cui / Keping Bi / Jiafeng Guo / Xueqi Cheng
- 版本：正式Findings ACL2024；1178-1192；DOI 10.18653/v1/2024.findings-acl.69
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共15物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/MORE_ Multi-mOdal REtrieval Augmented Generative Commonsense Reasoning.pdf>)
- PDF SHA256：`30904c691e8b850933ac264d039a5924f6566846f8f934c7461741fadbf59a15`

**摘要机制：** 用文本及图像检索补充预训练语言模型的常识，并在Common-Gen任务比较单模态与多模态预训练模型。

**A边界：** 正常多模态检索互补，不等于恶意单源经未知chunker形成必要协作块。

**B边界：** 可作为保留正常互补证据的误删效用对照；摘要未给正常query级误删、几何统计或最终OR校准。

**后续：** B正常互补证据/误删效用对照；需正文核检索与生成机制及预算。

**训练与调用预算：** 摘要未明确冻结范围、训练需求、检索轮数与每query生成/核验调用数。

**摘要数字：** []

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-HyperCL

**论文题名：** HyperCL: A Contrastive Learning Framework for Hyper-Relational Knowledge Graph Embedding with Hierarchical Ontology

- 作者（官方XML顺序）：Yuhuan Lu / Weijian Yu / Xin Jing / Dingqi Yang
- 版本：正式Findings ACL2024；2918-2929；DOI 10.18653/v1/2024.findings-acl.171
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共12物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/HyperCL_ A Contrastive Learning Framework for Hyper-Relational Knowledge Graph Embedding with Hierarchical Ontology.pdf>)
- PDF SHA256：`c97ca928ad048cb546a673754e5b8c8b9da148bb1d3e04ef2c5b8dd0781d27d9`

**摘要机制：** 针对超关系知识图谱嵌入，使用关系感知GAT捕捉层次ontology，并用概念感知对比损失缓解facts对ontology的主导。

**A边界：** 超关系事实/本体层次不等于单源未知分块投毒；摘要未显示A攻击约束。

**B边界：** 训练型KG链接预测框架，非摘要已建立的冻结检索块几何核验或query级误删控制；未示完整B。

**后续：** L1知识图谱表示背景；不据摘要判全文无撞车。

**训练与调用预算：** 明确GAT与对比损失训练；模型冻结、在线检索/LLM调用预算不明。

**摘要数字：** [{"literal": "three real-world datasets; average improvement of 3.1-7.4%", "boundary": "作者摘要报告的链接预测改进；具体指标、分母、相对/百分点和独立重复未核，非RAG投毒检测收益。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-SP3

**论文题名：** SP3: Enhancing Structured Pruning via PCA Projection

- 作者（官方XML顺序）：Yuxuan Hu / Jing Zhang / Zhe Zhao / Chen Zhao / Xiaodong Chen / Cuiping Li / Hong Chen
- 版本：正式Findings ACL2024；3150-3170；DOI 10.18653/v1/2024.findings-acl.187
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共21物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/SP3_ Enhancing Structured Pruning via PCA Projection.pdf>)
- PDF SHA256：`c3d8878a7fc4fde29613e9e7bbd147515ac470e0cb4838808ff62b493ea350f3`

**摘要机制：** 结构剪枝先将特征投影到主成分空间再掩码，以压缩PLM隐藏维度；摘要报告BERT、OPT和Llama压缩实验。

**A边界：** 摘要目标为模型压缩，未显示检索攻击或跨块必要性。

**B边界：** PCA投影改变模型/隐藏维度并用于剪枝；不能等同冻结编码器的几何异常检测或正常query误删校准。

**后续：** 谱/PCA组件邻近但任务与干预对象不同；完整B撞车未决。

**训练与调用预算：** 结构剪枝/投影涉及模型改变；训练和推理成本、是否可免训练不能由摘要确定。

**摘要数字：** [{"literal": "reduce d by 70%; compress 94% of BERTbase; maintain over 96% accuracy; outperform ... by 6%", "boundary": "全部为作者摘要的压缩/准确性报告；96%及6%的基线、绝对/相对口径与分母未由正文核定，不转为效应表或误删率。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-GeNE

**论文题名：** Context Length Extension via Generalized Extrapolation Scale

- 作者（官方XML顺序）：Linhan Li / Zhang Huaping
- 版本：正式Findings ACL2024；4211-4218；DOI 10.18653/v1/2024.findings-acl.249
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共8物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Context Length Extension via Generalized Extrapolation Scale.pdf>)
- PDF SHA256：`fff90bf3f6ee52e6c82e6b78ee152c81624b403d76764e17d21d3ad68a7e9bef`

**摘要机制：** GeNE在位置嵌入插值函数中随机缩放外推比例，通过finetuning实现训练短、测试长的上下文扩展。

**A边界：** 长上下文外推不等于未知chunker，也不直接证明单源投毒的实际共召回或块必要性。

**B边界：** 摘要明确finetuning；不等于冻结模型/编码器的几何检测，未给query级正常误删控制。

**后续：** 上下文长度与训练成本边界参考；需正文核位置映射、任务和预算。

**训练与调用预算：** 明确finetuning中随机缩放外推比例；在线调用与完整训练成本未知。

**摘要数字：** [{"literal": "64k contexts by training on 16k length", "boundary": "作者摘要报告的上下文长度；不是检索块大小、未知切块鲁棒性或投毒成功率。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

**元数据变体：** [{"position": 2, "xml": "Zhang Huaping", "pdf": "Huaping Zhang", "status": "same-author display-order discrepancy retained; no silent rewrite"}]

## R101-Translatotron-V(ison)

**论文题名：** Translatotron-V(ison): An End-to-End Model for In-Image Machine Translation

- 作者（官方XML顺序）：Zhibin Lan / Liqiang Niu / Fandong Meng / Jie Zhou / Min Zhang / Jinsong Su
- 版本：正式Findings ACL2024；5472-5485；DOI 10.18653/v1/2024.findings-acl.325
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共14物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Translatotron-V(ison)_ An End-to-End Model for In-Image Machine Translation.pdf>)
- PDF SHA256：`4149fb56e8183ec904060644a17f3d9fe2663d5a8d904f397d68022acf47044c`

**摘要机制：** 图中文字到图中文字的端到端翻译，包含图像编码/解码、目标文本解码器和图像tokenizer；两阶段训练及Structure-BLEU位置感知评估。

**A边界：** 视觉翻译/对齐不是RAG注入检测；摘要未示单源未知切块攻击。

**B边界：** 图像翻译质量评估不等于RAG块删除/证据支持检测或正常误删控制。

**后续：** L1视觉翻译任务背景；不授RAG防御或完整B信用。

**训练与调用预算：** 明确两阶段训练与多模块模型；参数比例不等于实际LLM调用/延迟预算。

**摘要数字：** [{"literal": "only 70.9% of parameters", "boundary": "相对级联模型的参数量报告；具体比较对象、质量/速度完整数值未核，非防御有效率。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-GeoHard

**论文题名：** GeoHard: Towards Measuring Class-wise Hardness through Modelling Class Semantics

- 作者（官方XML顺序）：Fengyu Cai / Xinran Zhao / Hongming Zhang / Iryna Gurevych / Heinz Koeppl
- 版本：正式Findings ACL2024；5571-5597；DOI 10.18653/v1/2024.findings-acl.332
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共27物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/GeoHard_ Towards Measuring Class-wise Hardness through Modelling Class Semantics.pdf>)
- PDF SHA256：`3a1a4adb999980e2b7ed8bc07eed7a026731834e2251007629ca928c726099e0`

**摘要机制：** 定义类级难度并研究跨学习范式、模型和人工判断的一致性，以语义embedding空间类几何度量难度，区别于实例级指标。

**A边界：** 类语义难度不是源/块攻击角色或每块共同必要；摘要未建立A。

**B边界：** 类级embedding几何是B组件近邻；需正文核距离/协方差/类内外统计和训练依赖，不能直接等于冻结四统计20维RF、独立正常TopK-max及最终OR误删控制。

**后续：** 优先正文：B几何组件近邻，完整撞车/无撞车均未决。

**训练与调用预算：** 摘要没有足够训练/编码器冻结与调用数细节；理论与实证主张均需正文核对。

**摘要数字：** [{"literal": "eight NLU datasets; over 59 percent on Pearson’s correlation", "boundary": "摘要的类级难度相关性改进；未核相对/百分点、指标分母或跨任务聚合，不转为59百分点、不当query误删改善。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。

## R101-Mind Your Format

**论文题名：** Mind Your Format: Towards Consistent Evaluation of In-Context Learning Improvements

- 作者（官方XML顺序）：Anton Voronov / Lena Wolf / Max Ryabinin
- 版本：正式Findings ACL2024；6287-6310；DOI 10.18653/v1/2024.findings-acl.375
- 实际阅读：L1，仅PDF p1完整Abstract；PDF共24物理页不等阅读页数。
- PDF：[论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Mind Your Format_ Towards Consistent Evaluation of In-Context Learning Improvements.pdf>)
- PDF SHA256：`221b869103baf8efb2d5dc65be5a3534a78bf474fd14860a028e16fdd0234c45`

**摘要机制：** 系统研究ICL模板敏感性及跨模型/设置不迁移，提出测试时Template Ensembles聚合多个模板预测以缓解格式选择影响。

**A边界：** 模板敏感性非未知切块投毒；摘要未建立单源跨块攻击。

**B边界：** 可作为B校准分布漂移与多模板调用预算参考；不是摘要已证明的正常TopK-max/OR误删控制。需正文核格式采样、随机性和重复调用。

**后续：** 优先正文：校准漂移与测试时集成预算参考；不凭摘要确立完整B撞车。

**训练与调用预算：** 测试时聚合多个模板预测；实际模板数、模型调用/批次/延迟及预算约束待正文。

**摘要数字：** [{"literal": "21 models (770M to 70B parameters) and 4 classification datasets", "boundary": "作者摘要报告的评测范围；随机guess、模板迁移与集成改善没有本轮正文数值验证，不能据模型数推LLM调用预算。"}]

数字为作者摘要报告；本次不作正文数值认证、效应合并或完整撞车/无撞车裁决。
