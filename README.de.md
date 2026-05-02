# GPT Image 2 Gen Skill

<p align="center">
  <strong>KI-Bildgenerierung mit GPT Image 2 — mit einem Befehl installieren, sofort loslegen.</strong>
</p>

<p align="center">
  <a href="#gpt-image-2-bildgenerierung">GPT Image 2</a> •
  <a href="#installation">Installation</a> •
  <a href="#api-key-erhalten">API Key</a> •
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

> **AI Agent?** Überspringe die README — gehe direkt zu [**llms-install.md**](llms-install.md) für eine Schritt-für-Schritt-Installationsanleitung für AI Agents.

---

## Was ist das?

Ein Skill für [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode), betrieben von [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill). Installiere den Skill und dein AI Agent kann Bilder mit GPT Image 2 generieren und bearbeiten.

| Skill | Beschreibung | Modell |
|-------|-------------|--------|
| **GPT Image 2 Gen** | Text-zu-Bild, Bildbearbeitung, Batch-Generierung | GPT Image 2 (OpenAI) |

---

## Installation

### Schnellinstallation (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### Installation über npm (Empfohlen)

```bash
npx evolink-gpt-image
```

Nicht-interaktiver Modus (für AI Agents / CI):

```bash
npx evolink-gpt-image -y
```

In ein bestimmtes Verzeichnis installieren:

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### Manuelle Installation

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## API Key erhalten

1. Registriere dich bei [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. Gehe zu Dashboard -> API Keys
3. Erstelle einen neuen Schlüssel
4. Setze die Umgebungsvariable:

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## GPT Image 2 Bildgenerierung

Generiere und bearbeite KI-Bilder durch natürliche Konversation mit deinem AI Agent.

### Funktionen

- **Text-zu-Bild** — Beschreibe was du willst, erhalte ein Bild
- **Bildbearbeitung** — Stelle Referenzbilder (1-16) bereit und beschreibe die Änderungen
- **Batch-Generierung** — Generiere bis zu 10 Bilder pro Anfrage
- **Verschiedene Größen** — 15 Seitenverhältnis-Presets + benutzerdefinierte Pixelmaße
- **Auflösungsstufen** — 1K (~1MP), 2K (~4MP), 4K (~8,3MP)
- **Qualitätsstufen** — Low (schnell), Medium (ausgewogen), High (beste Qualität)
- **Leistungsstarke Prompts** — Bis zu 32.000 Zeichen pro Prompt

### Verwendungsbeispiele

Sprich einfach mit deinem Agent:

> „Generiere ein Bild eines Sonnenuntergangs über dem Meer"

> „Erstelle ein minimalistisches Logo, 1024x1024, hohe Qualität"

> „Bearbeite dieses Bild — füge eine Katze neben der Person hinzu"

> „Generiere 4 Variationen eines Pixel-Art-Roboters in 4K"

### Voraussetzungen

- `curl` und `jq` auf deinem System installiert
- Umgebungsvariable `EVOLINK_API_KEY` gesetzt

### Skript-Referenz

```bash
# Text-zu-Bild (einfach)
./scripts/gpt-image-gen.sh "Ein wunderschöner Sonnenuntergang über dem Meer"

# Hohe Qualität 4K Breitbild
./scripts/gpt-image-gen.sh "Filmische Stadtlandschaft in der Abenddämmerung" --size 16:9 --resolution 4K --quality high

# Benutzerdefinierte Pixelmaße
./scripts/gpt-image-gen.sh "Minimalistisches Logo" --size 1024x1024

# Bildbearbeitung
./scripts/gpt-image-gen.sh "Füge eine Katze neben ihr hinzu" --image "https://example.com/photo.png"

# Batch-Generierung
./scripts/gpt-image-gen.sh "Pixel-Art-Roboter" --count 4 --quality high

# Testlauf (Payload-Vorschau)
./scripts/gpt-image-gen.sh "Test-Prompt" --dry-run
```

### API-Parameter

Siehe [references/api-params.md](references/api-params.md) für die vollständige API-Dokumentation.

---

## Dateistruktur

```
.
├── README.md                    # Englische Dokumentation
├── SKILL.md                     # Skill-Definition (für AI Agents)
├── _meta.json                   # Skill-Metadaten
├── bin/
│   └── cli.js                   # npm-Installer CLI
├── references/
│   └── api-params.md            # Vollständige API-Parameter-Referenz
└── scripts/
    └── gpt-image-gen.sh         # Bildgenerierungsskript
```

---

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| `jq: command not found` | jq installieren: `apt install jq` / `brew install jq` |
| `401 Unauthorized` | `EVOLINK_API_KEY` prüfen: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | Guthaben aufladen: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| Inhalt blockiert | Prompt wurde von der Moderation markiert — Beschreibung anpassen |
| Bild zu groß | Referenzbilder müssen jeweils <=50MB sein |
| Generierungs-Timeout | Bilder können 5-90s dauern. Versuche zuerst niedrigere Qualität/Auflösung. |

---

## Kompatibilität

| Agent | Installationsmethode |
|-------|---------------------|
| **OpenClaw** | `openclaw skills add <repo>` oder `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <dein-skills-verzeichnis>` |

---

## Lizenz

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
