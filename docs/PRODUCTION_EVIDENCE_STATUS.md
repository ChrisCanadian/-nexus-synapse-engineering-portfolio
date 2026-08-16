# Production Evidence Status

This page answers the evidence question the portfolio is designed to make visible:

> **How much of the current production path has been directly inspected or exercised, and how much is reconstructed, isolated, historical, or only documented?**

The answer is intentionally mixed. That is the point of the evidence labels.

## Evidence classes used here

### A. Deployed production inspection

Evidence obtained by inspecting the **actual deployed implementation and current production state**.

The strongest current example is the **August 14, 2026 read-only production audit**. It inspected deployed Python and production state without performing production writes or behavior-triggering requests.

This can establish what is wired, populated, degraded, omitted, conditional, or disconnected in the deployed system. It is **not the same thing as an end-to-end live execution trace**.

### B. Isolated production-target execution

Evidence from a controlled execution path using copied / redirected production-target state rather than the live production VM.

The key retained example is the **July 11, 2026 isolated production-target trace**. It exercised selected route/session handling, analysis, focus/node stages, SSR V2, associative recall, distributed cognition, Senate, provider routing, and memory-tool execution.

This is real execution evidence, but it should not be silently promoted into a claim that the exact same path was executed on the live VM at a later date.

### C. Bounded public proof

Standalone public artifacts exercise one architectural claim in a smaller inspectable system.

Examples:

- Nexus Proof Runtime;
- Live Runtime Acceptance Rig;
- Nexus Mode Card Creator.

These are useful because the claim boundary is explicit. They are **not fragments that combine to recreate or certify the private parent runtime**.

### D. Historical / reconstruction / design evidence

Older source, retained benchmarks, isolated V5 work, architecture documents, and lineage reconstruction help establish implementation history and architectural intent.

They are valuable, but weaker for claims about **current deployed behavior** unless a newer production-facing source confirms the same path.

## Current production responsibility matrix

| Area | Strongest retained public-safe evidence | Current defensible status |
|---|---|---|
| Authenticated runtime architecture | Aug 14 deployed-code inspection | Normal authenticated path identified; current architecture inspected |
| SSR V2 context construction | Aug 14 deployed-code/state inspection + Jul 11 isolated execution | Current and behaviorally consequential |
| Profile, gauges, mode, user rules, learned preferences | Aug 14 production-state inspection | Current / populated |
| Relational interaction + summary memory | Aug 14 production-state inspection | Current / populated |
| Session-local continuity / CAG | Aug 14 production-state inspection | Current, with observed broader-summary fallback in the latest audited session |
| Semantic/vector conversation memory | Aug 14 production-state inspection | Implemented but stale/reference-degraded in the audited state |
| Request analysis | Aug 14 deployed-code inspection | Current via external inference or static fallback; historical local NLP path not active |
| Focus + cognitive-node scoring | Aug 14 deployed-code inspection | Current; node-persistence hooks disconnected |
| Distributed cognition / Senate | Aug 14 deployed-code inspection + Jul 11 isolated execution | Current conditional advisory |
| Reflections | Aug 14 production-state inspection | Current / populated |
| Self-model projection | Aug 14 deployed-code/state inspection | Omitted in the audited current path |
| Tool registry / authority mediation | Aug 14 deployed-code/state inspection + Jul 11 memory-tool execution | Current; model proposal remains separate from runtime authority |
| Interaction / summary persistence | Aug 14 deployed-code/state inspection | Current |
| Learned-preference adaptation | Aug 14 production-state inspection | Current and later consumed by SSR V2 |
| Direct-feedback downstream effect | Aug 14 inspection | Persisted, but next-turn effect through the active SSR path not proven |
| Goals / curiosity / injectable background cognition | Aug 14 inspection | Empty or disconnected in the audited state |
| Thinker | Aug 14 deployed-code inspection | Not proven in the current main deployed path |
| Controlled primary-model swap parity | Public evidence set | Not demonstrated |
| Independent third-party replication | Public evidence set | Not demonstrated |

## What is actually strongest today?

The most defensible current-production claim is **not** “the entire runtime has been independently exercised end to end.”

It is narrower:

> **The actual deployed implementation and state have been inspected deeply enough to distinguish current, degraded, disconnected, omitted, and conditional responsibilities; selected runtime behaviors have separate isolated execution evidence; bounded public projects independently exercise narrower architectural claims.**

That is a stronger claim than a diagram or self-description, and a weaker claim than full independent live-production certification.

## Why the raw terminal dump is not the publication artifact

Raw operational logs can contain internal identifiers, environment details, profile state, provider details, or subsystem information that crosses the public boundary.

For public use, this repository therefore favors **sanitized structural receipts** that preserve:

- target and date;
- inspection or execution mode;
- checks performed;
- evidence class;
- pass / partial / not-demonstrated state;
- explicit non-claims.

See [`../evidence/SANITIZED_EVIDENCE_RECEIPTS.md`](../evidence/SANITIZED_EVIDENCE_RECEIPTS.md).

## Evidence-reading hierarchy

For claims about current Nexus behavior, prefer evidence in this order:

1. **Actual deployed production inspection / retained live-boundary evidence**
2. **Controlled isolated execution evidence tied to the production architecture**
3. **Bounded public proof artifacts**
4. **Retained deterministic tests / benchmarks / audits**
5. **Implementation present in source**
6. **Historical design documents / cross-source lineage reconstruction**

The lower categories are not “bad evidence.” They simply answer different questions.
