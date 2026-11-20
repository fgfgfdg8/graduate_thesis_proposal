# Learning to Erase Private Knowledge from Multi-Documents for Retrieval-Augmented Large Language Models（整理笔记）

核对日期：2026-11-15。本文是按既有阅读记录和公开一手来源重新撰写的中文分析，不复制论文摘要或正文。

## 论文身份与阅读范围

- Yujing Wang 等，**Learning to Erase Private Knowledge from Multi-Documents for Retrieval-Augmented Large Language Models**。Crossref 中 ACM 提交的记录将其列为 *Proceedings of the 35th ACM International Conference on Information and Knowledge Management* 论文，页码 4973–4984，出版日期 2026-11-06，DOI 10.1145/3799682.3840753；CIKM 2026 官方主会程序以 Eraser4RAG 名称列出同一 DOI。
- **既有阅读记录**：L3，逐页阅读 arXiv:2504.09910v2（2026-06-24）本地 PDF 物理第 1–12 页。本轮核验该文件哈希、首页与代表性表格数值，未重新逐页审读。
- 已读 arXiv 稿首页仍含会议模板占位符；正式出版身份来自出版方提交的元数据和会议官方程序，不能从占位符推断。ACM DOI 落地页本轮返回 HTTP 403；尚未取得并逐页比较 ACM 出版版，不能将 arXiv 的阅读等级转授给出版版。

## 方法、结果与适用边界

- Eraser4RAG 在多篇检索文档上抽取并合并实体关系，以预先给定的 private/public 知识约束文档改写；以 Flan-T5 和 PPO 优化隐私信息去除与公开信息保留。其实验构造会对全局关系采样并过滤，以模拟受控的跨文档推断风险。
- arXiv v2 物理第 9 页表 5 报告隐私问答攻击指标 r_attack 为 0.3745：只针对改写前可回答、由私有知识构造的问题。表中未给出各数据集拆分或逐项分母，不能把该值指定为单一数据集上的通用泄漏率。
- 物理第 8 页表 4 中，HotpotQA 的准确率由未改写的 0.2690 降至 Eraser4RAG 的 0.2585；按论文定义，效用问题及答案实体在私有知识图中不连通。该结果说明需要同时观察隐私与合法问答效用，不能外推为所有查询的损失。
- 论文处理控制方定义的隐私关系，不判断文档是否恶意，不提供来源鉴真或投毒块检测。关系抽取、私有/公开标注与实体归一化影响结果；图连通率是推断风险代理，不能作为通用隐私保证。

## 尚待核实

- ACM 出版 PDF 与已读 arXiv v2 是否存在实质差异，以及最终版的实验和表格口径。
- [作者仓库](https://github.com/yjEugenia/Eraser4RAG)页面存在，但本轮未验证其具体代码版本、数据许可和完整性，也未执行复现。

## 来源与携带性

- [arXiv v2 记录](https://arxiv.org/abs/2504.09910v2)；[arXiv v2 正文](https://arxiv.org/html/2504.09910v2)；[Crossref 中 ACM 出版元数据](https://api.crossref.org/works/10.1145/3799682.3840753)；[CIKM 2026 官方主会程序](https://cikm2026.diag.uniroma1.it/cikm-program/program.html)。
- [证据地图](../../../../docs/RAG安全证据地图_20261102.md)：项目内相对路径，目标文件已被 Git 跟踪；本次核验使用工作区内容。
- [本机文库 PDF](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Learning to Erase Private Knowledge from Multi-Documents for Retrieval-Augmented Large Language Models.pdf>)：**仓库外、仅本机路径，不随 Git 携带**。现存文件 12 页，SHA-256：a85e90c90625ea9b8ca5b16e8aca77b5f6cee006818f5348097a2298ce3d908a。本轮未重新下载 arXiv PDF 以进行字节比对。
