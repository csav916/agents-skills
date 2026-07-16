#!/usr/bin/env python3
"""Generate a single background image via the Gemini image API (stdlib only).

Usage:
    generate_image.py --prompt "..." --out path/to/file.png
                       [--aspect-ratio 9:16] [--resolution 2K]
                       [--model gemini-3.1-flash-image-preview] [--api-key KEY]
"""

import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
DEFAULT_RESOLUTION = "2K"
DEFAULT_RATIO = "9:16"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

VALID_RATIOS = {"1:1", "16:9", "9:16", "4:3", "3:4", "2:3", "3:2",
                "4:5", "5:4", "1:4", "4:1", "1:8", "8:1", "21:9"}
VALID_RESOLUTIONS = {"512", "1K", "2K", "4K"}


def generate_image(prompt, model, aspect_ratio, resolution, api_key, out_path):
    url = f"{API_BASE}/{model}:generateContent?key={api_key}"
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": resolution,
            },
        },
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST",
    )

    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else ""
            if e.code == 429 and attempt < 2:
                last_error = error_body
                time.sleep(20)
                continue
            print(json.dumps({"error": True, "status": e.code, "message": error_body}))
            sys.exit(1)
        except urllib.error.URLError as e:
            print(json.dumps({"error": True, "message": str(e.reason)}))
            sys.exit(1)
    else:
        print(json.dumps({"error": True, "message": f"Rate limited repeatedly: {last_error}"}))
        sys.exit(1)

    candidates = result.get("candidates", [])
    if not candidates:
        reason = result.get("promptFeedback", {}).get("blockReason", "UNKNOWN")
        print(json.dumps({"error": True, "reason": "IMAGE_SAFETY" if reason != "UNKNOWN" else reason,
                           "message": f"No candidates returned. blockReason: {reason}"}))
        sys.exit(1)

    parts = candidates[0].get("content", {}).get("parts", [])
    image_data = None
    for part in parts:
        if "inlineData" in part:
            image_data = part["inlineData"]["data"]
            break

    if not image_data:
        finish_reason = candidates[0].get("finishReason", "UNKNOWN")
        print(json.dumps({"error": True, "reason": finish_reason,
                           "message": f"No image in response. finishReason: {finish_reason}"}))
        sys.exit(1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    sidecar = out_path.with_suffix(".txt")
    sidecar.write_text(prompt, encoding="utf-8")

    return {
        "path": str(out_path.resolve()),
        "prompt_file": str(sidecar.resolve()),
        "model": model,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
    }


def main():
    parser = argparse.ArgumentParser(description="Generate one background image via Gemini")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--out", required=True, help="Output file path (.png)")
    parser.add_argument("--aspect-ratio", default=DEFAULT_RATIO)
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key", default=None)
    args = parser.parse_args()

    if args.aspect_ratio not in VALID_RATIOS:
        print(json.dumps({"error": True, "message": f"Invalid aspect ratio. Valid: {sorted(VALID_RATIOS)}"}))
        sys.exit(1)
    if args.resolution not in VALID_RESOLUTIONS:
        print(json.dumps({"error": True, "message": f"Invalid resolution. Valid: {sorted(VALID_RESOLUTIONS)}"}))
        sys.exit(1)

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_AI_API_KEY")
    if not api_key:
        print(json.dumps({"error": True, "message": "No API key. Set GEMINI_API_KEY env or pass --api-key"}))
        sys.exit(1)

    result = generate_image(
        prompt=args.prompt,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        api_key=api_key,
        out_path=Path(args.out),
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
