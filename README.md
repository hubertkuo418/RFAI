# ResearchForge AI Lab

> 可替換核心架構的個人 AI 研究 + 學習操作系統  
> Pluggable AI Research & Learning Operating System for AI Accelerator & Transformer Hardware Research

ResearchForge AI Lab是一套面向研究生與 AI 工程實作的個人 AI 作業系統，目標是把「文獻調研、課程學習、程式開發、實驗管理、硬體分析」整合成一條可自動化、可記憶、可擴充的研究工作流。

---

## 專案目標

本專案希望建立一個可替換核心、可長期累積知識、可串接多種工具的 AI Research & Learning OS，讓研究與修課流程自動化達到 70% 以上。

### 主要目標

- 自動搜尋與整理論文，生成 Survey 與 Research Gap。
- 建立可編輯、可回溯的長期記憶系統。
- 支援程式修改、測試與版本控制。
- 支援模型訓練、實驗追蹤與比較。
- 提供硬體分析能力，估算量化、剪枝、FPGA 相關成本。
- 新增 Course Learning Agent，強化課程學習與考試準備。

---

## 核心特色

### 1. 可替換 Core
本專案不綁死單一框架，而是讓核心調度層可替換為 PilotDeck、LangGraph 或自建 Core。
這樣可以根據開發階段、穩定性與需求自由調整，降低整體重構成本。

### 2. Agent 與 Core 解耦
Agent 專注於能力本身，Core 專注於任務調度與流程編排。
這種設計能讓研究、開發、學習、實驗與硬體分析各自獨立演進。

### 3. Memory 作為唯一長期記憶
系統以 Qdrant、PostgreSQL 與 Redis 組成記憶與資料層，保存論文、筆記、實驗、課程與任務資訊。  
透過語義檢索與結構化資料管理，讓系統能跨會話持續累積知識。

### 4. 所有能力 MCP 化
透過 MCP 風格的工具介面，把論文搜尋、GitHub 操作、實驗追蹤、硬體分析、課程處理模組化。 
這樣能提升系統可維護性，也方便日後擴充新工具。

---

## 系統架構

```text
Frontend Layer
(Open WebUI / Dashboard)

        ↓

Core Orchestration Layer
(PilotDeck / LangGraph / Custom Core)

        ↓

┌────────────┬────────────┬────────────┐
│ Agent Layer │ Tool Layer │ Memory Layer│
└────────────┴────────────┴────────────┘
```

### 前端層
- Open WebUI：主要聊天入口、Agent 入口、RAG 查詢、文件上傳。
- Dashboard：顯示任務狀態、實驗狀態、課程進度與研究追蹤。

### 核心調度層
- PilotDeck：適合做 WorkSpace-first 的研究工作區管理與長期記憶。
- LangGraph：適合做 stateful workflow、條件分支與多步驟流程控制。
- Custom Core：若未來需要完全控制，可改用自建調度核心。

### Agent 層
- Paper Agent
- Research Agent
- Coding Agent
- Experiment Agent
- Hardware Agent
- Writing Agent
- Knowledge Agent
- Course Learning Agent

### 工具層
- ArXiv MCP
- GitHub MCP
- MLflow MCP
- PaperQA MCP
- Hardware MCP
- Course MCP

### 記憶層
- Qdrant：向量記憶與語義檢索。
- PostgreSQL：結構化資料管理。
- Redis：快取與佇列。

### 自動化層
- n8n：每日論文摘要、每週課程複習、考前提醒、研究報告排程。

---

## Agent 設計總覽

本系統由多個可插拔 Agent 組成，透過 Core Orchestration Layer（PilotDeck / LangGraph / Custom Core）進行調度，並以 MCP（Model Context Protocol）統一工具介接。

---

## 📄 Paper Agent

### 功能
負責論文搜尋、PDF parsing、摘要、方法/結果提取與硬體特徵抽取。

### 使用工具
- ArXiv API / Semantic Scholar API
- PyMuPDF（PDF解析）
- Docling / Marker（結構化文件解析）
- PaperQA2（論文問答）
- OpenAI / LLM API（摘要與抽取）
- Qdrant（向量化存儲）

### 輸出
- Reading Notes
- Structured Paper Summary
- Hardware-related Feature Extraction（如 latency / bit-width / complexity）

---

## 🧠 Research Agent

### 功能
負責主題探索、Survey 生成、Research Gap 分析與研究方向規劃。

### 使用工具
- Open Deep Research
- LangGraph（流程控制）
- ArXiv / Semantic Scholar
- Qdrant（語意檢索）
- Notion API（知識同步）

### 輸出
- Research Survey
- Research Gap Report
- Research Roadmap

---

## 💻 Coding Agent

### 功能
負責 repo 修改、debug、test execution、commit 建議與工作流執行。

### 使用工具
- OpenHands（主要執行引擎）
- Aider（輔助 code editing）
- GitHub API
- Docker
- PyTest / Unittest
- VSCode Server（可選）

### 輸出
- Git Commit
- Pull Request
- Debug Report
- Code Refactor Suggestions

---

## 🧪 Experiment Agent

### 功能
負責 training automation、metrics logging、experiment comparison 與 report generation。

### 使用工具
- PyTorch
- MLflow（實驗追蹤核心）
- Weights & Biases（可選）
- TensorBoard
- Python training scripts

### 輸出
- Training Logs
- Experiment Comparison Table
- Performance Report

---

## ⚙️ Hardware Agent（核心差異化模組）

### 功能
提供 AI Accelerator / FPGA / RTL / HLS 研究所需的硬體分析能力。

---

### 子模組
- Quantization Agent
- Pruning Agent
- FPGA Estimation Agent
- RTL / HLS Analysis Agent

---

### 輸入
- Model Architecture（如 Transformer / CNN）
- Precision（FP32 / INT8 / INT4）
- Hardware Target（GPU / FPGA / ASIC）

---

### 輸出
- Latency Estimation
- LUT / DSP / BRAM usage
- Power Estimation
- Memory Footprint
- Hardware Cost Report

---

### 使用工具
- TorchAO
- BitsAndBytes
- ONNX Runtime
- Vivado / Vitis（FPGA toolchain）
- Verilator（RTL simulation）
- Python regression model
- HuggingFace Transformers

---

## ✍️ Writing Agent

### 功能
負責 paper draft、technical report、email 與會議紀錄撰寫。

### 使用工具
- OpenAI / LLM API
- Notion API
- Markdown / LaTeX
- Zotero（reference management）

### 輸出
- Research Paper Draft
- Technical Report
- Meeting Notes
- Email Draft

---

## 🧠 Knowledge Agent

### 功能
負責 semantic retrieval、knowledge graph 與 research memory 管理。

### 使用工具
- Qdrant（向量資料庫）
- PostgreSQL（結構化資料）
- Redis（cache / message queue）
- Notion API
- Neo4j（可選 knowledge graph）

### 輸出
- Semantic Search Results
- Knowledge Graph Relations
- Research Memory Retrieval

---

## 📘 Course Learning Agent

### 功能
將修課轉換為結構化、可記憶、可推理的學習系統。

---

### 核心能力
- Lecture Understanding（投影片解析）
- Concept Decomposition（概念拆解）
- Exam Pattern Analysis（考試分析）
- Practice Generation（題目生成）
- Review Scheduling（複習系統）
- Exam Survival Mode（考前總整理）

---

### 使用工具
- PyMuPDF（lecture PDF parsing）
- Whisper / ASR（課堂錄音轉文字）
- LLM（概念整理）
- Qdrant（課程記憶）
- Notion API（筆記同步）
- n8n（排程與提醒）

---

### 輸出
- Lecture Summary Notes
- Concept Breakdown Sheets
- Exam Prediction Report
- Practice Questions
- Final Exam Cheat Sheet

---

## 🧩 系統整合關係

所有 Agent 均透過 MCP 與 Core 互動：

Paper → Research → Knowledge → Writing  
Course → Knowledge → Exam Preparation  
Coding → Experiment → Hardware  
Hardware → Research Feedback Loop  

---

## 開發時程

### Phase 1（週 1–2）
- Core setup
- Qdrant
- Paper Agent
- Course Agent MVP（lecture summary）

### Phase 2（週 3–5）
- Research Agent
- Course Concept Decomposition
- Notion integration

### Phase 3（週 6–7）
- Coding Agent
- OpenHands

### Phase 4（週 8）
- Experiment Agent
- MLflow

### Phase 5（週 9–10）
- Hardware Agent（核心）

### Phase 6（週 11–12）
- 完整整合流程：
  Paper → Course → Survey → Code → Experiment → Hardware → Report

---

## 預期成果

### 研究效率
- 文獻整理效率提升約 70%
- 課程準備效率提升約 60%
- 實驗管理效率提升約 50%

### 系統成果
- AI Research OS
- AI Learning OS
- 可替換 Core 架構
- MCP 生態系統

### 研究價值
- Hardware-aware AI system
- AI accelerator analysis tool
- Course-aware knowledge OS

---

## 風險與對策

| 風險 | 對策 |
|---|---|
| Core 不穩定 | 使用可替換架構，Core 可切換為 PilotDeck / LangGraph / Custom Core |
| MCP 整合困難 | 採模組化設計，先串接成熟工具 |
| 時間不足 | 嚴格依 Phase 排程，先完成 MVP |
| 成本過高 | 採 local model fallback，降低 API 依賴 |

---

## 推薦技術棧

- **Core**：PilotDeck / LangGraph / Custom Core
- **Frontend**：Open WebUI / Next.js / TailwindCSS / shadcn/ui
- **Memory**：Qdrant / PostgreSQL / Redis
- **Automation**：n8n
- **Coding**：OpenHands / Aider
- **Experiment**：MLflow / W&B / PyTorch
- **Parsing**：PyMuPDF / Marker / Docling
- **Hardware**：TorchAO / Torch-Pruning / Vivado / Vitis / Verilator

---

## 目錄結構建議

```text
ResearchForge-AI-Lab/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── agents/
│   └── specs/
├── apps/
│   ├── dashboard/
│   ├── webui/
│   └── workflows/
├── services/
│   ├── core/
│   ├── memory/
│   ├── mcp/
│   └── automation/
└── experiments/
```

---

## 目前狀態

- [ ] Core 架構定義
- [ ] Qdrant 初始化
- [ ] Paper Agent MVP
- [ ] Course Agent MVP
- [ ] Research Agent
- [ ] Coding Agent
- [ ] Experiment Agent
- [ ] Hardware Agent
- [ ] Dashboard
- [ ] 全流程整合


---

## License

MIT License

---

## Contact

Created by Yu-Hao Kuo  
For research, learning, and hardware-aware AI workflow development.
