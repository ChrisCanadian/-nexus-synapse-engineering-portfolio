# Nexus Synapse Engineering Portfolio

### From a Rocket League overlay to a model-agnostic AI runtime

> **The model is not the system.**  
> Nexus Synapse moves continuity, state, context, authority, tools, and evidence into an explicit runtime around interchangeable model inference.

---

## The short version

I did not set out to build an AI runtime.

In August 2025, I was using GPT to help me build a custom overlay for streaming Rocket League. As the project grew, I kept running into the same limitations: memory and continuity disappeared, tool use was constrained, and prompt/context limits forced me to rebuild information the model had already seen.

Instead of working around the same problems again, I asked a different question:

> **How would you start building an AI?**

On August 19, 2025, I created `bootstrap.py`. That experiment kept expanding as I tried to move more responsibility out of the prompt and into software I could inspect, persist, govern, and test.

That became Nexus Synapse.

The Rocket League overlay is still unfinished.

---

## What Nexus Synapse became

**Nexus Synapse is a continuity runtime that prepares, governs, extends, and preserves the operating environment around interchangeable model inference.**

The language model performs inference inside that environment. The runtime owns the surrounding responsibilities.

At a high level:

```text
authenticated request
        ↓
analysis + eligible continuity
        ↓
Structured State Reconstruction (SSR)
        ↓
behavior / capability / authority boundaries
        ↓
selected model inference
        ↓
optional governed tool execution
        ↓
deterministic checks
        ↓
persistence + adaptation + evidence
        ↓
response
```

If you only want the current production responsibility chain without the project's historical terminology, start here:

**[Current Production Responsibilities — two-minute orientation](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)**

---

## Start here

1. **[Current Production Responsibilities](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)** — the shortest current-architecture view.
2. **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)** — what is production-inspected, isolated, reconstructed, historical, or not demonstrated.
3. **[Visual Gallery](docs/NEXUS_VISUAL_GALLERY.md)** — Nexus itself, not just the public extracted repos.
4. **[Public Technical Reference v1.1](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)** — the full current public-safe technical reference.

![Nexus Synapse visual tour](https://drive.google.com/uc?export=view&id=1OM2jeCOqsgvPKtwLNkFtp2cLGchtY7BY)

*Animated Nexus system tour. It is an orientation aid, not a literal runtime trace.*

---

## Public technical reference: source of truth

The **version-controlled Markdown file in this repository is the canonical public technical reference**:

- **Canonical source:** [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- **Rendered distribution copy:** [PDF in the Nexus Synapse Research Library / Drive](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view)

The current reference was reconciled against an **August 14, 2026 read-only inspection of the deployed production implementation and state**. Older July execution evidence remains useful, but is labeled as isolated production-target execution rather than silently treated as a current live-production trace.

The change-control rule is simple: **Markdown first, PDF second.** Architectural claim changes should be diffable in repository history before a new rendered export is published.

---

## Why this portfolio exists

The private Nexus runtime is large enough that publishing a sanitized copy would create a different problem:

> **What exactly is the public code supposed to demonstrate?**

Instead, I publish **bounded public proof surfaces from a private runtime**.

```text
private parent runtime
        ↓
identify one architectural claim
        ↓
extract the smallest useful public surface
        ↓
state what it demonstrates
        ↓
state what it does NOT demonstrate
        ↓
test that surface independently
```

These artifacts are not fragments that combine to recreate Nexus. Each is a bounded public surface intended to make one architectural idea inspectable.

## Public project map

| Artifact | What it demonstrates | What it is not |
|---|---|---|
| [**Nexus Proof Runtime**](https://github.com/ChrisCanadian/nexus-proof-runtime) | Authorization → execution → receipt/artifact → claim verification | Not the private Nexus conversation runtime, memory system, or production tool path |
| [**Live Runtime Acceptance Rig**](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Exercise a real boundary and check durable effects instead of trusting narration | Not a Nexus subsystem or whole-system certification framework |
| [**Nexus Mode Card Creator**](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Fuzzy behavioral intent → guided authoring → human confirmation → portable profile | Does not expose mode activation, weighting, persistence, identity composition, or private SSR integration |
| [**Early SSR / warehouse-style RAG gist**](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752) | Historical SQL-guided narrowing before semantic ranking | Not the current SSR implementation |
| [**Nexus Synapse Research Library**](https://sites.google.com/view/nexus-synapse-research-library/home) | Longer-form architecture, research, history, and evaluation material | Not production source code |

---

## Current SSR terminology

In current portfolio documentation, **SSR means Structured State Reconstruction**.

At a public-safe level, SSR is the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. That can include identity/profile state, gauges, mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

Earlier Nexus documents used `SSR` in several related ways. One important historical ancestor used structured/SQL filtering to narrow memory candidates before semantic ranking. Those earlier meanings remain part of the engineering history, but they are not the default current expansion.

See the [Glossary](docs/GLOSSARY.md) for the terminology trail.

---

## Evidence discipline

A recurring engineering principle in Nexus is:

> **A model statement is not evidence that an external action occurred.**

That leads to a deliberate separation:

```text
proposal
   ≠
authority
   ≠
execution
   ≠
evidence
   ≠
narration
```

The portfolio uses evidence labels because code presence is not automatically a live-system claim.

| Label | Meaning |
|---|---|
| **IMPLEMENTED** | Concrete executable code/schema materially represents the responsibility |
| **TESTED** | Assertion-bearing tests, retained runs, benchmarks, or audits support the claim |
| **DOCUMENTED / PLANNED** | The design is documented but evidence is insufficient for implemented/tested |
| **ARCHIVED / SUPERSEDED** | The path existed but was replaced, disabled, or is no longer authoritative |
| **LINEAGE-INFERRED** | The relationship was reconstructed across sources rather than stated contemporaneously |

![Nexus evidence-strength dashboard](https://drive.google.com/uc?export=view&id=1t_iO2oe8ZaH7BCGQwrX35v0pcVliOXxr)

*Visual orientation only. The version-controlled evidence pages remain authoritative if a visual and current text ever disagree.*

For the specific distinction between deployed inspection, isolated execution, public proof, and historical/reconstructed evidence, see **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)** and **[Sanitized Evidence Receipts](evidence/SANITIZED_EVIDENCE_RECEIPTS.md)**.

---

## Architectural evolution

Nexus did not evolve through one clean sequence of perfectly named product releases. Production, recovery, reconstruction, and proof work sometimes moved in parallel.

The strongest through-line is simpler:

> **Responsibility progressively moved out of the language model and into explicit runtime systems whose state and behavior could be inspected, persisted, challenged, and tested.**

![Nexus architectural evolution timeline](https://drive.google.com/uc?export=view&id=16Ir4bMmUlz7Rqkrj5hT1r3HjeyWlMRfo)

*Chronological/architectural synthesis, not a literal current production deployment graph.*

Read the deeper history in [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md).

---

## Public / private boundary

This repository is designed to explain Nexus **without making the private runtime reproducible**.

Public material may include high-level architecture, historical design artifacts, public-safe diagrams, evidence categories, sanitized case studies, bounded reference implementations, and public benchmarks where the test conditions can be explained.

Intentionally excluded:

- production database schemas/table structures;
- exact production SQL/query patterns;
- raw SSR contents, ordering, thresholds, selection rules, and weighting logic;
- private prompts and identity-composition mechanics;
- production tool wiring/internal APIs;
- deployment scripts, environment configuration, infrastructure paths, and runbooks;
- credentials, secrets, private endpoints, customer configuration, or user data;
- production conversations, memories, reflections, raw traces, or private logs.

See [`PUBLIC_BOUNDARY.md`](PUBLIC_BOUNDARY.md).

---

## About me

I am **Christopher Campbell**, an independent AI systems builder and logistics analyst based in Ontario, Canada. My professional background is logistics, warehouse/operations systems, SQL, ERP workflows, process improvement, quality thinking, and automation rather than computer science.

My path into this work looks roughly like this:

```text
warehouse / shipping operations
        ↓
ERP + SQL + process automation
        ↓
systems and quality thinking
        ↓
AI-assisted Python development
        ↓
Nexus Synapse
```

AI coding tools have been implementation partners for syntax, debugging, review, and exploration. The architecture, problem selection, operating concepts, acceptance criteria, and system-level decisions are the work documented here.

Nexus is my first Python project.

More: [`ABOUT_CHRIS.md`](ABOUT_CHRIS.md)

---

## Recommended reading order

1. [`docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md`](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)
2. [`docs/PRODUCTION_EVIDENCE_STATUS.md`](docs/PRODUCTION_EVIDENCE_STATUS.md)
3. [`docs/NEXUS_VISUAL_GALLERY.md`](docs/NEXUS_VISUAL_GALLERY.md)
4. [`docs/NEXUS_OVERVIEW.md`](docs/NEXUS_OVERVIEW.md)
5. [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
6. [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md)
7. [`docs/VERIFICATION_AND_EVIDENCE.md`](docs/VERIFICATION_AND_EVIDENCE.md)
8. [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
9. [`case-studies/`](case-studies/)
10. [`docs/GLOSSARY.md`](docs/GLOSSARY.md)
11. [`evidence/claims-and-evidence.json`](evidence/claims-and-evidence.json)

---

## What I am not claiming

This portfolio does **not** claim:

- AGI or consciousness;
- that every historical Nexus subsystem is still active;
- that every implemented subsystem is fully tested;
- independent certification of the private runtime;
- that isolated V5 reconstruction work is automatically the accepted production path;
- that the public Proof Runtime or Acceptance Rig reproduces the private parent system;
- that public artifacts are complete representations of Nexus Synapse;
- that receipt/hash verification establishes semantic truth;
- that Nexus invented memory, RAG, tool use, agent frameworks, or context engineering.

The point is narrower:

**document the architecture I built, show how it evolved, publish inspectable pieces where appropriate, and attach claims to the strongest evidence I actually have.**

---

## Research and public artifacts

- [Nexus Synapse Research Library](https://sites.google.com/view/nexus-synapse-research-library/home)
- [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime)
- [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig)
- [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator)
- [Historical SSR gist](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752)
- [Christopher Campbell on GitHub](https://github.com/ChrisCanadian)

---

## Status

This portfolio is a living engineering record.

Where current evidence changes, the intended practice is to update the **evidence label first**, then update the claim.

**Architecture can evolve. Evidence should remain traceable.**
