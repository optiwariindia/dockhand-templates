#!/usr/bin/env python3
"""
Dockhand Template Index Generator
Scans the `templates/` directory and compiles all `template.json` files into root `index.json` and `templates.json`.
"""

import os
import json
import glob

def generate_index():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(repo_root, "templates")
    index_file = os.path.join(repo_root, "index.json")
    templates_file = os.path.join(repo_root, "templates.json")

    templates = []
    
    # Find all template.json files
    pattern = os.path.join(templates_dir, "*", "template.json")
    template_paths = sorted(glob.glob(pattern))

    print(f"Found {len(template_paths)} templates.")

    for path in template_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                templates.append(data)
                print(f"  + Loaded: {data.get('title', os.path.basename(os.path.dirname(path)))}")
        except Exception as e:
            print(f"  ! Error loading {path}: {e}")

    catalog_data = {
        "version": "2",
        "templates": templates
    }

    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=2)

    with open(templates_file, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=2)

    print(f"\nSuccessfully generated {index_file} and {templates_file} with {len(templates)} templates.")

if __name__ == "__main__":
    generate_index()
