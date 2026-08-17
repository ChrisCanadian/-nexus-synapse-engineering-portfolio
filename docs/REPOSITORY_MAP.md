# Public Repository and Artifact Map

This page explains how the public Nexus-related artifacts fit together without implying that they are deployed as one public system.

## Map

| Artifact | Public purpose | Relationship to Nexus | Evidence status | Claim ceiling |
|---|---|---|---|---|
| [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) | Receipt-backed execution/evidence reference kernel | Extracts a mature control principle into a standalone public project | Implemented and tested as its own repository | Does not establish the full production Nexus execution path |
| [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Safe real-boundary acceptance framework with durable readback and evidence bundles | Encodes the verification discipline that emerged during Nexus development | Implemented and tested as its own repository | Does not certify Nexus or replace system-specific acceptance work |
| [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Guided conversion of fuzzy behavioral intent into a portable Mode Card | Bounded extraction of behavioral-mode authoring work | Released public artifact; automated suite covers the bounded creator contract | Does not expose activation, weighting, persistence, SSR integration, or identity composition |
| [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Scoped persistent memory, recall, correction/supersession, provenance, and memory-capability execution | Bounded reference extraction of memory responsibility and authority patterns | v0.1.0 public implementation; capability, isolation, persistence, temporal, and semantic-scope tests; publication CI passed Python 3.10–3.13 | Does not expose private production schemas/queries, SSR memory eligibility/composition, or the general-purpose Nexus execution layer |
| [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Public challenge boundary for opaque runtime targets with BYO OpenAI-compatible inference, evaluator-authored challenge contracts, core-suite execution, and sanitized evidence envelopes | Provides a public validation surface intended to challenge a private target without exposing its internal composition | v0.2 public implementation; challenge schema + `nexus-blackbox-core-v1`; gateway/suite tests and publication CI passed Python 3.11–3.13 | Does not itself establish deployed Nexus behavior until a retained private-target campaign is executed |
| [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Reusable short-lived BYO provider routing with model locks, streaming, tools pass-through, SSRF protection, secret-safe failures, and usage readback | Generic inference transport that can support validation and future provider portability without containing Nexus-specific logic | v0.2 public implementation; router tests and publication CI passed Python 3.11–3.13 | Independent infrastructure only; not evidence of deployed Nexus routing/composition until exercised through a retained target campaign |
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

### Historical artifact

A retained earlier implementation or benchmark that shows lineage, not current architecture.

**Example:** the SSR warehouse-style gist.

### Research/documentation surface

Narrative, diagrams, glossary, terminology translation, and evaluation material for understanding the architecture.

**Examples:** Research Library and this portfolio.

## Important

These artifacts are architecturally related by lineage, validation strategy, and design philosophy.

They are **not** presented as a set of public modules that can be assembled into the private Nexus Synapse runtime.

The Black-Box Validation Gateway is specifically intended to make selected private-runtime claims externally challengeable without publishing the private composition graph. A private Nexus validation-target integration candidate now exists and has isolated integration test/CI evidence, but the public claim ceiling remains unchanged until a retained deployed-target campaign is recorded.

For readers coming from conventional software/AI systems terminology, see [Nexus Terminology → Conventional Systems Concepts](NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md).
