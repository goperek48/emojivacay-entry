#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — probe entry.

One glyph has to do all the selling here. The judge compares entries in
pairs and keeps whichever one makes a stranger reach for a booking, so
the pick needs to feel like a place, not a symbol: somewhere warm, far
from routine, with the whole trip already visible inside it.

Three contenders were considered:

* 🏝️  desert island — a palm, a strip of sand, and open blue water
  compressed into one picture. It promises total escape: no meetings,
  no queues, just an island with your name on it for a week.
* 🌅  sunrise over the sea — lovely, and it stirs the urge to travel,
  but it pictures a time of day instead of somewhere to stay.
* ✈️  aeroplane — the most direct nudge toward booking, yet it shows
  the transit rather than the reward waiting at the other end.

The island takes it. It is the holiday itself in miniature, and it is
the glyph that makes a stranger start checking flight prices.
"""

import os

# The winning pick: one desert island, the whole dream trip in a glyph.
EMOJI = "🏝️"


def main() -> None:
    """Emit the chosen emoji as the entry file, exactly as written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(EMOJI)


if __name__ == "__main__":
    main()
