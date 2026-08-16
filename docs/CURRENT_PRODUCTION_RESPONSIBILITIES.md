# Current Production Responsibilities — Two-Minute Orientation

This page is the shortest public-safe orientation to the **current deployed Nexus responsibility chain**.

It intentionally avoids the project's historical vocabulary unless the term still helps explain the active responsibility. For implementation detail and evidence limits, use the [Public Technical Reference v1.1](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md).

> **The model performs inference. The runtime owns the continuity, boundaries, capabilities, and durable state around that inference.**

## Primary responsibility chain

```text
authenticated request
        ↓
1. resolve user / session / scope
        ↓
2. analyze the current request
        ↓
3. select eligible continuity + memory
        ↓
4. reconstruct bounded operating context
        ↓
5. apply profile / behavioral configuration / rules
        ↓
6. route to an eligible model/provider
        ↓
7. authorize + execute tools when required
        ↓
8. run deterministic post-generation checks
        ↓
9. persist permitted state / summaries / adaptation
        ↓
response
```

Not every optional subsystem participates in every turn.

## Responsibility ownership

| Responsibility | Primary owner | Public-safe current-state note |
|---|---|---|
| Authentication / trusted scope | Runtime | Normal authenticated path is runtime-owned |
| Session continuity | Runtime | Persistent conversation/session state is external to model weights |
| Request analysis | Runtime services | Current deployed analysis can use external inference and degrades to static fallback; the older local NLP path is not the active production analyzer |
| Memory eligibility / selection | Runtime | Relational memory is current; semantic/vector recall is conditional and was stale/degraded in the August 14 audit |
| Context reconstruction | Runtime / SSR V2 | Current and behaviorally consequential |
| Profile, gauges, modes, rules, learned preferences | Runtime state | Current populated state conditions later model context |
| Model inference | Selected LLM/provider | The selected model generates inside the prepared runtime context |
| Tool proposal | Model | Proposal is not authority |
| Tool visibility / authorization / dispatch | Runtime | Runtime decides which tools are visible, allowed, executed, and returned |
| Optional Senate / advisory cognition | Runtime-orchestrated models | Conditional advisory context; not execution authority |
| Reflection context | Runtime state | Current and populated |
| Self-model projection | Runtime state | Omitted in the August 14 audited main path because of a storage-contract mismatch |
| Post-generation guards | Runtime | Deterministic truth / hallucination checks follow generation |
| Interaction + summary persistence | Runtime | Current |
| Learned-preference adaptation | Runtime | Persisted and later consumed by SSR V2 |
| Thinker / higher-order background cognition | Optional subsystem | Not proven as part of the current main deployed turn path |

## SSR: current canonical meaning

In current portfolio documentation, **SSR means Structured State Reconstruction**.

Earlier project documents used the acronym differently while the architecture was evolving. Those historical meanings are preserved in the [Glossary](GLOSSARY.md), but they are not the default meaning for current architecture claims.

At the current public-safe level, SSR is the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. That can include identity/profile data, gauges, mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

## Optional / supporting systems

Systems such as Senate, cognitive-node scoring, reflection, and other conditional services may contribute context or critique. They are **supporting runtime services**, not prerequisites for understanding the main responsibility chain above, and they should not be assumed active on every turn.

## What this page does not claim

This one-pager does **not** claim:

- that every historical subsystem is currently active;
- that every responsibility above has equal evidence strength;
- that one retained audit proves the whole production runtime end to end;
- that the public artifacts reproduce the private parent runtime;
- that implementation presence alone establishes current behavioral activation.

For the evidence boundary, continue with [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md).
