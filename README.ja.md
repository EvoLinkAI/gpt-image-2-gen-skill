# GPT Image 2 Gen Skill

<p align="center">
  <strong>GPT Image 2 による AI 画像生成 — ワンコマンドでインストール、すぐに作成開始。</strong>
</p>

<p align="center">
  <a href="#gpt-image-2-画像生成">GPT Image 2</a> •
  <a href="#インストール">インストール</a> •
  <a href="#api-key-の取得">API Key</a> •
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

> **AI Agent ですか？** README をスキップして、[**llms-install.md**](llms-install.md) に直接アクセスしてください。AI Agent 向けのインストール手順が記載されています。

---

## これは何ですか？

[OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) 向けの skill で、[EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) を利用しています。この skill をインストールすると、AI agent が GPT Image 2 を使って画像の生成・編集ができるようになります。

| Skill | 説明 | モデル |
|-------|------|--------|
| **GPT Image 2 Gen** | テキストから画像生成、画像編集、バッチ生成 | GPT Image 2 (OpenAI) |

---

## インストール

### クイックインストール（OpenClaw）

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### npm でインストール（推奨）

```bash
npx evolink-gpt-image
```

非対話モード（AI agent / CI 向け）：

```bash
npx evolink-gpt-image -y
```

特定のディレクトリにインストール：

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### 手動インストール

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## API Key の取得

1. [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) でサインアップ
2. Dashboard -> API Keys に移動
3. 新しいキーを作成
4. 環境変数に設定：

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## GPT Image 2 画像生成

AI agent との自然な会話を通じて AI 画像を生成・編集できます。

### 機能

- **テキストから画像** — 欲しいものを説明すると画像を生成
- **画像編集** — 参照画像（1-16枚）を提供して編集内容を説明
- **バッチ生成** — 1リクエストで最大10枚の画像を生成
- **複数サイズ** — 15種類の比率プリセット + カスタムピクセルサイズ
- **解像度レベル** — 1K（約1MP）、2K（約4MP）、4K（約8.3MP）
- **品質レベル** — Low（高速）、Medium（バランス）、High（最高品質）
- **長文プロンプト** — 1回あたり最大32,000文字

### 使用例

agent に話しかけるだけ：

> 「海に沈む夕日の画像を生成して」

> 「ミニマリストなロゴを作成、1024x1024、高品質」

> 「この画像を編集 — 人物の隣に猫を追加して」

> 「ピクセルアートのロボットを4Kで4パターン生成して」

### 必要条件

- システムに `curl` と `jq` がインストール済み
- 環境変数 `EVOLINK_API_KEY` が設定済み

### スクリプトリファレンス

```bash
# テキストから画像（基本）
./scripts/gpt-image-gen.sh "海に沈む美しい夕日"

# 高品質 4K ワイドスクリーン
./scripts/gpt-image-gen.sh "夕暮れの未来都市スカイライン" --size 16:9 --resolution 4K --quality high

# カスタムピクセルサイズ
./scripts/gpt-image-gen.sh "ミニマリストロゴ" --size 1024x1024

# 画像編集
./scripts/gpt-image-gen.sh "彼女の隣に猫を追加" --image "https://example.com/photo.png"

# バッチ生成
./scripts/gpt-image-gen.sh "ピクセルアートロボット" --count 4 --quality high

# ドライラン（ペイロードのプレビュー）
./scripts/gpt-image-gen.sh "テストプロンプト" --dry-run
```

### API パラメータ

完全な API ドキュメントは [references/api-params.md](references/api-params.md) を参照してください。

---

## ファイル構成

```
.
├── README.md                    # 英語ドキュメント
├── SKILL.md                     # Skill 定義（AI agent 用）
├── _meta.json                   # Skill メタデータ
├── bin/
│   └── cli.js                   # npm インストーラー CLI
├── references/
│   └── api-params.md            # 完全な API パラメータリファレンス
└── scripts/
    └── gpt-image-gen.sh         # 画像生成スクリプト
```

---

## トラブルシューティング

| 問題 | 解決策 |
|------|--------|
| `jq: command not found` | jq をインストール：`apt install jq` / `brew install jq` |
| `401 Unauthorized` | `EVOLINK_API_KEY` を確認：[evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | クレジットを追加：[evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| コンテンツがブロックされた | プロンプトがモデレーションに引っかかりました — 説明を修正してください |
| 画像が大きすぎる | 参照画像は1枚あたり50MB以下にしてください |
| 生成タイムアウト | 画像生成には5-90秒かかります。まず低品質/低解像度で試してください。 |

---

## 互換性

| Agent | インストール方法 |
|-------|-----------------|
| **OpenClaw** | `openclaw skills add <repo>` または `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <skills-ディレクトリ>` |

---

## ライセンス

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
