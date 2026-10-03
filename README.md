# AI Tech Blog

A daily AI/tech publication with affiliate content. Static site, rebuilt from
Markdown and deployed to GitHub Pages.

## How publishing works

- New posts go in `posts/` as Markdown with frontmatter:
  `title`, `date` (YYYY-MM-DD), `subtitle` (optional), `tags` (comma-separated),
  `excerpt`, `disclosure: true/false`, and a `sources:` list.
- Slugs come from the filename, e.g. `posts/2026-10-04-my-post.md`
  → `/posts/2026-10-04-my-post/`.
- Amazon AU links (`amazon.com.au`) are automatically styled as product buttons.
- Build: `SITE_URL="https://sanchitgogna.github.io/ai-tech-blog" BASE_PATH="/ai-tech-blog" .venv/bin/python build.py`
- Output lands in `docs/` — GitHub Pages serves the `main` branch's `/docs` folder.
- Commit and push; the site updates in a minute or two.

## Daily automation

A scheduled job writes the day's post into `posts/`, rebuilds, commits, and pushes.
