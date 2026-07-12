---
title: 'AI Agent 沙盒化五層架構解析'
date: 2026-07-12
image: /images/AI筆記/ai-agent-sandboxing-layers.jpg
category: AI筆記
tags: [沙盒隔離, 爆炸半徑, Agent Harness, 工具攻擊面, 圍堵邊界]
description: '本影片系統性拆解 AI Agent 沙盒化的五層架構，說明當 Agent 能讀寫檔案、執行指令時，Prompt 不再是安全邊界，真正防線須由系統提供。'
quote: '「Prompt 是意圖，不是邊界。邊界是當指令失效時仍然有效的東西。」'
action: '依 S-C-A-L-E 法則設計 Agent 沙盒：預設關閉、覆蓋子程序、依爆炸半徑選層級、限縮工具攻擊面、讓安全路徑保持簡單。'
source_has_timestamps: true
---

## [核心摘要]

本影片系統性拆解了 AI Agent 沙盒化的五層架構：V8 Isolate/WASM、OS 級沙盒、Docker 容器、gVisor 用戶空間核心、Firecracker microVM。核心痛點在於：當 Coding Agent 從純文字生成進化到能讀寫檔案、執行指令、安裝套件時，Prompt 指令不再是安全邊界，真正的防線必須由作業系統與執行環境提供。影片建立了一個從「意圖」（Intent）到「圍堵」（Containment）的心智模型，幫助開發者依據 Blast Radius 選擇最適沙盒層級，而非盲目追求最強隔離。

***

## [詳細重點整理]

### 1. Coding Agent 為何需要沙盒 [00:00]

現代 Coding Agent 能直接在終端機執行真實指令：跑測試、編輯檔案、安裝套件。核心問題是——什麼在阻止它做出「正常軟體級別的災難」？例如刪錯資料夾、讀取不該看的 `.env` 檔、執行惡意的 post-install 腳本、或被 README 中的惡意指令誤導。

關鍵概念：**Blast Radius（爆炸半徑）**——當 Agent 出錯時，損害在哪一層停止擴散。

### 2. Agent Harness 的三個根本問題 [00:45]

每個 Agent Harness 最終必須回答三個問題：

- Agent 在哪裡執行？
- 它被允許碰觸什麼？
- 在人類或策略介入之前，它能做多少事？

當 Agent 只有文字輸出時，風險限於回答品質；一旦獲得工具能力（API 呼叫、檔案讀寫、子程序生成、Shell 指令），風險結構徹底改變。

關鍵概念：**Intent vs. Containment（意圖 vs. 圍堵）**——Prompt 是「意圖」，但邊界是當指令失效時仍然有效的東西。

### 3. Prompt 指令 vs. 真實圍堵 [01:45]

你可以告訴模型「只讀這個專案的檔案」，這是有用的指引，但不是強制執行。當模型嘗試讀取 SSH 設定檔時，問題不在於 System Prompt 寫得好不好，而在於作業系統或執行環境是否會說「不」。Agent 坐落在語言與執行的奇異邊界上：將自然語言轉化為工具呼叫，再變成檔案操作、網路請求或程式碼執行。

Microsoft Semantic Kernel 漏洞是典型範例——一個函式被暴露為可呼叫，參數未嚴格約束，一段語言變成了進入宿主執行的路徑。

關鍵概念：**Tool Surface = API Surface（工具表面即攻擊面）**——一旦給予模型工具，你的工具清單就是攻擊面。

### 4. 工具呼叫成為攻擊面 [03:15]

Agent 安全至少包含三道邊界：模型能呼叫什麼（工具註冊表）、這些工具能存取什麼（憑證）、執行被允許在系統哪裡造成損害（沙盒）。沙盒是第二道防線，當第一道（工具邊界驗證）出錯時提供保護。

### 5. 權限提示與審批疲勞 [04:30]

多數 Agent 產品使用審批提示作為主要安全機制。當你只批准一兩個有意義的動作時，你能保持專注；但當你連續批准 30 個微小動作時，大腦就不再將它們當作安全決策。這與瀏覽器權限、行動應用權限、Cookie 橫幅是同一個問題。

Anthropic 的 Claude Code 數據證實了這一點：開啟沙盒後，權限提示大幅下降。許多提示其實是在要求人類補償缺失的圍堵。良好的沙盒讓例行操作（讀檔案、寫輸出、跑測試）不需打擾人類，審批提示可保留給真正跨越邊界的動作。

關鍵概念：**Approval Fatigue（審批疲勞）**——過度依賴人工審批會削弱安全警覺性。

### 6. 沙盒在 Agent Harness 中的定位 [06:15]

Agent Harness 是圍繞模型的完整系統：工具、記憶體、指令、評估、審批、執行行為。沙盒是 Harness 的一部分，但它是離 Blast Radius 最近的那部分——它決定 Agent 的動作被允許落在何處。

### 7. 沙盒堆疊：從執行環境到 microVM [07:05]

五層沙盒由下而上：

| 層級 | 技術 | 隔離強度 | 適用場景 |
|------|------|----------|----------|
| Layer 1 | V8 Isolate / WASM | 最低 | 窄介面任務（JSON 轉換、純計算） |
| Layer 2 | OS 級沙盒（seatbelt, landlock, seccomp, namespaces） | 中低 | 本地 Coding Agent |
| Layer 3 | Docker 容器 | 中 | 內部自動化、可信程式碼 |
| Layer 4 | gVisor（用戶空間核心） | 中高 | 不可信程式碼、需容器體驗但更低核心暴露 |
| Layer 5 | Firecracker microVM | 最高 | 多租戶、使用者提交程式碼 |

越高層意味著更強隔離，但也意味著更高成本、更慢啟動、更多映像管理與網路工作。

關鍵概念：**Cheapest Sufficient Boundary（最低充分邊界）**——真正的決策不是「最強沙盒是什麼」，而是「能圍堵你擔心的失敗的最低成本邊界是什麼」。

### 8. OS 級沙盒對本地 Coding Agent 的意義 [08:45]

本地 Coding Agent 需要靠近你的專案：檔案、測試、本地工具、套件管理器。若放入乾淨的 VM，隔離更強但摩擦也更大——Agent 可能缺少依賴、快取和本地服務。OS 級沙盒讓 Agent 作為真實程序執行，同時系統仍能限制存取範圍。

- macOS：Apple 的 seatbelt sandbox
- Linux：Bubblewrap（namespace）、Landlock（檔案存取規則）、Seccomp（系統呼叫過濾）組合使用

重要注意事項：此層是**策略驅動**的——邊界品質取決於實際套用的策略。若子程序未被覆蓋，Agent 可以透過生成外部工具來繞過規則。

關鍵概念：**Policy as Security Model（策略即安全模型）**——不要只問用了什麼原始元件，要問預設值是什麼。

### 9. 一個檔案讀取貫穿五層沙盒 [10:45]

以 Agent 嘗試讀取 `/etc/passwd` 為例，同一請求在不同層有截然不同的結果：

| 層級 | 結果 |
|------|------|
| Layer 1 (V8/WASM) | 檔案操作根本不存在——「一個沒有門的房間」 |
| Layer 2 (OS 沙盒) | 請求到達真實核心，策略檢查後回傳 Permission Denied |
| Layer 3 (Docker) | 讀取成功，但讀到的是容器的 `/etc/passwd`，非宿主機的 |
| Layer 4 (gVisor) | 請求路由至 Sentry（用戶空間核心），由它決定回應 |
| Layer 5 (Firecracker) | Guest Kernel 處理，檔案屬於 microVM 的根檔案系統 |

關鍵概念：**Same Request, Different Worlds（同樣請求，不同世界）**——「沙盒」一詞隱藏了完全不同的機制。

### 10. System Call 的實際運作 [12:00]

應用層的檔案讀取（JS 的 `fs.readFile`、Python 的 `open`、Shell 的 `cat`）離開語言環境後變成 System Call。程式請求核心開啟路徑，核心檢查程序、路徑、權限、掛載點、沙盒策略，然後回傳 File Handle 或拒絕。沙盒的本質就是控制哪些請求能到達核心、核心認為程序被允許做什麼、或程序以為自己活在什麼世界裡。

### 11. Layer 1：V8 Isolate 與 WebAssembly [13:15]

V8 Isolate 是 V8 JavaScript 引擎的獨立執行狀態實例——一個進程內的「獨立 JavaScript 宇宙」，擁有自己的 Heap、物件和執行上下文。關鍵在於：Isolate 內的程式碼預設不具備作業系統能力，除非宿主提供。

- JavaScript 在瀏覽器中沒有 Node 的 `fs` 模組；在 Node 中有
- 在精心設計的隔離環境中，可能只暴露少量宿主函式

WebAssembly 運作方式類似：模組獲得線性記憶體，需要宿主的 imports 才能接觸外部世界。

權衡：純 Isolate 移除了危險部分，但也移除了有用部分。多數 Coding Agent 之所以有用，是因為它們能與真實開發環境互動。

關鍵概念：**Capability by Host Grant（宿主授權能力）**——安全取決於宿主決定哪些能力存在。

### 12. Layer 2：OS 級沙盒 [16:15]

程序是真實的、核心是真實的、檔案系統是真實的，只是程序在額外規則下執行。

- macOS：seatbelt sandbox，可描述程序可讀、寫、執行、通訊的策略
- Linux：Bubblewrap（namespace 建立受限系統視圖）、Landlock（非特權程序自我施加檔案存取限制）、Seccomp（過濾系統呼叫）

失敗模式是**錯誤配置**：若允許路徑太廣，沙盒會忠實執行一個糟糕的策略；若網路開放，讀取的秘密可以離開機器；若子程序不繼承限制，Agent 可以請求另一個程式代為執行被禁止的動作。

關鍵概念：**Faithful Enforcement of Bad Policy（忠實執行糟糕策略）**——沙盒只負責執行，不負責判斷策略好壞。

### 13. Layer 3：Docker 容器 [19:30]

容器不是微型虛擬機——它是宿主機上的正常程序，只是擁有不同的世界視圖。Linux namespace 創造這個視圖：mount namespace（獨立檔案系統佈局）、PID namespace（獨立程序樹）、network namespace（獨立網路介面）、user namespace（使用者映射）。Cgroups 加入資源控制。

關鍵限制：**核心仍然是共享的**。若工作負載發現核心漏洞或濫用暴露的掛載點，邊界可能比想像中弱。掛載 Docker Socket 等於交出宿主控制權；以 privileged 執行等於在模型上打了一個大洞。

### 14. Layer 4：gVisor 與用戶空間核心 [23:00]

gVisor 在容器與完整虛擬機之間插入一個用戶空間核心——**Sentry**。應用程式以為在跟 Linux 對話，但大部分對話其實是先經過 gVisor，而非直接到達宿主核心。

核心價值：減少不可信程式碼對宿主核心的直接接觸，因為核心攻擊面是容器的主要風險之一。

代價是相容性與效能：Linux 龐大，應用程式依賴其偏僻角落；某些工作負載產生大量系統呼叫，在中間放一個用戶空間核心會帶來額外開銷或碰到相容性邊界。

關鍵概念：**User-Space Kernel Intercept（用戶空間核心攔截）**——在應用與宿主核心之間插入翻譯層。

### 15. Layer 5：Firecracker 與 microVM [26:30]

microVM 是為快速啟動和高密度最佳化的小型虛擬機。Firecracker（源自 AWS）是最知名範例。關鍵變化是：工作負載獲得自己的 **Guest Kernel**。

- 容器中，程序共享宿主核心
- Firecracker 中，程序在 Guest OS 內執行，透過 VMM 與虛擬硬體通訊，底層使用 KVM 的硬體虛擬化

逃離 Guest 進入宿主是比逃離錯誤配置的程序沙盒困難得多的問題類別。這就是為什麼 microVM 出現在運行他人程式碼的產品中——託管 Agent 平台、程式碼執行產品、瀏覽器自動化沙盒、多租戶環境。

關鍵概念：**Tenant-Sized vs. Host-Sized Blast Radius（租戶級 vs. 宿主級爆炸半徑）**——microVM 將損害限制在租戶範圍內。

### 16. 如何選擇正確的沙盒 [29:30]

| 場景 | 建議層級 | 理由 |
|------|----------|------|
| 本地 Coding Agent | OS 級沙盒（Layer 2） | 符合人體工學，不犧牲實用性 |
| 內部自動化（可信程式碼） | Hardened Docker（Layer 3） | 成熟 DX，但需正確配置 |
| 使用者提交程式碼 | gVisor / microVM（Layer 4-5） | 威脅模型改變，需更強隔離 |

兩個常見錯誤：
- 將 Docker 視為沙盒的同義詞——廣泛掛載、root 權限、開放網路不是硬化邊界
- 直接跳到 Firecracker 因為聽起來很厲害——如果工作負載是你自己 repo 上的測試執行器，microVM 只增加機制而不買到太多實際安全

### 17. 通用沙盒原則 [34:00]

五條跨層級原則：

1. **Start Closed（預設關閉）**——網路預設關、檔案系統權限預設限縮、憑證預設不存在。Agent 應透過配置獲得存取權，而非從你的機器繼承。
2. **檔案系統與網路成對考量**——若 Agent 能讀秘密又能上網，就有一條資料外洩路徑。
3. **覆蓋子程序**——Agent 鮮少直接做所有事；Shell 呼叫套件管理器，套件管理器執行腳本，測試執行器生成 worker。若沙盒只適用第一個程序，Agent 有簡單的逃逸路線。
4. **依 Blast Radius 選擇**——個人 Coding Agent 編輯一個 repo 與 SaaS 產品執行數千使用者程式碼是完全不同的風險。
5. **讓安全路徑變簡單**——若安全需要冗長設定和完美記憶，它不會是日常使用的路徑。良好的預設值是安全模型觸達真實使用者的方式。

關鍵概念：**Default-Deny Security（預設拒絕安全）**——存取權應透過顯式配置獲得，而非繼承。

### 18. 工具註冊表、憑證與 Agent 攻擊面 [36:15]

一旦給予 Agent 工具，可呼叫函式清單就是攻擊面的一部分。每個接受路徑、URL、SQL 片段或指令參數的函式，其輸入都需在工具邊界驗證。

將工具視為**公共端點**：最小化工具清單、保持工具契約窄、在實際工作前驗證參數、優先使用結構化選擇而非自由文字字串。

重要警示：沙盒限制程式碼能去哪裡，但不會自動讓預期動作變安全。若你給 Agent 一個有效的生產 API Key，Agent 用它透過官方 API 刪除生產資料，檔案系統沙盒救不了你。

關鍵概念：**Three Boundaries of Agent Safety（Agent 安全的三道邊界）**——模型能呼叫什麼、工具能存取什麼、執行能在系統哪裡造成損害。沙盒只是第三道，必要但不充分。

### 19. 最終心智模型 [38:15]

Agent Harness 是一個「委派動作的執行環境」。一旦這樣看，沙盒就不再是可選的安全功能，而是生產架構的一部分：

- 工具註冊表決定哪些動作存在
- 憑證決定這些動作能觸及什麼
- 沙盒決定執行被允許在哪裡造成損害

下次聽到「Agent 在沙盒中執行」時，要問的後續問題是：哪一層？什麼檔案系統存取？什麼網路存取？子程序是否繼承？有哪些憑證存在？當模型自信地做錯事時會發生什麼？

關鍵概念：**Agent Harness as Runtime for Delegated Action（Agent Harness 即委派動作執行環境）**——沙盒是生產架構的一部分，而非附加安全功能。

***

## [技術/數據對比]

### 五層沙盒完整比較

| 層級 | 技術 | `/etc/passwd` 讀取結果 | 核心共享 | 啟動速度 | 適用場景 |
|------|------|----------------------|----------|----------|----------|
| Layer 1 | V8 Isolate / WASM | 操作不存在（無檔案 API） | 不適用 | 最快 | 窄介面任務 |
| Layer 2 | OS 沙盒（seatbelt/landlock/seccomp） | 核心策略檢查後拒絕 | 是（共享） | 快 | 本地 Coding Agent |
| Layer 3 | Docker 容器 | 成功，但讀到容器的檔案 | 是（共享） | 中 | 內部自動化、可信程式碼 |
| Layer 4 | gVisor | Sentry 攔截並決定回應 | 部分（透過 Sentry） | 中慢 | 不可信程式碼、容器體驗 |
| Layer 5 | Firecracker microVM | Guest Kernel 處理，屬 VM 檔案系統 | 否（獨立 Guest Kernel） | 慢 | 多租戶、使用者提交程式碼 |

### 安全決策矩陣

| 場景 | 推薦層級 | 關鍵配置 |
|------|----------|----------|
| 本地 Coding Agent | OS 級沙盒 | 網路關閉、僅 repo 可寫 |
| 內部自動化 | Hardened Docker | non-root、drop capabilities、網路關閉、唯讀 FS |
| 使用者提交程式碼 | gVisor 或 microVM | 完整租戶隔離 |

***

## [結論與行動建議]

> **啟發金句**
> 「Prompt 是意圖，不是邊界。邊界是當指令失效時仍然有效的東西。」

> **行動法則：S-C-A-L-E 法則**
> - **S**tart Closed — 預設關閉一切（網路、檔案、憑證）
> - **C**over Children — 子程序必須繼承沙盒限制
> - **A**lign Blast Radius — 依爆炸半徑選層級，不依名氣
> - **L**imit Tool Surface — 工具清單即攻擊面，保持最小化與參數驗證
> - **E**asy Safe Path — 讓安全路徑成為最簡單的路徑

> **生活實踐建議**
> 在設計 AI Agent 產品時，將沙盒選擇視為架構決策而非安全附加項。第一步先定義「你要圍堵什麼失敗」，再回推最適層級。對於內部工具，Hardened Docker 配合 non-root、無網路、唯讀 FS 即可涵蓋大部分需求；對於面向使用者的程式碼執行平台，務必從 gVisor 或 microVM 起步。同時，將工具註冊表當作公開 API 來管理——每個工具都需參數驗證與最小權限原則，沙盒只是當工具邊界失守時的最後防線。

***

## [參考連結]

- 原始 YouTube 影片：[AI Agent Sandboxing: Layers, Tradeoffs, and Blast Radius](https://youtu.be/-01_NB4SbBY) [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)
