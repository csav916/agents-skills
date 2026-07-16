#!/usr/bin/env python3
"""
Humanize Text Script
Transforms AI-generated or overly formal text into natural, conversational writing.
"""

import re
import sys
import json
import random
import argparse
from pathlib import Path
from typing import Dict, List, Tuple


class TextHumanizer:
    """Main class for humanizing text with various strategies."""
    
    def __init__(self, tone: str = "casual", formality: int = 5, audience: str = "general"):
        self.tone = tone
        self.formality = formality
        self.audience = audience
        self.tone_config = self._load_tone_config()
        
    def _load_tone_config(self) -> Dict:
        """Load tone configuration from assets."""
        config_path = Path(__file__).parent.parent / "assets" / "tone-templates.json"
        try:
            with open(config_path, 'r') as f:
                data = json.load(f)
                return data.get(self.tone, data.get("casual", {}))
        except FileNotFoundError:
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """Fallback configuration if JSON not found."""
        return {
            "contractions": True,
            "sentence_variety": True,
            "casual_transitions": True,
            "rhetorical_questions": False,
            "personality_words": []
        }
    
    def humanize(self, text: str) -> str:
        """Main humanization pipeline."""
        text = self._remove_ai_patterns(text)
        text = self._add_contractions(text)
        text = self._vary_sentence_structure(text)
        text = self._improve_transitions(text)
        text = self._add_personality(text)
        text = self._vary_paragraph_length(text)
        text = self._cleanup(text)
        return text
    
    def _remove_ai_patterns(self, text: str) -> str:
        """Remove common AI writing markers."""
        ai_patterns = {
            r'\bdelve into\b': 'explore',
            r'\bdelve\b': 'dive into',
            r'\bleverage\b': 'use',
            r'\butilize\b': 'use',
            r'\brobust\b': 'strong',
            r'\bin order to\b': 'to',
            r'\bfor the purpose of\b': 'to',
            r'\bdue to the fact that\b': 'because',
            r'\bat this point in time\b': 'now',
            r'\bin the event that\b': 'if',
            r'\bprior to\b': 'before',
            r'\bsubsequent to\b': 'after',
            r'\bit is important to note that\b': '',
            r'\bit should be noted that\b': '',
            r'\bfurthermore\b': self._random_transition(['also', 'plus', 'and', 'on top of that']),
            r'\bmoreover\b': self._random_transition(['also', 'plus', 'what\'s more']),
            r'\bin conclusion\b': self._random_transition(['so', 'overall', 'to wrap up', 'in the end']),
            r'\bthe aforementioned\b': 'this',
            r'\baforementioned\b': 'this',
            r'\bthe aforementioned\b': 'the',
            r'\bexemplify\b': 'show',
            r'\bparadigm\b': 'model',
            r'\bsynergize\b': 'work together',
        }
        
        for pattern, replacement in ai_patterns.items():
            if callable(replacement):
                text = re.sub(pattern, lambda m: replacement(), text, flags=re.IGNORECASE)
            else:
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Remove excessive formality phrases
        text = re.sub(r'\bIt is (?:worth noting|important to mention|crucial to understand) that\b\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bOne must (?:consider|note|understand)\b', 'Consider', text, flags=re.IGNORECASE)
        
        return text
    
    def _random_transition(self, options: List[str]):
        """Return a function that picks random transition."""
        def picker():
            return random.choice(options)
        return picker
    
    def _add_contractions(self, text: str) -> str:
        """Add natural contractions based on tone."""
        if not self.tone_config.get("contractions", True):
            return text
        
        if self.formality > 7:
            return text
        
        contractions = {
            r'\bis not\b': "isn't",
            r'\bare not\b': "aren't",
            r'\bwas not\b': "wasn't",
            r'\bwere not\b': "weren't",
            r'\bhas not\b': "hasn't",
            r'\bhave not\b': "haven't",
            r'\bhad not\b': "hadn't",
            r'\bwill not\b': "won't",
            r'\bwould not\b': "wouldn't",
            r'\bdo not\b': "don't",
            r'\bdoes not\b': "doesn't",
            r'\bdid not\b': "didn't",
            r'\bcan not\b': "can't",
            r'\bcannot\b': "can't",
            r'\bcould not\b': "couldn't",
            r'\bshould not\b': "shouldn't",
            r'\bmight not\b': "mightn't",
            r'\bmust not\b': "mustn't",
            r'\bI will\b': "I'll",
            r'\byou will\b': "you'll",
            r'\bwe will\b': "we'll",
            r'\bthey will\b': "they'll",
            r'\bI am\b': "I'm",
            r'\byou are\b': "you're",
            r'\bwe are\b': "we're",
            r'\bthey are\b': "they're",
            r'\bit is\b': "it's",
            r'\bthat is\b': "that's",
            r'\bwho is\b': "who's",
            r'\bwhat is\b': "what's",
            r'\bI have\b': "I've",
            r'\byou have\b': "you've",
            r'\bwe have\b': "we've",
            r'\bthey have\b': "they've",
        }
        
        # Apply contractions probabilistically based on formality
        contraction_rate = max(0.3, 1.0 - (self.formality / 10.0))
        
        for pattern, contraction in contractions.items():
            def maybe_contract(match):
                return contraction if random.random() < contraction_rate else match.group(0)
            text = re.sub(pattern, maybe_contract, text, flags=re.IGNORECASE)
        
        return text
    
    def _vary_sentence_structure(self, text: str) -> str:
        """Add sentence variety by occasionally combining or splitting sentences."""
        sentences = re.split(r'([.!?]+\s+)', text)
        result = []
        i = 0
        
        while i < len(sentences):
            sentence = sentences[i].strip()
            
            if not sentence:
                i += 1
                continue
            
            # Occasionally split long sentences
            if len(sentence.split()) > 25 and random.random() < 0.3:
                # Try to split at comma or conjunction
                split_match = re.search(r'(,\s+(?:and|but|or|yet|so)\s+)', sentence)
                if split_match:
                    parts = sentence.split(split_match.group(1), 1)
                    result.append(parts[0].strip() + '.')
                    result.append(' ')
                    result.append(parts[1].strip())
                else:
                    result.append(sentence)
            else:
                result.append(sentence)
            
            # Add separator if it exists
            if i + 1 < len(sentences):
                i += 1
                result.append(sentences[i])
            
            i += 1
        
        return ''.join(result)
    
    def _improve_transitions(self, text: str) -> str:
        """Vary transition words and phrases."""
        paragraphs = text.split('\n\n')
        improved = []
        
        for para in paragraphs:
            # Add occasional conversational hooks
            if self.tone in ['casual', 'conversational'] and random.random() < 0.2:
                hooks = ["Here's the thing:", "Look,", "So,", "Now,", "Listen,"]
                if not para.strip().startswith(tuple(hooks)):
                    para = random.choice(hooks) + " " + para.strip()
            
            improved.append(para)
        
        return '\n\n'.join(improved)
    
    def _add_personality(self, text: str) -> str:
        """Inject personality words and phrases based on tone."""
        personality_words = self.tone_config.get("personality_words", [])
        
        if self.tone == "casual":
            casual_insertions = {
                r'\breally\b': self._sometimes(['really', 'actually', 'honestly', 'truly']),
                r'\bvery\b': self._sometimes(['very', 'pretty', 'quite', 'super']),
            }
            for pattern, replacement in casual_insertions.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Add rhetorical questions occasionally
        if self.tone_config.get("rhetorical_questions", False) and random.random() < 0.1:
            sentences = text.split('. ')
            if len(sentences) > 2:
                insert_pos = random.randint(1, len(sentences) - 1)
                questions = [
                    "Why does this matter?",
                    "What does this mean?",
                    "How so?",
                    "Why is this important?"
                ]
                sentences.insert(insert_pos, random.choice(questions))
                text = '. '.join(sentences)
        
        return text
    
    def _sometimes(self, options: List[str]):
        """Return random choice from options."""
        return random.choice(options)
    
    def _vary_paragraph_length(self, text: str) -> str:
        """Ensure paragraphs aren't all the same length."""
        paragraphs = text.split('\n\n')
        
        if len(paragraphs) <= 2:
            return text
        
        # Occasionally combine short paragraphs or split long ones
        result = []
        i = 0
        
        while i < len(paragraphs):
            para = paragraphs[i].strip()
            
            if not para:
                i += 1
                continue
            
            # If paragraph is very short and next exists, sometimes combine
            if len(para.split()) < 15 and i + 1 < len(paragraphs) and random.random() < 0.3:
                next_para = paragraphs[i + 1].strip()
                combined = para + ' ' + next_para
                result.append(combined)
                i += 2
            else:
                result.append(para)
                i += 1
        
        return '\n\n'.join(result)
    
    def _cleanup(self, text: str) -> str:
        """Final cleanup pass."""
        # Fix double spaces
        text = re.sub(r' +', ' ', text)
        # Fix space before punctuation
        text = re.sub(r' +([.!?,;:])', r'\1', text)
        # Fix multiple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        # Capitalize after periods
        text = re.sub(r'([.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)
        # Fix spacing around quotes
        text = re.sub(r'"\s+', '"', text)
        text = re.sub(r'\s+"', '"', text)
        
        return text.strip()


def create_comparison(original: str, humanized: str) -> str:
    """Create side-by-side comparison."""
    try:
        from colorama import init, Fore, Style
        init()
        has_color = True
    except ImportError:
        has_color = False
    
    comparison = []
    comparison.append("=" * 80)
    comparison.append("BEFORE (Original):")
    comparison.append("=" * 80)
    comparison.append(original)
    comparison.append("\n" + "=" * 80)
    
    if has_color:
        comparison.append(Fore.GREEN + "AFTER (Humanized):" + Style.RESET_ALL)
    else:
        comparison.append("AFTER (Humanized):")
    
    comparison.append("=" * 80)
    comparison.append(humanized)
    comparison.append("=" * 80)
    
    return '\n'.join(comparison)


def main():
    parser = argparse.ArgumentParser(
        description="Humanize AI-generated text to sound more natural and conversational."
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='Input file path (or use stdin)'
    )
    parser.add_argument(
        '--tone',
        choices=['professional', 'casual', 'conversational', 'storytelling', 'technical-friendly'],
        default='casual',
        help='Tone/voice to apply (default: casual)'
    )
    parser.add_argument(
        '--formality',
        type=int,
        choices=range(1, 11),
        default=5,
        help='Formality level 1-10 (default: 5)'
    )
    parser.add_argument(
        '--audience',
        choices=['general', 'technical', 'business', 'creative'],
        default='general',
        help='Target audience (default: general)'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--compare',
        action='store_true',
        help='Show before/after comparison'
    )
    parser.add_argument(
        '--preserve-structure',
        action='store_true',
        help='Maintain original paragraph breaks strictly'
    )
    
    args = parser.parse_args()
    
    # Read input
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                original_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.", file=sys.stderr)
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print("Error: No input provided. Use a file or pipe text to stdin.", file=sys.stderr)
            print("Example: python humanize.py input.txt", file=sys.stderr)
            print("Example: echo 'text' | python humanize.py", file=sys.stderr)
            sys.exit(1)
        original_text = sys.stdin.read()
    
    if not original_text.strip():
        print("Error: Input text is empty.", file=sys.stderr)
        sys.exit(1)
    
    # Humanize
    humanizer = TextHumanizer(
        tone=args.tone,
        formality=args.formality,
        audience=args.audience
    )
    
    humanized_text = humanizer.humanize(original_text)
    
    # Output
    if args.compare:
        output_text = create_comparison(original_text, humanized_text)
    else:
        output_text = humanized_text
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"Humanized text written to: {args.output}", file=sys.stderr)
    else:
        print(output_text)


if __name__ == "__main__":
    main()
