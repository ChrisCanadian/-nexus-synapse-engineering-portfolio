# Sanitized Evidence Receipts

Raw terminal logs are not the public artifact of record for Nexus Synapse.

Operational output can contain identifiers, environment details, provider/profile information, private state, or implementation detail that crosses the public boundary. This page preserves the **structure of the evidence** without publishing the raw operational dump.

## Receipt 001 — Historical three-tier benchmark

```text
receipt_id: BENCH-2026-02-14
artifact: benchmark_3tier_20260214_163657.json
target: historical SSR_Minimal runtime benchmark
mode: retained benchmark packet
scope: 60 prompts across the recorded three-tier comparison
result: completed 60 / 60 prompts
evidence_class: TESTED / HISTORICAL
```

**Supports:** a retained benchmark run with prompt-level latency/output data exists.

**Does not support:** present-day production behavior, independent quality scoring, or current model/provider parity.

## Receipt 002 — July 11 isolated production-target execution

```text
receipt_id: PROD-TARGET-2026-07-11
target: isolated production-target runtime
mode: controlled execution against copied / redirected state
scope:
  - route/session handling
  - request analysis
  - focus/node stages
  - SSR V2 construction
  - associative recall
  - distributed cognition / Senate
  - provider routing
  - selected memory-tool execution
result: selected path exercised; not full production certification
evidence_class: TESTED / ISOLATED
```

**Supports:** selected runtime stages were executed together under a controlled production-target setup.

**Does not support:** that the exact same trace ran on the live production VM, that every tool class was exercised, or that every post-turn write was established.

## Receipt 003 — August 14 deployed production inspection

```text
receipt_id: PROD-INSPECT-2026-08-14
target: deployed production Python + production state
mode: read-only inspection
scope:
  - active/degraded/omitted path inspection
  - SSR/state readers
  - relational memory/adaptation state
  - tool registry / authority surfaces
  - conditional Senate wiring
  - reflection context
  - analysis fallback behavior
  - disconnected / stale mechanisms
result: current-state implementation and data-path status classified
writes_performed: none
evidence_class: IMPLEMENTED / PRODUCTION-INSPECTED
```

**Supports:** current deployed code/state was inspected deeply enough to classify important responsibilities as current, conditional, degraded, omitted, stale, or disconnected.

**Does not support:** a behavior-triggering live-production end-to-end execution, independent certification, or universal correctness.

## Receipt 004 — Bounded public proof surfaces

```text
receipt_id: PUBLIC-PROOF-FAMILY-2026
artifacts:
  - nexus-proof-runtime
  - Live-Runtime-Acceptance-Rig
  - nexus-mode-card-creator
mode: standalone public reference / validation surfaces
result: bounded architectural claims made inspectable outside the private parent runtime
evidence_class: PUBLIC-BOUNDARY / REFERENCE
```

**Supports:** individual architectural principles can be inspected and exercised independently.

**Does not support:** that the public projects combine to reconstruct or certify Nexus Synapse.

---

## Preferred future receipt shape

```text
receipt_id:
date:
target:
mode:
commit_or_build:
checks_performed:
result:
evidence_class:
artifacts_or_hashes:
redactions:
non_claims:
```

This format is deliberately more useful than a screenshot of a terminal window: it makes the **claim boundary** part of the receipt.
