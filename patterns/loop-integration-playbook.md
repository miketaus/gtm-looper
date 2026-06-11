# Loop Integration Across Claude Surfaces

How the objective/metric/boundary loop shows up on each Claude surface, and how to
make it a loop that *learns* rather than one that merely runs. Pairs with the
`loop-design` skill (the method) and `persona-value` (the metric for content/GTM work).

## The loop in one line

- **Objective** — what "done well" means, one sentence.
- **Metric** — how the system scores its own pass without a human reading every word.
- **Boundary** — what runs unattended vs. what stops for approval.
- **Feedback wire** — the one signal that, captured and fed back, makes the loop compound.

## A reusable metric

For any content or GTM work, score each asset on whether it connects a **defined
persona** to a **named value driver** (not a generic benefit). A persona-to-value
rubric like the Persona-Value Matrix makes a good shared scoring engine, because the
same rubric judges posts, landing pages, ads, and sequences. See
[The Persona-Value Matrix](https://www.michaeltaus.com/persona-value-matrix/).

## Surface by surface

### Claude Code
Native home of loops. Objective lives in `CLAUDE.md`; the metric is usually
machine-checkable (tests, type-checks, linters, build, exit codes); the boundary is the
permissions config (which commands auto-run vs. require confirmation). Learning wire: a
`DECISIONS.md` the loop appends to and re-reads, so solved problems stay solved.

### Claude Cowork
Knowledge-work loops for deliverables. Metric is a self-scoring rubric; boundary is how
many internal drafts before it shows you, and a pause for review before anything ships.
Learning wire: save winning outputs into the project as examples.

### Claude Desktop
Per-workspace loop definitions in project instructions, tuned to a voice and a set of
constraints. Learning wire: a "winning examples" set fed back as context.

### Claude.ai (web / Projects)
Put objective + metric + boundary in Project instructions so every chat runs the loop
pattern by default. Encode the metric into a custom Style. Learning wire: pin the best
outputs into Project knowledge.

### API / apps you build
Where "learns" pays most. Implement the loop in code: generate → self-score against the
metric → iterate to the boundary → emit top N. Learning wire: log each pass's score plus
any real user up/down signal to a datastore, then feed recent winners back as few-shot
examples.

### Orchestration with a human gate
For scheduled, hands-off content, a workflow runner (for example n8n) with a chat-based
approval step (for example a Telegram approve/reject) gives you the boundary for free.
Upgrade it from runs → learns with two additions: a self-scoring node *before* the
approval step (so only high-scoring drafts reach a human), and a log of every
approve/reject decision fed back as examples to the generation step.

## Loop template (copy-paste)

> Objective: **\<what done well looks like, one sentence\>**.
> After each pass, score 1–10 against: **\<your metric\>**.
> For anything below 9, critique it specifically, then rewrite.
> Take up to **\<N\>** passes, then show me only the top **\<K\>**.
> Capture **\<the one feedback signal\>** so the next run starts smarter.
> \[Attach 2–4 examples of the result you want — examples beat description.\]

## Where to start

Pick the surface where the boundary already exists (often the orchestration + approval
step), add the metric and the feedback wire, and you've turned a loop that runs into one
that learns — the highest-leverage upgrade for the least new infrastructure.
