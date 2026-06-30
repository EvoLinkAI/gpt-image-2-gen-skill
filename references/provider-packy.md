# Packy Provider Workflow

Use this document only when the selected provider is `packy`.

## Provider Identity

- Provider name: `packy`
- Generation script: `{SKILL_DIR}/scripts/packyapi.py`
- Edit script: `{SKILL_DIR}/scripts/packy_edit.py`
- Required environment variable: `PACKY_API_KEY`
- Dependencies: `curl`

## Supported Capabilities

- Text-to-image
- Image editing / image-to-image through `POST /v1/images/edits` with multipart file upload
- Ratio sizes, exact pixel sizes, and `auto`
- Quality control: `low`, `medium`, `high`, `auto`
- Output format selection: `png`, `jpeg`, `webp` for generation; prefer `png` or `jpeg` for edits

## Current Limitations

- `--count` currently supports only `1`
- `--resolution` is not supported
- `--callback` is not supported
- The current script is synchronous and does not expose an async task workflow

## Command Pattern

```bash
python {SKILL_DIR}/scripts/packyapi.py "prompt" [options]
python {SKILL_DIR}/scripts/packy_edit.py "prompt" --image ./input.png [options]
```

Examples:

```bash
python {SKILL_DIR}/scripts/packyapi.py "A beautiful sunset over the ocean"
python {SKILL_DIR}/scripts/packyapi.py "Minimalist logo design" --size 1024x1024 --quality medium
python {SKILL_DIR}/scripts/packyapi.py "Cinematic skyline at dusk" --size 16:9 --quality high --output-format png
python {SKILL_DIR}/scripts/packy_edit.py "Add a cat next to her" --image "./photo.png"
python {SKILL_DIR}/scripts/packy_edit.py "Turn this sketch into a polished product render" --image "./concept.png" --size 1:1
python {SKILL_DIR}/scripts/packy_edit.py "Only replace the background with a light gray studio wall" --image "./product.png" --mask "./mask.png" --input-fidelity high --output-format png
```

## Parameters

- `--size <ratio|WxH|auto>`
- `--quality <low|medium|high|auto>`
- `--count 1`
- `--output-compression <0-100>` for JPEG output only
- `--background <opaque>`
- `--moderation <auto|low>`
- `--user <string>`
- `--response-format <url>`
- `--output-format <png|jpeg|webp>`
- `--dry-run`

Edit-only parameters:
- `--image <local-file-path>`
- `--mask <local-png-path>`
- `--input-fidelity <high>`

## Execution Model

Packy uses a synchronous request flow.

1. Use `packyapi.py` for text-to-image requests and submit JSON to `/v1/images/generations`.
2. Use `packy_edit.py` for image edits and submit multipart form data to `/v1/images/edits`.
3. Parse the returned JSON response.
4. Emit image URLs from the response.

There is no separate task submission, polling, or timeout recovery protocol like the EvoLink script.

## Edit Input Rules

- Packy edits require a local file path for `--image` because the helper uploads the binary file with multipart form data.
- Only one source image is supported per request.
- `--mask` is optional and should usually be a PNG file for local edit regions.
- Prefer `--input-fidelity high` when the user wants to preserve the original subject and details.
- Prefer `png` or `jpeg` output for edits. Do not recommend `webp`.
- `transparent` background is not supported by the current helper for either generation or edits.
- The current helper intentionally only supports `response_format=url`.

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
- This provider document should stay aligned with `scripts/packyapi.py`, `scripts/packy_edit.py`, and `scripts/packy_common.py` rather than the EvoLink async workflow.
