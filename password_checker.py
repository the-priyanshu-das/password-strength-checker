#!/usr/bin/env python3
"""Local password-strength checker. Passwords are never stored or printed."""

from __future__ import annotations

import re
import sys
from getpass import getpass

try:
    from zxcvbn import zxcvbn
except ImportError:
    zxcvbn = None


def rule_feedback(password: str) -> tuple[list[str], int]:
    """Return useful observations and a simple rule-based score (0–4)."""
    checks = [
        (len(password) >= 12, "At least 12 characters"),
        (len(password) >= 16, "At least 16 characters (a stronger target)"),
        (bool(re.search(r"[a-z]", password)) and bool(re.search(r"[A-Z]", password)), "Mixes uppercase and lowercase letters"),
        (bool(re.search(r"\d", password)), "Contains a digit"),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Contains a symbol or non-ASCII character"),
    ]
    notes = [f"{'✓' if ok else '✗'} {label}" for ok, label in checks]
    # Length has extra weight; this score is only a checklist, not entropy.
    score = sum((2 if i < 2 else 1) for i, (ok, _) in enumerate(checks) if ok)
    if re.search(r"(.)\1{2,}", password):
        notes.append("! Contains a character repeated three or more times")
    if re.search(r"(?i)(password|qwerty|letmein|admin|welcome|123456)", password):
        notes.append("! Contains a commonly used password word or sequence")
    return notes, min(4, score)


def main() -> int:
    print("Password Strength Checker (local only)")
    print("Use a new password or passphrase; do not enter a password you currently use.")
    try:
        password = getpass("Password to assess (input hidden): ")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return 1
    if not password:
        print("No password entered.")
        return 1

    notes, fallback_score = rule_feedback(password)
    print("\nChecklist (these rules alone do not measure password strength):")
    for note in notes:
        print(f"  {note}")

    if zxcvbn is None:
        print(f"\nRule checklist score: {fallback_score}/4")
        print("For a strength estimate and personalized feedback, install the optional zxcvbn package.")
    else:
        result = zxcvbn(password)
        labels = ("Very weak", "Weak", "Fair", "Strong", "Very strong")
        score = result["score"]
        print(f"\nzxcvbn estimate: {labels[score]} ({score}/4)")
        if result.get("feedback", {}).get("warning"):
            print(f"  {result['feedback']['warning']}")
        for suggestion in result.get("feedback", {}).get("suggestions", []):
            print(f"  - {suggestion}")
        if not result.get("feedback", {}).get("suggestions") and not result.get("feedback", {}).get("warning"):
            print("  No specific improvements suggested.")
    # Do not retain the input longer than needed in the program's normal flow.
    password = ""
    return 0


if __name__ == "__main__":
    sys.exit(main())
