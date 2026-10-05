# Example — Interview Prep Coach (interactive)

Demonstration of [`prompts/career/interview-prep.txt`](../prompts/career/interview-prep.txt) with the variables filled in. This prompt is **turn-taking**: the AI asks one question, waits, then coaches. Below is the first exchange of a session. Illustrative example of what such a prompt **can** produce — **not guaranteed**.

## Prompt (filled)

> You are the interviewer for my upcoming interview. Run a realistic practice session: ask, wait for my answer, then give feedback and a stronger version — one question at a time.
>
> MY DETAILS
> - Role and company type I'm interviewing for: data analyst at a Cairo fintech
> - Interview stage and format: technical panel, 45 min
> - My background in 3 lines: 2 yrs reporting, SQL + Power BI, fintech-adjacent
> - What I'm most worried about: no degree in CS, explaining gaps
>
> YOUR TASK NOW: Start the session: confirm the setup in one line, then ask question 1.

## Example AI response — turn 1

> Setup confirmed: technical panel for a data-analyst role at a Cairo fintech, 45 minutes, and we'll drill your two worry areas along the way. One question at a time — answer like you would out loud.
>
> **Question 1 of 5:**
> "Walk me through a report or dashboard you built that changed a decision — not just what it showed, but what someone did because of it."

## Example user answer

> I built a Power BI dashboard for the finance team showing monthly collections by customer segment. They used to compile it in Excel manually. After the dashboard, the collections manager started doing weekly reviews and focused on the two segments that were behind.

## Example AI response — feedback on turn 1

> **Score: 6/10.**
>
> **What worked:** you led with the tool and the concrete object (dashboard, segments, weekly cadence) — a real project, not a textbook answer.
>
> **The missing piece:** "they started doing weekly reviews" is an activity, not an outcome. A fintech panel wants the decision's effect: did overdue amounts drop? By how much? Who exactly changed what? You gave me the *what* twice but no *so what*.
>
> **Model answer skeleton** (fill with your real numbers):
> - Situation: collections reporting was monthly, manual, and late — decisions lagged a cycle. [FILL: how late / how long a compile?]
> - Action: built a self-serve Power BI dashboard with collections by segment and aging buckets — mention one technical choice you're proud of (a DAX measure, a refresh pipeline).
> - Result: collections manager moved to weekly segment reviews and prioritized the 2 weakest segments; [FILL: measurable effect — e.g. "overdue 60+ days dropped ~X% in Y months" or, if you don't have the number, "the manager told me it cut their prep time from days to hours"].
>
> A useful habit: end every project story with one number or one quoted reaction. If the number doesn't exist, say why — "we didn't measure it, but here's the closest signal" is still a strong answer.
>
> **Question 2 of 5:** "You mention SQL on your CV. Tell me about the most complex query you've written — what made it complex?"

*(The session continues one question at a time; after question 5 it re-asks your two weakest answers in different wording, then closes with your STAR stories, defusals for the no-CS-degree and gap worries, and 3 questions for you to ask the panel.)*

---
*Generated for demonstration as part of Prompt Stash. Outputs vary by model and run.*
