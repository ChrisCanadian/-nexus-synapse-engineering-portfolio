# Case Study — Memory and Context Selection

## The problem

Persistent AI systems can accumulate more history than should be placed into every model call.

In conventional systems terms, this is a combination of **persistent application state, scoped retrieval, session continuity, and context assembly**.

Nexus development repeatedly treated this as a runtime responsibility:

> **What information is eligible for this turn, and how should it be represented before inference?**

## Early form

The early SSR work focused on structured narrowing before semantic work:

```text
large state / history
      ↓
structured scope
      ↓
bounded candidates
      ↓
semantic/contextual selection
      ↓
compact representation
```

The historical warehouse analogy was literal engineering inspiration: determine the order, narrow the inventory, assemble the pick list, and send only the useful material to the workstation.

In conventional retrieval language, the closest pattern is **structured candidate filtering followed by semantic ranking**.

## Broader evolution

Over time, the same idea expanded beyond retrieval.

Context construction increasingly included multiple kinds of state:

- identity/personality state;
- learned preferences;
- conversation/session continuity;
- memory summaries and relevant history;
- capabilities and tool context;
- current analysis/focus signals;
- optional advisory context.

The important architectural change was not “more memory.”

It was that **selection and representation became explicit runtime responsibilities** rather than an instruction to the model to somehow remember everything.

In current Nexus terminology, that broader responsibility is part of **Structured State Reconstruction (SSR)**. The closest conventional systems concepts are **state hydration / context assembly / context compilation**.

## Public Memory Kernel

The [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) now provides a bounded executable example of a narrower part of this problem:

```text
trusted scope
    ↓
validated memory capability
    ↓
read/write authority
    ↓
scoped persistence / recall / correction
    ↓
provenance + mutation receipt
```

The public kernel demonstrates scoped memory responsibility and memory-capability authority. It intentionally does **not** expose the private Nexus rules that decide which memories become eligible for SSR or how memory is composed with other runtime state.

See the dedicated [Memory Kernel case study](memory-kernel.md).

## Evidence boundaries

Historical Nexus material uses several overlapping terms and implementations.

For public communication:

- early SSR benchmarks are historical artifacts;
- current private selection rules are intentionally not published;
- not every historical SSR path used vector search;
- code presence alone does not establish current activation;
- current relational continuity and semantic/vector memory have different evidence/freshness conditions;
- V5 memory reconstruction work is described as isolated/tested where the evidence supports that status;
- the public Memory Kernel is evidence for the **public kernel**, not automatic evidence for current production memory behavior.

## Why this case study is intentionally high level

Detailed current schemas, query patterns, thresholds, weighting logic, memory projections, and prompt ordering are part of the private implementation boundary.

This case study documents the **responsibility shift** without making the private selection system reproducible.

See also:

- [Nexus Overview](../docs/NEXUS_OVERVIEW.md)
- [Nexus Terminology → Conventional Systems Concepts](../docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)
- [Architectural Evolution](../docs/ARCHITECTURAL_EVOLUTION.md)
- [Historical SSR case study](ssr-v1-warehouse-rag.md)
