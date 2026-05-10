---
name: gpt-image-2-gen
description: GPT Image 2 image generation skill with multiple providers. Supports a shared image-generation workflow plus provider-specific execution via EvoLink or Packy. Works with OpenClaw, Claude Code, OpenCode, Cursor. Powered by OpenAI GPT Image 2.
homepage: https://github.com/EvoLinkAI/gpt-image-2-gen-skill
metadata: {"openclaw":{"homepage":"https://github.com/EvoLinkAI/gpt-image-2-gen-skill","requires":{"bins":["jq","curl"],"env":["GPT_IMAGE_PROVIDER","EVOLINK_API_KEY","PACKY_API_KEY"]},"primaryEnv":"GPT_IMAGE_PROVIDER"}}
---

# GPT Image 2 Generation

An interactive AI image generation assistant powered by the GPT Image 2 model, with provider-specific execution through EvoLink or Packy.

## When to Activate This Skill

Activate this skill when the user asks to:
- Generate / create / make an image or picture
- Edit / modify an existing image
- Use GPT Image 2 or gpt-image-2
- Create AI art, illustrations, logos, icons, or any visual content
- Batch-generate image variations

Keywords: image, picture, illustration, photo, art, logo, icon, generate image, create image, image editing, gpt-image, text-to-image

## Script Locations

All script paths in this file are relative to the directory containing this `SKILL.md` file.

```text
SKILL_DIR = directory containing this SKILL.md
EvoLink script = {SKILL_DIR}/scripts/gpt-image-gen.sh
Packy script = {SKILL_DIR}/scripts/packyapi.py
EvoLink workflow doc = {SKILL_DIR}/references/provider-evolink.md
Packy workflow doc = {SKILL_DIR}/references/provider-packy.md
```

## After Installation

When this skill is first loaded, proactively greet the user and start setup with one question.

1. Determine which provider is available.
2. If `GPT_IMAGE_PROVIDER` is already set, use it.
3. Otherwise:
   - If only `EVOLINK_API_KEY` is set, use `evolink`.
   - If only `PACKY_API_KEY` is set, use `packy`.
   - If both are set, ask which provider they want to use.
   - If neither is set, ask them which provider they want to set up first.

Do not list all features or dump setup instructions unless the user asks. Keep the user moving forward.

## Core Principles

1. Guide, don't decide. Present options and let the user choose.
2. Let the user drive the creative vision. Use their words when they already know what they want.
3. Recognize what has already been provided and only ask for what is still missing.
4. Confirm intent before execution when the request is ambiguous.
5. Keep the shared workflow in this file, and rely on the provider-specific docs for execution details and unsupported features.

## Shared Flow

### Step 1: Determine Provider

Choose the provider before collecting provider-specific parameters.

- If `GPT_IMAGE_PROVIDER=evolink`, follow `references/provider-evolink.md`.
- If `GPT_IMAGE_PROVIDER=packy`, follow `references/provider-packy.md`.
- If `GPT_IMAGE_PROVIDER` is unset:
  - Use the only configured provider if exactly one API key is present.
  - Ask the user to choose if both are configured.
  - Ask the user which provider they want to use if neither is configured.

### Step 2: Understand Intent

Assess what the user wants based on their message.

- Intent is clear: move on to gathering the remaining information.
- Intent is ambiguous: ask whether they want to generate a new image, edit an existing image, or learn what the chosen provider supports.

If the chosen provider does not support the requested mode, explain that clearly and offer either:
- switching providers, or
- adjusting the request to fit the chosen provider.

### Step 3: Gather Shared Inputs

Check what the user has already provided and ask only for the missing pieces.

| Parameter | What to tell the user | Required? |
|-----------|----------------------|-----------|
| **Intent / mode** | Determine whether they want to generate a new image or perform another supported action for the chosen provider. | Yes |
| **Image content** (`prompt`) | Ask what they want to see or change. If they want inspiration, offer a few directions and let them choose. | Yes |
| **Size** | Supports ratio format like `1:1`, `16:9`, `9:16`, or exact pixels like `1024x1024`. Default: `auto`. | Optional |
| **Quality** | Usually `low`, `medium`, or `high`. Default: `medium`. | Optional |

Provider-specific parameters, defaults, and feature limits must be checked in the matching provider document before execution.

Shared gathering rules:
- Ask all missing questions in one message.
- Do not ask the same question twice.
- If the user says to use defaults, use the provider's documented defaults immediately.
- If the user already provided enough information, do not ask extra questions.

### Step 4: Execute

Once all required information is confirmed:

1. Tell the user you are starting the image generation.
2. Run the chosen provider script once.
3. Do not retry automatically unless the user explicitly asks.
4. Follow the provider document for command format, output handling, and provider-specific safeguards.
5. When complete, share the image URL or clearly explain the failure.

## Shared Output Handling

All providers should be treated as command-line tools whose output must be inspected.

At minimum, look for:
- `IMAGE_URL=<url>` on success
- `ERROR: ...` on failure

Some providers emit additional structured progress or result lines. Those are documented in the provider-specific workflow docs and should only be interpreted according to the selected provider.

## Shared Error Handling

Use friendly, actionable language.

- Missing provider selection: ask the user which provider they want to use.
- Missing API key: tell the user exactly which environment variable is required for the chosen provider.
- Unsupported capability: explain that the current provider does not support that feature, and offer switching providers if appropriate.
- Provider execution failure: summarize the error and suggest the smallest sensible next step.

## Model Capabilities Summary

Use this when the user asks what the model can do.

- **Text-to-image**: Generate an image from a prompt.
- **Sizes**: Ratio format like `1:1`, `16:9`, `9:16` or exact pixel format like `1024x1024`.
- **Quality**: Provider-dependent quality controls such as `low`, `medium`, and `high`.
- **Provider-specific features**: Editing, batch generation, callbacks, resolution tiers, output formats, and polling behavior depend on the selected provider.

## Provider Workflows

- `references/provider-evolink.md`: EvoLink-specific setup, command usage, async task flow, output protocol, and supported parameters.
- `references/provider-packy.md`: Packy-specific setup, command usage, synchronous flow, output protocol, and supported parameters.

## References

- `references/api-params.md`: Shared and EvoLink-oriented parameter reference
- `scripts/gpt-image-gen.sh`: EvoLink provider script
- `scripts/packyapi.py`: Packy provider script
