<!--
LIVING MEMORY for the persona-value skill.
ONE map per company (entity) — not per product. Personas and value drivers are
company-wide and shared across every product, feature, and experiment. It starts
mostly empty and fills in from evidence over time. The persona-value SKILL.md reads
this file before answering and rewrites it after new evidence.
Evidence log is APPEND-ONLY.
Confidence: 0 Hypothesis · 1 Signal · 2 Pattern · 3 Validated (PAID/STUCK only).
Evidence tier: SAID · DID · PAID · STUCK.
-->

# Persona-Value Map — [COMPANY]

_Last updated: [DATE] · Maintained by: [FOUNDER/TEAM]_

What the company does today: [one line]

> Personas and value drivers below are **company-wide**. Products, features, and
> experiments are tracked in the Bets register and feed evidence into these shared
> cells.

---

## Personas (company-wide)

| ID | Persona (role + job-to-be-done) | Segment | Status |
|----|----------------------------------|---------|--------|
| P1 | [e.g., Ops lead automating manual reporting] | [SMB/Mid/Ent] | active / hypothesis / retired |
| P2 | | | hypothesis |

## Value drivers (company-wide)

| ID | Value driver (specific outcome, not "saves time") | Status |
|----|---------------------------------------------------|--------|
| V1 | [e.g., Cut monthly reporting from 3 days to 2 hours] | active / hypothesis / retired |
| V2 | | hypothesis |

## The matrix

Rows = personas, columns = value drivers. Each cell = confidence (0–3) + strongest evidence tier.

| Persona \ Value | V1 | V2 |
|-----------------|----|----|
| P1 | 0 — | 0 — |
| P2 | 0 — | 0 — |

<!-- Cell format example: `2 PAID` = confidence 2, best evidence is willingness to pay. -->

---

## Bets register (products / features / experiments)

Each bet targets one or more cells. When it ships, its result becomes evidence.

| ID | Product / feature / experiment | Targets cell(s) | Status | Result → evidence |
|----|--------------------------------|-----------------|--------|-------------------|
| B1 | [e.g., Self-serve onboarding flow] | P1×V1 | planned / testing / shipped | [link to evidence entry] |
| B2 | | | planned | |

---

## Evidence log (append-only — newest at top)

<!-- One entry per signal. Never edit or delete past entries. -->

### [DATE] — [P? / V?] — [SAID/DID/PAID/STUCK]
- **Source:** [call with X / closed-won / churn interview / experiment B?]
- **Product/feature/experiment:** [B? or "n/a"]
- **What happened:** [concrete, 1–3 sentences]
- **Effect on matrix:** [P? × V? confidence 1 → 2]
- **Note:** [why it counts; any caveat]

---

## PMF signals (auto-surfaced)

- **Beachhead candidate(s):** [cells at confidence ≥2 with PAID/STUCK] — none yet
- **Contradictions to resolve:** none yet
- **Deprioritize candidates:** none yet

## Open questions / next moves

_Pick high-potential, low-confidence cells. Each is a discovery question or a bet._

1. [Question or bet targeting P? × V?, designed to produce DID/PAID/STUCK evidence]
2.
3.

---

## Changelog

| Date | Change | By |
|------|--------|----|
| [DATE] | Instantiated map | [NAME] |

---

<!-- EXAMPLE (delete before use) — shows the format filled in:

Bets register row:
| B1 | Self-serve onboarding flow | P1×V1 | shipped | see 2026-05-02 entry |

Evidence entry:
### 2026-05-02 — P1 / V1 — STUCK
- Source: 30-day cohort retention, self-serve onboarding
- Product/feature/experiment: B1
- What happened: Cohort that hit the 2-hour first report retained at 71% vs 38% baseline.
- Effect on matrix: P1 × V1 confidence 2 → 3
- Note: First STUCK evidence for V1; P1×V1 is now the beachhead. Build to compound it.

-->
