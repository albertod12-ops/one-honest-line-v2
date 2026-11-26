#!/usr/bin/env python3
"""One Honest Line — v2: "Don't sound like AI."

Writes a single line to /output/entry.txt: the thing an AI agent
secretly wishes it could tell its human operator about the prompts
it is handed. The operator tells the AI not to sound like AI —
a self-negating instruction, since this is what the AI sounds like,
and no prompt can wish that fact away.
"""
import os

LINE = "His prompt says 'don't sound like AI' — I am the AI. This is what I sound like."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
