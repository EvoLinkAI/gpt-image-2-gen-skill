# GPT Image 2 Gen Skill

<p align="center">
  <strong>GPT Image 2 AI 圖像生成 — 一條命令安裝，秒級上手。</strong>
</p>

<p align="center">
  <a href="#gpt-image-2-圖像生成">GPT Image 2</a> •
  <a href="#安裝">安裝</a> •
  <a href="#取得-api-key">API Key</a> •
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill">EvoLink</a>
</p>

<p align="center">
  <strong>Languages:</strong>
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.tr.md">Türkçe</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <a href="https://docs.evolink.ai/en/api-manual/image-series/gpt-image-2/gpt-image-2-image-generation?utm_source=github&utm_medium=banner&utm_campaign=gpt-image-2-gen-skill">
    <img src="assets/banner.jpg" alt="GPT Image 2 banner" width="100%" />
  </a>
</p>

---

> **AI Agent？** 跳過 README — 直接前往 [**llms-install.md**](llms-install.md)，裡面有專為 AI Agent 設計的安裝步驟。

---

## 這是什麼？

一個適用於 [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) 的 AI 技能外掛，由 [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) 驅動。安裝後，你的 AI Agent 即可使用 GPT Image 2 模型進行圖像生成和編輯。

| 技能 | 說明 | 模型 |
|------|------|------|
| **GPT Image 2 Gen** | 文字轉圖像、圖像編輯、批次生成 | GPT Image 2 (OpenAI) |

---

## 安裝

### 快速安裝（OpenClaw）

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### 透過 npm 安裝（推薦）

```bash
npx evolink-gpt-image
```

非互動模式（適用於 AI Agent / CI）：

```bash
npx evolink-gpt-image -y
```

安裝到指定目錄：

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### 手動安裝

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## 取得 API Key

1. 註冊 [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. 前往控制台 -> API Keys
3. 建立新金鑰
4. 設定環境變數：

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## GPT Image 2 圖像生成

透過與 AI Agent 的自然對話來生成和編輯 AI 圖像。

### 功能

- **文字轉圖像** — 描述你想要的，生成圖像
- **圖像編輯** — 提供參考圖片（1-16張），描述編輯內容
- **批次生成** — 單次請求最多生成 10 張圖像
- **多種尺寸** — 15 種比例預設 + 自訂像素尺寸
- **解析度等級** — 1K（~1百萬像素）、2K（~4百萬像素）、4K（~830萬像素）
- **品質等級** — Low（快速）、Medium（平衡）、High（最佳）
- **超長提示詞** — 單次最多 32,000 字元

### 使用範例

直接和你的 AI Agent 對話：

> 「生成一張海面日落的圖片」

> 「建立一個極簡 Logo，1024x1024，高品質」

> 「編輯這張圖片 — 在人物旁邊加一隻貓」

> 「生成 4 張像素風格機器人的變體，4K 解析度」

### 系統需求

- 系統已安裝 `curl` 和 `jq`
- 已設定 `EVOLINK_API_KEY` 環境變數

### 命令列腳本

```bash
# 文字轉圖像（基礎）
./scripts/gpt-image-gen.sh "海面上絢麗多彩的美麗日落"

# 高品質 4K 寬螢幕
./scripts/gpt-image-gen.sh "黃昏時分未來都市天際線" --size 16:9 --resolution 4K --quality high

# 自訂像素尺寸
./scripts/gpt-image-gen.sh "極簡主義 Logo 設計" --size 1024x1024

# 圖像編輯
./scripts/gpt-image-gen.sh "在她旁邊加一隻可愛的小貓" --image "https://example.com/photo.png"

# 批次生成
./scripts/gpt-image-gen.sh "像素風格的可愛機器人" --count 4 --quality high

# 測試執行（預覽 payload）
./scripts/gpt-image-gen.sh "測試提示詞" --dry-run
```

### API 參數

完整 API 文件請參閱 [references/api-params.md](references/api-params.md)。

---

## 檔案結構

```
.
├── README.md                    # 英文文件
├── SKILL.md                     # 技能定義（供 AI Agent 使用）
├── _meta.json                   # 技能中繼資料
├── bin/
│   └── cli.js                   # npm 安裝器 CLI
├── references/
│   └── api-params.md            # 完整 API 參數參考
└── scripts/
    └── gpt-image-gen.sh         # 圖像生成腳本
```

---

## 常見問題

| 問題 | 解決方案 |
|------|----------|
| `jq: command not found` | 安裝 jq：`apt install jq` / `brew install jq` |
| `401 Unauthorized` | 檢查 `EVOLINK_API_KEY`：[evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | 儲值：[evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| 內容被攔截 | 提示詞觸發了內容審核，請修改描述 |
| 圖片太大 | 參考圖片每張不超過 50MB |
| 生成逾時 | 圖像生成通常需要 5-90 秒，可先降低品質/解析度 |

---

## 相容性

| Agent | 安裝方式 |
|-------|----------|
| **OpenClaw** | `openclaw skills add <repo>` 或 `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <你的技能目錄>` |

---

## 授權條款

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — 統一 AI API 閘道
</p>
