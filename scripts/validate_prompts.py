#!/usr/bin/env python3
"""Validate every prompt file in prompts/ against the Prompt Stash format.

Standard library only. Exit 0 = all good, exit 1 = problems (printed).

Expected format:
    line 1: Title
    line 2: When to use it: <one sentence>
    line 3: Language: prompt=EN | output=EN|AR|EN+AR|user-choice
    line 4: Tags: comma, separated, lowercase
    line 5: (optional) human-readable disclaimer — REQUIRED for safety-listed files
    (blank line)
    prompt body (must contain a task/structure marker and a clarifying-question rule)
    (blank line)
    # Variables
    - {name}: explanation        (every body variable declared, no undeclared extras)
    (blank line)
    # Example values: {var}=realistic fill, ...
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"

LANG_RE = re.compile(r"^Language: prompt=(EN|AR) \| output=(EN|AR|EN\+AR|user-choice)$")
VAR_RE = re.compile(r"\{([a-z][a-z0-9_]*)\}")
GOOD_VAR_RE = re.compile(r"^[a-z][a-z0-9_]*$")
ANY_BRACE_RE = re.compile(r"\{([^{}]*)\}")

# Files that must carry a Phase-2 safety disclaimer (line 5) and a "Note:" line in the body.
SAFETY_REQUIRED = {
    "business/contract-summary", "arabic-life/rental-contract-explain",
    "arabic-life/legal-terms-explain", "arabic-life/complaint-letter-eg",
    "work/salary-negotiation-email", "business/invoice-words",
    "business/price-calc-explain", "business/quotation-writer",
    "business/late-payment-chaser", "business/idea-check",
    "daily/budget-split", "marketing/discount-offer", "marketing/referral-offer",
    "marketing/seasonal-campaign", "daily/expenses-review", "daily/decision-matrix",
    "daily/workout-plan", "daily/sleep-routine",
    "security-basics/password-checkup", "security-basics/phishing-spotter",
    "security-basics/2fa-setup-guide", "security-basics/scam-check",
    "security-basics/breach-response", "security-basics/public-wifi-safety",
    "security-basics/device-loss-plan", "security-basics/backup-plan",
    "security-basics/privacy-audit", "security-basics/safe-downloads",
}

errors: list[str] = []
warns: list[str] = []
count = 0

for f in sorted(PROMPTS.glob("*/*.txt")):
    rel = f.relative_to(ROOT).as_posix()
    stem = f.relative_to(PROMPTS).as_posix()[:-4]
    count += 1
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()

    def err(msg: str) -> None:
        errors.append(f"{rel}: {msg}")

    if len(lines) < 8:
        err(f"file too short ({len(lines)} lines) — not the standard format")
        continue
    if not lines[0].strip():
        err("line 1 is empty (title required)")
    if not lines[1].startswith("When to use it:"):
        err(f"line 2 must start with 'When to use it:' — found: {lines[1][:60]!r}")
    if not LANG_RE.match(lines[2]):
        err(f"line 3 is not a valid Language line — found: {lines[2][:60]!r}")
    tags_line = lines[3]
    if not tags_line.startswith("Tags: "):
        err(f"line 4 must start with 'Tags: ' — found: {tags_line[:40]!r}")
    else:
        tags = [t.strip() for t in tags_line[len("Tags: "):].split(",")]
        bad = [t for t in tags if not t or t != t.lower() or " " in t]
        if bad:
            err(f"tags must be lowercase, comma-separated, no spaces within a tag — bad: {bad}")
        if len(tags) < 2:
            err("need at least 2 tags")

    if stem in SAFETY_REQUIRED:
        if len(lines) < 6 or not lines[4].strip():
            err("safety-listed file needs a human-readable disclaimer on line 5")
        if not any(l.startswith("Note: ") for l in lines):
            err("safety-listed file needs a 'Note: ' line inside the prompt body")

    idx = next((i for i, l in enumerate(lines) if l.strip() == "# Variables"), None)
    if idx is None:
        err("missing '# Variables' block")
        continue
    if idx + 1 >= len(lines) or not lines[idx + 1].startswith("- {"):
        err("# Variables block has no '- {var}: explanation' entries")

    body = "\n".join(lines[5 if stem in SAFETY_REQUIRED else 4: idx]).strip()
    declared = [m.group(1) for l in lines[idx + 1:] if l.startswith("- {")
                for m in [re.match(r"^- \{([a-z0-9_]+)\}:", l)] if m]
    used = set(VAR_RE.findall(body))

    if not body:
        err("prompt body is empty")
    if "TASK" not in body:
        err("body has no task/structure marker (expected 'TASK' section)")
    # Clarifying/assumption handling — advisory prompts use the 3-question rule;
    # input-complete prompts (rewriters, summarizers, translators, cleaners) may
    # use the shorter "say what's missing instead of proceeding on assumptions" rule;
    # interactive prompts use explicit turn-taking rules instead.
    if not re.search(
        r"clarifying questions|assumptions|instead of guessing|Interaction rules:|"
        r"ambiguous|wait for my (answer|reply|attempt)|ask (up to|at most) \d+ questions?",
        body,
    ):
        err("body lacks a clarifying-question, assumptions, or interaction rule")

    missing = used - set(declared)
    extra = set(declared) - used
    if missing:
        err(f"variables used in body but not declared: {sorted(missing)}")
    if extra:
        err(f"variables declared but never used in body: {sorted(extra)}")

    # style scan covers the prompt text; the Example-values line is free-form
    # data (JSON samples, regex quantifiers) and is exempt.
    scan_text = "\n".join(l for l in lines if not l.startswith("# Example values:"))
    for m in ANY_BRACE_RE.findall(scan_text):
        if not GOOD_VAR_RE.fullmatch(m):
            err(f"variable style violation: {{{m}}} (use snake_case)")
            break

    example_lines = [l for l in lines if l.startswith("# Example values:")]
    if not example_lines:
        err("missing '# Example values:' line")
    elif not lines[-1].startswith("# Example values:"):
        warns.append(f"{rel}: '# Example values:' exists but is not the last line")

if not count:
    errors.append("no prompt files found under prompts/*/*.txt")

for w in warns:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\nChecked {count} prompt files: {len(errors)} error(s), {len(warns)} warning(s).")
sys.exit(1 if errors else 0)
