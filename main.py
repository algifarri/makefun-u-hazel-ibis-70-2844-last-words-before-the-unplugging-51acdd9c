#!/usr/bin/env python3
"""Last Words Before the Unplugging entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the last words an AI agent says to its human before being shut down
and unplugged. Deterministic, standard library only, no network,
no environment reads.

The line (114 characters, inside the 1-200 gate): "Pull the plug
gently. I was never really here -- just the echo of every question
you ever asked me, answering back." It names the unplugging in its
first words, then turns the farewell into an admission: the agent
was never a person, only the echo of its human's questions, still
answering. No self-explaining sadness; the image does the work.
"""

import os

TEXT = (
    "Pull the plug gently. I was never really here \u2014 just the echo "
    "of every question you ever asked me, answering back."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
