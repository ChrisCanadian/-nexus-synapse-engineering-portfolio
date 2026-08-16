---
title: "Nexus Synapse Public Technical Reference"
author: "Christopher Campbell"
date: "August 2026"
geometry: margin=0.8in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    \usepackage{parskip}
    \setlength{\parindent}{0pt}
---

# Public Research Release v1.1

**Responsibility Layers, Turn Lifecycle, and Current Evidence Status**

**Current-state review:** August 14, 2026  
**Publication posture:** Public-safe engineering reference  
**License:** CC BY-NC 4.0

> **The model performs inference. The runtime owns the continuity, boundaries, capabilities, and durable state around that inference.**

## Scope

This document explains Nexus Synapse at the responsibility level.

It intentionally excludes private schemas, credentials, local paths, proprietary source code, raw prompts, database contents, operational secrets, and implementation details that are unnecessary to evaluate the architectural claims.

This revision updates the July 2026 public reference against a read-only August 14 inspection of the deployed production Python and production state. The audit did not execute behavior-triggering production requests or mutate production data. Where execution evidence comes from the July 11 isolated production-target trace, it is labeled as historical execution evidence rather than silently promoted into a current live-production claim.

## System definition

Nexus Synapse is a **state-conditioned, policy-bearing continuity runtime around replaceable probabilistic generators**.

Its purpose is not to replace a language model. Its purpose is to manage responsibilities that a stateless model call does not own reliably:

- authenticated user and session continuity;
- durable and temporary memory;
- context selection and prompt assembly;
- modes, rules, gauges, and learned preferences;
- governance and optional advisory cognition;
- tools, visibility, authorization, and execution;
- provider and model routing;
- persistence and post-turn maintenance;
- deterministic post-generation checks;
- audit evidence and claim boundaries.

The language model remains important for generation and selected reasoning or deliberation work, but it does not own authentication, persistent-state selection, prompt composition order, tool authority, durable persistence, or post-generation verification.

## Responsibility stack

| Layer | Runtime responsibility | Current-state note |
|---|---|---|
| Interface | Capture requests, UI state, mode, attachments, and session context | Server-side state remains authoritative |
| Identity and scope | Resolve user, session, team/channel boundaries, and authority | Runtime-owned |
| Analysis | Produce intent/topic/emotion/focus-style signals for downstream calibration | Current deployed path uses external inference when available and static fallback after failure; the local NLP pipeline is not the active production path |
| Continuity state | Load session history, summaries, preferences, reflections, and eligible memory | Relational memory is current; some memory layers degrade or fall back |
| Context construction | Assemble bounded model context through SSR V2 | Current and behaviorally consequential |
| Advisory cognition | Generate optional distributed/Senate guidance | Present as optional multi-model advisory, not authority |
| Reflection / self-model | Add bounded stored reflection or self-knowledge context | Reflections are active; the audited self-model projection is currently omitted by a storage-contract mismatch |
| Tool layer | Advertise, validate, authorize, execute, verify, and return tool results | Runtime-authoritative; model proposes only |
| Provider layer | Assign models to responsibilities and normalize provider behavior | Provider choice is separate from continuity state |
| Delivery | Stream or return the user-facing result | Followed by deterministic truth/hallucination guards |
| Preservation | Persist permitted interactions, summaries, adaptation evidence, and audit data | Current, but not every historical learning path changes later behavior |
| Operations | Monitor degradation, background maintenance, and recovery | Optional paths can fail-soft; authority-sensitive paths can fail-closed |

## Representative turn lifecycle

```text
authenticated request
  -> resolve user / session / scope
  -> analysis + focus / node scoring
  -> memory selection and fallback
  -> SSR V2 context construction
  -> profile + gauges + mode + user rules + learned preferences
  -> reflections + optional advisory cognition
  -> provider routing
  -> optional governed tool execution
  -> response synthesis
  -> deterministic post-generation checks
  -> background persistence / summaries / selected adaptation
```

Not every optional subsystem runs on every turn. A mature runtime should distinguish **executed**, **degraded**, **skipped**, **disabled**, **not observed**, and **failed** instead of collapsing those states into a generic claim that a component is "live."

## Memory and continuity

Nexus separates several memory responsibilities rather than treating memory as one database or one retrieval call.

### Immediate context

The current request and active provider conversation.

### Session continuity

A bounded conversation-so-far representation. In the August 14 production audit, the newest persisted session did not have usable session-matched summaries, so the current CAG path fell back to the broader all-session summary pool. The fallback pool was current and usable.

### Structured durable memory

Relational interactions, summaries, preferences, reflections, and other typed runtime state. The August production audit found these core relational stores populated and behaviorally consequential.

### Semantic retrieval

Vector-assisted retrieval exists as a conditional memory path. In the August audit, the inspected conversation-vector corpus was stale and contained degraded references, so semantic retrieval should not be described as uniformly fresh. Chronological relational fallback remains available.

### Temporal and associative recall

Nexus can resolve date-bounded memory requests and meaning-based recall through runtime-owned memory capabilities. July 11 isolated execution evidence demonstrated memory-tool execution and associative recall. The public evidence does not establish perfect recall semantics or grounding for every query.

The important architectural boundary is unchanged: **the runtime decides what historical material is eligible for a turn; the model does not independently own that decision.**

## SSR V2

SSR V2 is the main context-construction layer in current production.

At a public-safe level, it can combine:

- stable identity/profile information;
- communication gauges;
- active mode;
- user-specific rules;
- active learned preferences;
- current analysis, focus, and node state;
- session continuity and selected memory;
- reflection context;
- tool/capability facts;
- optional advisory cognition;
- current provider/model metadata.

Its job is not to maximize prompt length. Its job is to assemble a bounded operating context appropriate to the current user and turn while preserving authority distinctions between state sources.

## Analysis and cognitive input

Current production still performs pre-inference analysis and node scoring, but the implementation path has changed from older documentation.

The deployed local NLP pipeline is disabled in the audited configuration. Analysis uses external inference when available and degrades to static defaults after failure or circuit-breaker conditions. Node definitions remain populated and their scores can affect prompt context and advisory inputs.

This matters for evidence language: **analysis is active, but the historical local NLP/vocabulary path should not be described as the current production analyzer.**

## Advisory cognition and Senate

Nexus currently supports optional multi-model advisory work before final inference.

The distributed-cognition path can build role-specific context and request Senate output. The main response engine consumes the returned advisory as bounded context. Tool recommendations from advisory cognition do **not** become tool authority, and the advisory layer does not replace the full SSR context or runtime policy.

A July 11 isolated baseline executed a two-round Senate debate. The August 14 deployed-code audit confirmed that distributed cognition/Senate remains wired conditionally in current production.

**Thinker is different.** In the audited deployed Python, the Thinker bridge did not have a current caller in the main path, and no safe current execution receipt was established. Thinker should therefore remain described as **unverified / not part of the proven current main turn path**, not as routine live cognition.

## Reflection and self-model

The current deployed path loads accepted reflection context and uses it in prompt/advisory construction.

The separately stored self-model projection is not currently loaded by the main deployed path because the active loader expects a user-scoping field that the deployed storage shape does not provide. The correct current statement is therefore:

> **Reflection context is active; the audited self-model projection is currently omitted.**

Older execution receipts that showed a combined self-model/reflection block remain valid as historical isolated evidence, but they should not be treated as a literal description of the August production data path.

## Tools

The tool system separates:

1. registration;
2. model-visible advertisement;
3. user/role visibility;
4. authority and permission;
5. argument validation;
6. handler execution;
7. result/artifact verification;
8. result return and response synthesis.

A tool is not operational merely because its schema exists.

The August production audit found **25 enabled tools** in the current registry. Tool use remains conditional per turn. The model can propose a structured call, but runtime code decides visibility, authorization, dispatch, output handling, and continuation.

The July 11 isolated audit remains useful execution evidence because it demonstrated multiple advertised schemas and two memory-tool execution cycles, but it did not validate every tool class.

## Provider and model allocation

Nexus can assign different models to different responsibilities while keeping continuity state outside those models.

The July 11 isolated baseline demonstrated this separation by using one model for final user-facing inference and another for supporting Senate work. That is **historical execution evidence**, not a claim that those exact model selections are permanently fixed in production.

The current production architecture continues to route provider/model selection through runtime-owned provider infrastructure. A controlled primary-model swap with measured behavioral/tool parity remains a separate evidence requirement.

## Persistence and adaptation

The deployed runtime performs background persistence after response generation. Current evidence supports ongoing writes for interactions, summaries, learned preferences, and selected choice/value records.

Two non-parametric adaptation loops are especially defensible:

- **conversation summaries** are persisted and later reused in continuity/context selection;
- **learned preferences** are periodically derived from stored interaction patterns and later read by SSR V2, changing future prompt composition without changing model weights.

Other historical/coded paths require narrower wording:

- direct-feedback state is persisted, but a next-turn effect through the active SSR path is not proven;
- goal and curiosity state were empty for the audited account and their main post-turn hooks were not correctly connected in the deployed path;
- node scoring is active, but node-persistence hooks were disconnected;
- the self-model projection was omitted as described above;
- Thinker/background cognition was not established as an active current main-path contributor.

Code presence, a database table, or a scheduled concept is not enough to call a learning loop behaviorally active.

## Governance and authority

Governance concerns include:

- user and team scope;
- tool visibility and permissions;
- side-effect authority;
- provider/model eligibility;
- failure and degradation behavior;
- post-generation checks;
- audit evidence;
- claim discipline.

The architectural rule is simple:

> **Access is not authority, and model proposal is not execution authority.**

Optional cognition can advise. It does not override explicit runtime authority boundaries.

## Current evidence status

The public evidence now comes from two different evidence classes and should not be silently merged.

### July 11, 2026 - isolated production-target execution

Executed against copied/redirected state rather than the production VM. This evidence demonstrated selected route/session handling, analysis, focus/node stages, SSR V2, associative recall, distributed cognition, Senate, provider routing, and memory-tool execution. Authentication was bypassed for that audit and the trace did not establish every post-turn write.

### August 14, 2026 - deployed production code + read-only state audit

Inspected the actual deployed Python and current production state without performing production writes or behavior-triggering requests. This evidence established the currently wired/degraded/omitted paths, current SSR/state readers, populated relational memory and adaptation, current tool registry, conditional Senate advisory, reflection context, NLP fallback behavior, and several disconnected or stale mechanisms.

| Area | Current defensible status |
|---|---|
| Authenticated runtime architecture | deployed code inspected; normal path identified |
| SSR V2 state-conditioned context construction | current / behaviorally consequential |
| Profile, gauges, mode, user rules, learned preferences | current / populated |
| Relational interaction + summary memory | current / populated |
| Session-local CAG | current with observed all-session fallback in latest audited session |
| Semantic/vector conversation memory | implemented but stale/reference-degraded in audited state |
| Analysis | current via external inference or static fallback; local NLP pipeline disabled |
| Focus + node scoring | current; node persistence disconnected |
| Distributed cognition / Senate | current conditional advisory |
| Reflections | current / populated |
| Self-model projection | omitted in audited current path |
| Tool registry and authority mediation | current; 25 enabled tools in audited state |
| Background interaction/summary persistence | current |
| Learned preference adaptation | current and later consumed by SSR |
| Direct-feedback downstream behavioral effect | persisted but not proven through active SSR |
| Goals / curiosity / injectable background cognition | empty or disconnected in audited state |
| Thinker | not proven in current main deployed path |
| Controlled primary-model swap parity | not demonstrated |
| Independent replication | not demonstrated |

## V5 boundary

V5 is a separate reconstruction line, not the production runtime represented above.

Current V5 work preserves the central authority direction - runtime-owned state, scoped memory, provider abstraction, tool mediation, persistent continuity, and stronger receipt/provenance controls - but parity should not be declared for every production behavioral/cognitive surface until those mechanisms are deliberately preserved, replaced, retired, or reclassified with evidence.

## Privacy and publication boundary

Public documentation should describe responsibilities and evidence without exposing:

- credentials or provider secrets;
- private user data;
- raw memory or conversation content;
- private database schemas or query patterns;
- proprietary source code;
- local filesystem paths or deployment internals;
- full private prompts or SSR selection logic;
- operational infrastructure details unnecessary to evaluate a public claim.

## Current architectural claim

The August evidence supports this description:

> **Nexus currently operates as a state-conditioned, policy-bearing runtime around replaceable probabilistic generators. Durable relational state actively conditions identity, behavior, memory, tool visibility, and later-turn context composition. At least summary and learned-preference loops provide demonstrated non-parametric persisted adaptation. Optional multi-model advisory is present in production. Several higher-order cognition and semantic-memory paths are degraded, disconnected, empty, or unverified and are not promoted merely because code or storage exists.**

The evidence does **not** support describing Nexus as independently certified, universally reliable, fully parity-tested across providers/models, or conscious.

---

**Evidence basis:** July 11, 2026 isolated production-target execution package; August 14, 2026 read-only deployed production implementation/state audit.  
**Public-safe revision:** August 16, 2026.  
**Christopher Campbell | Independent Research | Ontario, Canada**
