#!/usr/bin/env python3
"""One-shot Phase 1+2 migration: apply the strict format to all prompt files.
Deletes nothing; keeps bodies copy-paste friendly. Run once, then commit."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"

# ── Hand-authored metadata: stem -> (output_lang, tags) ──────────────────────
LANG_TAGS = {
    # debugging (EN)
    "website-error-fix": ("EN", "debugging, web, errors, beginner"),
    "bsod-explain": ("EN", "windows, hardware, troubleshooting"),
    "deploy-rollback": ("EN", "devops, deployment, incident-response"),
    "slow-pc-fix": ("EN", "windows, performance, troubleshooting"),
    "wifi-drop-fix": ("EN", "networking, troubleshooting, home"),
    "printer-fix": ("EN", "hardware, troubleshooting"),
    "phone-storage-fix": ("EN", "android, iphone, storage"),
    "battery-drain-fix": ("EN", "batteries, hardware, troubleshooting"),
    "overheating-fix": ("EN", "hardware, laptops, troubleshooting"),
    "email-bounce-fix": ("EN", "email, deliverability, troubleshooting"),
    # work (EN)
    "meeting-notes-fix": ("EN", "meetings, productivity, summary"),
    "reply-tone": ("EN", "email, communication, rewriting"),
    "cv-bullets": ("EN", "resume, career, writing"),
    "one-on-one-prep": ("EN", "management, career, meetings"),
    "salary-negotiation-email": ("EN", "salary, negotiation, career"),
    "out-of-office-writer": ("EN", "email, leave, communication"),
    "presentation-outline": ("EN", "presentations, communication"),
    "meeting-agenda": ("EN", "meetings, facilitation"),
    "jargon-simplifier": ("EN", "communication, technical-writing"),
    "task-priority-sort": ("EN", "productivity, prioritization"),
    # content
    "captions-ar": ("AR", "arabic, social-media, captions"),
    "hashtags": ("EN", "social-media, hashtags, discovery"),
    "bio-maker": ("EN", "social-media, branding, profile"),
    "video-script-short": ("user-choice", "video, scriptwriting, short-form"),
    "post-hooks": ("user-choice", "copywriting, hooks, social-media"),
    "content-calendar": ("EN", "content-strategy, planning, social-media"),
    "carousel-outline": ("EN", "social-media, content, design"),
    "product-description": ("EN+AR", "ecommerce, copywriting"),
    "newsletter-intro": ("user-choice", "email, newsletters, copywriting"),
    "comment-reply": ("user-choice", "community, social-media, engagement"),
    # study
    "summarize-lesson": ("EN", "studying, notes, summarizing"),
    "flashcards-maker": ("user-choice", "studying, flashcards, memory"),
    "exam-revision": ("EN", "studying, planning, exams"),
    "translate-term": ("EN+AR", "arabic, translation, vocabulary"),
    "essay-outline": ("EN", "writing, academic, outlines"),
    "practice-quiz": ("EN", "studying, quizzes, self-testing"),
    "feynman-explain": ("EN", "studying, understanding, tutoring"),
    "formula-explainer": ("EN", "math, science, learning"),
    "homework-hint": ("EN", "studying, tutoring, homework"),
    "mistake-log-analyzer": ("EN", "studying, exams, improvement"),
    # business
    "store-reply": ("user-choice", "customer-service, ecommerce"),
    "invoice-words": ("EN", "invoicing, freelance, payment"),
    "price-calc-explain": ("EN", "pricing, negotiation, sales"),
    "booking-confirm": ("EN", "customer-service, bookings"),
    "refund-apology": ("EN", "customer-service, refunds"),
    "quotation-writer": ("EN", "proposals, pricing, freelance"),
    "contract-summary": ("EN", "contracts, legal, review"),
    "supplier-email": ("EN", "procurement, negotiation, b2b"),
    "late-payment-chaser": ("EN", "payments, collections, freelance"),
    "idea-check": ("EN", "entrepreneurship, validation, market-research"),
    # dev (EN)
    "readme-writer": ("EN", "documentation, open-source"),
    "commit-message": ("EN", "git, conventions"),
    "regex-explain": ("EN", "regex, learning"),
    "sql-fix": ("EN", "sql, databases, debugging"),
    "api-error": ("EN", "apis, debugging"),
    "git-rescue": ("EN", "git, recovery"),
    "log-analyzer": ("EN", "logging, debugging, incident-response"),
    "code-reviewer": ("EN", "code-review, quality, security"),
    "env-setup-debug": ("EN", "environment, debugging, setup"),
    "dockerfile-fix": ("EN", "docker, devops, containers"),
    # daily (EN)
    "habit-plan": ("EN", "habits, behavior, productivity"),
    "budget-split": ("EN", "budgeting, personal-finance"),
    "trip-pack-list": ("EN", "travel, checklists"),
    "workout-plan": ("EN", "fitness, exercise, beginners"),
    "sleep-routine": ("EN", "sleep, health, routines"),
    # ai-coding (EN)
    "feature-to-prompt": ("EN", "prompt-engineering, coding, ai"),
    "code-explainer": ("EN", "code-reading, learning"),
    "refactor-request": ("EN", "refactoring, code-quality"),
    "test-writer": ("EN", "testing, quality"),
    "bug-repro-steps": ("EN", "debugging, qa"),
    "library-picker": ("EN", "dependencies, architecture, decision-making"),
    "migrate-code": ("EN", "migration, refactoring"),
    "performance-fix": ("EN", "performance, optimization"),
    "prompt-improver": ("EN", "prompt-engineering, meta"),
    "architecture-suggest": ("EN", "architecture, system-design"),
    # career
    "cv-reviewer": ("EN", "resume, career, job-search"),
    "cover-letter-writer": ("user-choice", "cover-letters, job-search"),
    "linkedin-profile-fix": ("user-choice", "linkedin, personal-branding"),
    "interview-prep": ("EN", "interviews, career, practice"),
    "star-story-builder": ("EN", "interviews, behavioral, storytelling"),
    "career-switch-plan": ("EN", "career-change, planning"),
    "freelance-profile": ("user-choice", "freelancing, platforms, profile"),
    "promotion-case": ("EN", "promotion, career, negotiation"),
    "rejection-reply": ("EN", "job-search, communication"),
    "skills-gap-map": ("EN", "skills, career, learning"),
    # marketing
    "ad-copy-writer": ("user-choice", "advertising, copywriting, paid-media"),
    "email-sequence": ("user-choice", "email-marketing, automation"),
    "discount-offer": ("EN", "promotions, pricing, retail"),
    "customer-persona": ("EN", "research, positioning, marketing"),
    "competitor-teardown": ("EN", "competitive-analysis, strategy"),
    "landing-copy": ("EN+AR", "landing-pages, conversion, copywriting"),
    "whatsapp-broadcast": ("user-choice", "whatsapp, local-marketing"),
    "review-request": ("user-choice", "reviews, reputation, local-business"),
    "referral-offer": ("EN", "referrals, growth, loyalty"),
    "seasonal-campaign": ("EN", "campaigns, seasonal, retail"),
    # files-data
    "excel-formula": ("EN", "excel, sheets, formulas"),
    "csv-cleaner": ("EN", "data-cleaning, spreadsheets"),
    "data-summarizer": ("EN", "analysis, reporting"),
    "file-organizer": ("EN", "organization, files, workflow"),
    "pdf-extract": ("EN", "pdf, data-extraction"),
    "sql-from-question": ("EN", "sql, databases, analytics"),
    "chart-picker": ("EN", "visualization, data, design"),
    "duplicate-finder": ("EN", "data-quality, reconciliation"),
    "report-skeleton": ("EN", "reporting, business"),
    "naming-convention": ("EN", "naming, organization, teams"),
    # security-basics (EN)
    "password-checkup": ("EN", "passwords, managers, security"),
    "phishing-spotter": ("EN", "phishing, scams, email-security"),
    "2fa-setup-guide": ("EN", "2fa, accounts, security"),
    "scam-check": ("EN", "scams, marketplace, fraud"),
    "breach-response": ("EN", "breaches, incident-response"),
    "public-wifi-safety": ("EN", "wifi, privacy, networks"),
    "device-loss-plan": ("EN", "lost-device, phones, recovery"),
    "backup-plan": ("EN", "backup, data-protection"),
    "privacy-audit": ("EN", "privacy, social-media, footprint"),
    "safe-downloads": ("EN", "malware, downloads, software"),
    # arabic-life
    "formal-arabic-email": ("AR", "arabic, email, formal-writing"),
    "complaint-letter-eg": ("EN+AR", "arabic, consumer-rights, complaints"),
    "occasion-messages": ("AR", "arabic, social, occasions"),
    "rental-contract-explain": ("AR", "arabic, rental, contracts"),
    "arabic-speech-notes": ("AR", "arabic, speeches, occasions"),
    "school-note-writer": ("AR", "arabic, school, parents"),
    "dialect-coach": ("AR", "egyptian-arabic, dialect, localization"),
    "arabic-job-application": ("EN+AR", "arabic, job-search, applications"),
    "legal-terms-explain": ("EN+AR", "arabic, paperwork, egypt"),
    "announcement-maker": ("AR", "arabic, announcements, community"),
}

# ── Example-values lines for the 29 v1/v2 files that lack one ────────────────
EXAMPLES = {
    "website-error-fix": "{what_i_was_doing}=opening my site after editing a page | {stack}=WordPress on shared hosting | {error_message}=Error establishing a database connection | {yes_no_and_when}=worked fine yesterday | {what_i_tried}=refreshed, restarted hosting",
    "bsod-explain": "{stop_code}=CRITICAL_PROCESS_DIED | {when_it_happens}=random, 2-3 times a day | {recent_changes}=Windows update last week | {pc_type}=4-year-old desktop",
    "deploy-rollback": "{platform}=Vercel | {what_changed}=bumped a payment library to the latest major version | {symptom}=checkout returns 500 for card payments | {deploy_method}=GitHub integration, auto-deploy on push | {time_since_deploy}=25 minutes",
    "meeting-notes-fix": "{paste_notes}=budget call - Ahmed says dev costs up 15%, keep the June launch? new laptop for design team, Shady to send quotes, follow up with supplier Sunday | {meeting_purpose}=June launch go/no-go | {audience}=my manager",
    "reply-tone": "{recipient}=a client who delayed the project 3 weeks | {desired_tone}=firm but professional | {goal}=get written approval of the new timeline without losing them | {length_limit}=under 120 words | {draft_reply}=Honestly this is getting unprofessional, third delay, please confirm dates in writing today.",
    "cv-bullets": "{role}=accountant | {target_job}=FP&A analyst | {number_of_bullets}=5 | {raw_duties}=did monthly closing, made reports in excel, boss liked my dashboards, trained a new guy",
    "captions-ar": "{platform}=Instagram | {topic}=خزانة ملابس شتوية وصلت حديثًا | {audience}=بنات جامعة | {tone}=مرح | {call_to_action}=اطلبي من اللينك في البايو",
    "hashtags": "{platform}=Instagram | {topic}=handmade silver rings | {niche}=handmade jewelry | {audience}=women 20-35 in Egypt and the Gulf | {language}=Arabic + English | {number_of_hashtags}=20",
    "bio-maker": "{platform}=Instagram | {who_i_am}=freelance photographer | {content_topics}=portraits, Cairo streets, behind-the-scenes | {target_audience}=brands and couples planning shoots | {unique_angle}=same-day preview gallery | {link_purpose}=booking form",
    "summarize-lesson": "{subject}=high school biology | {exam_focus}=cell division | {paste_lesson}=45 minutes of lecture about mitosis and meiosis phases | (lesson text pasted)",
    "flashcards-maker": "{number_of_cards}=15 | {language}=English | {paste_material}=chapter 4 notes on the French Revolution",
    "exam-revision": "{exam_date}=June 20 | {days_available}=10 | {hours_per_day}=2 | {topics_list}=kinematics easy, dynamics hard, energy medium, momentum hard",
    "translate-term": "{term}=opportunity cost | {subject}=economics | {level}=university first year",
    "essay-outline": "{essay_question}=Does social media do more harm than good to teenagers? | {word_count}=1000 | {academic_level}=high school senior | {key_sources}=class readings on attention and mental health",
    "store-reply": "{store_name}=Nour Home | {customer_message}=ordered a lamp 3 weeks ago, nothing arrived, nobody answers | {resolution}=resend with express shipping + 10% coupon | {reply_language}=Arabic",
    "invoice-words": "{your_business}=Sara Design Studio | {client_name}=Cafe Rivea | {items_list}=logo design, 3 social media templates | {currency}=EGP | {due_days}=14",
    "price-calc-explain": "{service}=brand identity package | {price}=18,000 EGP | {what_included}=logo system, color palette, 20-page brand guide, 2 revision rounds | {competitor_price}=8,000-30,000 EGP range",
    "booking-confirm": "{business_type}=dental clinic | {customer_name}=Mona Adel | {date_time}=Tuesday March 4, 5:30 PM | {location_or_link}=Zamalek branch, 2nd floor | {cancellation_policy}=free reschedule up to 24h before",
    "refund-apology": "{customer_name}=Khaled | {what_went_wrong}=wrong size shipped twice | {refund_amount}=1,200 EGP to the original card | {store_name}=Metro Wear",
    "readme-writer": "{project_name}=Qamis | {what_it_does}=CLI that converts spreadsheets of grades into formatted PDF report cards | {stack}=Python 3.12, Click | {install_steps}=pip install qamis, then qamis grades.xlsx --out reports/",
    "commit-message": "{changes_summary_or_diff}=moved email sending into a background queue, added retry with backoff | {commit_type}=refactor",
    "regex-explain": "{regex_pattern}=^\\+?20)?1[0125]\\d{8}$ | {sample_text}=01012345678, +201012345678, 01198765432, 12345",
    "sql-fix": "{sql_query}=SELECT * FROM orders WHERE customer_id IN (SELECT id FROM customers WHERE city = 'Cairo') AND total > 1000 | {what_is_wrong}=returns orders twice for some customers | {table_schemas}=orders(id, customer_id, total, status), customers(id, name, city)",
    "api-error": "{method_and_endpoint}=POST /v1/orders | {status_code}=422 | {response_body}={\"error\":\"invalid_currency\"} | {request_you_sent}=body had currency: \"EGP \" with a trailing space",
    "habit-plan": "{habit}=read 20 pages a day | {current_routine}=wake 7, work 9-5, dinner 8, scroll until midnight | {obstacle}=too tired after dinner",
    "budget-split": "{monthly_income}=15,000 EGP | {fixed_costs}=rent 6,000, utilities 1,200, transport 1,000, internet 500 | {savings_goal}=20,000 EGP emergency fund | {currency}=EGP",
    "trip-pack-list": "{destination}=Dahab | {days}=4 | {weather}=hot days, cool nights | {trip_type}=beach + light hiking",
    "workout-plan": "{days_per_week}=3 | {minutes_per_session}=30 | {fitness_level}=never trained | {goal}=feel better and lose weight",
    "sleep-routine": "{wake_up_time}=6:30 AM | {bedtime_now}=1:30 AM | {main_disruptor}=phone in bed",
}

# ── Phase 2: safety notes — rel-path stem -> (disclaimer under line 4, Note in body)
NOTE_LEGAL = ("Note: You are not a lawyer — say so plainly whenever legal topics come up, flag the points a licensed professional should review, and never state that a clause or position is definitely valid or invalid.")
NOTE_FIN = ("Note: Promise no guaranteed outcomes — state your assumptions explicitly and include one line noting these are planning estimates, not financial advice.")
NOTE_HEALTH = ("Note: This is general guidance, not medical advice — tell me to consult a doctor before starting if I mention pain, a health condition, pregnancy, or medication.")
NOTE_SEC = ("Note: Never ask for or accept real passwords, recovery codes, card numbers, or OTP codes — if I paste one, tell me to rotate it immediately and continue using placeholders.")
NOTE_DATA = ("Note: Before I paste anything, remind me to redact or mask personal and client data (names, phone numbers, account numbers, tokens) and replace them with placeholders.")

SAFETY = {
    "contract-summary": ("⚠️ Educational guidance — not legal advice.", NOTE_LEGAL),
    "rental-contract-explain": ("⚠️ Educational guidance — not legal advice.", NOTE_LEGAL),
    "legal-terms-explain": ("⚠️ Educational guidance — not legal advice.", NOTE_LEGAL),
    "complaint-letter-eg": ("⚠️ Educational guidance — not legal advice.", NOTE_LEGAL),
    "salary-negotiation-email": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "invoice-words": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "price-calc-explain": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "quotation-writer": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "late-payment-chaser": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "idea-check": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "budget-split": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "discount-offer": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "referral-offer": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "seasonal-campaign": ("ℹ️ Planning guidance with stated assumptions — not financial advice.", NOTE_FIN),
    "workout-plan": ("⚠️ General wellness guidance — not medical advice.", NOTE_HEALTH),
    "sleep-routine": ("⚠️ General wellness guidance — not medical advice.", NOTE_HEALTH),
    "password-checkup": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "phishing-spotter": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "2fa-setup-guide": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "scam-check": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "breach-response": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "public-wifi-safety": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "device-loss-plan": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "backup-plan": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "privacy-audit": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "safe-downloads": ("🔒 Safety guidance — never share real passwords, codes, or card numbers.", NOTE_SEC),
    "meeting-notes-fix": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "store-reply": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "reply-tone": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "comment-reply": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "csv-cleaner": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "data-summarizer": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "pdf-extract": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "duplicate-finder": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
    "log-analyzer": ("🔒 Privacy reminder — redact secrets and tokens before pasting.", NOTE_DATA),
    "code-reviewer": ("🔒 Privacy reminder — redact secrets and tokens before pasting.", NOTE_DATA),
    "bug-repro-steps": ("🔒 Privacy reminder — redact secrets and tokens before pasting.", NOTE_DATA),
    "customer-persona": ("🔒 Privacy reminder — redact personal or client data before pasting.", NOTE_DATA),
}

# ── Curated explanations for the most common variables; long tail falls back
VAR_COMMON = {
    "topic": "What the post, question, or session is about.",
    "platform": "Where this will be published or used (Instagram, X, TikTok, LinkedIn…).",
    "audience": "Who will read or receive this.",
    "tone": "The voice to write in.",
    "language": "Language (and dialect) for the output.",
    "languages": "Language(s) to write or reply in.",
    "goal": "The outcome you want from this.",
    "stack": "Your technologies and versions.",
    "error_message": "The exact error text you received.",
    "what_i_tried": "What you already attempted, so it is not repeated.",
    "recipient": "Who this message is for and your relationship to them.",
    "draft_reply": "Your current draft, pasted as-is.",
    "desired_tone": "How the message should land.",
    "length_limit": "Maximum length for the output.",
    "role": "Your current job title or position.",
    "target_job": "The job or role you are aiming for.",
    "number_of_bullets": "How many items to produce.",
    "raw_duties": "Your unpolished list of tasks and achievements.",
    "subject": "The subject or field this belongs to.",
    "level": "Your level (school, university, professional).",
    "currency": "The currency for all money figures (e.g. EGP).",
    "my_role": "Your role in this situation.",
    "client_name": "The client's (or counterparty's) name.",
    "question": "Your question in plain words.",
    "paste_notes": "Your raw notes, pasted between the markers.",
    "paste_lesson": "Your lesson transcript or notes, pasted between the markers.",
    "paste_material": "Your study material, pasted between the markers.",
    "paste_code": "Your code, pasted between the markers.",
    "paste_log": "Your log output, pasted between the markers.",
    "paste_data": "Your data table, pasted between the markers.",
    "paste_contract": "The contract text, pasted between the markers.",
    "paste_pdf_text": "The PDF's copied text, pasted between the markers.",
    "meeting_purpose": "Why the meeting happened.",
    "exam_date": "The date of your exam.",
    "destination": "Where you are traveling.",
    "habit": "The habit you want to build.",
    "obstacle": "What stopped you last time.",
    "project_name": "Your project's name.",
    "what_it_does": "What the project does, in your own words.",
    "install_steps": "The commands you actually used to run it.",
    "commit_type": "The type of change you think it is (feat, fix…).",
    "regex_pattern": "The regular expression to explain.",
    "sample_text": "Sample text the regex runs against.",
    "sql_query": "Your current SQL query.",
    "table_schemas": "Your tables and columns.",
    "symptom": "What is visibly broken.",
    "status_code": "The HTTP status code returned.",
    "main_disruptor": "What hurts your sleep most.",
    "niche": "Your niche or industry.",
    "call_to_action": "The action you want the reader to take.",
}

CLARIFY = "- If critical information is missing, ask up to 3 clarifying questions first; otherwise proceed with clearly-stated assumptions."

SPECIAL = [
    ("study/feynman-explain.txt", "HOW THIS WORKS", "YOUR TASK — run this coaching session in this exact order"),
    ("arabic-life/rental-contract-explain.txt", "الخطرعة", "الخطيرة"),
    ("arabic-life/legal-terms-explain.txt", "contrat مسجل", "عقد مسجل"),
]


def humanize(name: str) -> str:
    return name.replace("_", " ")


def explain(name: str) -> str:
    if name in VAR_COMMON:
        return VAR_COMMON[name]
    return f"The {humanize(name)} for this prompt — see Example values for a realistic fill."


def var_explanation(name: str) -> str:
    return f"- {{{name}}}: {explain(name)}"


migrated, problems = 0, []
for f in sorted(PROMPTS.glob("*/*.txt")):
    rel = f.relative_to(PROMPTS).as_posix()
    stem = f.stem
    if stem not in LANG_TAGS:
        problems.append(f"{rel}: no LANG_TAGS entry — skipped")
        continue
    output, tags = LANG_TAGS[stem]
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()

    title = lines[0].strip()
    when = lines[1].strip()
    if when.startswith("When to use:"):
        when = "When to use it:" + when[len("When to use:"):]
    elif not when.startswith("When to use it:"):
        problems.append(f"{rel}: line 2 not a when-to-use line")
        when = "When to use it: " + when

    body = lines[2:]
    # pull out existing example-values line
    example_line = None
    kept = []
    for l in body:
        if l.startswith("# Example values:"):
            example_line = l.strip()
        else:
            kept.append(l)
    if example_line is None:
        if stem in EXAMPLES:
            example_line = "# Example values: " + EXAMPLES[stem]
        else:
            problems.append(f"{rel}: no example values produced")
            example_line = "# Example values: (fill every variable with a realistic value)"
    body = kept
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()

    # special-case fixes
    for path_frag, old, new in SPECIAL:
        if rel == path_frag:
            body = [l.replace(old, new) for l in body]

    # clarifying-questions rule
    if not any("3 clarifying questions" in l for l in body):
        inserted = False
        for i, l in enumerate(body):
            if l.strip().upper().endswith("RULES") and i + 1 < len(body):
                body.insert(i + 1, CLARIFY)
                inserted = True
                break
        if not inserted:
            body += ["", "RULES", CLARIFY]

    # safety note inside body
    if stem in SAFETY:
        body += [SAFETY[stem][1]]

    # variables block from body
    var_names = []
    seen = set()
    for l in body:
        for m in re.findall(r"\{([A-Za-z0-9_ -]+)\}", l):
            m = m.strip()
            if m not in seen:
                seen.add(m)
                var_names.append(m)
    var_block = ["# Variables"] + [var_explanation(v) for v in var_names]

    out = [title, when, f"Language: prompt=EN | output={output}", f"Tags: {tags}"]
    if stem in SAFETY:
        out.append(SAFETY[stem][0])
    out.append("")
    out += body
    out.append("")
    out += var_block
    out.append("")
    out.append(example_line)
    f.write_text("\n".join(out) + "\n", encoding="utf-8")
    migrated += 1

print(f"migrated={migrated}")
for p in problems:
    print("PROBLEM:", p)
