# GPT Image 2 Gen Skill

<p align="center">
  <strong>Generación de imágenes con IA usando GPT Image 2 — instala con un comando, empieza a crear en segundos.</strong>
</p>

<p align="center">
  <a href="#generación-con-gpt-image-2">GPT Image 2</a> •
  <a href="#instalación">Instalar</a> •
  <a href="#obtener-una-api-key">API Key</a> •
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

> **¿Eres un AI Agent?** Salta el README — ve directamente a [**llms-install.md**](llms-install.md) para instrucciones de instalación paso a paso diseñadas para ti.

---

## ¿Qué es esto?

Un skill para [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) impulsado por [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill). Instala el skill y tu AI agent podrá generar y editar imágenes usando GPT Image 2.

| Skill | Descripción | Modelo |
|-------|-------------|--------|
| **GPT Image 2 Gen** | Texto a imagen, edición de imágenes, generación por lotes | GPT Image 2 (OpenAI) |

---

## Instalación

### Instalación rápida (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### Instalar vía npm (Recomendado)

```bash
npx evolink-gpt-image
```

Modo no interactivo (para AI agents / CI):

```bash
npx evolink-gpt-image -y
```

Instalar en un directorio específico:

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### Instalación manual

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## Obtener una API Key

1. Regístrate en [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. Ve a Dashboard -> API Keys
3. Crea una nueva clave
4. Configúrala en tu entorno:

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## Generación con GPT Image 2

Genera y edita imágenes con IA a través de conversación natural con tu AI agent.

### Capacidades

- **Texto a imagen** — Describe lo que quieres, obtén una imagen
- **Edición de imágenes** — Proporciona imágenes de referencia (1-16) y describe los cambios
- **Generación por lotes** — Genera hasta 10 imágenes por solicitud
- **Múltiples tamaños** — 15 presets de proporción + dimensiones personalizadas en píxeles
- **Niveles de resolución** — 1K (~1MP), 2K (~4MP), 4K (~8.3MP)
- **Niveles de calidad** — Low (rápido), Medium (equilibrado), High (mejor)
- **Prompts potentes** — Hasta 32,000 caracteres por prompt

### Ejemplos de uso

Simplemente habla con tu agent:

> "Genera una imagen de un atardecer sobre el océano"

> "Crea un logo minimalista, 1024x1024, alta calidad"

> "Edita esta imagen — añade un gato junto a la persona"

> "Genera 4 variaciones de un robot pixel art en 4K"

### Requisitos

- `curl` y `jq` instalados en tu sistema
- Variable de entorno `EVOLINK_API_KEY` configurada

### Referencia del script

```bash
# Texto a imagen (básico)
./scripts/gpt-image-gen.sh "Un hermoso atardecer sobre el océano"

# Alta calidad 4K panorámico
./scripts/gpt-image-gen.sh "Paisaje urbano cinematográfico al atardecer" --size 16:9 --resolution 4K --quality high

# Dimensiones personalizadas
./scripts/gpt-image-gen.sh "Logo minimalista" --size 1024x1024

# Edición de imagen
./scripts/gpt-image-gen.sh "Añade un gato junto a ella" --image "https://example.com/photo.png"

# Generación por lotes
./scripts/gpt-image-gen.sh "Robot pixel art" --count 4 --quality high

# Prueba en seco (previsualizar payload)
./scripts/gpt-image-gen.sh "Prompt de prueba" --dry-run
```

### Parámetros de la API

Consulta [references/api-params.md](references/api-params.md) para la documentación completa de la API.

---

## Estructura de archivos

```
.
├── README.md                    # Documentación en inglés
├── SKILL.md                     # Definición del skill (para AI agents)
├── _meta.json                   # Metadatos del skill
├── bin/
│   └── cli.js                   # CLI del instalador npm
├── references/
│   └── api-params.md            # Referencia completa de parámetros de la API
└── scripts/
    └── gpt-image-gen.sh         # Script de generación de imágenes
```

---

## Solución de problemas

| Problema | Solución |
|----------|----------|
| `jq: command not found` | Instala jq: `apt install jq` / `brew install jq` |
| `401 Unauthorized` | Verifica tu `EVOLINK_API_KEY` en [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | Añade créditos en [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| Contenido bloqueado | El prompt fue marcado por moderación — modifica tu descripción |
| Imagen demasiado grande | Las imágenes de referencia deben ser <=50MB cada una |
| Tiempo de generación agotado | Las imágenes pueden tardar 5-90s. Prueba con menor calidad/resolución primero. |

---

## Compatibilidad

| Agent | Método de instalación |
|-------|----------------------|
| **OpenClaw** | `openclaw skills add <repo>` o `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <tu-directorio-de-skills>` |

---

## Licencia

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
