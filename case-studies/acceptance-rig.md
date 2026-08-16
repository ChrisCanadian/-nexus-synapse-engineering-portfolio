# Case Study — Live Runtime Acceptance Rig

## What it is

[Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) is a small Python framework for exercising a real application boundary, verifying durable effects in its backing store, and exporting reviewable evidence.

It deliberately separates:

- **runtime execution success** — did the framework complete its campaign and preserve evidence?
- **acceptance outcome** — did the tested target satisfy the acceptance checks?

A failed acceptance check can therefore be a valid and useful campaign result.

## Why it was extracted

Nexus operational history repeatedly exposed the difference between:

```text
code exists
      ≠
imports work
      ≠
service is reachable
      ≠
request path is active
      ≠
durable state changed correctly
```

The rig turns that lesson into a reusable public framework.

## Public campaign shape

```text
preflight
  ↓
protected-state inventory
  ↓
verified backup before writes
  ↓
exercise real application boundary
  ↓
durable readback
  ↓
protected-state comparison
  ↓
PASS / FAIL / SKIP ledger
  ↓
reviewable evidence bundle
```

## What it demonstrates

The public project documents and tests:

- verified pre-write backup;
- explicit runtime/database adapters;
- marker-scoped test resources;
- durable backing-store readback;
- protected-state comparison;
- explicit `PASS / FAIL / SKIP`;
- retained evidence after partial/failing campaigns;
- cleanup manifests without automatic broad deletion;
- public-safe redaction guidance.

## What it does not establish

The framework does not:

- automatically understand arbitrary applications;
- certify Nexus;
- make testing production risk-free;
- prove backups are restorable;
- replace project-specific unit/integration testing;
- eliminate the need for project-specific adapter review.

## Why it matters to the portfolio

The rig represents a verification shift from “the API said it worked” to:

> **What durable evidence exists after the real boundary was exercised?**
