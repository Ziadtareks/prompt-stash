# 🗄️ PROMPT STASH

```text
 ╔═══════════════════════════════════════════════════════════════════════════╗
 ║   P R O M P T   S T A S H                                                 ║
 ║   135 Production-Grade AI Prompts • Zero Setup • Pure Copy-Paste          ║
 ║   Built for Builders, Freelancers, Teams & Students • 100% Plain Text     ║
 ╚═══════════════════════════════════════════════════════════════════════════╝
```

> **Stop talking to AI like a chatbot. Start directing it like a senior teammate.**

[![License: MIT](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Ziadtareks/prompt-stash?style=for-the-badge&logo=github&color=facc15)](https://github.com/Ziadtareks/prompt-stash/stargazers)
[![Latest Release](https://img.shields.io/github/v/release/Ziadtareks/prompt-stash?style=for-the-badge&logo=github&color=8b5cf6)](https://github.com/Ziadtareks/prompt-stash/releases)
![Prompts](https://img.shields.io/badge/Prompts-135%20Ready-f97316?style=for-the-badge)
![Folders](https://img.shields.io/badge/Categories-13%20Hubs-3b82f6?style=for-the-badge)
![Format](https://img.shields.io/badge/Format-Plain%20.txt-success?style=for-the-badge)
[![Worked Examples](https://img.shields.io/badge/Worked%20Examples-23%20Real%20Cases-ec4899?style=for-the-badge)](examples/README.md)
[![Validate & Build](https://github.com/Ziadtareks/prompt-stash/actions/workflows/validate.yml/badge.svg)](https://github.com/Ziadtareks/prompt-stash/actions/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-06b6d4?style=for-the-badge)](CONTRIBUTING.md)

---

No web apps to configure. No API keys. No subscription paywalls.  
Just 135 battle-tested `.txt` files engineered with strict roles, ordered execution, concrete output structures, and real-world boundaries. Open any prompt, fill `{variables}`, and watch ChatGPT, Claude, or Gemini deliver actual work instead of fluffy generalities.

**🆕 New in v4.2:** [government paperwork navigator](prompts/arabic-life/paperwork-guide.txt) 🏛️ · [LinkedIn post writer](prompts/content/linkedin-post.txt) (Egyptian Arabic option) 💬 · [security-focused code review](prompts/dev/security-review.txt) 🔐 · [status update emails](prompts/work/status-update-email.txt) ✉️ · [Instagram captions](prompts/content/instagram-captions.txt) 📸 — plus a [browser search page](docs/search.html) over the whole stash.

## 📋 Contents

1. [The 3-Step Recipe](#-the-3-step-recipe-in-30-seconds) — how it works in half a minute
2. [Quick Start in 60 Seconds](#-quick-start-in-60-seconds) — a fully filled prompt, input → output
3. [Fast-Track Solutions](#-fast-track-solutions) — click your current bottleneck
4. [The Hall of Fame](#-the-hall-of-fame-top-15-staff-picks) — the top 15 staff picks
5. [The 5 Power Hubs](#-the-5-power-hubs-choose-your-workflow) — all 135 prompts by folder
6. [The Prompt Blueprint](#️-the-prompt-blueprint) — the strict format every file follows
7. [Language Matrix](#-language-matrix) — English, فصحى, Egyptian dialect
8. [Search & Examples](#-search--examples) — the browser search page + 23 worked cases
9. [Limitations](#️-grounded-reality--limitations) — the honest part
10. [Contributing & License](#-want-to-add-a-prompt) — join in

---

## ⚡ The 3-Step Recipe (In 30 Seconds)

```text
  1. PICK A RECIPE            2. INJECT YOUR CONTEXT            3. GET CLEAN OUTPUT
 ┌──────────────────────┐    ┌───────────────────────────┐    ┌──────────────────────┐
 │ Open any .txt prompt │ ─> │ Replace {variables} with │ ─> │ Paste into any AI    │
 │ from the 13 folders  │    │ your raw notes, code, etc │    │ (Tables, steps, zero │
 └──────────────────────┘    └───────────────────────────┘    │ hallucinated fluff)  │
                                                              └──────────────────────┘
```

### 🥊 The Vibe Check: Before vs After

| ❌ What most people paste | ✅ What Prompt Stash delivers |
|---|---|
| *"Summarize my meeting notes"* | **Role + Guardrails + Strict Format:** |
| ↳ **AI gives:** 4 generic paragraphs that bury the real decisions and miss who owns what. | ↳ **AI delivers:** 3-sentence TL;DR + Bulleted decisions + Table of action items (`Task \| Owner \| Deadline`) + Ready-to-send attendee email. |

👉 **[See how it works on real meeting notes →](examples/work-meeting-notes-fix.md)**

---

## 🚀 Quick Start in 60 Seconds

**Pick:** [`work/meeting-notes-fix`](prompts/work/meeting-notes-fix.txt) · **Fill:** the `{variables}` · **Paste:** into any AI chat.

Here is the prompt with its variables filled — exactly what you'd paste:

```text
You are my executive assistant. Turn my raw notes into a clean, skimmable summary.
[... role, guardrails and task order from the file ...]

--- NOTES START ---
budget call - Ahmed says dev costs up 15%, keep the June launch?
new laptop for design team, Shady to send quotes, follow up with supplier Sunday
--- NOTES END ---

CONTEXT
- Meeting purpose: June launch go/no-go
- Who will read this summary: my manager
```

**What comes back** (unedited shape of a real single-pass output — see the [full example](examples/work-meeting-notes-fix.md)):

```text
1. TL;DR: Dev costs are up 15% and the team must decide whether the June launch
   survives; purchasing and supplier follow-ups were assigned.
2. KEY DECISIONS: launch decision deferred pending revised budget …
3. ACTION ITEMS:  Task              | Owner | Deadline
                  Send quotes       | Shady | —
                  Supplier follow-up| you   | Sunday
4. OPEN QUESTIONS: …   5. FOLLOW-UP EMAIL: ready to send.
```

That's the whole experience: **no install, no login, no framework** — one file, one paste, structured output.

---

## 🎯 Fast-Track Solutions

Click your current bottleneck and grab the exact prompt built for it:

* 💥 **"My website or script crashed with an unexpected error"**  
  → [`debugging/website-error-fix`](prompts/debugging/website-error-fix.txt) (diagnoses system layer, isolates root cause, and provides regression tests)
* 🐙 **"Git history is messy and I need to rescue changes safely"**  
  → [`dev/git-rescue`](prompts/dev/git-rescue.txt) (step-by-step branch repair without data loss)
* 📝 **"Need to turn messy meeting notes into clear action items"**  
  → [`work/meeting-notes-fix`](prompts/work/meeting-notes-fix.txt) (produces an executive summary, key decisions, and an owner/deadline table)
* 📮 **"Manager asked for a status update and my notes are a mess"**  
  → [`work/status-update-email`](prompts/work/status-update-email.txt) (60-second update email with progress, risks, and next steps)
* 🔐 **"This code touches auth and payments — check it before I merge"**  
  → [`dev/security-review`](prompts/dev/security-review.txt) (prioritized findings, fixes with code, hardening wins)
* 🏛️ **"I need an official Egyptian document and have no idea where to start"**  
  → [`arabic-life/paperwork-guide`](prompts/arabic-life/paperwork-guide.txt) (documents, offices in order, common rejection mistakes — in Arabic)
* 💼 **"I have a LinkedIn post in my head but can't get it out"**  
  → [`content/linkedin-post`](prompts/content/linkedin-post.txt) (hooks, full post, first comment — English or Egyptian Arabic)
* 🎯 **"Tailoring a CV for a specific job description"**  
  → [`career/cv-reviewer`](prompts/career/cv-reviewer.txt) (line-by-line audit against target role requirements and ATS standards)
* 🌐 **"Converting formal Arabic copy into natural, fluent Egyptian dialect"**  
  → [`arabic-life/dialect-coach`](prompts/arabic-life/dialect-coach.txt) (natural spoken phrasing without awkward machine translations)
* 💸 **"Planning a realistic monthly budget and expense split"**  
  → [`daily/budget-split`](prompts/daily/budget-split.txt) (balanced allocation across necessities, savings, and discretionary spending)
* 🎣 **"Checking suspicious emails, messages, or links for scam indicators"**  
  → [`security-basics/phishing-spotter`](prompts/security-basics/phishing-spotter.txt) (identifies phishing red flags before opening links or attachments)

---

## 🌟 The Hall of Fame: Top 15 Staff Picks

Our most popular, high-utility prompts — start here if you're new:

| # | Prompt Name | What It Does | Grab File |
|:---:|---|---|:---:|
| 1 | **Meeting Notes Cleaner** | Messy thoughts → 3-line TL;DR + Action Items table | [`work/meeting-notes-fix`](prompts/work/meeting-notes-fix.txt) |
| 2 | **Commit Message Writer** | "Fixed bug" is dead. Write crisp conventional commits | [`dev/commit-message`](prompts/dev/commit-message.txt) |
| 3 | **Website Error Fixer** | Triage crashes, isolate system layer, get a regression test | [`debugging/website-error-fix`](prompts/debugging/website-error-fix.txt) |
| 4 | **CV Reviewer** | Ruthless audit against a target job description | [`career/cv-reviewer`](prompts/career/cv-reviewer.txt) |
| 5 | **Interview Prep Coach** | Mock interview roleplay with candid, constructive grading | [`career/interview-prep`](prompts/career/interview-prep.txt) |
| 6 | **Budget Splitter** | Stop month-end financial panic with realistic buckets | [`daily/budget-split`](prompts/daily/budget-split.txt) |
| 7 | **Weekly Meal Planner** | 7 dinners + consolidated grocery checklist on budget | [`daily/weekly-meal-planner`](prompts/daily/weekly-meal-planner.txt) |
| 8 | **Excel Formula Builder** | Describe your logic in plain words, get the exact formula | [`files-data/excel-formula`](prompts/files-data/excel-formula.txt) |
| 9 | **WhatsApp Broadcast Writer** | Customer messages that generate orders instead of mutes | [`marketing/whatsapp-broadcast`](prompts/marketing/whatsapp-broadcast.txt) |
| 10 | **Quotation Writer** | Professional price quotes with protective terms | [`business/quotation-writer`](prompts/business/quotation-writer.txt) |
| 11 | **Feature-to-Prompt Translator** | Turn your vague idea into precise specs an AI coder can build | [`ai-coding/feature-to-prompt`](prompts/ai-coding/feature-to-prompt.txt) |
| 12 | **Phishing Spotter** | Sanity-check weird SMS, emails, or links safely | [`security-basics/phishing-spotter`](prompts/security-basics/phishing-spotter.txt) |
| 13 | **Formal Arabic Email** | Professional Modern Standard Arabic correspondence for companies and universities | [`arabic-life/formal-arabic-email`](prompts/arabic-life/formal-arabic-email.txt) |
| 14 | **Egyptian Dialect Coach** | Authentic Egyptian spoken phrasing without awkward machine translation | [`arabic-life/dialect-coach`](prompts/arabic-life/dialect-coach.txt) |
| 15 | **Flashcard Maker** | Complex lecture notes → ready-to-use study flashcards | [`study/flashcards-maker`](prompts/study/flashcards-maker.txt) |

---

## 🎧 The 5 Power Hubs (Choose Your Workflow)

Instead of wandering through dozens of folders, jump straight to your track:

```text
                                  🗄️ PROMPT STASH (135 Prompts)
                                                │
   ┌─────────────────┬──────────────────────────┼─────────────────────────┬─────────────────┐
   │                 │                          │                         │                 │
┌──┴───────────┐  ┌──┴───────────────┐  ┌───────┴──────────┐  ┌───────────┴────────┐  ┌─────┴──────────────┐
│ 💻 Code & AI │  │ 💼 Work & Career │  │ 🏪 Biz & Growth  │  │ 🌐 Social & Culture│  │ 🧠 Life & Security │
│  (31 Files)  │  │    (21 Files)    │  │    (20 Files)    │  │    (23 Files)      │  │    (40 Files)      │
└──────────────┘  └──────────────────┘  └──────────────────┘  └────────────────────┘  └────────────────────┘
```

### 1. 💻 The Builder's Arsenal (Engineering, DevOps & AI Coding)
* 🤖 [**ai-coding**](prompts/ai-coding/README.md) `(10 prompts)` — Write bulletproof prompts for coding LLMs, generate unit tests, plan architecture, and refactor spaghetti code.
* 💻 [**dev**](prompts/dev/README.md) `(11 prompts)` — Git rescues, SQL tuning, Dockerfile repair, regex explanations, readable commit messages — and a security-focused code review.
* 🐞 [**debugging**](prompts/debugging/README.md) `(10 prompts)` — Systematic triage for website errors, blue screens, printer jams, battery drain, and Wi-Fi drops.

### 2. 💼 The Operator's Suite (Workplace & Career Acceleration)
* 💼 [**work**](prompts/work/README.md) `(11 prompts)` — Executive meeting summaries, status update emails, difficult reply tones, 1-on-1 agendas, and salary negotiation.
* 🎯 [**career**](prompts/career/README.md) `(10 prompts)` — ATS-friendly CV reviews, STAR-method interview roleplays, LinkedIn profile rewrites, and promotion proposals.

### 3. 🏪 The Growth Engine (Small Business & Marketing)
* 🏪 [**business**](prompts/business/README.md) `(10 prompts)` — Professional quotes, late-payment chasers, supplier requests, refund apologies, and contract summaries.
* 📣 [**marketing**](prompts/marketing/README.md) `(10 prompts)` — High-converting WhatsApp broadcasts, ad copy variants, customer personas, seasonal campaigns, and review requests.

### 4. 🌐 Regional & Cultural Communication (Social & Local Context)
* 🌐 [**arabic-life**](prompts/arabic-life/README.md) `(11 prompts)` — Real estate contracts, official paperwork and government procedures, formal administrative petitions, and academic correspondence.
* ✍️ [**content**](prompts/content/README.md) `(12 prompts)` — Short-form video scripts (Reels/TikTok), social and Instagram captions, LinkedIn posts, engagement hooks, and carousel frameworks.

### 5. 🧠 The Life OS (Daily Systems, Study & Digital Safety)
* 🌱 [**daily**](prompts/daily/README.md) `(10 prompts)` — 50/30/20 budget splitting, weekly meal prep on a budget, habit roadmaps, and packing checklists.
* 📚 [**study**](prompts/study/README.md) `(10 prompts)` — Feynman technique explanations, active-recall flashcard sets, exam cram guides, and lesson summaries.
* 🗃️ [**files-data**](prompts/files-data/README.md) `(10 prompts)` — Complex Excel/Sheets formulas, CSV data scrubbing, chart picking, and messy PDF data extraction.
* 🔐 [**security-basics**](prompts/security-basics/README.md) `(10 prompts)` — Phishing detection, 2FA backup checklists, public Wi-Fi safety, and password checkups.

---

## 🚀 Quick Start Guide

Using **Prompt Stash** requires zero setup or external dependencies:

1. **Choose a category:** Browse one of the 13 folders above according to your task.
2. **Open the `.txt` file:** Each prompt defines a specific role, sequential tasks, and placeholders marked as `{variable}`.
3. **Fill the variables:** Check the `# Variables` block at the bottom of the file for field descriptions and realistic format examples under `# Example values`.
4. **Copy and paste directly:** Works out-of-the-box with ChatGPT, Claude, Gemini, or any LLM, producing structured outputs (tables, steps, and summaries) without apologies or filler text.

---

## 🌍 Language Matrix

Every single file explicitly declares its language protocol on Line 3:

| Header Tag | What it means |
|---|---|
| `Language: prompt=EN \| output=EN` | English prompt, English output. |
| `Language: prompt=EN \| output=AR` | English prompt, Arabic output (Modern Standard Arabic or Egyptian dialect specified inside). |
| `Language: prompt=EN \| output=EN+AR` | Generates a dual-language side-by-side output. |
| `Language: prompt=EN \| output=user-choice` | Includes a `{language}` variable — you decide on the fly. |

---

## 🛠️ The Prompt Blueprint

Behind the scenes, every prompt adheres to a strict four-stage architectural contract (enforced automatically via [`scripts/validate_prompts.py`](scripts/validate_prompts.py)):

```text
Title
When to use it: <single punchy sentence>
Language: prompt=EN | output=EN
Tags: comma, separated, lowercase
<optional safety disclaimer for legal/financial/health/security>

<Body: Persona + Context + Strict Ordered Task List + Guardrails + Output Format>

# Variables
- {variable_name}: required/optional, plain English description
# Example values: {variable_name}=realistic copy-paste sample
```

* **Zero Fluff:** Bans empty compliments ("You are an amazing assistant").
* **Ordered Execution:** Enforces sequential steps so the AI doesn't skip logic.
* **Format Lockdown:** Specifies tables, word limits, and exact section headers.
* **Grounded Honesty:** Instructs the model to ask up to 3 clarifying questions if vital data is missing, rather than hallucinating assumptions.

---

## 🔎 Search & Examples

* **[Browser search page](docs/search.html)** — open `docs/search.html` (works offline, from a local clone, or on any static host): filter all 135 prompts by task, title, or tag — including Arabic.
* **[23 worked examples](examples/README.md)** — full inputs and raw, single-pass AI outputs, clearly labeled as illustrative. Arabic-heavy on purpose.

👉 **[Explore All 23 Worked Examples in `examples/` →](examples/README.md)**

---

## ⚠️ Grounded Reality & Limitations

* **Prompts are amplifiers, not magicians:** A great prompt gives you structure and focus; you still provide the facts and final review.
* **Model variation:** Responses vary across models and releases. Our [examples](examples/README.md) are unedited single-pass samples, not guarantees.
* **Not professional advice:** Health, legal, financial, and security prompts instruct the model on its boundaries and urge consultation with accredited experts.
* **Egypt-specific content ages:** Government procedures, fees, and portals change; paperwork prompts deliberately mark figures as "verify with the official source" — always do.
* **Fictional data in examples:** Any names, prices, or numbers in `# Example values` are purely illustrative placeholders.

---

## 🤝 Want to Add a Prompt?

Have a killer prompt that saves you hours? We love pull requests!  
Start with the [`good first issue` queue](https://github.com/Ziadtareks/prompt-stash/labels/good%20first%20issue) for ready-made starter tasks, check out [CONTRIBUTING.md](CONTRIBUTING.md) for the format guidelines, and run the local validator script before opening your PR. Questions that don't fit an issue? The [Discussions forum](https://github.com/Ziadtareks/prompt-stash/discussions) is open.

---

## 🙏 Credits

Created and maintained by **[Ziad Tarek](https://github.com/Ziadtareks)** — with gratitude to every contributor who sharpens a prompt, files a report, or adds a worked example. Every merged contribution lands in the [release notes](https://github.com/Ziadtareks/prompt-stash/releases) with credit.

## 📄 License

Licensed under the permissive [MIT License](LICENSE) — free for personal, commercial, and educational use.
