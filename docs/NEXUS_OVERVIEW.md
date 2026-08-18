# Nexus Synapse — Overview

## The core idea in plain English

Nexus Synapse started as a personalized AI assistant and evolved into a runtime around replaceable language models.

The easiest way to understand the project is to start with a familiar systems idea:

> **Do not make one worker carry the entire operating environment in their head.**

Real work is supported by state, history, procedures, permissions, tools, approvals, handoffs, corrections, and evidence. Nexus applies that same responsibility-first thinking around model inference.

The language model can interpret, reason, propose, and communicate. The surrounding runtime is responsible for deciding what context is eligible, what authority exists, what actions are allowed, what should persist, and what evidence supports a consequential claim.

That is the practical meaning behind:

> **The model is not the system.**

If you come from operations, manufacturing, logistics, quality, healthcare, finance, legal, research, or another specialized field, start with [Nexus Synapse for Domain Experts](DOMAIN_EXPERT_ORIENTATION.md).

## The engineering definition

Nexus Synapse is a **state-conditioned, policy-bearing LLM orchestration and continuity runtime**.

The central design idea is:

> **The model should propose and synthesize, while the runtime selects context, governs consequences, persists identity and continuity, and verifies what actually happened.**

This separation makes the system more inspectable and testable without requiring the language model to be the durable owner of the surrounding system.

## Why this matters

In Nexus, responsibilities that are often left implicit in model behavior are increasingly represented as explicit runtime responsibilities:

- identity and continuity live in persistent state rather than only in a prompt;
- memory selection is a runtime responsibility with scoped boundaries;
- tools and actions are authorized, executed, and recorded outside the model;
- evidence such as receipts, artifacts, and logs supports completion claims;
- testing and verification are treated as part of the architecture.

The language model remains important for generation, interpretation, and some analysis. It does not own authentication, trusted user scope, durable persistence, tool authorization, or post-generation verification.

For a domain reader, that can be translated more simply:

- **history is not the same as current state;**
- **access is not the same as authority;**
- **a recommendation is not the same as an executed action;**
- **a statement that work completed is not the same as evidence that it completed.**

## Current high-level model

At a sanitized level, a turn can be described as:

```text
authenticated request
        ↓
analysis and focus signals
        ↓
memory selection and fallback
        ↓
prompt/context assembly
(identity, preferences, capabilities, context)
        ↓
optional advisory cognition
        ↓
provider routing
        ↓
optional governed tool execution
        ↓
response
        ↓
deterministic guards
        ↓
background persistence and learning
```

This diagram is intentionally high level. The public portfolio does not disclose the private production call graph, exact subsystem interfaces, retrieval rules, or deployment configuration.

![Governance lineage and runtime critique](https://drive.google.com/uc?export=view&id=1iqL3Gjzn6ljr1nto5KRbW5EHL9Mr6Om6)

*Public conceptual synthesis of the shift toward explicit runtime oversight. It should not be read as a literal current deployment graph or a claim that every illustrated lane is active on every turn.*

## The seven public repositories

The private Nexus runtime is not published. Instead, seven bounded repositories expose selected engineering responsibilities and historical lineage:

| Repository | Plain-language problem |
|---|---|
| [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) | Do not let an AI's statement that something happened count as proof that it happened. |
| [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Test the real target and durable effect, not just whether a test script returned success. |
| [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Turn desired AI behavior into a reusable profile without confusing behavior with authority. |
| [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Make memory scoped, correctable, traceable, and persistent rather than simply "remember everything." |
| [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Let outsiders challenge a closed runtime without publishing the private implementation. |
| [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Let model/provider transport change without rebuilding the surrounding application. |
| [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime) | Run an evidence-constrained reconstruction of the flat-file runtime that preceded Nexus. |

For the formal evidence status and claim ceiling of each repository, see the [Repository Map](REPOSITORY_MAP.md).

## How it evolved

The architecture did not emerge as a clean formal `V1 → V5` product-release sequence.

It evolved through overlapping epochs in which production continuity, reconstruction work, proof projects, and verification work sometimes proceeded in parallel.

The named public epochs are:

1. **Epoch A — ChrisAI bootstrap (Aug–Sep 2025)**
2. **Epoch B — Engine2_1 subsystem expansion (Sep–Oct 2025)**
3. **Epoch C — Original SSR and retrieval (Nov–Dec 2025)**
4. **Epoch D — SSR_Minimal extraction (Jan 2026)**
5. **Epoch E — Dyad cognitive state (Feb 2026)**
6. **Epoch F — Senate and Thinker (Mar–Apr 2026)**
7. **Epoch G — Production continuity and recovery (Apr–May 2026)**
8. **Epoch H — Isolated V5 reconstruction (Jul–Aug 2026)**
9. **Epoch I — Proof and acceptance (Jul–Aug 2026)**

Across those epochs, the same pattern repeats:

1. A responsibility starts as implicit model behavior.
2. It becomes explicit runtime state or service.
3. It is scoped, tested, and governed.
4. Evidence is required to support claims about it.

That through-line is more important than any one component name.

## SSR in the larger picture

For current portfolio documentation, **SSR means Structured State Reconstruction**.

At a public-safe level, SSR is the runtime responsibility that reconstructs a bounded operating context before inference from eligible identity/profile state, gauges, modes, rules, learned preferences, continuity/memory, reflection context, tool/capability facts, and optional advisory input.

In domain language, the closest analogy is not "give the worker the whole warehouse." It is **stage the right material, instructions, and state for the current job**.

Earlier project documents used `SSR` in several related ways, including retrieval-oriented terminology. One important historical ancestor used structured filtering/scoping before semantic ranking. The [Glossary](GLOSSARY.md) preserves that terminology drift without making the historical expansions the current definition.

Not every SSR path implies active vector search.

## Public versus private

This portfolio explains architecture and publishes bounded evidence surfaces.

It intentionally does not expose:

- private schemas or exact retrieval logic;
- exact activation/weighting rules;
- internal APIs;
- deployment details;
- credentials or private runtime data.

See [PUBLIC_BOUNDARY.md](../PUBLIC_BOUNDARY.md).

## Full technical reference

For the current responsibility-level architecture, deployed-state corrections, and explicit evidence ceiling, see:

- [Public Technical Reference v1.1 — canonical Markdown](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- [Public Technical Reference v1.1 — rendered PDF](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view)

The reference distinguishes the August 14, 2026 deployed-code/read-only-state audit from older isolated execution receipts.

## Continue reading

### Domain / operations readers

- [Nexus Synapse for Domain Experts](DOMAIN_EXPERT_ORIENTATION.md)
- [Visual Gallery](NEXUS_VISUAL_GALLERY.md)
- [Repository Map](REPOSITORY_MAP.md)
- [Architectural Evolution](ARCHITECTURAL_EVOLUTION.md)
- [Verification and Evidence](VERIFICATION_AND_EVIDENCE.md)

### AI / software / systems readers

- [Current Production Responsibilities](CURRENT_PRODUCTION_RESPONSIBILITIES.md)
- [Nexus Terminology → Conventional Systems Concepts](NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)
- [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md)
- [Public Technical Reference v1.1](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- [Glossary](GLOSSARY.md)
