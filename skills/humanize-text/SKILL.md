---
name: humanize-text
description: Transforms AI-generated text to sound more natural, conversational, and human-like by improving tone, flow, and authenticity. Use when text sounds robotic, overly formal, or needs to be more engaging and readable. Improves writing quality, not designed to evade AI detectors.
---

# Humanize Text Skill

## Overview

This skill transforms AI-generated or overly formal text into natural, conversational writing that sounds authentically human. It improves readability, engagement, and tone while preserving technical accuracy and meaning.

**Important Disclaimer**: This skill is designed to improve writing quality, naturalness, and reader engagement. It is NOT designed or intended to evade AI detection systems. The focus is on creating better, more effective communication.

## When to Use This Skill

Trigger this skill when:
- Text sounds robotic, stilted, or overly formal
- Writing lacks personality or conversational flow
- Sentence structure is too uniform or predictable
- Content needs to be more engaging for human readers
- User explicitly requests "humanizing" or "naturalizing" text
- Text contains common AI writing patterns (excessive use of "delve", "leverage", "robust", etc.)

## Core Capabilities

### Humanization Techniques

The skill applies multiple strategies to create natural-sounding text:

1. **Sentence Variety**: Mix short, punchy sentences with longer, flowing ones
2. **Natural Contractions**: Use "don't", "we'll", "it's" where appropriate
3. **Transition Diversity**: Vary connecting words and phrases
4. **Pattern Breaking**: Remove repetitive AI writing markers
5. **Personality Injection**: Add voice based on target tone
6. **Strategic Imperfections**: Include natural informalities (not errors)
7. **Paragraph Flow**: Vary paragraph lengths for better rhythm
8. **Rhetorical Elements**: Add questions, asides, or conversational hooks

### Supported Tones

- **Professional**: Polished but approachable business writing
- **Casual**: Relaxed, friendly, everyday conversation
- **Conversational**: Direct dialogue with the reader
- **Storytelling**: Narrative-driven, engaging flow
- **Technical-but-friendly**: Expert knowledge without jargon walls

## Usage

### Basic Command

```bash
python scripts/humanize.py input.txt --tone casual --output humanized.txt
```

### With Comparison

```bash
python scripts/humanize.py input.txt --tone professional --compare
```

### From stdin

```bash
echo "Your text here" | python scripts/humanize.py --tone conversational
```

### Parameters

- `input`: Input file path or text from stdin
- `--tone`: Tone mode (professional, casual, conversational, storytelling, technical-friendly)
- `--formality`: Formality level (1-10, default: 5)
- `--audience`: Target audience (general, technical, business, creative)
- `--output`: Output file path (optional)
- `--compare`: Show side-by-side before/after comparison
- `--preserve-structure`: Maintain original paragraph breaks strictly

## Workflow

1. **Analyze Input**: Detect current tone, formality, and AI patterns
2. **Apply Transformations**: Use tone-specific strategies from `assets/tone-templates.json`
3. **Pattern Replacement**: Remove common AI markers (see `references/humanization-patterns.md`)
4. **Flow Enhancement**: Improve transitions and sentence variety
5. **Quality Check**: Verify meaning preservation and coherence
6. **Output**: Return humanized text with optional comparison

## Reference Files

- **humanization-patterns.md**: Comprehensive guide to AI writing patterns and human alternatives
- **tone-templates.json**: Configuration templates for different writing voices

## Example Transformation

**Before**:
> It is important to note that the implementation of this solution will significantly enhance the overall efficiency of the system. Furthermore, it will leverage cutting-edge technology to deliver robust results.

**After** (Casual tone):
> Here's the thing: this solution will make your system way more efficient. Plus, it uses the latest technology to deliver solid results.

**After** (Professional tone):
> This solution will boost your system's efficiency significantly. It uses cutting-edge technology to deliver reliable, high-quality results.

## Dependencies

- Python 3.8+
- Standard library only (no external dependencies required)
- Optional: `colorama` for colored terminal output in comparison mode

## Best Practices

1. **Preserve Meaning**: Never sacrifice accuracy for style
2. **Context Matters**: Email tone differs from blog post tone
3. **Know Your Audience**: Technical audiences accept different patterns than general readers
4. **Test Output**: Always review humanized text for appropriateness
5. **Iterate if Needed**: Run multiple times with different settings for best results

## Limitations

- Cannot add factual content not present in the original
- May require manual refinement for highly specialized content
- Effectiveness varies by input text quality
- Not a substitute for human editing in high-stakes contexts
