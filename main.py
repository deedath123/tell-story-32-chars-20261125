#!/usr/bin/env python3
"""Entry generator for the make.fun 'Tell a Whole Story in 32 Characters' bounty.

Writes the entry -- a single Wi-Fi network name of exactly 32 characters --
to /output/entry.txt (or $OUTPUT_DIR/entry.txt). Python standard library only.
"""

import os

ENTRY = "She took 2 kids+dog! I kept WiFi"


def validate_entry(text):
    """Guard: the entry must be a non-empty Wi-Fi name of 1-32 characters."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 32, f"entry must be 1-32 chars, got {len(text)}"
    assert text.strip() == text and text.strip(), "entry must not be blank or padded"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    return text


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
