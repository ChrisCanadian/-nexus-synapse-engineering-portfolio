# Case Study — Nexus Memory Kernel

## Public artifact

[Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel)

## The bounded question

The private Nexus runtime has multiple continuity and memory responsibilities. Publishing those production paths directly would expose more implementation detail than is necessary to evaluate the architectural idea.

The public kernel therefore asks a smaller question:

> **Can persistent AI memory be made inspectable as a scoped capability with explicit read/write authority, correction lineage, provenance, and testable isolation?**

## What the public kernel implements

The standalone reference project includes:

- scoped SQLite-backed memory records;
- session-context retrieval;
- keyword and temporal recall;
- correction through successor records rather than silent overwrite;
- explicit supersession;
- provenance metadata;
- mutation receipts;
- an optional semantic-ranking adapter;
- a memory-only capability registry and execution gateway.

Its six public capabilities are:

```text
memory.search
memory.context
memory.inspect
memory.store
memory.correct
memory.supersede
```

## Why capability execution is part of the memory example

Storage alone does not demonstrate the authority boundary.

The public `MemoryCapabilityExecutor` makes the caller/runtime split explicit:

```text
caller proposes memory capability
        ↓
trusted host scope
        ↓
argument validation
        ↓
read/write authority
        ↓
bounded dispatch
        ↓
persistence / recall
        ↓
result + mutation receipt where applicable
```

The public executor is deliberately memory-only. It should not be read as a copy of the private Nexus general-purpose execution layer.

## What the tests establish

The v0.1.0 public repository includes tests for:

- execution of all six registered capabilities;
- write-authority enforcement;
- rejection of scope injection through capability arguments;
- rejection of caller-forged provenance labels;
- cross-user search isolation;
- cross-user inspect/correct/supersede rejection;
- correction/supersession lineage;
- persistence after database reopen;
- temporal filtering;
- semantic ranking only over already-scoped candidates.

The publication PR's GitHub Actions matrix passed on Python 3.10–3.13 before merge.

## Relationship to Nexus Synapse

This is a **bounded reference extraction of memory responsibilities**, not a module intended to be dropped back into the private runtime unchanged.

The public project demonstrates a generic responsibility pattern:

```text
trusted scope
    ↓
capability validation
    ↓
authority
    ↓
bounded memory operation
    ↓
provenance / receipt
```

It does not disclose how private Nexus determines memory eligibility for a turn, composes memory into SSR, combines memory with identity/behavioral state, or orchestrates the broader tool/capability surface.

## Claim ceiling

This artifact supports claims about **the public kernel itself**.

It does **not** establish:

- the exact current production Nexus memory implementation;
- the private production schema or query logic;
- current production semantic-memory freshness;
- private SSR selection/weighting rules;
- the private general-purpose Nexus execution layer;
- whole-system Nexus behavior.

That distinction is intentional.

## Why it belongs in the portfolio

The Memory Kernel gives outsiders an executable example of a broader Nexus design principle without requiring them to accept Nexus-specific terminology first:

> **The model can request memory; the runtime still owns scope, authority, durable state, and evidence.**

See also:

- [Memory and Context Selection](memory-and-context.md)
- [Nexus Terminology → Conventional Systems Concepts](../docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)
- [Repository Map](../docs/REPOSITORY_MAP.md)
