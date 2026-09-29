# 🗄️ Prompt Stash

**130 copy-paste AI prompts across 13 folders — plain text, zero setup, English + Arabic/Egyptian.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Prompts](https://img.shields.io/badge/prompts-130-8b5cf6)
![Folders](https://img.shields.io/badge/folders-13-blue)
![Format](https://img.shields.io/badge/format-plain%20txt-success)

No app, no signup, no build step. Open a `.txt` file, fill in the `{variables}`, paste it into any AI chat. Every prompt has a defined role, structure, and output format — plus safety notes where it touches legal, money, health, or security topics.

## ⚡ Try it in 30 seconds

**Without a prompt (what most people type):**

> summarize my meeting notes

…and you get a vague paragraph that misses decisions and actions.

**With Prompt Stash — open [`prompts/work/meeting-notes-fix.txt`](prompts/work/meeting-notes-fix.txt), paste it, and replace the variables:**

> You are my executive assistant. Turn my raw notes into a clean, skimmable summary…
> --- NOTES START ---
> june launch call — ahmed says dev costs up 15%… shady to get 3 quotes… mariam wants 2 days off mid june
> --- NOTES END ---

…and you get: a 3-line TL;DR, a **key decisions** list, an **action-items table** (task / owner / deadline), open questions, and a ready-to-send follow-up email. [See a full worked example →](examples/work-meeting-notes-fix.md)

## 🏆 Top 15 prompts

| Prompt | Use it when | File |
|---|---|---|
| Meeting Notes Cleaner | Messy notes → summary + action items | [`work/meeting-notes-fix`](prompts/work/meeting-notes-fix.txt) |
| Commit Message Writer | "fixed stuff" is not a commit message | [`dev/commit-message`](prompts/dev/commit-message.txt) |
| Website Error Fixer | Your site shows an error, you don't know where to start | [`debugging/website-error-fix`](prompts/debugging/website-error-fix.txt) |
| CV Reviewer | Your CV isn't landing interviews for a specific job | [`career/cv-reviewer`](prompts/career/cv-reviewer.txt) |
| Interview Prep Coach | Practice answers out loud with blunt feedback | [`career/interview-prep`](prompts/career/interview-prep.txt) |
| Budget Splitter | Payday money vanishes before month's end | [`daily/budget-split`](prompts/daily/budget-split.txt) |
| Weekly Meal Planner | A week of dinners + one shopping list, on a budget | [`daily/weekly-meal-planner`](prompts/daily/weekly-meal-planner.txt) |
| Excel Formula Builder | Describe the goal in words, get the formula | [`files-data/excel-formula`](prompts/files-data/excel-formula.txt) |
| WhatsApp Broadcast Writer | Customer messages that get read, not muted | [`marketing/whatsapp-broadcast`](prompts/marketing/whatsapp-broadcast.txt) |
| Quotation Writer | "How much?" → a professional quote that protects you | [`business/quotation-writer`](prompts/business/quotation-writer.txt) |
| Feature-to-Prompt Translator | Your one-line feature request gets junk code | [`ai-coding/feature-to-prompt`](prompts/ai-coding/feature-to-prompt.txt) |
| Phishing Spotter | A message feels off — check it before you tap | [`security-basics/phishing-spotter`](prompts/security-basics/phishing-spotter.txt) |
| Formal Arabic Email Writer | رسمية بالعربية الفصحى — companies, ministries, universities | [`arabic-life/formal-arabic-email`](prompts/arabic-life/formal-arabic-email.txt) |
| Egyptian Dialect Coach | فصحى → natural Egyptian for videos and ads | [`arabic-life/dialect-coach`](prompts/arabic-life/dialect-coach.txt) |
| Flashcard Maker | Study material → ready-to-use flashcards | [`study/flashcards-maker`](prompts/study/flashcards-maker.txt) |

## 📂 Browse all 130 prompts by folder

| Folder | Prompts | What's inside |
|---|---|---|
| 🐞 [debugging](prompts/debugging/README.md) | 10 | Fix the thing that broke — websites, Windows, printers, batteries, email |
| 💼 [work](prompts/work/README.md) | 10 | Meetings, emails, priorities and the career conversations in between |
| ✍️ [content](prompts/content/README.md) | 10 | Posts, captions, hooks and calendars — bilingual where it matters |
| 📚 [study](prompts/study/README.md) | 10 | Understand faster and remember longer — notes, quizzes, plans |
| 🏪 [business](prompts/business/README.md) | 10 | Run a small business: clients, quotes, invoices, complaints |
| 💻 [dev](prompts/dev/README.md) | 10 | Everyday developer repairs — git, SQL, logs, reviews, Docker |
| 🌱 [daily](prompts/daily/README.md) | 10 | Money, food, sleep, habits and the choices in between |
| 🤖 [ai-coding](prompts/ai-coding/README.md) | 10 | Work with AI coding tools: better prompts, tests, refactors, reviews |
| 🎯 [career](prompts/career/README.md) | 10 | Job search and promotion — CVs, interviews, LinkedIn, negotiations |
| 📣 [marketing](prompts/marketing/README.md) | 10 | Ads, WhatsApp, landing pages and seasons for small businesses |
| 🗃️ [files-data](prompts/files-data/README.md) | 10 | Tame spreadsheets, PDFs and folders into clean answers |
| 🔐 [security-basics](prompts/security-basics/README.md) | 10 | Defensive everyday security — no fear, just checklists |
| 🇪🇬 [arabic-life](prompts/arabic-life/README.md) | 10 | Formal Arabic, Egyptian dialect and Egypt paperwork — done right |

📸 **[Worked examples](examples/README.md)** — 13 prompts shown with filled variables and a realistic AI response.

## 🌍 Language guide

Line 3 of every prompt file declares its languages:

| Header | Meaning |
|---|---|
| `Language: prompt=EN \| output=EN` | Instructions in English, answer in English |
| `Language: prompt=EN \| output=AR` | Instructions in English, answer in Arabic (dialect named inside the prompt — Modern Standard or Egyptian) |
| `Language: prompt=EN \| output=EN+AR` | Answer delivered in both languages |
| `Language: prompt=EN \| output=user-choice` | The prompt has a `{language}` variable — you pick the output language |

Arabic-output prompts explicitly forbid stiff machine-translation phrasing and name the register (فصحى or Egyptian) per use case.

## 🧭 Which prompt should I use?

- **"I have a work problem"** → [work](prompts/work/README.md) (emails, meetings, priorities) or [career](prompts/career/README.md) (salary, interviews, promotion)
- **"I need Arabic text"** → [arabic-life](prompts/arabic-life/README.md) for formal/community writing, [content](prompts/content/README.md) for captions
- **"I'm debugging code"** → [dev](prompts/dev/README.md), or [debugging](prompts/debugging/README.md) if it's your computer, not your code
- **"I'm starting/running a small business"** → [business](prompts/business/README.md) + [marketing](prompts/marketing/README.md)
- **"I'm studying for an exam"** → [study](prompts/study/README.md)
- **"My files/data are a mess"** → [files-data](prompts/files-data/README.md)
- **"I want to build something with AI"** → [ai-coding](prompts/ai-coding/README.md)
- **"Something feels like a scam"** → [security-basics](prompts/security-basics/README.md)
- **"Life admin is chaos"** → [daily](prompts/daily/README.md)

## 📐 File format

Every prompt file follows one strict format (enforced by [`scripts/validate_prompts.py`](scripts/validate_prompts.py)):

```
Title
When to use it: <one sentence>
Language: prompt=EN | output=EN
Tags: comma, separated, lowercase
<disclaimer line — only on legal/financial/health/security prompts>

<prompt body: role, context, ordered task, constraints, output format>

# Variables
- {name}: what to fill in
# Example values: {name}=realistic fill, ...
```

The body works when pasted alone. Every prompt tells the AI to ask up to 3 clarifying questions only if critical info is missing — otherwise proceed with stated assumptions.

## ⚠️ Limitations (honest section)

- **Prompts are starting points, not magic.** They structure the request; you still supply the judgment and the real facts.
- **Outputs vary** by model, version, and mood of the day. The [examples](examples/README.md) are real single-pass generations, not guaranteed results.
- **Not professional advice.** Legal, financial, medical, and security prompts explicitly tell the AI its limits and point you to professionals for the serious stuff.
- **Egypt/Arabic focus** is a feature and a limit: EGP, Egyptian dialect, and local norms are first-class; other regions work but aren't specialized.
- Numbers in examples are fictional. Nothing in this repo is a statistic about real usage.

## 🤝 Contributing

PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for the file format, the checklist, and how to run the validator. Good first issues are tagged in the tracker.

## 📄 License

MIT — free to use, share, and remix. See [LICENSE](LICENSE).

Made by **[Ziad Tarek](https://github.com/Ziadtareks)**
