import requests, os

ORG = "wasdi-cloud"  # replace with your GitHub org
URL = f"https://api.github.com/orgs/{ORG}/repos"

resp = requests.get(URL)
repos = resp.json()

os.makedirs("content/projects", exist_ok=True)

for repo in repos:
    slug = repo["name"].lower().replace(" ", "-")
    filepath = f"content/projects/{slug}.md"
    with open(filepath, "w") as f:
        f.write(f"""---
title: "{repo['name']}"
date: {repo['created_at']}
repo_url: "{repo['html_url']}"
description: "{repo['description'] or ''}"
stars: {repo['stargazers_count']}
---
""")
