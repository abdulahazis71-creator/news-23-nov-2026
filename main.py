"""Write the day's news image to the output directory.

This program is the entry for make.fun's "Sum up 23 November's world
news in one image" bounty. It does one simple thing: it takes the
newspaper-style image stored next to this file (entry.png, a 1024x1024
summary of the world's news of Monday 23 November 2026) and copies it,
byte for byte, to the output directory as entry.png.

The grader runs this program twice in a fresh container with no
network access, and both runs must produce identical bytes. Copying a
fixed file is fully deterministic, so that requirement is met by
construction.

Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

# The image that ships with this repository.
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"

# The grader sets MAKEFUN_OUTPUT_DIR; outside the grader it defaults
# to /output, matching the competition's brief.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    """Copy entry.png into the output directory and report success.

    Returns 0 on success. If the bundled image is missing (for example
    a checkout that dropped the binary file), the program fails loudly
    with a clear message instead of crashing mid-copy.
    """
    if not SOURCE_IMAGE.is_file():
        print(f"error: {SOURCE_IMAGE} is missing; cannot write the entry image",
              file=sys.stderr)
        return 1
    destination = Path(OUTPUT_DIR) / "entry.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_IMAGE, destination)
    print(f"Wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
