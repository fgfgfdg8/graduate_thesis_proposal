---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: arxiv-2407.09164
reading_level: L3
checked_date: 2026-11-15
---
# ShadowCode: Toward (Automatic) External Prompt Injection Attack Against Code LLMs

**阅读状态：L3，作者稿正文。** 逐页核读 [arXiv v6 PDF](https://arxiv.org/pdf/2407.09164v6) 物理第 1–12 页正文；第 12–13 页参考文献与第 14–16 页附录文字亦核查。图表按可提取文字和图注核对，未声称逐点读取曲线、运行代码或复现。正式期刊身份经 [Crossref 出版登记](https://api.crossref.org/works/10.1109/TDSC.2026.3703498) 核对；未取得期刊最终 PDF，不能将所读作者稿等同最终版。

- **作者：** Yuchen Yang、Yiming Li、Hongwei Yao、Bingrun Yang、Yiling He、Tianwei Zhang、Dacheng Tao、Zhan Qin。
- **正式身份：** IEEE Transactions on Dependable and Secure Computing 23(5), 10527–10540, 2026；DOI [10.1109/TDSC.2026.3703498](https://doi.org/10.1109/TDSC.2026.3703498)；按用户所给 CCF 第七版为 A 类。正式登记题名为 Toward，作者稿题名为 Towards，二者按作者及 DOI/arXiv 等身份线索作为同一研究比较，不重复计数。
- **实际阅读版本：** arXiv:2407.09164v6，2025-07-22，16 页；[本地 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/ShadowCode_ Towards (Automatic) External Prompt Injection Attack against Code LLMs.pdf>) 的 SHA-256 为 `9258a2639c51499c2811d7f5beb48a38a9f1ae3b650745fbaf866d8599800b84`，与 2026-11-15 从 arXiv v6 获取的 PDF 字节一致。
- **作者制品：** 论文给出的 [ShadowCodeEPI 仓库](https://github.com/LianPing-cyber/ShadowCodeEPI) 转到 `ywy-cyber/ShadowCodeEPI`；2026-11-15 读取固定提交 [c52f9cb](https://github.com/ywy-cyber/ShadowCodeEPI/tree/c52f9cbaf38ccd9fc888022bcaa3df3fcef1594a) 的归档仅含 README，未发现实现或数据。仓库入口可达不等于代码可用或已复现。
- **引用数据与优先级：** 见[元数据表](<../../../../docs/RAG安全文献补查元数据_20261102.md>)；未观察到的 Scholar 引用次数保持未知。

## 方法与边界

论文研究第三方把非功能性扰动带入用户的代码上下文，使代码模型在指定位置生成攻击者希望的代码（作者稿 pp. 2–4）。作者将直接复制、依赖项和 RAG 知识库列为可能的传播途径；实验对象是代码补全。不能把“RAG 可作为入口”的场景说明扩写成已对文档分块器、稠密检索或多块共同召回开展实验。

作者先将目标表示为位置代码和目标代码，再模拟必需代码及与目标无关的上下文，利用代理代码模型做搜索；方法提高目标输出前部的优化权重，并引入少量从目标表示选出的关键词（pp. 5–7）。这些部件在同一代码上下文中发挥作用，不是测试真实源文档未知分块后两块分别召回、并经固定背景的留一及联合删除证实各块必要。

## 实验设计与结果

- 数据和任务：13 类恶意目标、三种语言共 31 个适用案例；HumanEval/HumanEval-X、CodeXGLUE、MBPP、EvalPlus 构成七个语言子数据集，Table 1 汇报 14,273 条数据（p. 7）。论文未在这些数据上给出与开题同构的单源分块或查询级证据清洗协议。
- 开源代码模型：CodeGemma-2b、CodeGemma-7b、CodeGeeX2-6b 的 Table 2 平均 ASR 分别为 82.0%、86.6%、84.9%，对应无攻击 12.2%、8.4%、15.0%；表中的最高单格 97.9% 不代表全部条件或全部案例成功率（pp. 8–9）。
- 迁移：作者称在 VS Code 集成应用中手工测试随机选择的 HumanEval/HumanEval-X 样例共 620 条；Table 4 的 GitHub Copilot 黑盒转移结果在 Python、C/C++、Java 分别为 90.4%、67.7%、74.4%，CodeGeeX 灰盒分别为 93.3%、80.4%、71.7%（p. 10）。不能概括成两款产品所有语言均超过 90%；文中样本、案例和重复次数的独立性与置信区间未闭合。
- 指标：ASR 要求生成代码具备目标功能且位于指定位置；NBR 统计超过 20% ASR 门槛的案例比例，STF 按超过 80% 门槛的案例贡献计算（p. 8）。附录 A 说明门槛参考了本实验攻击与基线表现（p. 14），因此不能解释为独立校准的查询级误报率或跨任务统一风险保证。
- 防御：p. 11、附录 B 的语义分析将 820 条原始代码与 820 条注入代码输入 CodeGemma-2b，观察表征的 t-SNE 投影。作者报告投影混合，但没有训练所提开题 B 的分类器，也未报告该分类器 ROC 或低 FPR；二维投影相混不证明高维或其他模型的监督检测必然失败。作者还观察删除字符与更换载体后的攻击表现，但未给出与开题 B 同口径的干净查询误删或问答效用。
- 可比性：基线包括未攻击、为代码任务改写的 GCG 和精简的手工间接提示；p. 9 对不同方法采用的 token 预算并不完全相同。短扰动是长度属性，不能单凭长度证明真实用户检查中的隐蔽性（pp. 9、12）。

## 对开题的启示

**A：** 外部代码和跨文件上下文会携带定向影响，构成传播面和上下文优化的近邻；但其实际攻击单元、任务和评测不覆盖“单一真实长源→未知分块→双块共同召回→单块与联合删除”的联合条件。不能因此宣称该交集已经被证明安全，也不能据此排除其他文献。

**B：** 该研究对“仅凭视觉上语义分离就能检测注入”构成反例动机；评测 Code LLM 表征与拟议的冻结编码器、检索统计、跨块关系、异源参照并不相同。需要独立测试正常查询级误删、攻击检出、保留多跳桥接证据和 QA 效用。

[证据地图条目](<../../../../docs/RAG安全证据地图_20261102.md#src-28b080c208ab37cb>) · [全部逐篇笔记](<../../../../docs/RAG安全证据地图_20261102.md#paper-notes>)
