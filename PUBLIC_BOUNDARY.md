# Public Boundary

This repository is a **public engineering portfolio**, not a reproducible specification of the private Nexus Synapse runtime.

The public package that this portfolio is built from was explicitly scoped as a high-level architectural narrative for engineering leaders, hiring managers, technical collaborators, and interested peers. It was designed to explain the design decisions and verification philosophy without exposing production internals.

## Public material may include

- high-level architecture;
- architectural evolution and named epochs;
- public-safe diagrams;
- historical design artifacts;
- evidence categories and verification methodology;
- bounded reference implementations;
- sanitized case studies;
- public benchmarks where the conditions can be explained;
- links to released public repositories and research material.

## Intentionally excluded

To protect private implementation details and operational security, this portfolio does not publish:

- detailed production subsystem boundaries or internal APIs;
- production database schemas, table names, or exact query patterns;
- exact provider routing, entitlement, or capability-selection logic;
- raw SSR ordering, thresholds, weighting, or private assembly rules;
- private prompts or identity-composition mechanics;
- deployment scripts, environment configuration, operational runbooks, or private infrastructure paths;
- current private defect lists, disconnected paths, or migration gaps;
- credentials, secrets, private endpoints, or user/customer data;
- production conversations, memories, reflections, traces, or logs.

## Public artifacts are bounded

The public reference projects linked from this portfolio are intentionally narrow.

They are **not fragments intended to be combined into a clone of Nexus**.

For example:

- **Nexus Proof Runtime** demonstrates a receipt-backed authorization/execution/evidence pattern.
- **Live Runtime Acceptance Rig** demonstrates safe live-boundary acceptance and evidence retention.
- **Nexus Mode Card Creator** demonstrates bounded behavioral-profile authoring.
- The historical SSR gist demonstrates an early SQL-guided context-selection approach.

Each artifact has its own public boundary and claim ceiling.

## Evidence language

This portfolio prefers conservative language:

- **implemented in source** over **live**;
- **exercised by a retained rig** over **fully tested**;
- **operational at the recorded date** over **durable**;
- **isolated V5 reconstruction** over **V5 release**;
- **reference kernel** over **production subsystem**;
- **evidence supports** over **proves** when the available evidence is partial.

The purpose of these distinctions is not to weaken the project history. It is to keep architecture claims attached to the strongest evidence actually available.

## Licensing

Separate public repositories retain their own licenses.

No license in a linked public artifact should be interpreted as granting rights to unpublished Nexus Synapse runtime code, private repositories, private data, prompts, schemas, or other material that is not actually published under that license.

Return to the [portfolio README](README.md).
