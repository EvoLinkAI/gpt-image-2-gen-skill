#!/usr/bin/env python3

import argparse
import json
import os
import sys

from packy_common import PackyApiError, emit_results, require_api_key, submit_form, validate_size


class ParsedArgs:
    def __init__(
        self,
        prompt,
        image,
        size,
        quality,
        output_format,
        mask,
        input_fidelity,
        output_compression,
        background,
        moderation,
        response_format,
        dry_run,
    ):
        self.prompt = prompt
        self.image = image
        self.size = size
        self.quality = quality
        self.output_format = output_format
        self.mask = mask
        self.input_fidelity = input_fidelity
        self.output_compression = output_compression
        self.background = background
        self.moderation = moderation
        self.response_format = response_format
        self.dry_run = dry_run

    def validate(self):
        validate_size(self.size)
        if not os.path.isfile(self.image):
            raise PackyApiError(f"Image input not found: {self.image}")
        if self.mask and not os.path.isfile(self.mask):
            raise PackyApiError(f"Mask input not found: {self.mask}")
        if self.output_format == "webp":
            raise PackyApiError("Packy image edits recommend png or jpeg output. Do not use webp for edits")
        if self.output_compression is not None and self.output_format != "jpeg":
            raise PackyApiError("--output-compression is only supported when --output-format is jpeg")
        if self.output_compression is not None and not 0 <= self.output_compression <= 100:
            raise PackyApiError("--output-compression must be between 0 and 100")
        if self.background == "transparent":
            raise PackyApiError("Packy image edits do not support transparent background")

    def to_fields(self):
        fields = {
            "model": "gpt-image-2",
            "prompt": self.prompt,
            "size": self.size,
            "quality": self.quality,
            "response_format": self.response_format,
            "output_format": self.output_format,
            "n": 1,
        }
        if self.input_fidelity is not None:
            fields["input_fidelity"] = self.input_fidelity
        if self.output_compression is not None:
            fields["output_compression"] = self.output_compression
        if self.background is not None:
            fields["background"] = self.background
        if self.moderation is not None:
            fields["moderation"] = self.moderation
        return fields


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="packy_edit.py",
        description="Submit GPT Image 2 image edit requests through Packy.",
    )
    parser.add_argument("prompt")
    parser.add_argument("--image", required=True, help="Local source image file path")
    parser.add_argument("--size", default="auto", help="Image size, such as 1024x1024 or auto")
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high", "auto"],
        default="medium",
        help="Render quality",
    )
    parser.add_argument(
        "--output-format",
        choices=["png", "jpeg", "webp"],
        default="png",
        help="Output image format",
    )
    parser.add_argument("--mask", help="Optional PNG mask file path for localized image edits")
    parser.add_argument(
        "--input-fidelity",
        choices=["high"],
        help="Preserve the source subject and details",
    )
    parser.add_argument(
        "--output-compression",
        type=int,
        help="JPEG compression level from 0 to 100",
    )
    parser.add_argument(
        "--background",
        choices=["opaque", "transparent"],
        help="Background mode. Use opaque for Packy edits",
    )
    parser.add_argument(
        "--moderation",
        choices=["auto", "low"],
        help="Safety moderation mode",
    )
    parser.add_argument(
        "--response-format",
        choices=["url", "b64_json"],
        default="url",
        help="Response format",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the request payload without sending the request",
    )

    parsed, unknown = parser.parse_known_args(argv)
    for arg in unknown:
        if arg in {"--count", "--resolution", "--callback"}:
            raise PackyApiError(f"{arg} is not supported by the Packy edit helper")
    if unknown:
        raise PackyApiError(f"Unknown parameter: {unknown[0]}")

    return ParsedArgs(
        prompt=parsed.prompt,
        image=parsed.image,
        size=parsed.size,
        quality=parsed.quality,
        output_format=parsed.output_format,
        mask=parsed.mask,
        input_fidelity=parsed.input_fidelity,
        output_compression=parsed.output_compression,
        background=parsed.background,
        moderation=parsed.moderation,
        response_format=parsed.response_format,
        dry_run=parsed.dry_run,
    )


def main(argv):
    api_key = require_api_key()
    args = parse_args(argv)
    args.validate()
    fields = args.to_fields()

    if args.dry_run:
        print("DRY_RUN: model=gpt-image-2 provider=packy mode=edit")
        print(json.dumps(fields, ensure_ascii=True, indent=2))
        print(f"EDIT_IMAGE={args.image}")
        if args.mask:
            print(f"EDIT_MASK={args.mask}")
        return

    print(
        f"INFO: Submitting image edit request (provider=packy, model=gpt-image-2, size={args.size}, quality={args.quality}, image={args.image})"
    )
    files = {"image": args.image}
    if args.mask:
        files["mask"] = args.mask
    response_body = submit_form("/v1/images/edits", fields, files, api_key)
    emit_results(response_body)


if __name__ == "__main__":
    main(sys.argv[1:])
