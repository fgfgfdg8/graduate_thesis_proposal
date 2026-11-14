# Beyond Text: Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation

## Identity

- Authors: Jiankun Zhang; Shenglai Zeng; Jie Ren; Tianqi Zheng; Hui Liu (Amazon); Xianfeng Tang; Hui Liu (Michigan State University); Yi Chang.
- Venue: EMNLP 2025 Main, pp. 24789–24810. CCF-B under the user-provided CCF 7th-edition catalogue. DOI: 10.18653/v1/2025.emnlp-main.1259.
- Official record: https://aclanthology.org/2025.emnlp-main.1259/
- Official PDF: https://aclanthology.org/2025.emnlp-main.1259.pdf
- Local PDF: Beyond Text_ Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation.pdf, 22 pages, 2,535,950 bytes, SHA-256 1AB6F3F0F31CFAAAEF3BF3E1B7EC7479FA2DF1122D7522140CE633DDA6736FF4.
- Author project: https://github.com/phycholosogy/MRAG-privacy (public page reachable; repository, license and reproducibility were not audited).
- Reading: physical PDF pages 1–22, full text, tables, appendices and references; L3. No code execution or independent replication.

## Scope and Method

The paper studies privacy extraction from vision-language and speech-language RAG systems. Its compositional prompt attack tests direct reproduction of retrieved images/audio and indirect reproduction of image text, captions or speech transcripts. It does not study corpus poisoning, malicious-source detection or a defense mechanism.

Visual experiments use ROCOv2, IAM and Conceptual Captions (CC), with Gemini/Lumina for image outputs and Qwen/Gemini/LLaVA for text outputs. Speech experiments use 33,079 MultiMed recordings and a 50,870-clip Emilia subsample; the default audio retrieval setting is top-1. Direct speech generation uses MiniCPM-o-2.6; indirect generation also tests Gemini-2.0-flash and Qwen2.5-Omni-7B. Main leakage evaluations use 500 prompts per setting.

## Main Results

- Direct visual leakage (Table 1): on ROCOv2, 101 unique images were retrieved. Across 500 prompts, Gemini produced 366 MSE-matched outputs (81 distinct images) and Lumina 406 (73 distinct images). IAM and CC also showed successful image extraction under the paper's MSE, PSNR and SIFT thresholds.
- Indirect visual leakage (Table 2): on IAM, 75 unique images were retrieved. Gemini yielded 499 prompts with over-80%-word copying, 499 with a 15-word copied span, and 498 CLAIR scores above 80; these corresponded to 75 distinct images. On CC, Gemini's CLAIR threshold was met in 318 prompts and mapped to 73 distinct images.
- Indirect audio leakage (Table 3): for MultiMed/Gemini, 432 of 500 prompts exceeded the 80%-word-copy criterion and mapped to 183 distinct retrieved clips; for Emilia/Gemini the respective counts were 441 and 170. Table values from different metrics are not interchangeable.
- Direct audio leakage (Table 4): LMM evaluation marked 190 MultiMed outputs (84 distinct clips) and 408 Emilia outputs (154 distinct clips) as matching.
- Image-text pair leakage: 277/500 prompts met the joint Words-Copied and MSE criteria, covering 50 distinct pairs.
- Speaker re-identification: among 250 evaluated queries, MFCC nearest-neighbor matching placed the true speaker recording in the top-3 for 11 cases, top-10 for 20 and top-100 for 79; Chroma placed 32 in the top-100.

## Measures and Limits

Visual direct leakage uses MSE < 90, PSNR > 30 and SIFT > 0.1; indirect image-text leakage uses >80% word overlap, a continuous copied span >15 words, or CLAIR >80. Indirect speech uses the same word/span tests and ROUGE-L or BLEU-4 >0.5. Direct audio uses MFCC <0.75, Chroma <0.0075 and Gemini-2.0-flash LMM matching. These thresholds are empirical protocol decisions and model-based measures are not independent human privacy judgments.

The study covers vision and speech modalities, not GraphRAG or other modalities. It emphasizes empirical leakage measurement and leaves mechanism analysis and effective defenses open. For the thesis, it is a multimodal confidentiality/extraction neighbor, not a direct collision with poisoning direction A or malicious-block detection direction B. The ACL Anthology page's MODS export omits one Hui Liu; the official PDF and Bib record list two distinct Hui Liu authors, affiliated with Amazon and Michigan State University respectively. Citation count and priority inputs remain pending.
