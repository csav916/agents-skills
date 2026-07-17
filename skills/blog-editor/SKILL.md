---
name: blog-editor
description: >
  Refines a blog-writer draft into a shorter, more human read while preserving
  its SEO/AEO/GEO signals. Cuts padding, breaks the formulaic H2/H3/FAQ
  template feel, replaces flat/corporate phrasing with a natural voice, and
  strips every em-dash from the final article. Targets roughly 30% shorter
  than the input. Use when user says "edit this blog", "make this less dry",
  "tighten this post", "refine the draft", invokes /blog-editor, or
  automatically as the final phase of /blog-writer.
user-invokable: true
argument-hint: "<paste article or blog-writer output>"
license: MIT
metadata:
  author: custom
  version: "1.1.0"
  category: content
---

# Blog Editor — Refine, Don't Regenerate

Takes a finished (usually blog-writer-generated) draft and edits it into something a
real person will actually finish reading — shorter, less formulaic, more human —
without gutting the SEO/AEO/GEO work already baked into it.

**This is an editing pass, not a rewrite from scratch.** Preserve the article's facts,
sources, and claims. Change how it's said and how much of it needs saying, not what
it says.

**Input format:** `/blog-editor <paste the article, or the full blog-writer output block>`

---

## Autonomy Principle

Run the full edit without stopping to ask questions. If the input is missing obvious
structure (no clear title/H2s), infer it and proceed. Only pause if you're handed
something that isn't a blog draft at all.

---

## Phase 1 — Intake & Lock the Non-Negotiables

Parse the input. If it's a full blog-writer output block, pull the `SEO METADATA`
(primary keyword, slug, meta description) and `SOURCES USED` list directly instead of
re-deriving them.

Identify and lock these as non-negotiable — they must survive editing in some form:

- Primary keyword present in the title, first 100 words, and at least one H2
- At least 2 FAQ-style Q&As survive, answer-first (lead with the direct answer, not a wind-up)
- Heading hierarchy stays clean: H1 → H2 → H3, no skipped levels
- The 3–4 strongest cited stats/facts survive with their `[Source Name]` citation
- Meta description (if present) stays 150–160 characters
- The article still directly answers the original search question in the intro

Everything else — exact word count, exact section count, exact FAQ count, exact
citation count — is negotiable in service of readability.

---

## Phase 2 — Diagnose the Dryness

Read the draft section by section and flag, silently, what's making it a slog:

- **Padding** — sentences that restate a point already made, throat-clearing openers
  ("In this section, we'll cover..."), redundant transitions, filler qualifiers
- **Formulaic structure** — every H2 is the same length and shape (setup → explain →
  example, repeated identically); the FAQ just restates body content verbatim instead
  of adding anything; sections that could obviously be merged because they're really
  one idea split in two
- **Flat, corporate voice** — hedge phrases ("it's important to note," "in today's
  landscape," "overall," "generally speaking"), zero opinion or specificity, no
  rhetorical questions, uniform 15–20 word sentences with no rhythm variation, no
  concrete example a reader can picture

This diagnosis drives Phases 3–4 — don't skip straight to editing without it, or the
cuts end up arbitrary instead of targeted at what's actually dry.

---

## Phase 3 — Cut Pass (Target: ~30% shorter)

Compute the target: current word count × 0.7. State the actual number in the output.

Cut in this order, stopping once you hit the target — don't over-cut past it just
because more could theoretically go:

1. Redundant or restating sentences
2. Throat-clearing intros/outros within each section
3. The weakest, most generic FAQ entries — keep the ones that are specific and
   non-overlapping with the body, cut the ones that just paraphrase a body sentence
4. Merge H2 sections that cover overlapping ground into one section
5. Thin the citation load — keep the 3–4 strongest, cut decorative ones that don't
   change what the reader does with the information

**Never cut:** the keyword-bearing opening line, the strongest FAQ answers, any
concrete example/scenario, the closing call to action.

If the draft is already at or under the target length, skip the cut pass — go
straight to Phase 4. Don't pad it back up.

---

## Phase 4 — Voice Pass (Break the Formula)

- Vary section openings — no two H2s should start with the same grammatical
  construction (e.g., not every section opening with "When it comes to...")
- Replace flat/corporate phrasing with direct, specific, conversational phrasing.
  Cut hedge words ("typically," "generally," "it's worth noting," "in most cases")
  unless they're load-bearing for accuracy
- If the draft doesn't already have one, add a single concrete, specific scenario
  or example the reader can picture — this does more for "human" than any amount of
  word-smithing
- Vary sentence length on purpose. Short sentence. Then one that runs longer to
  explain the why behind it. Uniform sentence length reads as generated even when
  every sentence is individually fine
- Let a point of view show through somewhere — a stance, a caveat, a "here's what
  actually works and here's what doesn't" moment. Neutral information relay is part
  of what makes AI-drafted content feel dry
- If the `humanize-text` skill is available, apply its tone/flow techniques during
  this pass rather than reinventing them here

---

## Phase 5 — Em-Dash Sweep (Mandatory)

Scan the entire edited article for the em-dash character (—) and eliminate every
instance. This step is not optional — the edit is not complete while any remain, and
Phase 7 output must not be delivered until this sweep is clean.

For each em-dash found, replace it with whatever reads most naturally in context, not
just the nearest substitute:

- A comma, if it was setting off a parenthetical
- A period and a new sentence, if it was joining two independent clauses
- A colon, if it was introducing a list or explanation
- Parentheses, if it was a true aside
- "and," "but," or "because," if it was standing in for a connector

Don't just delete the dash and mash the words together — reread the resulting sentence
and rewrite it so it reads naturally, not like punctuation was surgically removed.

Do one final pass over the whole article specifically hunting for em-dashes before
moving to Phase 6. Zero remaining is a hard requirement, not a preference.

---

## Phase 6 — SEO/AEO/GEO Integrity Recheck

Confirm every Phase 1 non-negotiable still holds after cutting and rewriting:

- [ ] Primary keyword in title, first 100 words, ≥1 H2
- [ ] ≥2 FAQ entries remain, answer-first
- [ ] Heading hierarchy still clean (H1 → H2 → H3)
- [ ] 3–4 strongest cited facts retained with citation
- [ ] Intro still directly answers the original search question
- [ ] Meta description still 150–160 characters (if present)
- [ ] Zero em-dashes remain anywhere in the article

If a cut broke one of these, restore the minimum needed to fix it specifically —
don't restore the original text wholesale, that defeats the edit.

---

## Phase 7 — Output

Deliver in this exact format:

```
✂️ EDITED BLOG ARTICLE
=======================

BEFORE → AFTER
---------------
Word Count:   [orig] → [new]  (-[X]%)
Sections:     [orig count] → [new count]   [note any merges/cuts]
FAQ Entries:  [orig count] → [new count]

WHAT CHANGED
------------
- [e.g. "Merged 'Common Mistakes' into 'How to Fix It' — they covered the same ground"]
- [e.g. "Cut 3 generic FAQ entries, kept the 2 most specific"]
- [e.g. "Added a concrete example in the intro; varied section openings"]
- [e.g. "Cut hedge phrasing throughout ('it's important to note', 'generally speaking')"]

---

[FULL EDITED ARTICLE — Markdown, ready to paste into WordPress/CMS]

---

SEO/AEO/GEO INTEGRITY CHECK
-----------------------------
[x] Primary keyword in title, intro, ≥1 H2
[x] FAQ block intact (answer-first)
[x] Heading hierarchy clean
[x] Key stats retained with citation
[x] Still answers the original search question
[x] Zero em-dashes remain
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Input is raw text with no clear headings | Infer H1/H2 structure from paragraph breaks and topic shifts, then proceed |
| Draft is already short/tight (under target) | Skip the cut pass, run voice pass only, note this in the output |
| Cutting would break a non-negotiable and there's no slack left | Keep the element, cut elsewhere instead, and note the exception in WHAT CHANGED |
| Input has no discoverable primary keyword | Infer it from the title/first paragraph and state the assumption |
| Draft leans heavily on em-dashes for sentence structure | Rewrite the underlying sentences, not just swap the punctuation — a wall of comma splices is worse than the em-dashes were |
