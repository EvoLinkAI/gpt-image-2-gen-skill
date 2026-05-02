# GPT Image 2 Gen Skill

<p align="center">
  <strong>Génération d'images IA avec GPT Image 2 — installez en une commande, créez en quelques secondes.</strong>
</p>

<p align="center">
  <a href="#génération-gpt-image-2">GPT Image 2</a> •
  <a href="#installation">Installation</a> •
  <a href="#obtenir-une-api-key">API Key</a> •
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

> **AI Agent ?** Passez le README — allez directement à [**llms-install.md**](llms-install.md) pour des instructions d'installation étape par étape conçues pour vous.

---

## Qu'est-ce que c'est ?

Un skill pour [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) propulsé par [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill). Installez le skill et votre AI agent pourra générer et éditer des images avec GPT Image 2.

| Skill | Description | Modèle |
|-------|-------------|--------|
| **GPT Image 2 Gen** | Texte vers image, édition d'images, génération par lots | GPT Image 2 (OpenAI) |

---

## Installation

### Installation rapide (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### Installation via npm (Recommandé)

```bash
npx evolink-gpt-image
```

Mode non interactif (pour AI agents / CI) :

```bash
npx evolink-gpt-image -y
```

Installer dans un répertoire spécifique :

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### Installation manuelle

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## Obtenir une API Key

1. Inscrivez-vous sur [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. Allez dans Dashboard -> API Keys
3. Créez une nouvelle clé
4. Configurez la variable d'environnement :

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## Génération GPT Image 2

Générez et éditez des images IA par conversation naturelle avec votre AI agent.

### Fonctionnalités

- **Texte vers image** — Décrivez ce que vous voulez, obtenez une image
- **Édition d'images** — Fournissez des images de référence (1-16) et décrivez les modifications
- **Génération par lots** — Générez jusqu'à 10 images par requête
- **Tailles multiples** — 15 presets de ratio + dimensions personnalisées en pixels
- **Niveaux de résolution** — 1K (~1MP), 2K (~4MP), 4K (~8,3MP)
- **Niveaux de qualité** — Low (rapide), Medium (équilibré), High (meilleur)
- **Prompts puissants** — Jusqu'à 32 000 caractères par prompt

### Exemples d'utilisation

Parlez simplement à votre agent :

> « Génère une image d'un coucher de soleil sur l'océan »

> « Crée un logo minimaliste, 1024x1024, haute qualité »

> « Édite cette image — ajoute un chat à côté de la personne »

> « Génère 4 variations d'un robot pixel art en 4K »

### Prérequis

- `curl` et `jq` installés sur votre système
- Variable d'environnement `EVOLINK_API_KEY` configurée

### Référence du script

```bash
# Texte vers image (basique)
./scripts/gpt-image-gen.sh "Un magnifique coucher de soleil sur l'océan"

# Haute qualité 4K écran large
./scripts/gpt-image-gen.sh "Paysage urbain cinématographique au crépuscule" --size 16:9 --resolution 4K --quality high

# Dimensions personnalisées
./scripts/gpt-image-gen.sh "Logo minimaliste" --size 1024x1024

# Édition d'image
./scripts/gpt-image-gen.sh "Ajoute un chat à côté d'elle" --image "https://example.com/photo.png"

# Génération par lots
./scripts/gpt-image-gen.sh "Robot pixel art" --count 4 --quality high

# Test (aperçu du payload)
./scripts/gpt-image-gen.sh "Prompt de test" --dry-run
```

### Paramètres de l'API

Consultez [references/api-params.md](references/api-params.md) pour la documentation complète de l'API.

---

## Structure des fichiers

```
.
├── README.md                    # Documentation en anglais
├── SKILL.md                     # Définition du skill (pour AI agents)
├── _meta.json                   # Métadonnées du skill
├── bin/
│   └── cli.js                   # CLI de l'installateur npm
├── references/
│   └── api-params.md            # Référence complète des paramètres API
└── scripts/
    └── gpt-image-gen.sh         # Script de génération d'images
```

---

## Dépannage

| Problème | Solution |
|----------|----------|
| `jq: command not found` | Installer jq : `apt install jq` / `brew install jq` |
| `401 Unauthorized` | Vérifiez votre `EVOLINK_API_KEY` sur [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | Ajoutez des crédits sur [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| Contenu bloqué | Le prompt a été signalé par la modération — modifiez votre description |
| Image trop volumineuse | Les images de référence doivent faire <=50 Mo chacune |
| Délai de génération dépassé | Les images peuvent prendre 5-90s. Essayez d'abord une qualité/résolution inférieure. |

---

## Compatibilité

| Agent | Méthode d'installation |
|-------|----------------------|
| **OpenClaw** | `openclaw skills add <repo>` ou `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <votre-répertoire-skills>` |

---

## Licence

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
