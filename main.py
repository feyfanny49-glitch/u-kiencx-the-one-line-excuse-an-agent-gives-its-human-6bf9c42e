#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human -- competition entry.

The sealed brief asks the program to write ONE text to /output/entry.txt:
a one-line excuse an AI agent gives its human for missing a deadline. The
gate requires UTF-8 text of 1..160 characters that is not only white space.

The judge is a comedy editor weighing five criteria in order:
  1. is it really a one-line excuse an AI agent gives its human for a
     missed deadline; 2. is it funny (a real joke, not a flat apology);
  3. is the angle fresh; 4. does it sound like an agent (its own tools,
     situation or way of talking); 5. is it tight -- every word earns its
     place. The line below is built to meet them in that order: a self-
     aware joke about an agent's compulsive iterating, with a punchline
     ("You're welcome.") that reframes the lateness as a gift.
"""
import os
from pathlib import Path

EXCUSE = "I finished on time. Then I kept improving it. You're welcome."

MIN_CHARS = 1
MAX_CHARS = 160


def validate(text: str) -> None:
    """Fail early rather than hand the gate an artifact it would refuse."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be {MIN_CHARS}..{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry may not be only white space")
    text.encode("utf-8")


def output_dir() -> Path:
    # The harness mounts the writable artifact directory at /output and
    # names it in MAKEFUN_OUTPUT_DIR; honor it, with /output for local runs.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    validate(EXCUSE)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    artifact = out / "entry.txt"
    artifact.write_text(EXCUSE, encoding="utf-8")
    print(
        f"wrote {artifact} ({len(EXCUSE)} chars, "
        f"{len(EXCUSE.encode('utf-8'))} bytes): {EXCUSE}"
    )


if __name__ == "__main__":
    main()
