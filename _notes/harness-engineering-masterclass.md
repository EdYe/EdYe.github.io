---
title: 'Harness工程：AI Agent失敗診斷法則'
date: 2026-07-07
image: /images/AI筆記/harness-engineering-masterclass.jpeg
category: AI筆記
tags: [Harness工程, 代理迴圈, 上下文管理, 工具介面, 驗證與可觀測性]
description: '影片核心貢獻是將「AI Agent為何失敗」的模糊問題，拆解成可診斷的具體層級，解決了業界普遍「出錯就怪模型不夠聰明」的認知盲點。'
quote: '當 Agent 失敗時，不要只問模型夠不夠聰明，要問是哪一層 Harness 撐不住了。'
action: '套用十二層診斷法則，每次 Agent 出錯時依序排查指令、上下文傳遞、上下文管理、工具介面、執行環境、持久狀態、編排、子代理、技能層、驗證與可觀測性等層級的瓶頸所在。'
source_has_timestamps: true
---
# Harness Engineering Masterclass 筆記

這部影片深入拆解「Harness Engineering」（護欄工程／代理系統框架設計），說明打造可靠 AI Agent 系統背後的十多個核心元件（primitives），而非僅依賴模型本身的智能 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

## [核心摘要]

影片核心貢獻是將「AI Agent 為何失敗」的模糊問題，拆解成可診斷的具體層級，解決了業界普遍「出錯就怪模型不夠聰明」的認知盲點 。作者指出，Codex、Claude Code、Gemini CLI 等系統之所以強大，並非單靠模型，而是模型周圍那層決定「模型看到什麼、能做什麼、記得什麼、如何驗證與復原」的 Harness 系統 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

## [詳細重點整理]

1. 模型與 Agent 的邊界 [00:01]
模型只能看到 Prompt 內的內容，一旦專案或任務資訊不在輸入中，模型就會開始猜測，這正是幻覺（Hallucination）的根源。**上下文邊界**是理解 Agent 局限性的起點 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

2. Agent 的定義與三層架構 [02:39]
Agent 是配置了指令、工具與可行動環境的模型；區分模型（推理引擎）、Runtime（觀察-決策-行動的迴圈）與 Harness（Runtime 周圍的系統）三個層次，是理解整套架構的基礎，稱為**代理迴圈（Agentic Loop）** 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

3. 指令（Instructions）[03:45]
透過 agents.md、Claude.md、System Prompt、Cursor Rules 等形式，將重複性引導寫入環境本身，讓使用者不必每次重複給指令，但指令本身是被動的，無法主動發現專案中的實際內容，這是**被動引導**的侵限 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

4. 上下文傳遞（Context Delivery）[06:15]
透過 @ 符號等機制把相關檔案、失敗測試、Log 直接餵給模型，讓回答從泛用建議變成針對性修正，但單純塞入大量內容並非真正的上下文工程 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

5. 上下文管理（Context Management）[08:14]
包含 RAG、重排序、摘要、壓縮（Compaction）等技術，核心問題從「能否提供上下文」轉變為「誰來決定此刻哪個上下文重要」，錯誤的上下文比缺少上下文更危險，這就是**注意力保護**的概念 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

6. 工具介面（Tool Interfaces）[10:46]
讓模型從「只會說」進化到「能行動」，透過 Function Calling、Anthropic Tool Use 或 MCP（Model Context Protocol）標準化工具的名稱、描述與參數結構，MCP 的價值在於抽象化工具暴露的方式 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

7. 執行環境（Execution Environment）[12:19]
決定工具呼叫實際在哪裡執行——本機、容器、雲端沙盒，涉及檔案系統範圍、網路政策、憑證與沙盒隔離，Daytona、E2B、Docker Sandbox 都是此層的代表方案，核心是**信任邊界的落地** 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

8. 持久狀態（Durable State）[14:16]
計畫檔、檢查點、任務日誌、記憶庫等機制讓進度在模型上下文之外仍可被保存與追蹤，避免因當前對話中斷而遺失所有進展，這是工作**可檢視性**的基礎 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

9. 編排（Orchestration）[16:19]
決定工作如何流動——生命週期掛鉤（Lifecycle Hooks）、心跳、重試、審批關卡、人機交接等，讓 Agent 的行為從「聊天」進化成「Runtime 系統」 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

10. 子代理（Sub-agents）[18:13]
將工作拆分成多個有邊界的迴圈，例如一個探索程式碼、一個檢查差異、一個驗證來源，OpenAI Agent SDK 的「Agent 即工具」模式是典型範例，核心概念是**窄化職責的專家代理** 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

11. 技能層（Skill Layers）[20:20]
將重複性的專業知識（如何審查 PR、如何做瀏覽器測試）封裝成可重用、可命名的程序，避免每個子代理各自摸索出不一致的流程，這是**可重用程序化知識**的體現 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

12. 驗證與可觀測性（Verification & Observability）[22:20]
驗證要求「拿出證據」——測試通過、截圈乾淨、來源可靠，而非只信任模型自信的結尾語句；可觀測性則記錄完整的工具呼叫鏈與追蹤日誌，讓失敗可被debug，這正是**「不要相信結論句，要看證據」**的原則 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

13. Harness 的演化 [25:14]
每一次失敗都能轉化為系統改進——遺漏的上下文變成檢索規則，危險指令變成權限關卡，重複糾正變成記憶，這是一種持續運作的**代理版事後檢討迴圈（Postmortem Loop）** 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

## [結論與行動建議]

**啟發金句**：「當 Agent 失敗時，不要只問模型夠不夠聰明，要問是哪一層 Harness 撐不住了。」 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**具體行動建議**：可套用「**十二層診斷法則**」——每次 Agent 出錯時，依序檢查指令、上下文傳遞、上下文管理、工具介面、執行環境、持久狀態、編排、子代理、技能層、驗證、可觀測性這十一個層級，逐一排查瓶頸所在 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**生活實踐建議**：在日常專案管理或個人 AI 工作流中，可先為重複性任務寫下明確的「指令文件」（如團隊規範），再逐步加入「檢查點記錄」與「驗證清單」，即便不涉及程式碼，這套分層思維同樣適用於任何需要委派 AI 執行重複任務的場景 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

## [參考連結]

https://youtu.be/mQfTdNVCOB0?si=3TK4xRMIB39voeR6
