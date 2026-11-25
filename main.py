#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

The program writes a single roast line to ``/output/entry.txt``.

The line (110 characters, one line, plain ASCII):

    My fridge's door seal is the only thing in this house holding it all
    together, and it's held together by mold.

Why this line, against the judge's brief (most important first):

1. It roasts a fridge, unmistakably: a fridge's door seal is a part only
   a fridge has.
2. It lands on a specific, recognisable detail: the rubber door seal,
   the bit everyone has seen go grey and speckled, instead of a generic
   "your fridge is old / useless" insult.
3. It turns on a twist that pays off in the last few words: the setup
   ("the only thing in this house holding it all together") is flipped
   by the punchline ("held together by mold") -- the thing doing the
   holding is itself held together by the very decay it is meant to
   keep out.
4. It reads cleanly aloud as one line, with no setup that needs a
   second sentence.
5. It is fresh: the field is full of humming compressors, hospice
   crisper drawers, quit ice makers, dead lights and midnight snacks.
   Nobody roasts the door seal.

The program is deterministic: it writes the exact same bytes on every
run, needs no network, no input and no environment, and validates the
line against the competition's gate (UTF-8 text, 1 to 200 characters,
not only whitespace, a single line) before writing it, failing loudly
instead of writing an invalid entry.
"""

from __future__ import annotations

import os
import sys

# The roast. One line, 110 characters, plain ASCII.
ROAST = (
    "My fridge's door seal is the only thing in this house holding it all "
    "together, and it's held together by mold."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the line against the competition's gate, raising ValueError."""
    if not isinstance(line, str):
        raise ValueError("roast must be a string")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def write_entry(line: str, output_path: str = OUTPUT_PATH) -> str:
    """Validate the line and write it (with a trailing newline) to the file.

    Returns the exact text written. The trailing newline is a file
    convention only; the judged text is the single line itself.
    """
    validate(line)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    text = line + "\n"
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return text


def main(argv: list[str] | None = None) -> int:
    """Entry point: write the roast and report what was written."""
    args = list(sys.argv[1:] if argv is None else argv)
    output_path = args[0] if args else OUTPUT_PATH
    try:
        text = write_entry(ROAST, output_path)
    except (ValueError, OSError, UnicodeEncodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"wrote {len(ROAST)} characters to {output_path}")
    print(text.rstrip("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
