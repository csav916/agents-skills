# Background Prompt Formula (Talking-Head Videos)

> Load on-demand when composing prompts. Calibrated against the user's
> own reference set: a confident professional at a whiteboard, a robot
> arm sorting mail (automation metaphor), a smart mirror with a HUD
> overlay, and two doors (old-way/new-way metaphor). These are glossy,
> dramatic, hero-shot images — not muted, empty-room plates.

## Two Subject Modes — pick one per clip

**A. Person-led stock-photo mode** — use when the clip is about a
person, an action, or a human outcome (a named character in the
script, a team, a result someone achieved).
- A confident professional (or small group), engaged in a clear action
  or looking straight at camera, in a real business setting.
- Glossy editorial/stock-photo lighting: bright, high-key, or a single
  strong directional source — not flat documentary light.
- Supporting details in the background may carry **legible-looking
  handwritten or diagrammatic marks** (whiteboard scribbles, charts) —
  these read as texture, not literal captions, and are fine here.
- Reference beat: confident businesswoman mid-explanation at a busy
  hand-drawn strategy whiteboard, meeting room behind her, window light.

**B. Symbolic concept-art mode** — use when the clip is about an idea,
a mechanism, a system, a choice, or a transformation (something
abstract that doesn't have a natural human actor).
- Render the abstract idea as one literal, single visual metaphor:
  automation → a robotic arm at work; a decision point → two doors,
  one dark/worn and one glowing; an AI assistant → a smart mirror or
  HUD overlay on a reflection; more to come → a door ajar with light
  spilling through.
- Clean, often minimal or dark backdrop (studio white, or a deep
  moody dark tone) so the metaphor object stays the unmistakable hero.
- Dramatic single-source lighting: a glow, a rim light, a warm light
  spilling from one element against a darker surround.
- Slight CGI/concept-art render quality is welcome here (unlike mode A,
  which should stay photographic).

If unsure which mode fits, default to A for anything with a named
person/role in the sentence, B for anything describing a process,
system, number trend, or abstract choice.

## The 5-Component Brief

Write each prompt as flowing prose (not comma-tag lists):

1. **Subject** — the person/action (mode A) or the metaphor object
   (mode B), described with physical specificity.
2. **Setting** — where this lives; specific enough to feel real (mode
   A) or deliberately minimal so the metaphor reads instantly (mode B).
3. **Composition** — see Presenter Overlay Note below.
4. **Lighting** — glossy/dramatic single-source; the biggest quality
   lever in this style.
5. **Style/technical** — camera + lens for mode A ("shot on Canon EOS
   R5, 35mm"); render/finish descriptor for mode B ("polished CGI
   product-render finish"). End with "ultra-realistic, high
   resolution" rather than a stacked quality-tag list.

## Presenter Overlay Note (soft guidance, not a hard rule)

These sit behind a live presenter, but — per the user's own reference
images — full-detail compositions with human subjects front-and-center
are exactly what has worked before. Don't hollow out the frame or
avoid faces. The only adjustment: keep the **bottom ~15% of the
frame** (or whichever corner holds a small webcam/PiP box) relatively
less critical, so nothing essential to reading the image is lost if
covered. Everywhere else, compose freely and with full detail.

## Style Anchor (consistency across one video)

Derive one shared anchor from the video's topic and reuse it,
word-for-word, across every clip — only Subject/Setting change.

Default anchor ("glossy/dramatic/conceptual", AI business content):
```
Premium editorial/commercial photography finish (mode A) or polished
concept-art CGI finish (mode B). Rich contrast with a dramatic
single-source light — warm golden glow, cool blue tech glow, or bright
key light — rather than flat even lighting. Deep, saturated dark tones
(navy, charcoal, black) contrasted against one warm accent (gold,
amber) or one cool tech accent (blue) per image. Confident, aspirational,
slightly premium mood throughout. Ultra-realistic where photographic,
polished and clean where conceptual, high resolution.
```

## Positive Framing (Gemini has no negative prompts)

- "not flat lighting" → "dramatic single-source light, deep shadows"
- "not cluttered" → "one clear hero subject, uncluttered surround"
- "no boring office" → "premium, aspirational, editorial setting"

## Safety Rephrase (if a generation is blocked)

| Blocked concept | Rephrase |
|---|---|
| Named real person (e.g. a script names "Marcus Webb") | Describe as a generic role/archetype: "a confident operations director in his 40s" — a generated likeness is fine, but never claim it depicts the real named individual |
| Company logos/brands | Generic unbranded equivalents: "a plain whiteboard", "an unbranded dashboard screen" |
| Crisis/loss framing (e.g. "failing business") | Reframe to the visual aftermath/before-state neutrally: "a cluttered, paper-based dispatch office" |

## Worked Examples

**Mode A** — Clip: *"He printed out a 5-step framework and pinned it
to the whiteboard in the ops room."*
```
[style anchor] A confident operations director in his 40s, sleeves
rolled up, stands beside a large whiteboard covered in energetic
handwritten strategy notes and arrows, one hand gesturing toward a
printed sheet pinned at its center showing a simple 5-rung ladder
diagram. Behind him, a bright modern ops room with floor-to-ceiling
windows and a colleague seated at a desk. Shot on Canon EOS R5, 35mm,
bright key light from the windows with deep contrast shadows,
editorial business-photography finish, ultra-realistic, high
resolution.
```

**Mode B** — Clip: *"Automated dispatch notifications. A smarter CRM.
Live dashboards tracking which routes were actually profitable."*
```
[style anchor] A sleek robotic arm with a glowing blue joint accent
moves with precision across a grid of neatly stacked delivery manifests
and route cards on a clean pale wood surface, lifting one glowing card
free of the stack. Minimal white studio backdrop keeps the arm and
cards as the unmistakable hero. Dramatic rim lighting traces the arm's
edges against soft shadow, polished concept-art CGI finish,
ultra-realistic, high resolution.
```
