# Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving

## 身份与阅读范围

- **作者与发表**：Xin Quan、Marco Valentino、Louise A. Dennis、André Freitas；[EMNLP 2024 Main](https://aclanthology.org/2024.emnlp-main.172/)，pp.2933–2958，DOI `10.18653/v1/2024.emnlp-main.172`；会议按所给第七版目录为CCF-B。ACL Anthology标注Outstanding Paper Award。
- **正式PDF**：[本地论文](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving.pdf>)共26个物理页，SHA-256 `14916d5d0a2dfa6053bf40882da172befce8690259050b6a840a32c23b0d66bb`，与ACL正式PDF字节一致。主文p1–9完整阅读L3；附录p13–26逐页核读，p12附录开头核对；参考文献p10–12未逐条追溯。未运行Isabelle、论文代码或实验。
- **开放资源**：[作者代码与数据](https://github.com/neuro-symbolic-ai/explanation_refinement)，论文脚注直接指向该仓库；检查README、目录和MIT许可，固定提交`003ec20444a427492ce072c34255d90245e436d3`。论文页亦列[补充数据包](https://aclanthology.org/attachments/2024.emnlp-main.172.data.zip)；仅以范围读取核对压缩包目录及部分结果，未下载校验整个压缩包。Google Scholar引用数和完整优先级待统一核验。

## 方法及研究对象

Explanation-Refiner针对带自然语言解释的NLI：给定前提、假设和解释句，LLM以事件语义和一阶逻辑将解释转为Isabelle/HOL公理，将前提写进`assumes`、目标写进`shows`，再生成粗略推理及证明步骤。证明器返回语法错误、未通过的步骤或超时，LLM依据反馈修正语法并筛选、改写解释，再次尝试证明（p2–5、16–20）。算法最多进行11次外层检查，可理解为初始检查加至多10轮修订；每次语法纠错最多3次，求解超时阈值65秒。多选QA以**正确答案**构造待证假设，因此其证明通过率不是实际答题选择准确率。

形式证明只保证形式化表达式相对于给定公理可推导；公理是否为真、自然语言转换是否忠实需要独立检查。p17提示示例将含“typically”的句子形式化成未显式保留该限定的全称式。作者也指出逻辑一致性与AI安全之间仍需进一步研究（p9、17）。

## 实验与原文限制

- 正文报告e-SNLI、QASC、WorldTree共300个有代表性的样本；仓库三个数据文件各100条。Figure 3的纵轴是逻辑有效解释数：GPT-4分别为36→84、12→55、2→37，即各100条条件下提升48、43、35个百分点，不是相对增长率或RAG攻击检测率（p5–6）。
- Figure 6中将形式化组件换为GPT-4、保留原模型推理，e-SNLI上Llama2-70b通过数由7增至65；该对照涉及不同模型访问及调用开销，不能直接转化为轻量成本保证（p7）。
- 作者对修订结果做了人工事实性与是否琐碎评价：QASC中GPT-3.5与GPT-4分别有2.27%和1.82%的修订解释含与事实不符的句子。已读文本未明确各组确切人工评价样本数、评审人数和一致性；结果不能视作全部原始样本的事实真实性保证（p7–8）。
- [ACL补充结果](https://aclanthology.org/attachments/2024.emnlp-main.172.data.zip)中被范围读取的e-SNLI GPT-4/GPT-3.5结果文件，`repaired at = iteration 0`字段分别有31/14条，Figure 3初始有效数为36/19；两文件分别另有16/45条缺该字段，最终有该字段的条数为84/55，与图中最终数一致。尚未确认这些文件是绘图输入或缺字段处理方式，不据此判定哪一处有误。
- p24 Figure 24的酒保案例标记该轮证明失败；但其印刷公理已存在一个同时满足`Person`与`Black`的对象，足以推出示出的存在性目标。这里说明指定证明步骤失败不等于目标在所示公理下不可证；这是对印刷公式的逻辑核对，不是Isabelle实现复现。p16算法输入写`h`而第32行写`H`，也只作为排版差异记录。

## 对开题A/B的定位

对B，形式化多句证据、判定前提与结论蕴含、使用错误反馈修正解释，是较早的神经符号方法先例；VeriCoT是后续同类近邻。但本方法处理给定NLI前提和解释，不直接验证检索来源或事实真值，不提供恶意chunk筛选、正常query最终误删率或多跳证据保留保证。

对A，论文未研究恶意RAG知识库、单源未知chunker或多块联合召回与共同必要性；不能将定理证明成功视为来源可信或攻击无效的证明。
