# gtm-looper

**Design loops, not prompts.** Open-source Claude skills for founders who'd rather build
the machine than crank the handle.

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

The most leveraged AI users stopped prompting one instruction at a time and started
writing **loops** — small systems that judge their own work against a metric and keep
going until it's good. This repo gives you two of those loops as installable skills.

📄 Start with the essay: [**Write Loops, Not Prompts**](<your-blog-essay-url>)

---

## The skills

### 🔁 `loop-design`
The general engine. Turns any task into a loop with three parts — **objective** (what
"done well" means), **metric** (how it scores its own pass without you reading every
word), and **boundary** (what runs unattended vs. what stops for you). Then it shows you
how to add the one feedback wire that turns a loop that *runs* into a loop that *learns*.

### 🎯 `persona-value`
The loop pointed at the only question that decides whether a startup lives: **who values
what?** It maintains one living, company-wide matrix of which buyer personas care about
which value drivers, scored by evidence strength (said → did → paid → stuck), and refines
it from every deal, churn, and experiment. One source of truth for discovery, GTM, and
product scope. Built on the [Persona-Value Matrix](https://www.michaeltaus.com/persona-value-matrix/).

---

## Install

**Claude Code** (available in every project):
```bash
git clone https://github.com/miketaus/gtm-looper
cp -r gtm-looper/skills/loop-design   ~/.claude/skills/
cp -r gtm-looper/skills/persona-value ~/.claude/skills/
```
Restart Claude Code and run `/skills` to confirm. Invoke directly with `/loop-design`.

**Claude.ai / Desktop / Cowork:** upload the packaged `.skill` files via
**Settings → Capabilities → Skills**.

To make Claude *consult these every session*, also paste the one-line pointer from
[`patterns/loop-design-install-guide.md`](patterns/loop-design-install-guide.md) into
your `CLAUDE.md` / Project instructions.

---

## The idea in 30 seconds

A prompt is a single ask you crank by hand. A loop is the machine that cranks the asks
for you and judges its own output, so your job moves from executing tasks to designing
the system. The keystroke work disappears; the judgment work — picking the objective,
the metric, the boundary — is the part that compounds. Full argument in
[the essay](<your-blog-essay-url>).

---

## Subscribe

New essays on loops, GTM, and building with AI go out to the newsletter first:
**👉 [subscribe here](<your-newsletter-url>)**.

---

## License

MIT — take the skills, fork them, ship them. A link back is appreciated, not required.
