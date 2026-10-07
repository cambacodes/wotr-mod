"""Exact legacy JSON and destination newline policies (no normalization)."""
import json
import os


def serialize(payload, profile, destination):
    if profile == "expansion":
        newline = "\r\n" if destination is not None and destination.exists() and b"\r\n" in destination.read_bytes() else "\n"
    else:
        # story.build used Path.write_text without a newline argument. Existing
        # package bytes never selected its policy; the host text writer did.
        newline = None
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    raw = text.replace("\n", os.linesep if newline is None else newline).encode("utf-8")
    return text, newline, raw


def write_story(destination, compiled):
    # Retain the text writer's errors and platform behavior, as well as bytes.
    destination.write_text(compiled._text, encoding="utf-8", newline=compiled._newline)
