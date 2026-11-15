# Universal Vulnerabilities in Large Language Models: Backdoor Attacks for In-context Learning

## 书目信息与版本

- **作者**：Shuai Zhao、Meihuizi Jia、Luu Anh Tuan、Fengjun Pan、Jinming Wen。
- **正式出处**：Proceedings of EMNLP 2024, pp. 11507–11522；DOI [10.18653/v1/2024.emnlp-main.642](https://doi.org/10.18653/v1/2024.emnlp-main.642)。EMNLP主会按第七版CCF目录为B类；本文不是Findings论文。
- **官方来源**：[ACL Anthology记录与正式PDF](https://aclanthology.org/2024.emnlp-main.642/)。
- **本地PDF**：[论文库文件](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Universal Vulnerabilities in Large Language Models_ Backdoor Attacks for In-context Learning.pdf>)；16个物理页，19,720,855 bytes，SHA-256 `A6D91A4235BEEDF951FD4B40F5C897D3ED0E447BBAC4DC49B7CF5A7B639FA539`。
- **阅读范围**：正式版PDF物理页1–16全文，L3；参考文献未逐条审计，未运行代码或复现。
- **代码**：作者[ICLAttack GitHub仓库](https://github.com/shuaizhao95/ICLAttack)可访问，未审代码和许可证、未运行。ACL所列软件包URL于2026-11-14返回404，因此不作有效工件链接。

## 威胁模型与方法

ICLAttack面向攻击者能影响演示上下文构造、但不更新目标LLM参数的设置。论文分开研究两种投毒入口：在演示样例中加入触发行为，以及在演示提示/模板中植入可触发的恶意指令结构。触发器与目标行为由攻击者预先设定；推理时，用户查询与已被污染的演示上下文共同输入模型。作者以OPT、GPT-Neo、GPT-J、Falcon等模型评估分类任务，并扩展到GPT-4摘要生成。

这与检索增强上下文存在概念邻近：只要示例或上下文由攻击者控制，参数冻结并不消除上下文后门风险。但论文没有向持久知识库写入恶意passage，也未评估检索器、chunker、Top-K或检索后过滤，因此不是RAG语料投毒实验。

## 结果与解释边界

- 摘要报告OPT系列在三个分类数据集上的平均ASR为95.0%；这是作者报告的跨数据集汇总，不代表每个模型、数据集或触发设置均达到该值。分类任务的攻击结果见正文实验部分与Tables 1–4。
- **clean-label不能泛化到全文所有实验**：摘要将poisoned examples概括为correctly labeled；但附录C的LCSTS摘要生成实验明确写明修改演示样例标签。该GPT-4设置报告ASR 92.67%及ROUGE-1/2/L 38.02/20.01/32.89（PDF物理p.15，会议页11521）；示例模板见Table 11（物理p.16，会议页11522）。因此应按任务和实验配置分别描述标签是否保持。
- 论文测试的是演示上下文对模型输出的后门影响，不报告检索召回、真实知识库污染、未知分块鲁棒性或query级过滤误报。
- 附录的分类样例展示触发器加入上下文与查询后的模板设计，但其任务标签和人工构造样例不等真实RAG证据来源的真实性核验。

## 对开题A/B的关系

**A方向**：它直接限制“在上下文中投毒演示样例即可形成后门”这一宽泛表述，但其对象是ICL demonstrations/prompts，不是单一真实长源文档经受害者未知chunker产生的同源块；未检验这些块在同一query下共同Top-K召回、逐块必要性或端到端RAG攻击成功率。

**B方向**：论文不做检索后恶意文档检测、跨块事实关系判定、来源真实性复核或正常query误删校准。它可作上下文通道威胁先例，不是B检测器的竞争方法。

## 阅读定位

| 主张 | 论文位置 |
|---|---|
| ICLAttack与两种演示上下文投毒入口 | 正文§3–3.3，PDF物理pp.3–5（会议页11509–11511） |
| OPT与其他模型分类结果、基线和防御 | 正文§4，PDF物理pp.5–10（会议页11511–11516） |
| 摘要生成任务修改演示标签及ASR结果 | 附录C，PDF物理p.15（会议页11521） |
| 各数据集演示模板 | Table 11，PDF物理p.16（会议页11522） |
