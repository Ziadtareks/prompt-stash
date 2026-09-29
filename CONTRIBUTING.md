# Contributing to Prompt Stash 🗄️

Thanks for wanting to add to the stash! The bar is deliberately high — every prompt here is meant to be copy-paste reliable for a stranger on a bad day. This guide tells you exactly what "good" looks like.

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
- [ ] All `{variables}` declared in `# Variables` and shown in `# Example values`
- [ ] Tested on **at least 2 AI assistants** (e.g. ChatGPT + Claude or Gemini) with the example values
- [ ] Safety notes added if the topic touches legal, money, health, or security
- [ ] `python scripts/validate_prompts.py` passes
- [ ] `python scripts/build_index.py` run (regenerates `prompts.json` + folder READMEs)
- [ ] `python scripts/check_links.py` passes

## Local checks

```bash
python scripts/validate_prompts.py   # format validation (also runs in CI on PRs)
python scripts/build_index.py        # regenerate prompts.json + folder READMEs
python scripts/check_links.py        # every markdown link resolves
```

CI runs all three on every pull request — your PR will fail if the generated files are stale, so run `build_index.py` before committing.

## Proposing changes to existing prompts

Open an issue with the "Prompt improvement" template, or go straight to a PR. Keep the original use case; improvements to structure, constraints, and safety are always welcome — rewrites that change the purpose need an issue first.

## Licensing

By contributing, you agree your contributions are licensed under the project's [MIT License](LICENSE).
