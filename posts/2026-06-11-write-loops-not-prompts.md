---
title: "Write Loops, Not Prompts"
slug: write-loops-not-prompts
excerpt: "The most leveraged AI users stopped prompting. For founders, the loop that matters most isn't pointed at your content — it's pointed at who values what."
tags: ["GTM", "AI", "Loops", "Product-Market Fit"]
canonical_url: ""
status: draft
---

The most leveraged people I know have quietly stopped prompting their AI. Not because prompting got worse, but because they found something with far more leverage. The clearest articulation of the shift comes from Boris Cherny, who built Claude Code, and was written up well by [Dharmesh Shah](https://simple.ai/p/learning-to-write-your-first-ai-loop): stop typing one instruction at a time, and start writing a loop that does the work for you.

It's worth understanding the distinction, because it changes what your job actually is.

## A prompt is a task. A loop is a machine.

A prompt is a single ask you crank by hand. You ask, you read the answer, you judge it, you decide what comes next, you ask again. You are the engine, and the output is capped at whatever patience you had to keep refining.

A loop is the machine that generates those asks for you and judges its own output, so you step out of the per-turn driver's seat and into designing the system. You stop cranking and start building the thing that cranks.

A loop needs exactly three parts:

- **Objective** — what "done well" means, in one sentence. Not the task ("write a headline") but the standard ("a headline a skeptical buyer reads and thinks *that's my problem*").
- **Metric** — how the system scores its own pass, without you reading every word. This is the hard part, and the one most people skip.
- **Boundary** — how far it runs on its own before it stops and checks with you.

Give it those three and it runs itself: it drafts, scores against the metric, rewrites what falls short, and repeats until it's good or it hits the boundary. You design once instead of steering constantly.

## A loop that runs vs. a loop that learns

Most automation is a loop that *runs*: it does the same thing today it did yesterday. Useful, but flat.

A loop that *learns* captures whether each pass actually landed and feeds that signal back into the next one. It compounds. The difference is almost always one small addition — a score that gets logged, a thumbs up or down, a file of winners the next run reads first. One feedback wire, and a loop that was merely tireless becomes one that gets sharper every cycle. Over enough cycles, the learning loop wins by default.

## The loop that decides whether your startup lives

Here's the part that matters if you're building a company.

You can wrap a loop around your content, your code, your inbox — and you should. But the loop that determines whether your startup survives isn't any of those. It's the one pointed at a single question: **who values what?**

Every founder is running that loop whether they admit it or not. Most run it by hand and badly: a customer call here, a gut feeling there, a hopeful pivot when the runway gets short. The signal arrives constantly — a closed deal, a churned account, a landing page that converts or doesn't — and most of it evaporates instead of accumulating into anything you can steer by.

So make that loop explicit, and give it the three parts:

- **Objective:** a validated map of which buyer persona genuinely cares about which value driver — the thing customer discovery is *actually* for.
- **Metric:** score every signal by how strong it is. Talk is weak (people misreport what they'll do); behavior is better; willingness to pay is strong; retention is strongest. The discipline that keeps you honest: nothing counts as "validated" on the strength of a flattering interview quote alone. It has to be backed by what people *did* or *paid*.
- **Boundary:** the matrix proposes; real customers dispose. The loop tells you what to go test next; you still have to go test it.

I've written up the specific framework I use for this — the [Persona-Value Matrix](https://www.michaeltaus.com/persona-value-matrix/) — but the framework matters less than the move: treat product-market fit as a loop that learns, not a one-time deck you fill out and forget.

## The trick: give the loop a memory

A learning loop is only as good as what it remembers. If every session starts from scratch, nothing compounds. So the highest-leverage version of this is to give the loop a persistent memory — a living document that every win, loss, and experiment updates, so the map of who-values-what gets sharper on its own over time, across every tool you use. The loop stops being a thing you run and becomes a thing that accrues.

## Your job is loop design

If you were hoping the loops free you up to do nothing, here's the bad news: the people running them are busier than ever. The keystroke work disappears, which is the win. The judgment work doesn't.

You pick the objective, which forces you to define what "good" even means. You choose the metric, which is a bet on what's worth optimizing. You draw the boundary, which is where your values and your risk tolerance live. Those are the decisions that were always yours, and now they're the *only* ones that are. Loop design is the skill that compounds from here.

So pick one thing you already do with AI, and write down its objective, its metric, and its boundary. If you can't name the metric yet — if you can't say how the system would know a pass got better or worse without you reading it — congratulations: you just found the real work.

---

*I packaged the two loops I lean on most as open-source skills you can install and fork: **loop-design** (the general engine) and **persona-value** (the one pointed at who-values-what). They're in the repo linked below. Take them, break them, tell me what you'd change.*
