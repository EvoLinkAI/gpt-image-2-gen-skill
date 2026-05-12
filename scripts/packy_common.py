import json
import os
import subprocess


PACKY_API_BASE = "https://www.packyapi.com"
VALID_RATIOS = {
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


class PackyApiError(Exception):
    pass


def validate_size(size: str):
    if size == "auto":
        return

    if size in VALID_RATIOS:
        return

    normalized = size.replace("×", "x")
    parts = normalized.split("x")
    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        raise PackyApiError("Invalid size format. Use ratio (e.g. 16:9), pixels (e.g. 1024x1024), or 'auto'")

    width = int(parts[0])
    height = int(parts[1])
    if width % 16 != 0 or height % 16 != 0:
        raise PackyApiError(f"Width and height must be multiples of 16. Got {width}x{height}")
    if width < 16 or width > 3840 or height < 16 or height > 3840:
        raise PackyApiError(f"Each dimension must be between 16-3840 pixels. Got {width}x{height}")

    pixels = width * height
    if pixels < 655360 or pixels > 8294400:
        raise PackyApiError(f"Pixel budget must be 655,360-8,294,400. Got {pixels} ({width}x{height})")


def require_api_key() -> str:
    api_key = os.environ.get("PACKY_API_KEY", "")
    if api_key:
        return api_key
    raise PackyApiError(
        "PACKY_API_KEY environment variable is required.\n\n"
        "To get started:\n"
        "1. Register at: https://www.packyapi.com\n"
        "2. Create a Sora group token\n"
        "3. Set the environment variable:\n"
        "   export PACKY_API_KEY=your_key_here"
    )


def run_curl(curl_command) -> str:
    completed = subprocess.run(
        curl_command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    response_body = completed.stdout
    if completed.returncode != 0:
        stderr_message = completed.stderr.strip()
        raise PackyApiError(f"curl request failed with exit code {completed.returncode}: {stderr_message}")
    return response_body


def submit_json(endpoint: str, payload, api_key: str) -> str:
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    curl_command = [
        "curl.exe",
        "--silent",
        "--show-error",
        "--location",
        "--request",
        "POST",
        f"{PACKY_API_BASE}{endpoint}",
        "--header",
        f"Authorization: Bearer {api_key}",
        "--header",
        "Content-Type: application/json",
        "--header",
        "Accept: */*",
        "--data",
        body,
    ]
    return run_curl(curl_command)


def submit_form(endpoint: str, fields, files, api_key: str) -> str:
    curl_command = [
        "curl.exe",
        "--silent",
        "--show-error",
        "--location",
        "--request",
        "POST",
        f"{PACKY_API_BASE}{endpoint}",
        "--header",
        f"Authorization: Bearer {api_key}",
        "--header",
        "Accept: */*",
    ]
    for key, value in fields.items():
        curl_command.extend(["--form", f'{key}={json.dumps(value, ensure_ascii=False)}'])
    for key, file_path in files.items():
        curl_command.extend(["--form", f"{key}=@{file_path}"])
    return run_curl(curl_command)


def emit_results(response_body: str):
    parsed = json.loads(response_body)
    results = parsed.get("data", [])
    if not isinstance(results, list) or not results:
        raise PackyApiError("Packy response did not include any image URLs")

    found_url = False
    for item in results:
        if isinstance(item, dict) and item.get("url"):
            print(f"IMAGE_URL={item['url']}")
            found_url = True
    if not found_url:
        raise PackyApiError("Packy response did not include any image URLs")
