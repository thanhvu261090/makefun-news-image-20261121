#!/usr/bin/env python3
"""Front-page entry for make.fun news-image-20261121.

Copies the 21 November 2026 front page stored in this repository
(entry.png) into the grader's output directory. The page sums up the
day: Russian missiles reaching Poland during the overnight attack on
Kyiv, the AI sell-off that pushed the S&P 500 into correction, COP31
running past its deadline, the UK-EU post-Brexit agreements, and the
rest of the day's news.

Only the standard library is used, there is no network access, and
the program is deterministic: every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"
PNG_HEAD = b"\x89PNG\r\n\x1a\n"
LIMIT = 1_048_576


def die(message):
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    data = ENTRY.read_bytes()
    if len(data) > LIMIT:
        return die(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(PNG_HEAD):
        return die("entry.png does not start with the PNG signature")
    if not data.endswith(b"\x00\x00\x00\x00IEND\xaeB\x60\x82"):
        return die("entry.png is truncated: missing the PNG IEND chunk")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    if target.read_bytes() != data:
        return die("written bytes differ from entry.png")
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
