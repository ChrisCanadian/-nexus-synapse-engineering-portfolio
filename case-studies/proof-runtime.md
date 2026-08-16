# Case Study — Nexus Proof Runtime

## What it is

[Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) is a standalone public reference project for receipt-backed execution and artifact evidence.

Its core public statement is simple:

> Models can propose actions. The runtime decides whether an action is authorized, executes a versioned tool contract, records what happened, verifies produced artifacts, and checks claims against evidence before an application presents them as fact.

## Why it was extracted

During Nexus development, proposal, authorization, execution, and narration increasingly became separate responsibilities.

The public reference kernel makes that control pattern inspectable without publishing the private Nexus conversation runtime, memory implementation, SSR selection logic, identity system, production schemas, provider configuration, or operational data.

## Public control chain

```text
trusted principal + scope
        ↓
capability / manifest exposure
        ↓
policy + approval checks
        ↓
validated execution
        ↓
runtime-owned receipt
        ↓
artifact verification
        ↓
claim verification
```

## What the public project demonstrates

The repository documents and tests mechanisms including:

- deny-by-default permissions and approvals;
- trusted host identity that model arguments cannot override;
- versioned tool contracts;
- schema validation;
- scoped idempotent replay;
- runtime-owned terminal receipts;
- owner-bound atomic artifact writes;
- SHA-256 tamper detection;
- trusted-context claim verification;
- offline deterministic tests.

## What it does not establish

The project explicitly does not include:

- Nexus SSR;
- Nexus memory or personalization;
- private identity composition;
- autonomous planning loops;
- production authentication/network isolation;
- private provider or deployment configuration.

It is a **reference kernel**, not a production Nexus subsystem.

## Why it matters to the portfolio

This is the clearest executable example of a recurring Nexus principle:

```text
proposal ≠ authority ≠ execution ≠ evidence ≠ narration
```

The project exists so that principle can be reviewed as code instead of accepted as an architectural claim.
