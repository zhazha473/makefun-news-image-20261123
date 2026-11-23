#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 make.fun entry.

Copies the pre-rendered entry.png (drawn fresh in this session by
compose.py) to the harness output directory. Standard library only,
no network, deterministic: the bytes written are exactly the bytes
of entry.png in this repository.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: the two grader runs must write identical bytes, so confirm
    # the copy is complete before reporting success.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        print("error: incomplete copy", file=sys.stderr)
        return 1
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
