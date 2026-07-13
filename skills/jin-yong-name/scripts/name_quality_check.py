#!/usr/bin/env python3
"""Check hard-to-enforce batch quality rules for jin-yong-name outputs.

Input is JSON on stdin:
{
  "names": [
    {"name": "罗澄怀", "tones": "2-2-2", "structure": "清雅字+品格字"},
    {"name": "罗本立", "tones": "2-3-4", "structure": "典籍无痕"}
  ]
}

The script intentionally checks only mechanical risks. It does not judge beauty,
source quality, homophones, or real-life name feel.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter

HIGH_FREQ_SAFE_CHARS = set("本立谦修齐景行允衡和知远明守安正诚言")
ALL_LEVEL_PATTERNS = {"1-1-1", "1-1-2", "1-2-1", "1-2-2", "2-1-1", "2-1-2", "2-2-1", "2-2-2"}


def normalize_tones(value: str) -> str:
    digits = re.findall(r"[1-5]", value or "")
    return "-".join(digits)


def load_payload() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        raise SystemExit("No JSON input. Pass {'names': [...]} on stdin.")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}") from exc
    if not isinstance(payload.get("names"), list):
        raise SystemExit("Input must contain a names list.")
    return payload


def main() -> int:
    payload = load_payload()
    issues: list[str] = []
    endings: list[str] = []
    structures: list[str] = []
    high_freq_names = 0

    for idx, item in enumerate(payload["names"], 1):
        name = str(item.get("name", "")).strip()
        tones = normalize_tones(str(item.get("tones", "")))
        structure = str(item.get("structure", "")).strip()

        if not name:
            issues.append(f"#{idx}: missing name")
            continue

        endings.append(name[-1])
        if structure:
            structures.append(structure)

        core_chars = name[1:] if len(name) >= 2 else name
        if any(char in HIGH_FREQ_SAFE_CHARS for char in core_chars):
            high_freq_names += 1

        tone_parts = tones.split("-") if tones else []
        if len(tone_parts) == 3:
            if len(set(tone_parts)) == 1:
                issues.append(f"{name}: same-tone triple ({tones})")
            elif tones in ALL_LEVEL_PATTERNS:
                issues.append(f"{name}: all-level-tone pattern ({tones}); downgrade or replace")
        elif tones:
            issues.append(f"{name}: expected a three-syllable full-name tone sequence, got {tones}")
        else:
            issues.append(f"{name}: missing tone sequence")

    for ending, count in Counter(endings).items():
        if count >= 2:
            issues.append(f"batch: {count} names share ending character '{ending}'")

    for structure, count in Counter(structures).items():
        if count >= 2:
            issues.append(f"batch: {count} names share structure '{structure}'")

    if len(payload["names"]) >= 3 and high_freq_names >= 2:
        issues.append("batch: two or more names use high-frequency safe characters")
    if len(payload["names"]) >= 5 and high_freq_names >= 3:
        issues.append("batch: three or more outputs use high-frequency safe characters")

    result = {
        "ok": not issues,
        "issues": issues,
        "checked": len(payload["names"]),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
