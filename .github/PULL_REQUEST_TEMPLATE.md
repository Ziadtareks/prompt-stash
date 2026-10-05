# Pull Request

## What does this PR do?

<!-- New prompt / prompt improvement / worked example / docs / tooling / fix -->

## Checklist

- [ ] One logical change (or clearly separated commits)
- [ ] New prompts follow [CONTRIBUTING.md](../CONTRIBUTING.md): strict format, `{snake_case}` variables, declared in `# Variables`, filled in `# Example values`
- [ ] Tested the prompt on at least 2 AI assistants with realistic values
- [ ] Safety disclaimer + `Note:` line added for legal / financial / medical / security prompts; "redact before pasting" reminder where users paste data
- [ ] No duplicated purpose with an existing prompt (searched the folder READMEs)
- [ ] `python scripts/validate_prompts.py` passes
- [ ] `python scripts/build_index.py` run so `prompts.json`, the folder READMEs and `docs/search.html` are fresh
- [ ] `python scripts/check_links.py` passes
- [ ] No secrets, no real personal data, no fabricated statistics or claims

> CI runs all three checks automatically on this PR — you can rely on it, but running them locally first saves a round trip.
