---
name: persona-value
description: >-
  Maintain ONE living persona-value matrix for the whole company and use it as the
  single source of truth for three things: customer discovery / product-market fit,
  go-to-market and content, and product scope and design decisions. Use this
  whenever the founder or team is doing customer discovery, defining or refining
  personas, mapping value propositions, running win/loss or churn analysis,
  reviewing how content or experiments performed, deciding what to build, prioritize,
  or cut, resolving a design tradeoff, choosing which segment to focus on, or judging
  product-market fit. Also use it right after any loop that touched personas or
  value, to capture the learning. Don't answer from general knowledge — read the
  living matrix, update it from new evidence, and say what changed and what to test
  or build next.
---

# Persona-Value (a living, company-wide skill)

## What this is

This skill maintains **one living persona-value matrix for your company**: a
structured, evidence-backed map of which buyer personas care about which value
drivers, and how sure you are. It is the single source of truth behind three jobs
a founding team does constantly:

1. **Discovery / PMF** — who actually values what, and where the beachhead is.
2. **GTM & content** — which persona to target with which value driver.
3. **Product scope & design** — what to build, prioritize, cut, and how to resolve
   design tradeoffs.

These are the same question asked three ways, so they share one matrix. That's why
this is a single skill: a win in sales, a churn interview, and a feature experiment
all update the *same* personas and value drivers. Split them apart and your
roadmap and your messaging start optimizing against different beliefs about the
same customers.

The skill has two parts:

- **A static brain** (this file): the method, the scoring rubric, and the update
  protocol. It rarely changes.
- **A living memory** (`references/persona-value-map.md`): the company's matrix,
  evidence log, bets register, and changelog. It changes constantly. There is **one
  map per company (entity)** — not one per product. Personas and value drivers are
  company-wide and shared across every product, feature, and experiment.

Always read `references/persona-value-map.md` before answering, and update it after
any new evidence. The brain is portable and shareable between founders; the memory
is your company's.

Based on [The Persona-Value Matrix](https://www.michaeltaus.com/persona-value-matrix/).

## The matrix in brief

Rows are **personas** (a specific buyer — role, the job they're trying to do, and
segment — not a demographic). Columns are **value drivers** (a specific outcome the
company creates — "cut onboarding from weeks to hours," not "saves time"). Each cell
holds how strongly *that persona* values *that driver*, as a confidence score plus
the evidence behind it.

Personas and value drivers live at the **company level**. A product, feature, or
experiment is a **bet** that one or more cells are real; shipping it and watching
what happens is how you generate evidence about those cells. So experiments across
many products feed one shared matrix — they don't each get their own.

## Scoring rubric (this is the metric)

**Confidence (0–3):**
- **0 — Hypothesis.** A reasoned guess. No evidence yet.
- **1 — Signal.** One credible data point points this way.
- **2 — Pattern.** Multiple independent data points agree.
- **3 — Validated.** Backed by behavior or money, not just words.

**Evidence tier (what kind of signal it is):**
- **SAID** — stated in conversation. Weakest; people misreport what they'll do.
- **DID** — observed action (signed up, activated, referred, returned).
- **PAID** — willingness to pay, or actually paid.
- **STUCK** — retention / repeated use. The strongest signal of real value.

**The gate that keeps you honest:** a cell may not reach confidence **3** on SAID
evidence alone. Validated requires PAID or STUCK. This stops the matrix from
filling with flattering interview quotes that never convert.

## Update protocol (what makes it living)

When new evidence arrives, run these steps and write the result into
`references/persona-value-map.md`:

1. **Capture** the signal plainly: what happened, the source, the date, and — if it
   came from shipping something — which **product / feature / experiment** produced
   it. Keep it concrete.
2. **Classify** it onto the matrix: which persona(s) and which value driver(s)? If
   nothing fits, propose a new persona or value driver with status `hypothesis` —
   don't force a bad fit.
3. **Tier the evidence** (SAID / DID / PAID / STUCK) and judge its strength.
4. **Update the cell.** Raise or lower confidence per the rubric. Append an entry to
   the evidence log with date, source, experiment tag, tier, and note. Evidence is
   **append-only** — never delete or overwrite; the trail is the asset.
5. **Reconcile.** If new evidence contradicts a high-confidence cell, flag it for
   review rather than silently overwriting — contradictions are where learning
   hides. Merge duplicate personas/values; mark for retirement any with sustained
   non-resonance after real effort.
6. **Surface.** Report what changed, the current PMF beachhead candidate(s), and the
   2–3 highest-leverage things to test or build next.

## Reading the matrix for product-market fit

- **Beachhead** = a single persona (or tight segment) with at least one value driver
  at confidence ≥2 backed by PAID or STUCK evidence. Focus there.
- **Diffuse matrix** (lots of cells at confidence 1, nothing high) = pre-PMF. Narrow,
  don't broaden. Pick the most promising column and go deep.
- **A driver strong across many personas** can signal a platform play, but still
  force a beachhead choice — "valued by everyone" with no clear ICP usually means no
  one buys urgently.
- **A persona with all-low cells** after genuine effort is a candidate to
  deprioritize. Saying no is a PMF decision too.

## Using the matrix for product scope & design

The roadmap is a portfolio of bets on cells. Use the matrix to decide what earns
build time:

- **Prioritize** bets that *compound a validated cell* (confidence ≥2, PAID/STUCK) —
  these deepen the beachhead — and cheap bets that *test a high-potential,
  low-confidence cell*. Rank by leverage × how much it moves confidence.
- **Cut or defer** anything that serves a retired persona, an invalidated cell, or no
  active cell at all. A feature that doesn't map to a live persona×value cell is
  scope creep until it earns one — make it earn a `hypothesis` cell first.
- **Resolve design tradeoffs** in favor of the highest-confidence persona×value the
  product is committed to. Don't degrade a validated cell to chase a hypothesis cell;
  if a design serves persona A's validated driver at the expense of persona B's
  unvalidated one, that's usually the right call, and the matrix says so explicitly.
- **Record the bet.** When you commit to building something, log it in the bets
  register against the cell(s) it targets, so its eventual result flows back as
  evidence instead of being forgotten.

## Using the matrix for GTM & content

Score every asset on whether it connects a **defined persona** to a **value driver
the matrix says that persona actually cares about** (confidence ≥1, ideally ≥2).
Lead with your highest-confidence cells in demand gen; use lower-confidence cells as
explicit experiments. This is the metric that content loops optimize against.

## Drive the next discovery (close the loop)

Don't just record — point at what to learn next. From the matrix, pick cells that are
**high-potential but low-confidence**, or any flagged contradiction, and generate 3–5
discovery questions designed to elicit DID / PAID / STUCK evidence rather than more
SAID. Ask about past behavior and real tradeoffs ("walk me through the last time
you…", "what did you do instead, and what did it cost you?"), not hypotheticals
("would you use…?").

## How this composes with `loop-design`

`loop-design` is the general engine for running any improvement loop; this skill is
the shared memory those loops optimize against. A content or experiment loop uses
`loop-design` for the mechanics and this matrix for the metric and targeting. When a
loop ends, its result enters here as an evidence entry via the update protocol. One
supplies the loop; the other supplies the truth it's chasing.

## Keeping the memory living, per surface

- **Claude Code / Cowork** — the map file is writable. Update
  `references/persona-value-map.md` directly and commit it to your repo. This is the
  true living mode and the natural home for a founding team.
- **Claude.ai / Desktop** — uploaded skills are read-only at runtime, so keep the
  living map as a **Project knowledge** doc the whole team updates, while the method
  stays in the skill. Re-upload the skill only when the *method* changes, not the
  data.
- **API / apps** — store the map in your datastore; load it into context each run and
  write updates back programmatically, so the loop can run hands-off at scale.
