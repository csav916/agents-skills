---
name: local-opportunity
description: "Local market opportunity scanner. Input a city, category, and keyword to identify whether the market replicates the 'NOLA Pattern' — weak competition ranking #1 with basic on-page SEO and no backlinks. Scores the top 10 SERP competitors on 10 weakness signals and outputs an Opportunity Score with an actionable entry plan. Use when user says: local opportunity, market research, rank in [city], find rankable market, replicate [site] success, local SEO gap, or city + keyword + opportunity."
user-invokable: true
argument-hint: "<city> <category> <keyword>"
license: MIT
metadata:
  author: custom
  version: "1.0.0"
  category: seo
---

# Local Market Opportunity Scanner

## Purpose

Identify local markets where a new site can rank on page 1 of Google with basic on-page SEO and minimal backlinks — the same pattern that puts autoglassnola.com at #1 for "New Orleans auto glass" despite zero schema, ~1 backlink, and no citations.

**Inputs (from skill arguments):**
- `city` — target city (e.g., "Houston", "Austin TX", "Baton Rouge Louisiana")
- `category` — business type (e.g., "auto glass", "plumber", "roofing", "HVAC")
- `keyword` — primary search phrase (e.g., "windshield replacement", "emergency plumber", "roof repair")

**Invocation example:**
```
/local-opportunity Houston "auto glass" "windshield replacement"
```

---

## The NOLA Pattern — Your Benchmark

Before scoring, internalize what a HIGH opportunity market looks like. autoglassnola.com ranks #1 in New Orleans because:

| Signal | What was found |
|--------|---------------|
| SERP competitors | All small local sites — no national brands in top 3 |
| Schema markup | Zero schema on any competitor page |
| Review signals | Competitors had <40 reviews on average |
| Citations | No BBB, no Chamber, no Angi for most competitors |
| On-page basics | Titles/H1s had city keywords but nothing else |
| Backlinks | Near-zero for all local competitors |
| EMD advantage | autoglassnola.com — keyword + city abbreviation in domain |
| Content | Thin but keyword-matched service pages existed |

A market that matches 6+ of these signals = HIGH opportunity. Fewer = harder.

---

## Step-by-Step Analysis

### Step 1 — Build Search Queries

Construct these exact queries from the user's inputs:

```
PRIMARY:    [keyword] [city]
SECONDARY:  [keyword] [city] [state if not already in city]
LONG-TAIL:  best [keyword] [city]
NEAR-ME:    [keyword] near [city]
```

Example for Houston / auto glass / windshield replacement:
- `windshield replacement Houston`
- `windshield replacement Houston TX`
- `best windshield replacement Houston`
- `windshield replacement near Houston`

### Step 2 — Pull the SERPs

Run WebSearch for the PRIMARY and SECONDARY queries. Collect all results.

Immediately classify each result into one of these buckets:

| Bucket | Examples | Impact |
|--------|----------|--------|
| **National brand** | Safelite, Glass America, AutoGlassOnly, Angi, HomeAdvisor, Yelp, Thumbtack, BBB | Heavy competition signal — hard to displace |
| **Local aggregator** | Yelp city page, Angi city page, Nextdoor | Reduces organic real estate |
| **Local competitor** | Small local business sites | Target for weakness scoring |
| **Directory listing** | YellowPages, Manta, Citysearch | Neutral — shows thin citation landscape |

**Red flag triggers (mark market as HARD immediately):**
- 3+ national brands in top 10
- Yelp + Angi + HomeAdvisor all in top 5 (aggregator wall)
- A local competitor with obvious DA strength (news coverage, large review count, BBB badge)

### Step 3 — Score Each Local Competitor

For each **local competitor** (not national, not aggregator) in the top 10:

Fetch the competitor's homepage with WebFetch. Extract these 10 signals:

#### Competitor Weakness Checklist

Score 1 point per weakness found. Higher score = weaker competitor = more opportunity.

| # | Signal to check | Weakness (score 1) | Strength (score 0) |
|---|----------------|--------------------|--------------------|
| 1 | Schema markup | No JSON-LD or schema found | LocalBusiness or subtype schema present |
| 2 | Title tag | Generic, missing city OR keyword | City + keyword both in title |
| 3 | H1 tag | Missing local intent (no city or service) | City + service in H1 |
| 4 | Reviews on page | No review count, no star rating, no aggregateRating | 10+ reviews, star rating visible or in schema |
| 5 | Google Maps embed | No Maps iframe on page | Maps embed present |
| 6 | Authority citations | No BBB badge, no Chamber link, no press links | Any one of: BBB, Chamber, press mention |
| 7 | Service pages | Single-page site OR no dedicated per-service pages | Dedicated page per core service |
| 8 | Meta description | Missing or duplicate | Unique, keyword-relevant meta description |
| 9 | Mobile/CTA signals | No tel: link, no click-to-call | tel: link present above fold |
| 10 | Content depth | Thin (<300 words), no FAQ, no local specifics | 500+ words, FAQs, local content |

**Competitor weakness score: X/10**

Fetch at least 5 local competitors. If fewer than 3 local competitors exist in the top 10, note this — it means the SERP is dominated by nationals/aggregators (harder market).

### Step 4 — SERP Composition Analysis

After classifying all results, count:

| Metric | Value | Score impact |
|--------|-------|-------------|
| National brands in top 10 | Count | Each = -8 pts from Opportunity Score |
| National brands in top 3 | Count | Each = -15 pts from Opportunity Score |
| Aggregators (Yelp/Angi) in top 5 | Count | Each = -5 pts |
| Local competitors in top 10 | Count | More locals = more beatable |
| Average local competitor weakness | X/10 | Core input to scoring |

### Step 5 — EMD Opportunity Check

An exact-match domain (EMD) is a strong early advantage (e.g., `autoglassnola.com` for auto glass New Orleans).

Check these patterns via WebSearch for whether they exist AND whether they rank:

```
[keyword][cityabbrev].com       → autoglassnola.com, plumberatl.com
[city][keyword].com             → neworleansautoglass.com, houstonplumber.com
[keyword]in[city].com           → autoglassinhouston.com
[keyword][city].com             → windshieldhouston.com
```

**EMD scoring:**
- Pattern is available (not taken) = +10 pts opportunity (EMD can be registered)
- Pattern is taken but by a WEAK site = +5 pts (beatable)
- Pattern is taken by a STRONG site = -5 pts
- Multiple strong EMD competitors = -10 pts

### Step 6 — Review Landscape Check

Run a WebSearch for the Yelp category page in that city:
```
site:yelp.com [category] [city]
```

Check the top 3 Yelp results for the category:
- What is the review count of the #1 Yelp listing?
- What is the average review count of the top 5?

**Review benchmark:**
| Avg top-5 Yelp reviews | Signal |
|------------------------|--------|
| <25 reviews | Very weak market — easy to enter |
| 25-75 reviews | Moderate — manageable |
| 75-200 reviews | Competitive — reviews strategy needed |
| 200+ reviews | Hard — established players |

### Step 7 — Calculate Opportunity Score

```
BASE SCORE: 50

+ (Average competitor weakness score × 5)     [max +50]
  → avg weakness 8/10 = +40, avg 5/10 = +25, avg 3/10 = +15

- (National brands in top 3 × 15)             [up to -45]
- (National brands in top 10, beyond top 3 × 8) [up to -24]
- (Aggregators in top 5 × 5)                  [up to -15]
+ EMD opportunity bonus                        [+10 / +5 / 0 / -5 / -10]
+ Review landscape bonus:
    <25 avg reviews = +10
    25-75 = +5
    75-200 = 0
    200+ = -10

FINAL OPPORTUNITY SCORE: 0–100
```

**Opportunity tiers:**

| Score | Tier | Verdict |
|-------|------|---------|
| 75–100 | 🟢 HIGH | Strong NOLA Pattern match. Enter now with basic on-page + EMD. |
| 50–74 | 🟡 MEDIUM | Winnable but requires schema, citations, and 20+ reviews to compete. |
| 25–49 | 🟠 HARD | Nationals or strong locals present. Needs 6+ months of link building. |
| 0–24 | 🔴 SATURATED | Dominated. Avoid unless significant budget for long-term authority building. |

---

## Output Format

Generate a report with these sections:

---

### LOCAL OPPORTUNITY REPORT — [Keyword] in [City]

**Opportunity Score: XX/100 — [TIER]**
**NOLA Pattern Match: X/8 signals**

#### SERP Composition
| Position | Site | Type | Beatable? |
|----------|------|------|-----------|
| 1 | example.com | Local | Yes |
| 2 | yelp.com | Aggregator | No |
...

#### Competitor Weakness Scores
| Competitor | Weakness Score | Key Gaps |
|------------|---------------|----------|
| site1.com | 8/10 | No schema, no reviews, no Maps |
| site2.com | 6/10 | No schema, thin content |
...

#### EMD Opportunity
- Recommended domain pattern: `[keyword][city].com` or `[city][keyword].com`
- Status: Available / Taken (weak) / Taken (strong)

#### Review Landscape
- Top Yelp competitor reviews: X
- Average top-5 reviews: X
- Difficulty: Easy / Moderate / Hard

#### Score Breakdown
| Factor | Points |
|--------|--------|
| Competitor weakness (avg X/10) | +XX |
| National brands (X in top 3) | -XX |
| Aggregators in top 5 | -XX |
| EMD opportunity | +XX |
| Review landscape | +XX |
| **Total** | **XX/100** |

#### Entry Strategy (if score ≥ 50)

**Minimum to rank in 60–90 days:**
1. Register EMD if available
2. Build site with: title (city+keyword), H1 (city+service), dedicated service page per offering
3. Add LocalBusiness/[subtype] schema with areaServed, geo, telephone, openingHours
4. Claim GBP with correct primary category
5. Claim Yelp, BBB, Bing Places, Apple Business Connect
6. Submit to Data Axle, Foursquare, Neustar (data aggregators)
7. Get 10+ Google reviews within 30 days

**To lock in the ranking (90–180 days):**
1. Build "best of [city] [category]" list placements
2. Join local Chamber of Commerce
3. Create dedicated location pages for nearby cities (non-doorway: 60%+ unique content)
4. Run local digital PR for brand mentions

#### What This Analysis Could NOT Verify
- Exact monthly search volume for the keyword (requires paid tool like DataForSEO or Ahrefs)
- Actual Domain Authority of competitors (requires Moz/Ahrefs API)
- GBP listing strength of competitors (requires geo-grid tool)
- Real-time local pack (3-pack) positions — results vary by searcher location

---

## Batch Mode

If the user provides multiple city/keyword combinations, run them in parallel and produce a comparison table ranked by Opportunity Score:

```
/local-opportunity batch:
  Houston / auto glass / windshield replacement
  Dallas / auto glass / windshield replacement
  San Antonio / auto glass / auto glass repair
```

Output a ranked table:
| Market | Score | Tier | Top Competitor | Avg Weakness |
|--------|-------|------|----------------|--------------|
| Dallas auto glass | 78 | 🟢 HIGH | ... | 7.2/10 |
...

---

## Error Handling

| Scenario | Action |
|----------|--------|
| SERP returns only nationals (no local sites) | Report SATURATED, skip weakness scoring, explain why |
| Fewer than 3 local competitors found | Note thin local market — can be opportunity (easy entry) or niche too small |
| WebFetch blocked on competitor site | Score what's available from the SERP title/description alone; flag as "partial data" |
| City not recognized / too small | Ask user to confirm city name + state; suggest using metro area instead |
| Keyword too broad (e.g. "repair") | Ask user to narrow: "Do you mean [auto repair / windshield repair / appliance repair]?" |

---

## Quick Reference — NOLA Pattern Signals

Use this checklist as a fast gut-check before deep scoring:

- [ ] Top 3 results are all small local sites (no Safelite, no Glass America, no Angi)
- [ ] None of the top 5 have visible schema markup
- [ ] Review counts across top 5 average under 50
- [ ] No BBB badge or Chamber link visible on any top-5 site
- [ ] At least one EMD pattern is available or held by a weak site
- [ ] Yelp is present but NOT in position 1-2
- [ ] Competitors have city keyword in title but miss H1, schema, Maps, citations
- [ ] No single competitor has clear link authority (press mentions, .edu/.gov links, high review count)

**6+ signals checked = enter the market aggressively.**
**3–5 signals = enter with a more complete strategy.**
**<3 signals = find a different market.**
