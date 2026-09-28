# 🗄️ Prompt Stash

> A stash of 29 copy-paste AI prompts for debugging, work, content, study, business, dev & daily life — plain text, zero setup.

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
| Lesson Summarizer | A class or lecture needs to become clean revision notes | [`prompts/study/summarize-lesson.txt`](prompts/study/summarize-lesson.txt) |
| Flashcard Maker | You have study material and want question-answer flashcards | [`prompts/study/flashcards-maker.txt`](prompts/study/flashcards-maker.txt) |
| Exam Revision Planner | An exam is coming and you don't know how to split your days | [`prompts/study/exam-revision.txt`](prompts/study/exam-revision.txt) |
| Term Translator (EN ↔ AR) | An English study term needs its Arabic meaning explained | [`prompts/study/translate-term.txt`](prompts/study/translate-term.txt) |
| Essay Outline Builder | An essay assignment and a blank page — build the skeleton first | [`prompts/study/essay-outline.txt`](prompts/study/essay-outline.txt) |
| Customer Reply Writer | A store customer messaged and you need a professional reply fast | [`prompts/business/store-reply.txt`](prompts/business/store-reply.txt) |
| Invoice Writer | You finished client work and need a clean invoice with the right wording | [`prompts/business/invoice-words.txt`](prompts/business/invoice-words.txt) |
| Price Explainer | A client says your price is too high and you must justify it | [`prompts/business/price-calc-explain.txt`](prompts/business/price-calc-explain.txt) |
| Booking Confirmation Message | Someone booked your service and needs a clear confirmation | [`prompts/business/booking-confirm.txt`](prompts/business/booking-confirm.txt) |
| Refund Apology Letter | You must refund a customer and want to keep their trust | [`prompts/business/refund-apology.txt`](prompts/business/refund-apology.txt) |
| README Writer | You built a project and the README is empty or embarrassing | [`prompts/dev/readme-writer.txt`](prompts/dev/readme-writer.txt) |
| Commit Message Writer | You have staged changes and "fixed stuff" is not a commit message | [`prompts/dev/commit-message.txt`](prompts/dev/commit-message.txt) |
| Regex Explainer | You found a regex and have no idea what it actually matches | [`prompts/dev/regex-explain.txt`](prompts/dev/regex-explain.txt) |
| SQL Query Fixer | Your SQL query is slow or returns wrong rows | [`prompts/dev/sql-fix.txt`](prompts/dev/sql-fix.txt) |
| API Error Decoder | An API returns an error code and the docs didn't help | [`prompts/dev/api-error.txt`](prompts/dev/api-error.txt) |
| Habit Plan Builder | You want a habit and keep quitting by day four | [`prompts/daily/habit-plan.txt`](prompts/daily/habit-plan.txt) |
| Budget Splitter | Payday came and the money vanishes before month's end | [`prompts/daily/budget-split.txt`](prompts/daily/budget-split.txt) |
| Trip Packing List | You always arrive and realize you forgot something important | [`prompts/daily/trip-pack-list.txt`](prompts/daily/trip-pack-list.txt) |
| Beginner Workout Plan | You want to start exercising at home with no equipment | [`prompts/daily/workout-plan.txt`](prompts/daily/workout-plan.txt) |
| Sleep Routine Fixer | You scroll until 2am and feel wrecked every morning | [`prompts/daily/sleep-routine.txt`](prompts/daily/sleep-routine.txt) |

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
│   ├── content/
│   │   ├── captions-ar.txt
│   │   ├── hashtags.txt
│   │   └── bio-maker.txt
│   ├── study/
│   │   ├── summarize-lesson.txt
│   │   ├── flashcards-maker.txt
│   │   ├── exam-revision.txt
│   │   ├── translate-term.txt
│   │   └── essay-outline.txt
│   ├── business/
│   │   ├── store-reply.txt
│   │   ├── invoice-words.txt
│   │   ├── price-calc-explain.txt
│   │   ├── booking-confirm.txt
│   │   └── refund-apology.txt
│   ├── dev/
│   │   ├── readme-writer.txt
│   │   ├── commit-message.txt
│   │   ├── regex-explain.txt
│   │   ├── sql-fix.txt
│   │   └── api-error.txt
│   └── daily/
│       ├── habit-plan.txt
│       ├── budget-split.txt
│       ├── trip-pack-list.txt
│       ├── workout-plan.txt
│       └── sleep-routine.txt
├── LICENSE
├── README.md
└── RELEASE_NOTES.md
```

Every prompt file is 3 parts, in order: **title** (line 1), **when to use** (line 2), then the full copy-paste prompt with `{variables}`.

## ➕ Add your own

PRs welcome — one prompt per `.txt` file, same 3-part format, plain beginner-friendly English (Arabic output where relevant), and `{variables}` for anything user-specific.

## 📄 License

MIT — free to use, share, and remix. See [LICENSE](LICENSE).

Made by **[Ziad Tarek](https://github.com/Ziadtareks)**
