import sys
import json

def generate_queries(tool_name):
    queries = [
        f"{tool_name} for small business tutorial",
        f"{tool_name} ROI for contractors",
        f"{tool_name} save time and money SMB",
        f"{tool_name} lead generation small business",
        f"{tool_name} vs manual workflow ROI"
    ]
    return queries

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tool = sys.argv[1]
        print(json.dumps(generate_queries(tool)))
    else:
        print("Usage: python3 generate_queries.py <tool_name>")
