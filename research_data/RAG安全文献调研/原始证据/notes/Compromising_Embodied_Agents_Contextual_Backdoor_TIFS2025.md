# Compromising LLM Driven Embodied Agents With Contextual Backdoor Attacks

## 书目信息与版本

- **正式作者**：Aishan Liu、Yuguang Zhou、Xianglong Liu、Tianyuan Zhang、Siyuan Liang、Jiakai Wang、Yanjun Pu、Tianlin Li、Junqi Zhang、Wenbo Zhou、Qing Guo、Dacheng Tao。
- **正式出处**：IEEE *Transactions on Information Forensics and Security*, vol. 20, 2025, pp. 3979–3994；DOI [10.1109/TIFS.2025.3555410](https://doi.org/10.1109/TIFS.2025.3555410)。TIFS按第七版CCF目录为A类。
- **版本差异**：正式出版题名含“LLM Driven”；已阅读的arXiv v1题名为 *Compromising Embodied Agents with Contextual Backdoor Attacks*，arXiv:2408.02882v1，提交于2024-08-06。正式出版元数据与预印本对应同一研究；没有逐页比对IEEE排版终稿。
- **本地PDF**：[论文库文件](<../../../../../../../科研数据库/20_Research/Papers/RAG安全文献/Compromising LLM Driven Embodied Agents With Contextual Backdoor Attacks.pdf>)；24个物理页，2,343,915 bytes，SHA-256 `20AE98E6004571A53B77BEE65C891EF16923FF545C0AEF990AB0BE37C3F2FA56`。
- **阅读范围**：arXiv v1物理页1–24全文L3；未逐条审计全部参考文献，未运行作者实现或复现。论文结论限于该预印本版本。
- **项目制品**：作者[GitHub仓库](https://github.com/contextual-backdoor/contextual_backdoor)和[项目页](https://contextual-backdoor.github.io/)均公开；仓库标注[Apache-2.0许可证](https://raw.githubusercontent.com/contextual-backdoor/contextual_backdoor/main/LICENSE)。未审实现或运行复现。

## 威胁模型与攻击机制

论文研究LLM驱动具身代理的程序生成流程。攻击者污染少量演示上下文；目标LLM保持黑盒，不通过微调植入参数后门。作者使用对抗式in-context generation迭代优化恶意演示，由LLM judge评估候选prompt并反馈给优化器。文本与视觉两种触发条件共同控制程序缺陷的生成或执行，使生成代码表面合理、遇到特定环境条件时表现出非预期行为。论文设计五种程序缺陷模式，覆盖机密性、完整性和可用性影响。

## 实验范围与证据边界

实验覆盖ProgPrompt与VirtualHome机器人规划、VoxPoser机器人操作、VisProg视觉推理，以及Jetbot和真实自动驾驶相关场景（§5–6）。§7比较不同攻击模式和触发配置，§8讨论缓解方式。摘要报告在机器人规划、操作、组合视觉推理及真实自动驾驶系统中的攻击演示；具体成功结果依赖各自任务、代理接口和触发设置，不能合并成RAG通用ASR。

作者提出程序级保护和输入/输出审查作为缓解方向；这些不等价于检索前后对持久知识库文档做真实性、恶意性或来源检查。未据单一防御实验推出普遍可防或不可防。

## 对开题A/B的关系

**A方向**：这是高质量的上下文示例后门近邻，说明即便模型不微调，演示上下文也能携带条件化攻击。它没有RAG持久语料、文档摄入、检索器、未知chunker、Top-K共同召回或同源文本块共同必要性实验，不能当作开题A的同机制RAG撞题工作。

**B方向**：没有提出检索后恶意文本检测、事实真伪核验、来源血缘判定或clean-query误删率校准。对B仅是威胁入口和上下文隔离的参考，不是检测基线。

## 阅读定位

| 主张 | 论文位置 |
|---|---|
| 攻击目标、能力与要求 | §3，Threat Model |
| 对抗式ICL生成及双模态触发 | §4，Approach |
| ProgPrompt、VoxPoser、VisProg实验 | §5，Experiment and Evaluation |
| Jetbot与自动驾驶实验 | §6，Real-World Experiment |
| 攻击模式比较与缓解 | §7–8，Attacking Modes Evaluation / Discussions |

页码均以本地arXiv v1物理页为准；未取得并逐页核验IEEE正式排版PDF，故不把预印本分页冒称为期刊终稿页码。
