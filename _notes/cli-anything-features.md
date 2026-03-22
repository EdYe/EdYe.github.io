---
title: 'CLI-Anything：讓軟體變AI Agent原生工具'
date: 2026-03-22
image: /images/AI筆記/cli-anything-features.jpg
category: AI筆記
tags: [CLI-Anything, AI Agent, CLI, 自動化Pipeline, 開源工具]
description: 'CLI-Anything 是由香港大學數據科學實驗室開發的開源工具，核心用途是將任意有原始碼的軟體自動轉換成 AI Agent 可直接操控的命令列介面'
quote: "Today's Software Serves Humans. Tomorrow's Users will be Agents."
action: '將 CLI-Anything 與 Claude Code 整合，擴展 Agent 可操控的軟體範疇'
source_has_timestamps: false
---

# cli anything 有什麼用

**CLI-Anything** 是由香港大學數據科學實驗室（HKUDS）開發的開源工具，核心用途是**將任意有原始碼的軟體自動轉換成 AI Agent 可直接操控的命令列介面（CLI）**，讓現有軟體具備「Agent-Native」特性。

## 解決什麼問題

目前 AI Agent 推理能力已很強，但要操控 GIMP、OBS Studio 等專業 GUI 軟體，要麼 UI 自動化不穩定、要麼軟體根本沒有 API。CLI-Anything 的核心命題是：

> **"Today's Software Serves Humans. Tomorrow's Users will be Agents."**

## 為什麼選擇 CLI？

CLI 是人類與 AI Agent 的共同語言，原因如下：

- **天然匹配 LLM** — 文字指令就是 LLM 最擅長的輸入輸出格式
- **自描述** — 一個 `--help` 就能讓 Agent 自動探索全部功能
- **輸出穩定可靠** — 結構化輸出讓 Agent 行為可預測
- **輕量通用** — 幾乎零開銷，跨平台執行


## 七階段全自動 Pipeline

你只需要給它一個 GitHub 倉庫網址，它會自動走完：

1. **分析** — 理解軟體結構與能力
2. **設計** — 規劃 CLI 指令架構
3. **實作** — 以 Python Click 框架生成 CLI 層
4. **規劃測試**
5. **編寫測試** — 已通過 1,508 項測試驗證
6. **文件** — 自動產生說明文件
7. **發布** — 可直接使用的 CLI 工具

## 實際應用範例

以 LibreOffice 為例，Agent 可以這樣操作：

```bash
# 建立文件 → 加標題 → 匯出 PDF，一氣呵成
cli-anything-libreoffice document new -o report.json --type writer
cli-anything-libreoffice --project report.json writer add-heading -t "Q1 Report" --level 1
cli-anything-libreoffice --project report.json export render output.pdf -p pdf
```

目前已在 GIMP、OBS Studio 等 11 款複雜開源軟體上成功驗證。

## 限制

- **需要原始碼** — 若是已編譯的黑盒二進位檔（如許多商業軟體），則無法使用
- 生成的 CLI 不一定一次覆蓋軟體所有功能，需透過 `refine` 指令迭代補全


## 對你的應用價值

以你的 AI Agent 開發背景來看，CLI-Anything 可以和 **Claude Code** 深度整合——Claude Code 本身每天就透過 CLI 執行數千個真實任務，這個工具可以大幅擴展 Agent 能操控的軟體範疇，是打造複雜 Agentic Workflow 的好工具。
