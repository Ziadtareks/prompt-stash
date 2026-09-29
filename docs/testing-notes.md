# Testing notes — Task 8, v4.1.0 content-quality pass

**Method (honest):** structured desk-checks, not live model runs. For each prompt below we filled the variables with plausible fictional inputs, stepped through the prompt as a strong assistant would, and checked three things: (1) does the OUTPUT FORMAT section fully determine the answer's shape, (2) do the constraints actually bind (no invented facts, no guaranteed outcomes, redaction reminders), (3) does the clarifying rule fire only when it should. No pass rates are claimed — these are findings, not benchmarks.

## Prompts checked (10)

| Prompt | Category | Finding | Action |
|---|---|---|---|
| `arabic-life/formal-arabic-email` | Arabic output (MSA) | Variety fixed to فصحى رسمية معاصرة; honorifics/closing conventions present; no-invented-citations rule present. Example values contain no law numbers. | None needed |
| `arabic-life/occasion-messages` | Arabic output (variants) | **Incoherence found:** the task list asked for short/medium/long in one dialect while OUTPUT FORMAT demanded 2-3 formality-labeled variants per length. | **Fixed** — task list now requests formality-labeled variants per length (فصحى رسمية → ودية مصرية) |
| `business/contract-summary` | Legal disclaimer | 6 sections in order ending with the disclaimer line; red-flag clause categories enumerated; `[تحقق]`-style placeholders consistent with the no-invented-citations rule. | None needed |
| `daily/budget-split` | Financial disclaimer | Warning-check trigger (>60%) is objective; the 3-fixes cap prevents advice sprawl; "compare to my own goal, not ideal budgets" binds scope. Missing-numbers path uses [MISSING] markers. | None needed |
| `dev/commit-message` | Dev | Subject/body limits are checkable; split advice section prevents bundled-commit mess; breaking-change footer conditional is explicit. | None needed |
| `dev/sql-fix` | Dev | Fixed SQL + "why it works" + index-or-skip keeps the answer falsifiable; the "ask exactly one question if 'wrong' is ambiguous" rule replaces the generic 3-question rule correctly. | None needed |
| `study/feynman-explain` | Interactive | **Issues found:** duplicated rules from two passes; one rule missing its bullet marker; interaction rules and honesty rule now explicit (one question per message, wait, min 2 rounds, accuracy-over-encouragement). | **Fixed** — rules deduplicated, bullet normalized, honesty line added |
| `files-data/csv-cleaner` | Data cleaning | Preserve-first step, ordered cleaning steps, and the traps section (Egyptian phone leading zeros, date flips) are concrete; [MISSING] convention prevents silent gap-filling; redaction reminder present. | None needed |
| `career/cv-reviewer` | Career | Judged against the pasted posting (not an imaginary ideal); [FILL] convention blocks invented metrics; verdict is forced to one of three options. | None needed |
| `security-basics/phishing-spotter` | Security | "Links replaced with [LINK]" is enforced in the variable docs and example; verdict is forced to a 4-value scale; if-already-paid triage is ordered. No request for real credentials anywhere. | None needed |

## What was learned

1. **Mechanical insertion needs a normalization step.** The clarifying-rule insertion left bullets without their `- ` marker in 70 files and dropped the blank line after the header in 90 — none of which the original validator caught. Both are now covered (the bullet fix is content-side; the blank line is format-side).
2. **Two regimes of the clarifying rule are legitimate.** Advisory prompts keep the 3-question rule with named specifics; input-complete prompts (summarizers, translators, rewriters, cleaners) use "say what's missing instead of proceeding on assumptions"; interactive prompts (feynman-explain, interview-prep, homework-hint, difficult-conversation-rehearsal) use turn-taking rules. The validator accepts all three and rejects none-and-neither.
3. **OUTPUT FORMAT and the task list can drift apart** when one is edited without the other (caught in occasion-messages). The validator now requires OUTPUT FORMAT to exist; the CI diff check keeps generated tables fresh, but content coherence between task list and OUTPUT FORMAT remains a human review point.
4. **Arabic-capable prompts need the variety decision stated per file**, not inferred: user-choice files now carry the conditional "If the requested output language is Arabic…" rule, so the model never guesses a register.

## Not covered

- No live-model runs were performed in this pass; behavior across specific model versions is untested.
- The remaining 120 prompts had the same mechanical checks applied (validator) but not individual desk-checks.
