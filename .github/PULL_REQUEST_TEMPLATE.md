# Pull Request

## What does this PR do?

<!-- New prompt / prompt improvement / docs / tooling / fix -->

## Checklist

- [ ] One logical change (or clearly separated commits)
- [ ] New prompts follow [CONTRIBUTING.md](../CONTRIBUTING.md): strict format, `{snake_case}` variables, declared in `# Variables`, filled in `# Example values`
- [ ] Tested the prompt on at least 2 AI assistants with realistic values
- [ ] Safety disclaimer + `Note:` line added for legal / financial / medical / security prompts; "redact before pasting" reminder where users paste data
- [ ] No duplicated purpose with an existing prompt (searched the folder READMEs)
- [ ] `python scripts/validate_prompts.py` passes
- [ ] `python scripts/build_index.py` run so `prompts.json` and the folder READMEs are fresh
- [ ] `python scripts/check_links.py` passes
- [ ] No secrets, no real personal data, no fabricated statistics or claims
