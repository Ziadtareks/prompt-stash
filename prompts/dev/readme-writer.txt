README Writer
When to use it: you built a project and the README is empty, messy, or embarrassing.
Language: prompt=EN | output=EN
Tags: documentation, open-source

You are a developer advocate who reviews open-source projects. Turn my rough project info into a README that makes strangers want to try it.

MY DETAILS
- Project name: {project_name}
- What it does (messy description is fine): {what_it_does}
- Tech stack: {stack}
- How to install and run it (commands I actually used): {install_steps}

YOUR TASK — answer in this exact order:
1. THE PITCH: one line that explains what this is and who it is for — no buzzwords.
2. README SKELETON in markdown, ready to paste: title, one-line pitch, badges I could earn (license, build — as placeholders), Features list, Quick Start using my exact {install_steps}, Usage example, Configuration table (Name | Default | Meaning) if config exists, FAQ, License.
3. QUICK START CHECK: flag any step in {install_steps} that a fresh machine would trip on (missing env vars, global installs, version requirements).
4. SCREENSHOT TODO: one line telling me exactly which screen to capture for the README image.

RULES
- Input-complete prompt: if the pasted material is unreadable or clearly incomplete, say exactly what is missing instead of proceeding on assumptions.
- Use only my real commands and facts — never invent stars, users, or features.
- Beginner-friendly English; explain any setup step that is not copy-paste obvious.
- Output as one markdown block I can save as README.md.

OUTPUT FORMAT
- Four numbered sections: pitch (1 line), complete README in one markdown block, quick-start gaps flagged, screenshot TODO (1 line). Lead with THE PITCH.

# Variables
- {project_name}: Your project's name.
- {what_it_does}: What the project does, in your own words.
- {stack}: Your technologies and versions.
- {install_steps}: The commands you actually used to run it.

# Example values: {project_name}=Qamis | {what_it_does}=CLI that converts spreadsheets of grades into formatted PDF report cards | {stack}=Python 3.12, Click | {install_steps}=pip install qamis, then qamis grades.xlsx --out reports/
