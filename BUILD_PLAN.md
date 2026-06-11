# BUILD_PLAN.md

The rollout, as a loop you execute phase by phase.

- **Objective:** a working content pipeline — author in this repo, publish to Ghost,
  amplify to social through an approval gate — plus the public skills repo it runs on.
- **Metric:** each phase has explicit acceptance checks. A phase is done only when its
  checks pass and it's committed.
- **Boundary:** stop at every ⛔ checkpoint and ask the human. Anything involving
  secrets, OAuth, making the repo public, or publishing live is theirs to approve.

## Operating rules

1. Work phases in order. Don't start a phase until the previous one's checks pass.
2. Before any real network send, run the `--dry-run` path first.
3. Commit after each phase: `feat(phaseN): …`.
4. At each ⛔ checkpoint: stop, summarize what's needed, and wait. Do not attempt to
   enter credentials, complete OAuth, flip the repo to public, or publish live yourself.
5. After each phase, report 3 lines: what you did · acceptance result · what's next.

---

## Phase 0 — Repo bootstrap
**Goal:** a clean, initialized repo matching `CLAUDE.md`'s layout, safe to be public.
- [ ] `git init`; confirm `.gitignore` ignores `.env`, `private/`, `**/*.local.md`,
      `__pycache__/`, `*.pyc`, `dist/`.
- [ ] Confirm tree: `skills/`, `patterns/`, `posts/`, `scripts/`, `README.md`,
      `CLAUDE.md`, `LICENSE`, `requirements.txt`, `.env.example`.
- [ ] Run a privacy sweep before the first commit: grep the tree for client names,
      emails, secret-shaped strings, and private URLs. The only intended personal
      reference is the `michaeltaus.com` Persona-Value Matrix link. Fix anything else.
- [ ] `pip install -r requirements.txt`.
- [ ] `cp .env.example .env` (leave values blank for now).
- **Acceptance:** privacy sweep clean; `git status` clean after first commit; `python
  scripts/publish_to_ghost.py posts/2026-06-11-write-loops-not-prompts.md --dry-run` prints a payload.
- ⛔ **Human checkpoint:** the human creates the **public** GitHub repo and adds the
  remote (`git remote add origin …`). Repo creation and visibility are the human's to
  set — prepare everything and the push, but don't create the repo or change its
  visibility yourself.

## Phase 1 — Ghost publish path (verify the engine)
**Goal:** a real draft appears in Ghost from a repo post.
- [ ] Document the one-time Ghost setup in README (Admin → Integrations → custom
      integration → copy the `id:secret` Admin API key).
- [ ] Add a `make dry` / `make draft` convenience target (or a short `scripts/` note).
- **Acceptance:** with `.env` filled by the human, running the script on the example
  post creates a Ghost **draft**; running it again **updates** that draft (no duplicate).
- ⛔ **Human checkpoint:** the human adds the Ghost integration and fills `.env`. Ask
  before the first live `--publish`.

## Phase 2 — Skill packaging + release
**Goal:** skills are installable as versioned `.skill` files.
- [ ] Add `scripts/repackage_skills.py`: validate each `skills/*/SKILL.md`, zip each
      into `dist/<name>.skill`.
- [ ] Optional: a GitHub Action that runs it on tag/release and attaches artifacts.
- **Acceptance:** running it emits valid `.skill` files for `loop-design` and
  `persona-value`; frontmatter validation passes.

## Phase 3 — Social variants
**Goal:** each post yields native social variants, no bare link-drops.
- [ ] Add `scripts/make_social_variants.py`: from a post, generate a LinkedIn-native
      post and an X thread into `posts/<slug>.social.md`. Use `skills/loop-design` for
      the iterate-and-score loop and `skills/persona-value` as the metric.
- **Acceptance:** variants are generated, native (no "link in comments" crutch), and
  within platform length norms.

## Phase 4 — Orchestration + approval (n8n)
**Goal:** end-to-end flow with a human gate.
- [ ] Add `scripts/pipeline.py` entrypoint: draft post → publish Ghost **draft** →
      emit the social variants → return links/paths.
- [ ] Scaffold an n8n workflow (export JSON to `automation/`): schedule trigger →
      call `pipeline.py` → Telegram approve/reject → on approve, flip the Ghost draft to
      published and push social variants via the official-API scheduler → log result.
- **Acceptance:** a dry-run with a test post reaches the Telegram approval step; on
  approve, the draft is published and variants are queued.
- ⛔ **Human checkpoint:** the human connects LinkedIn/X via the scheduler's OAuth and
  approves each publish. No browser-extension automation.

## Phase 5 — Growth instrumentation (the loop that learns)
**Goal:** the pipeline gets smarter over time.
- [ ] Log per-post outcomes (subscribers gained, engagement) to PocketBase.
- [ ] Weekly review step: surface top performers, and feed the signal back into topic
      selection and into `skills/persona-value`'s map (treat readers as a persona).
- **Acceptance:** a metrics log exists and the weekly step produces an update to the
  persona-value map.

## Phase 6 — Ship the first piece
**Goal:** prove the whole pipeline on a real post.
- [ ] The inaugural post already exists at `posts/2026-06-11-write-loops-not-prompts.md`.
      Run it through Phases 1→4 (Ghost draft → review → publish → social variants).
- **Acceptance:** the post is live on Ghost with the repo+newsletter footer, and the
  social variants are queued — all via the pipeline, not by hand.

---

**Definition of done:** a new post can go from a prompt in Claude Code to a Ghost draft
plus queued social variants, gated by one Telegram approval, with the skills installable
from the public repo and outcomes logged back into the persona-value map.
