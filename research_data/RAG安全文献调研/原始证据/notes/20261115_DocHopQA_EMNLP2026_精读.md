# DocHop-QA：EMNLP 2026 正式版精读与开题 A/B 对照

核查日期：2026-11-15（Asia/Shanghai）。以下页码为正式 PDF 的物理页。阅读等级 **L3（正文范围）**：逐页阅读正文 §1–8 及 Limitations（物理页 1–10）；补读附录 B、D.1、D.3、E、G.2 的相关段落，参考文献及其余附录未逐项精读。未运行论文制品或复现实验；Google Scholar 引用数待统一核查。

## 1. 身份与版本

- **论文**：Jiwon Park、Seohyun Pyeon、Jinwoo Kim、Rina Carines Cabral、Zhenyuan He、Yihao Ding、Soyeon Caren Han，*DocHop-QA: Towards Multi-Hop Reasoning over Multimodal Document Collections*，EMNLP 2026 主会正式论文，58233–58261。[ACL Anthology 论文页](https://aclanthology.org/2026.emnlp-main.2563/)及[正式 DOI](https://doi.org/10.18653/2026.emnlp-main.2563)。Anthology 作者元数据最后一名显示 **Caren Han**，PDF 首页在相同作者位置写 **Soyeon Caren Han**；此处分别保留来源写法。[同一研究的 arXiv v4](https://arxiv.org/html/2508.15851v4) 第五作者写作 **Zhenuyan He**，正式会议信息和 PDF 写 **Zhenyuan He**；版本间拼写差异未消解。
- **CCF**：用户提供的《第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）》PDF 物理页 58 将 EMNLP 列为**B 类会议**；该论文为 Anthology 所列 EMNLP 主会论文，不当作 ACL 主会或 CCF-A；具体论文是否属于目录认定的 Full/Regular 类型尚未单独核实。
- **本地正式版 PDF**：[按完整标题命名的 29 页 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/DocHop-QA_ Towards Multi-Hop Reasoning over Multimodal Document Collections.pdf>)；23,599,060 字节，SHA-256 `60de057c14c70354bc241e8c1741f936a21e1b5c623f8488575a0b4c90e810be`。来源为 Anthology 正式 PDF，分段下载后校验字节范围、PDF 首尾标记和首页标题；未逐字与其他版本比对。

## 2. 问题、方法与评测

DocHop-QA 是多文档科学问答基准，用于观察文本、表格和页面版面中的证据整合，**不是 RAG 投毒攻击、检测或防御方法**。作者从 PMC Open Access 文献中构造约 2 万文档对、9,250 个不同文档；最终 11,379 个问答实例按 11 类问题概念构造，包含单文档和多文档情形（§3–5、表 2、图 2）。问题以 LLM 生成和规则模板结合，证据按词法/语义相似性及针对问题类型的规则匹配；段落型多为 fan-hop，表格型按 chain-hop 串联证据（§3.2–3.4）。

无链接的描述需要限定：§3.2 称表格引用链接是文内结构锚点而非文档配对条件；附录 D.3 对 TS/TSL 类型又明确通过**表格引文标记**关联被引用文档的摘要。因此不能把整个题集笼统描述为完全不依赖引用关联；文档配对规则与后续证据链链接是不同环节。

四项任务分别评估生成式答案、结构化答案索引、OCR 版面框索引和 XML 实体索引；生成结果主要按与参考答案的 BLEU/ROUGE 词汇重叠计分（§6、附录 G.2），不能等同投毒防御成功率。作者另报告检索的单片段召回和完整多跳召回：表 10 中 GTR-large 的 Top-5 snippet recall 为 **0.76**，complete recall 为 **0.39**；后者要求共同取回所有支持片段。具体采样与实现口径须在复现时核对，不把该差距直接当作防御过滤造成的损失。

在选作人工评价的 **50 题**上，表 9 报告 Qwen3-VL-8B 的 question-only、GTR top-5 和 gold snippets 条件 ROUGE-L 分别为 **10.2、28.2、48.5**；人类持完整文档的结果为 **58.6**。输入内容和对象不同，不把各差值解释为单一环节的因果效应或总体代表性估计。

## 3. 与开题的具体关系

- **A：攻击与共同必要性。** 论文研究正常证据整合，不涉及攻击者写入真实长文档、未知分块、恶意块联合召回、固定背景的 `C00/C10/C01/C11` 对照或定向错误答案；多文档或多跳标签不自动证明某两个块对攻击共同必要。它可提供正常证据定位和多证据共同召回的效用基准，不能作为同源协同投毒的撞题证据。
- **B：防御与干净效用。** complete recall 对“支持片段是否共同保留”有参考价值；若用于过滤评估，需在固定语料和查询上另记过滤前后全部支持片段共同存活、逐角色存活与答案质量，并另以**干净查询为分母**统计“任意块被直接误删”的查询级 FPR。本文没有恶意检索块检测、源真实性校验、query 级最终误删校准或异源可信锚点规则，不应把 complete recall 叫作这些安全指标。
- **验证建议。** 当前题目以自动匹配证据为基础，评测共同必要性之前应对相同背景执行逐片段与成组替换/删减，核验标签与模型输出；这是基于开题提出的后续实验设计，并非论文已完成的因果实验。

## 4. 数据质量、制品与限制

作者在 §4 使用 50 个有意覆盖题型的实例进行人工与 LLM 评判比较；全量数据的约 92% / 87% / 76%（自然性 / 准确性 / 完整性达到至少 3 分）是 **Qwen3.5-9B 自动评分**，不能说成全量人工标注通过率。附录 E 表 17 显示一致性依评价指标和维度变化，例如该模型准确性维度的 Krippendorff α 为 −0.441；作者在同页讨论高分集中对部分指标的影响。附录 G.2 还说明参考答案由 GPT-4.1 根据选中片段合成，三位作者进行了交叉核查，但该段未给出可据以确认的人工逐题覆盖比例。实验指标及模型评估不等于事实正确性的无条件保证。

论文附录 B 指向代码和数据短链；该短链的命令行请求触发 Cloudflare 403，但浏览器会话成功跳转到作者提供的 [DocHopQA 总目录](https://drive.google.com/drive/folders/1lpM7aq2By_v5Cn5soh82cFx3p8jjdo1n)，其中可见 [代码目录](https://drive.google.com/drive/folders/1ek-kZb6DY6WoeESB_yazepeJ6jJRNhqB)和[数据目录](https://drive.google.com/drive/folders/1GmFaJZSkSjeGPY-plWmWlxxUs8Hg9Pd5)。这些观察支持制品与论文对应，但未测试匿名访问、运行代码、复现或完整下载。关联的 [Hugging Face 数据卡](https://huggingface.co/datasets/anonymousaaai123/DocHopQA_Dataset)写总量 11,379，同时列段落型 8,547、表格型 2,812，两者相加为 11,359；正式 PDF 表 2 的八项段落型数字相加为 8,567、三项表格型为 2,812。差 20 的原因与实际逐条分类未核，不能据此推断数据缺失。数据卡沿用早期六作者与 Cabal 拼写，不能代替正式会议信息。

论文数据来自 PMC Open Access，底层原始文献仍须遵守各自许可；论文自身也指出生成模板规律、缺少显式中间推理标注及细粒度表格运算不足等局限。尚未检查全部数据、PDF 图片或发布制品。
