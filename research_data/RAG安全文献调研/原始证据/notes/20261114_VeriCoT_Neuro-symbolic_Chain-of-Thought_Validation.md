# VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks

## 身份、版本与阅读范围

- **作者**：Yu Feng、Nathaniel Weir、Kaj Bostrom、Sam Bayless、Darion Cassel、Sapana Chaudhary、Benjamin Kiesl-Reiter、Huzefa Rangwala。
- **正式身份**：[ICLR 2026 Conference论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d7b3cef7c31b94a4a533db83d01a8882-Abstract-Conference.html)，[OpenReview接受决定为Poster](https://openreview.net/forum?id=zHuV3Vatov)，按第七版推荐目录为CCF-A；会议官方书目列出版日期2026-04-20及页码133170–133208。作者预印本为[arXiv:2511.04662](https://arxiv.org/abs/2511.04662)，`10.48550/arXiv.2511.04662`是预印本DOI；未确认独立会议版DOI。
- **实际阅读**：[本地论文PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/VeriCoT_ Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks.pdf>)共39个物理页，SHA-256 `13d257c1069267fbcd9f4e20c8e64e030702968c46fdd8929df9af25dde33d71`，首页标明ICLR 2026；正文p1–10已读，p11–14参考文献按相关主题扫描，p15–39附录逐页阅读。正文阅读等级L3；未复现代码、求解器或端到端实验。
- **制品与引用**：未核到可明确归属于该论文的公开代码或专用数据、权重；未找到不等于不存在。论文使用公开研究基准，但不能把第三方基准说成作者发布的专用制品。Google Scholar引用数及完整优先级待统一核验。

## 方法与证据来源

论文验证模型已生成的自然语言CoT，而不是先判断检索文档是否恶意。它对每一步扩充符号词表、转换为SMT-LIB公式，以Z3检查与先前公式的矛盾和蕴含；不足时由LLM从题目、上下文或常识中生成支持前提，并可让LLM-as-Judge分别判断来源归因与常识可接受性。不能翻译、相互矛盾、无法找到充分前提分别标为untranslatable、contradiction、ungrounded；格式转换和词表扩展最多尝试三轮（p3–5）。求解器的结论只相对于表达式和前提成立；前提是否真实、自然语言翻译是否忠实仍依赖外部判断。

## 数据与实验结果

- 论文采用ProofWriter、BioASQ Task 12b Phase B和LegalBench-SARA，测试集分别为400、340、367条；ProofWriter仅保留蕴含和矛盾标签，不含Unknown。SARA的367条由272个entailment与95个numeric实例构成（p6、15）。验证器采用Claude-3.5-Sonnet-V2，另以Qwen2.5-7B-Instruct研究微调（p5、8）。
- Table 1中，ProofWriter、BioASQ、SARA的通过率分别为45.2%、25.3%、15.2%；验证精度分别为94.1%、84.3%、87.0%；VCAR分别为42.5%、21.3%、13.2%。此处“精度”是**通过验证的样本中最终答案正确的比例**，VCAR是全部样本中既通过又答案正确的比例，均不是逐推理步骤正确率或恶意文档检测精度（p6–7）。
- Table 4中，使用LLM-as-Judge信号反思后，三项VCAR分别为54.8%、30.9%、19.7%；但ProofWriter和BioASQ的最终任务准确率分别从75.8%降到73.7%、从81.4%降到80.5%，不能概括为所有任务准确率均提高。Table 5中BioASQ在验证SFT后为79.7%，叠加DPO后为79.4%（p8）。
- 人工分析每数据集各抽20例，并在四类验证结果间均衡抽样；报告翻译准确比例为80%–87%，LLM-as-Judge与人工判断一致比例为95%–100%，60例中96.7%的CoT拆分保留原信息。比例对应的判断对象及小样本均衡抽样方式限制其外推，不能视作部署分布的误报或漏报率（p7–8）。
- 论文未报告可核实的每样本端到端耗时、API/token成本或吞吐量，并将减少LLM调用、降低延迟列为未来工作（p10）。

## 原文案例的限制与逻辑核查

- p4称由出生于2005年和`age(2023) ≤ 18`可判定“年龄至多15”矛盾；仅依据页面展示的不等式，`age=15`同时满足两式，故该文字示例的矛盾结论缺少必要前提。这是对印刷示例的逻辑核查，不等于已复现实现错误。
- BioASQ案例p17、25–33把“可非选择性通过不超过1000 Da的分子”转换为“若可通过则必不超过1000 Da”；后者比所示自然语言更强，案例的矛盾判断依赖该形式化。修订后所示条件式也未单独断言宏分子存在，故Pass本身不足以认证自然语言的宏分子事实。
- SARA案例p33–39把“可能存在管辖影响”标为untranslatable，反思后删除该句；同时把普遍适用的农业劳动覆盖表述作为常识前提。结论依赖前提的法律适用性；该失败仅表明当前表示及翻译流程未处理该句，不是说SMT原则上不能表达可能性。

## 对开题A/B的定位

- **A攻击**：本文没有受害者未知分块、单源互补载荷共同召回或恶意块投毒评估，不能作为这些攻击链的直接先例。
- **B防御**：逐步抽取前提、形式化、蕴含/矛盾检查和错误反馈是跨命题核验的直接方法参考；但自洽的伪前提仍可推出攻击者目标。论文没有建立多块来源可信、恶意块识别、最终生成约束、正常query误删率或延迟预算保证。
- VeriCoT正文将[Explanation-Refiner](https://aclanthology.org/2024.emnlp-main.172/)列为最相关工作；[FLARE](https://aclanthology.org/2025.emnlp-main.1193/)是相关多跳形式化路线。此处仅登记其可追查的正式来源，不以引用关系代替原文精读。
