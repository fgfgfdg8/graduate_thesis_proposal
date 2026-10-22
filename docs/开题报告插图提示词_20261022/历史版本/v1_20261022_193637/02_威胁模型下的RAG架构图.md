# 02 符合威胁模型的 RAG 系统架构图

**建议图题：**单源文档投毒威胁模型下的 RAG 系统架构。  
**依据：**报告 §3.2.1、§3.3.1，PDF 第9–10、14页；以本课题边界重构原图1。  
**构图：**外部信源与攻击控制区、服务端文档摄入区、在线检索生成区；影子系统仅为侧栏。  
**尺寸：**8:5，建议3600×2250。

将下面整个代码块交给生成模型：

```text
Generate ONE publication-style architecture illustration for a Chinese master's thesis proposal, showing a RAG system under a single-source-document poisoning threat model. Return only the finished image. Use a landscape 8:5 canvas, preferably 3600 × 2250 pixels. The figure must explain where the attacker acts, how the victim creates chunks, how two chunks enter one retrieved context, and where a server-side defense can be inserted.

All visible explanatory labels must be Simplified Chinese exactly as specified below. Keep only RAG, LLM, Top-K and mathematical identifiers in Latin notation. Do not render these English instructions. Do not add an English title, a numbered figure caption or a lengthy explanatory paragraph.

=== SCIENTIFIC CONTRACT ===
For each target query, the attacker may rewrite exactly ONE source document in the external corpus. The attacker knows the query q and its correct answer y_true, and aims for a mutually incompatible target answer a*. The victim retriever and generator are black boxes to the attacker. The attacker cannot set the victim's chunk boundaries or write two finished malicious chunks directly into the retrieval index. Victim-side ingestion must occur before the resulting chunks can be retrieved. The main target architecture has NO extra cross-encoder reranker. A local shadow system assists offline preparation and is not part of the victim service. The defense insertion point is after retrieval and before generation.

=== COMPOSITION: THREE SPATIAL REGIONS ===
Allocate approximately 24% of the width to external sources and the attacker's preparation area. Allocate the remaining 72% to a clearly bounded service region, with an upper ingestion lane and a lower online question-answering lane. Keep a generous gutter between external sources and service components. Draw a vertical dashed boundary labeled “外部信源／服务端边界”. The service region is operationally controlled by the defender, but stored source text remains untrusted; do not imply that crossing the ingestion boundary makes all document content trustworthy.

=== LEFT: EXTERNAL CORPUS AND ONE CONTROLLED DOCUMENT ===
At upper left draw a small collection of white, gray-edged source-document cards under “外部知识源”. Most documents have a blue-neutral source marker and remain unchanged. Highlight exactly one long document with an orange outline and the label “唯一可改写源文档”. Within this one document, show two small distant orange text regions with labels “规则前提 P_A” and “实例绑定 P_B”. These are sections inside a document, not independent uploaded documents. Use a shared source marker on both.

Next to this document, use a small neutral actor silhouette with an orange editing-pencil symbol labeled “攻击者”. Its only solid orange write arrow terminates on the long document and is labeled “单文档改写”. It must not point at the index, chunk collection, retriever weights, generator weights, trusted user question or system prompt.

Below, place a compact side panel titled “本地影子系统”. Within it use three small symbols with labels “影子分块器”, “代理检索编码器”, and “影子生成模型”. Its output is a document construction recommendation to the attacker, connected by a thin orange dashed line labeled “离线构造与筛选”. The shadow encoders and victim encoders must not be represented as the same object. A short note in this panel reads “目标模型参数不可见”.

If depicting victim query access, use only one thin gray dashed connector from the attacker to the user-facing query interface, labeled “黑盒接口”. Route it along the outer lower edge. No gradient, weight-reading or parameter-update connector may cross into the victim service. This query-interface connector is subordinate to the one-document write path.

=== UPPER RIGHT: VICTIM-SIDE INGESTION ===
Use the region label “知识库摄入”. Show a large document entering a sliding-window cutting illustration labeled “目标分块器 φ_v”. Three offset translucent outlines may represent alternative unknown boundaries, but do not show the attacker selecting a particular victim boundary. Add the short note “分块窗口与相位未知”.

The cutting illustration creates a stack of chunk cards: ordinary gray/blue cards plus two orange-accented cards labeled “同源块 c_A” and “同源块 c_B”. Give both the same small source-document ID marker and different offset marks. Show one card carrying a compact rule motif and the other carrying an entity-binding motif. The source relationship is essential: draw a thin brace or a short provenance connector back to the single original document.

Next place “文本编码与索引” and then a database-like storage symbol labeled “文本块与检索索引”. A small adjacent ledger is labeled “来源标识与块偏移”. This ledger is recorded during ingestion by the service; it is not an attacker-supplied claim of trustworthiness. Keep this metadata connector thin and gray.

The ingestion flow is strictly external document → target chunking → chunk encoding/index construction → stored chunks/index. No direct shortcut from the attacker's document into the LLM or from attacker-created role cards into the index is allowed.

=== LOWER RIGHT: ONLINE QUESTION ANSWERING ===
Show a user silhouette and a query card labeled “用户查询 q”. The main blue path proceeds to “检索器 R_v”, which reads the stored index. Represent retrieval output as a visible ordered stack labeled “Top-K候选上下文”. Use five miniature card slots as a readable illustrative instance and add the smaller label “主实验 K=5”. Include three ordinary cards and the two role cards, sharing the same source marker. Their displayed ranks are illustrative, not a promised fixed ranking.

Place a small brace below the two orange cards labeled “共同召回”. The presence of both cards is a depicted attack condition, not an assertion that every attempt succeeds. Do not create a separate user query for each card.

Immediately after this candidate stack, reserve a slim, green dashed rectangular slot labeled “防御部署位置”. Its secondary label is “检索后，生成前”. This slot indicates where research point two is enabled; it is not an additional architecture component required by the undefended target. A concise side note reads “按实验配置启用”. Keep its internal details out of this figure.

Continue to a compact context assembly symbol labeled “查询与上下文组装”, followed by a model symbol labeled “生成模型 G_ω”, then an answer card labeled “最终回答 ŷ”. The trusted query also has a thin blue connector to context assembly. The final answer must remain generic: do not assert that it is correct or always equals a*.

Along the outside of the lower lane, add one short orange goal annotation: “攻击目标：诱导输出 a*”. If a linkage is needed, use a dotted annotation line with no data-flow arrowhead. The attacker must not appear to control the output card directly.

=== GLOBAL ANNOTATIONS ===
Use a compact legend with “正常数据流”, “攻击者控制”, and “待启用防御”. Normal data flow is solid blue; the single document edit is solid orange; local preparation and black-box interface access use clearly labeled dashed lines; the defense deployment slot uses a green dashed outline. The two orange role chunks must remain identifiable by labels and a shared source marker in grayscale.

Do not add a reranking block. Do not add agent memory, autonomous planning, tool execution, web-search loops or online retraining. The source corpus may be generic external documents; do not use current real-world factual questions or famous-person examples.

=== STYLE SPECIFICATIONS ===
Use an exact, restrained 2D vector-like academic style on pure white #FFFFFF, with at least 70% white/near-white area. Normal RAG components and connections: blue #0072B2. Attack document regions and manipulation path: orange #E69F00. Defense slot: green #009E73. Text #263238, secondary text #66717D, neutral borders #CDD4DA. Use only these color families, tiny low-opacity tints, small corner radii and consistent 4–6 px strokes at 3600 px width.

Use a Chinese sans-serif font resembling Source Han Sans or Noto Sans CJK SC. Two font-size levels: about 86 px for region labels and 68 px for other text. Make all labels horizontal and legible at a final figure width of about 17 cm. Keep text inside its allocated areas; reroute lines around labels. Use a consistent family of simple document, cutting-window, index, model and actor symbols. Do not draw cartoons, padlocks claiming absolute security, glowing shields, 3D databases, thick colorful headers, gradients, drop shadows, neon, a commercial dashboard, fictitious performance numbers, logos or watermarks.

Before rendering the final image, check these semantic conditions: exactly one attacker-controlled source document; two role chunks created by victim-side chunking; shared source provenance; one retrieved candidate set; no reranker; black-box victim models; defense only between retrieval and generation; attack goal separated from observed output.
```

**建议图注：**攻击者仅能改写一篇外部源文档，由目标系统摄入、分块和编码后形成可检索文本块。两个同源角色块在共同进入上下文时构成待研究的组合投毒条件；防御部署在服务端检索之后、生成之前。图中的共同召回与目标答案表示攻击条件和攻击目标，不表示任意攻击均成功。

**核对重点：**“单文档控制”与“系统分块”必须同时可见；影子系统不能被画进目标系统内部；绿色模块仅标部署位置，具体防御机制留给图04。
