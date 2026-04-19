![Status](https://img.shields.io/badge/status-active-success?style=flat-square) ![Mode](https://img.shields.io/badge/mode-minimum_viable-blue?style=flat-square) ![Focus](https://img.shields.io/badge/current_focus-backend_flagship-success?style=flat-square)

# python-playground

My Python learning playground — tracking my way through the official [Python Tutorial](https://docs.python.org/3/tutorial/) as a foundation for backend engineering.

## 🎯 Why this repo exists

This is the groundwork for my flagship project [`payment-ledger-api`](https://github.com/ikuko-otani) (FastAPI + SQLAlchemy 2.0 async + PostgreSQL), to be shipped by June 2026 as part of my preparation for Senior Backend Engineer roles at EU scale-ups (Mollie, HelloFresh, Revolut, Prima, GetYourGuide).

## ✅ Learning Status (as of 2026-04-19)

Completed Chapters 9.1–9.5 of the official Python Tutorial. Chapters 9.6–9.11 are **intentionally deferred** — they will be learned on-demand while building the flagship project, as recommended by my learning plan dated 2026-04-19.

### Progress

| Chapter | Topic | Status |
|---|---|---|
| 9.1 | A Word About Names and Objects | ✅ Done |
| 9.2 | Python Scopes and Namespaces | ✅ Done |
| 9.3 | A First Look at Classes | ✅ Done |
| 9.4 | Random Remarks | ✅ Done |
| 9.5 | Inheritance | ✅ Done |
| 9.6 | Private Variables | ⏸ Deferred — learn on demand |
| 9.7 | Odds and Ends | ⏸ Deferred — learn on demand |
| 9.8 | Iterators | ⏸ Deferred — will re-encounter via SQLAlchemy query results |
| 9.9 | Generators | ⏸ Deferred — will re-encounter when streaming data |
| 9.10 | Generator Expressions | ⏸ Deferred — learn on demand |
| 9.11 | Classes (summary notes) | ⏸ Deferred — learn on demand |

## 🧭 Why defer 9.6–9.11?

The decision is deliberate and tactical, not a knowledge gap I am hiding:

1. **I already have working mental models for the blocked concepts.** Iterators, generators, and private-variable conventions appear naturally inside FastAPI + SQLAlchemy code, where I will meet them in real context rather than isolated tutorial examples.
2. **My 73-day sprint (2026-04-19 → 2026-06-30) is optimized for shipping.** Tutorial completion is not a hiring signal for EU backend roles; a production-grade flagship project is. Finishing Chapter 9 cover-to-cover would delay the flagship start by roughly two weeks with marginal portfolio benefit.
3. **On-demand learning has higher retention.** When SQLAlchemy returns a generator-backed result set, that is the moment to truly understand `yield` — not a week earlier in an abstract tutorial.

This trade-off is documented in `learning_plan_minimum_viable.md` (v3, 2026-04-19), which I review at the 2026-06-30 checkpoint.

## 📅 When 9.6–9.11 will be revisited

- **Trigger-based (preferred):** when I hit iterators/generators/private-name idioms during flagship implementation, I return to the relevant tutorial section with real context.
- **Calendar-based fallback:** if no trigger appears by 2026-09-30 (post-flagship), I do a focused 2-day sweep to close the gap.

## 🔗 Related repositories

- [`payment-ledger-api`](https://github.com/ikuko-otani) — flagship project (target: ship by 2026-06)
- [`neetcode-250`](https://github.com/ikuko-otani/neetcode-250) — DSA preparation (Phase 1 starts 2026-07-01)
- [`typescript-playground`](https://github.com/ikuko-otani/typescript-playground) — on strategic hold
- [`react-playground`](https://github.com/ikuko-otani/react-playground) — on strategic hold
- [`laravel-playground`](https://github.com/ikuko-otani/laravel-playground) — strategic retreat

## 📚 References

- [The Python Tutorial — Classes (Chapter 9)](https://docs.python.org/3/tutorial/classes.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
