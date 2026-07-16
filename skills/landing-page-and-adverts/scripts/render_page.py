import sys
import os
import json

def render_template(template_content, data):
    """
    A simple template renderer that handles variables and basic loops for benefits/testimonials.
    """
    result = template_content
    
    # 1. Handle simple variables: {{var_name}}
    for key, value in data.items():
        if not isinstance(value, list):
            result = result.replace(f"{{{{{key}}}}}", str(value))
    
    # 2. Handle Benefits Loop: {{#each benefits}} ... {{/each}}
    if "benefits" in data:
        start_tag = "{{#each benefits}}"
        end_tag = "{{/each}}"
        if start_tag in result and end_tag in result:
            start_idx = result.find(start_tag)
            end_idx = result.find(end_tag) + len(end_tag)
            loop_template = result[start_idx + len(start_tag) : result.find(end_tag)]
            
            loop_content = ""
            for item in data["benefits"]:
                item_html = loop_template
                item_html = item_html.replace("{{this.title}}", item.get("title", ""))
                item_html = item_html.replace("{{this.description}}", item.get("description", ""))
                loop_content += item_html
            
            result = result[:start_idx] + loop_content + result[end_idx:]

    # 3. Handle Testimonials Loop: {{#each testimonials}} ... {{/each}}
    if "testimonials" in data:
        start_tag = "{{#each testimonials}}"
        end_tag = "{{/each}}"
        if start_tag in result and end_tag in result:
            start_idx = result.find(start_tag)
            end_idx = result.find(end_tag) + len(end_tag)
            loop_template = result[start_idx + len(start_tag) : result.find(end_tag)]
            
            loop_content = ""
            for item in data["testimonials"]:
                item_html = loop_template
                item_html = item_html.replace("{{this.quote}}", item.get("quote", ""))
                item_html = item_html.replace("{{this.author}}", item.get("author", ""))
                item_html = item_html.replace("{{this.role}}", item.get("role", ""))
                loop_content += item_html
            
            result = result[:start_idx] + loop_content + result[end_idx:]
            
    return result

def main():
    if len(sys.argv) < 3:
        print("Usage: python render_page.py <data.json> <output.html>")
        return

    json_path = sys.argv[1]
    output_path = sys.argv[2]
    template_path = os.path.join(os.path.dirname(__file__), "../templates/landing_page_template.html")

    if not os.path.exists(json_path):
        print(f"Error: JSON file not found at {json_path}")
        return

    with open(json_path, 'r') as f:
        data = json.load(f)

    with open(template_path, 'r') as f:
        template_content = f.read()

    rendered_html = render_template(template_content, data)

    with open(output_path, 'w') as f:
        f.write(rendered_html)

    print(f"Successfully rendered landing page to {output_path}")

if __name__ == "__main__":
    main()
