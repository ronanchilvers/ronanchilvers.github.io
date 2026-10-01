#!/usr/bin/env python3
"""Validate generated search metadata, local images and sitemap destinations."""

import argparse
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    """Collect metadata and visible page structure from generated HTML."""

    def __init__(self):
        """Initialise collections without requiring a browser or dependencies."""
        super().__init__()
        self.meta = defaultdict(list)
        self.canonicals = []
        self.headings = []
        self.images = []
        self.schemas = []
        self.title = ""
        self.capture = None
        self.text = ""

    def handle_starttag(self, tag, attrs):
        """Record relevant elements and begin capturing titles or JSON-LD."""
        attrs = dict(attrs)
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property", ""))].append(
                attrs.get("content", "")
            )
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        elif tag == "img":
            self.images.append(attrs)
        if tag in ("h1", "title") or (
            tag == "script" and attrs.get("type") == "application/ld+json"
        ):
            self.capture = tag
            self.text = ""

    def handle_data(self, data):
        """Accumulate text inside the element currently being captured."""
        if self.capture:
            self.text += data

    def handle_endtag(self, tag):
        """Finish a captured heading, title or structured-data block."""
        if tag == self.capture:
            if tag == "h1":
                self.headings.append(self.text.strip())
            elif tag == "title":
                self.title = self.text.strip()
            else:
                self.schemas.append(self.text)
            self.capture = None


def local_file(root, url):
    """Map a public URL to its file in the generated output directory."""
    path = root / unquote(urlsplit(url).path).lstrip("/")
    return path / "index.html" if path.is_dir() else path


def validate(root, environment):
    """Return validation failures and counts for a complete Hugo build."""
    errors = []
    pages = {}
    images = 0
    for file in sorted(root.rglob("*.html")):
        if re.fullmatch(r"google[0-9a-f]+\.html", file.name):
            continue
        page = Page()
        page.feed(file.read_text(encoding="utf-8"))
        label = str(file.relative_to(root))

        def require(condition, message):
            """Associate a failed page check with its generated filename."""
            if not condition:
                errors.append(f"{label}: {message}")

        require(bool(page.title), "missing title")
        require(len(page.headings) == 1 and bool(page.headings[0]), "expected one non-empty h1")
        require(len(page.canonicals) == 1, "expected one canonical link")
        canonical = page.canonicals[0] if page.canonicals else ""
        parsed = urlsplit(canonical)
        require(parsed.scheme == "https" and bool(parsed.netloc), "canonical must be absolute HTTPS")
        require(not parsed.query and not parsed.fragment, "canonical must not contain a query or fragment")
        require(local_file(root, canonical) == file, "canonical does not identify this page")
        require(canonical not in pages, "duplicate canonical URL")
        pages[canonical] = page

        for name in ("description", "og:title", "og:description", "og:url", "og:type",
                     "og:image", "og:image:alt", "twitter:card", "twitter:title",
                     "twitter:description", "twitter:image", "twitter:image:alt"):
            require(len(page.meta[name]) == 1 and bool(page.meta[name][0].strip()), f"expected one non-empty {name}")

        def meta(name):
            """Return a metadata value after reporting absent or duplicate tags."""
            return page.meta[name][0] if page.meta[name] else ""

        require(meta("og:title") == page.title == meta("twitter:title"), "social titles disagree with page title")
        require(meta("og:description") == meta("description") == meta("twitter:description"), "social descriptions disagree")
        require(meta("og:url") == canonical, "Open Graph URL disagrees with canonical")
        require(meta("og:image") == meta("twitter:image"), "social images disagree")
        noindex = any("noindex" in {token.strip() for token in value.lower().split(",")}
                      for value in page.meta["robots"])
        if environment == "development" or file.name == "404.html" or parsed.path == "/error/":
            require(noindex, "page must be noindex")

        for image in page.images:
            images += 1
            require("alt" in image, "image is missing alternative text")
            source = urljoin(canonical, image.get("src", ""))
            if urlsplit(source).netloc == parsed.netloc:
                image_file = local_file(root, source)
                require(image_file.is_file(), f"image does not exist: {source}")
                if image_file.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
                    require(all(str(image.get(key, "")).isdigit() and int(image[key]) > 0
                                for key in ("width", "height")), f"image lacks intrinsic dimensions: {source}")

        image_url = urlsplit(meta("og:image"))
        require(image_url.scheme in ("http", "https") and bool(image_url.netloc), "preview image must be an absolute URL")
        if image_url.netloc == parsed.netloc:
            require(local_file(root, meta("og:image")).is_file(), "preview image does not exist")

        expected_type = "BlogPosting" if meta("og:type") == "article" else "WebSite" if parsed.path == "/" else None
        require(len(page.schemas) == (1 if expected_type else 0), "unexpected structured-data block count")
        for raw in page.schemas:
            try:
                schema = json.loads(raw)
                require(schema.get("@context") == "https://schema.org", "invalid schema context")
                require(schema.get("@type") == expected_type, "incorrect schema type")
                require(schema.get("url") == canonical, "schema URL disagrees with canonical")
                require(schema.get("description") == meta("description"), "schema description disagrees")
                if expected_type == "BlogPosting":
                    require(bool(schema.get("headline")), "missing article headline")
                    require(schema.get("image") == meta("og:image"), "schema image disagrees")
                    require(schema.get("mainEntityOfPage") == canonical, "article page URL disagrees")
                    author = schema.get("author", {})
                    require(bool(author.get("name")) and bool(author.get("url")), "missing article author")
                    for key in ("datePublished", "dateModified"):
                        if key == "datePublished" or key in schema:
                            date = datetime.fromisoformat(schema.get(key, ""))
                            require(date.tzinfo is not None, f"{key} must include a timezone")
            except (ValueError, TypeError, AttributeError) as error:
                require(False, f"invalid structured data: {error}")

    home = next((url for url in pages if urlsplit(url).path == "/"), "")
    for url in pages:
        if urlsplit(url).netloc != urlsplit(home).netloc:
            errors.append(f"{url}: canonical host disagrees with homepage")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        sitemap = ET.parse(root / "sitemap.xml")
        urls = [element.text for element in sitemap.findall("s:url/s:loc", namespace)]
        expected = {url for url, page in pages.items()
                    if not any("noindex" in value.lower() for value in page.meta["robots"])}
        if len(urls) != len(set(urls)):
            errors.append("sitemap.xml: duplicate URLs")
        if set(urls) != expected:
            errors.append(f"sitemap.xml: URLs disagree with indexable pages; extra={set(urls) - expected}, missing={expected - set(urls)}")
        if environment == "production" and not urls:
            errors.append("sitemap.xml: production sitemap must contain indexable pages")
    except (ET.ParseError, OSError) as error:
        errors.append(f"sitemap.xml: {error}")
        urls = []
    try:
        robots = (root / "robots.txt").read_text(encoding="utf-8")
        if f"Sitemap: {urljoin(home, 'sitemap.xml')}" not in robots:
            errors.append("robots.txt: incorrect sitemap URL")
        if "Disallow: /" in robots:
            errors.append("robots.txt: pages must remain crawlable")
    except OSError as error:
        errors.append(f"robots.txt: {error}")
    if not pages:
        errors.append("no generated pages found")
    return errors, (len(pages), images, len(urls))


def main():
    """Run generated-output checks and return a build-friendly exit status."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Hugo output directory")
    parser.add_argument("--environment", choices=("production", "development"), default="production")
    args = parser.parse_args()
    errors, counts = validate(args.directory.resolve(), args.environment)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"SEO checks passed: {counts[0]} pages, {counts[1]} images, {counts[2]} sitemap URLs ({args.environment}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
