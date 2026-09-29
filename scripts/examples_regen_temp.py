#!/usr/bin/env python3
"""Task 7: regenerate example files so their filled prompt matches the current
prompt body exactly. Also refreshes the label wording. One-shot."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / "examples"

FILLS = {
 "work-meeting-notes-fix": {
  "paste_notes": "june launch call — ahmed says dev costs up 15% vs plan, asked if we still launch june 22. sara: packaging sample #2 looks good, needs final approve. me: told them we decide friday. new laptop for design (sara asked). shady to get 3 quotes. TOLD everyone i'll send recap. also supplier said shipping up? check. mariam wants 2 days off mid june",
  "meeting_purpose": "June launch go/no-go", "audience": "my manager"},
 "debugging-website-error-fix": {
  "what_i_was_doing": "opening my blog after editing a post", "stack": "WordPress on shared hosting",
  "error_message": '"Error establishing a database connection"', "yes_no_and_when": "worked fine yesterday",
  "what_i_tried": "refreshed the page, restarted from the hosting panel"},
 "dev-commit-message": {
  "changes_summary_or_diff": "I added a `discount_code` column to the orders table, passed it through the checkout API, and applied it in the total calculation. Also updated the checkout tests.",
  "commit_type": "feat"},
 "dev-code-reviewer": {
  "language": "Python (FastAPI)", "purpose": "endpoint that returns a user's saved addresses",
  "main_worry": "security of user input",
  "paste_code": '```python\n@app.get("/addresses")\ndef get_addresses(user_id: int):\n    rows = db.execute(f"SELECT * FROM addresses WHERE user_id = {user_id}")\n    return [dict(r) for r in rows]\n```'},
 "ai-coding-feature-to-prompt": {
  "feature_idea": "users can save posts to read later", "stack": "Next.js 15, Supabase, Tailwind",
  "codebase_patterns": "server actions + optimistic UI pattern",
  "definition_of_done": "works logged-in only, undo toast, empty state"},
 "career-cv-reviewer": {
  "job_requirements": "Data analyst: SQL, Power BI, stakeholder reporting, 3+ years experience",
  "field_and_level": "finance graduate, 2 years reporting", "application_stats": "40 applications, 1 interview",
  "paste_cv": "Omar Khaled — hardworking finance professional seeking growth opportunities.\nExperience: Al-Nour Trading Co., Accountant (2024–present): responsible for accounting tasks, monthly reports, and helping with audits. Eshta Trading, Junior Accountant (2023–2024): data entry, invoices, assisting senior accountants.\nSkills: Excel, Power BI, communication, teamwork.\nEducation: BCom Accounting, Cairo University."},
 "study-flashcards-maker": {
  "number_of_cards": "10", "language": "English",
  "paste_material": "Photosynthesis: plants convert light energy into chemical energy (glucose) using carbon dioxide and water, releasing oxygen. Happens in the chloroplast, using the pigment chlorophyll. Two stages: light-dependent reactions (in the thylakoid, need light, produce ATP and NADPH, split water) and the Calvin cycle (in the stroma, no light needed, uses ATP + NADPH to turn CO2 into glucose). Limiting factors: light intensity, CO2 concentration, temperature."},
 "business-quotation-writer": {
  "my_business": "Nour Designs — hello@nourdesigns.example, Instagram @nourdesigns.example",
  "client_and_request": "Cafe Rivea — logo + menu design + 5 social media posts",
  "items_and_prices": "logo 6,000; menu 3,500; posts 750 each", "payment_terms": "50% deposit", "valid_days": "14"},
 "marketing-whatsapp-broadcast": {
  "business_and_news": "Sweet Meter — winter menu launched (6 new desserts)",
  "recipients": "past buyers on my broadcast list", "action": "reply to pre-order for next weekend",
  "offer_and_deadline": "first 30 orders get a free mini cheesecake; closes Thursday",
  "language_and_tone": "Egyptian Arabic, friendly"},
 "files-data-excel-formula": {
  "tool": "Excel 365", "goal": "total sales per salesperson per month with a dropdown picker",
  "sheet_layout": "A: date, B: salesperson, C: amount, D: region (data on sheet \"Sales\", summary on sheet \"Summary\")",
  "edge_cases": "some amounts blank, names with extra spaces"},
 "arabic-life-formal-arabic-email": {
  "recipient_type": "university admissions office", "purpose": "request an extension of enrollment deadline",
  "key_facts": "student ID 20210435, semester starts Sep 14, I travel Sep 20",
  "relationship": "admitted student", "attachments": "passport copy, payment receipt"},
 "arabic-life-occasion-messages": {
  "occasion": "graduation with honors", "recipient": "my manager's daughter (I was invited to the party)",
  "personal_details": "the graduate is Salma, engineering faculty, first in class",
  "channel": "WhatsApp to the manager", "dialect": "formal-leaning Egyptian"},
 "arabic-life-dialect-coach": {
  "formal_text": "يسعدنا أن نعلن عن وصول منتجاتنا الجديدة إلى جميع الفروع، وتفضلوا بزيارتنا لتجربتها",
  "context": "Instagram reel voiceover for a bakery", "audience": "Cairo general, 20–40",
  "formality": "polished but friendly"},
}

LABEL_OLD = re.compile(r"The response below was generated.*?fictional[^\n]*")
LABEL_NEW = ("Illustrative example of what such a prompt **can** produce. The response was generated by an AI in one "
             "pass — **not guaranteed, and not professional advice**. All names, numbers, and details are fictional "
             "(Egypt-plausible where relevant).")

for md in sorted(EX.glob("*.md")):
    stem = md.stem
    if stem == "README":
        continue
    fills = FILLS.get(stem)
    if fills is None:
        print(f"NO FILLS: {stem}")
        continue
    prompt_path = None
    name = stem.split("-", 1)[1]
    for folder in (ROOT / "prompts").iterdir():
        cand = folder / (name + ".txt")
        if cand.exists():
            prompt_path = cand
            break
        cand = folder / (name.split("-", 1)[1] + ".txt")
        if cand.exists():
            prompt_path = cand
            break
    if prompt_path is None:
        print(f"NO PROMPT FILE: {stem}")
        continue
    text = prompt_path.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(text) if not l.strip()) + 1
    if text[4].startswith(("⚠", "ℹ", "🔒")):
        start = 5
    idx = next(i for i, l in enumerate(text) if l.strip() == "# Variables")
    body = text[start:idx]
    filled = []
    for l in body:
        for k, v in fills.items():
            l = l.replace("{" + k + "}", v)
        filled.append("> " + l if l.strip() else ">")
    block = "## Prompt (filled)\n\n" + "\n".join(filled) + "\n\n## Example AI response"

    md_text = md.read_text(encoding="utf-8")
    md_text = LABEL_OLD.sub(LABEL_NEW, md_text)
    md_text = re.sub(r"## Prompt \(filled\)\n\n.*?\n\n## Example AI response",
                     block.replace("\\", "\\\\"), md_text, flags=re.S)
    md.write_text(md_text, encoding="utf-8")
    print("regenerated", md.name)
