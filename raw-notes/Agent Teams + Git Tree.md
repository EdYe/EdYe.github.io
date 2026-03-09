## Claude Agent Teams + Git Worktree

核心概念是：**每個 agent 在自己的 worktree 工作，互不干擾，最後再整合**。

---

### 為什麼這個組合很強大？

Claude agent（如 Claude Code）在執行任務時會大量讀寫檔案。如果多個 agent 共用同一個工作目錄，會互相衝突。Worktree 讓每個 agent 有**獨立的沙盒環境**，卻共享同一份 git 歷史。

---

### 基本架構

```
repo/                    ← 主分支（orchestrator agent 在這裡）
repo-agent-1/            ← agent 1 的 worktree（做 feature A）
repo-agent-2/            ← agent 2 的 worktree（做 feature B）
repo-agent-3/            ← agent 3 的 worktree（寫測試）
```

---

### 工作流程

**1. Orchestrator 拆解任務並建立 worktree**

```bash
# orchestrator 分析任務後，為每個 subagent 準備環境
git worktree add ../repo-agent-1 -b feature/auth main
git worktree add ../repo-agent-2 -b feature/api main
git worktree add ../repo-agent-3 -b feature/tests main
```

**2. 各 subagent 在自己的 worktree 平行工作**

每個 agent 收到的 prompt 中包含：
- 明確的任務範圍
- 自己的工作目錄路徑（例如 `../repo-agent-1`）
- 不應該碰的檔案範圍

**3. Subagent 完成後 commit**

```bash
# 每個 agent 在自己的分支上 commit
cd ../repo-agent-1
git add .
git commit -m "feat: implement auth module"
```

**4. Orchestrator 整合結果**

```bash
# 回到主目錄進行 merge 或 review
cd repo
git merge feature/auth
git merge feature/api
git merge feature/tests

# 清理 worktree
git worktree remove ../repo-agent-1
git worktree remove ../repo-agent-2
git worktree remove ../repo-agent-3
```

---

### 實際 Prompt 設計技巧

給 subagent 的指令應該包含：

```
你是負責實作 authentication 模組的 agent。
你的工作目錄是：/path/to/repo-agent-1
你只能修改以下路徑的檔案：src/auth/
完成後請執行：git add . && git commit -m "feat: ..."
不要修改 package.json 或任何設定檔。
```

---

### 衝突預防策略

| 策略 | 說明 |
|------|------|
| **檔案所有權劃分** | 每個 agent 負責不同的目錄，明確界定邊界 |
| **介面先行** | orchestrator 先定義 API 介面/型別，agent 再實作 |
| **唯讀共享檔** | 設定檔、schema 等由 orchestrator 管理，agent 只讀不寫 |
| **分支命名規則** | `agent/{task-id}/description` 方便追蹤 |

---

### 進階：動態建立 worktree 的腳本

```bash
#!/bin/bash
# setup-agents.sh

TASKS=("auth" "api" "tests" "docs")
BASE_BRANCH="main"
REPO_NAME=$(basename $(pwd))

for task in "${TASKS[@]}"; do
  BRANCH="agent/$(date +%Y%m%d)/$task"
  DIR="../${REPO_NAME}-${task}"
  
  git worktree add "$DIR" -b "$BRANCH" "$BASE_BRANCH"
  echo "✅ Created worktree for $task at $DIR"
done
```

---

### 適合的任務類型

- **平行開發**：前端/後端/測試同時進行
- **大型重構**：不同模組分別處理
- **多版本維護**：agent 同時在 v1、v2 上 backport 修復
- **Code review + 修改**：一個 agent review，另一個 agent 修改

這個模式的精髓是：**git worktree 解決了檔案系統層面的隔離問題**，讓 agent parallelism 真正可行。