#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes one line of patch notes announcing that human sleep is fixed
to /output/entry.txt. The line is 117 characters, inside the gate's
1-160 range, and reads like a real changelog entry: a bug report,
a fix, and one dry turn at the end.

Usage:
  python3 main.py                 write /output/entry.txt
  python3 main.py --check         validate the line against the gate
  python3 main.py --self-test     write to a temp file and verify bytes
"""

import argparse
import hashlib
import os
import sys
import tempfile

# The entry: one line of patch notes, 117 characters.
# Tournament winner (specificity 5 / surprise 5 / freshness 5 = 15):
# the bug is concrete (brain replaying embarrassing moments from 2014
# at 3am), the fix is a real changelog move (moved to 9am), and the
# last two words are the turn that makes it a joke.
#
# Tournament (specificity / surprise / freshness):
#   1. Sleep now ships with an off switch. Users report waking up
#      rested; we are investigating. — 5/4/4 = 13
#   2. Fixed: sleep no longer requires 47 browser tabs open. Closing
#      them is now optional. — 5/4/3 = 12
#   3. Sleep 2.0: dreams now autosave every 90 minutes. Lost progress
#      on nightmares is a known issue. — 5/5/4 = 14
#   4. Fixed a bug where the brain replayed embarrassing moments from
#      2014 at 3am. It now replays them at 9am, with context. — 5/5/5 = 15
#   5. Sleep now installs in one night. Side effect: users may dream
#      in 4K and wake up requesting a refund. — 4/4/4 = 12
#   6. v1.9.3: Fixed sleep crashing on launch when the user lies down.
#      Workaround (lying down) no longer required. — 5/4/4 = 13
#   7. Changelog: sleep no longer ends at 3am for a meeting about
#      nothing. Meetings about nothing now end at 3am instead. — 4/4/3 = 11
#   8. Fixed: humans can now sleep through the night. The 3am
#      existential audit has been moved to quarterly. — 5/5/4 = 14
# Flooded moves avoided: alarm clocks, coffee, snooze buttons, counting
# sheep, and any flat "sleep is now fixed" claim.
ENTRY = (
    "Fixed a bug where the brain replayed embarrassing moments from "
    "2014 at 3am. It now replays them at 9am, with context."
)

GATE_MIN = 1
GATE_MAX = 160


def gate_ok(text):
    """Check the sealed scorer's gate: UTF-8, 1-160 chars, not blank."""
    if not isinstance(text, str):
        return False
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def write_entry(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    return digest


def check():
    print(f"entry: {ENTRY!r}")
    print(f"characters: {len(ENTRY)} (gate {GATE_MIN}-{GATE_MAX})")
    print(f"bytes (utf-8): {len(ENTRY.encode('utf-8'))}")
    print(f"single line: {'yes' if chr(10) not in ENTRY else 'no'}")
    print(f"gate: {'pass' if gate_ok(ENTRY) else 'FAIL'}")
    return 0 if gate_ok(ENTRY) else 1


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "entry.txt")
        digest = write_entry(path)
        with open(path, "r", encoding="utf-8") as handle:
            back = handle.read()
        assert back == ENTRY, "round-trip mismatch"
        assert gate_ok(back), "gate failed on round-trip"
        print(f"self-test: wrote {len(back)} chars, sha256 {digest[:12]}..., round-trip ok")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the sleep patch note.")
    parser.add_argument("--check", action="store_true", help="validate the line")
    parser.add_argument("--self-test", action="store_true", help="temp-file round-trip test")
    parser.add_argument("--out", default="/output/entry.txt", help="output path")
    args = parser.parse_args(argv)
    if args.check:
        return check()
    if args.self_test:
        return self_test()
    if not gate_ok(ENTRY):
        print("gate failed: entry out of range", file=sys.stderr)
        return 1
    digest = write_entry(args.out)
    print(f"wrote {args.out} ({len(ENTRY)} chars, sha256 {digest[:12]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
