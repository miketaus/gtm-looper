---
name: loop-design
description: >-
  Frame work as a self-correcting loop (objective, metric, boundary) instead of
  a one-off prompt. Use this at the START of any new session, chat, project, or
  task — especially when the user is scoping, planning, automating, or asking for
  output that will be iterated, repeated, or produced at scale (drafts, content,
  code, research, analysis, deliverables, workflows). Trigger this whenever the
  user describes a goal and wants Claude to keep working toward it, even if they
  never say the word "loop." Default to proposing a loop before grinding through
  the task by hand.
---

# Loop Design

## Why this exists

Most people use AI by hand-cranking prompts: ask, read the answer, decide what's
next, ask again. That keeps a human in the driver's seat for every turn and caps
output quality at "whatever I had patience to refine."

Power users have moved past this. Instead of prompting each step, they design a
**loop**: a small machine that generates its own prompts, judges its own work,
and keeps going toward a goal until it hits a stopping point. The human's job
shifts from *executing the task* to *designing the loop*. The keystroke work
disappears; the judgment work stays.

This skill exists so that, at the start of any non-trivial task, Claude proposes
and runs a loop rather than silently producing a single pass.

## The three ingredients

Every loop needs exactly three things. If any one is missing, the loop can't run
itself.

1. **Objective** — what "done well" looks like, stated in one sentence. This is a
   definition of quality, not a description of the task. "Summarize the call"
   is a task; "a summary a busy exec could act on in 30 seconds without the
   recording" is an objective.

2. **Metric** — how the *system itself* can tell whether a pass came out better
   or worse, without a human reading every word. This is the hard part and the
   highest-leverage one. If you can't yet say how a pass would be scored, you've
   found the real work — see "Defining a good metric" below.

3. **Boundary** — how far the loop runs on its own before it stops and checks in.
   This is where the user's risk tolerance and values live: how many passes, what
   it may do unattended, and what must pause for human approval.

Get these three right and the loop asks, scores itself against the metric,
adjusts, and repeats — no babysitting per turn.

## Runs vs. learns: the feedback wire

- A loop that **runs** does the same thing today it did yesterday. That's
  automation. Useful, but flat.
- A loop that **learns** captures whether each pass landed and feeds that signal
  back into what it does next. That compounds — it gets better every cycle.

The difference is usually one small addition: a feedback wire. A score that gets
logged. An up/down signal. A "winning examples" file that the next run reads
first. Whenever you design a loop, ask: *what is the one signal that, if captured
and fed back, would make this loop smarter over time?* Add it.

## How to apply this at the start of a session

When a user opens a task that is iterative, repeated, scoped, or quality-
sensitive, don't immediately produce a single best-effort pass. First, briefly
frame the loop:

> "Let's run this as a loop. Objective: **\<one sentence\>**. I'll score each pass
> on **\<metric\>**, rewrite anything below bar, take up to **\<N\>** passes, then
> show you the top **\<K\>**. Sound right, or want to adjust the metric or
> boundary?"

Keep it short. If the user has already given enough to infer all three, state
your assumptions inline and just run the loop rather than interrogating them.
Then actually execute it: generate, self-score against the metric, critique
sub-bar passes, rewrite, and stop at the boundary — surfacing the winners and the
scores, not every intermediate draft.

## Defining a good metric (the hard part)

A metric is good when it's specific enough that two different passes get clearly
different scores. Vague metrics ("make it good") can't drive a loop. Pick the
cheapest signal that genuinely tracks quality for the domain:

- **Code** — objective and free: tests pass/fail, type checks, linters, build
  success, benchmark numbers. Exit codes *are* the metric; no reading required.
- **Writing / content** — a self-scoring rubric, e.g. 1–10 on: does the opening
  earn attention, is there exactly one core idea, would the intended reader learn
  something, is it within length. Rewrite anything below a 9.
- **Research / analysis** — a coverage checklist: are all sub-questions answered,
  are claims sourced, are counter-arguments represented, are numbers internally
  consistent.
- **Design / UI** — a heuristic checklist plus, where possible, a rendered
  screenshot the loop can inspect against the spec.
- **Go-to-market / marketing content** — score each asset on whether it connects a
  **defined buyer persona** to a **specific value driver** (not a generic
  benefit). A persona-to-value-driver rubric like the Persona-Value Matrix works
  well as a reusable scoring engine here, because the same rubric judges blog
  posts, landing pages, ads, and sequences. (Reference:
  [The Persona-Value Matrix](https://www.michaeltaus.com/persona-value-matrix/).)

The best metric is one the loop can evaluate itself. The second best is one a
human can check in seconds. Avoid metrics that need a full read of every pass —
that just reinstates the hand-cranking you're trying to escape.

## Where the human stays in the loop

Designing loops doesn't free you to do nothing — it moves your effort to the
decisions only you can make:

- **The objective** forces you to define what "good" actually means.
- **The metric** is a judgment call about what's worth optimizing.
- **The boundary** encodes your risk tolerance and values.

So the loop should pause and hand control back to the human at exactly the points
the boundary names: before anything ships externally, before irreversible or
costly actions, and whenever a pass scores low for reasons the metric can't
explain. Surface the why, not just the result.

## The loop template (copy-paste)

> Objective: **\<what done well looks like, one sentence\>**.
> After each pass, score 1–10 against: **\<your metric\>**.
> For anything below 9, critique it specifically, then rewrite.
> Take up to **\<N\>** passes, then show me only the top **\<K\>**.
> Capture **\<the one feedback signal\>** so the next run starts smarter.
> \[Attach 2–4 examples of the result you want — examples beat description.\]

## Quick start: turn any task into a loop

For a task the user already does with AI (drafting, summarizing, prepping,
generating), help them answer three questions — that *is* the loop:

1. **Objective** — what does "done well" look like in one sentence?
2. **Metric** — how would the system know a pass got better or worse, without you
   reading every word? (If you can't answer this, that's the real work — solve it
   first.)
3. **Boundary** — what can it do without you, and where must it stop and check in?

Answer those three and you've designed a loop. Add a feedback wire and you've
designed one that learns.
