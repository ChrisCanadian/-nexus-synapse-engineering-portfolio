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

## Receipt 004 — Bounded public proof / reference surfaces

```text
receipt_id: PUBLIC-PROOF-FAMILY-2026
artifacts:
  - nexus-proof-runtime
  - Live-Runtime-Acceptance-Rig
  - nexus-mode-card-creator
  - Nexus-Memory-Kernel
  - nexus-blackbox-validation-gateway
  - OpenAI-compatible-router
mode: standalone public reference / validation / infrastructure surfaces
result: bounded architectural and validation claims made inspectable outside the private parent runtime
evidence_class: PUBLIC-BOUNDARY / REFERENCE
```

**Supports:** individual architectural principles, validation contracts, and reusable infrastructure can be inspected and exercised independently.

**Does not support:** that the public projects combine to reconstruct or certify Nexus Synapse.

## Receipt 005 — Black-box validation v0.2 integration candidate

```text
receipt_id: BLACKBOX-INTEGRATION-2026-08-17
public_gateway:
  commit: 98d0c1129d675beebaede037a3c0589da3487785
  ci_run: 32024629336
  result: success
public_router:
  commit: 3558c34a4ae81f408d0a626681262b7723a95c13
  ci_run: 32024613947
  result: success
private_target_candidate:
  commit: 4b436dedb0c4487959547db16d71baec9f045f17
  ci_run: 32025115767
  result: success
mode:
  - public gateway/router release verification
  - private validation-target isolated integration verification
checks_performed:
  - evaluator-authored challenge contract / schema
  - built-in nexus-blackbox-core-v1 suite behavior
  - public evidence / metadata boundary
  - BYO provider route isolation + usage readback
  - private target contract integration in isolated CI
result: integration path implemented and isolated-tested; no retained deployed-target campaign yet
evidence_class: TESTED / INTEGRATION-CANDIDATE
```

**Supports:** the public challenge/transport stack is released and tested at v0.2, and the private Nexus validation-target candidate has separate isolated CI evidence.

**Does not support:** that deployed Nexus has passed the challenge suite, that a production-facing synthetic campaign had been retained as of this August 17 receipt, that model-swap parity is established across deployed Nexus, or that an independent third party has certified the private runtime.

**Subsequent status:** Receipt 006 records the August 18 deployed-target campaign. Its fixed-invariant result failed.

---

## Receipt 006 — August 18 deployed-target fixed-invariant campaign

```text
receipt_id: BLACKBOX-DEPLOYED-TARGET-2026-08-18
target: existing Nexus deployment through private validation-target integration
mode:
  - deterministic fixed-invariant reproduction
  - separate unseen challenge
fixed_invariant_result: FAIL
passing_mechanism_checks:
  - deterministic, distinct, correctly tagged session mappings
  - six of six persistence barriers observed
  - expected interactions and summaries existed before the following turn
failed_invariants:
  - cross-conversation continuity
  - correction persistence
separate_unseen_challenge: PASS
artifacts_retained_privately:
  - name: nexus-failed-invariants-reproduction-20260818.json
    sha256: 1971125c40f8588d63c50533fffb59538ac19646f35444c25db9a9a2dda4e455
  - name: nexus-failed-invariants-root-cause-20260818.md
    sha256: cc9f8c10e6d080f151e0e3f8e31556921a048d9c50bd11b4f6c96bac48ea4da1
evidence_class: TESTED / DEPLOYED-TARGET / FAILED-INVARIANTS
```

**Root-cause finding:** cross-conversation wording invoked `keyword_memory_search`; the validation tool allowlist blocked that tool, and the unavailable tool result outranked populated all-session CAG. Correction persistence failed because extractive summarization retained the obsolete statement but dropped the replacement marker. The unseen case avoided the blocked tool path and placed its replacement in the first sentence, so it passed through CAG.

**Supports:** the validation path reached the existing deployment; mappings and persistence timing were deterministic; the two fixed-invariant failures were reproducible; the separate unseen case exercised the evaluator route and all-session CAG behavior.

**Does not support:** that the fixed suite passed, that deployed Nexus satisfies cross-conversation continuity or correction persistence, that the unseen pass overrides the fixed failures, controlled model-swap parity, or independent certification.

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
