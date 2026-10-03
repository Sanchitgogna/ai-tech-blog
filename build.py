#!/usr/bin/env python3
"""Static site generator for the AI Tech Blog.

Usage:  .venv/bin/python build.py
Reads posts/*.md (frontmatter + markdown), renders into public/.
"""
import os, re, shutil, html
from datetime import datetime
from pathlib import Path
import markdown

HERE = Path(__file__).parent
POSTS_DIR = HERE / "posts"
TPL_DIR = HERE / "templates"
STATIC_DIR = HERE / "static"
OUT_DIR = HERE / "docs"  # GitHub Pages serves from /docs on main

SITE_NAME = "AI Tech Blog"
# Set after deploy, e.g. "https://username.github.io/ai-tech-blog"
SITE_URL = os.environ.get("SITE_URL", "https://example.github.io/ai-tech-blog").rstrip("/")
# Path prefix for links: "/ai-tech-blog" for project pages, "" for custom domain
BASE_PATH = os.environ.get("BASE_PATH", "/ai-tech-blog").rstrip("/")
if BASE_PATH:
    BASE = BASE_PATH + "/"
else:
    BASE = "/"

md = markdown.Markdown(extensions=["extra", "tables", "fenced_code", "smarty"])


def parse_post(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError(f"No frontmatter in {path}")
    raw_fm, body = m.group(1), m.group(2)
    fm = {}
    sources = []
    in_sources = False
    for line in raw_fm.splitlines():
        if re.match(r"^sources\s*:", line):
            in_sources = True
            continue
        if in_sources:
            sm = re.match(r"^\s*-\s*(.*)$", line)
            if sm:
                sources.append(sm.group(1).strip())
                continue
            elif line.strip() == "":
                continue
            else:
                in_sources = False
        km = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if km:
            fm[km.group(1).strip()] = km.group(2).strip().strip('"')
    fm["sources"] = sources
    fm["slug"] = path.stem
    return fm, body


def fmt_date(d: str) -> str:
    dt = datetime.strptime(d, "%Y-%m-%d")
    return dt.strftime("%-d %B %Y")


def render_base(page_title, meta_description, content, head_extra=""):
    tpl = (TPL_DIR / "base.html").read_text(encoding="utf-8")
    return (tpl.replace("{{page_title}}", html.escape(page_title))
               .replace("{{meta_description}}", html.escape(meta_description))
               .replace("{{base_path}}", BASE)
               .replace("{{head_extra}}", head_extra)
               .replace("{{content}}", content))


def tag_link(tag):
    slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
    return f'<a class="tag" href="{BASE}tags/{slug}/">{html.escape(tag)}</a>'


def amazon_buttonize(html_body: str) -> str:
    """Style Amazon affiliate links as buttons."""
    def repl(m):
        href, text = m.group(1), m.group(2)
        return f'<a class="product-link" href="{href}">{text}</a>'
    return re.sub(r'<a href="([^"]*amazon\.com\.au[^"]*)">([^<]*)</a>', repl, html_body)


def build():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    (OUT_DIR / "posts").mkdir(parents=True)
    (OUT_DIR / "tags").mkdir(parents=True)
    shutil.copytree(STATIC_DIR, OUT_DIR / "static")

    posts = []
    for p in sorted(POSTS_DIR.glob("*.md")):
        fm, body = parse_post(p)
        body_html = md.convert(body)
        md.reset()
        body_html = amazon_buttonize(body_html)
        fm["body_html"] = body_html
        fm["date_fmt"] = fmt_date(fm["date"])
        posts.append(fm)
    posts.sort(key=lambda x: x["date"], reverse=True)

    # --- post pages ---
    post_tpl = (TPL_DIR / "post.html").read_text(encoding="utf-8")
    for fm in posts:
        tags = [t.strip() for t in fm.get("tags", "").split(",") if t.strip()]
        tag_links = "".join(tag_link(t) for t in tags)
        subtitle_html = f'<p class="post-subtitle">{html.escape(fm["subtitle"])}</p>' if fm.get("subtitle") else ""
        disclosure_html = ""
        if fm.get("disclosure", "").lower() == "true":
            disclosure_html = ('<div class="disclosure"><strong>Affiliate disclosure:</strong> '
                               'this post contains affiliate links. If you buy through them, we may earn '
                               'a commission at no extra cost to you. Prices were checked on the date shown '
                               'and may have changed.</div>')
        sources_html = ""
        if fm.get("sources"):
            items = "".join(f"<li>{s}</li>" for s in fm["sources"])
            sources_html = f'<div class="sources"><h3>Sources</h3><ol>{items}</ol></div>'
        content = (post_tpl.replace("{{date}}", fm["date_fmt"])
                           .replace("{{tag_links}}", tag_links)
                           .replace("{{title}}", html.escape(fm["title"]))
                           .replace("{{subtitle_html}}", subtitle_html)
                           .replace("{{disclosure_html}}", disclosure_html)
                           .replace("{{body}}", fm["body_html"])
                           .replace("{{sources_html}}", sources_html))
        page = render_base(fm["title"] + " — " + SITE_NAME,
                           fm.get("excerpt", fm["title"]), content)
        d = OUT_DIR / "posts" / fm["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(page, encoding="utf-8")

    # --- index ---
    cards = []
    for fm in posts:
        tags = [t.strip() for t in fm.get("tags", "").split(",") if t.strip()]
        tag_links = "".join(tag_link(t) for t in tags)
        cards.append(
            f'<a class="post-card" href="{BASE}posts/{fm["slug"]}/">'
            f'<p class="post-meta">{fm["date_fmt"]}{tag_links}</p>'
            f'<h2>{html.escape(fm["title"])}</h2>'
            f'<p class="excerpt">{html.escape(fm.get("excerpt", ""))}</p></a>')
    index_tpl = (TPL_DIR / "index.html").read_text(encoding="utf-8")
    index_content = index_tpl.replace("{{post_cards}}", "\n".join(cards))
    (OUT_DIR / "index.html").write_text(
        render_base(SITE_NAME + " — AI, explained like a human.",
                    "A daily publication on AI and technology: news analysis, explainers, and gear coverage.",
                    index_content), encoding="utf-8")

    # --- tag pages ---
    tag_map = {}
    for fm in posts:
        for t in [t.strip() for t in fm.get("tags", "").split(",") if t.strip()]:
            tag_map.setdefault(t, []).append(fm)
    for tag, tposts in tag_map.items():
        slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
        cards = []
        for fm in tposts:
            cards.append(
                f'<a class="post-card" href="{BASE}posts/{fm["slug"]}/">'
                f'<p class="post-meta">{fm["date_fmt"]}</p>'
                f'<h2>{html.escape(fm["title"])}</h2>'
                f'<p class="excerpt">{html.escape(fm.get("excerpt", ""))}</p></a>')
        content = (f'<section class="tag-header"><p class="post-meta">Tag</p><h1>{html.escape(tag)}</h1></section>'
                   f'<section class="post-list">{"".join(cards)}</section>')
        d = OUT_DIR / "tags" / slug
        d.mkdir(parents=True)
        (d / "index.html").write_text(
            render_base(f"{tag} — {SITE_NAME}", f"Posts tagged {tag}.", content), encoding="utf-8")

    # --- about ---
    about_md = (HERE / "about.md").read_text(encoding="utf-8") if (HERE / "about.md").exists() else ""
    about_html = md.convert(about_md) if about_md else "<p>A daily publication on AI and technology.</p>"
    md.reset()
    about_content = f'<article class="about"><h1>About</h1>{about_html}</article>'
    d = OUT_DIR / "about"
    d.mkdir(parents=True)
    (d / "index.html").write_text(
        render_base("About — " + SITE_NAME, "About the AI Tech Blog.", about_content), encoding="utf-8")

    # --- robots, sitemap, rss ---
    (OUT_DIR / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    urls = [f"{SITE_URL}/", f"{SITE_URL}/about/"]
    for fm in posts:
        urls.append(f"{SITE_URL}/posts/{fm['slug']}/")
    for tag in tag_map:
        slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
        urls.append(f"{SITE_URL}/tags/{slug}/")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc></url>")
    sm.append("</urlset>")
    (OUT_DIR / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

    rss = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0"><channel>',
           f'<title>{html.escape(SITE_NAME)}</title>',
           f'<link>{SITE_URL}/</link>',
           '<description>A daily publication on AI and technology.</description>']
    for fm in posts[:20]:
        rss.append("<item>"
                   f"<title>{html.escape(fm['title'])}</title>"
                   f"<link>{SITE_URL}/posts/{fm['slug']}/</link>"
                   f"<pubDate>{datetime.strptime(fm['date'], '%Y-%m-%d').strftime('%a, %d %b %Y 00:00:00 +0000')}</pubDate>"
                   f"<description>{html.escape(fm.get('excerpt', ''))}</description>"
                   "</item>")
    rss.append("</channel></rss>")
    (OUT_DIR / "feed.xml").write_text("\n".join(rss), encoding="utf-8")

    # keep GitHub Pages from ignoring underscore dirs
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(posts)} posts -> {OUT_DIR}")


if __name__ == "__main__":
    build()
