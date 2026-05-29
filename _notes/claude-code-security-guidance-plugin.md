---
title: '在 Claude 撰寫程式碼時即時偵測安全問題'
date: 2026-05-29
image: /images/影片筆記/claude-code-security-guidance-plugin.jpeg
category: 影片筆記
tags: [縱深防禦, 多層次安全檢查, 模式比對, 代理式深度審查, 安全責任分層]
description: '此外掛在 Claude Code 編寫與修改程式碼的同一工作階段中，自動針對常見安全漏洞進行多層次審查（字串模式比對＋模型審查＋代理式深度檢查），並回饋修正建議'
quote: '讓 AI 在寫程式的當下就帶著「安全意識」，遠比事後補破洞便宜得多。'
action: '先在常用 repo 完成外掛安裝與規則設定，再建立「寫完一段就看一次安全提示」的習慣。'
source_has_timestamps: true
---
[核心摘要]  
此外掛在 Claude Code 編寫與修改程式碼的同一工作階段中，自動針對常見安全漏洞進行多層次審查（字串模式比對＋模型審查＋代理式深度檢查），並回饋修正建議，讓注入攻擊、不安全反序列化、不安全 DOM API 等問題盡量在進入 Pull Request 前就被發現並修補，成為既有 SAST／CI 安全工具之外、嵌在開發流中的「即時安全護欄」。 [claudepluginhub](https://www.claudepluginhub.com/plugins/anthropics-claude-security-guidance-plugins-security-guidance)

***

[詳細重點整理]

1. 外掛目的與角色定位 [00:00]  
- 這個 **security-guidance 外掛程式**會在你使用 Claude Code 時自動審查 Claude 所做的程式碼變更，盡量在 PR 之前攔截常見漏洞，降低人工 Code Review 的安全負擔。 [helpnetsecurity](https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/)
- 它是工作階段內的輔助工具，負責「提早發現並修復」；PR 階段再交給 **Code Review** 多代理審查補漏，後面仍可搭配 CI 中的靜態分析與套件掃描器做更嚴格的把關。 [claude](https://claude.com/product/claude-security)

  關鍵概念：**縱深防禦（Defense in Depth）**

2. 前置需求與安裝條件 [02:15]  
- 必須使用 Claude Code CLI 2.1.144 以上版本並在 PATH 中具備 Python 3.8+，外掛會優先嘗試 `python3`、`python` 或 `py -3` 來建立自己的執行環境。 [github](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
- 工作目錄必須是 git 儲存庫，回合結束與提交審查會依賴 git diff；若不在 repo 中則只執行每次編輯的模式檢查。首次執行時會在 `~/.claude/security/` 建立虛擬環境並安裝 Claude Agent SDK，失敗時會退回為一次性審查模式。 [github](https://github.com/anthropics/claude-plugins-official)

  關鍵概念：**代理模式（Agentic Review Mode）**

3. 外掛安裝與啟用流程（本機工作階段） [04:30]  
- 在 Claude Code 工作階段中，透過官方 Anthropic 市集安裝：`/plugin install security-guidance@claude-plugins-official`，如找不到市集需先 ` /plugin marketplace add anthropics/claude-plugins-official` 再重試。 [github](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
- 安裝後執行 `/reload-plugins` 讓目前工作階段載入外掛，之後外掛會自動運行，不需要再手動呼叫指令即可開始進行安全檢查。 [helpnetsecurity](https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/)

  關鍵概念：**自動載入外掛（Auto-loaded Plugin）**

4. 在雲端工作階段與共享專案啟用 [06:10]  
- user scope 的外掛只存在於本機，用不到網頁版 Claude Code；若要在雲端工作階段或共享 repo 中生效，需要在專案 `.claude/settings.json` 宣告：`"enabledPlugins": { "security-guidance@claude-plugins-official": true }`。 [github](https://github.com/anthropics/claude-plugins-official)
- 企業管理員可透過受管理設定，在組織層級統一設定 `enabledPlugins`，讓團隊所有成員一打開專案就享有同一套安全護欄配置。 [github](https://github.com/anthropics/claude-plugins-official)

  關鍵概念：**專案／組織層級啟用（Project & Org Scoped Enablement）**

5. 三個審查時間點與深度層級 [08:20]  
- 外掛在三個時間點審查 Claude 的變更：每次檔案編輯後、每個回合結束時，以及 Claude 透過 Bash 執行 git commit 或 git push 時，各自對應不同深度與成本的檢查。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time)
- 使用者可為每個層級新增自訂規則；內建檢查無法單獨關閉，但可以透過環境變數分別停用每一層，或直接關閉所有模型支援審查。 [helpnetsecurity](https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/)

  關鍵概念：**多層次安全檢查（Layered Security Checks）**

6. 每次檔案編輯後的模式檢查 [10:00]  
- 當 Claude 透過 Edit/Write 類工具寫入檔案後，外掛會以字串或正規表達式比對方式掃描新內容中的高風險模式，不呼叫模型，因此不增加用量成本。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time)
- 典型偵測項目包含動態程式碼執行（如 eval/new Function、os.system、child_process.exec）、不安全反序列化（如 pickle）、以及 DOM 注入相關 API（dangerouslySetInnerHTML、innerHTML、document.write），也會特別注意 `.github/workflows/` 之類具高權限影響的檔案。 [claudemarketplaces](https://claudemarketplaces.com/plugins/anthropics-claude-code/security-guidance)

  關鍵概念：**模式比對檢查（Pattern-based Scanning）**

7. 模式檢查的告警行為與自訂規則 [12:05]  
- 每個模式在相同工作階段、同一檔案中只會觸發一次警告，以避免對話被重複訊息洗版；警告會被附加到 Claude 下一步的上下文中，讓 Claude 自己在後續編輯中修正問題。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time)
- 使用者可在 `.claude/security-patterns.yaml`（或 .yml/.json）中新增自訂規則，透過 substrings／regex、paths／exclude_paths 等欄位設定專案特有的敏感模式（如 API key 前綴、多租戶未過濾查詢等）。外掛最多載入約 50 條自訂規則，並會跳過有災難性回溯風險的正則。 [backslash](https://www.backslash.security/blog/claude-code-security-best-practices)

  關鍵概念：**可擴充安全規則（Extensible Security Patterns）**

8. 每個回合結束的模型審查 [14:30]  
- 一個回合指「你送出訊息 → Claude 執行工作與修改 → Claude 回覆」這整個 cycle；回合結束後，外掛會計算此次工作樹的 git diff（包含編輯工具、Bash 指令、子代理變更），並送給一個專注安全的 Claude 實例做獨立審查。 [claude](https://claude.com/product/claude-security)
- 這層模型審查可偵測字串比對看不到的問題，例如授權繞過、不安全直接物件參考、注入攻擊、伺服器端請求偽造與弱加密等，若有問題會在後續回合以提示方式要求 Claude 修正。 [anthropic](https://www.anthropic.com/product/security)

  關鍵概念：**模型支援安全審查（Model-assisted Review）**

9. 回合審查的邊界條件 [16:20]  
- 每次回合最多覆蓋約 30 個已修改檔案，並且連續觸發約三次後會暫停，等你處理完現有問題再繼續，以避免過度噪音。 [helpnetsecurity](https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/)
- 這個審查在背景執行，不影響 Claude 主回應時間，但仍會消耗與一般請求相同的模型用量，預設使用 Claude Opus 4.7，也可以透過 `SECURITY_REVIEW_MODEL` 環境變數切換模型。 [claude](https://claude.com/product/claude-security)

  關鍵概念：**背景非阻塞審查（Background Non-blocking Review）**

10. 提交與推送時的代理式深度審查 [18:00]  
- 當 Claude 在 Bash 工具裡執行 `git commit` 或 `git push` 時，外掛會觸發更深層的代理式審查，閱讀周邊程式碼（呼叫者、消毒函式、相關檔案），用更多上下文降低誤報，再將確認的問題回報給 Claude 處理。 [anthropic](https://www.anthropic.com/product/security)
- 這個階段只會對 Claude 透過 Bash 執行的 git 操作生效，開發者自己在 shell 中做的 commit/push 不會被審查；審查每小時約有 20 次滾動上限，且若與回合結束審查重複，Claude 不會再收到二次提示，以保持訊息乾淨。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time)

  關鍵概念：**代理式深度審查（Agentic Deep Review）**

11. 指南檔與安全規則的多層合併 [20:15]  
- 外掛會從使用者目錄與專案目錄依序搜尋 `claude-security-guidance.md` 與 `security-patterns` 檔案，包含 `~/.claude/`、`.claude/` 與 `.claude/*.local.*` 三個層級，並將可用的指引內容串接，合計大小上限約 8 KB。 [backslash](https://www.backslash.security/blog/claude-code-security-best-practices)
- 管理員可透過裝置管理或版本控制，分發組織層級的指南檔與模式檔案，讓整個團隊共用同一套安全 baseline，再由個別專案或個人透過 local 變體做加成。 [backslash](https://www.backslash.security/blog/claude-code-security-best-practices)

  關鍵概念：**分層安全政策（Layered Security Policy）**

12. 收費模式與模型設定 [22:10]  
- 每次編輯的模式檢查不使用模型，因此完全不增加費用；回合結束與提交審查會各自額外消耗模型用量，計入與其他 Claude 請求相同的用量配額。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time)
- 提交審查屬於代理式流程，一次提交可能引發多次模型互動；可透過 `SECURITY_REVIEW_MODEL` 控制回合審查、`SG_AGENTIC_MODEL` 控制提交審查所用模型，讓團隊在成本與精度之間做平衡。 [claude](https://claude.com/product/claude-security)

  關鍵概念：**成本感知安全配置（Cost-aware Security Config）**

13. 停用、解除安裝與層級控制 [24:00]  
- 若要在保留外掛安裝的前提下調整層級，可設定環境變數：`ENABLE_PATTERN_RULES=0` 停用每次編輯模式檢查、`ENABLE_STOP_REVIEW=0` 停用回合結束審查、`ENABLE_COMMIT_REVIEW=0` 停用提交／推送審查，`ENABLE_CODE_SECURITY_REVIEW=0` 一次關閉所有模型審查，`SECURITY_GUIDANCE_DISABLE=1` 則完全停用外掛。 [github](https://github.com/anthropics/claude-plugins-official)
- 若只想在使用者層級暫停外掛，可用 `/plugin disable security-guidance@claude-plugins-official`，而 `/plugin uninstall` 則會從 user scope 中完全卸載；若外掛是透過專案設定或受管理設定啟用，停用行為會寫入 local 設定或需要管理員操作，不會影響其他成員。 [github](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)

  關鍵概念：**細粒度停用控制（Granular Disable Controls）**

14. 與 hooks 的整合運作機制 [26:10]  
- 外掛完全建立在 Claude Code 的 **hooks** 機制上，並註冊 `SessionStart`、`UserPromptSubmit`、`PostToolUse`（編輯與 Bash）、`Stop` 等事件，在適當時機啟動 Python 環境、記錄 git baseline、進行模式檢查與背景審查。 [github](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
- 這個外掛是「從 hook 裡啟動獨立模型呼叫並把結果回寫到工作階段」的實作範例，若要自訂安全流程，可以參考其原始碼設計自己的 hook 型外掛或安全檢查。 [backslash](https://www.backslash.security/blog/claude-code-security-best-practices)

  關鍵概念：**事件導向安全 hook（Event-driven Security Hooks）**

15. 與其他安全工具的協作位置 [28:00]  
- 在整體工具堆疊中，此外掛負責「工作階段內」的即時檢查與修補；之上可以用 `/security-review` 做一次性分支安全檢查，PR 階段使用 Code Review 多代理審查，CI 再由既有 SAST／依賴掃描器涵蓋語言特定規則與供應鏈風險。 [anthropic](https://www.anthropic.com/product/security)
- 每一階段都能補上前一階段漏掉的問題，因此外掛設計成不阻擋寫入或提交，而是把發現的問題當作額外提示交給開發者與 Claude 協作處理，而非單一完整解決方案。 [anthropic](https://www.anthropic.com/product/security)

  關鍵概念：**安全責任分層（Layered Responsibility）**

***

[技術/數據對比]

常見安全檢查層級與工具角色對照表  

| 階段           | 工具／機制                         | 覆蓋範圍與特性                                                                 |
|----------------|------------------------------------|-------------------------------------------------------------------------------|
| 編輯器中       | **security-guidance 外掛**        | 即時模式比對＋輕量模型審查，攔截常見漏洞並在同一工作階段修復。 [kucoin](https://www.kucoin.com/news/flash/anthropic-launches-security-guidance-plugin-for-claude-code-to-detect-vulnerabilities-in-real-time) |
| 按需（本機）   | `/security-review` 指令           | 由開發者主動啟動，對當前分支做一次性安全掃描。 [claude](https://claude.com/product/claude-security)             |
| Pull Request   | Claude Code Review（Team/Enterprise） | 多代理、具完整程式碼庫上下文的正確性與安全審查。 [claude](https://claude.com/product/claude-security)            |
| CI／管線階段   | SAST／依賴掃描／政策檢查          | 語言特定規則、供應鏈與政策強制執行，補足 AI 審查以外的組織要求。 [claude](https://claude.com/product/claude-security) |

***

[結論與行動建議]

- 啟發金句：  
  **「讓 AI 在寫程式的當下就帶著『安全意識』，遠比事後補破洞便宜得多。」**  

- 具體行動建議（F-D-L 法則）：  
  - F（First setup）：先在常用的 repo 裡完成一次完整設定（安裝外掛、設定 `.claude/settings.json`、建立 `claude-security-guidance.md`）。  
  - D（Define rules）：用 `claude-security-guidance.md` 與 `security-patterns.yaml` 明確寫出你們團隊的威脅模型與敏感模式。  
  - L（Loop check）：在日常開發中觀察每次編輯與回合結束後的警告，建立「寫完一段，就看一次安全提示」的習慣。  

- 生活／工作實踐建議：  
  - 在你負責的關鍵服務（例如多租戶 SaaS 或金流相關模組）先導入此外掛，針對「日誌不能記敏感 ID、多租戶必須帶 org_id、管理路由必須做權限檢查」等規則，寫進 `claude-security-guidance.md`；之後讓 Claude 幫你「自動提醒自己」，逐步把這些安全要求變成團隊的肌肉記憶，而不是靠每次腦中 checklist。  

[參考連結]  
- security-guidance 外掛資訊與市集條目： [claudepluginhub](https://www.claudepluginhub.com/plugins/anthropics-claude-security-guidance-plugins-security-guidance)
- 官方 Claude Code plugins 儲存庫（含 hooks 與外掛設計範例）： [github](https://github.com/anthropics/claude-plugins-official)
- Claude 安全能力與 Code Review 相關介紹： [claude](https://claude.com/product/claude-security)
