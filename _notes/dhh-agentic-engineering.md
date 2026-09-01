---
title: 'DHH：從 AI 懷疑者到 100% 代理派'
date: 2026-09-01
image: /images/AI筆記/dhh-agentic-engineering.jpg
category: AI筆記
tags: [代理分水嶺, 品味瓶頸, 策略性模糊, 計畫可攜性, 溫度即創造力]
description: 'DHH（Ruby on Rails 之父、37signals CTO）在 13 個月內從 AI 懷疑者翻轉為 100% 代理派：自 2025/11/24 Opus 4.5 起，Agent 從自動補全進化到自選路徑。'
quote: '「無法認知此刻重量的人，才是活在妄想裡。」——不承認世界已經天翻地覆，才是真正的精神病。'
action: '🎯依 P-P-R 法則實踐：Problem 只描述問題與期望結果、善用策略性模糊；Prototype 先做最小版本親自使用再迭代；Review 實作用 A 家模型、審查用 B 家獨立來源，不受信任的代碼一律在隔離 VM 執行。'
source_has_timestamps: true
source_raw: DHH
---

# [核心摘要]

DHH(Ruby on Rails 之父、37signals CTO)在 13 個月內從 AI 懷疑者翻轉為 100% 代理派：自 2025/11/24 Opus 4.5 起，Agent 從自動補全進化到自選路徑。他以零手寫程式碼、純品味導航，三個月打造出 Linux 發行版 Omarchy Quattro。核心翻轉：實作趨近免費，稀缺的只剩願景、品味與判斷力。 [youtube](https://www.youtube.com/watch?v=NYFGCESmikA)

***

# [詳細重點整理]

## 1. 三階段代理演化：從自動補全到全權委託 [02:56]

- 前代理時代：聊天機器人是好導師，但不改變「親手鑿程式碼」的工作本質 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- **2025/11/24 Opus 4.5 分水嶺**：模型未必更聰明，躍進的是 harness——工具使用、自我檢查、儀器化電腦的能力，讓產出「近乎自己親手寫的」 [startuphub](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/agentic-engineering-is-now-writing-all-the-code)
- 2026 初春：sub-agents 出現，任務拆分給八個子代理並行，耗時縮至 1/5~1/10,但人仍在駕駛座 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 2026 夏季(Opus 5、Fable、GPT Sol):人只描述模糊問題，Agent 自選路徑。GPS 類比——早期導航怕被帶進港灣，現在車自己會開 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 網頁 CRUD 類應用可達 100% AI 生成；安全關鍵系統(核電廠、自駕車)仍需細看 [lexfridman](https://lexfridman.com/dhh-2-transcript)

關鍵概念：**代理分水嶺**

## 2. 大型組織為何沒加速：瓶頸不在實作 [18:14]

- 有人類團隊協作時，瓶頸是 human bandwidth 與溝通：PM、設計師、VP、CTO 都想參與 shaping,生產力就死在那裡 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 10X/100X/1000X 提升只發生在人「直接」面對 Agent,中間不能有人類中介 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 多數組織卡的不是實作，而是 ideas、vision、taste;Microsoft 數萬程式師數十年沒做出偉大軟體即是明證 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- Basecamp 5 教訓：放任設計師 vibe coding,個別 PR 都合理、合起來摧毀系統架構，最後靠人工清理收拾殘局 [lexfridman](https://lexfridman.com/dhh-2-transcript)

關鍵概念：**品味瓶頸**

## 3. 開源的宗教改革時刻 [27:30]

- 三個月內合併超過 1,000 個 PR;Omarchy 上約 400 個未合併 PR,一週內翻倍 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- Agent 產出的 PR 打敗中位數人類工程師：bug report 資訊齊全、說明 why、補註解、寫單元測試 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 拒絕 Agent 的 PR 不傷任何人感情——維護者神經質的義務感得以解除 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 新流程：Agent 預審 PR、在 VM 驗證修復、只把「可合併決策」摘要給人類 [lexfridman](https://lexfridman.com/dhh-2-transcript)

關鍵概念：**去仲介化**(程式設計師祭司階層瓦解，如馬丁路德 95 條釘上教會大門) [lexfridman](https://lexfridman.com/dhh-2-transcript)

## 4. Vibe Coding vs 代理工程 [47:05]

- 定義：vibe coding = 告訴 Agent 去建、完全不看實作；若還會審視實作的形狀與比例，那是另一回事 [zhiding](https://www.zhiding.cn/gaofei/2026/0828/3197787.shtml)
- 程式設計師不必然更擅長：寫軟體大半是產品管理(做什麼、給誰、V1 邊界)，這技能在開發者間分布不均 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 老手的陷阱是過度指定：Opus 5 的 system prompt 縮減了 80%,因為太多指令反而傷害模型表現 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 敏捷 25 年前的教訓重演：沒人知道自己要什麼，直到用過——先做小版本、實際使用、再迭代；也可請模型先給多個替代方案 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)

關鍵概念：**策略性模糊**

## 5. 手寫程式終結，但架構價值仍在 [1:00:06]

- 美觀一致的程式碼依然值錢——不再是因為人要讀，而是 token 稀缺：Agent 能一次掌握、無需重學整個 context 的系統，修改成本更低 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)
- 放任架構爛成 ball of mud,每個 PR 都要付出代價 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)

關鍵概念：**Token 經濟學**

## 6. 給程式設計師的建議 [1:10:24]

- 不要預測任何事：連這領域最頂尖的人也不知道兩代模型後的世界長什麼樣 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 知識不會囤積：去背包旅行一年，兩週就能追上前線——数千人同時在試錯與篩選，你只需來收割結果 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 只愛打字寫 code 機械部分的人會辛苦；愛「做出東西」的人不會。允許自己為舊工藝哀悼一陣子 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**無囤積焦慮**

## 7. 工作環境：16 執行緒、4 台機器、一人瓶頸 [1:31:46]

- 拋棄 IDE,回歸終端機：tmux 分頁 → 改用 Herdr,Agent 需要決策時主動通知；Neovim 降級為專案瀏覽器，用來讀 diff 與周邊程式碼 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 四台 mini PC + KVM + WireGuard 網路，約 16 個並行執行緒——硬體還能撐，人撐不住；像跑一小時賽車般耗神，無法永續 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)
- 對策：建造能隔夜自主消化 PR 與 issue 的 bot,每天寄一封「只剩這些待決」的 email;37signals 實驗讓 Agent 當 Basecamp 同事，用 to-do 指派而非 chat(chat 會讓人坐著乾等) [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**平行流 / 人類瓶頸**

## 8. 速度癡迷：45 秒安裝的作業系統 [1:44:11]

- 新 Mac 要 42 分鐘才可用、Windows 要 90 分鐘;Omarchy 安裝低於 60 秒(紀錄 45 秒)，硬體客製映像的目標是 12 秒 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 手法樸實：使用者回答五個問題的同時預載套件;砍映像體積(JetBrains 字型從 200 MB 縮到 16 MB) [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- McLaren 工程師為 1,400 公斤賽車減 370 克的類比；引 Mitchell Hashimoto:「對卓越的追求無需解釋」 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**永久性回報**(省下的一秒，之後的每天都持續省下)

## 9. 模型實測:Python 函式庫移植到 Rust [2:21:05]

- 情境：單一 prompt、零 Rust 知識、一行程式碼未審 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- Fable 產出八步計畫、45 分鐘完成大半，但訂閱額度中途耗盡，由 Opus 5 拿著同一份計畫接手完成——證明**好計畫可跨模型移植** [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 總排名：Fable 最佳、Opus 5 第二；Sol 與 Grok 4.6 以約 1/10 的 token 成本緊追 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**計畫可攜性**

## 10. Harness 與雙模型四眼審查 [2:37:55]

- 標準工作流：一家模型實作、另一家供應商的模型審查——用 Claude 建、Codex 最高設定審，近期加入 Grok;連 Copilot 都已從噪音升級到值得重新打開 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- Shopify CTO 對真實生產事故的研究：Agent 審查的 PR 造成的停機比人類審查的更少 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 37signals 資安團隊被 Agent 找到的漏洞修補洪流淹沒；最狠一句：沒看到洪流不代表你安全，只代表你是瞎的、而你的對手不是 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**獨立來源審查**

## 11. 自主代理的安全設計 [2:58:20]

- Omarchy 自主 bot 的設計：coordinator 指揮多個 worker 在隔離 VM 中執行，不受信任的 PR 代碼與測試輸出不進入受信任環境 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)
- 系統自行發現：對抗性的測試回饋可能污染模型後續的決策 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)

關鍵概念：**信任邊界隔離**

## 12. Linux 將贏得桌面 [3:38:35]

- Linux 三十年來被嘲笑的一切——一切皆 config file、一切皆 CLI、人類讀不懂的錯誤訊息——正是 Agent 最需要的介面；Agent 認得整台機器的原始碼,能解讀那則密碼錯誤訊息 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- Omarchy 內建 crash watcher,當機時主動提議去查明原因;熱鍵只能用滑鼠改的封閉 OS,在這個時代反而是障礙 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 連 Linus Torvalds 都歡迎 AI 貢獻核心;Omarchy 基金會獲 800 萬美元支持，三天內湧入 330 個插件 [podscripts](https://podscripts.co/podcasts/the-standup-with-theprimeagen/dhh-omarchy-quattro-announcement)

關鍵概念：**Agent 原生作業系統**

## 13. 程式設計的未來：英語是最美的程式語言 [3:59:24]

- 「如果有一種程式語言比 Ruby 更美，那就是英語。」 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 溫度不是缺陷而是創造力來源：溫度設 0 會得到每次相同的答案，但也永遠不會比你已想到的更好——沒有隨機性就沒有創造力,模型與人皆然 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- Lex 的補充：好 prompt 的特質是策略性模糊——過度指定，模型照字面服從，你得到自己的答案而非更好的答案;寫太模糊則得到隨機。這個時代的技能更像「編輯」而非「打字」 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

關鍵概念：**溫度即創造力**

> 影片後半另有人生議題章節：AI 影片生成與電影 [2:50:57]、為人父 [3:10:28]、PewDiePie [3:49:51]、政治與移民 [4:22:17]、長壽與過度優化 [4:53:54]、永恆輪迴 [5:05:38],非技術重點故未展開。 [youtube](https://www.youtube.com/watch?v=NYFGCESmikA)

***

# [結論與行動建議]

**啟發金句**

> 「無法認知此刻重量的人，才是活在妄想裡。」——不承認世界已經天翻地覆，才是真正的精神病。 [lexfridman](https://lexfridman.com/dhh-2-transcript)

**具體行動建議:P-P-R 法則**

- **Problem**:描述問題與期望結果，不規定實作路徑；善用策略性模糊，讓模型提出你沒想到的更好解法 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- **Prototype**:先做最小版本、親自使用後再迭代；必要時請模型一次給多個替代方案，用人類的比較判斷力做篩選 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)
- **Review**:實作用 A 家模型、審查用 B 家(獨立來源)；關鍵層(model layer)人工把關，不受信任的代碼一律在隔離 VM 執行 [with-agents](https://with-agents.dev/summaries/coding-with-agents/dhh-future-of-programming-ai-agentic-engineering/)

**生活實踐建議**

- 對 AI 顧問與架構審查工作：客戶的痛點已從「寫不出來」移轉到「不知道要什麼」與「誰守護架構一致性」——顧問價值應重新定位在願景、品味與審查治理，而非產能 [lexfridman](https://lexfridman.com/dhh-2-transcript)
- 在自己的 Gitea + MCP + LLM gateway 工作流中實踐計畫可攜性:把 Fable 級模型產出的計畫存成工件，交由低成本模型執行，用 gateway 依任務分級路由，直接管理那 24 倍的價差 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)
- 維護 side project 或開源庫：讓 Agent 預審 PR、VM 驗證、產出決策摘要，人只保留合併決策；用「每天一封 email」的非同步節奏，取代全程盯梢 16 個執行緒的燃燒 [zensoftware](https://zensoftware.cloud/articles/dhh-on-programming-with-ai-agents)

***

# [參考連結]

- 原始 YouTube 影片：[https://youtu.be/NYFGCESmikA](https://youtu.be/NYFGCESmikA)
- 官方逐字稿:[https://lexfridman.com/dhh-2-transcript](https://lexfridman.com/dhh-2-transcript)