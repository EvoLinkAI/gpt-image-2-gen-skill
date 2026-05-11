# Packy Provider Workflow

Use this document only when the selected provider is `packy`.

## Provider Identity

- Provider name: `packy`
- Script: `{SKILL_DIR}/scripts/packyapi.py`
- Required environment variable: `PACKY_API_KEY`
- Dependencies: `curl`

## Supported Capabilities

- Text-to-image
- Ratio sizes, exact pixel sizes, and `auto`
- Quality control: `low`, `medium`, `high`, `auto`
- Output format selection: `png`, `jpeg`, `webp`

## Current Limitations

- `--count` currently supports only `1`
- `--image` is not supported
- `--resolution` is not supported
- `--callback` is not supported
- The current script is synchronous and does not expose an async task workflow

## Command Pattern

```bash
python {SKILL_DIR}/scripts/packyapi.py "prompt" [options]
```

Examples:

```bash
python {SKILL_DIR}/scripts/packyapi.py "A beautiful sunset over the ocean"
python {SKILL_DIR}/scripts/packyapi.py "Minimalist logo design" --size 1024x1024 --quality medium
python {SKILL_DIR}/scripts/packyapi.py "Cinematic skyline at dusk" --size 16:9 --quality high --output-format png
```

## Parameters

- `--size <ratio|WxH|auto>`
- `--quality <low|medium|high|auto>`
- `--count 1`
- `--output-format <png|jpeg|webp>`
- `--dry-run`

## Execution Model

Packy uses a synchronous request flow.

1. Build the request payload.
2. Submit one HTTP request through `curl`.
3. Parse the returned JSON response.
4. Emit image URLs from the response.

There is no separate task submission, polling, or timeout recovery protocol like the EvoLink script.

## Output Protocol

Parse these lines from stdout and stderr:

| Line format | Meaning | Action |
|-------------|---------|--------|
| `INFO: ...` | Request start information | Optional progress context. |
| `IMAGE_URL=<url>` | Generated image URL | Return the image URL to the user. |
| `DRY_RUN: ...` | Payload preview mode | Do not treat as a real generation result. |
| `ERROR: ...` | Failure | Surface the message clearly. |

The current script does not emit `TASK_SUBMITTED`, `STATUS_UPDATE`, `ELAPSED`, or `POLL_TIMEOUT`.

## Error Guidance

- Missing `PACKY_API_KEY`: Ask the user to set the Packy API key.
- Unsupported parameter: Explain that the chosen Packy script does not support that option.
- `curl` execution failure: Surface the stderr summary when available.
- Invalid JSON response: Explain that the provider returned an unexpected response.
- Missing image URL in response: Explain that generation did not return usable image URLs.

## Notes

- Packy requests are currently sent via `curl` from Python to avoid HTTP client fingerprint issues seen with `urllib`.
- This provider document should stay aligned with `scripts/packyapi.py` rather than the EvoLink async workflow.
