# GPT Image 2 Gen Skill

<p align="center">
  <strong>GPT Image 2를 활용한 AI 이미지 생성 — 한 줄 명령으로 설치, 바로 시작.</strong>
</p>

<p align="center">
  <a href="#gpt-image-2-이미지-생성">GPT Image 2</a> •
  <a href="#설치">설치</a> •
  <a href="#api-key-발급">API Key</a> •
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

> **AI Agent인가요?** README를 건너뛰고 [**llms-install.md**](llms-install.md)로 바로 이동하세요. AI Agent를 위한 단계별 설치 가이드가 있습니다.

---

## 이것은 무엇인가요?

[OpenClaw](https://github.com/openclaw/openclaw) / [Claude Code](https://github.com/anthropics/claude-code) / [OpenCode](https://github.com/opencode-ai/opencode)용 skill로, [EvoLink](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)로 구동됩니다. 이 skill을 설치하면 AI agent가 GPT Image 2를 사용하여 이미지를 생성하고 편집할 수 있습니다.

| Skill | 설명 | 모델 |
|-------|------|------|
| **GPT Image 2 Gen** | 텍스트-이미지 변환, 이미지 편집, 배치 생성 | GPT Image 2 (OpenAI) |

---

## 설치

### 빠른 설치 (OpenClaw)

```bash
openclaw skills add https://github.com/EvoLinkAI/gpt-image-2-gen-skill
```

### npm으로 설치 (권장)

```bash
npx evolink-gpt-image
```

비대화형 모드 (AI agent / CI용):

```bash
npx evolink-gpt-image -y
```

특정 디렉토리에 설치:

```bash
npx evolink-gpt-image -y --path ~/.claude/skills
```

### 수동 설치

```bash
git clone https://github.com/EvoLinkAI/gpt-image-2-gen-skill.git
cd gpt-image-2-gen-skill
openclaw skills add .
```

---

## API Key 발급

1. [evolink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill)에서 가입
2. Dashboard -> API Keys로 이동
3. 새 키 생성
4. 환경 변수 설정:

```bash
export EVOLINK_API_KEY=your_key_here
```

---

## GPT Image 2 이미지 생성

AI agent와의 자연스러운 대화를 통해 AI 이미지를 생성하고 편집하세요.

### 기능

- **텍스트-이미지 변환** — 원하는 것을 설명하면 이미지 생성
- **이미지 편집** — 참조 이미지(1-16장)를 제공하고 편집 내용 설명
- **배치 생성** — 요청당 최대 10장의 이미지 생성
- **다양한 크기** — 15가지 비율 프리셋 + 사용자 정의 픽셀 크기
- **해상도 등급** — 1K (~1MP), 2K (~4MP), 4K (~8.3MP)
- **품질 등급** — Low (빠름), Medium (균형), High (최고)
- **강력한 프롬프트** — 프롬프트당 최대 32,000자

### 사용 예시

agent에게 말하기만 하면 됩니다:

> "바다 위 일몰 이미지를 생성해줘"

> "미니멀리스트 로고 만들어줘, 1024x1024, 고품질"

> "이 이미지를 편집해줘 — 사람 옆에 고양이를 추가해"

> "픽셀 아트 로봇 4K로 4가지 변형 생성해줘"

### 요구 사항

- 시스템에 `curl`과 `jq` 설치 필요
- `EVOLINK_API_KEY` 환경 변수 설정 필요

### 스크립트 참조

```bash
# 텍스트-이미지 (기본)
./scripts/gpt-image-gen.sh "바다 위의 아름다운 일몰"

# 고품질 4K 와이드스크린
./scripts/gpt-image-gen.sh "황혼의 미래 도시 스카이라인" --size 16:9 --resolution 4K --quality high

# 사용자 정의 픽셀 크기
./scripts/gpt-image-gen.sh "미니멀리스트 로고" --size 1024x1024

# 이미지 편집
./scripts/gpt-image-gen.sh "그녀 옆에 고양이 추가" --image "https://example.com/photo.png"

# 배치 생성
./scripts/gpt-image-gen.sh "픽셀 아트 로봇" --count 4 --quality high

# 드라이 런 (페이로드 미리보기)
./scripts/gpt-image-gen.sh "테스트 프롬프트" --dry-run
```

### API 파라미터

전체 API 문서는 [references/api-params.md](references/api-params.md)를 참조하세요.

---

## 파일 구조

```
.
├── README.md                    # 영문 문서
├── SKILL.md                     # Skill 정의 (AI agent용)
├── _meta.json                   # Skill 메타데이터
├── bin/
│   └── cli.js                   # npm 설치 CLI
├── references/
│   └── api-params.md            # 전체 API 파라미터 참조
└── scripts/
    └── gpt-image-gen.sh         # 이미지 생성 스크립트
```

---

## 문제 해결

| 문제 | 해결 방법 |
|------|-----------|
| `jq: command not found` | jq 설치: `apt install jq` / `brew install jq` |
| `401 Unauthorized` | `EVOLINK_API_KEY` 확인: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| `402 Payment Required` | 크레딧 충전: [evolink.ai/dashboard](https://evolink.ai/dashboard?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill) |
| 콘텐츠 차단됨 | 프롬프트가 콘텐츠 검토에 걸렸습니다 — 설명을 수정하세요 |
| 이미지가 너무 큼 | 참조 이미지는 각 50MB 이하여야 합니다 |
| 생성 시간 초과 | 이미지 생성에 5-90초 소요됩니다. 먼저 낮은 품질/해상도로 시도하세요. |

---

## 호환성

| Agent | 설치 방법 |
|-------|-----------|
| **OpenClaw** | `openclaw skills add <repo>` 또는 `npx evolink-gpt-image` |
| **Claude Code** | `npx evolink-gpt-image -y --path ~/.claude/skills` |
| **OpenCode** | `npx evolink-gpt-image -y --path ~/.opencode/skills` |
| **Cursor** | `npx evolink-gpt-image -y --path <skills-디렉토리>` |

---

## 라이선스

MIT

---

<p align="center">
  Powered by <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gpt-image-2-gen-skill"><strong>EvoLink</strong></a> — Unified AI API Gateway
</p>
