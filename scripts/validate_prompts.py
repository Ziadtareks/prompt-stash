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

# build_index.py is side-effect-free at import (everything runs under main());
# it owns SAFETY_REQUIRED and generate() so checker and generator never drift.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index  # noqa: E402

LANG_RE = re.compile(r"^Language: prompt=(EN|AR) \| output=(EN|AR|EN\+AR|user-choice)$")
VAR_RE = re.compile(r"\{([a-z][a-z0-9_]*)\}")
GOOD_VAR_RE = re.compile(r"^[a-z][a-z0-9_]*$")
ANY_BRACE_RE = re.compile(r"\{([^{}]*)\}")
AR_LINE_RE = re.compile(r"If the requested output language is Arabic:")

# Safety-listed files now live in build_index.SAFETY_REQUIRED (aliased below).
SAFETY_REQUIRED = build_index.SAFETY_REQUIRED

errors: list[str] = []
warns: list[str] = []
count = 0
titles_seen: dict[str, str] = {}

MAX_FILE_CHARS = 4500  # prompts must stay paste-friendly; documented in CONTRIBUTING.md
AR_ADJACENT_RE = re.compile(r"[\u0600-\u06FF][A-Za-z]|[A-Za-z][\u0600-\u06FF]")

for f in sorted(PROMPTS.glob("*/*.txt")):
    rel = f.relative_to(ROOT).as_posix()
    stem = f.relative_to(PROMPTS).as_posix()[:-4]
    count += 1
    raw = f.read_bytes()
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()

    def err(msg: str) -> None:
        errors.append(f"{rel}: {msg}")

    if raw.startswith(b"\xef\xbb\xbf"):
        err("file starts with a UTF-8 BOM — save as UTF-8 without BOM")
    if b"\r\n" in raw:
        err("file has CRLF line endings — the repo standard is LF (see .gitattributes)")
    title = lines[0].strip() if lines else ""
    if title in titles_seen:
        err(f"duplicate title — {titles_seen[title]} uses the same title")
    else:
        titles_seen[title] = rel

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

    # every declared variable should have a realistic fill in Example values
    example_text = " ".join(example_lines)
    missing_fills = [v for v in declared if f"{{{v}}}=" not in example_text]
    if missing_fills:
        warns.append(f"{rel}: no example fill for {missing_fills} in '# Example values:'")

    # v4.1 content-quality checks
    if "OUTPUT FORMAT" not in body:
        err("body lacks an OUTPUT FORMAT section")
    if any("see Example values" in l for l in lines[idx + 1:] if l.startswith("- {")):
        err("Variables block still contains a lazy 'see Example values' explanation")

    m = LANG_RE.match(lines[2])
    if m and m.group(2) in ("AR", "EN+AR"):
        if "ARABIC STYLE" not in body:
            err("Arabic-output prompt lacks an ARABIC STYLE block (variety + anti-machine-translation rules)")
    elif m and m.group(2) == "user-choice":
        if not AR_LINE_RE.search(body):
            err("user-choice prompt lacks the conditional Arabic-style instruction")

    if len(text) > MAX_FILE_CHARS:
        err(f"file is {len(text)} characters (limit {MAX_FILE_CHARS}) — split or tighten it")

    if "\ufffd" in text:
        err("contains U+FFFD replacement characters (mojibake)")
    if re.search(r"[\u2E80-\u9FFF\uF900-\uFAFF]", text):
        err("contains CJK characters — no EN/AR prompt should ever include them (corrupted paste?)")
    for i, l in enumerate(lines, 1):
        if AR_ADJACENT_RE.search(l):
            err(f"line {i}: Latin letter directly attached to an Arabic word — fix the mixed-script word")
            break

if not count:
    errors.append("no prompt files found under prompts/*/*.txt")

# generated files must match what build_index would write right now
for rel, expected in sorted(build_index.generate().items()):
    actual_path = ROOT / rel
    if not actual_path.exists():
        errors.append(f"generated file missing: {rel} — run: python scripts/build_index.py")
        continue
    actual = actual_path.read_text(encoding="utf-8")
    if actual != expected:
        errors.append(f"{rel} is stale (does not match current prompts) — run: python scripts/build_index.py")

for w in warns:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\nChecked {count} prompt files: {len(errors)} error(s), {len(warns)} warning(s).")
sys.exit(1 if errors else 0)
