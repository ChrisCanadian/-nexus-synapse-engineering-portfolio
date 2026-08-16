# Term Glossary — Nexus Synapse

Terms in this project changed meaning over time. This glossary records reconciled usage for public communication and flags where drift risk is high.

## SSR

**Current canonical meaning:** **Structured State Reconstruction**.

For current architecture claims, SSR refers to the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. At a public-safe level, that can include identity/profile data, gauges, active mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

**Historical terminology:** Earlier Nexus documents used the acronym in several related but different ways, including Semantic SQL Retrieval, Structured-SQL-RAG, SQL-guided RAG, SSR personality engine, and SSR prompt builder. Those terms are preserved as historical source language rather than treated as the current expansion.

**Retrieval lineage:** One important early SSR ancestor used structured/SQL filtering to narrow candidates before semantic ranking. That retrieval pattern is historically significant, but **SSR does not currently mean vector search**, and not every SSR path implies an embedding stage.

**Drift risk:** High in historical material; low when using the current canonical expansion above.

## CAG

**Observed expansions**

- Conversation Archive/Cache — implemented `CAGManager` meaning.
- Context Adaptive Generator — explanatory/book meaning.
- Context-Augmented Generation — explanatory expansion in manuscript material.

**Reconciled usage**

Use **Conversation Archive/Cache** for code/runtime claims. Preserve other expansions only as source-specific public metaphors.

**Drift risk:** High.

## Engine2_0 / Engine2_1

- **Engine2_0:** Early integrated monolithic engine (Aug–Sep 2025). Named historical epoch.
- **Engine2_1:** Large modular response, personality, memory, emotion, multimodal, and routing system (Sep–Oct 2025). Named historical epoch.

**Drift risk:** Medium for Engine2_0; low for Engine2_1.

## V1–V4 retrospective labels

Book/manuscript material uses labels such as V1 monster file, V2 false architecture, V3 over-reach, and V4 SSR Minimal.

**Reconciled usage**

Use the named epochs in the architectural history. Treat V1–V4 labels as retrospective/source-specific, not formal releases.

**Drift risk:** High.

## V5

**Observed usage:** Isolated reconstruction repository and branch family (Jul–Aug 2026).

**Reconciled usage:** Implementation/reconstruction program, not a production release.

Prefer **isolated V5 reconstruction** rather than **V5 release** unless a source specifically establishes a release/deployment state.

**Drift risk:** High.

## Production

Historical usage has included several different meanings:

- implemented locally;
- developer rig passed;
- considered production-ready;
- present on the VM;
- enabled on the request path;
- operational but silently degraded;
- repaired through temporary infrastructure;
- durably deployed at an exact commit.

**Reconciled usage**

Where possible, split claims into:

1. implementation;
2. test;
3. deployment target;
4. activation;
5. durability.

**Drift risk:** Very high.

## Dyad

**Observed usage:** Twelve stackable cognitive nodes with activation and overrides (Feb 2026).

**Reconciled usage:** Explicit cognitive-state subsystem with global definitions/rules and per-user overrides.

**Drift risk:** Medium.

## Senate

**Observed usage:** Multiple advisory/deliberative implementations and seat rosters across snapshots.

**Reconciled usage**

Never draw “the Senate” with one timeless roster. Attach a roster to a source date/version and identify whether it describes an implementation, debate path, fallback path, or behavioral example.

**Drift risk:** High.

## Thinker

**Observed usage:** Conversation observer plus between-session reflection daemon (Mar–May 2026).

**Reconciled usage:** Two related advisory lanes:

- conversation observer;
- between-session reflection daemon.

**Drift risk:** Medium.

## Learning

**Observed usage:** Vocabulary, emotional, personality, preference, feedback, reflection, and candidate updates from Sep 2025 onward.

For an `IMPLEMENTED` learning claim, identify:

1. signal source;
2. transformation/candidate logic;
3. persistence or state mutation;
4. active call site.

**Drift risk:** Very high.

## Proof Runtime

**Observed usage:** Standalone receipt-backed reference kernel.

**Reconciled usage:** Never call it a production Nexus subsystem. Draw it as a separate public reference project.

**Drift risk:** High.

## Acceptance campaign

A framework execution can validly produce a target `FAIL`.

**Reconciled usage:** Separate campaign integrity from target outcome. A defect can produce a valid failure result while the acceptance campaign itself operated correctly and preserved evidence.

**Drift risk:** Medium.

## Reading rules

Prefer:

- **implemented in source** over **live**;
- **exercised by a retained rig** over **fully tested**;
- **operational at the recorded date** over **durable**;
- **isolated V5 reconstruction** over **V5 release**;
- **reference kernel** over **production subsystem**;
- **evidence supports** over **proves** when logs or data are partial.

These rules do not weaken the history. They make the strongest parts harder to dismiss.
