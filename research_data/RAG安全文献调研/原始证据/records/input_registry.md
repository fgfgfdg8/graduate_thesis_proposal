# 调研输入材料登记

证据地图中的开题页码均指所保存的原始开题报告 PDF 的物理页，不是页脚印刷号。以下本地留档未纳入 Git；列出文件名和哈希用于识别版本，不把无法随仓库取得的文件伪装成可用链接。

| 材料 | 版本与可追溯入口 |
|---|---|
| 用户提交的开题报告 PDF | 本地留档文件名为 `开题报告-吴丰艺-面向大语言模型检索增强生成系统的安全攻防研究.pdf`；SHA-256 `d015d18618bbcf7033f4fdef33428e9f5c661c6c43967d39c1d951c7186dfa6b`。原提交路径目前不存在，本地留档可供核对；同目录名称含“修改版”的文件未证明与该原稿相同。可另对照仓库中的[研究内容源码](../../../../partitions/section3_content.tex)，但两者的版本差异尚未系统核对。 |
| 第七版 CCF 推荐国际学术会议和期刊目录 | 用户提供的正式版 PDF SHA-256 `271b630b576bf8a4f802e767f5694caded93680e22b3a19bef7902591c45c1d3`；[CCF 官方发布说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml)。 |
| 调研开始前的技术总结快照 | `original_summary_before_20261102.md` 的登记 SHA-256 为 `18d0ef69df2b3bc0f293d16a01005828f7cedbf43cba2e1b8d2abb5185f41427`；其历史快照与[当前攻防总结](../../../../docs/RAG安全文献攻防技术手段总结报告.md)应按版本区分。 |


## TRIS 结构化身份修复记录（2026-11-15）

- 对象：`TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning`，Findings of EMNLP 2026，ACL Anthology `2026.findings-emnlp.2122`。核对 [ACL Anthology](https://aclanthology.org/2026.findings-emnlp.2122/) 与 [arXiv:2609.00470](https://arxiv.org/abs/2609.00470)；[arXiv:2603.23293](https://arxiv.org/abs/2603.23293) 是另一篇数学论文。
- 修复前精确旧值：现役 `study_registry.jsonl` 和 `metadata_export.jsonl` 中，`study_id` 为 `arxiv-2603.23293` 的 TRIS 记录各自顶层 `arxiv_ids` 均为 `["2603.23293"]`；两处订正为 `["2609.00470"]`。原值是错误的论文身份，不是别名。
- 内部 `study_id`、`report_id`、`source_id`、`evidence_id`、逐篇笔记旧文件名及其关联均保留。`sources.jsonl` 的历史 `metadata_snapshot.arxiv_id`（两条）和 `metadata_snapshot.arxiv_doi`（`10.48550/arXiv.2603.23293`），以及 `priority_inputs.jsonl` 和导出内 `legacy.original.study_match` 的旧冲突记录均为历史证据，保留原样，不代表当前论文身份。打分池、成员和既有 SHA 记录不变。
- `metadata_export_manifest.json` 记载的是 2026-11-07 生成时的历史状态；本次修复前其 `study_registry.jsonl`、`sources.jsonl`、`reports.jsonl` 登记哈希已与现役文件不一致，故不改写历史清单或假称导出已重新生成。
- Git 状态：该登记文件已受版本控制；两份现役 JSONL 被现有 `.gitignore` 排除，其修改不会出现在普通 `git diff`。修复前文件 SHA-256：`study_registry.jsonl` 为 `9146c47aa99cbe81ecb37175799fe2636d597d65ea726fd23f24abdd5a6a693a`；`metadata_export.jsonl` 为 `debfd2a3faac20cc0f087d2083fe6a6f5b25382aa223898a1789b1edafb4735c`。
