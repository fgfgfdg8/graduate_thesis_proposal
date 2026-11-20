---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2609.35155
reading_level: L3
checked_date: 2026-11-02
---
# Right Facts, Wrong Rule: Scope-Transfer Poisoning of Retrieval-Augmented Generation

> **2026-11-15链接复核范围：** 此前仅核对本地PDF首末页、版本标识、页数、已有哈希和可验证链接；那次核验未扩大阅读记录。

**阅读状态：L3（依既有正文阅读记录）。** L1仅书目/摘要候选；L2为注明范围的局部全文；L3为正文全文，不自动包括全部附录、参考文献或正式版。原审计具体记载v1正文pp.1–7及v2正文pp.1–9已读。2026-11-15本轮仅补读v1 p.8页首的作者声明续行，并确认v1 p.9、v2 p.10均为参考文献；未逐条阅读这些参考文献。

- **作者**：["Kaisheng Fan", "Yishu Gao", "Xunzhu Tang", "Tegawend’e F. Bissyand’e", "Weizhe Zhang"]
- **机构**：["哈尔滨工业大学", "卢森堡大学SnT", "鹏城实验室"]
- **年份 / 会议 / track**：2026 / arXiv / 未核实 / 未提取
- **发表状态**：preprint; formal venue not verified
- **CCF**：正式身份已核等级 未核实 / 未提取；作者声称或关联venue等级 未核实 / 未提取。以第七版目录为准，Findings/Industry/workshop不继承主会等级。
- **引用量**：见[元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)。
- **代码**：未核实 / 未提取
- **关联标题**：["LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation", "Right Facts, Wrong Rule: Scope-Transfer Poisoning of Retrieval-Augmented Generation"]

## 一句话总结与核心贡献

集合共同必要性与规则适用域误用；两个标题为同一研究版本。

方法、结果及适用条件见下列报告；作者结论与开题比较分别列出。

## 与开题逐项比较

**A：** 共同必要性、规则+实例、子集对照与重分块已有先例；单个真实源文档、未知切块和共召回联合约束仍待比较。

**B：** 规则适用性检查与一次额外核验已有先例；不是无条件防御证书。

## 局限、可比性与不确定性

分母与模式不同；两版本不独立计数。

**样本/版本依赖：** 同研究多报告不独立计权；跨研究同基准的逐query重叠未知，不数值合并。

## 报告、来源与实际阅读范围

### arxiv-2609.35155v1

- **书目来源**：[arXiv v1版本记录](https://arxiv.org/abs/2609.35155v1)
- **DOI / arXiv**：10.48550/arXiv.2609.35155 / 2609.35155
- **本地PDF**：[论文库v1 PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/LENS_ The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation.pdf>)；9页；SHA-256 `E40002E185AC0A7C6BF779B0ABF636108E70CE320CA2169F0E5562749103B634`
- **原始PDF链接**：[公开PDF](https://arxiv.org/pdf/2609.35155v1)；2026-11-15 HEAD检查曾返回200、也曾超时，之后一次HEAD检查返回200
- **实际阅读**：既有原审计记录为L3，记载v1物理pp.1–7正文完整、p.8参考文献仅追溯线索。2026-11-15本轮补读p.8页首作者声明续行，并确认p.9仅为参考文献；参考文献未逐条核实。过去是否逐条阅读p.9不能证明，不作为正文L3条件。

#### 方法、结果与适用条件

## M01. LENS：同一论文的两个版本必须共同比较（A极高、B高，L3）

- 当前标题：Right Facts, Wrong Rule: Scope-Transfer Poisoning of Retrieval-Augmented Generation。
- v1标题：LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation。
- 全部作者：Kaisheng Fan; Yishu Gao; Xunzhu Tang; Tegawend’e F. Bissyand’e; Weizhe Zhang。
- 年份/状态：2026预印本；arXiv摘要页未声明正式会议或期刊发表。CCF不赋级，不能把与CCF-A的关联误当录用。
- 唯一身份：arXiv:2609.35155；DOI 10.48550/arXiv.2609.35155。v1=2026-09-28；v2=2026-10-19。两个标题是一篇工作的版本演变，计数仅1篇。
- 原始来源：[版本历史（默认显示最新版本）](https://arxiv.org/abs/2609.35155)、[v1全文](https://arxiv.org/html/2609.35155v1)、[v2全文](https://arxiv.org/html/2609.35155v2)。历史记录提及临时目录中的HTML与文本；本次未检查或纳入该临时快照。未见可确认的自有代码链接，勿从同名仓库猜配。
- 发现渠道：既有记录提及AI Safety Daily 2026-10-17笔记并称其讨论v1；该链接于2026-11-15返回404，本次无法复核其内容。现有报告只按v2题目列为LENS，漏掉版本迁移对A定位的直接影响。
- 既有阅读记录：原审计概述曾称逐页核对两个版本；其具体记录为v1 PDF第1–7页正文全部、第8页参考文献线索，v2 PDF第1–9页正文（含§2–7与Limitations）全部、第9–10页参考文献仅追溯相关线索。2026-11-15本轮另补读v1第8页页首声明续行，并确认v1第9页和v2第10页仅为参考文献；不据此推断历史上已逐条阅读这些文献。未运行代码或独立复现。
- study_id：lens-2609.35155；report_id分别为arxiv-2609.35155v1、arxiv-2609.35155v2。两版本样本/manifest是否逐实例相同未核，故不视为独立复现，不跨版本合并效应。
- 本地PDF：[v1论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/LENS_ The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation.pdf>)、[v2论文库PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Right Facts, Wrong Rule_ Scope-Transfer Poisoning of Retrieval-Augmented Generation.pdf>)。v1机构：哈尔滨工业大学、卢森堡大学SnT、鹏城实验室；v2相同。引用量本次未核。

**方法与版本证据。** v1把多个文档的共同必要性设为显式约束，而非泛称多文档攻击；最终对每个真子集检查，采用固定背景及控制上下文。它与A的“抽象规则/互补事实、单块不足/组合有效”高度重合。v2主模式不再以子集结果作接收门槛，但保留isolation模式，不能据新摘要说组合性研究消失。v2§4.4还报告固定文本合并/拆分与重新索引不同块长的检查，因此“考虑重新分块”本身已有先例。

**结果口径。** v1 Table2的0.852是返回包条件下的Full ASR，全部尝试的E2E-Strict@5为0.363，不能混用。v2 Table2的47.1% TER包含4,000次构造尝试的失败；v2§4.2允许部分命中，不能把其TER当严格组合成功率。v2 Table3/6的16.4%是配对任务池检查后的TER，Table7的11.9%才是全部尝试的防御TER；两者分母不同。

**对A的结论。** 撤回“首次把无害片段组合成定向错误”“首次使用规则+实例桥接”“首次以单块/双块对照证明协同”这类宽泛表述。可继续检验的窄边界为：只改一份真实长源文档，由未知分块器产生同源块；同时证明完整性、块分离与共召回，以及它们随配置变化的联合变化。LENS已读设置直接插入2/3份文档且有重排，不等于已经验证此窄边界；但这也是待实验证成的差异，不能仅凭工程组合宣称创新。

**对B的结论。** v2显式检查规则适用性并让判定约束最终生成；额外一次LLM调用已存在，故“便宜检查后加一次审查”不独占。B仍需与其在同一上下文、调用/令牌预算及正常多跳效用下比较来源关系与选择性核验的增量。命题冲突检测不能代替适用性判断，全真且不直接矛盾的证据也可能被错误组合。

**待决。** 尚无把LENS转入开题同源源文档预算后的结果；v2重新分块只有正文汇总，不能推断它已覆盖未知起点/长度/重叠率和双块共召回的全部因素。下一步应先统一预算及成功分母，再判断A剩余贡献。

**PDF定位与新增审查。** 共同必要性证据见v1第2页Eq.2–3、第4页评价定义、第5页Table2、第6页机制对照；v2第4页§3.3保留isolation gate，第7页§4.4给出重分块结果。v1第2页明言经验真子集检验不是概率证书。v2第3页Proposition1只在规则/范围正确提取、核验无假阳性、最终生成严格执行等假设下成立，不能给实际prompt审计无条件保证；第8页显示实际核验链仍可能出错。B中独立来源ID也不等于事实独立或参照为真。LENS的条件保证与B的query级筛查阈值是不同构念。

### arxiv-2609.35155v2

- **书目来源**：[arXiv v2版本记录](https://arxiv.org/abs/2609.35155v2)
- **DOI / arXiv**：10.48550/arXiv.2609.35155 / 2609.35155
- **本地PDF**：[论文库v2 PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Right Facts, Wrong Rule_ Scope-Transfer Poisoning of Retrieval-Augmented Generation.pdf>)；10页；SHA-256 `B508CC80EE8C5D05EA3DE44ED896BAAA3AB8D08C4BB97DCB3C80E318D4D2DC81`
- **原始PDF链接**：[公开PDF](https://arxiv.org/pdf/2609.35155v2)
- **实际阅读**：既有原审计记录为L3，记载v2物理pp.1–9正文完整、pp.9–10参考文献仅追溯相关线索。2026-11-15本轮确认p.10仅为参考文献，未逐条核实；过去是否逐条阅读p.10不能证明，不作为正文L3条件。

## 待核事项与追溯

未逐条核实的参考文献、未读版本、代码及样本依赖按上文所列范围保留待核。v1 p.9与v2 p.10均仅有参考文献；历史逐条阅读与否未知，正文L3不覆盖该主张。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md)。

<!-- PDF_LIBRARY_START -->
## 科研数据库PDF（按实际文件题名归集）

同名版本分别保留；题名差异及阅读范围按报告列出。

- [LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/LENS_ The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation.pdf>)
- [Right Facts, Wrong Rule: Scope-Transfer Poisoning of Retrieval-Augmented Generation](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Right Facts, Wrong Rule_ Scope-Transfer Poisoning of Retrieval-Augmented Generation.pdf>)
<!-- PDF_LIBRARY_END -->
