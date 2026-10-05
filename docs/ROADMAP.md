# 🗺️ Roadmap — prepared ground, no promised dates

Prompt Stash's core promise stays fixed: **plain `.txt` files, zero setup, MIT, no accounts, no API keys, no framework.** Everything below extends that core without ever becoming a requirement to use the library. Items are listed in the order they become cheap to build, given what already exists.

## What already exists (the foundation)

| Piece | Where | Why it matters for the future |
|---|---|---|
| Machine-readable index | [`prompts.json`](../prompts.json) — title, when-to-use, folder, language, tags, variables, safety flag per prompt | The single source every tool below reads; nothing scrapes `.txt` files |
| Self-contained search page | [`docs/search.html`](search.html) — zero-dependency, works offline via `file://` | Ready to serve as-is on GitHub Pages; no build step exists to port |
| Strict validated format | [`scripts/validate_prompts.py`](../scripts/validate_prompts.py) | Any exporter/converter can trust the input structure |
| CI + staleness checks | [`.github/workflows/validate.yml`](../.github/workflows/validate.yml) | Generated artifacts can't drift from the prompt files |

## Next steps (cheap, high-leverage)

1. **GitHub Pages for the search page** — Repo Settings → Pages → "Deploy from a branch" → `main` + `/docs`. That's the entire task; `search.html` already links to the repo and filters by tag, folder, and Arabic text. *(One settings change — no code.)*
2. **Espanso export** — a small `scripts/export_espanso.py` that reads `prompts.json` and writes one `.yml` trigger file per prompt (e.g. `:ps-meeting-notes`). Pure stdlib, same pattern as `build_index.py`. The validator would gain an "exports are fresh" staleness check.
3. **Raycast / Alfred snippet export** — same importer, different serializer (`.json`/`.csv`). Only worth doing after (2) proves the export pattern.

## Further out (only when someone asks loudly)

4. **Chrome extension** — a popup that loads `prompts.json` from a pinned release tag and inserts the chosen prompt into the focused textarea. Structure note: the extension would ship read-only index + files, so the repo stays the only source of truth.
5. **"Copy" buttons on a hosted index** — the GitHub Pages search page gains a copy-to-clipboard button (one `navigator.clipboard.writeText` per hit).
6. **Prompt deep links** — a `?q=` parameter on the search page so people can share pre-filtered views (e.g. `search.html?q=عقد`).

## Non-goals

- No accounts, sync, or telemetry — the folder of `.txt` files must remain fully functional on its own.
- No runtime dependency for the core experience: everything here is optional sugar around files you can read with `cat`.
- No prompt "ratings" or tracking — curation happens through the Hall of Fame and review, not metrics.
