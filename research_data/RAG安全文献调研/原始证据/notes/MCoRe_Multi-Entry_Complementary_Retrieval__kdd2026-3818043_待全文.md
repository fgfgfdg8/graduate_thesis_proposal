---
tags: [rag-security-evidence, kdd2026, multi-hop-qa, retrieval, preliminary]
study_id: doi-10.1145-3770855.3818043
reading_level: L1
checked_date: 2026-11-16
status: pending-full-text
---
# MCoRe: Multi-Entry Complementary Retrieval with Reflection-Guided Iteration for Multi-Hop QA

> **当前是待全文的核查记录，并非逐页精读。** 已读大会目录、ACM摘要、公开代码和部分评估脚本；尚未取得或逐页阅读论文PDF，因而无法给正文页码、验证表格、实验分母或为PDF计算SHA-256。下文分别标明摘要陈述、静态代码事实和本笔记的推断，不以代码或摘要冒充正文结论。

## 身份、版本与去重

- **作者（正式顺序）**：Juxiang Zeng、Zhuohui Gao、Zhe Hou、Pinghui Wang、Guangmingzi Yang、Zehua Lei、Tao Duan、Jing Tao。ACM论文页（本机直接请求受限）、[Crossref记录](https://api.crossref.org/works/10.1145/3770855.3818043)和大会目录一致。Semantic Scholar 对部分作者使用带连字符或缩写形式；此处以ACM正式元数据为准，不把名字形式差异当作其他论文。
- **正式身份**：Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2，2026，出版页码6397–6408，DOI `10.1145/3770855.3818043`。ACM页面标注2026-08-08出版、开放访问及CC BY-NC-ND 4.0；此许可是论文出版版本的声明，不是代码许可证。
- **轨道证据**：[KDD 2026官方论文目录](https://kdd2026.kdd.org/papers/)的February Cycle中，此题名和DOI对应条目`track`为`rtp`；同页`cycle2TrackLabels`将`rtp`映射为`Research`。因此这是**Research track**。本地[第七版CCF目录](<../../../../../文献分区参照表/第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）.pdf>)物理p.35将SIGKDD列为数据库/数据挖掘/内容检索领域A类会议；这是会议级分类，轨道身份由大会目录另证。
- **去重范围**：本任务此前对三份主文档、既有notes/Bib及指定论文库按完整题名、DOI和别名检查；指定库的可读PDF还检查了元数据及首页。当前又对`research_data`中文本按DOI、题名和`MCoRe`检索，并直接检查notes及论文库的同名文件；均未找到本篇已有独立全文笔记或同名PDF。此结论限于当时所检查位置；不排除不可读文件或其他位置存在副本。注意MCoRe是复用缩写，不能仅凭名称合并其他任务的同名论文或代码库。
- **PDF状态与可读范围**：ACM页面提供正式PDF入口，但本次访问停在Cloudflare真人验证；[OpenAlex记录](https://api.openalex.org/works/https://doi.org/10.1145/3770855.3818043)和[Semantic Scholar记录](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3770855.3818043?fields=title,authors,openAccessPdf,url,externalIds,publicationVenue)未提供独立可下载作者稿。未找到可核验的arXiv版本；这不证明作者稿不存在。没有下载本地PDF，**PDF SHA-256：不可得**，正文物理页码、页数与正式出版页码的映射也尚未核验。取得全文后以论文标题命名并按用户指定目录归档；在文件实际取得前不创建本地PDF链接。

## ACM摘要可支持的内容

论文讨论多跳问答中的证据分散，以及不同语义粒度可能遗漏桥接信息。摘要称方法将实体、句子、摘要作为互补检索入口，入口与chunk显式关联，命中映射回chunk并在chunk级投票融合；若当前证据不足，则通过反思识别缺失桥接线索并提出后续查询。ACM补充视频的文字说明列出MuSiQue、2Wiki和HotpotQA三个基准。这里是摘要和补充说明的复述，不等同于已核对正文实现与全部实验设置。

摘要称相对先进基线，在三个多跳问答基准上平均提高6.77个EM点和8.79个F1点；2Wiki上的提升最多为12.70个EM点和14.06个F1点。**限制**：当前未见对应表格，具体比较基线、各数据集测试样本数、模型和检索设置、平均权重及“最多”的准确比较对象均未核实。不能把这些数字写成特定基线或特定样本量下的独立复现结果，也不能推断统计显著性。

## 公开代码：固定版本的静态核验

- [GitHub仓库](https://github.com/zhgao0729/MCORE)的README写明完整题名并自称官方仓库；仓库所属账号展示的作者名和单位与论文作者Zhuohui Gao一致。2026-11-16观察到`main`为提交`bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8`。仓库About说明仍是部分实现、拟在论文接收后完整发布；不能据此断言当前代码已覆盖论文全部实验。
- [Zenodo固定版本20441360](https://api.datacite.org/dois/10.5281/zenodo.20441360)记录作者Zhuohui Gao、版本`v1.0.0.0`、2026-05-29、MIT许可，关联上述仓库。下载归档仅在内存检查，大小7,941,788字节，MD5 `eade91b493e1914cd8a493a9f29be932`，与Zenodo元数据一致；内有README、脚本和三份数据JSONL，没有PDF。归档中的README、LICENSE、`tree_builder.py`、`reflect_retrieval.py`及两个评估脚本与上述GitHub提交逐字节一致；未将整个仓库逐文件比对，亦未执行代码或复现论文。MIT许可针对该软件归档，不替代论文出版许可。
- [树构建代码](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/tree_builder.py#L57-L187)先从数据样例构造带标题、文本和页面标识的列表，再按512-token目标合并页面；超过目标的单个页面被保留为一个较长chunk，而非强制切开；`text_chunker`先汇集不同样例的页面再合并。其[chunk节点构建](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/tree_builder.py#L289-L318)只将chunk文本、索引、子节点和嵌入传给`Node`，此前`pages`等元数据并未在此处作为字段传入；标题仍可能存在于文本中。仅凭这段实现不能把索引里的chunk视为已验证的单一真实来源切块，也不能排除项目其他代码有额外信息。
- [检索代码](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/reflect_retrieval.py#L90-L174)的实体、句子和摘要入口各自沿节点关联映射到chunk，并为命中chunk累加计数后排序。一次实体或摘要入口可能关联多个chunk，但“多个入口投同一chunk一票”不等于“同一源的多个不同chunk针对同一查询共同召回”。[迭代代码](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/reflect_retrieval.py#L203-L309)最多进行四轮，在当前代码中按文本去重、反思后续查询，并对跨轮结果做RRF融合。以上是此固定版本的静态行为，不证明其与正式论文所有实验一一对应。
- **评估分母边界**：归档中的`musique.jsonl`、`wiki.jsonl`和`hotpot.jsonl`各有1,000行；这是归档文件的行数，不是已确认的论文测试集分母。[MuSiQue评估脚本](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/evaluate/evaluate_musique.py#L117-L150)对读入结果列表逐例累计EM/F1，再除以`len(qa_pairs)`；[2Wiki脚本](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/evaluate/evaluate_2wiki.py#L85-L98)也按结果列表长度平均。当前[检索示例](https://github.com/zhgao0729/MCORE/blob/bd7aec1b74dd83eb56d7dfa9da70bf3adfcb97d8/reflect_retrieval.py#L415-L460)使用`data[757:]`；若实际输入恰好为归档中1000行且全部成功执行，候选数才是243。这是条件推算，不能用作论文表格分母。
- **运行边界**：README给出命令行示例，但所检查的构建、检索和评估脚本含硬编码路径，不能仅凭README判断这些参数会被正确处理。未安装依赖、运行任何模型或验证论文数值，也未审计全部文件；ACM页面的Artifacts Available徽章本身不是本次复现证明。

## 对开题A/B的暂定参考价值

| 问题 | 目前可支持的判断 | 尚需论文全文或新实验确认 |
|---|---|---|
| **A：真实源经切块形成的同源多片，在同一查询共同召回；逐片及联合删除检验必要性** | 这是**多粒度检索机制近邻**：入口关联和反思式补检可供设计多片召回基线、记录入口到chunk的命中路径。代码中摘要节点可关联多个chunk，但各chunk的来源与关系仍需另行核实。 | 摘要和已检查代码没有证明同一真实源经目标chunker得到的不同互补块在同一查询共同入选，也没有给出逐块/联合删除对答案的因果必要性。不能将多入口命中同块、或单入口关联多块，直接认定为A的完整证据。是否存在更具体的论文实验，待逐页阅读。 |
| **B：证据检测、来源可信、干净查询误删和正常效用** | 常规多跳QA的EM/F1和多轮检索开销是正常效用评估的候选维度；应与最终保留的证据集合及查询级结果联合观察。 | 目前未见恶意证据检测、来源认证、干净查询误删或防御阈值校准的直接证据；尚不能据未读全文断言论文完全没有相关内容。QA准确率和标记块级指标均不能替代干净查询级误删率或来源可信。 |

## 作者稿与机构仓储检索

- **arXiv**：在其官方搜索中分别查询完整题名片段、题名`MCoRe`、DOI及短语`Reflection-Guided Iteration`，均未返回该文；按第一作者姓名查询亦未命中。导出API请求超时。结果只说明这些查询当时未找到，不能证明不存在不同题名或未被索引的作者稿。
- **作者主页和ResearchGate**：合作者[Tao Duan主页](https://toduan.github.io/)给出同一完整题名与作者名单，所设Paper链接指向ResearchGate条目。该条目的搜索索引显示暂无公开全文，但该索引可能滞后；本次对ResearchGate页面的直接请求返回403，无法独立核实其实时文件状态，也未向作者发送请求。
- **机构知识库**：在标识为西安交通大学机构知识库的学者导航中，检查[Juxiang ZENG的10条可见成果](https://ir.specialsci.cn/xajt/scholar/result?scholar=c8e70d3bbd55299f%3AJuxiang%20ZENG)及[Tao DUAN的1条可见成果](https://ir.specialsci.cn/xajt/scholar/result?scholar=7e7ab1c27fcf82f8%3ATao%20DUAN)，未见本篇；同名作者消歧、其他作者及该库全部记录未被穷尽，不能据此断言机构库不存在副本。
- **聚合索引及归档**：[OpenAlex](https://api.openalex.org/works/W7197015838)仅列出出版版本的DOI落地页，`pdf_url`为空，且未报告有机构仓储全文；[OpenAIRE DOI查询](https://api.openaire.eu/search/publications?doi=10.1145%2F3770855.3818043&format=json)仅返回由Crossref汇聚的DOI链接；DBLP列出的Unpaywall入口经oadoi重定向到同一ACM DOI，并未给出另一作者稿。[Zenodo 20441360的DataCite登记](https://api.datacite.org/dois/10.5281/zenodo.20441360)是软件版本`v1.0.0.0`，不是论文PDF；归档内容与校验范围见上文。CORE检索接口本次返回服务错误，不能把它当作“无全文”证据。
- **与ACM的关系**：上述作者主页的题名和作者顺序与ACM出版记录一致；未取得可核验的另一论文文本，故无法比较作者稿和正式出版稿的内容、版本差异或哈希。ACM正式论文页标记开放访问，但本环境下PDF请求停在真人验证；这是本次获取受阻的状态，不等同于论文需要付费。未获得合法可读全文，保留`L1 / pending-full-text`，不生成占位PDF，也不填写臆测的正文页码和实验分母。
## 待完成

取得合法正式PDF或作者稿后，记录其实际版本、文件大小、SHA-256和可核验的相对路径；逐页阅读并明确物理页与会刊页的对应关系；核表格中的基线、模型、每个数据集/指标的实际分母和平均方式；核对代码链接是否为论文作者指定版本，并根据正文再修订A/B映射。当前摘要中的提升幅度和代码样例行数都不能填补这些缺口。