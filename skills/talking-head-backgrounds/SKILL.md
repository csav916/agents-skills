---
name: talking-head-backgrounds
description: "Generate a matching set of background images for a talking-head video script, one image per clip/section — or just the enhanced prompts with no API spend, if the user asks for prompts only. Reads each clip's content, tone, and concrete details, turns that into an enhanced Gemini image prompt (with a consistent style and subject-mode selection), and generates the image unless prompts-only is requested. Use when the user pastes a numbered/multi-clip script and asks for background images, video backgrounds, clip backgrounds, B-roll visuals, or just prompts for a talking-head or faceless video."
argument-hint: "[paste numbered script clips] [optional: \"prompts only\"]"
user-invokable: true
license: MIT
compatibility: "Requires a Gemini API key (GEMINI_API_KEY or GOOGLE_AI_API_KEY) from https://aistudio.google.com/apikey"
---

# Talking-Head Background Generator

Turns a clip-by-clip video script into one background image per clip,
generated via Gemini image generation (stdlib REST fallback — no MCP
setup required, just an API key).

## Prerequisites

Check for an API key before doing anything else:
```bash
python "C:\Users\csav7\.claude\skills\talking-head-backgrounds\scripts\generate_image.py" --help
```
(this just validates python/the script are reachable). Then check:
```bash
echo %GEMINI_API_KEY%%GOOGLE_AI_API_KEY%
```
If neither `GEMINI_API_KEY` nor `GOOGLE_AI_API_KEY` is set, ask the user
for a Google AI Studio key (https://aistudio.google.com/apikey) and pass
it per-call with `--api-key`, or offer to set it as a user env var for
future runs. Never print the key back or log it anywhere.

If the user has the `banana`/`nanobanana-mcp` MCP server connected
(check via available tools for `gemini_generate_image`), prefer that
tool instead of the script — same underlying API, no CLI needed.

## Pipeline

### 1. Parse the script into ordered clips

Input looks like numbered clips, each a sentence or two, e.g.:
```
1
47 employees. A freight company operating across three states...
2
The operations director, Marcus Webb, did something simple...
```
Split on the numeric markers (or blank-line-separated paragraphs if no
numbers are present). Strip trailing commas/stray punctuation from
copy-paste artifacts. Preserve clip order — it determines file order.

### 2. Establish one shared style anchor for the whole script

Read the full script once and identify the overall topic/tone (e.g. an
AI business case study). Build a single **style anchor** paragraph
(palette, lighting, mood, camera/render style) that will be reused
unchanged across every clip's prompt, per `references/prompt-formula.md`
→ "Style Anchor". This is what makes the set of images feel like one
continuous video rather than N random pictures. Default to the
"glossy/dramatic/conceptual" anchor in that file — rich contrast,
dramatic single-source light, premium/aspirational mood — unless the
user has asked for a different look.

Confirm the anchor with the user in one line only if the script's topic
is ambiguous; otherwise proceed without asking.

### 3. Analyze each clip, pick a subject mode, and derive a prompt

For each clip, decide which of the two subject modes in
`references/prompt-formula.md` fits:
- **Mode A (person-led stock-photo)** — the clip is about a person, an
  action, or a human outcome (a named character, a team, a result).
- **Mode B (symbolic concept-art)** — the clip is about an idea, a
  mechanism, a system, a choice, or a transformation with no natural
  human actor (render it as one literal visual metaphor, the way a
  robotic arm stands for automation or two doors stand for a choice).

Then extract:
- **Concrete subject** for that mode — a specific person+action (A) or
  a specific metaphor object (B). Prefer literal objects/scenes
  mentioned in the text (a whiteboard, a freight warehouse) over vague
  abstractions.
- **Key details worth rendering** (numbers as visual quantity, not
  literal digits; named artifacts; actions).
- **Tone** (aspirational, tense, triumphant, matter-of-fact) — shades
  the lighting/mood for this clip.

Compose the full prompt: `[style anchor] + [mode A or B subject and
setting] + [presenter overlay note] + [lighting nuance for this clip's
tone]`, following `references/prompt-formula.md` in full. Load that
reference file now if you haven't already. Full-detail compositions
and human subjects front-and-center are fine (per the user's own
reference images) — the only overlay consideration is keeping the
bottom ~15% of frame (or wherever their webcam/PiP sits) relatively
less critical; don't hollow out the whole frame.

Never claim a generated person depicts a real named individual from
the script (e.g. "Marcus Webb") — generate a confident generic
archetype instead, per the safety table.

### 4. Decide output mode: prompts-only or generate

Default to generating images. Switch to **prompts-only** (no API
calls, no cost) if the user's request signals it — e.g. "just the
prompts", "prompts only", "don't generate yet", "without spending on
the API", "show me the prompts first". If ambiguous, ask in one line
rather than assuming — image generation costs real money per call.

**Prompts-only mode:**
- Still do steps 1-3 in full (parse, style anchor, per-clip mode +
  composed prompt).
- Do not call `generate_image.py` or any MCP image tool.
- Print each clip's full composed prompt in the response, numbered to
  match clip order, with the aspect ratio/resolution you'd use noted
  once. Mention the shared style anchor once.
- Don't create the output folder or write any files unless the user
  asks you to save the prompts to disk.
- Tell the user they can generate any subset later ("generate images
  for clips 2 and 5", or "generate all of these") without re-deriving
  the prompts — just reuse what's already been composed.

**Generate mode** continues below.

### 5. Generate

Pick an output folder: `~/Documents/talking_head_backgrounds/<slug>/`
where `<slug>` is a short kebab-case slug of the script's topic (ask
the user for a project name only if you can't derive a reasonable one).

For each clip, in order, call:
```bash
python "C:\Users\csav7\.claude\skills\talking-head-backgrounds\scripts\generate_image.py" \
  --prompt "<composed prompt>" \
  --out "<output_folder>\01_background.png" \
  --aspect-ratio 9:16 --resolution 2K
```
Number files by clip order (`01_`, `02_`, ...). The script also writes
a `.txt` sidecar with the exact prompt next to each image, for
regeneration/tweaking later.

If a call returns `IMAGE_SAFETY` or a block reason, rephrase per the
safety table in the reference doc and retry once before telling the
user it needs a rewrite.

If using the MCP tool instead of the script, call `set_aspect_ratio`
(9:16) once, then `gemini_generate_image` per clip, saving outputs into
the same numbered convention.

### 6. Report back

In generate mode: for each clip, show clip number, one-line prompt
summary, output file path. Mention the shared style anchor once so the
user can see what's holding the set together.

In prompts-only mode: for each clip, show clip number, subject mode
(A/B), and the full composed prompt text — this *is* the deliverable,
so don't summarize it away.

## Cost awareness

Gemini image pricing (approx, gemini-3.1-flash-image-preview):
- 1K: ~$0.04/image · 2K: ~$0.08/image · 4K: ~$0.16/image

For a 5-10 clip script at 2K that's roughly $0.40-$0.80 per full set.
Mention the estimate before generating a full batch. Prompts-only mode
has zero API cost — that's the point of offering it.

## Error handling

| Error | Resolution |
|---|---|
| No API key | Ask for a Google AI Studio key; use `--api-key` or set `GEMINI_API_KEY` |
| `IMAGE_SAFETY` / blocked | Rephrase per safety table in `references/prompt-formula.md`, retry once |
| HTTP 429 (rate limited) | Script auto-retries twice with a 20s backoff; if still failing, wait ~60s |
| Invalid aspect ratio/resolution | Use one of the valid values listed in `scripts/generate_image.py --help` |

## Reference

- `references/prompt-formula.md` — full prompt formula, style-anchor
  template, safe-zone composition rule, safety rephrase table. Load
  on-demand, not needed for parsing/planning steps.
