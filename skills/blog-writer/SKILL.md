---
name: blog-writer
description: >
  Full-pipeline blog article generator. Takes a search question and primary keyword,
  runs keyword research, deep topic research, writes a complete SEO-optimized blog post,
  runs content quality, search experience, and AI visibility checks, then hands the
  draft to the blog-editor skill for a final pass that cuts length and formulaic
  structure so the result reads like it was written by a person. Use when user says
  "write a blog", "blog article", "write me a post", "blog post about", or invokes
  /blog-writer.
user-invokable: true
argument-hint: "<search question> | <primary keyword>"
license: MIT
metadata:
  author: custom
  version: "1.0.0"
  category: content
---

# Blog Writer — Full Pipeline

Automatically researches, writes, and optimizes a complete blog article. No manual steps required.

**Input format:** `/blog-writer <search question> | <primary keyword>`

Example: `/blog-writer how do I fix a leaking pipe? | leaking pipe repair`

---

## Autonomy Principle

Run the full pipeline without stopping to ask questions. Make reasonable assumptions and surface them in the final output. Only pause if the input is completely ambiguous.

---

## Phase 1 — Parse Input

Extract two values from the argument:
- **Search Question** — the query a user would type into Google (e.g., "how do I fix a leaking pipe?")
- **Primary Keyword** — the exact keyword to target (e.g., "leaking pipe repair")

If the user did not use the `|` separator, infer the primary keyword from the search question by identifying the core noun phrase.

---

## Phase 2 — Keyword & Intent Research (run in parallel)

Run both of these simultaneously:

### 2A — Keyword Intelligence (invoke seo-cluster approach)
Using WebSearch, find:
- The top 5 ranking pages for the primary keyword
- What headings/sections they cover (H2/H3 structure)
- Related questions from "People Also Ask"
- Semantic variations and LSI keywords
- Search intent: informational / transactional / navigational / commercial

### 2B — Topic Research (invoke deep-research approach)
Using WebSearch, gather:
- Key facts, statistics, and data points with sources
- Expert opinions or quotes if available
- Common mistakes people make on this topic
- Step-by-step processes or how-to information
- Recent developments (check publication dates)
- At least 5 credible sources to cite

**Compile findings into an internal content brief before writing.**

---

## Phase 3 — Content Brief

Before writing, summarize:

```
CONTENT BRIEF
=============
Search Question: [question]
Primary Keyword: [keyword]
Search Intent: [type]
Target Word Count: [1,500–2,500 words for blog posts]
Key Sections to Cover: [list H2s]
Must-Include Facts: [top 3-5 data points]
People Also Ask to Address: [list]
Semantic Keywords to Include: [list]
```

---

## Phase 4 — Write the Full Blog Article

Write a complete, publish-ready blog post following these rules:

### Structure
- **Title (H1):** Include the primary keyword. Make it compelling and click-worthy. 60 characters max.
- **Meta Description:** 150–160 characters. Include the primary keyword. Write it as a benefit-driven teaser.
- **Introduction (100–150 words):** Hook the reader, state the problem, promise the solution. Include the primary keyword in the first 100 words.
- **Table of Contents:** List all H2 sections as anchor links.
- **Body Sections (H2s):** 4–8 sections. Each H2 should match a user question or topic cluster. Use H3s for sub-points.
- **FAQ Section:** Answer 3–5 "People Also Ask" questions in concise 2–4 sentence answers.
- **Conclusion (100–150 words):** Summarize key takeaways. Include a clear call to action.

### Writing Rules
- Write for a human first, search engine second
- Use short paragraphs (2–4 sentences max)
- Use bullet lists and numbered steps where appropriate
- Use active voice
- Vary sentence length — mix short punchy sentences with longer explanatory ones
- Write at a Grade 8–10 reading level (clear, not dumbed down)
- Include the primary keyword naturally 3–5 times total (never forced)
- Include semantic/LSI keywords throughout
- Cite all facts with [Source Name] inline references
- Add [IMAGE SUGGESTION: description] placeholders where visuals would help
- Add [INTERNAL LINK: topic] placeholders where internal links should go

### Tone
- Confident and helpful, not salesy
- Conversational but credible
- Match the brand voice: knowledgeable expert talking to a real person

---

## Phase 5 — SEO & Quality Optimization (run in parallel after draft)

Apply all three checks simultaneously and revise the article based on findings:

### 5A — Content Quality Check (seo-content approach)
Verify:
- [ ] Primary keyword in H1, first 100 words, and at least one H2
- [ ] Word count meets minimum (1,500 for blog posts)
- [ ] E-E-A-T signals present (facts cited, author-level expertise demonstrated)
- [ ] No thin sections (each H2 has at least 150 words)
- [ ] No keyword stuffing (density stays 1–3%)
- [ ] Readability: sentences average 15–20 words

### 5B — Search Experience Check (seo-sxo approach)
Verify:
- [ ] Content matches the search intent identified in Phase 2
- [ ] The article directly answers the search question in the introduction
- [ ] People Also Ask questions are answered in the FAQ
- [ ] Content depth matches or exceeds the top-ranking competitors found in Phase 2
- [ ] No content gaps vs. top 5 competitors

### 5C — AI Search Visibility Check (seo-geo approach)
Verify:
- [ ] Article contains clear, quotable statements (facts with numbers/specifics)
- [ ] Answer-first format on key questions (direct answer before elaboration)
- [ ] Heading hierarchy is clean: H1 → H2 → H3
- [ ] Key data points are in lists or tables (easily extractable by AI)
- [ ] Content can stand alone as a cited source

---

## Phase 6 — Editorial Refinement (invoke blog-editor)

The Phase 5 draft is SEO-solid but reliably runs long and formulaic — that's expected
at this stage, it's what Phase 6 exists to fix. Invoke the `blog-editor` skill on the
full Phase 5 draft (article + SEO metadata + sources) to:

- Cut the draft by roughly 30%, removing padding and redundant sections
- Break the rigid H2/H3/FAQ template feel and vary structure/section openings
- Replace flat or corporate phrasing with a natural, human voice
- Recheck SEO/AEO/GEO integrity after cutting (keyword placement, FAQ block,
  heading hierarchy, strongest citations, answer-first intro) and restore anything
  a cut broke

Use blog-editor's output — the edited article plus its BEFORE → AFTER summary and
integrity check — as the basis for Phase 7. Don't perform a separate manual polish
pass here; that's blog-editor's job.

---

## Phase 7 — Final Output

Deliver the finished, edited article in this exact format:

---

```
📄 FINISHED BLOG ARTICLE
========================

SEO METADATA
------------
Title: [H1 title]
Meta Description: [150-160 chars]
Primary Keyword: [keyword]
Target URL Slug: /[suggested-slug]
Word Count: [final word count]  (drafted at [pre-edit count], edited -[X]%)

---

[FULL EDITED ARTICLE — formatted in Markdown, ready to paste into WordPress/CMS]

---

OPTIMIZATION SCORECARD
-----------------------
Content Quality:     [score]/100
SEO Optimization:    [score]/100
AI Search Ready:     [score]/100
Readability Grade:   [grade level]

EDITORIAL SUMMARY (from blog-editor)
-------------------------------------
[WHAT CHANGED bullets from blog-editor's output]

SOURCES USED
------------
1. [Source name + URL]
2. ...

IMAGE PLACEHOLDERS
------------------
[List all [IMAGE SUGGESTION] placeholders with recommended alt text]

INTERNAL LINK OPPORTUNITIES
----------------------------
[List all [INTERNAL LINK] placeholders with suggested anchor text]
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| No primary keyword provided | Infer it from the search question and state the assumption |
| Topic has very little online data | Note the gap, write from first principles, flag low-confidence sections |
| Search question is too broad | Narrow it to the most likely informational intent and state the assumption |
| Conflicting information found | Cite both sources, present the consensus view, note the disagreement |
