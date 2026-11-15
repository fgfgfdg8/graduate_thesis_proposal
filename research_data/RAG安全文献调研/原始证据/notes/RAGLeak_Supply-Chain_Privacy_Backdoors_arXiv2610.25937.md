---
tags: [llm-generated, rag-security-evidence, privacy, backdoor]
study_id: arxiv-2610.25937
reading_level: L3
checked_date: 2026-11-13
---
# RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation

**阅读状态：L3。** arXiv v1本地22页PDF正文及附录已全文阅读；未独立复现。

- **作者**：Yuchen Chen；Wei Cheng；Yuan Xiao；Junda He；Jieke Shi；PingPing OuYang；Quanjun Zhang；Chunrong Fang；David Lo；Zhenyu Chen
- **版本与日期**：arXiv:2610.25937v1，2026-10-19提交，cs.CR；截至2026-11-13官方记录只列v1，未核实正式venue
- **CCF**：预印本无正式venue，不赋CCF等级
- **PDF**：[论文库PDF（跨仓库相对路径）](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/RAGLeak_ Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation.pdf>)；22页；SHA-256 `CD4EB90E699768BA0B88223FCD1EE743CA6F70EF2D868CB0766D41296616D335`
- **代码**：作者曾提供匿名代码入口；2026-11-15访问返回HTTP 401（not_connected），无法核验公开可访问性；未审查代码或复现
- **引用与优先级**：Google Scholar未观测；优先级未计算

## 方法与结果

攻击者控制生成器提供方并投毒其微调数据植入后门，但不控制受害方检索器或知识库。带触发词的查询仍正常检索，后门生成器将正常检索到的私密上下文以可逆混淆方式输出，再由辅助LLM重建。论文明确排除向知识库注入恶意文档。

主实验默认微调数据投毒率40%，dense top-3，按解码文本ROUGE-L > 0.5计攻击成功。三个任务的RAGLeak ASR范围为HealthCareMagic 0.91-1.00、EnronQA 0.58-0.73、CodeSearchNet 0.86-0.88。防御测试后仍观察到较高ASR，但CodeSearchNet的benign ASR本身为0.40-0.44，必须与基线并列解读。作者承认检索架构、部署环境和防御覆盖有限。

## 与开题的关系

这是生成器微调供应链导致的隐私后门近邻，不是知识库语料投毒：攻击者不写入或操纵检索库，检索内容本身是正常上下文。它不检测恶意文档、事实真实性或恶意证据块。该工作要求把生成器供应链与检索语料完整性区分；只有当开题扩展到生成器后门或隐私外泄时才构成直接研究范围竞争。

它与2025年ACISP同名论文 *RAGLeak: Membership Inference Attack on RAG-Based Large Language Models*（DOI `10.1007/978-981-96-9101-2_8`）是不同研究，不能合并书目或阅读等级。

## 来源与追溯

[arXiv v1记录](https://arxiv.org/abs/2610.25937v1)。正文与附录页码按本地22页PDF计；远端PDF直链本次未单独核验。引用数未核，未运行代码。

[返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-20261113-ragleak-supplychain) · [元数据汇总](../../../../docs/RAG安全文献补查元数据_20261102.md)
