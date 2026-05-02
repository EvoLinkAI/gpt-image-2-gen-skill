# GPT Image 2 Gen Skill

<p align="center">
  <strong>Geração de imagens com IA usando GPT Image 2 — instale com um comando, comece a criar em segundos.</strong>
</p>

<p align="center">
  <a href="#geração-com-gpt-image-2">GPT Image 2</a> •
  <a href="#instalação">Instalar</a> •
  <a href="#obter-uma-api-key">API Key</a> •
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

> **AI Agent?** Pule o README — vá direto para [**llms-install.md**](llms-install.md) para instruções de instalação passo a passo projetadas para você.

---

## O que é isso?

Um skill para [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) alimentado por [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill). Instale o skill e seu AI agent ganha a capacidade de gerar e editar imagens usando GPT Image 2.

| Skill | Descrição | Modelo |
|-------|-----------|--------|
| **GPT Image 2 Gen** | Texto para imagem, edição de imagens, geração em lote | GPT Image 2 (OpenAI) |

---

## Instalação

### Instalação rápida (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### Instalar via npm (Recomendado)

```bash
npx evolink-gpt-image
```

Modo não interativo (para AI agents / CI):

```bash
npx evolink-gpt-image -y
```

Instalar em um diretório específico:

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### Instalação manual

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## Obter uma API Key

1. Cadastre-se em [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. Vá para Dashboard -> API Keys
3. Crie uma nova chave
4. Configure no seu ambiente:

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## Geração com GPT Image 2

Gere e edite imagens com IA através de conversa natural com seu AI agent.

### Capacidades

- **Texto para imagem** — Descreva o que você quer, receba uma imagem
- **Edição de imagens** — Forneça imagens de referência (1-16) e descreva as edições
- **Geração em lote** — Gere até 10 imagens por solicitação
- **Múltiplos tamanhos** — 15 presets de proporção + dimensões personalizadas em pixels
- **Níveis de resolução** — 1K (~1MP), 2K (~4MP), 4K (~8.3MP)
- **Níveis de qualidade** — Low (rápido), Medium (equilibrado), High (melhor)
- **Prompts poderosos** — Até 32.000 caracteres por prompt

### Exemplos de uso

Simplesmente converse com seu agent:

> "Gere uma imagem de um pôr do sol sobre o oceano"

> "Crie um logo minimalista, 1024x1024, alta qualidade"

> "Edite esta imagem — adicione um gato ao lado da pessoa"

> "Gere 4 variações de um robô pixel art em 4K"

### Requisitos

- `curl` e `jq` instalados no seu sistema
- Variável de ambiente `EVOLINK_API_KEY` configurada

### Referência do script

```bash
# Texto para imagem (básico)
./scripts/gpt-image-gen.sh "Um belo pôr do sol sobre o oceano"

# Alta qualidade 4K widescreen
./scripts/gpt-image-gen.sh "Paisagem urbana cinematográfica ao entardecer" --size 16:9 --resolution 4K --quality high

# Dimensões personalizadas
./scripts/gpt-image-gen.sh "Logo minimalista" --size 1024x1024

# Edição de imagem
./scripts/gpt-image-gen.sh "Adicione um gato ao lado dela" --image "https://example.com/photo.png"

# Geração em lote
./scripts/gpt-image-gen.sh "Robô pixel art" --count 4 --quality high

# Teste (pré-visualizar payload)
./scripts/gpt-image-gen.sh "Prompt de teste" --dry-run
```

### Parâmetros da API

Consulte [references/api-params.md](references/api-params.md) para documentação completa da API.

---

## Estrutura de arquivos

```
.
├── README.md                    # Documentação em inglês
├── SKILL.md                     # Definição do skill (para AI agents)
├── _meta.json                   # Metadados do skill
├── bin/
│   └── cli.js                   # CLI do instalador npm
├── references/
│   └── api-params.md            # Referência completa de parâmetros da API
└── scripts/
    └── gpt-image-gen.sh         # Script de geração de imagens
```

---

## Solução de problemas

| Problema | Solução |
|----------|---------|
| `jq: command not found` | Instale jq: `apt install jq` / `brew install jq` |
| `401 Unauthorized` | Verifique sua `EVOLINK_API_KEY` em [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | Adicione créditos em [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| Conteúdo bloqueado | O prompt foi sinalizado pela moderação — modifique sua descrição |
| Imagem muito grande | Imagens de referência devem ter <=50MB cada |
| Tempo de geração esgotado | Imagens podem levar 5-90s. Tente menor qualidade/resolução primeiro. |

---

## Compatibilidade

| Agent | Método de instalação |
|-------|---------------------|
| **OpenClaw** | `openclaw skills add <repo>` ou `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <seu-diretório-de-skills>` |

---

## Licença

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
