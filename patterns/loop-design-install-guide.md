# Installing the `loop-design` skill across Claude surfaces

You have **one portable skill** (`loop-design/SKILL.md`, also packaged as
`loop-design.skill`). Agent Skills follow an open standard, so the same file
works everywhere — only the *install location* and the *always-on hook* change
per surface.

Two things to install on each surface:

1. **The skill** — the full method. Triggers when Claude recognizes relevant
   work (a skill loads on relevance, not on every turn).
2. **The always-on pointer** — one line in that surface's persistent-instructions
   slot. This is what makes Claude *consider the loop at the top of every
   session*, even before the skill triggers. Without it, the skill is available
   but not guaranteed to fire on a vague opening message.

### The always-on pointer (paste this into the persistent slot on each surface)

> At the start of any new task, project, or chat, default to framing the work as
> a loop (consult the `loop-design` skill). State the **Objective** (what "done
> well" means in one sentence), the **Metric** (how to self-score a pass without
> me reading every word), and the **Boundary** (how many passes, what runs
> unattended, what must pause for my approval). Prefer a loop that *learns* — name
> the one feedback signal worth capturing and feeding back. Propose the loop
> before producing a single hand-made pass.

---

## 1. Claude Code

**Install the skill**
- Personal (all your projects): copy the folder to `~/.claude/skills/loop-design/`
- Project-only (and shareable via the repo): `.claude/skills/loop-design/`
- Restart Claude Code, then run `/skills` to confirm it loaded. Invoke directly
  any time with `/loop-design`.

**Always-on hook**
- Paste the pointer into `CLAUDE.md` at the repo root (project-scoped) or
  `~/.claude/CLAUDE.md` (applies to every project). CLAUDE.md is read into context
  every session, so this is your guaranteed "considered each time."

**Surface note (free, objective metrics live here):** in Code your metric is
often machine-checkable — tests, type-checks, linters, build success, exit codes.
Tell the loop to treat green as the score and iterate on red. Your **boundary** is
the permissions config: which commands auto-run vs. require confirmation; gate
destructive ops (migrations, deploys, force-push). The **learning wire** is a
`DECISIONS.md` the loop appends to and re-reads, so it stops re-litigating solved
problems.

---

## 2. Claude.ai (web)

**Install the skill**
- Settings → Capabilities → Skills → upload `loop-design.skill` (custom Skills are
  available on paid plans and shared across your workspace).

**Always-on hook**
- For a specific client/workstream: create a **Project** and paste the pointer
  into the Project instructions. Every chat in that Project loads it.
- For account-wide default: put a short version in your profile preferences.
- Optional: encode the metric into a **custom Style** so self-scoring rubrics
  apply automatically to the writing it produces.

**Surface note:** this is the lightest-weight loop — great for content and
deliverables. The metric is usually a self-scoring rubric; the boundary is "how
many drafts before you show me," and the learning wire is pinning winning outputs
into Project knowledge so the next chat starts from your best work.

---

## 3. Claude Desktop

**Install the skill**
- Desktop uses your Claude.ai account, so a skill uploaded via Capabilities is
  already available here too.

**Always-on hook**
- Put the pointer in your company's Project instructions so every chat frames work
  as a loop. Keep winning examples in that Project's knowledge as the learning wire.

---

## 4. Claude Cowork

**Install the skill**
- Install the custom skill the same way (Capabilities / workspace skills). Cowork
  has subagents, so a forked loop can run passes in parallel and report back.

**Always-on hook**
- Paste the pointer into the workspace/project instructions Cowork uses for the
  engagement.

**Surface note:** Cowork is where loops do real knowledge-work end to end. Define
the boundary explicitly — what it may finish autonomously vs. what pauses for
review before it leaves the workspace (anything client-facing, factual, or
irreversible).

---

## 5. Claude API / apps you build

**Install the skill**
- Reference pre-built Skills by `skill_id`, or upload custom Skills via the Skills
  API (`/v1/skills`); the Agent SDK also loads filesystem `SKILL.md` artifacts.
  Custom Skills are shared workspace-wide.

**Always-on hook**
- Include the pointer (or the three-ingredient framing) directly in your app's
  **system prompt** — that's the API's persistent slot.

**Surface note (this is where "learns" pays most):** implement the loop in code —
`generate → self-score against the metric → critique → iterate to the boundary →
emit top N`. Then add the feedback wire: log each pass's score plus any real user
signal (e.g., an up/down on the output) to your datastore, and feed recent winners
back as few-shot examples on the next run. That single wire turns a loop that runs
into a loop that learns and compounds.

---

## Sharing with other founders

- Send them `loop-design.skill` (upload via Capabilities) or the `loop-design/`
  folder (drop into `~/.claude/skills/` for Claude Code).
- Tell them to also paste the always-on pointer into their persistent slot — the
  skill alone won't fire reliably on a cold "help me with X" without it.
- The skill is generalized: nothing client-specific, so it applies to any project
  out of the box. The only thing to personalize is the GTM metric example, which
  references a persona-to-value-driver rubric they can swap for their own.

---

## Ready to share

The skill's GTM metric section links to the Persona-Value Matrix writeup at
<https://www.michaeltaus.com/persona-value-matrix/>, so other founders who install
it land on the full method. Nothing else to fill in — the files are generalized
and ready to hand out.
