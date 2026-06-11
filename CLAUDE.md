# CLAUDE.md — gtm-looper

Personal content pipeline: author posts and skills here, publish to Ghost, amplify
to social. This file is your durable context. The work queue is `BUILD_PLAN.md`.

## Architecture (decisions already made — don't relitigate)

- **This repo = source of truth + asset host.** Posts (`posts/`), skills (`skills/`),
  and patterns (`patterns/`) live here. People install skills straight from the repo.
- **Ghost = published narrative + the owned email list.** It renders posts and runs
  the newsletter. It does NOT host the skill binaries — the repo does.
- **Social = top-of-funnel**, driven from each post via an official-API scheduler.
- **n8n = orchestration + human approval** (Telegram). It schedules runs and gates
  anything going live.
- **Claude Code (you) = the generation + publish engine.**

## Repo map

```
skills/      installable Agent Skills (loop-design, persona-value) — keep open (MIT)
patterns/    playbooks and reference docs
posts/       canonical post markdown (dated, YAML frontmatter) — the source of truth
scripts/     publish_to_ghost.py (+ scripts added during the build)
```

## Non-negotiables (guardrails)

- **Secrets live only in `.env`** (gitignored). Never commit them, never print them in
  output, never hardcode. Credential setup and OAuth are done by the human, not you.
- **Draft-first.** `publish_to_ghost.py` creates drafts by default. A live publish or a
  social post happens only after explicit human approval (the Telegram gate). Never
  auto-publish.
- **No browser-extension automation for LinkedIn** — it risks the account. Social goes
  out only through official-API schedulers.
- **Repo markdown is canonical.** Publishing is idempotent (update by slug), so never
  create duplicate posts.
- **Skills stay open.** Capture email via the post/README subscribe CTA, never by
  gating a skill download.
- **This is a PUBLIC repo.** Never commit anything personal, client-identifying, or
  customer-specific: no client names, no real customer evidence, no private URLs, no
  real `.env`. When in doubt, leave it out.
- **Real persona-value data is private.** The repo ships only the *template* at
  `skills/persona-value/references/persona-value-map.md`. When instantiating it for a
  real company, copy it to `private/persona-value-map.md` (gitignored) or keep the
  working map in Ghost / Project knowledge — never fill the in-repo template with real
  personas, deals, or customer quotes.

## Conventions

- Python scripts in `scripts/`, run with `--dry-run` before any real send.
- Posts: `posts/YYYY-MM-DD-slug.md` with frontmatter (`title, slug, excerpt, tags,
  feature_image, canonical_url, status`).
- Skills follow the Agent Skills standard (`SKILL.md` + optional `references/`); keep
  each SKILL.md under ~500 lines.
- Commit after each completed build phase with a clear message.

## How to work (loop-design, applied to yourself)

At the start of any task, frame it as a loop: state the **objective**, the **metric**
you'll check it against, and the **boundary** where you stop and ask. Prefer loops that
learn. When generating or judging content, use `skills/persona-value` as the metric
(does this connect a defined persona to a value driver?). The skills in `skills/` are
yours to consult.
