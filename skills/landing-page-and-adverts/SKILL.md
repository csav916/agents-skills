---
name: landing-page-and-adverts
description: "Create high-converting landing pages and advertisements based on human physiology and conversion psychology data. Use for: building landing pages, writing ad copy, optimizing CRO, and applying psychological triggers."
---

# Landing Page and Adverts Skill

This skill enables the creation of landing pages and advertisements that leverage human physiology and psychological triggers to maximize conversion rates.

## 1. Core Workflow

When a user requests a landing page or advertisement:

1.  **Analyze Intent**: Determine the target audience, the core pain point, and the desired action (CTA).
2.  **Apply Psychology**: Consult `references/conversion_psychology.md` to select the most effective triggers (Scarcity, Urgency, Social Proof, etc.).
3.  **Design Structure**: Follow the best practices in `references/design_best_practices.md` for visual hierarchy and eye-tracking patterns (F-Pattern, Z-Pattern).
4.  **Generate Content**:
    *   For **Landing Pages**: Use the template at `templates/landing_page_template.html`. You can populate it using the script `scripts/render_page.py` with a JSON data structure similar to `references/example_data.json`.
    *   For **Adverts**: Focus on emotional hooks (Greed, Fear, Pride) and benefit-driven headlines.
5.  **Deliver**: Provide the HTML code directly and, if multiple assets are involved, package them into a ZIP file.

## 2. Key Design Principles

*   **Benefit-First Headlines**: Never lead with a feature. Lead with the transformation the user will experience.
*   **The Power of "Above the Fold"**: Ensure the Headline, Subheadline, and primary CTA are visible immediately.
*   **Directional Cues**: Use visual pointers (arrows, gaze) to guide the eye toward the CTA.
*   **AEO (Answer Engine Optimization)**: Structure headings and FAQs to be easily parsed by AI search engines.

## 3. Tool Usage

### Generating a Landing Page
To generate a professional HTML landing page:
1.  Prepare a JSON file with the page content (see `references/example_data.json` for the schema).
2.  Run the rendering script:
    ```bash
    python3 /home/ubuntu/skills/landing-page-and-adverts/scripts/render_page.py data.json output.html
    ```
3.  Read the resulting HTML and provide it to the user.

### Optimizing for Conversion
If a user asks to optimize an existing page:
1.  Read the current page content.
2.  Compare against the benchmarks in `references/conversion_psychology.md`.
3.  Suggest changes based on the "14 Core Elements" found in the research documentation.

## 4. Resource Directory
- `scripts/render_page.py`: Python script to generate HTML from JSON.
- `references/conversion_psychology.md`: Detailed triggers and conversion data.
- `references/design_best_practices.md`: Eye-tracking and structural best practices.
- `templates/landing_page_template.html`: A high-converting Tailwind CSS template.
- `references/example_data.json`: Sample data structure for the landing page.
