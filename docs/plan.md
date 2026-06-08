# ResearchForgeAI

## An Autonomous Multi-Agent Research Infrastructure for Transformer Accelerator Research

---

# 執行摘要

本計畫旨在建立 ResearchForgeAI，一套基於 Hermes Agent Framework 之自主研究代理系統（Autonomous Research Agent System），專為人工智慧加速器（AI Accelerator）與 Transformer 硬體研究所設計。

隨著大型語言模型（Large Language Models, LLMs）與生成式人工智慧快速發展，研究工作已逐漸由單純的論文閱讀擴展至文獻探索、知識管理、程式開發、實驗追蹤、會議管理以及硬體分析等多項流程。研究人員必須同時處理大量資訊與複雜工作流，導致研究效率受到限制。

本計畫以 Hermes Agent 作為核心平台，結合 Qdrant、OpenHands、MLflow、Docling、Zotero、n8n 與 Vitis HLS 等工具，建立具備長期記憶、技能學習、多代理協作以及自動化工作流能力之研究基礎設施。

系統將聚焦於 Transformer Accelerator 研究情境，透過 Research Agent、Meeting Agent、Coding Agent、Experiment Agent、Hardware Analysis Agent 與 FPGA Analysis Agent 等模組，協助研究生完成從文獻探索到硬體實現之完整研究流程。

本計畫預計於八週內完成最小可行產品（Minimum Viable Product, MVP），並逐步擴展為可支援實驗室級研究之自主研究平台。

---

# 第一章 計畫背景

## 1.1 研究背景

近年來大型語言模型與生成式人工智慧技術快速發展，使研究工作模式產生重大變化。

傳統研究流程主要以閱讀論文與撰寫報告為主，而現代研究則涉及：

- 文獻搜尋與管理
- 知識整合與長期保存
- 研究會議紀錄與追蹤
- 程式開發與版本管理
- 模型訓練與實驗分析
- AI Accelerator 設計與評估
- FPGA 實作與驗證

在 Transformer Accelerator 研究中，研究人員除了需理解演算法與模型架構外，亦需考量硬體資源、記憶體存取、資料流設計以及 FPGA 部署等問題。

因此建立一套整合式研究基礎設施已成為提升研究效率的重要課題。

## 1.2 問題陳述

### 知識管理問題

- 論文與課程資料分散
- Meeting 紀錄缺乏整理
- 難以建立長期知識庫
- 缺乏跨來源檢索能力

### 研究探索問題

- 文獻搜尋成本高
- Survey 建立耗時
- Research Gap 難以分析

### 會議管理問題

- Meeting 記錄不完整
- 決策內容易遺失
- 待辦事項缺乏追蹤

### 程式開發問題

- 程式修改紀錄分散
- 缺乏 AI 協助開發流程
- 測試與驗證效率低

### 實驗管理問題

- 超參數管理困難
- 實驗結果缺乏統一追蹤
- 報告生成耗時

### 硬體研究問題

- 模型硬體成本估算繁瑣
- FPGA 資源分析需大量人工操作
- 缺乏快速設計評估工具

## 1.3 計畫目標

建立 ResearchForgeAI，達成以下目標：

1. 建立統一研究知識管理平台
2. 建立自主文獻探索系統
3. 建立研究會議智慧管理系統
4. 建立 AI 輔助程式開發系統
5. 建立實驗追蹤與分析平台
6. 建立 Accelerator Analysis Framework
7. 建立 FPGA Analysis Framework
8. 建立可持續學習之 Research Skill System

---

# 第二章 系統架構設計

## 2.1 整體架構

```text
                    Hermes Agent
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
        Memory         Skills        Automation
          │               │               │
          └───────────────┼───────────────┘
                          │
                          ▼
                 Research Coordinator
                          │
 ┌──────────┬──────────┬──────────┬──────────┐
 ▼          ▼          ▼          ▼          ▼
Paper    Meeting    Coding    Hardware    FPGA
Agent    Agent      Agent     Agent       Agent
```

Research Coordinator Agent 作為核心控制單元，負責代理協調、記憶檢索以及工作流管理。

## 2.2 系統分層架構

### Agent Layer

負責任務協調與代理管理。

### Skill Layer

負責技能封裝與技能學習。

### Memory Layer

負責長期知識保存與檢索。

### Tool Layer

負責外部工具整合。

### Automation Layer

負責自動化工作流執行。

## 2.3 技術堆疊

| 類別 | 技術 |
|--------|--------|
| Agent Framework | Hermes Agent |
| Workflow | n8n |
| Memory Database | Qdrant |
| Knowledge Management | Obsidian |
| Paper Management | Zotero |
| PDF Parsing | Docling |
| Coding Assistant | OpenHands |
| Experiment Tracking | MLflow |
| Deep Learning | PyTorch |
| Hardware Analysis | ONNX |
| FPGA Development | Vitis HLS |
| Scheduling | Hermes Cron |
| MCP Integration | Hermes MCP |

---

# 第三章 Agent 模組設計

## 3.1 Memory Agent

### 功能

建立長期研究知識庫。

### 管理內容

- Papers
- Courses
- Meetings
- Projects
- Experiments
- Hardware Reports

### 核心能力

- Semantic Search
- Metadata Search
- Knowledge Linking
- Long-Term Memory

## 3.2 Paper Agent

### 功能

建立論文管理與分析流程。

### 能力

- arXiv 搜尋
- PDF 解析
- 論文摘要
- Citation 分析
- 文獻關聯分析

## 3.3 Research Agent

### 功能

研究方向探索。

### 能力

- Survey 建立
- Research Gap 分析
- Future Work 探索
- Research Roadmap 規劃

## 3.4 Meeting Agent

### 功能

研究會議智慧管理。

### 能力

- Speech-to-Text
- Summary Generation
- Decision Extraction
- Action Item Tracking
- Research Idea Extraction

## 3.5 Coding Agent

### 功能

AI 輔助軟體開發。

### 能力

- Code Generation
- Code Refactoring
- Test Generation
- Pull Request Generation

## 3.6 Experiment Agent

### 功能

實驗管理與追蹤。

### 能力

- Hyperparameter Tracking
- Result Comparison
- Visualization
- Report Generation

## 3.7 Hardware Analysis Agent

### 功能

Transformer Accelerator 分析。

### 分析內容

- Parameter Count
- FLOPs
- MAC Operations
- Memory Footprint
- Bandwidth Requirement
- Latency Estimation
- Throughput Estimation

## 3.8 FPGA Analysis Agent

### 功能

FPGA 資源分析。

### 分析內容

- DSP Usage
- BRAM Usage
- LUT Usage
- FF Usage
- Timing Estimation
- Resource Utilization

---

# 第四章 自動化工作流設計

## 4.1 Paper Workflow

```text
arXiv
   ↓
Docling
   ↓
Embedding
   ↓
Qdrant
   ↓
Memory
```

## 4.2 Course Workflow

```text
Course Material
      ↓
Summarization
      ↓
Knowledge Graph
      ↓
Memory
```

## 4.3 Meeting Workflow

```text
Meeting Audio
      ↓
Whisper
      ↓
Meeting Agent
      ↓
Action Items
      ↓
Knowledge Base
```

## 4.4 Coding Workflow

```text
Issue
  ↓
Coding Agent
  ↓
OpenHands
  ↓
Testing
  ↓
Pull Request
```

## 4.5 Experiment Workflow

```text
Training
   ↓
MLflow
   ↓
Analysis
   ↓
Report
```

## 4.6 Hardware Workflow

```text
Model
  ↓
ONNX Analysis
  ↓
Resource Estimation
  ↓
Report
```

## 4.7 FPGA Workflow

```text
HLS Design
   ↓
Resource Analysis
   ↓
Timing Analysis
   ↓
Report
```

---

# 第五章 八週時程規劃

| 週數 | 階段 | 交付物 |
|--------|--------|--------|
| Week 1 | Hermes 環境建置 | 基礎平台 |
| Week 2 | Memory Agent | Knowledge Base |
| Week 3 | Paper Agent | Paper Pipeline |
| Week 4 | Research Agent | Research Assistant |
| Week 5 | Meeting Agent | Meeting Intelligence |
| Week 6 | Coding Agent + Experiment Agent | Development Platform |
| Week 7 | Hardware Analysis Agent | Accelerator Analyzer |
| Week 8 | FPGA Analysis Agent + 系統整合 | MVP 完成 |

---

# 第六章 資源需求

## 硬體需求

| 項目 | 規格 |
|--------|--------|
| CPU | 8 Core 以上 |
| RAM | 32 GB 以上 |
| GPU | RTX 3090 或以上 |
| Storage | 1 TB SSD |
| FPGA | Xilinx Alveo（選配） |

## 軟體需求

| 類別 | 工具 |
|--------|--------|
| Agent Platform | Hermes Agent |
| Memory | Qdrant |
| Workflow | n8n |
| Coding | OpenHands |
| Experiment | MLflow |
| Knowledge | Obsidian |
| Paper | Zotero、Docling |

---

# 第七章 風險管理

| 風險 | 影響 | 緩解措施 |
|--------|--------|--------|
| Tool Integration Failure | 中 | 模組化架構 |
| Memory Database Failure | 中 | 定期備份 |
| Meeting Transcription Error | 中 | 人工校正 |
| Hardware Estimation Error | 高 | 建立驗證資料集 |
| FPGA Toolchain Failure | 高 | 初期聚焦分析功能 |
| 開發時間不足 | 高 | 優先完成 MVP |

---

# 第八章 預期成果

## MVP 成果

- Memory Agent
- Paper Agent
- Research Agent
- Meeting Agent
- Coding Agent
- Experiment Agent
- Hardware Analysis Agent
- FPGA Analysis Agent

## 研究成果

### Research Memory Schema

建立統一研究知識模型。

### Meeting Intelligence Framework

建立研究會議智慧管理框架。

### Accelerator Analysis Framework

建立 Transformer Accelerator 分析系統。

### FPGA Analysis Framework

建立 FPGA 資源分析系統。

### Autonomous Research Agent Framework

建立自主研究代理架構。

---

# 第九章 評估指標

| 指標 | 目標 |
|--------|--------|
| Memory Query Latency | < 500 ms |
| Search Accuracy | > 85% |
| Meeting Summary Accuracy | > 90% |
| Action Item Accuracy | > 90% |
| Hardware Estimation Error | < 10% |
| FPGA Report Generation Time | < 5 分鐘 |

---

# 第十章 結論

本計畫提出 ResearchForgeAI，一套基於 Hermes Agent Framework 的自主研究代理系統。

系統透過多代理協作、長期記憶管理、技能學習以及自動化工作流，整合研究生於文獻探索、知識管理、會議管理、程式開發、實驗追蹤以及 Transformer Accelerator 研究所需之核心流程。

未來可進一步結合 FPGA 自動化設計流程、硬體效能預測模型以及 AI Accelerator Co-Design 技術，逐步發展為支援智慧研究之新型研究基礎設施平台。