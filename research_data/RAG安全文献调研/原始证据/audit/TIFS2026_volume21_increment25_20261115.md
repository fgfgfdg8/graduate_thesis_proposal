# TIFS 2026 第 21 卷：25 条目录增量证据

> 后续补证：此前 IEEE Xplore 机构会话导出的 2026-11-15 CSV 已复制留存，675 条与既有 650+25 身份记录的逐条对账见文末。下文此前关于完整导出尚未留存的表述反映当时的状态；官网 DOM 和浏览器下载过程仍未独立留存。

核查日期：2026-11-15（Asia/Shanghai）。本文件保存上一轮已完成的 IEEE 目录浏览、题名筛查及摘要核查的交接证据，并于本次持久化时重新对照本地旧快照和 Crossref。逐条机器可读数据见 [TIFS2026_volume21_increment25_20261115.jsonl](TIFS2026_volume21_increment25_20261115.jsonl)。此列表按旧池身份分组，**不是可独立证明的官网排序号**。

## 范围和口径

- IEEE 官方 [TIFS 第 21 卷目录](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=11313711&punumber=10206)：上一轮通过机构会话按 100 条一页浏览，报告 7 页依次为 100、100、100、100、100、100、75，共 675 个不同文章 ID；这是 2026-11-15 可见快照，不是全年最终目录。此前已保存的官方导出是 2026-11-02 的本机原始 CSV `../catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.02-08.20.47.csv` 与规范化记录 `../catalogs/catalog_tifs_browser_sources/normalized/TIFS_2026_articles.jsonl`；两份完整源文件含摘要且未纳入 Git。[650 条题名、DOI 与文章 ID 的精简快照](<TIFS2026_20261102_650_题名DOI快照.jsonl>)已随本记录保存，不包含摘要，其 SHA-256 为 `343cea64c17b89d9567195adfd8ae893b1f737840a9aa077c8182083a5295c3c`。既有本机审计为 `../catalogs/catalog_tifs_browser_sources/TIFS_2026_audit.json`。
- 上一轮报告当前目录前 650 ID 排序、LF 连接、无末尾 LF 的 SHA-256 为 `79de2a17bf2a9ced63bdb3415e4f63b4b5b4d7ee8e23f2e13aa62cac6799bed2`；本次对旧 650 ID 同法重算得到相同值。上轮报告的末尾 25 ID 同法 SHA-256 为 `fef0ce97cd72c31c2bcbe62781d71d680525ab3ffec78d5ace26188db491e503`，本次根据交接逐条重算一致。**当前目录 DOM/完整 ID 清单未落盘**，所以前 650 的官网端哈希是上轮浏览见证，不能说本文件独立保存了 675 条官网原始记录。
- 本机旧研究总池 `../catalogs/catalog_security_journals_sources/articles.jsonl` 中 17 条已存在，旧字段均为 `volume=null`、`scope=unassigned_early_access_or_volume_missing`；本机旧逐行登记对账 `local_catalog_registry_round235_20261106_sources/row_reconciliation.jsonl` 中对应 17 条均为 `no_exact_registered_match` 且阅读等级为空。这两份完整本机快照未纳入 Git，缺少时无法独立重放对旧池的不存在判断。其余 8 条在**这两个指定旧快照**里按 DOI、规范化完整题名和可用文章 ID 未找到；这不能证明在其他或更新记录中不存在。25 条均不在旧 650 条卷快照中，故本增量指**相对该卷快照新增的位置集合**，不是声称 25 篇首次发现或首次发表。旧池原题名、旧状态和一基行号均见 JSONL。
- [Crossref 无关键词日期窗查询](<https://api.crossref.org/journals/1556-6013/works?filter=from-pub-date%3A2026-01-01%2Cuntil-pub-date%3A2026-12-31&rows=1000&select=DOI%2Ctitle%2Cvolume%2Cissue%2Cpublished%2Ccreated%2CURL%2Ctype%2Clink%2Cpage%2Cauthor>) 以 `from-pub-date=2026-01-01,until-pub-date=2026-12-31`、`rows=1000` 获取：本次返回 729 条，`volume=21` 671 条，`volume` 缺失 58 条；671 条的 `issue` 均缺失。25 条的 DOI 经大小写规范化后与 Crossref 一致，题名逐字一致，记录链接的 `arnumber` 与 IEEE ID 全部匹配；这只是元数据链接核对，不代表 PDF 可用。
- 使用旧 650 加本次 25 构成的 675 DOI 集合对照 Crossref 的 671 条卷 21 集合：后者没有额外 DOI；前者多出 `10.1109/TIFS.2026.3677691`、`10.1109/TIFS.2026.3678080`、`10.1109/TIFS.2026.3678112`、`10.1109/TIFS.2026.3681434`。四条都在 Crossref 响应中，但其 `volume` 字段缺失。不得把其余缺卷号记录自动归入第 21 卷，也不得把缺卷号等同于 Early Access。

## 筛选与核查层级

题名宽筛词：`RAG`、`GraphRAG`、`retriev*`、`knowledge base`、`corpus`、`multi-hop`、`graph`、`reasoning`、`evidence`、`truth`、`provenance`、`context`、`poison*`、`backdoor`、`attack`、`detect*`、`trust`、`LLM`、`VLM`。大小写不敏感；直接命中统计使用 `RAG/GraphRAG/retriev*/knowledge base/corpus/multi-hop`，含词界、空格或连字符，25 条为 **0**。这只是题名层级筛选，不能据此排除摘要或全文中的相关内容。各行命中词见 JSONL。

上一轮实际查看 IEEE 官方完整摘要的仅 4 条，记本次 L1：`11740714`、`11740729`、`11740753`、`11776018`；其余 21 条仅核题名。没有把下载的元数据、摘要或标题核查记作 PDF 全文阅读。对前两篇，官网有 PDF 入口，但上轮浏览器 PDF 区域黑屏，直接 HTTP 请求返回 418，**未确认取得正式 PDF**；其余 23 篇未在该增量中检查 PDF。上述增量核查和 JSONL 保存的是上轮浏览观察的转录，该轮未保留 IEEE 页面 DOM、摘要原文、截图或 PDF；Crossref 当时的响应原件也未持久化。来源可变时只能按下面方法重新获取，不得将这里当成原始快照。

**2026-11-15 后续全文更新（现时状态）**：两篇后来通过机构授权取得 IEEE 正式 PDF 并阅读可提取文字，均为跨域背景，不是 RAG 安全直接先例。11740714 读物理页 1–13（印刷页 9666–9678），见 [Honeypot 逐篇笔记](../notes/20261115_TIFS_Honeypot_3744635_精读.md)；11740729 读物理页 1–14（印刷页 9636–9649），见 [Trusformer 逐篇笔记](../notes/20261115_TIFS_Trusformer_3744652_精读.md)。关键图表已目视核对，未逐格审计全部图表或复现实验。旧 JSONL 的 L1 字段仍记录原目录核查时点，不随此次全文阅读回写；本次对其余 23 条未新增全文阅读记录。上述黑屏、418 和当时未确认取得 PDF 保留为历史观察。

- `11740714` Honeypot：预训练语言模型分类任务的训练数据后门防御；可作为异常信号及样本降权的跨域方法邻近，不能称 RAG 恶意块检测。
- `11740729` Trusformer：用户信任图上的信任传播和路径推理；可作信任路径的跨域方法邻近，不能称多跳 RAG 投毒先例。
- `11740753` 为移动众包中对恶意聚合者的隐私感知真值发现，`11776018` 为针对 LLM/VLM 多层防护的攻击；目前只是摘要级线索，不应直接认定为 RAG 知识库投毒或检测。

下方涉及原始总池及对账文件的复核脚本需要本机完整快照；只取得 Git 中的精简快照时，可复核 650 条文章 ID 与 25 条增量，但不能重放旧总池的缺席判断。

## 25 条逐条索引

“旧池”仅指上述指定旧总池；“未发现”不表示其他旧记录均不存在。L1 表示原增量核查时查看了官方完整摘要；下表两条已追加后续全文状态，其余保持原核查层级。

| IEEE ID / 官方页 | 题名 | DOI | 旧池 | 原核查层级与已补的全文状态 |
|---|---|---|---|---|
| [11753684](https://ieeexplore.ieee.org/document/11753684/) | Micro Motion Aware for Deception Detection | [10.1109/TIFS.2026.3746871](https://doi.org/10.1109/TIFS.2026.3746871) | 已存在，旧未分卷 | 题名 |
| [11740734](https://ieeexplore.ieee.org/document/11740734/) | STEAD: Subversion-Resistant Portable Encrypted Data Deduplication With File Sharing | [10.1109/TIFS.2026.3744626](https://doi.org/10.1109/TIFS.2026.3744626) | 已存在，旧未分卷 | 题名 |
| [11753675](https://ieeexplore.ieee.org/document/11753675/) | Comments on “Server-Aided Public Key Authenticated Searchable Encryption With Constant Ciphertext and Constant Trapdoor” | [10.1109/TIFS.2026.3746876](https://doi.org/10.1109/TIFS.2026.3746876) | 已存在，旧未分卷 | 题名 |
| [11740746](https://ieeexplore.ieee.org/document/11740746/) | MRTracer: Toward Causally Faithful and Scalable Image Provenance Analysis | [10.1109/TIFS.2026.3744645](https://doi.org/10.1109/TIFS.2026.3744645) | 已存在，旧未分卷 | 题名 |
| [11753686](https://ieeexplore.ieee.org/document/11753686/) | WildDFDet: Robust Unsupervised DeepFake Detection in the Wild | [10.1109/TIFS.2026.3746866](https://doi.org/10.1109/TIFS.2026.3746866) | 已存在，旧未分卷 | 题名 |
| [11740701](https://ieeexplore.ieee.org/document/11740701/) | MBR-CLIP: Text Semantic-Guided Early Fusion Network for Multimodal Biometric Recognition | [10.1109/TIFS.2026.3744647](https://doi.org/10.1109/TIFS.2026.3744647) | 已存在，旧未分卷 | 题名 |
| [11740705](https://ieeexplore.ieee.org/document/11740705/) | Label-Aware Distribution-Based Dynamic Weighting Aggregation for Hierarchical Backdoor Defense in Federated Learning | [10.1109/TIFS.2026.3744651](https://doi.org/10.1109/TIFS.2026.3744651) | 已存在，旧未分卷 | 题名 |
| [11695227](https://ieeexplore.ieee.org/document/11695227/) | CAN-SHIELD: A Sensitive Hierarchical Intelligent Encryption and Layered Defense Mechanism for In-Vehicle CAN Systems | [10.1109/TIFS.2026.3734784](https://doi.org/10.1109/TIFS.2026.3734784) | 已存在，旧未分卷 | 题名 |
| [11740753](https://ieeexplore.ieee.org/document/11740753/) | Robust Privacy-Aware Truth Discovery Against Malicious Aggregators in Mobile Crowdsourcing | [10.1109/TIFS.2026.3744650](https://doi.org/10.1109/TIFS.2026.3744650) | 已存在，旧未分卷 | L1 官方摘要 |
| [11740749](https://ieeexplore.ieee.org/document/11740749/) | Publicly Verifiable Homomorphic Secret Sharing With Context and Result Hiding | [10.1109/TIFS.2026.3744639](https://doi.org/10.1109/TIFS.2026.3744639) | 已存在，旧未分卷 | 题名 |
| [11740697](https://ieeexplore.ieee.org/document/11740697/) | DualGuard: An Adaptive Detection Framework for Concurrent Malicious and Normality Drifts in Network Traffic | [10.1109/TIFS.2026.3744632](https://doi.org/10.1109/TIFS.2026.3744632) | 已存在，旧未分卷 | 题名 |
| [11740729](https://ieeexplore.ieee.org/document/11740729/) | Trusformer: Assessing Trust via Reasoning Like a Transformer | [10.1109/TIFS.2026.3744652](https://doi.org/10.1109/TIFS.2026.3744652) | 已存在，旧未分卷 | L1 官方摘要 → 正式全文逐页阅读（PDF 1–14；[笔记](../notes/20261115_TIFS_Trusformer_3744652_精读.md)） |
| [11740728](https://ieeexplore.ieee.org/document/11740728/) | LuTBA: Lightweight and Updatable Touch-Based Authentication Scheme for Mobile Devices | [10.1109/TIFS.2026.3744613](https://doi.org/10.1109/TIFS.2026.3744613) | 已存在，旧未分卷 | 题名 |
| [11740714](https://ieeexplore.ieee.org/document/11740714/) | Multi-Layer Honeypot Framework for Defending Pre-Trained Language Models Against Backdoor Attacks in Classification Tasks | [10.1109/TIFS.2026.3744635](https://doi.org/10.1109/TIFS.2026.3744635) | 已存在，旧未分卷 | L1 官方摘要 → 正式全文逐页阅读（PDF 1–13；[笔记](../notes/20261115_TIFS_Honeypot_3744635_精读.md)） |
| [11740716](https://ieeexplore.ieee.org/document/11740716/) | The Role of Information Incompleteness in Defending Against Stealth Attacks | [10.1109/TIFS.2026.3744641](https://doi.org/10.1109/TIFS.2026.3744641) | 已存在，旧未分卷 | 题名 |
| [11753674](https://ieeexplore.ieee.org/document/11753674/) | A Two-Stage Robust Reversible Image Watermarking Scheme Using 2D Lattice QIM With Quantization Strips | [10.1109/TIFS.2026.3746868](https://doi.org/10.1109/TIFS.2026.3746868) | 已存在，旧未分卷 | 题名 |
| [11753627](https://ieeexplore.ieee.org/document/11753627/) | Printed Electronics-Based Optical Unclonable Label for Artificial Intelligence Authentication | [10.1109/TIFS.2026.3746874](https://doi.org/10.1109/TIFS.2026.3746874) | 已存在，旧未分卷 | 题名 |
| [11775888](https://ieeexplore.ieee.org/document/11775888/) | Fisher Information Limits of Satellite RF Fingerprint Identifiability for Authentication | [10.1109/TIFS.2026.3750742](https://doi.org/10.1109/TIFS.2026.3750742) | 未发现 | 题名 |
| [11775896](https://ieeexplore.ieee.org/document/11775896/) | Physical Adversarial Attack Against LiDAR-Based 3D Perception via 2D Patches | [10.1109/TIFS.2026.3750721](https://doi.org/10.1109/TIFS.2026.3750721) | 未发现 | 题名 |
| [11775904](https://ieeexplore.ieee.org/document/11775904/) | GameRLFed: Robust Federated Learning Against Evolving Backdoor Attacks via Game Theory and Deep Reinforcement Learning | [10.1109/TIFS.2026.3750691](https://doi.org/10.1109/TIFS.2026.3750691) | 未发现 | 题名 |
| [11776018](https://ieeexplore.ieee.org/document/11776018/) | Tokens in Disarray: A Unified Adversarial Attack Against Multi-Layered Safeguards in LLMs and VLMs | [10.1109/TIFS.2026.3750686](https://doi.org/10.1109/TIFS.2026.3750686) | 未发现 | L1 官方摘要 |
| [11775907](https://ieeexplore.ieee.org/document/11775907/) | OceanWhisper: A Covert Communication Scheme for Time-Varying Underwater Acoustic Channels | [10.1109/TIFS.2026.3750752](https://doi.org/10.1109/TIFS.2026.3750752) | 未发现 | 题名 |
| [11775887](https://ieeexplore.ieee.org/document/11775887/) | Federated Quantum Learning With Adaptive Differential Privacy via Quantum Noise | [10.1109/TIFS.2026.3750716](https://doi.org/10.1109/TIFS.2026.3750716) | 未发现 | 题名 |
| [11775891](https://ieeexplore.ieee.org/document/11775891/) | Open-Set X-Ray Prohibited Item Detection via Uncertainty-Aware Unknown Discovery and Positive-Negative Prototype Learning | [10.1109/TIFS.2026.3750758](https://doi.org/10.1109/TIFS.2026.3750758) | 未发现 | 题名 |
| [11775895](https://ieeexplore.ieee.org/document/11775895/) | Road Network-Aware Personalized Trajectory Protection With Differential Privacy Under Spatiotemporal Correlations | [10.1109/TIFS.2026.3750736](https://doi.org/10.1109/TIFS.2026.3750736) | 未发现 | 题名 |

## 现有来源完整性

下列 SHA-256 为 2026-11-15 本次本地读取的文件**原始字节**哈希，不是上面的 ID 集合哈希。源路径以项目根目录为基准。

| 来源 | SHA-256 |
|---|---|
| 原始 IEEE CSV `export2026.11.02-08.20.47.csv` | `d194a48dfeef4369b146f9c01ca41c361ccad8f351c6e96fb6143939f24beacc` |
| 旧 650 条规范化 `TIFS_2026_articles.jsonl` | `7eaf057ecf35b3e95ec10b044ac11da914b093d577defdb6e4105b72f8802045` |
| 旧总池 `articles.jsonl` | `4f3ef3f6d682c763a07f4b1c298cf4af8c60275f86f0865f47705e88ccc0a015` |
| 旧登记对账 `row_reconciliation.jsonl` | `dc24d80cef79486df7df0afc802a9e55a228b22867fdedf19e5376160efcbdf7` |

## 可复核方法和剩余缺口

1. 在机构会话打开上面的 IEEE 目录，设置每页 100 条，逐页记录当时总数及每条文章 ID；官方目录会继续更新，应标注访问日期，再将该列表与 2026-11-02 旧 650 ID 比较。不得把后续新增归入本次快照。
2. 以下只读脚本在本文件所在 `audit` 目录执行，核对本地 25 条、650 条、去重、旧池及旧登记行号、17/8、4/21 和两组 ID 集合哈希。行号为一基物理行号。

```powershell
@'
from pathlib import Path
import hashlib, json, re, unicodedata

def load(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()]
def normdoi(s):
    return (s or '').lower().replace('https://doi.org/', '').strip()
def normtitle(s):
    return re.sub(r'[\W_]+', '', unicodedata.normalize('NFKC', s or '').casefold())
def sethash(values):
    return hashlib.sha256('\n'.join(sorted(values)).encode('utf-8')).hexdigest()

e = load(Path('TIFS2026_volume21_increment25_20261115.jsonl'))
old = load(Path('../catalogs/catalog_tifs_browser_sources/normalized/TIFS_2026_articles.jsonl'))
pool = load(Path('../catalogs/catalog_security_journals_sources/articles.jsonl'))
reg = load(Path('local_catalog_registry_round235_20261106_sources/row_reconciliation.jsonl'))
ids, old_ids = [x['ieee_article_id'] for x in e], [str(x['ieee_article_id']) for x in old]
assert len(e) == len(set(ids)) == len({normdoi(x['doi']) for x in e}) == 25
assert len(old) == len(set(old_ids)) == 650 and not (set(ids) & set(old_ids))
assert sethash(ids) == 'fef0ce97cd72c31c2bcbe62781d71d680525ab3ffec78d5ace26188db491e503'
assert sethash(old_ids) == '79de2a17bf2a9ced63bdb3415e4f63b4b5b4d7ee8e23f2e13aa62cac6799bed2'
for x in e:
    p, q = x['previous_general_pool'], x['previous_registry_reconciliation']
    if p['line'] is not None:
        assert normdoi(pool[p['line']-1]['doi']) == normdoi(x['doi'])
        assert pool[p['line']-1]['volume'] is None
        assert normdoi(reg[q['line']-1]['doi']) == normdoi(x['doi'])
        assert reg[q['line']-1]['status'] == 'no_exact_registered_match'
    else:
        assert q['line'] is None
        assert not any(normdoi(y.get('doi')) == normdoi(x['doi']) or normtitle(y.get('title')) == normtitle(x['title']) or '/document/' + x['ieee_article_id'] in (y.get('source_url') or '') for y in pool)
        assert not any(normdoi(y.get('doi')) == normdoi(x['doi']) or normtitle(y.get('title')) == normtitle(x['title']) or str(y.get('article_id') or '') == x['ieee_article_id'] for y in reg)
assert sum(x['previous_general_pool']['line'] is not None for x in e) == 17
assert sum(x['incremental_check']['official_abstract_checked'] for x in e) == 4
print('PASS: 25 unique; old 650; prior pool 17/8; abstract 4/21; hashes and source rows')
'@ | python -
```

3. 再运行上述 Crossref 查询；核对 `total-results`、实际返回条数、每条 `volume` 和 `issue`，用 DOI 去重，25 条用 `link` 中的 `arnumber` 和题名交叉核对。响应可能更新，计数不应被当成永久不变量。过去曾出现 429，稍后重试成功；官方 PDF 直连和查看器失败见上文，不能推断不存在 PDF。
4. 其余21条已补读官方完整摘要，详见[逐篇筛查](<TIFS2026_volume21_20261115_未读摘要补筛.md>)；连同原先4条，25/25摘要均已筛。尚缺官网675条原始响应/截图的持久副本、除上述两篇以外相关候选的全文精读、2026-11-15之后新分配卷记录以及旧池以外的全面排重；此记录不覆盖其他期刊或年度。

原增量任务的写入边界（历史）：当时仅创建本说明及同目录的 25 条 JSONL。任务开始后、任何交付文件写入前观察到三份主文档的哈希发生并行变化；本任务未对它们或 citation.bib 写入，也未回滚已有改动。

2026-11-15 后续全文更新写入边界：仅新增上述两篇独立笔记并就地更新本说明；未改动原 25 条 JSONL、三份主文档或 citation.bib，未操作 Git。机构授权 PDF 保留在指定本地论文库。


## 2026-11-15 后续补证：675 条导出与既有快照逐条对账

### 来源与完整性

- 原始导出：`D:\Downloads\export2026.11.15-01.04.15.csv`；按不覆盖方式复制至 [`../catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.15-01.04.15.csv`](../catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.15-01.04.15.csv)。原文件复制前、复制后和目标副本的原始字节 SHA-256 均为 `a2b5a06f11bae750a8ef2c7cc074898eabcbd34196ba7a4be0d045cd42905154`。该 CSV 含摘要，依现有 Git 忽略规则本机留存，未强制加入 Git。
- 650 条身份快照：[`TIFS2026_20261102_650_题名DOI快照.jsonl`](TIFS2026_20261102_650_题名DOI快照.jsonl)，原始字节 SHA-256 `343cea64c17b89d9567195adfd8ae893b1f737840a9aa077c8182083a5295c3c`；对应的 [2026-11-02 原始导出](../catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.02-08.20.47.csv) SHA-256 `d194a48dfeef4369b146f9c01ca41c361ccad8f351c6e96fb6143939f24beacc`。
- 25 条增量身份记录：[`TIFS2026_volume21_increment25_20261115.jsonl`](TIFS2026_volume21_increment25_20261115.jsonl)，原始字节 SHA-256 `34953b6066937c860d857f9b936161c85db9573b54c4c1f79dfef0d7b7e6b149`。这两份 JSONL 均为 Git 中已有的无摘要身份证据；两者合并即覆盖本次 675 条，不再另造重复精简清单。

### 对账结果与差异

- 2026-11-15 CSV 用 CSV 解析器读取到 **675 条数据记录**：675 个非空且唯一的 IEEE article ID、675 个非空且大小写规范化后唯一的 DOI、675 个非空且经 NFKC/空白/大小写规范化后唯一的题名；所有记录的出版物为 IEEE Transactions on Information Forensics and Security、年份为 2026、卷号为 21，`Issue` 均为空。675 个 PDF Link 均为 `https://ieeexplore.ieee.org/stamp/stamp.jsp`，且各含一个数字 `arnumber`。
- 650 条 JSONL 对其原始 CSV：ID 交集 650、双方独有 0；题名逐字一致 650/650、DOI 经去除首尾空白及大小写折叠后一致 650/650。650 条快照 DOI 全为小写、原始 CSV DOI 使用大写 `TIFS`，因此 DOI 原始字符串相等为 0/650；这是大小写表示差异，不是 DOI 身份差异。
- 新 CSV 对 650 条快照：ID 交集 650，快照独有 0、新 CSV 独有 25；650 条题名逐字一致、DOI 规范化后一致。新旧两份 CSV 共有的 650 条 ID、原始 DOI、题名逐字一致，且新 CSV 的前 650 条 ID 与旧 CSV 的顺序完全一致。
- 新 CSV 对 25 条记录：ID 交集 25，增量记录独有 0、新 CSV 独有 650；25 条题名和 DOI 原始字符串均逐字一致。650 与 25 的 ID 交集、规范化 DOI 交集均为 0；两份快照合并后与新 CSV 的 ID 集合、逐 ID DOI 和逐 ID 题名分别为 **675/675 一致，无缺失或额外记录、无 DOI 或题名差异**。两份既有记录的 675 条官方文章链接均与各自 article ID 一致；链接是由 ID 形成的 IEEE `/document/<ID>/` 地址，不代表本次访问了每个页面或验证 PDF 可用性。
- 排列差异：新 CSV 后 25 条与增量 JSONL 的 **ID 集合相同，顺序并不完全相同**。相对位置 17 和 18（CSV 逻辑数据记录 #667 和 #668）依次为 `11775888`、`11753627`；25 条 JSONL 的相同位置依次为 `11753627`、`11775888`。其余 23 个对应位置相同。上文已说明增量 JSONL 按旧池身份分组，不应把它的行号视为官网排序。
- 各 ID 按字符串升序、以 LF 连接且末尾不加 LF 后取 SHA-256：旧 650 为 `79de2a17bf2a9ced63bdb3415e4f63b4b5b4d7ee8e23f2e13aa62cac6799bed2`；增量 25 为 `fef0ce97cd72c31c2bcbe62781d71d680525ab3ffec78d5ace26188db491e503`；新 CSV 675 为 `a6d1a631516f27bc07edcadfafbcae060bb08aa8d5f182118122eff14dba82a9`。这是 ID 集合哈希，不是文件字节哈希，也不包含排序顺序。

### 匹配方法与复现

使用 UTF-8 BOM 容忍模式和标准 CSV 解析器按逻辑记录读取；从 IEEE `PDF Link` 的唯一 `arnumber` 参数提取数字 ID，与两个 JSONL 中 `ieee_article_id` 做一对一精确联结，先检查空值及重复，再做集合差。按同一 ID 独立对照 DOI（`strip().casefold()`）和题名原始 Unicode 字符串；另外计算题名 NFKC、连续空白合并和大小写折叠后的唯一数。未用模糊题名代替 ID 或 DOI，未丢弃标点，也未把 ID 集合相等当作 DOI/题名相等的证明。

在项目根目录执行以下 PowerShell；脚本只读取上述文件、打印逐项统计、相对旧快照的新增 ID 及全部规范化 DOI/逐字题名差异，失败时停止。`data_record` 是不含表头的 CSV 逻辑数据记录序号，不是可能受引号和换行影响的物理文件行号。

```powershell
$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = 'utf-8'
@'
import csv, hashlib, json, re, unicodedata
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

base = Path('research_data/RAG安全文献调研/原始证据')
new_path = base / 'catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.15-01.04.15.csv'
old_path = base / 'catalogs/catalog_tifs_browser_sources/raw_csv/export2026.11.02-08.20.47.csv'
snap_path = base / 'audit/TIFS2026_20261102_650_题名DOI快照.jsonl'
inc_path = base / 'audit/TIFS2026_volume21_increment25_20261115.jsonl'
files = [(new_path, 'a2b5a06f11bae750a8ef2c7cc074898eabcbd34196ba7a4be0d045cd42905154'),
         (old_path, 'd194a48dfeef4369b146f9c01ca41c361ccad8f351c6e96fb6143939f24beacc'),
         (snap_path, '343cea64c17b89d9567195adfd8ae893b1f737840a9aa077c8182083a5295c3c'),
         (inc_path, '34953b6066937c860d857f9b936161c85db9573b54c4c1f79dfef0d7b7e6b149')]
for path, expected in files:
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    print('SHA256', path, actual)
    assert actual == expected, path

def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))
def read_jsonl(path):
    with path.open(encoding='utf-8-sig') as f:
        return [json.loads(line) for line in f if line.strip()]
def extract_id(row):
    u = urlsplit(row['PDF Link'])
    ids = parse_qs(u.query).get('arnumber', [])
    assert u.scheme == 'https' and u.hostname == 'ieeexplore.ieee.org'
    assert u.path == '/stamp/stamp.jsp' and len(ids) == 1 and re.fullmatch(r'\d+', ids[0])
    return ids[0]
def from_csv(row):
    return {'id': extract_id(row), 'doi': row['DOI'], 'title': row['Document Title']}
def from_snapshot(row):
    article_id = str(row['ieee_article_id'])
    link = row.get('official_article_url', row.get('article_url_derived_from_pdf_link'))
    assert link == f'https://ieeexplore.ieee.org/document/{article_id}/'
    return {'id': article_id, 'doi': row['doi'], 'title': row['title']}
def doi(s):
    return s.strip().casefold()
def title_key(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip().casefold()
def id_hash(rows):
    return hashlib.sha256('\n'.join(sorted(x['id'] for x in rows)).encode('utf-8')).hexdigest()
def check_rows(label, rows, expected):
    assert len(rows) == expected
    assert all(x['id'] and doi(x['doi']) and x['title'].strip() for x in rows)
    assert len({x['id'] for x in rows}) == expected
    assert len({doi(x['doi']) for x in rows}) == expected
    print('ROWS', label, expected, 'id_hash', id_hash(rows))
def compare(label, left, right):
    a = {x['id']: x for x in left}
    b = {x['id']: x for x in right}
    shared = a.keys() & b.keys()
    doi_diff = [{'id': k, 'left': a[k]['doi'], 'right': b[k]['doi']}
                for k in sorted(shared) if doi(a[k]['doi']) != doi(b[k]['doi'])]
    title_diff = [{'id': k, 'left': a[k]['title'], 'right': b[k]['title']}
                  for k in sorted(shared) if a[k]['title'] != b[k]['title']]
    print('COMPARE', label, json.dumps({
        'shared': len(shared), 'left_only': len(a.keys() - b.keys()),
        'right_only': len(b.keys() - a.keys()),
        'doi_raw_equal': sum(a[k]['doi'] == b[k]['doi'] for k in shared),
        'doi_normalized_equal': len(shared) - len(doi_diff),
        'title_raw_equal': len(shared) - len(title_diff),
        'doi_differences': doi_diff, 'title_differences': title_diff}, ensure_ascii=False))
    assert not doi_diff and not title_diff
    return a.keys() - b.keys(), b.keys() - a.keys()

new_raw, old_raw = read_csv(new_path), read_csv(old_path)
new = [from_csv(x) for x in new_raw]
old = [from_csv(x) for x in old_raw]
snap = [from_snapshot(x) for x in read_jsonl(snap_path)]
inc = [from_snapshot(x) for x in read_jsonl(inc_path)]
for label, rows, size in [('new_csv', new, 675), ('old_csv', old, 650),
                           ('snapshot650', snap, 650), ('increment25', inc, 25)]:
    check_rows(label, rows, size)
assert id_hash(new) == 'a6d1a631516f27bc07edcadfafbcae060bb08aa8d5f182118122eff14dba82a9'
assert id_hash(snap) == '79de2a17bf2a9ced63bdb3415e4f63b4b5b4d7ee8e23f2e13aa62cac6799bed2'
assert id_hash(inc) == 'fef0ce97cd72c31c2bcbe62781d71d680525ab3ffec78d5ace26188db491e503'
assert not ({x['id'] for x in snap} & {x['id'] for x in inc})
assert not ({doi(x['doi']) for x in snap} & {doi(x['doi']) for x in inc})
assert len({title_key(x['title']) for x in new}) == 675
assert all(x['Publication Title'] == 'IEEE Transactions on Information Forensics and Security'
           and x['Publication Year'] == '2026' and x['Volume'] == '21' and x['Issue'] == ''
           for x in new_raw)
assert compare('old_csv_vs_snapshot650', old, snap) == (set(), set())
added, missing = compare('new_csv_vs_old_csv', new, old)
print('ADDED_IDS_VS_OLD_CSV', json.dumps(sorted(added)))
assert not missing and added == {x['id'] for x in inc}
assert compare('new_csv_vs_snapshot650', new, snap)[1] == set()
assert compare('new_csv_vs_increment25', new, inc)[1] == set()
assert compare('new_csv_vs_snapshot_union', new, snap + inc) == (set(), set())
assert new[:650] == old  # ID, original DOI, title, and order
order_diff = [{'increment_position': j, 'data_record': 650 + j,
               'csv_id': a['id'], 'increment_id': b['id']}
              for j, (a, b) in enumerate(zip(new[650:], inc), 1) if a['id'] != b['id']]
print('INCREMENT_ORDER_DIFFERENCES', json.dumps(order_diff, ensure_ascii=False))
assert order_diff == [
    {'increment_position': 17, 'data_record': 667, 'csv_id': '11775888', 'increment_id': '11753627'},
    {'increment_position': 18, 'data_record': 668, 'csv_id': '11753627', 'increment_id': '11775888'}]
print('PASS: 675 identity records reconciled; no abstract or topic screening performed')
'@ | python -X utf8 -
```

本次对账以此前机构会话导出的CSV及本地历史证据为依据，未独立见证导出会话，也没有重新取得官网 DOM、网页截图或浏览器下载记录。本轮公开网页抓取该卷目录时返回 HTTP 418，未使用用户的机构认证会话，不能据此推断其机构访问状态；原始 CSV 的留存补齐了可重放的导出身份记录，但不替代官网 DOM 证据。未重新筛查这 650+25 条的题名或摘要。此结果只描述该次 675 条导出，不代表 2026 年全年、后续分卷或 issue 级目录闭合。
