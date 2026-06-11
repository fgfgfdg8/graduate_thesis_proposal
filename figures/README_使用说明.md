# LLM Agent 架构图 LaTeX/TikZ 源码使用说明

## 1. 编译环境
建议使用 XeLaTeX 编译，因为图中包含中文与数学公式。

```bash
xelatex fig1_risk_evaluation_standalone.tex
xelatex fig2_trace_graph_attribution_standalone.tex
xelatex fig3_overall_framework_standalone.tex
```

也可以一次性编译三张图示例文档：

```bash
xelatex main_all_figures.tex
```

## 2. 文件说明
- `common_style.tex`：统一字体、颜色、箭头与节点样式。
- `fig1_risk_evaluation_body.tikz`：图 1 的 TikZ 图体，可直接 `\input` 到论文。
- `fig2_trace_graph_attribution_body.tikz`：图 2 的 TikZ 图体。
- `fig3_overall_framework_body.tikz`：图 3 的 TikZ 图体。
- `fig*_standalone.tex`：每张图的独立编译入口。
- `main_all_figures.tex`：三张图合并示例。

## 3. 插入论文的方法
在论文导言区加入：

```latex
\usepackage{graphicx}
\input{common_style.tex}
```

正文中插入：

```latex
\begin{figure}[htbp]
  \centering
  \resizebox{\textwidth}{!}{\input{fig1_risk_evaluation_body.tikz}}
  \caption{面向 LLM Agent 的工具调用链风险度量与可解释评估框架}
\end{figure}
```

## 4. 字体说明
`common_style.tex` 默认使用 Times New Roman；若系统没有 Times New Roman，则回退到 Tinos。
中文默认使用 Noto Serif CJK SC；如果在 Windows 或 Overleaf 自定义环境中需要强制宋体，可把 `common_style.tex` 中的 CJK 字体设置改为：

```latex
\setCJKmainfont{SimSun}
```

## 5. 公式说明
图中的公式均为 LaTeX 数学源码，不是图片文字，可继续修改变量、权重与指标名称。
