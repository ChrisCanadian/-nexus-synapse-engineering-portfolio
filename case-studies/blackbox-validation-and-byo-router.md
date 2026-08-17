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

The v0.2 gateway owns the public validation contract:

- short-lived validation sandboxes;
- BYO OpenAI-compatible provider handoff;
- supported public artifact submission such as `mode-card.v1`;
- opaque target forwarding;
- sanitized run/evidence envelopes;
- a hard metadata firewall between private target and public evidence;
- a machine-readable challenge schema for evaluator-authored tests;
- the built-in `nexus-blackbox-core-v1` suite;
- independent router-usage verification;
- cleanup/revocation support;
- application kill switch and access controls.

It does not reproduce Nexus and does not publish the private adapter that translates a challenge into private runtime behavior.

### OpenAI-compatible Router

The v0.2 router owns generic inference transport:

- ephemeral in-memory provider routes;
- per-route API keys;
- model locking;
- OpenAI-compatible chat completions;
- streaming SSE;
- tools / tool-calls pass-through;
- `/v1/models` compatibility;
- route expiry/deletion and completion ceilings;
- outbound SSRF protection;
- secret-safe failure behavior;
- request-scoped route credentials compatible with ordinary OpenAI-style bearer use;
- secret-free usage readback so the validation layer can verify that evaluator-owned provider traffic actually traversed the router.

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

That supports a stronger test of the thesis:

> **The model is not the system.**

If runtime-owned invariants survive controlled model substitution, the evaluator has evidence that those invariants are not merely properties of one selected generator.

The public router is infrastructure for that experiment. It does not by itself demonstrate Nexus model-substitution parity.

## What the public tests establish

The v0.2 gateway and router repositories each have automated suites and GitHub CI.

The gateway tests cover the public challenge surface, artifact handling, metadata sanitation, evidence-envelope behavior, access/kill-switch behavior, challenge execution against an opaque test target, challenge-schema validation, built-in suite behavior, cleanup, and router-observation handling.

The router tests cover route isolation, model locking, OpenAI-compatible request forwarding, streaming, tool-call pass-through, route lifecycle behavior, SSRF protection, secret-safe error handling, request-scoped route credentials, and secret-free usage readback.

Publication CI passed on Python 3.11–3.13 for both repositories after the v0.2 merges.

## Private-target integration status

The private Nexus parent repository now has a dedicated validation-target integration candidate with isolated integration tests and CI.

That matters because the public challenge contract no longer ends only at a synthetic mock design: there is now a private implementation path intended to terminate against the real Nexus runtime responsibilities while keeping the construction graph hidden.

But the evidence boundary remains important:

> **Implemented and isolated-tested is not the same as deployed and retained.**

At the current portfolio update, no retained deployed-target campaign has yet been recorded through that private integration. The public repository therefore must not claim that Nexus has passed the built-in core suite or an independent evaluator's unseen challenge.

## Current claim ceiling

The public gateway currently supports the claim:

> **A public-safe black-box validation surface with evaluator-authored challenge contracts, a retained core suite, provider-use verification, and sanitized evidence boundaries can be implemented and tested without publishing the target runtime's private composition logic.**

The router currently supports the claim:

> **BYO OpenAI-compatible model transport can be isolated into a reusable, provider-facing component with route isolation and observable usage evidence without embedding Nexus-specific runtime logic.**

The private integration work supports a narrower internal status statement:

> **A private Nexus validation-target integration has been implemented and isolated-tested as a deployment candidate.**

These still do **not** establish:

- that the gateway has completed a retained challenge campaign against the deployed Nexus target;
- that Nexus has passed `nexus-blackbox-core-v1` on a production-facing synthetic tenant;
- that external evaluators have authored and executed independent Nexus challenge packs;
- controlled model-swap parity across the deployed private runtime;
- whole-system certification;
- any private Nexus implementation detail.

Those stronger claims require the retained real-target campaign and, separately, genuinely independent evaluator-authored testing.

## Why this belongs in the portfolio

Earlier public projects made individual architectural responsibilities inspectable. This pair adds a different capability: a path for outsiders to test selected claims **against an opaque private target** rather than only reviewing bounded public analogues.

The progression is now:

```text
explain a claim
→ publish a bounded artifact
→ publish the challenge contract
→ let outsiders author a challenge
→ execute against an opaque target
→ retain observable evidence
```

The private runtime still does not need to become a reconstruction kit.

See also:

- [Production Evidence Status](../docs/PRODUCTION_EVIDENCE_STATUS.md)
- [Public Repository and Artifact Map](../docs/REPOSITORY_MAP.md)
- [Public Boundary](../PUBLIC_BOUNDARY.md)
- [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig)
