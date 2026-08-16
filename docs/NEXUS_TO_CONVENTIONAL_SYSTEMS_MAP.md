# Nexus Terminology → Conventional Systems Concepts

Nexus developed its own subsystem names while the architecture was evolving. Those names are useful inside the project, but they should not force an outside engineer to learn a private vocabulary before evaluating the work.

This page translates **Nexus terminology → closest conventional concept → Nexus-specific implementation decision → current evidence qualification**.

A conventional analogue is **not** a claim that two systems are identical, and a Nexus name is **not** a novelty claim by itself.

## Fast translation table

| Nexus term | Closest conventional concept(s) | What Nexus does with it | Current evidence / qualification |
|---|---|---|---|
| **SSR — Structured State Reconstruction** | Context assembly, state hydration, context compiler | Reconstructs a bounded operating context from eligible persistent/runtime state before model inference instead of treating the system prompt as the sole state carrier | Current SSR V2 path is deployed and behaviorally consequential in the August 14 production audit |
| **CAG — Conversation Archive/Cache** | Session-context cache, rolling conversation state, continuity buffer | Supplies bounded conversation continuity as one input to broader context construction | Current path exists; the newest audited session used a broader all-session summary fallback because usable session-matched summaries were absent |
| **Gauges** | Scalar configuration parameters, behavioral control values | Persisted intensity controls modify communication behavior without being treated as identity themselves | Persisted and consumed by current context construction |
| **Modes** | Behavioral policy/profile overlay, task persona/configuration profile | Applies a temporary behavioral/role configuration without granting execution authority or replacing the core user/runtime identity boundary | Current persisted mode state is consumed by SSR; public Mode Card Creator exposes authoring, not private activation logic |
| **Dyad / cognitive nodes** | Feature scoring, control-state vector, runtime signal graph | Computes bounded signals that can condition prompt/advisory context | Node scoring is current; audited node-persistence hooks were disconnected, so scoring and durable node learning should not be conflated |
| **Senate / distributed cognition** | Multi-agent deliberation, ensemble advisory, critique panel | Separate advisory model work contributes bounded context to the final response path while remaining subordinate to runtime authority | Current conditional advisory path is wired; a July isolated trace exercised a two-round debate |
| **Thinker** | Background maintenance worker, reflection daemon, scheduled analysis job | Historical/background cognition lane intended to perform between-turn or between-session reflection/maintenance work | Not proven as part of the current main deployed turn path in the August audit |
| **Reflections** | Derived episodic memory, self-evaluation record, reflective summary | Persists derived observations that can later re-enter model/advisory context | Accepted reflection context is current and populated in the audited production state |
| **Self-model** | Persistent self-representation / structured self-state | Separate structured representation intended to contribute bounded self-related state | The audited current self-model projection is omitted because of a storage-contract mismatch; historical evidence should not be promoted into a current-path claim |
| **Continuity** | Persistent application/session state, durable user state | Keeps user/session/history state outside interchangeable model weights so a model call is not the sole owner of continuity | Core relational continuity is current; individual memory paths have different freshness/quality levels |
| **Authority mediation** | Authorization, policy enforcement, capability control | Separates model proposal from permission, execution, evidence, and final narration | Runtime-owned tool visibility/authorization/dispatch is current; advisory/model output is not execution authority |
| **Tool / capability executor** | Command dispatcher, capability gateway, application service layer | Validates and dispatches runtime capabilities under trusted scope and returns normalized results; consequence-bearing operations remain outside pure model narration | Current production tool mediation is runtime-owned; the public Memory Kernel exposes only a deliberately bounded memory-capability version |

## The evaluation pattern

For any named Nexus subsystem, use four questions:

```text
1. What conventional systems concept is this closest to?
        ↓
2. What responsibility does Nexus assign to it?
        ↓
3. What is different about the Nexus composition or authority boundary?
        ↓
4. What evidence supports the current claim?
```

That is more useful than asking whether the subsystem name itself is novel.

---

## SSR — Structured State Reconstruction

**Closest conventional concepts:** context assembly, state hydration, context compilation.

The interesting decision is not the acronym. Nexus treats pre-inference context construction as an explicit runtime responsibility. The runtime decides which eligible state sources can contribute to a turn and composes a bounded operating context before handing work to an interchangeable generator.

At a public-safe level, that can include profile/identity state, behavioral controls, current mode, user rules, learned preferences, continuity/memory, reflections, capability facts, analysis signals, and optional advisory cognition.

**What is different:** the composition is treated as runtime state reconstruction rather than a static prompt template or a request for the model to remember everything itself.

**Evidence qualification:** SSR V2 is current and behaviorally consequential in the August 14 deployed-code/read-only-state audit. Exact ordering, selection rules, weighting, and production queries remain private.

---

## CAG — Conversation Archive/Cache

**Closest conventional concepts:** session-context cache, rolling conversation state, continuity buffer.

CAG is one continuity source, not the whole Nexus memory architecture. Its job is to provide bounded conversation-so-far material for context construction.

**What is different:** CAG is subordinate to broader runtime context reconstruction rather than being treated as the complete memory system.

**Evidence qualification:** the current CAG path remains active, but the newest audited session lacked usable session-matched summaries and therefore used the broader all-session summary fallback. That degraded/fallback condition is part of the current evidence record.

---

## Gauges and Modes

### Gauges

**Closest conventional concepts:** scalar configuration values, behavioral control parameters.

Gauges represent *how much* of a behavior/control tendency should be expressed. They should not be read as a claim that Nexus invented configurable personality sliders.

### Modes

**Closest conventional concepts:** behavioral policy overlays, task profiles, temporary role/persona configuration.

Modes shape how the assistant approaches a task without automatically granting authority or replacing durable identity.

**What is different:** both are persisted runtime inputs that can be assembled into context while remaining separate from execution authority.

**Evidence qualification:** current persisted gauge/mode state is read by the production context-construction path. The public [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) intentionally stops at portable authoring and does not expose private activation/weighting/integration logic.

---

## Dyad / cognitive nodes

**Closest conventional concepts:** feature scoring, control-state vectors, runtime signals.

The node layer represents explicit scored state that can influence downstream context/advisory work.

**What is different:** the values live in the runtime rather than needing to be inferred anew inside the final model response.

**Evidence qualification:** current production computes node/focus signals, but audited persistence hooks for node updates were disconnected. Current scoring and durable adaptive node learning are therefore different claims.

---

## Senate / distributed cognition

**Closest conventional concepts:** multi-agent deliberation, ensemble advisory, critique/debate panels.

Nexus did not invent multi-agent debate.

**What is different:** Senate output is deliberately **advisory**. It can contribute bounded context, but it does not inherit consequence authority merely because a model produced a recommendation. Tool recommendations remain recommendations until the runtime authorizes and executes a capability.

**Evidence qualification:** the August production audit found the advisory path conditionally wired. A July isolated production-target trace separately exercised a two-round Senate debate. Those are different evidence classes and should remain labeled that way.

---

## Thinker

**Closest conventional concepts:** background worker, reflection daemon, scheduled maintenance/analysis job.

Thinker historically represented background observation/reflection responsibilities.

**What is different:** conceptually, it moves some maintenance/reflection work outside the immediate user-facing model call.

**Evidence qualification:** the August audit did not establish Thinker as an active contributor to the current main deployed turn path. It belongs in the architecture history and current caveat list, not in a blanket claim that it runs on every turn.

---

## Reflections and self-model

### Reflections

**Closest conventional concepts:** derived episodic memory, reflective summaries, self-evaluation records.

Accepted reflection records are persisted derived context that can later be reintroduced into the runtime.

**Current status:** active and populated in the audited production state.

### Self-model

**Closest conventional concepts:** structured persistent self-representation / self-state.

The separately stored self-model projection is conceptually distinct from reflections.

**Current status:** the audited production loader currently omits that projection because of a storage-contract mismatch. This is a useful example of why Nexus documentation separates *implemented*, *wired*, and *currently consumed*.

---

## Continuity and memory

**Closest conventional concepts:** durable application state, session persistence, episodic/semantic memory services.

Nexus uses multiple memory responsibilities rather than treating memory as a single vector database or retrieval call.

**What is different:** the runtime owns eligibility and scope. The final model does not independently decide which historical records it is authorized to retrieve.

The public [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) is a bounded standalone reference implementation of **scoped persistence + recall + correction/supersession + provenance + memory-capability execution**. It is not the private production memory implementation and does not expose current SSR selection rules.

**Evidence qualification:** relational continuity is current and consequential. The audited semantic/vector conversation corpus was stale/reference-degraded, while relational/chronological fallbacks remained available. Those conditions should not be collapsed into “memory is live” as one undifferentiated statement.

---

## Authority mediation and capability execution

**Closest conventional concepts:** authorization middleware, policy enforcement, command dispatch, capability gateway.

The central Nexus rule is:

> **Model proposal is not execution authority.**

A model can propose a capability call. Runtime code owns visibility, trusted scope, authorization, dispatch, output handling, and durable evidence where required.

**What is different:** this boundary is applied as a recurring system design rule around model inference rather than trusting natural-language narration as proof of side effects.

The public [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) demonstrates the broader proposal → authority → execution → receipt distinction. The [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) demonstrates a narrower memory-specific capability boundary.

---

## Why keep the Nexus names at all?

The names are useful for tracking the project's architecture and historical evolution. They become a problem only when the reader is expected to treat a name as explanation or novelty evidence.

The intended public communication rule is therefore:

> **Use the Nexus term for project identity; translate it into conventional systems language for evaluation; make novelty claims only about specific implementation/composition decisions that the evidence can support.**

For current production-path evidence, continue with:

- [Current Production Responsibilities](CURRENT_PRODUCTION_RESPONSIBILITIES.md)
- [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md)
- [Public Technical Reference v1.1](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- [Glossary](GLOSSARY.md)
