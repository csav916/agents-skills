---
name: lead-pipeline
description: >
  Chains the maps-lead-finder and lead-researcher agents into one command: scrapes
  Google Maps for businesses without websites in a given area, then enriches the
  resulting list with owner names and/or emails from public sources. Use when user
  says "find me leads", "build a lead list", "find businesses without websites and
  get their owners/emails", or invokes /lead-pipeline.
user-invokable: true
argument-hint: "<business type> in <location> | owner|email|both"
license: MIT
metadata:
  author: custom
  version: "1.0.0"
  category: lead-gen
---

# Lead Pipeline — Maps Scrape + Owner/Email Research

Runs the full lead-gen pipeline end to end: find no-website businesses on Google Maps,
then research their owners and/or emails. No manual hand-off between agents required.

**Input format:** `/lead-pipeline <business type> in <location> | owner|email|both`

Example: `/lead-pipeline handyman businesses in Southern Oregon | both`

---

## Phase 1 — Parse Input

Extract from the argument:
- **Business type / query** — what kind of business to search for (e.g. "handyman businesses", "plumbers")
- **Location** — city, region, or state. If it's a region rather than a single city, don't resolve it yourself — `maps-lead-finder` already handles multi-city expansion internally, just pass the region through as given.
- **Enrichment scope** — `owner`, `email`, or `both`. If the user didn't specify this (no `|` segment, or ambiguous phrasing), ask before running anything — enrichment is the slowest and most credit/time-costly part of the pipeline, so don't guess and burn a run on the wrong scope.

## Phase 2 — Run maps-lead-finder

Invoke the `maps-lead-finder` agent **in the foreground** (`run_in_background: false` — Phase 3 needs its output path before it can start). Give it a self-contained prompt with the business type and location from Phase 1.

From its result, capture:
- The exact output CSV path (should be in `C:\Users\csav7\Downloads\`)
- The total business count found
- Any anomalies it flagged (category drift, coordinate mismatches, etc.)

If it finds zero businesses, stop here — report that to the user rather than proceeding to Phase 3 with an empty file.

## Phase 3 — Run lead-researcher

Invoke the `lead-researcher` agent **in the foreground**, passing:
- The exact CSV path from Phase 2
- The enrichment scope from Phase 1 (owner / email / both)

It will write the enriched file as `<original-name>_enriched.csv` in the same Downloads folder and report a hit-rate summary (how many rows got a real value vs. stayed blank).

## Phase 4 — Final Report

Give the user one consolidated summary, not two separate agent reports pasted back to back:

```
LEAD PIPELINE COMPLETE
=======================
Search: [business type] in [location]
Businesses found (no website): [count]  ([per-city/area breakdown if multi-city])
Enrichment: [owner / email / both]
  Owner names found: [X] / [total]   (if applicable)
  Emails found:      [X] / [total]   (if applicable)

File: C:\Users\csav7\Downloads\[filename]_enriched.csv

Flags: [any anomalies from either phase worth a manual look — coordinate
mismatches, low-confidence registry matches, category drift]
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Enrichment scope not specified | Ask before running Phase 2 — don't default to "both" |
| `BROWSERACT_API_KEY` missing/empty (surfaced by maps-lead-finder) | Stop, tell the user to set it, don't proceed to Phase 3 |
| maps-lead-finder finds 0 businesses | Stop after Phase 2, report zero results, skip research entirely |
| lead-researcher can't find owner/email for most rows | Still deliver the file — report the low hit rate plainly rather than treating it as a failure |
| Region resolves to an unusually large number of cities/businesses | Before Phase 2, tell the user the rough scope (city count, est. credits) and confirm if it looks like a large/expensive run |
