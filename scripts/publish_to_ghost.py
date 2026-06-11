#!/usr/bin/env python3
"""
publish_to_ghost.py — publish a repo markdown file to Ghost via the Admin API.

Design goals (so this behaves well inside a Claude Code / n8n pipeline):
  - Source of truth is the markdown file in your repo; Ghost is just the renderer.
  - Idempotent: re-running on the same slug UPDATES the post instead of duplicating.
  - Safe by default: creates a DRAFT. Publishing/scheduling is an explicit flag.
  - Secrets come from the environment, never the file or the command line.
  - Appends a standard footer linking back to your public repo + newsletter.

Usage:
  export GHOST_ADMIN_API_URL="https://yourblog.ghost.io"
  export GHOST_ADMIN_API_KEY="64f...:9ab..."          # Admin API key (id:secret)
  python scripts/publish_to_ghost.py posts/my-post.md            # -> draft
  python scripts/publish_to_ghost.py posts/my-post.md --publish  # -> published
  python scripts/publish_to_ghost.py posts/my-post.md --schedule 2026-06-20T14:00:00Z
  python scripts/publish_to_ghost.py posts/my-post.md --dry-run  # print, don't send

Optional env:
  REPO_URL          e.g. https://github.com/you/skills  -> footer backlink
  NEWSLETTER_URL    e.g. https://yourblog.ghost.io/#/portal/signup -> footer CTA

Markdown frontmatter (YAML) understood:
  title, slug, excerpt, tags (list), feature_image (local path or URL),
  canonical_url, status. CLI flags override frontmatter/status.

Deps: requests, pyjwt, markdown, python-frontmatter  (see requirements.txt)
"""

import argparse
import datetime as dt
import os
import sys
from pathlib import Path

import frontmatter
import jwt  # PyJWT
import markdown as md
import requests

ADMIN_PATH = "/ghost/api/admin"
ACCEPT_VERSION = "v5.0"


def make_token(admin_api_key: str) -> str:
    """Ghost Admin API auth is a short-lived JWT signed with the key's secret.

    The key looks like `id:secret` where secret is hex. The JWT header must carry
    `kid` = id, and the payload audience must be `/admin/`. Tokens may live at most
    5 minutes, so we mint a fresh one per run.
    """
    try:
        key_id, secret = admin_api_key.split(":")
    except ValueError:
        sys.exit("GHOST_ADMIN_API_KEY must be in the form `id:secret`.")
    iat = int(dt.datetime.now(tz=dt.timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(
        payload,
        bytes.fromhex(secret),
        algorithm="HS256",
        headers={"alg": "HS256", "typ": "JWT", "kid": key_id},
    )


def auth_headers(token: str) -> dict:
    return {
        "Authorization": f"Ghost {token}",
        "Accept-Version": ACCEPT_VERSION,
        "Content-Type": "application/json",
    }


def slug_from(path: Path, meta: dict) -> str:
    if meta.get("slug"):
        return meta["slug"]
    # strip a leading date like 2026-06-11- from the filename for a clean slug
    stem = path.stem
    parts = stem.split("-", 3)
    if len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit():
        return parts[3]
    return stem


def build_html(body_md: str, repo_url: str, newsletter_url: str, lossless: bool) -> str:
    """Render markdown to HTML and append a standard footer.

    Ghost converts posted HTML into its native editor format. That conversion is
    slightly lossy; pass --html-card to wrap the whole body in a Ghost HTML card
    for byte-exact rendering (better for code-heavy posts, at the cost of editing
    the post natively in Ghost later).
    """
    html = md.markdown(
        body_md,
        extensions=["fenced_code", "tables", "attr_list", "sane_lists", "toc"],
    )
    footer_bits = []
    if repo_url:
        footer_bits.append(
            f'The skills and patterns in this post are open source — '
            f'install or fork them here: <a href="{repo_url}">{repo_url}</a>.'
        )
    if newsletter_url:
        footer_bits.append(
            f'If this was useful, <a href="{newsletter_url}">subscribe</a> '
            f'to get the next one.'
        )
    if footer_bits:
        html += "\n<hr>\n<p><em>" + " ".join(footer_bits) + "</em></p>\n"
    if lossless:
        html = f"<!--kg-card-begin: html-->\n{html}\n<!--kg-card-end: html-->"
    return html


def get_post_by_slug(base: str, headers: dict, slug: str):
    r = requests.get(f"{base}{ADMIN_PATH}/posts/slug/{slug}/", headers=headers, timeout=30)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()["posts"][0]


def upload_image(base: str, headers: dict, image_path: Path) -> str:
    """Upload a local image and return its hosted URL. Multipart, so no JSON header."""
    h = {k: v for k, v in headers.items() if k != "Content-Type"}
    with open(image_path, "rb") as f:
        files = {"file": (image_path.name, f), "purpose": (None, "image")}
        r = requests.post(f"{base}{ADMIN_PATH}/images/upload/", headers=h, files=files, timeout=60)
    r.raise_for_status()
    return r.json()["images"][0]["url"]


def main():
    ap = argparse.ArgumentParser(description="Publish a markdown file to Ghost.")
    ap.add_argument("path", help="Path to the markdown post.")
    ap.add_argument("--publish", action="store_true", help="Publish immediately (default: draft).")
    ap.add_argument("--schedule", metavar="ISO8601", help="Schedule for a future UTC time, e.g. 2026-06-20T14:00:00Z.")
    ap.add_argument("--html-card", action="store_true", help="Wrap body in a Ghost HTML card for lossless rendering.")
    ap.add_argument("--dry-run", action="store_true", help="Print the payload; send nothing.")
    args = ap.parse_args()

    path = Path(args.path)
    if not path.exists():
        sys.exit(f"No such file: {path}")

    post = frontmatter.load(path)
    meta, body = post.metadata, post.content

    base = (os.environ.get("GHOST_ADMIN_API_URL") or "").rstrip("/")
    key = os.environ.get("GHOST_ADMIN_API_KEY") or ""
    repo_url = os.environ.get("REPO_URL", "")
    newsletter_url = os.environ.get("NEWSLETTER_URL", "")

    status = "draft"
    published_at = None
    if args.publish:
        status = "published"
    if args.schedule:
        status, published_at = "scheduled", args.schedule

    slug = slug_from(path, meta)
    html = build_html(body, repo_url, newsletter_url, args.html_card)

    payload = {
        "title": meta.get("title") or path.stem,
        "slug": slug,
        "html": html,
        "status": status,
        "tags": [{"name": t} for t in meta.get("tags", [])],
    }
    if meta.get("excerpt"):
        payload["custom_excerpt"] = meta["excerpt"]
    if meta.get("canonical_url"):
        payload["canonical_url"] = meta["canonical_url"]
    if published_at:
        payload["published_at"] = published_at

    if args.dry_run:
        token_ok = bool(key)
        print(f"[dry-run] target: {base or '(GHOST_ADMIN_API_URL unset)'}")
        print(f"[dry-run] slug:   {slug}  status: {status}")
        print(f"[dry-run] token:  {'would mint JWT' if token_ok else 'NO KEY SET'}")
        print(f"[dry-run] tags:   {[t['name'] for t in payload['tags']]}")
        print(f"[dry-run] html:   {len(html)} chars")
        print("[dry-run] first 300 chars of html:\n" + html[:300])
        return

    if not base or not key:
        sys.exit("Set GHOST_ADMIN_API_URL and GHOST_ADMIN_API_KEY before a real run.")

    headers = auth_headers(make_token(key))

    # feature image: upload if it's a local file, else pass through a URL
    fi = meta.get("feature_image")
    if fi:
        fp = Path(fi)
        payload["feature_image"] = upload_image(base, headers, fp) if fp.exists() else fi

    existing = get_post_by_slug(base, headers, slug)
    qs = "?source=html"
    if existing:
        # Ghost requires the current updated_at on edits as a collision guard.
        payload["updated_at"] = existing["updated_at"]
        url = f"{base}{ADMIN_PATH}/posts/{existing['id']}/{qs}"
        r = requests.put(url, headers=headers, json={"posts": [payload]}, timeout=60)
        action = "updated"
    else:
        url = f"{base}{ADMIN_PATH}/posts/{qs}"
        r = requests.post(url, headers=headers, json={"posts": [payload]}, timeout=60)
        action = "created"

    if not r.ok:
        sys.exit(f"Ghost API error {r.status_code}: {r.text}")

    result = r.json()["posts"][0]
    print(f"✓ {action} [{result['status']}] {result['title']}")
    print(f"  edit:    {base}/ghost/#/editor/post/{result['id']}")
    if result.get("url"):
        print(f"  preview: {result['url']}")


if __name__ == "__main__":
    main()
