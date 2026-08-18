# Case Study — ChrisAI Runtime Historical Reconstruction

## Public artifact

- [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime)

## Why this is a different artifact class

Most public Nexus repositories are bounded current-day reference, authoring, validation, or infrastructure surfaces. ChrisAI Runtime answers a different question:

> **What did the runnable architecture look like before the database, Structured State Reconstruction, and later Nexus responsibility split?**

The repository is a modern executable reconstruction of the earlier flat-file ChrisAI runtime. It is constrained by surviving historical code, dated configuration, migration code, tests, and pre-migration documentation.

That makes it a **historical reconstruction**, not a preserved historical artifact and not a stripped copy of modern Nexus.

## Reconstructed responsibility shape

At its public-safe level, the reconstruction shows:

```text
persona text files + simple input analysis
                    ↓
             direct prompt assembly
                    ↓
            configurable local model
                    ↓
                response
                    ↓
       JSON memory / learning / history
```

The value is architectural contrast. Readers can execute a small evidence-constrained "before" state and compare it with the later movement of continuity, context selection, authority, tools, persistence, and evidence into explicit runtime responsibilities.

## Evidence and reconstruction discipline

The source repository records whether a historical statement is directly verified, configuration-supported, inferred, unknown, or unavailable. Safe replacement persona text is labeled as reconstruction material rather than represented as recovered original prose.

The reconstruction deliberately excludes later or unrelated material, including:

- modern Nexus database and SSR internals;
- Senate, Thinker, gauges, modes, and current governance/runtime composition;
- production tools, schemas, prompts, credentials, or user data;
- the personal streaming-overlay precursor project;
- components whose exact early contract cannot be supported by surviving evidence.

## Authorship and provenance

Christopher Campbell designed and built ChrisAI and maintains this reconstruction. AI coding and review tools assisted during the project history and reconstruction work without being represented as authors, owners, or licensors.

The reconstruction's repository-specific provenance is recorded in its [`ATTRIBUTION.md`](https://github.com/ChrisCanadian/chrisai-runtime/blob/main/ATTRIBUTION.md). The cross-repository operation is governed by this portfolio's [Credits and Attribution](../CREDITS_AND_ATTRIBUTION.md) policy.

## Claim ceiling

The public artifact supports this narrow claim:

> **A runnable reconstruction of the early flat-file ChrisAI responsibility shape can be built from surviving historical evidence while explicitly marking reconstruction decisions and gaps.**

It does **not** establish:

- a byte-for-byte checkout of the August 2025 source;
- that every reconstructed line or ordering existed verbatim;
- current deployed Nexus behavior;
- modern Nexus internals or a path to reproduce the private runtime;
- completeness of the surviving historical archive.

The repository is therefore useful lineage evidence and an executable historical reference, not current-production proof.
