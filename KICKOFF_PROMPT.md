# Paste this as your first message to Claude Code

You're working in the `gtm-looper` repo (now on GitHub, public). Read `CLAUDE.md`
and `BUILD_PLAN.md` before doing anything.

First, confirm Phase 0's acceptance still holds: run the privacy sweep (grep the tree
for client names, emails, secret-shaped strings, private URLs — the only intended
personal reference is the michaeltaus.com link) and confirm `python
scripts/publish_to_ghost.py posts/2026-06-11-write-loops-not-prompts.md --dry-run`
renders. Then complete the build by working `BUILD_PLAN.md` Phases 1→6 in order.

For each phase: do the tasks, run the acceptance checks, commit with a clear
`feat(phaseN): …` message, and push. Stop and ask me at every ⛔ human checkpoint —
anything involving secrets, OAuth, or publishing live. I'll add Ghost credentials to
`.env` myself. Never put secrets in files or commits, and never publish or post on my
behalf without my explicit go-ahead.

After each phase, report 3 lines: what you did · acceptance result · what's next.

Begin with Phase 1 (verify the Ghost publish path) and tell me exactly what you need
from me to complete it.
