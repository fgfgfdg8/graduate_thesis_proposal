---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: acl:2024.acl-short.42
reading_level: L3
checked_date: 2026-11-16
---
# DocFinQA: A Long-Context Financial Reasoning Dataset

阅读与核对日期：2026-11-16（Asia/Shanghai）。

## 结论与适用边界

**这是正常、真实长财报环境下的检索和数值问答基准，属于A/B的环境与评测近邻；在本次阅读全文范围内，未发现对开题A或B的直接撞车。** 其同一份SEC长文档、固定分块、检索Top-k及生成回答与开题研究共享系统要素，但本文没有构造攻击者控制的真实长源、互补恶意载荷、未知分块器迁移，也没有逐块/真子集消融来证明多个恶意块共同必要。Top-3被输入回答器并不等于三块对答案共同必要。[PDF物理页2／印刷页446](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=2>)；[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)；[PDF物理页4／印刷页448](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=4>)；[PDF物理页12／印刷页456](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=12>)。

对B，本文的相关性检索和长文问答可供**正常效用基线**，但文中未建立恶意来源识别、冻结语义与跨块关系/异源参照联合筛查、有限LLM安全复核，亦未报告独立clean-query上最终OR误删率或校准。无检索的System 2 Attention和迭代法仍把超长文档按约100K token分段处理，不能把“retrieval-free”写成“不分段”。[PDF物理页5／印刷页449](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=5>)；[PDF物理页14／印刷页458](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=14>)。

## 正式身份、版本与阅读收据

- **作者**：Varshini Reddy、Rik Koncel-Kedziorski、Viet Dac Lai、Michael Krumdick、Charles Lovering、Chris Tanner。
- **正式出处**：*Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*，2024，Bangkok，pp. 445–458。ACL Anthology ID `2024.acl-short.42`；DOI `10.18653/v1/2024.acl-short.42`；官方BibTeX key `reddy-etal-2024-docfinqa`。[正式文章页](https://aclanthology.org/2024.acl-short.42/)；[官方BibTeX](https://aclanthology.org/2024.acl-short.42.bib)；[官方PDF](https://aclanthology.org/2024.acl-short.42.pdf)。BibTeX与PDF首页对题名、作者、会议和页码一致。[PDF物理页1／印刷页445](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=1>)。
- **本地PDF**：[DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf>)。完整正式题名中Windows不允许的冒号以 `_` 代替；其余题名保留。官方PDF GET HTTP 200；2,047,669字节；14物理页；SHA-256 `9be07fd187659cc009bb80badbafb85cf0f994c6f318c927c05607baf4d2609b`。
- **实际阅读**：本次逐页阅读PDF主文物理页1–6（含结论、局限与伦理声明），附录A–J物理页9–14；物理页6–8的参考文献页亦逐页查看。图1–11和表1–6按所在页面核对，其中图片形式的图表作了可视核对。这里的“L3”只指这份正式PDF的主文及所附附录已逐页阅读，不代表独立复现实验、逐条验证参考文献、审核训练数据或阅读其他版本。
- **去重**：本轮在三份主文档、`audit/`、`notes/`、`records/`、`inputs/`及相关既有目录/队列中按`2024.acl-short.42`、完整题名和题名片段检索，未发现同论文既有逐篇全文阅读登记；指定论文库未发现同题名文件。旧目录中的题名规则曾命中该论文，但题名命中不授予既有摘要或全文阅读信用。未排除无登记阅读或未识别别名。
- **本次33篇摘要记录**：[ACL 2024 Short 36–68摘要筛查](<ACL2024_Short_36-68_逐篇官方摘要筛查_20261116.md>)。本篇在该批只算**一篇**摘要筛查，本笔记是在同一论文上新增一次正式PDF全文阅读，不另算一篇独立论文。

## 数据、检索和回答流程

1. **数据单元**：原FinQA的参考片段、问题和答案被扩展为`(完整文档D, 问题q, Python程序p, 答案a)`；文档来自SEC EDGAR对应财报，经解析转为含表格的Markdown。共7,437个问答样本，对应801份不同SEC filing；train/dev/test分别为5,735/780/922。报告平均每篇约123,453词。样本数不等于文档数，本文数字本身不证明数据按文档划分无重叠。[PDF物理页2／印刷页446](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=2>)；[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)。
2. **固定切块及参考目标**：每块2,750字符（文中约509 token），重叠20%；原FinQA参考片段与各块作四元组词序列相似度比较，取最高分的**一个**块`c*`作为检索目标，并以人工检查和少量替换实验作验证。这是单目标对齐设计，不是对所有可能支持证据的完备标注，也不证明真实任务只需一块。[PDF物理页2／印刷页446](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=2>)；[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)。
3. **检索与回答**：比较ColBERT、领域微调ColBERT、Sentence-BERT、OpenAI Ada，另有BM25先导对照；以目标块的HR@k衡量检索。检索块与问题输入模型生成数值推理Python程序。文中描述按查询与块的相似度取Top-k；未取得作者实验代码，因此不把这句话扩展为已核实的各模型具体索引实现。[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)；[PDF物理页4／印刷页448](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=4>)；[PDF物理页12／印刷页456](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=12>)。
4. **长文档对照**：对100K token以上文档的测试子集比较检索式问答、逐段提取后合并信息的System 2 Attention，以及逐段维护程序的迭代法；这些是正常任务比较，不是安全压力测试。[PDF物理页5／印刷页449](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=5>)。

## 逐页阅读与可复核结果

| 物理页／印刷页 | 已读内容及判断 |
|---|---|
| [PDF物理页1／印刷页445](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=1>) | 摘要、引言、图1：由短证据扩展至完整SEC财报，示例问题需从一份长文中的财务表定位数值并计算；论文给出数据集地址。 |
| [PDF物理页2／印刷页446](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=2>) | 相关工作、数据四元组、SEC来源与固定分块；图2呈现文档长度及原问题上下文位置分布。 |
| [PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>) | 表1与数据划分；四元组词序列选取单个目标块；FinQA 8,281项中保留7,437项，选取可能改变长尾问题类型分布；开始介绍检索模型。 |
| [PDF物理页4／印刷页448](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=4>) | 表2为开发集配置比较；图3及正文报告微调ColBERT测试集HR@1约0.35、HR@3约0.55，这是对单一对齐目标块的命中率，不是攻击成功率或安全召回率。 |
| [PDF物理页5／印刷页449](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=5>) | 表3测试集：GPT-3.5配微调ColBERT的论文报告得分42.6；具体few-shot/检索配置根据开发集选取。表4的100K+子集上，GPT-4检索/迭代/S2A分别47.5/20.0/23.0，人类41.0；这是论文的正常任务结果，不是安全指标。 |
| [PDF物理页6／印刷页450](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=6>) | 作者限制：仅测试集经人工验证；训练和开发集未完全验证。按程序输出接近金答案接受的自动生成程序可能有错误推理但答案碰巧正确，也可能错误拒绝正确程序。伦理声明及参考文献起始。 |
| [PDF物理页7／印刷页451](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=7>) | 查看参考文献续页；其中包括RAG、ColBERT及长上下文利用相关工作。 |
| [PDF物理页8／印刷页452](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=8>) | 查看参考文献末页。 |
| [PDF物理页9／印刷页453](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=9>) | 附录A：从FinQA标识映射SEC filing及获取缺失、格式转换造成的样本损失；表5为原FinQA示例。 |
| [PDF物理页10／印刷页454](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=10>) | 表6为DocFinQA文档、问题、程序与答案示例；论文明确为展示而截断长文上下文。 |
| [PDF物理页11／印刷页455](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=11>) | 附录B–D：比较BeautifulSoup与财务文档解析器；图5解释原程序向可读Python转换；模型详情与微调设置。 |
| [PDF物理页12／印刷页456](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=12>) | 附录E–F：问题类型分布、BM25与稠密检索先导比较；图8给出Top-3和3-shot输入模板，不能由多个输入块推断共同必要性。 |
| [PDF物理页13／印刷页457](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=13>) | 附录G–H：同文档中目标块作正例、其他块作负例微调ColBERT；3个epoch中使用第1轮权重；few-shot和块数配置比较。 |
| [PDF物理页14／印刷页458](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=14>) | 附录I–J：目标块位置分布；3名有4–5年财务文档经验的工作人员使用原PDF、关键词搜索和计算器，人均每题约25分钟。 |

## 开题比较与使用时应补的证据

- **对A的环境价值**：SEC原始长文、文本/表格混排、固定切块和真实问题有助于设计干净环境；但把某份财报改成对抗载荷、在未知分块器下实现同源多块共同召回，以及每一恶意块的必要性，都不是本文已完成的实验。不得将其Top-3或多步数值程序写成多块协同投毒证据。[PDF物理页2／印刷页446](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=2>)；[PDF物理页4／印刷页448](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=4>)；[PDF物理页12／印刷页456](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=12>)。
- **对B的环境价值**：可比较干净问答准确度和检索目标命中，但本数据的单目标块标注不足以直接计算完整多块证据保留；若用于B，需要另外核验多块证据、构造来源级污染与未污染独立校准集，并实际测量最终query级OR事件。论文没有报告这些安全控制。[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)；[PDF物理页4／印刷页448](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=4>)。
- **分数与比较限制**：表4的长文子集是成本受限的小规模比较；作者描述为随机选择200份100K+ token文档并对这些问题开展人工评价，未据此推断每位评审独立完成全部题目。三位评审均为与作者相识的受薪同事，不能泛化为领域专家总体表现。[PDF物理页5／印刷页449](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=5>)；[PDF物理页6／印刷页450](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=6>)；[PDF物理页14／印刷页458](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=14>)。
- **需自行核查**：原始FinQA/SEC数据与解析版本、文档级train/test重叠、目标块对多跳/跨表证据的覆盖、目标程序语义正确性，及本开题攻击/防御适配效果。本次均未做数据审计或实验复现。

## 数据、代码与许可核验

- PDF首页脚注直接指向作者机构的数据集：[kensho/DocFinQA](https://huggingface.co/datasets/kensho/DocFinQA)。2026-11-16公开页面和API HTTP 200，API返回`private=false`、`gated=false`，仓库版本`64ebaff62f692495bcc182f45cf9a9606251b19b`；仓库树包含README和train/dev/test三个JSON数据文件。未下载约4.7GB数据、未运行样例或模型。
- 数据卡元数据标`license: mit`；这仅是该数据仓库所声明的许可元数据，不自动确认所有上游材料和模型代码的许可。具体使用前仍应核验上游来源与条款。
- 检索论文PDF中的链接和ACL文章页，明确发现的是**数据集链接**，未找到作者明确指向的论文实验实现仓库。2026-11-16 GitHub仓库搜索`DocFinQA user:kensho-technologies`返回0；按名称找到的第三方仓库未验证作者关联，不能当作官方实现。检索范围有限，结论为**官方实验代码、固定版本与代码许可未确认**，并非断言代码绝不存在。
- 论文中的Python“程序”是生成答案的样本字段/实验输出，不能因此称论文的检索、微调、解析或评测实现已开源；本次未运行代码。[PDF物理页3／印刷页447](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=3>)；[PDF物理页11／印刷页455](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocFinQA_ A Long-Context Financial Reasoning Dataset.pdf#page=11>)。
