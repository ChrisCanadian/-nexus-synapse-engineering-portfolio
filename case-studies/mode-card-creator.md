# Case Study — Nexus Mode Card Creator

## What it is

[Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) is a bounded public authoring tool for turning natural-language behavioral intent into a portable Mode Card.

A Mode Card contains a small, inspectable set of fields such as:

- name and description;
- role;
- instructions;
- communication style;
- boundaries;
- conversation starters.

## Why it was extracted

Nexus has richer private behavioral-mode machinery, but the public project intentionally stops at the **creation boundary**.

The public flow is:

```text
fuzzy human intent
      ↓
guided model-mediated interview
      ↓
ambiguity / contradiction resolution
      ↓
human readback + confirmation
      ↓
portable structured Mode Card
      ↓
STOP
```

## The unusual part

The no-code path is an AI-readable Markdown protocol.

A capable host assistant can read `MODE_CREATOR.md`, run the interview, adapt follow-up questions, ask for confirmation, and output the structured artifact without requiring a Nexus installation.

There is also a small Python reference implementation that performs the same bounded authoring job.

## Authority boundary

A Mode Card describes **behavioral posture**, not authority.

The public creator does not claim to grant:

- tool permission;
- memory access;
- browsing;
- policy exemptions;
- runtime activation;
- identity precedence;
- governance authority.

Host-dependent capabilities are represented conditionally rather than assumed.

## What remains private

The public project intentionally excludes:

- runtime activation or automatic selection;
- numeric behavioral weights;
- scoring/formulas;
- private state reconstruction;
- persistence;
- identity composition;
- memory/preference interaction;
- tool/governance integration;
- host-runtime wiring.

## Why it matters to the portfolio

This artifact demonstrates a different kind of boundary than the proof runtime or acceptance rig:

> **How much of an authoring workflow can be made portable without publishing the machinery that makes the result consequential?**
