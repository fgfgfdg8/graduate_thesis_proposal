# `fig_rag_conceptions.pdf` 的生成说明

## 为什么这个 PDF 要纳入版本控制

`figures/rag_conceptions.svg` 是 **draw.io 导出**的 SVG。它的正文不是 `<text>`，而是
**13 组** `<switch>`，每组包含：

- `<foreignObject>`：真正的 XHTML 文字
- `<image>`：内嵌 base64 位图，作为不支持 `foreignObject` 的渲染器的回退

这决定了**只有浏览器内核能把它渲染成矢量文字**：

| 渲染器 | `foreignObject` | 结果 |
| --- | --- | --- |
| Chromium（Edge / Chrome） | 支持 | ✅ 矢量文字，可搜索、可选中 |
| Inkscape 1.4 / cairo | 不支持 | ❌ 退回 base64 位图，文字模糊 |
| cairosvg | 不支持 | ❌ 退回 base64 位图，文字模糊 |

实测证据：Inkscape 生成的 PDF **不含任何嵌入字体**（`pdffonts` 输出为空），
Chromium 生成的 PDF 嵌入 8 个字体（`Noto-Sans-SC`、`MicrosoftYaHei`、`ComicSansMS` 等）。

Overleaf 环境无法执行浏览器渲染，因此把渲染结果**直接纳入版本控制**
（`.gitignore` 末尾为该文件开了例外，因为 `*.pdf` 被整体忽略）。

## 重新生成

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File figures\render_rag_conceptions.ps1
```

脚本会自动：

1. 从 SVG 根元素读取 `width`/`height`（**尺寸不写死**，你改画布大小也不用改脚本）
2. 把 SVG 内联进一份 HTML
3. 用 Edge 无头模式打印为 PDF
4. **校验通过后才覆盖**仓库里的 PDF

三个必须遵守的约束（脚本已内置，改动时不要破坏）：

| 约束 | 原因 |
| --- | --- |
| SVG 必须**内联**进 HTML，不能用 `<img src>` | 否则 `foreignObject` 不渲染，得到空白页 |
| 工作路径必须是**纯 ASCII** | 中文路径会让 `file://` URL 失效，浏览器静默不出图 |
| `@page` 尺寸取 SVG 的 `width`/`height`，`margin: 0` | 否则页面留白或裁切 |

## 校验标准

| 检查项 | 期望 |
| --- | --- |
| `pdfinfo` 的 Page size | `661.92 x 460.08 pts`（即 882 × 613 px @96 dpi） |
| `pdfinfo` 的 Pages | `1` |
| `pdffonts` | 至少包含 `MicrosoftYaHei` / `Noto-Sans-SC` |
| `pdfimages -list` | **只有表头、没有数据行**（证明文字是真矢量，没退化成位图） |
| `pdftotext` | 能抽出完整中英文文字 |

`pdfimages -list` 与 `pdftotext` 两条最有价值：前者能立刻发现「文字变图片了」，
后者能立刻发现「文字画错了」。若 `pdffonts` 为空，说明误用了 `<img src>`。

## 该 PDF 不是字节可复现的

Chromium 会把生成时间写进 PDF 元数据（`CreationDate` / `ModDate`），
所以**即使 SVG 没有变化，重跑脚本也会产生全新的文件哈希**。

实测：对同一份 SVG 连续跑两次，`pdfinfo` 的页面尺寸、页数、字体表完全一致，
但 SHA-256 不同。

因此：**不要用「哈希是否相同」判断图片有没有变**；只在你确实改过 SVG 时才重跑，
否则会白白产生一个时间戳 diff 的提交。若需要判断内容是否真的变化，
请比对 `pdftotext` 的输出。

## ⚠️ 两个必须知道的坑

### 1. 直接改 SVG 文字，会让 base64 回退图过期

SVG 里的 13 张 base64 `<image>` 是 draw.io **导出那一刻**的位图快照。
如果只改 `<foreignObject>` 里的文字而不改回退图，就会出现：

- Chromium 渲染 → 走 `foreignObject` → **新文字，正确**
- Inkscape 打开 → 走 base64 回退 → **旧文字**

本仓库的 PDF 由 Chromium 生成，所以**结果是对的**；但 SVG 本身存在
「文字与回退图不一致」的状态。用 Inkscape 校验该 SVG 时请留意这点。

### 2. SVG 是导出产物，不是源头

改 SVG 只是改「快照」。**真正的源头是 draw.io 工程文件**。
若日后从 draw.io 重新导出覆盖该 SVG，手动改的文字会**全部丢失、退回原样**。

所以：如果这些文字错误在 draw.io 工程里也存在，请**同步修正工程文件**，
否则下次导出会复发。

## 修订记录

### 2026-09-28：修正图内三处文字错误

在 `rag_conceptions.svg` 的 `<foreignObject>` 中直接修正（**尚未同步到 draw.io 工程**）：

| 位置 | 修正前 | 修正后 |
| --- | --- | --- |
| 上下文框 | `as the CEO of Open`**`Al`**` since 2019.` | `as the CEO of Open`**`AI`**` since 2019.` |
| 上下文框 | `for the`**`question`**` based on the context.` | `for the `**`question`**` based on the context.` |
| 知识库文档 | `as the CEO `**`if`**` OpenAI since 2019.` | `as the CEO `**`of`**` OpenAI since 2019.` |

注意第一处是**小写字母 `l` 被敲成了大写字母 `I` 的形近错误**（`OpenAl` / `OpenAI`），
肉眼极易漏看；本项目用码点比对（`I` = U+0049）来确认，而不是靠肉眼。
