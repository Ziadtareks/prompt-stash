# Contributing to Prompt Stash 🗄️

Thanks for wanting to add to the stash! The bar is deliberately high — every prompt here is meant to be copy-paste reliable for a stranger on a bad day. This guide tells you exactly what "good" looks like.

**Short on time?** Pick something from the [`good first issue`](https://github.com/Ziadtareks/prompt-stash/labels/good%20first%20issue) queue — each one is scoped to be a safe, satisfying first PR. Not sure about anything? Ask in [Discussions](https://github.com/Ziadtareks/prompt-stash/discussions); no question is too small. Please also keep our [Code of Conduct](CODE_OF_CONDUCT.md) in mind: be kind, be honest, help beginners.

## The format (non-negotiable)

Every prompt lives in `prompts/<folder>/<prompt-name>.txt` and follows this exact layout:

```
Title
When to use it: <one sentence>
Language: prompt=EN | output=EN|AR|EN+AR|user-choice
Tags: comma, separated, lowercase
<disclaimer line — REQUIRED on legal/financial/health/security prompts>

<prompt body>

# Variables
- {variable_name}: one-line explanation

# Example values: {variable_name}=realistic fill, ...
```

### Body rules

1. **Structure**: a specific role, a context block (`MY DETAILS`), an ordered task ("YOUR TASK — answer in this exact order"), and a `RULES` section.
2. **Clarifying rule**: include the standard line — *"If critical information is missing, ask up to 3 clarifying questions first; otherwise proceed with clearly-stated assumptions."*
3. **Variables**: `{snake_case}` everywhere. Every variable used in the body must be declared in `# Variables`.
4. **Language**: for Arabic output, name the register (Modern Standard Arabic vs Egyptian dialect) and forbid stiff machine-translation phrasing.
5. **No filler**: no "you are the world's best…". A specific role with constraints beats flattery.
6. **Safety**: legal/financial/medical/security prompts need a disclaimer line under the tags AND a `Note:` line in the body telling the AI its limits. Security prompts never ask for real passwords, codes, card numbers, or OTPs. Prompts that take pasted data remind users to redact personal/client info.
7. **Honesty**: no invented statistics, no guaranteed outcomes, no fabricated sources. Use `[FILL]` markers where the user must supply facts.

## Naming rules

- File name: lowercase `snake_case`, descriptive, ends with the action (`-fix`, `-writer`, `-planner`).
- Folder: only the 13 existing folders. Proposing a new folder = open an issue first.
- One prompt per file. If it needs "or" in the title, it's two prompts.

## New-prompt checklist

- [ ] No existing prompt covers this (search the folder READMEs first)
- [ ] A real-world use case — you've actually needed it, or cite where people ask for it
- [ ] All `{variables}` declared in `# Variables` with a real explanation (required/optional + format hint + example — the validator rejects lazy "see Example values" lines)
- [ ] Body ends with an `OUTPUT FORMAT` section: sections in order, length/item counts, and what comes first
- [ ] Tested on **at least 2 AI assistants** (e.g. ChatGPT + Claude or Gemini) with the example values
- [ ] Safety notes added if the topic touches legal, money, health, or security
- [ ] Arabic-capable prompts (output AR / EN+AR / user-choice) carry the ARABIC STYLE variety + anti-machine-translation rules
- [ ] File size ≤ 4,500 characters (validator limit — keep prompts paste-friendly; split instead of growing)
- [ ] `python scripts/validate_prompts.py` passes
- [ ] `python scripts/build_index.py` run (regenerates `prompts.json` + folder READMEs)
- [ ] `python scripts/check_links.py` passes

## Local checks

```bash
python scripts/validate_prompts.py   # format validation (also runs in CI on every PR)
python scripts/build_index.py        # regenerate prompts.json + folder READMEs + docs/search.html
python scripts/check_links.py        # every markdown link resolves
```

CI runs automatically on every PR (validate → rebuild → stale-check → link-check) — **as soon as GitHub Actions is available for the account**. Current status (Oct 2026): the workflow is enabled and correct, but GitHub reports *"Actions has been disabled for this user"* at the account level, so no runs fire yet — resolving that requires contacting [GitHub Support](https://support.github.com/contact). Until it's lifted: run the three commands locally, and use the pre-push hook below. Either way, run `build_index.py` before committing so the generated files are fresh.

**Pre-push hook (recommended):** install it once and every `git push` runs the same checks.
- Git Bash (Windows/macOS/Linux): `cp scripts/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push`
- PowerShell (Windows): `Copy-Item scripts\pre-push .git\hooks\pre-push` (no chmod needed)
- Verify it's installed: `git hook run pre-push 2>/dev/null || .git/hooks/pre-push`
- Uninstall: delete `.git/hooks/pre-push`. The hook needs `python` on your PATH; if you use `py` on Windows, edit the hook's first command accordingly.

## Your first contribution (pick one)

1. **A worked example** — pick a prompt you actually use, fill it, and capture the AI's output in `examples/` (see an existing file for the shape). No validator changes needed.
2. **A "when to use it" sharpening** — some intro lines are still flabby. Making one punchier is a real, reviewable PR.
3. **A new prompt from the issue queue** — issues labeled `good first issue` contain pre-scoped prompt ideas with the variables already thought through.
4. **A docs fix** — broken link, unclear instruction, a Windows-vs-Unix gap in this guide. Small PRs welcome.

## Recognition

Every merged PR is credited in the release notes, and repeat contributors are listed in the README's Credits section. No contribution is too small to say thank you for.

## Proposing changes to existing prompts

Open an issue with the "Prompt improvement" template, or go straight to a PR. Keep the original use case; improvements to structure, constraints, and safety are always welcome — rewrites that change the purpose need an issue first.

## Licensing

By contributing, you agree your contributions are licensed under the project's [MIT License](LICENSE).
