# 🗄️ Prompt Stash

> A tiny stash of 9 copy-paste AI prompts for debugging, work, and content — plain text, zero setup.

No app, no signup, no dependencies. Open a `.txt` file, fill in the `{variables}`, paste it into any AI chat (ChatGPT, Claude, Gemini…), and get a useful answer instead of a generic one. Curated from the prompts people actually ask for on Reddit and GitHub.

## 📋 The Stash

| Prompt | Use it when | File |
|---|---|---|
| Website Error Fixer | Your site shows an error and you don't know where to start | [`prompts/debugging/website-error-fix.txt`](prompts/debugging/website-error-fix.txt) |
| Blue Screen (BSOD) Explainer | Windows crashed with a blue screen stop code | [`prompts/debugging/bsod-explain.txt`](prompts/debugging/bsod-explain.txt) |
| Deploy Rollback Plan | A fresh deployment broke production and you need to recover fast | [`prompts/debugging/deploy-rollback.txt`](prompts/debugging/deploy-rollback.txt) |
| Meeting Notes Cleaner | Messy meeting notes need to become a summary + action items | [`prompts/work/meeting-notes-fix.txt`](prompts/work/meeting-notes-fix.txt) |
| Reply Tone Rewriter | Your email/message reply draft has the wrong tone | [`prompts/work/reply-tone.txt`](prompts/work/reply-tone.txt) |
| CV Bullet Writer | You need resume bullets that sound impressive (and stay honest) | [`prompts/work/cv-bullets.txt`](prompts/work/cv-bullets.txt) |
| Arabic Caption Writer | You need natural Arabic captions for a social post | [`prompts/content/captions-ar.txt`](prompts/content/captions-ar.txt) |
| Hashtag Finder | You want a discovery-focused hashtag set (broad + niche) | [`prompts/content/hashtags.txt`](prompts/content/hashtags.txt) |
| Social Bio Maker | Your profile bio is empty, outdated, or says nothing | [`prompts/content/bio-maker.txt`](prompts/content/bio-maker.txt) |

## 🚀 How to use

1. Open any `.txt` file and copy everything.
2. Replace the `{variables}` with your own details.
3. Paste it into any AI chat and hit enter.

## 🗂 Structure

```
prompt-stash/
├── prompts/
│   ├── debugging/
│   │   ├── website-error-fix.txt
│   │   ├── bsod-explain.txt
│   │   └── deploy-rollback.txt
│   ├── work/
│   │   ├── meeting-notes-fix.txt
│   │   ├── reply-tone.txt
│   │   └── cv-bullets.txt
│   └── content/
│       ├── captions-ar.txt
│       ├── hashtags.txt
│       └── bio-maker.txt
├── LICENSE
├── README.md
└── RELEASE_NOTES.md
```

Every prompt file is 3 parts, in order: **title** (line 1), **when to use** (line 2), then the full copy-paste prompt with `{variables}`.

## ➕ Add your own

PRs welcome — one prompt per `.txt` file, same 3-part format, plain beginner-friendly English, and `{variables}` for anything user-specific.

## 📄 License

MIT — free to use, share, and remix. See [LICENSE](LICENSE).

Made by **[Ziad Tarek](https://github.com/Ziadtareks)**
