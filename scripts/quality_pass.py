#!/usr/bin/env python3
"""Content-quality pass runner. Stages:
  bodies  — Task 2 (OUTPUT FORMAT) + Task 5 (clarify right-sizing) + Task 6 (filler removal) + Task 1 rewrites
  arabic  — Task 3 (variety + anti-MT blocks)
  vars    — Task 4 (real variable documentation)
Idempotent per stage where practical; prints what it could not apply."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from quality_data_files import F, AR_BLOCKS, STD, AR_ADD  # noqa: E402
from quality_data_vars import VAR_DOCS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
stage = sys.argv[1] if len(sys.argv) > 1 else "all"

CLARIFY_PATTERNS = [
    re.compile(r"^- If critical information is missing, ask up to 3 clarifying questions.*$"),
    re.compile(r"^- If you are missing a key detail, ask me exactly one question.*$"),
    re.compile(r"^- If you are missing a key detail, ask me exactly one targeted question.*$"),
    re.compile(r"^- Do not guess silently — if information is missing, ask me exactly one targeted question first.$"),
    re.compile(r"^- If you need more context, ask me (for it|exactly one question) before (answering|you answer).$"),
    re.compile(r"^- If a detail .*(changes the plan|would change the plan).* ask (one|exactly one) question.*$"),
    re.compile(r"^- If my (goal|statement) (and my draft )?(clearly )?conflict.*ask.*first.$"),
    re.compile(r"^- If the (situation|stop code|term) is ambiguous.*ask.*first.$"),
    re.compile(r"^- If information is missing, ask me exactly one (targeted )?question first.$"),
]
AR_LINE_RE = re.compile(r"If the requested output language is Arabic:")


def split_file(text: str):
    lines = text.splitlines()
    idx = next(i for i, l in enumerate(lines) if l.strip() == "# Variables")
    vidx = next(i for i, l in enumerate(lines) if l.startswith("# Example values:"))
    header, body, variables, example = lines[:4], lines[4:idx], lines[idx:vidx], lines[vidx]
    return header, body, variables, example


def strip_blank(seq):
    out = list(seq)
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


changed = skipped = 0
for f in sorted(PROMPTS.glob("*/*.txt")):
    rel = f.relative_to(PROMPTS).as_posix()[:-4]
    if rel not in F:
        print(f"NO DATA: {rel}")
        continue
    d = F[rel]
    text = f.read_text(encoding="utf-8")
    header, body, variables, example = split_file(text)
    body = strip_blank(body)
    orig_body = list(body)

    # ── stage: bodies ──
    if stage in ("bodies", "all"):
        if d["body"] is not None:
            body = d["body"].splitlines()
        # clarify right-sizing: remove every existing clarify-ish bullet, insert ours after RULES
        body = [l for l in body if not any(p.match(l.strip()) for p in CLARIFY_PATTERNS)]
        cl = d["cl"] if d["cl"] is not None else STD
        done = False
        for i, l in enumerate(body):
            if l.strip().upper().endswith("RULES") and i + 1 <= len(body):
                body.insert(i + 1, cl)
                done = True
                break
        if not done:
            body += ["RULES", cl]
        # extra constraint lines
        for extra in reversed(d["add"]):
            if extra not in body:
                rules_i = next((i for i, l in enumerate(body) if l.strip().upper().endswith("RULES")), None)
                if rules_i is not None:
                    body.insert(rules_i + 1, extra)
                else:
                    body.append(extra)
        # OUTPUT FORMAT section at the end of the body
        if "OUTPUT FORMAT" not in body:
            body += ["", "OUTPUT FORMAT", "- " + d["of"]]

    # ── stage: arabic ──
    ar_key = d["ar"] or AR_ADD.get(rel)
    if stage in ("arabic", "all") and ar_key:
        if not any(AR_BLOCKS.get(d["ar"], [None])[0] == l or (d["ar"] == "choice" and AR_LINE_RE.search(l)) for l in body):
            key = ar_key
            block = list(AR_BLOCKS[key])
            # insert before OUTPUT FORMAT if present, else append
            oi = next((i for i, l in enumerate(body) if l.strip() == "OUTPUT FORMAT"), None)
            block += [""] if oi is None else [""]
            body = body[:oi] + block + body[oi:] if oi is not None else body + block

    # ── stage: vars ──
    if stage in ("vars", "all"):
        new_vars = []
        for l in variables:
            m = re.match(r"^- \{([a-z0-9_]+)\}:", l)
            if m and m.group(1) in VAR_DOCS:
                new_vars.append(f"- {{{m.group(1)}}}: {VAR_DOCS[m.group(1)]}")
            else:
                new_vars.append(l)
        variables = new_vars

    new_text = "\n".join(header + strip_blank(body) + ["", ""] + strip_blank(variables) + [""] + [example]) + "\n"
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        changed += 1
    else:
        skipped += 1

print(f"stage={stage} changed={changed} unchanged={skipped}")
