#!/usr/bin/env python3
import os
import json
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")

def fix_templates():
    pattern = os.path.join(TEMPLATES_DIR, "*", "template.json")
    paths = sorted(glob.glob(pattern))
    print(f"Fixing {len(paths)} template.json files...")

    all_templates = []

    for p in paths:
        folder_name = os.path.basename(os.path.dirname(p))
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)

            category = data.get("category", "Utilities")
            if isinstance(category, list):
                categories = category
                category = category[0] if category else "Utilities"
            else:
                categories = [category]

            icon_url = f"https://raw.githubusercontent.com/optiwariindia/dockhand-templates/main/templates/{folder_name}/icon.svg"

            # Construct clean Portainer v2 / Dockhand compliant template object
            cleaned = {
                "type": 3,  # 3 = Compose Stack
                "title": data.get("title", folder_name.title()),
                "name": data.get("name", folder_name),
                "categories": categories,
                "category": category,
                "description": data.get("description", ""),
                "platform": "linux",
                "restart_policy": "unless-stopped",
                "logo": icon_url,
                "icon": icon_url,
                "image": data.get("image", ""),
                "administrator_only": False,
                "repository": {
                    "url": "https://github.com/optiwariindia/dockhand-templates",
                    "stackfile": f"templates/{folder_name}/docker-compose.yml"
                },
                "env": data.get("env", [])
            }

            # Save updated template.json back to individual folder
            with open(p, "w", encoding="utf-8") as f:
                json.dump(cleaned, f, indent=2)

            all_templates.append(cleaned)
            print(f"  + Fixed: {cleaned['title']} ({folder_name})")

        except Exception as e:
            print(f"  ! Error processing {p}: {e}")

    # Build root index.json and templates.json
    catalog_data = {
        "version": "2",
        "templates": all_templates
    }

    index_path = os.path.join(REPO_ROOT, "index.json")
    templates_path = os.path.join(REPO_ROOT, "templates.json")

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=2)

    with open(templates_path, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=2)

    print(f"\nSuccessfully generated {index_path} and {templates_path} with {len(all_templates)} templates.")

if __name__ == "__main__":
    fix_templates()
