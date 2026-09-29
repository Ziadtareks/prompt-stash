# Changelog

All notable changes to Prompt Stash are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses semver where MAJOR = prompt-format or breaking structural changes.

## [Unreleased] — v4.1.1

### Fixed
- Working-tree line endings: `.gitattributes` now enforces `eol=lf` for `*.txt`, `*.md`, `*.py`, `*.json`, `*.yml` and `scripts/pre-push`; 173 files had CRLF on disk after checkout (repo blobs were already LF).

### Changed
- `scripts/validate_prompts.py` additionally detects CRLF, UTF-8 BOM, duplicate prompt titles, and stale generated files (`prompts.json` / folder READMEs) — failing with clear messages.
- `scripts/build_index.py` writes LF explicitly, so the pre-push hook is idempotent (no phantom diffs).
- 13 generic variable explanations replaced with specific ones (what to enter + format example).
- CONTRIBUTING.md states that CI is currently unavailable, points to local checks and the pre-push hook, and documents both Windows (PowerShell `Copy-Item`) and Git Bash hook-install commands; PR template no longer implies CI runs.
- Arabic proofread across prompts and examples: fixed the مصراعيها idiom, a leftover untranslated term in legal-terms-explain example values, stiff phrasing (صياغة رصينة، تكثيف القصة، طابع إعلان), a doubled بالعربية, and mixed-script fragments in examples.

### Not changed
- Prompt purposes, file and folder names, the header format, license, About description, and topics (already correct).

## [4.1.0] — 2026-09-29

### Changed (content quality — the format was already standard; this pass made the prompts produce specific, structured answers)
- **All 130 prompts** now end with an explicit `OUTPUT FORMAT` section (sections in order, length/item counts, what leads).
- **Clarifying rules right-sized per prompt type:** advisory prompts keep the 3-question rule with named specifics; input-complete prompts (summarizers, translators, rewriters, cleaners) use a shorter assumptions rule; interactive prompts (feynman-explain, interview-prep, homework-hint, difficult-conversation-rehearsal) use explicit turn-taking rules.
- **All 385 placeholder variable explanations replaced** with real docs (required/optional + format hint + example); 7 near-duplicate variables' docs corrected per file context.
- **Arabic quality:** all 28 Arabic-capable prompts carry an `ARABIC STYLE` block — variety fixed per use case (فصحى for formal/official, Egyptian dialect for casual), anti-machine-translation rules, honorifics/closing conventions, and a ban on invented law numbers or official fees; occasion-messages now requires 2-3 formality-labeled variants per message length and cultural/religious tone rules.
- Rubric pass across all 130 prompts (7 criteria × 0-2): average **11.24 → 13.12 / 14**; bodies with filler or generic-answer risk tightened. Details in the v4.1.0 rubric review (QUALITY.md, since removed).

### Added
- Validator checks: OUTPUT FORMAT presence, no lazy variable docs, Arabic variety statement for Arabic-output prompts, file size limit (4,500 chars), mojibake/Latin-in-Arabic-word detection.
- `docs/testing-notes.md` — desk-check findings for 10 prompts (2 Arabic-output, 2 legal/financial, 2 dev, 1 interactive, 1 data-cleaning, 1 career, 1 security).
- 3 new worked examples (content, daily, security-basics): **16 examples covering all 13 folders**.

### Fixed
- feynman-explain: duplicated rules, missing bullet marker, misplaced `{context}` doc.
- password-checkup: clarifying rule duplicated the security note instead of handling missing info.
- occasion-messages: task list contradicted its OUTPUT FORMAT (single-dialect vs formality variants).
- ~90 files: blank-line separator after the header lost in an earlier pass; ~70 files: bullet markers on inserted rules.

### Not changed
- Prompt purposes, file and folder names, the standard header layout, the MIT license, and the zero-setup plain-text promise. Prompts already meeting the quality bar were not edited for the sake of a diff.

## [Unreleased] — v4.0.0

### Changed
- **Every prompt file standardized to one strict format**: `Title` → `When to use it:` → `Language: prompt=… | output=…` → `Tags:` → body → `# Variables` block → `# Example values` line. Bodies stay copy-paste friendly.
- Consistent `{snake_case}` variables everywhere; every variable declared in `# Variables` with a one-line explanation.
- Every prompt now instructs the AI to ask up to 3 clarifying questions only when critical information is missing, otherwise proceed with stated assumptions.
- Removed filler; verified every prompt has a defined role, ordered task, and output structure. Fixed Arabic typos in rental-contract-explain and legal-terms-explain; gave feynman-explain an explicit task marker.

### Added
- **Safety & honesty layer** on 38 prompts touching legal, financial, health, or security topics (and on prompts that accept pasted personal/client data): human-readable disclaimer under the header + a `Note:` line instructing the AI to state its limits. Security prompts never request real passwords, codes, card numbers, or OTPs.
- **5 new `daily` prompts** (folder completed to 10): weekly-meal-planner, expenses-review, difficult-conversation-rehearsal, decision-matrix, weekly-reset. Total: **130 prompts**.
- **`examples/`** — 13 worked demonstrations (filled prompt + realistic AI response, clearly labeled as non-guaranteed), covering 10 folders including 3 Arabic-output prompts.
- **Quality tooling** (standard library only, optional to use): `scripts/validate_prompts.py`, `scripts/build_index.py` (generates `prompts.json` + per-folder READMEs), `scripts/check_links.py`; GitHub Actions workflow running all three on PRs.
- **Community files**: CONTRIBUTING.md, issue templates ("New prompt idea", "Prompt improvement"), pull-request template, Code of Conduct, this changelog, `TOPICS.txt` (suggested GitHub topics), `docs/launch-post.md` (draft announcement).

### Changed (docs)
- README rebuilt: one-line pitch, 30-second before/after, Top-15 table, per-folder index, language guide, quick-finder, and an honest Limitations section. The full prompt tables moved into each folder's README (generated).

## [3.0.0] — 2026-09-29

### Added
- 96 prompts: existing folders topped up to 10 each (debugging, work, content, study, business, dev) and 6 new folders — ai-coding, career, marketing, files-data, security-basics, arabic-life (10 each). Total: 125 prompts across 13 folders; `daily` intentionally stayed at 5.
- New-file standard at the time: title (line 1), when-to-use (line 2), full prompt with `{variables}`, `# Example values` line; Egypt-relevant content (EGP, Arabic output options); defensive-only security prompts.
- README folder tree + counts; topics study/business.

## [2.0.0] — 2026-09-29

### Added
- 20 prompts and 4 new folders: study, business, dev, daily (5 each). Total: 29 prompts across 7 categories.
- README table of all prompts with use cases and file paths.

## [1.0.0] — 2026-09-29

### Added
- Initial release: 9 prompts across debugging, work, and content.
- MIT license, README, release notes.
