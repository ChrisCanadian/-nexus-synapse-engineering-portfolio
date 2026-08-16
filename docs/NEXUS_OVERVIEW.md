# Nexus Synapse — Overview

## The core idea

Nexus Synapse started as a personalized AI assistant and evolved into a **state-conditioned, policy-bearing LLM orchestration runtime**.

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

SSR has had multiple meanings during the project's history.

For public communication:

- **SSR retrieval method** refers to structured filtering/scoping before semantic ranking.
- **SSR runtime/prompt family** refers more broadly to the machinery that assembles identity, preferences, capabilities, tools, memory, and context for generation.

Not every historical use of `SSR` implies active vector search. The glossary preserves those distinctions.

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

- [Public Technical Reference v1.1 (PDF)](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view)
- [Public Technical Reference v1.1 (Markdown)](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)

The reference distinguishes the August 14, 2026 deployed-code/read-only-state audit from older isolated execution receipts.

## Continue reading

- [Architectural Evolution](ARCHITECTURAL_EVOLUTION.md)
- [Verification and Evidence](VERIFICATION_AND_EVIDENCE.md)
- [Repository Map](REPOSITORY_MAP.md)
- [Glossary](GLOSSARY.md)
