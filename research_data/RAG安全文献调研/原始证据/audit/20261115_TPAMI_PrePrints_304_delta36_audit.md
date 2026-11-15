# TPAMI PrePrints 旧304 DOI差集36条：持久审计

## 快照与证据边界

- 继承的原始在线优先快照：2026-11-15 06:40:23 +08:00；该时刻 CSDL 的 TPAMI PrePrints 为 340 条、340 个唯一规范化 DOI。此前已完成这 36 个官方摘要的逐条筛查；本文件**沿用既有判断，未将本次元数据复核记为新的摘要筛查或正文阅读信用**。
- 差集口径：按 DOI 去首尾空格并转小写，当前 PrePrints 减去 2026-11-07 本地旧 304 条唯一 DOI；新增 36，旧集合移出 0。本次 2026-11-15 约 06:44 +08:00 重新取官方 PrePrints 后再次独立复算，仍为 340/340、差集 36、移出 0，36 条按当时 PrePrints 的原始顺序 #1–36 排列。旧 268、281 快照不能代替该 304 母集。
- **旧 304 的版本与本地来源**：2026-11-07 14:13:17–14:13:18 +08:00 的 CSDL PrePrints 响应体本机留存于 `tmp/rag_TPAMI2026_PrePrints_official_20261107_sources/http/preprints_current/response.body`，SHA-256 为 `bdafbf7cef138681275c7dd1562c005c28555c5dc2a662b39b9b24848116ef07`；逐条 JSON 解析后形成的本地原始行快照为 `../链接来源快照/84ff933d1605779d3b571bcdbc3a7d5d732deb878d2ae85fbfe8f4266ec0bfdb.jsonl`，304 行，文件 SHA-256 与文件名一致。逐项核对 `native`、顺序与 JSON pointer 均为 304/304 一致。304 行记录未记载自身的提取时刻；本机文件创建及最后写入时间均为 2026-11-14 22:27:19 +08:00，文件属性不单独证明提取时刻。原始响应体和原始行均含摘要，不是下列公开精简文件，也不保证随仓库分发。
- 重要：这 36 条是**整个在线优先池的新记录，不是 TPAMI 2026 vol.48 issue 12 的目录**；目前没有证据证明它们属于第 12 期，未来是否编入以及编入哪一期仍须等正式目录。记录中的 year=5555、volume=null、issueNum=01 为 PrePrints 原生占位字段，不应解读成 2026 年第 1 期或第 12 期。
- A 指“单一真实长源经实际分块、同 query 共同召回且逐块共同必要”；B 指“固定文本表征四统计、离线 RF、低误报与最终删块后的 QA 效用”。下表的排除仅表示原有摘要级 A/B 本轮纳入判断，不是证明论文没有价值。
- 来源与重放：官方 [TPAMI PrePrints 查询](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20preprints(idPrefix%3A%22tp%22)%20%7B%20id%20doi%20title%20abstract%20year%20volume%20issueNum%20pubDate%20fno%20authors%20%7B%20fullName%20%7D%20%7D%20%7D) 返回 `data.preprints`；逐条链接指向官方 CSDL 的 `articleByFno` JSON，其 `data.articleByFno.abstract` 字段为官方英文摘要完整原文。36 个 `articleByFno` 已在 2026-11-15 本次复核中与在线优先列表的 DOI、题名和摘要字段逐项一致。
- **摘要保存方式与原始时刻边界**：本审计正文提供官方入口、中文要点及 SHA-256；约 06:44 复核时的摘要哈希按 JSON 解析所得原生字符串的 UTF-8 字节计算，不额外解码 HTML 实体。最初 06:40 的 340 条响应正文及约 06:44 的响应正文均未固定保存，不能证明最初 06:40 的字段与之后一致，也不能重建这两个时刻的原始 HTTP 响应。下方 07:39 的重取快照保存了这 36 个摘要，且其字段哈希与已记录的 06:44 摘要哈希一致；它仍是后来重取的数据。
- 分类沿用上一轮：优先跨域候选 4 项（#15、#17、#25、#26），弱方法参考 4 项（#1、#11、#22、#28），其余 28 项不作为 A/B 直接候选；直接 RAG 安全近邻 0 项。#25、#26 的单篇正文阅读见本轮笔记，未把跨域候选升级为直接撞车。
- 独立摘要复核同样未发现直接RAG安全近邻，并认为#3、#5、#23可作为可选的低优先级跨域评价或对齐参考；它们仍不满足A/B直接候选条件，原有分类数量按首次筛查口径保留。#15、#17仍为待正文的跨域候选，不能按摘要认定方法或性能。

## 2026-11-15 07:39 官方重取与可复核源

- **请求与范围**：2026-11-15 07:39:34 +08:00 无登录凭据访问本文件上方的 IEEE CSDL 官方 TPAMI PrePrints GraphQL 查询，HTTP 200；返回 340 条、340 个唯一规范化 DOI。按 DOI 去首尾空格并转小写与旧 304 比较，新增 36、旧集移出 0；36 个目标 DOI 恰为该次差集。对照既有 #1–36，重取记录的 DOI、题名、fno 及摘要 SHA-256 均 36/36 一致。该观察不赋予任何记录 TPAMI 48(12) 归属。
- **本地原始重取快照**：`20261115_073934_TPAMI_PrePrints_refetch_delta36.jsonl`；UTF-8 无 BOM、LF 换行、36 行、84,090 字节，SHA-256：`86a8495f86ca2c6cb41f3a5cd71083131a0a13c7946d3036673c8c79321653eb`。它是 2026-11-15 07:39:34 +08:00 官方重取结果中的 36 条 JSON 字段重新序列化，保留摘要原文，不是 HTTP 响应字节原件或公开精简文件。36 行记录未记载自身的提取时刻；本机文件创建及最后写入时间均为 2026-11-15 07:42:59 +08:00，文件属性不单独证明提取时刻。
- **可公开分享的精简 304**：[20261107_TPAMI_PrePrints_304_public_metadata.jsonl](./20261107_TPAMI_PrePrints_304_public_metadata.jsonl)；304 行、124,349 字节；SHA-256：`9b6d2da869e25d201d0fe105be5e9cbc1789d8564b28c91f6d6ca3c4962a934a`。来源是上述 2026-11-07 本地 304 行原始快照。
- **可公开分享的精简 36**：[20261115_073934_TPAMI_PrePrints_delta36_public_metadata.jsonl](./20261115_073934_TPAMI_PrePrints_delta36_public_metadata.jsonl)；36 行、13,707 字节；SHA-256：`cd253e53dfe92f033b5b0f933b2fa8cb71c456bdff68014edb39d2ccac615857`。来源是上述 2026-11-15 07:39:34 本地 36 行原始重取快照。两份精简文件的提取时刻为 2026-11-15 08:08:42 +08:00；均为本地生成的 UTF-8 无 BOM、LF JSONL，并非两个时间点的原始 HTTP 字节。
- **精简字段及缺失语义**：仅保存规范 DOI（去首尾空格并转小写）、原题名、fno、原生 `year`/`volume`/`issueNum`/`pubDate`、源序号及摘要 SHA-256。旧 304 还保留原生 `periodicalIssueLabel`/`periodicalIssueVolume`；36 条查询未请求这两项，不虚填 null。旧集保留 `source_ordinal1`，新集保留 `audit_seq_0644` 和 `preprints_ordinal1_at_refetch`；原生占位字段不解释为正式卷期。摘要为 null 时 `abstract_is_null=true`、哈希为 null；旧集第 235 条是唯一 null，新集无 null，空字符串则按 UTF-8 空字节计算其哈希。未保留摘要原文、作者、HTTP 会话、邮箱或本机路径。
- **指纹边界**：非 null 摘要的 SHA-256 按 JSON 解析后的原生字符串 UTF-8 字节计算，不额外解码 HTML 实体。哈希只是摘要字段指纹，不含摘要或论文正文；仅凭精简文件不能重建或核实摘要原文，更不能核实论文正文。对照摘要原文须另有可核验的来源。
- **时点边界**：本地 36 条原始快照是 07:39 的重取与抽取，不是 06:40 或 06:44 的原始响应；字段哈希匹配不能证明从未保存的完整 HTTP 响应逐字节相同。06:40、06:44 和 07:39 的完整 340 条响应均未固定保存；“340/304/36、旧集移出 0”是当时在线观察。两份精简文件只保存旧 304 与新 36 的字段，虽可离线验证两组互不重叠及并集有 340 个 DOI，却不能仅凭它们证明该并集等于任一时点的完整在线响应或验证旧集移出为 0。
- **旧快照字节与 Git 策略**：旧 304 文件 938,893 字节、UTF-8 无 BOM、304 个 LF、0 个 CR，文件 SHA-256 与文件名一致。只读检查该路径生效的 Git 属性为 `text=auto`、`eol=lf`，`filter`、`working-tree-encoding`、`ident` 未指定，仓库 `core.autocrlf=false`。以当前内容分别运行不带过滤与按该路径应用 Git 过滤的 `git hash-object --stdin`，两者对象 ID 均为 `a07d65fdd8f6f1a2bf6e9cc411638d2bf7e8baf9`；因此在本机当前规则下这些字节不会被 Git 清洗转换。实际跟踪/提交另受忽略规则和未来配置影响。
- **敏感数据检查**：此前对旧快照和 36 条原始重取快照进行的模式扫描未发现非空 Cookie、认证、密码、API key、访问令牌、会话令牌或私钥字段，也未匹配常见凭据、Cookie 赋值、邮箱或 URL 内凭据。两份原始快照可含论文作者姓名和摘要；公开精简文件按固定字段白名单生成，不包含作者、摘要原文、HTTP 会话、邮箱或本机路径。模式扫描不能识别所有可能的敏感信息。

### 在本审计目录下复核

以下 PowerShell 片段只读取本审计文件与两份公开 JSONL，即可核对文件哈希、白名单、序号、摘要 null 标记、304/36 DOI 及文中 36 条元数据。默认在两份本地原始 JSONL 都存在时再逐条核对原始字段和摘要指纹，旧 304 响应体存在时继续验证响应体；缺少原件时明确跳过。只测公开文件可将最后的 `python -X utf8 -B -` 改为 `python -X utf8 -B - --public-only`；需要强制原始 JSONL 存在可改为 `python -X utf8 -B - --require-local-sources`。这些检查均不能补出未保存的 340 条完整响应。

```powershell
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
@'
import hashlib
import json
import re
import sys
from pathlib import Path

# 在本审计目录执行；默认可仅依赖本审计文档与两份公开 JSONL。
args = set(sys.argv[1:])
if args - {'--public-only', '--require-local-sources'} or len(args) > 1:
    raise SystemExit('用法：不带参数、--public-only 或 --require-local-sources')

def check(ok, message):
    if not ok:
        raise SystemExit('验证失败：' + message)

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def load_jsonl(path, expected_sha, count):
    check(path.is_file(), '缺少文件：' + path.name)
    data = path.read_bytes()
    check(sha256(data) == expected_sha, '文件 SHA-256 不匹配：' + path.name)
    check(not data.startswith(b'\xef\xbb\xbf') and b'\r' not in data and data.endswith(b'\n'),
          '需要 UTF-8 无 BOM、LF 和末尾换行：' + path.name)
    try:
        lines = data.decode('utf-8').splitlines()
        rows = [json.loads(line) for line in lines]
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit('JSONL 解析失败：' + path.name) from exc
    check(len(rows) == count, '行数不符：' + path.name)
    return rows

old_public = Path('20261107_TPAMI_PrePrints_304_public_metadata.jsonl')
new_public = Path('20261115_073934_TPAMI_PrePrints_delta36_public_metadata.jsonl')
old = load_jsonl(old_public, '9b6d2da869e25d201d0fe105be5e9cbc1789d8564b28c91f6d6ca3c4962a934a', 304)
new = load_jsonl(new_public, 'cd253e53dfe92f033b5b0f933b2fa8cb71c456bdff68014edb39d2ccac615857', 36)
common = {'doi', 'title', 'fno', 'year', 'volume', 'issueNum', 'pubDate',
          'abstract_is_null', 'abstract_sha256_utf8'}
old_fields = common | {'source_ordinal1', 'periodicalIssueLabel', 'periodicalIssueVolume'}
new_fields = common | {'audit_seq_0644', 'preprints_ordinal1_at_refetch'}
email = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.I)
local_path = re.compile(r'(?:^|[\s(="\x27])[A-Za-z]:(?:\\|/(?!/))')
http_data = re.compile(r'https?://|\b(?:set-cookie|authorization|access_token|api_key)\s*[:=]', re.I)

def validate_public(rows, fields, label):
    for pos, row in enumerate(rows, 1):
        check(isinstance(row, dict) and set(row) == fields, f'{label} #{pos} 字段白名单不符')
        doi, title, fno = row['doi'], row['title'], row['fno']
        check(isinstance(doi, str) and doi == doi.strip().lower() and
              re.fullmatch(r'10\.\d{4,9}/\S+', doi) is not None, f'{label} #{pos} DOI 不规范')
        check(isinstance(title, str) and bool(title.strip()) and isinstance(fno, str) and bool(fno.strip()),
              f'{label} #{pos} 题名或 fno 不完整')
        for key in fields & {'year', 'volume', 'issueNum', 'pubDate', 'periodicalIssueLabel', 'periodicalIssueVolume'}:
            check(row[key] is None or isinstance(row[key], str), f'{label} #{pos} 原生字段类型异常')
        check(type(row['abstract_is_null']) is bool, f'{label} #{pos} 摘要 null 标记类型异常')
        digest = row['abstract_sha256_utf8']
        check((row['abstract_is_null'] and digest is None) or
              (not row['abstract_is_null'] and isinstance(digest, str) and
               re.fullmatch(r'[0-9a-f]{64}', digest) is not None), f'{label} #{pos} 摘要指纹与 null 标记不一致')
        for value in row.values():
            if isinstance(value, str):
                check(not (email.search(value) or local_path.search(value) or http_data.search(value)),
                      f'{label} #{pos} 出现疑似邮箱、路径或会话信息')

validate_public(old, old_fields, '旧304')
validate_public(new, new_fields, '新36')
check([r['source_ordinal1'] for r in old] == list(range(1, 305)), '旧304 原始序号不连续')
check([r['audit_seq_0644'] for r in new] == list(range(1, 37)), '新36 审计序号不连续')
check(len({r['preprints_ordinal1_at_refetch'] for r in new}) == 36 and
      all(type(r['preprints_ordinal1_at_refetch']) is int and
          1 <= r['preprints_ordinal1_at_refetch'] <= 340 for r in new), '重取序号异常')
old_dois, new_dois = {r['doi'] for r in old}, {r['doi'] for r in new}
check(len(old_dois) == 304 and len(new_dois) == 36 and old_dois.isdisjoint(new_dois), 'DOI 重复或交集非空')
null_rows = [r['source_ordinal1'] for r in old if r['abstract_is_null']]
check(null_rows == [235] and not any(r['abstract_is_null'] for r in new), '空摘要数量或序号异常')

# 文档的既有 #1–36 记录提供另一组序号、题名、DOI、fno 和摘要指纹。
audit = Path('20261115_TPAMI_PrePrints_304_delta36_audit.md').read_text(encoding='utf-8')
parts = re.findall(r'(?ms)^### #(\d+) ([^\n]+)\n(.*?)(?=^### #\d+ |^## 正文阅读追踪|\Z)', audit)
expected = {}
for seq, title, body in parts:
    doi = re.search(r'DOI：([^；\s]+)', body)
    fno = re.search(r'IEEE fno：(\d+)', body)
    digest = re.search(r'官方摘要字段 SHA-256：\x60([0-9a-f]{64})\x60', body)
    check(bool(doi and fno and digest), f'审计正文 #{seq} 元数据不完整')
    check(int(seq) not in expected, '审计正文序号重复')
    expected[int(seq)] = (title.strip(), doi.group(1).strip().lower(), fno.group(1), digest.group(1))
check(set(expected) == set(range(1, 37)), '审计正文不是完整 #1–36')
for row in new:
    actual = (row['title'].strip(), row['doi'], row['fno'], row['abstract_sha256_utf8'])
    check(actual == expected[row['audit_seq_0644']], f'新36 与审计正文 #{row["audit_seq_0644"]} 不一致')
print('公开文件通过：304/36，DOI 唯一且互不重叠；null 摘要 1/0；36 条与审计正文一致。')
print('304+36=340 是两份持久文件的并集计数；不能证明它是当时的完整在线响应或旧集移出为 0。')

local_old = Path('../链接来源快照/84ff933d1605779d3b571bcdbc3a7d5d732deb878d2ae85fbfe8f4266ec0bfdb.jsonl')
local_new = Path('20261115_073934_TPAMI_PrePrints_refetch_delta36.jsonl')
old_response = Path('../../../../tmp/rag_TPAMI2026_PrePrints_official_20261107_sources/http/preprints_current/response.body')
if '--public-only' in args:
    print('公开文件模式：未读取本地原始快照；摘要指纹不能单独验证摘要或论文正文。')
elif local_old.is_file() and local_new.is_file():
    old_raw = load_jsonl(local_old, '84ff933d1605779d3b571bcdbc3a7d5d732deb878d2ae85fbfe8f4266ec0bfdb', 304)
    new_raw = load_jsonl(local_new, '86a8495f86ca2c6cb41f3a5cd71083131a0a13c7946d3036673c8c79321653eb', 36)

    def project(record, kind):
        native = record['native']
        abstract = native['abstract']
        check(abstract is None or isinstance(abstract, str), '原始摘要字段类型异常')
        digest = None if abstract is None else sha256(abstract.encode('utf-8'))
        row = ({'source_ordinal1': record['source_ordinal1']} if kind == 'old' else
               {'audit_seq_0644': record['audit_seq_0644'],
                'preprints_ordinal1_at_refetch': record['preprints_ordinal1_at_refetch']})
        row.update({key: native[key] for key in ('title', 'fno', 'year', 'volume', 'issueNum', 'pubDate')})
        row['doi'] = native['doi'].strip().lower()
        if kind == 'old':
            check(record['DOI_key'] == row['doi'], '旧快照 DOI_key 不一致')
            row.update({key: native[key] for key in ('periodicalIssueLabel', 'periodicalIssueVolume')})
        else:
            check(record['abstract_sha256_utf8'] == digest, '36 条原快照摘要指纹不一致')
        row['abstract_is_null'] = abstract is None
        row['abstract_sha256_utf8'] = digest
        return row

    check([project(r, 'old') for r in old_raw] == old, '旧304 公共字段与原快照不一致')
    check([project(r, 'new') for r in new_raw] == new, '新36 公共字段与原快照不一致')
    print('本地原始 JSONL 通过：304/304 和 36/36 公共字段及摘要指纹一致。')
    if old_response.is_file():
        response_bytes = old_response.read_bytes()
        check(sha256(response_bytes) == 'bdafbf7cef138681275c7dd1562c005c28555c5dc2a662b39b9b24848116ef07',
              '旧304 官方响应体 SHA-256 不匹配')
        response = json.loads(response_bytes.decode('utf-8'))['data']['preprints']
        check(len(response) == 304, '旧304 官方响应体行数不符')
        check(all(r['source_ordinal1'] == i and r['native'] == response[i - 1] and
                  r['source_JSON_pointer'] == f'/data/preprints/{i - 1}' and
                  r['source_body_SHA256'] == sha256(response_bytes) for i, r in enumerate(old_raw, 1)),
              '旧304 响应体与快照的来源关系不一致')
        print('本地旧304 官方响应体通过：304/304 原生记录及指针一致。')
    else:
        print('未提供旧304 官方响应体：跳过该层核验。')
else:
    check('--require-local-sources' not in args, '要求本地原始快照，但至少一份不存在')
    print('未同时提供本地原始快照：跳过来源逐字段核验；摘要指纹不能单独验证摘要或论文正文。')
print('摘要 SHA-256 仅为原生字符串 UTF-8 指纹，不提供摘要原文，也不验证论文正文。')
'@ | python -X utf8 -B -
if ($LASTEXITCODE -ne 0) { throw "离线验证失败（退出码 $LASTEXITCODE）" }
```
## 36 条原序记录

### #1 S2C2Seg++: Training-Free Category-Space Selection with Semantic-Spatial Fusion for Open-Vocabulary Segmentation

- DOI：10.1109/TPAMI.2026.3753590；IEEE fno：11794458；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211794458%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`75ea2efb7b7d9d54e7b1b7bc55a5524074359115be92310c5d34e7459dab304b`。
- 官方摘要要点（中文转述）：无需额外训练的语义分割，结合推理时类别子集选择与语义/空间预测融合。
- 既有 A/B 判断：**弱方法参考·B**。自适应候选筛选可作类比；未见 RAG 检索块安全判定或最终误删校准。

### #2 Generative Point Cloud Registration With Match-ControlNet

- DOI：10.1109/TPAMI.2026.3753622；IEEE fno：11794459；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211794459%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`a94d98facfa8c9d76eb108fefcec415bcc778d67e012677f375d8573d86fc7cb`。
- 官方摘要要点（中文转述）：利用可控二维生成模型构造跨视角一致图像，改进三维点云配准。
- 既有 A/B 判断：**排除 A/B 直接候选**。任务为几何配准，未见检索块共同必要或污染检测。

### #3 Image Quality Assessment for Machine-oriented Communication

- DOI：10.1109/TPAMI.2026.3748556；IEEE fno：11794943；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211794943%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`fb597b27993dcfee3e1ae932d3013eda9af2e49bfcd5aa34908134ab721b4807`。
- 官方摘要要点（中文转述）：研究面向机器通信的图像质量评价、失真数据与评估指标。
- 既有 A/B 判断：**排除 A/B 直接候选**。机器视觉传输质量不等于 RAG 安全/删块效用。

### #4 2D Gaussian Splatting for Semantic Segmentation via Discrete-to-Continuous Representation toward Boundary-Preserving Feature Upsampling

- DOI：10.1109/TPAMI.2026.3753018；IEEE fno：11793274；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793274%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`c6e733bf8ce3b0e0875afcee30526f51c890e3b37eb4d3875a7d7c846a5dbd21`。
- 官方摘要要点（中文转述）：用二维高斯表示及连续上采样改善语义分割边界。
- 既有 A/B 判断：**排除 A/B 直接候选**。目标是图像分割，非 A 的文本块或 B 的防御。

### #5 Person Recognition at Altitude and Range: Fusion of Face, Body Shape and Gait

- DOI：10.1109/TPAMI.2026.3752429；IEEE fno：11793295；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793295%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`7e8fecf669b765e7005c1bbdb956e6c0beb61bdd97e4621e821fd758e760efba`。
- 官方摘要要点（中文转述）：融合人脸、身体形状和步态以识别远距离人物。
- 既有 A/B 判断：**排除 A/B 直接候选**。生物识别任务，与 RAG 投毒及必要块筛查无直接对应。

### #6 Kernel Adaptive Deformable Convolution for Remote Sensing Object Detection

- DOI：10.1109/TPAMI.2026.3752695；IEEE fno：11793302；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793302%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`ae7e2e59af3bf3b1bc865074e16ca6f42f64d5e1012019be1fe7fb7b7d9fec9c`。
- 官方摘要要点（中文转述）：以核自适应可变形卷积改进遥感目标检测。
- 既有 A/B 判断：**排除 A/B 直接候选**。遥感图像目标检测，未见 RAG 安全对象。

### #7 A Simple but Efficient Method to Achieve High Performance with Extreme Sparsity

- DOI：10.1109/TPAMI.2026.3753244；IEEE fno：11793861；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793861%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`e09a3628facd9e012f595e30cafdc97f250487cc53b0056d7b6eeb5de423612e`。
- 官方摘要要点（中文转述）：研究高稀疏度下保持模型性能的网络稀疏化方法。
- 既有 A/B 判断：**排除 A/B 直接候选**。模型剪枝不是针对检索证据或攻击的筛查。

### #8 Seeing Text Clearly in the Dark: Unifying Localization and Enhancement via Deep Morphological Synergy

- DOI：10.1109/TPAMI.2026.3753279；IEEE fno：11793875；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793875%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`6e99e06246a8fd183998500445c34d566f0d130013472cbeece0e34668c0372c`。
- 官方摘要要点（中文转述）：联合暗光场景下文字定位和图像增强。
- 既有 A/B 判断：**排除 A/B 直接候选**。视觉文字定位并非 RAG 检索文本块的安全校验。

### #9 Representation of Directed Acyclic Graphs by Sequences of Instructions for Symbolic Regression

- DOI：10.1109/TPAMI.2026.3752551；IEEE fno：11793949；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793949%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`5d78945d75804125a3acc71c5042ea1c709578dfa3fbbb121089eb4dd6f3b341`。
- 官方摘要要点（中文转述）：为符号回归的有向无环表达式构造指令序列规范编码，减少重复搜索。
- 既有 A/B 判断：**排除 A/B 直接候选**。表达式图去重不对应检索块必要性或投毒检测。

### #10 TRUE: Towards Robust, Unique, and Efficient Model Fingerprint Generation and Verification

- DOI：10.1109/TPAMI.2026.3752300；IEEE fno：11790289；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211790289%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`f2181bfc617d612292e0dcd0900d338d866b61bdfc23d07a1b755a15561b5bc3`。
- 官方摘要要点（中文转述）：使用对抗样本生成和验证模型指纹，并优化鲁棒性、唯一性和验证开销。
- 既有 A/B 判断：**排除 A/B 直接候选**。这是模型知识产权指纹安全，非 RAG 证据攻击或过滤。

### #11 HPS-MVC: Hierarchical Pseudo-Supervised Multi-View Clustering

- DOI：10.1109/TPAMI.2026.3752120；IEEE fno：11790294；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211790294%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`a6a1dc7834d8d1f377a51dcab3c19a1e6e67bfbefd5f0a6ac59732b263e431f7`。
- 官方摘要要点（中文转述）：多视图聚类中以层级伪监督引导锚图融合，并对锚图加权。
- 既有 A/B 判断：**弱方法参考·B**。图融合权重可作方法类比；不验证污染块、误删或问答效果。

### #12 Contextual Chamfer Distance for Point Cloud Restoration

- DOI：10.1109/TPAMI.2026.3752196；IEEE fno：11790298；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211790298%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`7da3100afc8a61062a46ea5d8d2ce4a15c7daab81481f6b66a2df048c42352de`。
- 官方摘要要点（中文转述）：构造考虑局部密度和远程结构一致性的点云恢复距离。
- 既有 A/B 判断：**排除 A/B 直接候选**。几何重建一致性不是 RAG 证据关系安全。

### #13 Vector Map as Language: Toward Unified Remote Sensing Vector Mapping

- DOI：10.1109/TPAMI.2026.3752281；IEEE fno：11790302；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211790302%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`1af5b67ef23a769b1b7264b38aff47413f68bcccdce534fd276b7d616e027bde`。
- 官方摘要要点（中文转述）：将遥感图像到多类矢量地图转换为结构化文本生成。
- 既有 A/B 判断：**排除 A/B 直接候选**。虽然涉及语言和结构，目标是地理制图而非检索安全。

### #14 Bridging the Training Gap with Hyperion: A Training-Free Style Transfer Method on Diffusion Transformers

- DOI：10.1109/TPAMI.2026.3752263；IEEE fno：11790306；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211790306%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`5ba3b6c843a2283317cff803a3515c1af7490c1689c0111a824addecaad81069`。
- 官方摘要要点（中文转述）：冻结多模态扩散模型，通过潜变量优化和分布对齐实现风格迁移。
- 既有 A/B 判断：**排除 A/B 直接候选**。图像风格控制与 A/B 的文本证据任务无直接对应。

### #15 Towards Robust Multi-View Clustering via Early-to-late Manifold Consistency Calibration

- DOI：10.1109/TPAMI.2026.3752509；IEEE fno：11792949；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211792949%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`4a4414b9ca43fa372e50254b45d321fe615540de91e5bf7ee964eaff5e348914`。
- 官方摘要要点（中文转述）：多视图聚类利用早期融合形成的全局流形作为锚，对局部视图一致性评分并加权晚期融合。
- 既有 A/B 判断：**优先跨域候选·B**。可借鉴一致性加权；没有 RAG 污染标签、query 级误删校准或最终 QA 验证。

### #16 Talking Head Generation: A Comprehensive Survey

- DOI：10.1109/TPAMI.2026.3752684；IEEE fno：11793281；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793281%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`548b4f50c25cb857f4381f0a460361a6c72632d5c5f6fef8c4c73d0a6924ee7d`。
- 官方摘要要点（中文转述）：综述视频、音频等驱动的说话人头部生成方法。
- 既有 A/B 判断：**排除 A/B 直接候选**。数字人生成综述，并非 RAG 安全研究。

### #17 Exploring Aleatoric Uncertainty in Object Detection via Vision Foundation Models

- DOI：10.1109/TPAMI.2026.3752490；IEEE fno：11793282；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793282%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`2f561384fc0a3b529c7ad8315d2957ad052585d2db42ce186c1f8579452e9263`。
- 官方摘要要点（中文转述）：在视觉基础模型特征空间估计目标实例的数据不确定性，并用于数据中心训练与过滤。
- 既有 A/B 判断：**优先跨域候选·B**。不确定性和样本过滤可作 B 方法参考；目标检测噪声不同于恶意块、query 最终删块事件。

### #18 SplitKD: Enhancing Generalization and Straggler Resistance of Federated Learning via Parameter Split and Distillation

- DOI：10.1109/TPAMI.2026.3752851；IEEE fno：11793285；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793285%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`6ce16342d97f624e61e994a23f18e7b6e3ac97c970d604afacdeac03d283fa5b`。
- 官方摘要要点（中文转述）：通过参数拆分与蒸馏提升联邦学习泛化及对慢节点的抵抗。
- 既有 A/B 判断：**排除 A/B 直接候选**。联邦训练效率/泛化不是 RAG 检索防御。

### #19 Revealing Subtle Heat Flows All Around Us Using Microbolometric Videos

- DOI：10.1109/TPAMI.2026.3752581；IEEE fno：11793287；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793287%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`c5ac975ab5ab4c12c27a1665d148cf782cb18124f001ebd97981ad26924dde3f`。
- 官方摘要要点（中文转述）：从微测辐射热计视频揭示细微热流。
- 既有 A/B 判断：**排除 A/B 直接候选**。热成像物理测量，与 RAG 安全无直接关系。

### #20 Asymmetric Apparent-aware Relation Consistency Learning for Video Relation Grounding

- DOI：10.1109/TPAMI.2026.3752541；IEEE fno：11793292；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793292%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`6c536681411a9ab970d5891079d8ffd95cea5c979b4f51db66226d22ab7f3499`。
- 官方摘要要点（中文转述）：以非对称关系一致性与时空细化提升视频关系定位。
- 既有 A/B 判断：**排除 A/B 直接候选**。视频视觉关系定位不证明文本 chunk 共同必要或污染。

### #21 End-to-end Semantic-centric Video-based Multimodal Affective Computing

- DOI：10.1109/TPAMI.2026.3752601；IEEE fno：11793307；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211793307%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`4bee2a263deee5b39a427f751afac2edcbe5ca9353ab53be86776ed5b0353912`。
- 官方摘要要点（中文转述）：构建语义中心的端到端视频多模态情感计算框架。
- 既有 A/B 判断：**排除 A/B 直接候选**。情感识别中的模态语义不一致不是恶意 RAG 块检测。

### #22 Q-Eval+: From Absolute to Relative Quality Evaluation for Text-to-Vision Content

- DOI：10.1109/TPAMI.2026.3751387；IEEE fno：11780592；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211780592%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`6903bddb6fe6c1dff7e9121f6492e7b043e091269726511977a14cab85997f1a`。
- 官方摘要要点（中文转述）：构建文生图像/视频绝对质量与相对比较数据，并设计统一评价模型。
- 既有 A/B 判断：**弱方法参考·B**。相对比较和顺序一致性可启发评价；不提供 RAG 低误报防御证据。

### #23 Unified Human Motion Pretraining via Generative Chrono-Structural Decomposition and Alignment

- DOI：10.1109/TPAMI.2026.3751312；IEEE fno：11780651；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211780651%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`054c89140a09643eab28c9f4cb3f4f957cc9b1e4f2c61aeb48c9586066c6df4b`。
- 官方摘要要点（中文转述）：将人体运动及文本分解为时间和身体结构单元并对齐。
- 既有 A/B 判断：**排除 A/B 直接候选**。运动语言对齐不是长源分块后的共同必要性验证。

### #24 Spectral Super-Resolution Guided Registration for Hyperspectral and Multispectral Blind Fusion

- DOI：10.1109/TPAMI.2026.3750924；IEEE fno：11783156；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783156%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`e2c029931e3743b85dd8bb883d15a7fbfb3366144a567fefcc9490e918282822`。
- 官方摘要要点（中文转述）：通过光谱超分辨引导未配准高光谱与多光谱图像融合。
- 既有 A/B 判断：**排除 A/B 直接候选**。光谱图像配准/融合不对应 RAG 攻击。

### #25 When Structures Speak: A Quotient-based Detector for Generated Graphs

- DOI：10.1109/TPAMI.2026.3751997；IEEE fno：11783171；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783171%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`1c8aebba748a1cb2915cd8c11a1c7a8a7b934168f8dbb359a696acff4f14157b`。
- 官方摘要要点（中文转述）：以 3/4/5 环频率构造生成图检测统计量，使用真实图校准并测试自适应规避。
- 既有 A/B 判断：**优先跨域候选·B**。整图来源判定和误报校准可借鉴；无类型图生成鉴别不等于 RAG 块投毒检测。接受稿全文已另记。

### #26 Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning

- DOI：10.1109/TPAMI.2026.3751756；IEEE fno：11783174；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783174%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`25ea05b6d8d07bd9afc04a03c3b33d56e78881ce8b55b8ee7de0f640264bb703`。
- 官方摘要要点（中文转述）：基于部分信息分解、多分支 Transformer 与熵代理，学习多模态冗余、独有及联合表示。
- 既有 A/B 判断：**优先跨域候选·A**。联合信息与 A 有方法联系；未验证真实长源分块、共同召回及逐块必要性。作者稿和附录已另记。

### #27 Enhancing Gradient Inversion Attacks in Federated Learning via Hierarchical Feature Optimization

- DOI：10.1109/TPAMI.2026.3751908；IEEE fno：11783177；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783177%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`bee214d10a403380270d65c7f85f1c226498051f834ef8422940e99c52c105f9`。
- 官方摘要要点（中文转述）：研究联邦学习中利用共享梯度和生成先验重建数据的层级特征优化攻击。
- 既有 A/B 判断：**排除 A/B 直接候选**。虽属隐私攻击，但攻击面是联邦梯度而非检索库或 RAG 生成。

### #28 Vision Remember: Recovering Visual Information in LVLMs via Vision Feature Resampling

- DOI：10.1109/TPAMI.2026.3751856；IEEE fno：11783182；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783182%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`2c39a953226c8add989adb1fa49dcead49ffdab16de34d85517d861232052910`。
- 官方摘要要点（中文转述）：分析视觉语言模型压缩 token 和逐层对齐造成的信息流失，通过特征重采样回注视觉信息。
- 既有 A/B 判断：**弱方法参考·A**。视觉信息保留可启发研究；不证真实长源中多个检索块对同一查询均必要。

### #29 Leveraging Biomolecule and Natural Language through Multi-Modal Learning: A Survey

- DOI：10.1109/TPAMI.2026.3751956；IEEE fno：11783183；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783183%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`f6cf17af240cb99248a9a492ea378610fbc0164b3fa96977ca0761f9a1dab9c9`。
- 官方摘要要点（中文转述）：综述生物分子与自然语言的多模态学习及下游任务。
- 既有 A/B 判断：**排除 A/B 直接候选**。生物分子建模综述，不是 RAG 安全直接近邻。

### #30 Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph Foundation Models

- DOI：10.1109/TPAMI.2026.3751712；IEEE fno：11783184；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783184%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`c878053bf1d0f5596b745f725959ee6a46bc6e0983276f9cb7a7a0cf51c596b7`。
- 官方摘要要点（中文转述）：为跨领域动态图基础模型设计解耦、差异条件化提示。
- 既有 A/B 判断：**排除 A/B 直接候选**。模型适配中的 prompt 不是间接提示注入或检索投毒。

### #31 EnvGS++: Modeling View-Dependency with Real-Time Environment Gaussians

- DOI：10.1109/TPAMI.2026.3751695；IEEE fno：11783185；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783185%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`ef3249cc82add2f96f440ab4a71bb08f0f7503802d44d2889104fbf9094545cc`。
- 官方摘要要点（中文转述）：用环境高斯表示建模复杂反射和新视角三维渲染。
- 既有 A/B 判断：**排除 A/B 直接候选**。图形渲染问题，与 RAG 安全无直接对应。

### #32 Frequency-Adaptive Object Detection Using Events and Frames

- DOI：10.1109/TPAMI.2026.3751726；IEEE fno：11783189；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783189%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`d9e59488c10c99d50e75b4ba24a3395db0fe16ceecbc45267801c2f1e0ed47b7`。
- 官方摘要要点（中文转述）：融合事件相机和 RGB 帧处理目标检测中的频率失配。
- 既有 A/B 判断：**排除 A/B 直接候选**。视觉检测同步问题，不是检索证据过滤。

### #33 Burst Spiking Neural Networks

- DOI：10.1109/TPAMI.2026.3748342；IEEE fno：11783191；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783191%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`3728991e59ab6816dd5d3a4a818eac016090f774dcf3d8dd33621bda667fc8b9`。
- 官方摘要要点（中文转述）：研究脉冲神经网络在输入扰动下的准确率与鲁棒性。
- 既有 A/B 判断：**排除 A/B 直接候选**。通用网络输入鲁棒性不直接研究 RAG 块投毒或误删。

### #34 FoveaCam Duo: Foveated Stereo for Standoff Depth Sensing

- DOI：10.1109/TPAMI.2026.3751728；IEEE fno：11783192；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783192%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`c8a12c80d1ffdbe4a249172189b6b1cda4b6cdc451965dcbd2ef54101c5f826d`。
- 官方摘要要点（中文转述）：通过注视式双目、可转向光学与校准实现远距深度感知。
- 既有 A/B 判断：**排除 A/B 直接候选**。硬件视觉深度测量，与 RAG 证据安全无直接关系。

### #35 Paint Bucket Colorization Using Anime Character Color Design Sheets

- DOI：10.1109/TPAMI.2026.3750920；IEEE fno：11783199；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783199%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`7d39f86e3709aeb440076aa70453c5c8100d94726e6fcb7dd4a9f3a60f802eaa`。
- 官方摘要要点（中文转述）：利用角色配色设计表与跨帧一致性进行动画线稿上色。
- 既有 A/B 判断：**排除 A/B 直接候选**。动画视觉上色任务，非 RAG 安全。

### #36 Non-homogeneous Skeletal Feature Selection via Dimension-wise Fuzzy Auditing

- DOI：10.1109/TPAMI.2026.3751059；IEEE fno：11783205；[官方摘要全文 JSON](https://www.computer.org/csdl/api/v1/graphql?query=query%20%7B%20articleByFno(fno%3A%2211783205%22)%20%7B%20id%20title%20doi%20abstract%20year%20volume%20issueNum%20%7D%20%7D)。
- 官方摘要字段 SHA-256：`792c7e7f2fae809af88841610099371a758dcf2910c0f1567ab2e0674a479546`。
- 官方摘要要点（中文转述）：研究流形不均匀条件下的无监督特征选择和逐维模糊审计。
- 既有 A/B 判断：**排除 A/B 直接候选**。一般高维特征选择不是检索块必要性或污染防御验证。

## 正文阅读追踪

- #25 NFQ：[出版方托管作者接受稿阅读笔记](../notes/20261115_TPAMI_NFQ_3751997.md)。
- #26 MIIB：[arXiv v1 作者稿及附录阅读笔记](../notes/20261115_TPAMI_MIIB_3751756.md)。
