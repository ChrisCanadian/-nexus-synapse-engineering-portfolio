# Case Study — Black-Box Validation Gateway + BYO Model Router

## Public artifacts

- [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway)
- [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router)

## The engineering problem

The private Nexus runtime can be inspected internally, but publishing its construction logic would undermine the public/private boundary the portfolio is meant to preserve.

That creates a validation problem:

> **How can an outside evaluator challenge selected runtime claims without receiving the private runtime, its composition graph, its schemas, or its internal state-selection logic?**

The answer is to separate the **challenge boundary** from the **implementation boundary**.

```text
evaluator
    ↓
public challenge contract
    ↓
opaque private target
    ↓
observable result / effect
    ↓
sanitary evidence envelope
```

The evaluator should be able to control the challenge and observe the result without being given the machinery that produced it.

## Why two repositories?

The validation gateway and model router are deliberately separate responsibilities.

### Nexus Black-Box Validation Gateway

The gateway owns the public validation contract:

- short-lived validation sandboxes;
- BYO OpenAI-compatible provider handoff;
- supported public artifact submission such as `mode-card.v1`;
- opaque target forwarding;
- sanitized run/evidence envelopes;
- challenge-runner support;
- application kill switch and access controls.

It does not reproduce Nexus and does not publish the private adapter that translates a challenge into private runtime behavior.

### OpenAI-compatible Router

The router owns generic inference transport:

- ephemeral in-memory provider routes;
- per-route API keys;
- model locking;
- OpenAI-compatible chat completions;
- streaming SSE;
- tools / tool-calls pass-through;
- `/v1/models` compatibility;
- route expiry/deletion and completion ceilings;
- outbound SSRF protection;
- secret-safe failure behavior.

It contains no Nexus-specific memory, identity, SSR, authority, behavioral-state, entitlement, or composition logic.

That separation makes the router recyclable. The validation gateway can use it, but future software can use the same provider transport without inheriting Nexus concepts.

## Relationship to the existing public artifacts

The gateway gives the existing public Nexus artifacts a common validation boundary without making them modules of a public Nexus clone.

```text
Mode Card Creator ───────┐
Memory Kernel ───────────┤
Proof Runtime ───────────┼── public contracts / evidence ideas
Acceptance Rig ──────────┘
              ↓
Black-Box Validation Gateway
              ↓
opaque private target
```

The relationship is contractual, not reconstructive.

For example, the Mode Card Creator can produce a public artifact accepted by the gateway while the private target remains solely responsible for how that artifact is interpreted or applied. Likewise, Memory Kernel concepts can inspire observable challenge invariants without exposing private Nexus memory-selection or SSR-composition logic.

## Why BYO inference matters

The evaluator can supply an OpenAI-compatible model/provider instead of relying on a model chosen or funded by the Nexus operator.

That supports a stronger future test of the thesis:

> **The model is not the system.**

If runtime-owned invariants survive controlled model substitution, the evaluator has evidence that those invariants are not merely properties of one selected generator.

The public router is infrastructure for that experiment. It does not by itself demonstrate Nexus model-substitution parity.

## What the public tests establish

The v0.1.0 gateway and router repositories have their own automated suites and GitHub CI.

The gateway tests cover the public challenge surface, artifact handling, evidence sanitation, access/kill-switch behavior, and challenge execution against an opaque test target.

The router tests cover route isolation, model locking, OpenAI-compatible request forwarding, streaming, tool-call pass-through, route lifecycle behavior, SSRF protection, and secret-safe error handling.

Publication CI passed on Python 3.11–3.13 for both repositories.

## Current claim ceiling

This is the most important part.

The public gateway currently supports the claim:

> **A public-safe black-box validation surface can be implemented and tested without publishing the target runtime's private composition logic.**

The router currently supports the claim:

> **BYO OpenAI-compatible model transport can be isolated into a reusable, provider-facing component without embedding Nexus-specific runtime logic.**

They do **not yet** establish:

- that the gateway has challenged the current production Nexus runtime;
- that a production-facing synthetic Nexus tenant is live;
- that external evaluators have authored and executed independent Nexus challenge packs;
- controlled model-swap parity across the real private runtime;
- whole-system certification;
- any private Nexus implementation detail.

Those stronger claims require an actual private adapter/tenant connection and retained black-box challenge runs.

## Why this belongs in the portfolio

Earlier public projects made individual architectural responsibilities inspectable. This pair adds a different capability: a path for outsiders to test selected claims **against an opaque private target** rather than only reviewing bounded public analogues.

That moves the public strategy from:

```text
explain a claim
→ publish a bounded artifact
→ let outsiders inspect the artifact
```

one step closer to:

```text
publish the challenge contract
→ let outsiders author the challenge
→ execute against the private target
→ retain observable evidence
```

The private runtime still does not need to become a reconstruction kit.

See also:

- [Production Evidence Status](../docs/PRODUCTION_EVIDENCE_STATUS.md)
- [Public Repository and Artifact Map](../docs/REPOSITORY_MAP.md)
- [Public Boundary](../PUBLIC_BOUNDARY.md)
- [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig)
