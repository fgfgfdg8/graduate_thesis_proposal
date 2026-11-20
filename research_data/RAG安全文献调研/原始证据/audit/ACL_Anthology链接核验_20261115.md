# ACL Anthology 外链只读核验记录

- 核验日期：2026-11-15；最终文档快照核对时间：11:36:22（北京时间）。这是当次核验记录，不代表此后链接或文档状态。
- 范围：三份 RAG 主文档中的 ACL Anthology 外链；本次核验本身只读，未修改文档、创建临时文件或提交。核验期间三份文档曾被其他工作区操作更新；重新读取后 ACL URL 数量和用于核题的标题未变，以下统计对应最终快照。
- 官方数据：[ACL 全量 BibTeX](https://aclanthology.org/anthology.bib.gz)，文件标注生成于 2026-11-13，压缩文件 SHA-256：`7861b42a6f8b313cfd31d3e711658e161947fad771d96419a1e4205ae567f984`；[ACL 数据说明](https://aclanthology.org/faq/api/)列出官方 GitHub `data/xml` 元数据。数据在内存中读取和处理。

## 抽取与总量

扫描三份 Markdown 中以 HTTP(S) 表达的 ACL Anthology 地址，按 URL 边界分离表格竖线、引号及中文标点；排除 3 处仅作为检索词的 `site:aclanthology.org`。URL 出现次数包含重复引用，不同 URL 按抽取到的完整地址去重，论文 ID 去除页面、`.pdf`、`.bib` 后缀后归并。

| 文档 | URL 出现 | 不同 URL | 论文 ID |
|---|---:|---:|---:|
| [攻防技术手段总结报告](<../../../../docs/RAG安全文献攻防技术手段总结报告.md>) | 0 | 0 | 0 |
| [文献补查元数据](<../../../../docs/RAG安全文献补查元数据_20261102.md>) | 8,560 | 1,396 | 1,097 |
| [文献证据地图](<../../../../docs/RAG安全证据地图_20261102.md>) | 3,674 | 1,922 | 1,126 |
| 合并去重 | 12,234 | 2,186 | 1,137 |

2,186 个不同 URL 分为论文页 1,137、PDF 784、BibTeX 248、目录／活动／版权页 17；对应出现次数依次为 10,026、1,326、354、528。跨文档存在重复，不能将各文档的去重数直接相加。

## ID、题名和链接类型

- 将论文 ID 与全量 BibTeX 的官方 URL 索引比对：**1,137 个 ID 均存在于 2026-11-13 快照**。从可辨识的链接文字、元数据表格行及论文笔记标题提取题名，对大小写、标点、Unicode 和 BibTeX/LaTeX 格式做适度归一化，并复核差异候选。自动比较覆盖 1,126 个 ID；另 10 个按相邻论文标题核对，1 个按文中简称 AGEA 与官方论文页核对。未发现可确认的错连论文。`PDF`、`公开PDF` 等通用显示名称不作为论文题名。
- 证据地图中识别出的 866 组相邻论文页／PDF 配对，ID 均一致。识别出的 40 个以论文 ID 作显示名称的链接，其显示 ID 与目标 ID 一致。
- 当前结论为：**未发现经核实的错误链接，故无同篇替代链接可列**；不是对全部 URL 在线可访问性或每次上下文关联正确性的保证。

## 抽测覆盖

- 对文档中出现的以下 12 个 PDF 地址发送低并发 HEAD 请求，均返回 HTTP 200、`application/pdf`；未逐一请求 784 个不同 PDF，HEAD 也不验证完整文件内容。以下均为 `https://aclanthology.org/<ID>.pdf`：`2024.findings-emnlp.500`、`2026.findings-acl.899`、`2024.acl-long.59`、`2026.findings-emnlp.1644`、`2024.findings-acl.668`、`2025.emnlp-main.1765`、`2024.acl-short.35`、`2026.emnlp-industry.252`、`2026.emnlp-main.2158`、`2026.findings-acl.1733`、`2026.findings-emnlp.1604`、`2026.findings-emnlp.507`。
- 17 个不同目录／活动／版权地址全部低并发 HEAD，均返回 200：12 个卷目录、4 个活动页、1 个版权页。其余单篇论文页和 BibTeX 地址未逐个做 HTTP 检测。

## Refiner 题名异写

[官方论文页](https://aclanthology.org/2024.findings-emnlp.500/)元数据为 *Refiner: Restructure Retrieved Content Efficiently to Advance Question-Answering Capabilities*；同一 ID 的[官方 PDF](https://aclanthology.org/2024.findings-emnlp.500.pdf)首页为 *Restructure Retrieval Content Efficiently to Advance Question-Answering Capabilities*。这是同篇的官方来源异写，非错链；[证据地图第 11546 行](<../../../../docs/RAG安全证据地图_20261102.md#src-51c725d07a326183-h1>)已有记录。

## 未覆盖边界

- **431 次论文相关 URL 出现**未能通过自动规则安全绑定到该处题名；其 ID 可能在文档其他位置或人工补核中已完成一次题名匹配，但不能因此断言这 431 次上下文均正确。抽取到的其余题名关联也不是逐条人工阅读全部 12,234 次出现。
- 批量目录证明的是快照中存在对应 ID 和书目记录，不保证每个页面、PDF 或 BibTeX 端点当下可访问；目录不存在亦不能单独证明快照生成后出现的论文无效。不能把访问失败直接判为死链。
- 不覆盖拼错的域名、未识别的相对地址、其他网站和 DOI 外链；目录页、活动页与单篇论文页分别计数。

## 最终文档快照 SHA-256

- 攻防技术手段总结报告：`437e6ca9352cdc17fe679be77181a872b6b3b169c6630bc14f95b38a0223424e`
- 文献补查元数据：`39f4c0d0dc95632e560258267eff5e83630fd3a9490d8ca1e255173ab6f72c7c`
- 文献证据地图：`92eb75f9072fd9b4bbd80ce203bd612e8dad102cc2701425801d2f9a660277ff`
