---
tags: [llm-generated, conf-paper-recommend, rag-security-evidence]
study_id: work-c7904f2868ef
reading_level: L3
checked_date: 2026-11-19
venue: "EMNLP 2026 Main"
ccf: "B"
doi: "10.18653/2026.emnlp-main.1772"
pdf_sha256: "9baefcadd810def675dae2f870ce26900e2eab03d08ef3ba0d02b5f0db142508"
pdf_pages: 20
---
# FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG

**阅读状态：L3（正文全文）+ 附录定向阅读。** 已读正式EMNLP 2026 PDF正文pp.1–9（文章页40386–40394）和附录A–U中与机制、数据、校准、消融及限制相关的页面；参考文献未逐条核对，附录所有表格未逐格复算。

## 正式身份

- **作者/机构**：Zhe Yu、Wenpeng Xing、Tiancheng Zhao、Mohan Li、Changting Lin、Meng Han；Binjiang Institute of Zhejiang University、Zhejiang University、Guangzhou University、GenTel.io。
- **年份/会议/track**：2026 / EMNLP 2026 Main；正式主会论文。
- **CCF**：第七版目录EMNLP主会为CCF-B；本文按主会记B。
- **正式出版信息**：Proceedings of EMNLP 2026, pp.40386–40405；[ACL Anthology](https://aclanthology.org/2026.emnlp-main.1772/)；[DOI](https://doi.org/10.18653/2026.emnlp-main.1772)；[BibTeX](https://aclanthology.org/2026.emnlp-main.1772.bib)。
- **本地PDF**：[正式EMNLP PDF](<D:/学在东南/科研数据库/20_Research/Papers/RAG安全文献/FIDES_ Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG.pdf>)，20物理页，1,278,528 bytes，SHA-256 `9baefcadd810def675dae2f870ce26900e2eab03d08ef3ba0d02b5f0db142508`。
- **代码**：正式PDF附录V称实现、评测脚本和配置将在发表后以MIT许可证公开，并称重写提示位于代码库；本次未取得可核验的公开仓库URL，因此不把它写成已开放代码。
- **版本线索**：未核arXiv或预印本版本；科学判断以正式EMNLP版为准。

## 一句话总结

FIDES是一个**训练-free、白盒、逐token的自适应对比解码器**：在每一步同时比较context路径与no-context路径的输出分布、逐层hidden trajectory及context路径的内部预测演化，用固定融合权重重算contrastive强度，使模型更倾向于遵循与参数记忆冲突的检索证据。它提高的是**decoder对给定证据的忠实性**，不是证据真实性、来源安全性或投毒检测。

## 方法

### 1. 双路径对比解码

设query为`x`、检索文档为`d`、已生成前缀为`y_<t`：

- context路径输入`[d; x; y_<t]`，得到logits `z_ctx(t)`和逐层hidden `h_ctx(t,l)`；
- no-context路径输入`[x; y_<t]`，得到`z_noctx(t)`和`h_noctx(t,l)`；
- 在token级做对比：

`z_final(t) = (1 + α_t) z_ctx(t) − α_t z_noctx(t)`

其中`α_t ≥ 0`控制当前step抑制参数记忆、放大context的强度。

### 2. 三个深度信号

- **Opposition**：`JSD(softmax(z_ctx(t)) || softmax(z_noctx(t)))`，衡量输出分布层面的context–memory分歧；
- **Shift**：比较context和no-context路径的归一化逐层hidden state距离，再按固定尺度裁剪；
- **Noise**：用Logit Lens比较context路径中点层和最终层的预测分布，衡量context路径内部预测演化。

三信号按固定权重融合为FIDES score，并映射为`α_t`。作者强调权重和尺度是先根据无标签信号统计/架构范围固定，再在所有数据集和backbone上不变；不是按测试集调参。

### 3. 关键设计边界

- 需要logits、逐层hidden state及LM head，属于**白盒解码器**；不能直接用于只能取生成文本的黑盒API。
- 双路径每步前向，显著增加推理成本；
- 只改变logits，不改变模型权重，也不训练probe；
- 不验证检索claim是否真实；作者明确说，若检索错误或被对抗编辑，FIDES可能跟随错误证据。

## 主要结果

- 三个知识冲突QA设置：NQ-Swap、PopQA（CF-RAG）、TriviaQA（CF-RAG）；NQ非冲突控制，每个主设置`n=8,000`。
- 四个主backbone：LLaMA2-7B、Mistral-7B、LLaMA3-8B、Qwen3-8B；扩展至LLaMA2-13B和LLaMA3-70B。
- 作者报告FIDES在全部18个model–dataset设置中取得最高Context Fidelity；相对Standard RAG提高约14–28个百分点，相对最强的同预算训练-free基线AdaCAD提高约3–13个百分点。
- LLaMA3-70B上CF约92–94%、F1约62–63%。
- 128个匹配NQ-Swap pair的机制审计：冲突使answer-position Opposition增加0.0969、`α_t`增加0.0727（均`p<1e-4`）；但raw Shift效应很小且不显著，clipped Noise在该checkpoint饱和为1.0。作者明确不声称每个信号都独立识别冲突。
- 在PopQA加入20%/50%无关文档时，FIDES比Standard RAG和CAD更稳；50%噪声下FIDES下降5.7点，Standard RAG下降12.8点、CAD下降14.1点。该实验是**无关文档噪声**，不是针对恶意或事实错误的对抗证据。
- 延迟：FIDES整体约为Standard RAG的2.02–2.05倍；信号计算相对CAD只增加8.2%–11.2%，但双路径是主要成本。

## 与开题A/B的关系

### A方向

FIDES不是攻击论文，也没有恶意客户端、语料投毒或未知chunker。它研究的是**模型在有冲突证据时是否遵循context**，因此不能用来支持A的攻击面或块共同必要性。其价值仅在于提供一个“context-following”评价参照：即使攻击成功让恶意证据进入context，模型仍可能忽略它；反过来，FIDES提高follow-context后也可能更忠实于错误证据。

### B方向

**直接方法近邻，但不是安全检测器。** FIDES的Opposition/Shift/Noise是解码阶段的内部信号，和B可能使用的四统计、冻结编码器、来源/命题关系不同；其token级干预并不做检索块准入、来源认证或最终query级误删控制。

其负结果对B很重要：

1. 不能把“模型遵循检索证据”当作“证据真实”；FIDES明确可跟随错误或对抗编辑证据；
2. 若B的解码端或后验核验采用冲突/内部信号，必须单独测试语义相关但事实错误的证据；
3. FIDES的白盒要求和双路径成本意味着它不能直接替代黑盒RAG安全过滤器；
4. 论文只覆盖单文档英文QA、实体级counterfactual和有限噪声；多文档矛盾、部分正确证据、多跳链和正常query最终OR误删仍待验证。

## 局限与证据边界

- 需要logits和hidden states，不适合generation-only黑盒API；
- 双路径推理带来约2倍延迟；本文未实现prefix缓存/冲突门控的优化收益；
- 不是事实核验器：错误证据与正确证据都可能被更强地遵循；
- 机制证据主要来自LLaMA3-8B的128个匹配pair，raw Shift不显著、Noise饱和；
- 未覆盖MoE/SSM、多语言、多模态和自然发生的部分正确证据；
- 引用数未查询，不写0；代码是否已公开未确认；未运行或复现。

## 来源与实际阅读范围

- 正式PDF：[ACL Anthology](https://aclanthology.org/2026.emnlp-main.1772.pdf)；DOI `10.18653/2026.emnlp-main.1772`。
- 实际阅读：正文pp.1–9，附录关键方法/实验/限制页；未逐条核对参考文献，未复算全部附录表格。
- 历史L1事件：2026-11-02仅读官方卷内摘要，未取得PDF；该旧事件保留为历史，不覆盖本L3记录。
- [返回证据地图](../../../../docs/RAG安全证据地图_20261102.md#src-87e6ec5ae7331805)
- [全部逐篇笔记](../README.md)
