# Public Repository and Artifact Map

This page explains how the public Nexus-related artifacts fit together without implying that they are deployed as one public system.

If you are not coming from AI/software engineering, the shortest version is:

| Repository | The problem in ordinary work terms |
|---|---|
| [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) | Do not treat "I did it" as proof. Separate permission, action, and evidence. |
| [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Verify the real target changed, not just that the test script ran successfully. |
| [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Turn desired working style into a reusable profile without confusing style with authority. |
| [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Keep memory scoped, correctable, traceable, and persistent. |
| [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Let someone test a closed system without handing them its private implementation. |
| [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Change or supply the model/provider without redesigning the application around it. |
| [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime) | Run an evidence-constrained reconstruction of the flat-file runtime that preceded Nexus. |

For a fuller domain-first explanation, see [Nexus Synapse for Domain Experts](DOMAIN_EXPERT_ORIENTATION.md).

## Map

| Artifact | Public purpose | Relationship to Nexus | Evidence status | Claim ceiling |
|---|---|---|---|---|
| [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) | Receipt-backed execution/evidence reference kernel | Extracts a mature control principle into a standalone public project | Implemented and tested as its own repository | Does not establish the full production Nexus execution path |
| [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Safe real-boundary acceptance framework with durable readback and evidence bundles | Encodes the verification discipline that emerged during Nexus development | Implemented and tested as its own repository | Does not certify Nexus or replace system-specific acceptance work |
| [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Guided conversion of fuzzy behavioral intent into a portable Mode Card | Bounded extraction of behavioral-mode authoring work | Released public artifact; automated suite covers the bounded creator contract | Does not expose activation, weighting, persistence, SSR integration, or identity composition |
| [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Scoped persistent memory, recall, correction/supersession, provenance, and memory-capability execution | Bounded reference extraction of memory responsibility and authority patterns | v0.1.0 public implementation; capability, isolation, persistence, temporal, and semantic-scope tests; publication CI passed Python 3.10–3.13 | Does not expose private production schemas/queries, SSR memory eligibility/composition, or the general-purpose Nexus execution layer |
| [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Public challenge boundary for opaque runtime targets with BYO OpenAI-compatible inference, evaluator-authored challenge contracts, core-suite execution, and sanitized evidence envelopes | Provides a public validation surface intended to challenge a private target without exposing its internal composition | v0.2 public implementation and CI; August 18 deployed-target fixed-invariant campaign recorded as failed, with a separate unseen challenge pass | Gateway tests and partial deployed-target observations do not establish that deployed Nexus passed validation |
| [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Reusable short-lived BYO provider routing with model locks, streaming, tools pass-through, SSRF protection, secret-safe failures, and usage readback | Generic inference transport that can support validation and future provider portability without containing Nexus-specific logic | v0.2 public implementation; router tests and publication CI passed Python 3.11–3.13 | Independent infrastructure only; its observed use in one campaign does not establish provider parity or a Nexus validation pass |
| [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime) | Runnable historical reconstruction of the early flat-file, pre-database, pre-SSR ChrisAI architecture | Historical predecessor/lineage evidence rather than a current Nexus extraction | v0.1.0 reconstruction candidate; surviving code, dated configuration, migration material, tests, and pre-migration documentation constrain the implementation | Not a byte-for-byte original checkout, not proof every reconstructed line existed verbatim, and not evidence of modern or deployed Nexus internals |
| [Historical SSR gist](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752) | Historical Structured-SQL-RAG / warehouse-style context-selection demonstration | Early ancestor of later SSR/context reconstruction | Historical benchmark and trace material retained | Not current SSR and not evidence for every later Nexus retrieval claim |
| [Nexus Synapse Research Library](https://sites.google.com/view/nexus-synapse-research-library/home) | Long-form public research and architecture narrative | Documentation/research surface | Documented public material | Not production source code |
| [Public Technical Reference v1.1](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view) | Current public-safe responsibility map and evidence ceiling | Portfolio + Research Library technical reference | Reconciled to August 14 deployed-code/read-only-state audit; July execution kept as dated evidence | Not production source, not a replication guide, and not a claim that every coded subsystem is active |
| This portfolio | Curated map of the engineering journey, evidence, and public artifacts | Public front door | Documentation + linked evidence | Does not make the private runtime reproducible |

## Why separate repositories?

The private Nexus parent runtime is intentionally not being reduced to one sanitized public monolith.

Instead, public work is extracted around a narrow question:

```text
What claim are we trying to make inspectable?
        ↓
What is the smallest useful public artifact that demonstrates it?
        ↓
What evidence supports that artifact?
        ↓
What does it explicitly NOT establish?
```

That approach keeps each artifact falsifiable and easier to review.

The newer validation work adds another pattern:

```text
public challenge contract
        ↓
opaque target boundary
        ↓
observable behavior / evidence
```

The challenge surface can be public while the target's private composition remains undisclosed.

## Public artifact classes

### Reference kernel

A deliberately small executable implementation of one architectural control/responsibility pattern.

**Examples:** Nexus Proof Runtime and Nexus Memory Kernel.

### Acceptance framework

A reusable framework for safely exercising a real boundary and retaining evidence.

**Example:** Live Runtime Acceptance Rig.

### Black-box validation surface

A public challenge gateway that exposes inputs, observable outputs, and evidence envelopes while keeping the target implementation opaque.

**Example:** Nexus Black-Box Validation Gateway.

### Reusable infrastructure

A generic component that supports public validation or future integration but does not contain Nexus-specific composition logic.

**Example:** OpenAI-compatible Router.

### Authoring surface

A bounded tool that ends before private runtime consequence/activation logic begins.

**Example:** Nexus Mode Card Creator.

### Historical reconstruction

A modern executable artifact constrained by surviving historical evidence. It is not represented as original bytes or current architecture.

**Example:** ChrisAI Runtime.

### Historical artifact

A retained earlier implementation or benchmark that shows lineage, not current architecture.

**Example:** the SSR warehouse-style gist.

### Research/documentation surface

Narrative, diagrams, glossary, terminology translation, and evaluation material for understanding the architecture.

**Examples:** Research Library and this portfolio.

## Important

These artifacts are architecturally related by lineage, validation strategy, and design philosophy.

They are **not** presented as a set of public modules that can be assembled into the private Nexus Synapse runtime.

The Black-Box Validation Gateway is specifically intended to make selected private-runtime claims externally challengeable without publishing the private composition graph. A retained August 18, 2026 campaign against the existing deployment recorded deterministic session mapping and all six persistence barriers, but the fixed invariants still failed: cross-conversation continuity was displaced by a blocked memory-tool result, and correction persistence lost the replacement value during extractive summarization. A separate unseen challenge passed through all-session CAG. The failed fixed-invariant outcome remains controlling; deployed Nexus is not presented as having passed validation.

For readers coming from conventional software/AI systems terminology, see [Nexus Terminology → Conventional Systems Concepts](NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md).

For readers coming from a domain/operations background, see [Nexus Synapse for Domain Experts](DOMAIN_EXPERT_ORIENTATION.md).
