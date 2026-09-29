#!/usr/bin/env python3
"""Temporary Task-1 rubric scorer. Writes pre/post scores as JSON for QUALITY.md."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "pre_scores.json"

ROLE_RE = re.compile(r"You are [a-z]")
HONESTY_RE = re.compile(r"assumption|uncertain|not a lawyer|not financial advice|not medical advice|Note: ", re.I)


def score(path: Path) -> dict:
    rel = path.relative_to(PROMPTS).as_posix()[:-4]
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    idx = next((i for i, l in enumerate(lines) if l.strip() == "# Variables"), None)
    body = "\n".join(lines[5:idx]) if lines[4] and not lines[4].startswith(("#", "When")) else "\n".join(lines[4:idx])
    if body.strip().startswith(("⚠", "ℹ", "🔒")):
        body = "\n".join(lines[6:idx])
    s = {}
    s["role_context"] = 2 if ROLE_RE.search(body) and ("MY DETAILS" in body or "MARKERS" in body or "PASTE" in body) else (1 if ROLE_RE.search(body) else 0)
    s["task_clarity"] = 2 if "YOUR TASK" in body and "exact order" in body else (1 if "TASK" in body else 0)
    s["output_structure"] = 2 if "OUTPUT FORMAT" in body else (1 if "exact order" in body else 0)
    rules_i = next((i for i, l in enumerate(lines) if l.strip().upper().endswith("RULES")), None)
    n_rules = 0
    if rules_i is not None:
        j = rules_i + 1
        while j < len(lines) and (lines[j].startswith("- ") or lines[j].startswith("Note: ")):
            n_rules += 1
            j += 1
    s["constraints"] = 2 if n_rules >= 3 else (1 if n_rules >= 1 else 0)
    s["honesty"] = 2 if HONESTY_RE.search(body) and "assumption" in body.lower() else (1 if HONESTY_RE.search(body) else 0)
    var_lines = [l for l in lines[idx + 1:] if l.startswith("- {")] if idx else []
    lazy = [l for l in var_lines if "see Example values" in l]
    s["variables"] = 2 if var_lines and not lazy and all(len(l) > 25 for l in var_lines) else (1 if var_lines else 0)
    lang = lines[2] if len(lines) > 2 else ""
    s["language"] = 2 if lang.startswith("Language:") and (("AR" in lang and ("dialect" in text or "فصحى" in text or "Modern Standard" in text or "Egyptian" in text)) or "output=EN |" in lang or "user-choice" in lang) else 1
    s["total"] = sum(s.values())
    return {"file": rel, **s}


results = [score(f) for f in sorted(PROMPTS.glob("*/*.txt"))]
OUT.write_text(json.dumps(results, indent=1), encoding="utf-8")
weak = [r for r in results if r["total"] < 11]
mid = [r for r in results if r["total"] in (11, 12)]
print(f"scored={len(results)} weak(<11)={len(weak)} mid(11-12)={len(mid)} strong(13+)={len(results)-len(weak)-len(mid)}")
for r in weak:
    print(f"  WEAK {r['total']:>2} {r['file']}: " + ", ".join(f"{k}={v}" for k, v in r.items() if k not in ("file", "total") and v < 2))
