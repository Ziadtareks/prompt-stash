# Changelog

All notable changes to Prompt Stash are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses semver where MAJOR = prompt-format or breaking structural changes.

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
