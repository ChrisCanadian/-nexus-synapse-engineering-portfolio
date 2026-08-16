# Case Study — Early SSR / Warehouse-Style RAG

## Status

**Historical artifact. Not the current private SSR implementation.**

The retained public gist is an early Structured-SQL-RAG demonstration for AI personality/context management.

## The warehouse analogy

The core idea came from warehouse operations:

> Do not load the whole warehouse and then decide what you need. Determine the job, narrow the eligible inventory, and build the pick list first.

The public gist describes an early flow roughly as:

```text
user query
    ↓
input analysis
    ↓
structured SQL scope/filtering
    ↓
bounded candidate set
    ↓
semantic or contextual selection
    ↓
selective context injection
    ↓
model dispatch
```

## What the historical gist demonstrates

The retained artifact includes examples of:

- SQL-side filtering;
- CTE-based query structure;
- inline context labeling;
- selective injection of communication traits;
- cached reference traits;
- compact prompt assembly;
- summary-bullet memory rather than full conversation dumps;
- fallback behavior for SQL failure, empty caches, and latency spikes;
- execution traces and sample data;
- historical local benchmark material.

The gist explicitly uses the Oracle/WMS “optimized pick list” analogy.

## Evidence discipline

The gist contains multiple benchmark snapshots from 2025 with different reported prompt-reduction/performance figures.

Those numbers should be read as **historical benchmark results under the conditions recorded in the gist**, not as current Nexus performance and not as universal evidence that one retrieval approach always outperforms another.

The architectural lineage is more important than any single percentage:

> **The runtime determines eligible scope before the model receives context.**

That principle later expanded beyond personality retrieval into broader structured state/context reconstruction.

## What it is not

This artifact is not:

- current SSR;
- the private production schema;
- the full memory system;
- evidence that every later use of the term SSR included vector search;
- a reproducible description of the present Nexus runtime.

## Source

Historical public gist:  
https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752
