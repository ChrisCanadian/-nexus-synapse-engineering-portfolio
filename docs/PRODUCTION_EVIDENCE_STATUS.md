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

### C. Bounded public proof and validation infrastructure

Standalone public artifacts exercise one architectural claim or validation responsibility in a smaller inspectable system.

Examples:

- Nexus Proof Runtime;
- Live Runtime Acceptance Rig;
- Nexus Mode Card Creator;
- Nexus Memory Kernel;
- Nexus Black-Box Validation Gateway;
- OpenAI-compatible Router.

The first four expose bounded architectural responsibilities. The Black-Box Validation Gateway adds a public challenge surface for an opaque target, while the OpenAI-compatible Router provides generic BYO model transport for that validation path and other future uses.

These are useful because the claim boundary is explicit. They are **not fragments that combine to recreate or certify the private parent runtime**.

The v0.2 validation gateway now includes an evaluator-authored challenge schema, the built-in `nexus-blackbox-core-v1` suite, a metadata firewall, cleanup/revocation support, and independent observation of router usage. The v0.2 router adds request-scoped route credentials and secret-free usage readback while preserving route isolation, model locking, streaming, tool pass-through, SSRF protection, and secret-safe failure handling.

The private parent repository contains a dedicated validation-target integration with isolated tests and CI. A retained campaign was then executed against the existing deployment on August 18, 2026. The fixed-invariant outcome **failed** even though deterministic session mapping and all six persistence barriers were observed. Cross-conversation continuity failed when `keyword_memory_search` was blocked by the validation tool allowlist and its unavailable result outranked the populated all-session CAG. Correction persistence failed when extractive summarization retained the obsolete marker but dropped its replacement. A separate unseen challenge passed through all-session CAG when its wording avoided the blocked tool path and placed the replacement in the first sentence.

These mechanism-level observations and the separate unseen pass are useful diagnostic evidence. They do not convert the fixed-invariant campaign into a pass.

### D. Historical / reconstruction / design evidence

Older source, the public ChrisAI historical reconstruction, retained benchmarks, isolated V5 work, architecture documents, and lineage reconstruction help establish implementation history and architectural intent.

They are valuable, but weaker for claims about **current deployed behavior** unless a newer production-facing source confirms the same path.

## Current production responsibility matrix

| Area | Strongest retained public-safe evidence | Current defensible status |
|---|---|---|
| Authenticated runtime architecture | Aug 14 deployed-code inspection | Normal authenticated path identified; current architecture inspected |
| SSR V2 context construction | Aug 14 deployed-code/state inspection + Jul 11 isolated execution | Current and behaviorally consequential |
| Profile, gauges, mode, user rules, learned preferences | Aug 14 production-state inspection | Current / populated |
| Relational interaction + summary memory | Aug 14 production-state inspection | Current / populated |
| Session-local continuity / CAG | Aug 14 production-state inspection + Aug 18 deployed-target challenge | Current, with all-session fallback observed; fixed cross-conversation continuity failed when a blocked memory-tool result outranked populated CAG |
| Semantic/vector conversation memory | Aug 14 production-state inspection | Implemented but stale/reference-degraded in the audited state |
| Request analysis | Aug 14 deployed-code inspection | Current via external inference or static fallback; historical local NLP path not active |
| Focus + cognitive-node scoring | Aug 14 deployed-code inspection | Current; node-persistence hooks disconnected |
| Distributed cognition / Senate | Aug 14 deployed-code inspection + Jul 11 isolated execution | Current conditional advisory |
| Reflections | Aug 14 production-state inspection | Current / populated |
| Self-model projection | Aug 14 deployed-code/state inspection | Omitted in the audited current path |
| Tool registry / authority mediation | Aug 14 deployed-code/state inspection + Jul 11 memory-tool execution | Current; model proposal remains separate from runtime authority |
| Interaction / summary persistence | Aug 14 deployed-code/state inspection + Aug 18 deployed-target challenge | Session mappings and six persistence barriers passed; correction persistence still failed because extractive summarization dropped the replacement marker |
| Learned-preference adaptation | Aug 14 production-state inspection | Current and later consumed by SSR V2 |
| Direct-feedback downstream effect | Aug 14 inspection | Persisted, but next-turn effect through the active SSR path not proven |
| Goals / curiosity / injectable background cognition | Aug 14 inspection | Empty or disconnected in the audited state |
| Thinker | Aug 14 deployed-code inspection | Not proven in the current main deployed path |
| Public black-box validation surface | Black-Box Validation Gateway v0.2 + CI + Aug 18 campaign | Gateway remains implemented/tested standalone; the retained deployed-target fixed-invariant campaign failed, with a separate unseen challenge pass recorded only as a narrower result |
| Generic BYO model transport | OpenAI-compatible Router v0.2 + CI + Aug 18 provider observation | Implemented/tested standalone; provider counts advanced on unseen turns, but observed transport use does not establish model-swap parity or a Nexus validation pass |
| Private black-box target integration | Private integration CI + Aug 18 deployed-target campaign | Integration exercised against the existing deployment; fixed invariants failed, so the result is diagnostic deployed-target evidence, not acceptance |
| Controlled primary-model swap parity in Nexus | Public evidence set | Not demonstrated against the deployed private runtime |
| Independent third-party black-box validation of Nexus | Public evidence set | Operator-run deployed-target evidence exists; genuinely independent third-party validation is not demonstrated |
| Independent third-party replication | Public evidence set | Not demonstrated |

## What is actually strongest today?

The most defensible current-production claim is **not** “the entire runtime has been independently exercised end to end.”

It is narrower:

> **The actual deployed implementation and state have been inspected deeply enough to distinguish current, degraded, disconnected, omitted, and conditional responsibilities; selected runtime behaviors have separate isolated execution evidence; bounded public projects independently exercise narrower architectural claims.**

The newer black-box stack is now stronger than a standalone gateway mock: the public gateway and router are released/tested at v0.2, the private target integration has isolated CI evidence, and a retained August 18 campaign traversed the existing deployment. That campaign produced useful root-cause evidence but **did not pass** its fixed invariants. The separate unseen challenge pass is recorded without being promoted into suite success.

That is stronger evidence than a diagram or self-description and weaker than acceptance, model-swap parity, independent validation, or live-production certification.

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
3. **Externally authored black-box challenge evidence against a production-facing target**
4. **Bounded public proof artifacts and validation infrastructure**
5. **Retained deterministic tests / benchmarks / audits**
6. **Implementation present in source**
7. **Historical design documents / cross-source lineage reconstruction**

The lower categories are not “bad evidence.” They simply answer different questions.
