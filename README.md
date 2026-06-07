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

## Agent 設計

### 📄 Paper Agent

#### Responsibility
Responsible for paper search, PDF parsing, summarization, method/result extraction, and hardware feature extraction.

Outputs are directly fed into:
- Knowledge Base (Qdrant)
- Research Workflow (LangGraph / Core Engine)

#### Tools Used
- ArXiv API
- Semantic Scholar API
- Crossref API
- PyMuPDF (PDF parsing)
- Docling / Marker (document structuring)
- PaperQA2 (QA over papers)
- OpenAI / LLM (summarization + extraction)

#### Outputs
- Structured paper summary
- Method breakdown
- Experimental results extraction
- Hardware-relevant metadata

---

### 🧠 Research Agent

#### Responsibility
Handles topic exploration, survey generation, research gap analysis, and research roadmap planning.

Integrates:
- Papers
- Notes
- Experiment results
- Course knowledge

#### Tools Used
- Open Deep Research
- LangGraph (workflow orchestration)
- Qdrant (retrieval memory)
- LLM (survey synthesis)
- Notion API (optional export)

#### Outputs
- Survey report
- Research gap analysis
- Research roadmap
- Direction recommendations

---

### 💻 Coding Agent

#### Responsibility
Responsible for repository modification, debugging, test execution, commit suggestions, and workflow automation.

#### Tools Used
- OpenHands (primary execution engine)
- Aider (lightweight coding assistant)
- GitHub API
- Docker
- PyTest / unittest
- VSCode Remote / CLI tools

#### Outputs
- Code patches
- Git commits / PR suggestions
- Debug reports
- Automated test results

---

### 🧪 Experiment Agent

#### Responsibility
Handles training automation, metrics logging, experiment comparison, and report generation.

#### Tools Used
- MLflow (primary tracking system)
- Weights & Biases (optional)
- PyTorch
- TensorBoard
- Hydra / config systems

#### Outputs
- Experiment logs
- Training reports
- Model comparison tables
- Performance analysis

---

### ⚙️ Hardware Agent

#### Responsibility
Core differentiation module for AI Accelerator / FPGA research.

Provides hardware-aware analysis for:
- Quantization effects
- Pruning efficiency
- FPGA mapping estimation
- RTL / HLS cost modeling

---

#### Submodules
- Quantization Agent
- Pruning Agent
- FPGA Estimation Agent
- RTL / HLS Analysis Agent

---

#### Inputs
- Model architecture (e.g., Transformer, CNN)
- Precision (FP32 / INT8 / INT4)
- Hardware target (FPGA / ASIC / GPU)

---

#### Outputs
- Latency estimation
- LUT usage
- DSP usage
- BRAM usage
- Power estimation
- Memory footprint

---

#### Tools Used
- TorchAO
- BitsAndBytes
- Intel Neural Compressor
- Vivado (FPGA synthesis reference)
- Vitis HLS / Intel HLS
- Verilator (RTL simulation)
- Custom regression models (Python / sklearn)

---

### ✍️ Writing Agent

#### Responsibility
Generates academic writing, technical reports, emails, and meeting notes.

#### Tools Used
- LLM (GPT / Claude / local models)
- Notion API
- Markdown / LaTeX tools
- Pandoc (document export)

#### Outputs
- Paper drafts
- Technical reports
- Meeting notes
- Email drafts

---

### 🧠 Knowledge Agent

#### Responsibility
Handles semantic retrieval, knowledge graph construction, and long-term research memory management.

#### Tools Used
- Qdrant (vector database)
- PostgreSQL (structured metadata)
- Redis (cache / short-term memory)
- Optional: Neo4j (knowledge graph)

#### Outputs
- Semantic search results
- Knowledge graph relations
- Research memory embeddings
- Cross-document linking

---

### 📘 Course Learning Agent

#### Responsibility
Transforms academic courses into structured, retrievable, and exam-oriented knowledge systems.

---

#### Core Functions

##### 1. Lecture Understanding
- Slides / notes parsing
- Key concept extraction
- Formula identification

##### 2. Concept Decomposition
Breaks concepts into:

Definition → Intuition → Formula → Example → Pitfall

##### 3. Exam Pattern Analysis
- Past exam analysis
- Question type clustering
- Topic weighting estimation

##### 4. Practice Generation
- Similar questions
- Progressive difficulty questions
- Concept trap questions

##### 5. Review Scheduler
- Spaced repetition system
- Auto reminders
- Summary cards generation

##### 6. Exam Survival Mode
- One-page formula sheet
- High-yield concepts
- Quick revision notes

---

#### Tools Used
- PyMuPDF (slides parsing)
- Whisper (optional lecture transcription)
- LLM (concept extraction + synthesis)
- Qdrant (memory storage)
- Notion API (course organization)
- n8n (reminder automation)

---

#### Outputs
- Structured lecture notes
- Exam preparation sheets
- Concept breakdown graphs
- Practice problem sets
- Revision schedules

---

### 🔗 System Integration

All agents interact through:

- Core Orchestration Layer (PilotDeck / LangGraph / Custom Core)
- MCP Tool Protocols
- Shared Memory Layer (Qdrant + PostgreSQL + Redis)

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
