# EvoLink Provider Workflow

Use this document only when the selected provider is `evolink`.

## Provider Identity

- Provider name: `evolink`
- Script: `{SKILL_DIR}/scripts/gpt-image-gen.sh`
- Required environment variable: `EVOLINK_API_KEY`
- Dependencies: `jq`, `curl`

## Supported Capabilities

- Text-to-image
- Image editing with reference image URLs
- Batch generation with `--count 1-10`
- Ratio sizes, exact pixel sizes, and `auto`
- Resolution tiers with ratio sizes: `1K`, `2K`, `4K`
- HTTPS callback URL

## Command Pattern

```bash
EVOLINK_API_KEY=$EVOLINK_API_KEY {SKILL_DIR}/scripts/gpt-image-gen.sh "prompt" [options]
```

Examples:

```bash
EVOLINK_API_KEY=$EVOLINK_API_KEY {SKILL_DIR}/scripts/gpt-image-gen.sh "A beautiful sunset over the ocean"
EVOLINK_API_KEY=$EVOLINK_API_KEY {SKILL_DIR}/scripts/gpt-image-gen.sh "Cinematic skyline at dusk" --size 16:9 --resolution 4K --quality high
EVOLINK_API_KEY=$EVOLINK_API_KEY {SKILL_DIR}/scripts/gpt-image-gen.sh "Add a cute kitten next to her" --image "https://example.com/input.png" --size 1:1
EVOLINK_API_KEY=$EVOLINK_API_KEY {SKILL_DIR}/scripts/gpt-image-gen.sh "Pixel art cute robot" --size 1:1 --resolution 2K --quality high --count 4
```

## Parameters

- `--image <url[,url,...]>`: Reference image URLs for editing
- `--size <ratio|WxH|auto>`
- `--resolution <1K|2K|4K>`
- `--quality <low|medium|high>`
- `--count <1-10>`
- `--callback <https://...>`
- `--dry-run`

## Execution Model

EvoLink uses an async task flow.

1. Submit generation request.
2. Extract the task id.
3. Poll task status until completion or timeout.
4. Emit final image URLs when available.

The script handles its own polling internally and may run for up to 5 minutes.

## Output Protocol

Parse these lines from stdout and stderr:

| Line format | Meaning | Action |
|-------------|---------|--------|
| `TASK_SUBMITTED: task_id=<id> estimated=<Ns>` | Request succeeded and is queued | Do not rerun automatically. Confirm generation has started. |
| `STATUS_UPDATE: <message>` | Progress update during polling | Relay or summarize progress for the user. |
| `IMAGE_URL=<url>` | Generated image URL | Return the image URL to the user. |
| `ELAPSED=<Ns>` | Total generation time | Optionally mention the duration. |
| `POLL_TIMEOUT: task_id=<id> dashboard=<url>` | Local polling timed out | Tell the user the image may still complete and they should check the dashboard. |
| `RESULT_JSON=...` | Raw final response summary | Use for debugging only when needed. |
| `ERROR: ...` | Failure | Surface the message clearly. |

## Critical Rules

- Once you see `TASK_SUBMITTED:`, the request has already been queued on the server.
- Do not rerun the script unless the user explicitly asks to retry.
- If polling times out, the task may still be running on the server.

## Error Guidance

- `401`: Invalid or missing API key.
- `402`: Insufficient balance.
- `403`: Access denied or token lacks model access.
- `429`: Rate limit exceeded.
- `400`: Invalid parameters, moderation block, or image size problem.
- `503`: Service temporarily unavailable.

## Notes

- Dashboard: `https://evolink.ai/dashboard`
- For detailed API behavior, also see `references/api-params.md`.
