#!/usr/bin/env python3

import argparse
import json
import sys

from packy_common import PackyApiError, emit_results, require_api_key, submit_json, validate_size


class ParsedArgs:
    def __init__(
        self,
        prompt,
        size,
        quality,
        count,
        output_format,
        output_compression,
        background,
        moderation,
        user,
        response_format,
        dry_run,
    ):
        self.prompt = prompt
        self.size = size
        self.quality = quality
        self.count = count
        self.output_format = output_format
        self.output_compression = output_compression
        self.background = background
        self.moderation = moderation
        self.user = user
        self.response_format = response_format
        self.dry_run = dry_run

    def to_payload(self):
        payload = {
            "model": "gpt-image-2",
            "prompt": self.prompt,
            "size": self.size,
            "quality": self.quality,
            "response_format": self.response_format,
            "output_format": self.output_format,
            "n": self.count,
        }
        if self.output_compression is not None:
            payload["output_compression"] = self.output_compression
        if self.background is not None:
            payload["background"] = self.background
        if self.moderation is not None:
            payload["moderation"] = self.moderation
        if self.user is not None:
            payload["user"] = self.user
        return payload


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
        "--output-compression",
        type=int,
        help="JPEG compression level from 0 to 100",
    )
    parser.add_argument(
        "--background",
        choices=["opaque", "transparent"],
        help="Background mode. Use opaque for Packy generation",
    )
    parser.add_argument(
        "--moderation",
        choices=["auto", "low"],
        help="Safety moderation mode",
    )
    parser.add_argument("--user", help="Optional end-user or business identifier")
    parser.add_argument(
        "--response-format",
        choices=["url"],
        default="url",
        help="Response format. Only url is supported by this helper",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the request payload without sending the request",
    )

    parsed, unknown = parser.parse_known_args(argv)
    for arg in unknown:
        if arg in {"--resolution", "--callback", "--image", "--mask", "--input-fidelity", "--style", "--stream", "--partial_images"}:
            raise PackyApiError(f"{arg} is not supported by the Packy provider helper")
    if unknown:
        raise PackyApiError(f"Unknown parameter: {unknown[0]}")

    if parsed.count != 1:
        raise PackyApiError("Packy only supports --count 1 for gpt-image-2")
    if parsed.output_compression is not None and not 0 <= parsed.output_compression <= 100:
        raise PackyApiError("--output-compression must be between 0 and 100")
    if parsed.output_compression is not None and parsed.output_format != "jpeg":
        raise PackyApiError("--output-compression is only supported when --output-format is jpeg")
    if parsed.background == "transparent":
        raise PackyApiError("Packy generation does not support transparent background")
    return ParsedArgs(
        prompt=parsed.prompt,
        size=parsed.size,
        quality=parsed.quality,
        count=parsed.count,
        output_format=parsed.output_format,
        output_compression=parsed.output_compression,
        background=parsed.background,
        moderation=parsed.moderation,
        user=parsed.user,
        response_format=parsed.response_format,
        dry_run=parsed.dry_run,
    )


def main(argv):
    api_key = require_api_key()
    args = parse_args(argv)
    validate_size(args.size)
    payload = args.to_payload()

    if args.dry_run:
        print("DRY_RUN: model=gpt-image-2 provider=packy mode=generation")
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return

    print(
        f"INFO: Submitting image generation request (provider=packy, model=gpt-image-2, size={args.size}, quality={args.quality}, count={args.count})"
    )
    response_body = submit_json("/v1/images/generations", payload, api_key)

    emit_results(response_body)


if __name__ == "__main__":
    main(sys.argv[1:])
