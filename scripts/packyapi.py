#!/usr/bin/env python3

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


PACKY_API_BASE = "https://www.packyapi.com"


class ParsedArgs:
    def __init__(self, prompt, size, quality, count, output_format, dry_run):
        self.prompt = prompt
        self.size = size
        self.quality = quality
        self.count = count
        self.output_format = output_format
        self.dry_run = dry_run

    def validate_size(self):
        if self.size == "auto":
            return

        valid_ratios = {
            "1:1",
            "1:2",
            "2:1",
            "1:3",
            "3:1",
            "2:3",
            "3:2",
            "3:4",
            "4:3",
            "4:5",
            "5:4",
            "9:16",
            "16:9",
            "9:21",
            "21:9",
        }
        if self.size in valid_ratios:
            return

        normalized = self.size.replace("×", "x")
        parts = normalized.split("x")
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            error("Invalid size format. Use ratio (e.g. 16:9), pixels (e.g. 1024x1024), or 'auto'")

        width = int(parts[0])
        height = int(parts[1])

        if width % 16 != 0 or height % 16 != 0:
            error(f"Width and height must be multiples of 16. Got {width}x{height}")
        if width < 16 or width > 3840 or height < 16 or height > 3840:
            error(f"Each dimension must be between 16-3840 pixels. Got {width}x{height}")

        pixels = width * height
        if pixels < 655360 or pixels > 8294400:
            error(f"Pixel budget must be 655,360-8,294,400. Got {pixels} ({width}x{height})")

    def to_payload(self):
        return {
            "model": "gpt-image-2",
            "prompt": self.prompt,
            "size": self.size,
            "quality": self.quality,
            "response_format": "url",
            "output_format": self.output_format,
            "n": self.count,
        }


def error(message: str) -> None:
    sys.stderr.write(f"ERROR: {message}\n")
    raise SystemExit(1)

def parse_args(argv) -> ParsedArgs:
    parser = argparse.ArgumentParser(
        prog="packy_gpt_image.py",
        description="Submit GPT Image 2 generation requests through Packy.",
    )
    parser.add_argument("prompt")
    parser.add_argument("--size", default="auto", help="Image size, such as 1024x1024 or auto")
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high", "auto"],
        default="medium",
        help="Render quality",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of images to generate (Packy only supports 1)",
    )
    parser.add_argument(
        "--output-format",
        choices=["png", "jpeg", "webp"],
        default="png",
        help="Output image format",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the JSON payload without sending the request",
    )

    parsed, unknown = parser.parse_known_args(argv)
    for arg in unknown:
        if arg in {"--resolution", "--callback", "--image"}:
            error(f"{arg} is not supported by the Packy provider helper")
    if unknown:
        error(f"Unknown parameter: {unknown[0]}")

    if parsed.count != 1:
        error("Packy only supports --count 1 for gpt-image-2")

    return ParsedArgs(
        prompt=parsed.prompt,
        size=parsed.size,
        quality=parsed.quality,
        count=parsed.count,
        output_format=parsed.output_format,
        dry_run=parsed.dry_run,
    )

def submit(payload, api_key: str) -> str:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{PACKY_API_BASE}/v1/images/generations",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")

def main(argv):
    api_key = os.environ.get("PACKY_API_KEY", "")
    if not api_key:
        error(
            "PACKY_API_KEY environment variable is required.\n\n"
            "To get started:\n"
            "1. Register at: https://www.packyapi.com\n"
            "2. Create a Sora group token\n"
            "3. Set the environment variable:\n"
            "   export PACKY_API_KEY=your_key_here"
        )

    args = parse_args(argv)
    args.validate_size()
    payload = args.to_payload()

    if args.dry_run:
        print("DRY_RUN: model=gpt-image-2 provider=packy")
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return

    print(
        f"INFO: Submitting image generation request (provider=packy, model=gpt-image-2, size={args.size}, quality={args.quality}, count={args.count})"
    )
    response_body = submit(payload, api_key)

    try:
        parsed = json.loads(response_body)
    except json.JSONDecodeError:
        error(f"Packy returned invalid JSON: {response_body}")

    results = parsed.get("data", [])
    if not isinstance(results, list) or not results:
        print(f"RESULT_JSON={json.dumps(parsed, ensure_ascii=True, separators=(',', ':'))}")
        error("Packy response did not include any image URLs")

    found_url = False
    for item in results:
        if isinstance(item, dict) and item.get("url"):
            print(f"IMAGE_URL={item['url']}")
            found_url = True

    print(f"RESULT_JSON={json.dumps(parsed, ensure_ascii=True, separators=(',', ':'))}")

    if not found_url:
        error("Packy response did not include any image URLs")


if __name__ == "__main__":
    main(sys.argv[1:])
