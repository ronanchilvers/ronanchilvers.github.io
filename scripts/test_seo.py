#!/usr/bin/env python3
"""Exercise Hugo metadata and indexing using temporary content and output."""

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

from check_seo import Page, validate


class SearchMetadataTest(unittest.TestCase):
    """Verify author controls, fallback behaviour and production exclusions."""

    @classmethod
    def setUpClass(cls):
        """Build production and development fixtures without editing site content."""
        cls.workspace = tempfile.TemporaryDirectory(prefix="artifakt-seo-test-")
        cls.root = Path(cls.workspace.name)
        cls.repo = Path(__file__).resolve().parents[1]
        content = cls.root / "content"
        shutil.copytree(cls.repo / "content", content)
        fixtures = {
            "override": {
                "title": "Visible article title",
                "summary": "The card excerpt stays separate.",
                "seo_title": 'Oracle & "omens" | By Lantern Light',
                "description": 'Choose "omens" & <possibilities>; </script> is text.',
                "seo_image": "/images/twelve-duchies/logo.png",
                "seo_image_alt": 'A map & "lantern"',
                "lastmod": "2025-03-05T13:00:00+00:00",
                "categories": ["Twelve Duchies"],
            },
            "summary": {
                "title": "Summary fallback",
                "summary": "Explore **tables** and [dice](https://example.com/) & adventures.",
                "categories": ["Twelve Duchies"],
            },
            "minimal": {"title": "Minimal article"},
            "legacy": {
                "title": "Legacy images",
                "images": {"banner": "house-rules-banner.png", "thumbnail": "house-rules-thumbnail.png"},
                "categories": ["Twelve Duchies"],
            },
            "noindex": {"title": "Private search listing", "noindex": True},
        }
        posts = content / "posts" / "seo-test"
        posts.mkdir()
        for name, fields in fixtures.items():
            fields = dict(date="2025-03-01T12:00:00+00:00", draft=False,
                          slug=f"seo-test-{name}", **fields)
            frontmatter = "\n".join(f"{key}: {json.dumps(value)}" for key, value in fields.items())
            (posts / f"{name}.md").write_text(
                f"---\n{frontmatter}\n---\nAn isolated adventure with fallback metadata.\n\n"
                '![A map & lantern](/images/home.png "Map illustration")\n',
                encoding="utf-8",
            )
        for environment in ("production", "development"):
            command = ["hugo", "--environment", environment, "--contentDir", str(content),
                       "--destination", str(cls.root / environment), "--cacheDir", str(cls.root / "cache"),
                       "--noBuildLock", "--minify", "--clock", "2026-10-01T12:00:00+01:00"]
            result = subprocess.run(command, cwd=cls.repo, capture_output=True, text=True)
            if result.returncode:
                cls.workspace.cleanup()
                raise RuntimeError(result.stdout + result.stderr)

    @classmethod
    def tearDownClass(cls):
        """Remove all temporary fixture content and generated builds."""
        cls.workspace.cleanup()

    def page(self, name, environment="production"):
        """Read a rendered fixture page from the requested environment."""
        page = Page()
        page.feed((self.root / environment / "2025" / "03" /
                   f"seo-test-{name}" / "index.html").read_text(encoding="utf-8"))
        return page

    def test_complete_builds(self):
        """Check every page and image in both generated environments."""
        for environment in ("production", "development"):
            with self.subTest(environment=environment):
                errors, _ = validate(self.root / environment, environment)
                self.assertEqual(errors, [])

    def test_editorial_overrides_and_escaping(self):
        """Keep visible titles separate and round-trip punctuation safely."""
        page = self.page("override")
        self.assertEqual(page.headings, ["Visible article title"])
        self.assertEqual(page.title, 'Oracle & "omens" | By Lantern Light')
        self.assertEqual(page.meta["description"], ['Choose "omens" & <possibilities>; </script> is text.'])
        self.assertEqual(page.meta["og:image:alt"], ['A map & "lantern"'])
        schema = json.loads(page.schemas[0])
        self.assertEqual(schema["description"], page.meta["description"][0])
        self.assertEqual(schema["datePublished"], "2025-03-01T12:00:00+00:00")
        self.assertEqual(schema["dateModified"], "2025-03-05T13:00:00+00:00")
        self.assertEqual(schema["image"], "https://artifakt.co.uk/images/twelve-duchies/logo.png")
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap = ET.parse(self.root / "production" / "sitemap.xml")
        entry = next(entry for entry in sitemap.findall("s:url", ns)
                     if entry.find("s:loc", ns).text == page.canonicals[0])
        self.assertEqual(entry.find("s:lastmod", ns).text, schema["dateModified"])

    def test_plain_summary_fallback(self):
        """Convert a Markdown summary into readable search metadata."""
        page = self.page("summary")
        self.assertEqual(page.meta["description"], ["Explore tables and dice & adventures."])
        self.assertNotIn("dateModified", json.loads(page.schemas[0]))

    def test_optional_fields_and_missing_category(self):
        """Publish a post with only required fields using safe image defaults."""
        page = self.page("minimal")
        self.assertTrue(page.meta["description"][0].startswith("An isolated adventure"))
        self.assertEqual(page.meta["og:image"], ["https://artifakt.co.uk/images/home.png"])
        self.assertEqual(page.images[1]["width"], "1024")
        self.assertEqual(page.images[1]["loading"], "lazy")

    def test_legacy_image_mapping(self):
        """Continue resolving existing banner and thumbnail filename overrides."""
        page = self.page("legacy")
        self.assertEqual(page.meta["og:image"], ["https://artifakt.co.uk/images/twelve-duchies/house-rules-banner.png"])
        archive = (self.root / "production" / "categories" / "twelve-duchies" / "index.html").read_text()
        self.assertIn("/images/twelve-duchies/house-rules-thumbnail.png", archive)

    def test_noindex_exclusion_and_preserved_archives(self):
        """Exclude opted-out posts while keeping category and tag URLs discoverable."""
        page = self.page("noindex")
        self.assertEqual(page.meta["robots"], ["noindex, follow"])
        sitemap = (self.root / "production" / "sitemap.xml").read_text()
        self.assertNotIn(page.canonicals[0], sitemap)
        self.assertIn("https://artifakt.co.uk/categories/twelve-duchies/", sitemap)
        self.assertIn("https://artifakt.co.uk/tags/ose/", sitemap)
        self.assertNotIn("/posts/index.xml", sitemap)
        self.assertTrue((self.root / "production" / "posts" / "index.xml").is_file())

    def test_build_check_rejects_invalid_metadata(self):
        """Prove the deployment gate fails when a generated description disappears."""
        output = self.root / "broken"
        shutil.copytree(self.root / "production", output)
        file = output / "2025" / "03" / "seo-test-minimal" / "index.html"
        file.write_text(file.read_text().replace("name=description", "name=removed-description"))
        errors, _ = validate(output, "production")
        self.assertTrue(any("expected one non-empty description" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
