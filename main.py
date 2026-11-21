#!/usr/bin/env python3
"""Entry for make.fun news-image-20261121.

Writes the front page held in this repository (entry.png) to the output
directory the grader provides, so the judge sees the image that sums up
Saturday 21 November 2026: Russian missiles landing in Poland as the
overnight barrage hits Kyiv, the AI sell-off dragging the S&P 500 into
correction, COP31 running past its deadline, the UK-EU post-Brexit deals,
and the day's other stories.

Standard library only; no network; deterministic: both runs write the
exact same bytes, and the copy is checked byte-for-byte before exit.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    raise SystemExit(f"main.py: {message}")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    size = os.path.getsize(SOURCE)
    if size > 1048576:
        fail(f"entry.png is {size} bytes, over the 1 MiB cap")
    with open(SOURCE, "rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            fail("entry.png is not a PNG file")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(SOURCE, "rb") as a, open(dest, "rb") as b:
        if a.read() != b.read():
            fail("output bytes differ from entry.png")
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
