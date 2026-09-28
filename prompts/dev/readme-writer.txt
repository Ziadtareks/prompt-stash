README Writer
When to use: you built a project and the README is empty, messy, or embarrassing.

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
- Use only my real commands and facts — never invent stars, users, or features.
- Beginner-friendly English; explain any setup step that is not copy-paste obvious.
- Output as one markdown block I can save as README.md.
