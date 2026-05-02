# GPT Image 2 Gen Skill

<p align="center">
  <strong>Генерация изображений с помощью ИИ на базе GPT Image 2 — установка одной командой, создание за секунды.</strong>
</p>

<p align="center">
  <a href="#генерация-изображений-gpt-image-2">GPT Image 2</a> •
  <a href="#установка">Установка</a> •
  <a href="#получение-api-key">API Key</a> •
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

> **AI Agent?** Пропустите README — перейдите сразу к [**llms-install.md**](llms-install.md) для пошаговой инструкции по установке, разработанной для AI Agent'ов.

---

## Что это?

Skill для [OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode) на базе [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill). Установите skill, и ваш AI agent получит возможность генерировать и редактировать изображения с помощью GPT Image 2.

| Skill | Описание | Модель |
|-------|----------|--------|
| **GPT Image 2 Gen** | Текст в изображение, редактирование изображений, пакетная генерация | GPT Image 2 (OpenAI) |

---

## Установка

### Быстрая установка (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### Установка через npm (Рекомендуется)

```bash
npx evolink-gpt-image
```

Неинтерактивный режим (для AI agent'ов / CI):

```bash
npx evolink-gpt-image -y
```

Установка в определённую директорию:

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### Ручная установка

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## Получение API Key

1. Зарегистрируйтесь на [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)
2. Перейдите в Dashboard -> API Keys
3. Создайте новый ключ
4. Установите переменную окружения:

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## Генерация изображений GPT Image 2

Генерируйте и редактируйте ИИ-изображения через естественный диалог с вашим AI agent'ом.

### Возможности

- **Текст в изображение** — Опишите что хотите, получите изображение
- **Редактирование изображений** — Предоставьте референсные изображения (1-16) и опишите правки
- **Пакетная генерация** — Генерируйте до 10 изображений за запрос
- **Множество размеров** — 15 пресетов соотношений + пользовательские размеры в пикселях
- **Уровни разрешения** — 1K (~1МП), 2K (~4МП), 4K (~8,3МП)
- **Уровни качества** — Low (быстро), Medium (сбалансировано), High (лучшее)
- **Мощные промпты** — До 32 000 символов на промпт

### Примеры использования

Просто поговорите с вашим agent'ом:

> «Сгенерируй изображение заката над океаном»

> «Создай минималистичный логотип, 1024x1024, высокое качество»

> «Отредактируй это изображение — добавь кота рядом с человеком»

> «Сгенерируй 4 варианта пиксельного робота в 4K»

### Требования

- `curl` и `jq` установлены в системе
- Переменная окружения `EVOLINK_API_KEY` установлена

### Справка по скрипту

```bash
# Текст в изображение (базовый)
./scripts/gpt-image-gen.sh "Красивый закат над океаном"

# Высокое качество 4K широкоформатный
./scripts/gpt-image-gen.sh "Кинематографичный городской пейзаж в сумерках" --size 16:9 --resolution 4K --quality high

# Пользовательские размеры в пикселях
./scripts/gpt-image-gen.sh "Минималистичный логотип" --size 1024x1024

# Редактирование изображения
./scripts/gpt-image-gen.sh "Добавь кота рядом с ней" --image "https://example.com/photo.png"

# Пакетная генерация
./scripts/gpt-image-gen.sh "Пиксельный робот" --count 4 --quality high

# Тестовый запуск (предпросмотр payload)
./scripts/gpt-image-gen.sh "Тестовый промпт" --dry-run
```

### Параметры API

Полную документацию API см. в [references/api-params.md](references/api-params.md).

---

## Структура файлов

```
.
├── README.md                    # Документация на английском
├── SKILL.md                     # Определение skill (для AI agent'ов)
├── _meta.json                   # Метаданные skill
├── bin/
│   └── cli.js                   # CLI npm-установщика
├── references/
│   └── api-params.md            # Полный справочник параметров API
└── scripts/
    └── gpt-image-gen.sh         # Скрипт генерации изображений
```

---

## Устранение неполадок

| Проблема | Решение |
|----------|---------|
| `jq: command not found` | Установите jq: `apt install jq` / `brew install jq` |
| `401 Unauthorized` | Проверьте `EVOLINK_API_KEY`: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | Пополните баланс: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| Контент заблокирован | Промпт отмечен модерацией — измените описание |
| Изображение слишком большое | Референсные изображения должны быть <=50МБ каждое |
| Таймаут генерации | Генерация может занять 5-90с. Попробуйте сначала более низкое качество/разрешение. |

---

## Совместимость

| Agent | Способ установки |
|-------|-----------------|
| **OpenClaw** | `openclaw skills add <repo>` или `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <ваша-директория-skills>` |

---

## Лицензия

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
