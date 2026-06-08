# ResearchForge AI Lab

## AI-Driven Research Infrastructure for Accelerator-Oriented Graduate Research

---

# 執行摘要

本計劃旨在建立 **ResearchForge AI Lab**，一套專為研究生設計之 AI 研究基礎設施（Research Infrastructure），整合論文管理、研究探索、課程學習、會議管理、程式開發、實驗追蹤、知識管理以及硬體分析流程。

系統以「整合現成工具 + 自行開發核心模組」為主要策略，透過 OpenClaw、n8n、Qdrant、OpenHands、MLflow 等成熟工具建立完整研究工作流，並將開發資源集中於具有研究價值之核心模組。

本計畫預計於八週內完成最小可行產品（MVP），未來可持續擴展為實驗室級研究輔助平台。

---

# 第一章 計畫背景

## 1.1 研究背景

大型語言模型與生成式人工智慧快速發展，使研究工作逐漸由單純閱讀論文轉變為：

- 文獻探索
- 知識管理
- 研究會議
- 程式開發
- 模型訓練
- 硬體部署

等多流程協同作業。

未來於 TASL Lab 從事 Transformer Accelerator 相關研究時，將同時面對：

- 論文閱讀量快速增加
- Meeting 資訊碎片化
- 實驗結果難以追蹤
- FPGA 開發流程複雜
- 知識分散於不同工具

等問題。

因此需要建立一套可持續使用之研究基礎設施。

---

## 1.2 問題陳述

### 知識管理問題

- 論文、課程、Meeting 紀錄彼此分離
- 無法跨來源搜尋

### 研究探索問題

- 新方向搜尋成本高
- 缺乏統一研究入口

### 會議管理問題

- Meeting 紀錄不完整
- Action Item 易遺漏

### 開發流程問題

- 程式修改缺乏紀錄
- 實驗結果難以比較

### 硬體研究問題

- FPGA 資源估算需大量人工計算
- Accelerator 設計缺乏快速分析工具

---

## 1.3 計畫目標

建立 ResearchForge AI Lab v2，達成以下目標：

1. 建立統一研究知識庫
2. 建立完整研究工作流
3. 建立會議智慧管理系統
4. 建立實驗追蹤平台
5. 建立硬體分析平台
6. 建立 FPGA 分析平台
7. 提升研究效率
8. 產出具有研究價值之核心模組

---

# 第二章 系統架構設計

## 2.1 整體架構

```text
                    OpenClaw
                         │
                         ▼
                  ResearchForge
                         │
 ┌──────────┬──────────┬──────────┐
 │          │          │          │
 ▼          ▼          ▼          ▼
n8n      Qdrant    OpenHands   MLflow
```

---

## 2.2 ResearchForge Skills

```text
ResearchForge
├── Memory Skill
├── Paper Skill
├── Research Skill
├── Course Skill
├── Meeting Skill
├── Coding Skill
├── Experiment Skill
├── Hardware Skill
└── FPGA Skill
```

---

## 2.3 技術堆疊

| 類別 | 技術 |
|--------|--------|
| Orchestration | OpenClaw |
| Workflow | n8n |
| Memory | Qdrant |
| Coding | OpenHands、Aider |
| Experiment | MLflow、TensorBoard |
| Paper | Zotero、Docling |
| Learning | NotebookLM、Obsidian、Anki |
| Core Development | Python |
| Hardware Analysis | PyTorch、ONNX |
| FPGA Analysis | Vitis HLS |

---

# 第三章 技能模組設計

## 3.1 Memory Skill

### 功能

建立統一知識管理系統。

### 管理內容

- Papers
- Courses
- Meetings
- Experiments
- Hardware Reports
- FPGA Reports

### 核心能力

- 向量搜尋
- Metadata Search
- 跨來源搜尋
- 長期知識保存

---

## 3.2 Paper Skill

### 功能

建立論文管理流程。

### 能力

- 論文收集
- PDF 解析
- 摘要生成
- 文獻搜尋
- 文獻關聯分析

---

## 3.3 Research Skill

### 功能

協助研究方向探索。

### 能力

- Survey 建立
- Research Gap 分析
- Future Work 建議
- 新研究方向探索

---

## 3.4 Course Skill

### 功能

建立研究所課程學習系統。

### 能力

- 課程摘要
- 知識圖譜
- 問答系統
- 間隔重複學習

---

## 3.5 Meeting Skill

### 功能

建立研究會議管理系統。

### 支援類型

- Professor Meeting
- Lab Meeting
- Paper Discussion
- Project Review
- Technical Meeting

### 核心能力

- 語音轉文字
- 會議摘要
- 決策整理
- 關鍵字擷取
- Action Item 生成
- 待辦事項追蹤

### 輸出內容

- Summary
- Decisions
- Tasks
- Keywords
- Research Ideas

---

## 3.6 Coding Skill

### 功能

建立 AI 輔助開發流程。

### 能力

- 程式生成
- 程式修改
- 自動測試
- Pull Request 建立

---

## 3.7 Experiment Skill

### 功能

建立實驗管理平台。

### 能力

- 實驗追蹤
- 指標比較
- 結果分析
- 報告生成

---

## 3.8 Hardware Skill

### 功能

建立硬體資源分析工具。

### 分析內容

- Parameter Count
- Memory Footprint
- MACs
- Bandwidth
- Throughput
- Latency

---

## 3.9 FPGA Skill

### 功能

建立 FPGA 資源分析工具。

### 分析內容

- DSP
- BRAM
- LUT
- FF
- Latency
- Timing

---

# 第四章 自動化工作流

## 4.1 論文工作流

```text
arXiv
  ↓
Docling
  ↓
Embedding
  ↓
Qdrant
```

---

## 4.2 課程工作流

```text
Course
  ↓
NotebookLM
  ↓
Obsidian
  ↓
Anki
  ↓
Qdrant
```

---

## 4.3 Meeting 工作流

```text
Meeting Audio
      ↓
Speech-to-Text
      ↓
Meeting Skill
      ↓
Memory Skill
      ↓
Qdrant
```

---

## 4.4 開發工作流

```text
Issue
  ↓
OpenHands
  ↓
Test
  ↓
Pull Request
```

---

## 4.5 實驗工作流

```text
Training
   ↓
MLflow
   ↓
TensorBoard
   ↓
Report
```

---

# 第五章 八週時程規劃

| 週數 | 階段 | 交付物 |
|--------|--------|--------|
| Week 1 | 基礎環境建置 | GitHub Repository、Docker、OpenClaw |
| Week 2 | Memory Skill | Knowledge Base |
| Week 3 | Paper Skill | Paper Pipeline |
| Week 4 | Research Skill + Course Skill | Learning System |
| Week 5 | Meeting Skill | Meeting Intelligence System |
| Week 6 | Coding Skill + Experiment Skill | Development Platform |
| Week 7 | Hardware Skill | Hardware Analyzer |
| Week 8 | FPGA Skill + 系統整合 | MVP 完成 |

---

# 第六章 資源需求

## 硬體需求

| 項目 | 規格 |
|--------|--------|
| CPU | 8 Core 以上 |
| RAM | 32GB 以上 |
| GPU | RTX 3090 / 4090 |
| Storage | 1TB SSD |
| FPGA | Xilinx Alveo（選配） |

---

## 軟體需求

| 類別 | 工具 |
|--------|--------|
| Knowledge Base | Qdrant |
| Workflow | n8n |
| Coding | OpenHands、Aider |
| Experiment | MLflow |
| Paper | Zotero、Docling |
| Learning | NotebookLM、Obsidian、Anki |

---

# 第七章 風險管理

| 風險 | 影響 | 緩解措施 |
|--------|--------|--------|
| Tool Integration Failure | 中 | 採模組化設計 |
| Hardware Analyzer 精度不足 | 高 | 建立驗證資料集 |
| FPGA Toolchain 不穩定 | 高 | 第一版聚焦分析 |
| Meeting Transcription Error | 中 | 建立人工修正流程 |
| 開發時間不足 | 高 | 優先完成 MVP |

---

# 第八章 預期成果

## MVP 模組

| 模組 | 狀態 |
|--------|--------|
| Memory Skill | 完成 |
| Paper Skill | 完成 |
| Research Skill | 完成 |
| Course Skill | 完成 |
| Meeting Skill | 完成 |
| Coding Skill | 完成 |
| Experiment Skill | 完成 |
| Hardware Skill | 完成 |
| FPGA Skill | 完成 |

---

## 核心研究成果

| 項目 | 研究價值 |
|--------|--------|
| ResearchForge Memory Schema | 統一知識管理 |
| Meeting Intelligence Framework | 研究會議智慧管理 |
| Hardware Analyzer | Accelerator Analysis |
| FPGA Analyzer | FPGA Design Analysis |

---

# 第九章 評估指標

| 指標 | 目標 |
|--------|--------|
| Memory Query Latency | < 500 ms |
| Search Accuracy | > 85% |
| Meeting Summary Accuracy | > 90% |
| Action Item Extraction Accuracy | > 90% |
| Hardware Analyzer Error | < 10% |
| FPGA Report Generation | < 5 分鐘 |

---

# 第十章 結論

ResearchForge AI Lab 旨在建立一套完整的研究基礎設施，透過九大 Skill 模組整合研究工作流程，將研究生常見的論文閱讀、課程學習、會議管理、程式開發、實驗追蹤以及硬體分析工作統一納入同一平台。

本計畫以「整合現成工具、聚焦核心創新」為原則，將開發資源集中於 Memory Schema、Meeting Intelligence、Hardware Analyzer 與 FPGA Analyzer 等具有研究價值的模組，最終形成可支援 Transformer Accelerator 研究之 AI 驅動研究平台。