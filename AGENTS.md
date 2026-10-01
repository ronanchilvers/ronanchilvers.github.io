# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## Overview

This is a Hugo static site, "By Lantern Light", a personal blog focused on tabletop roleplaying games. It uses Hugo v0.152.2 (extended), pinned in the deployment workflow.

## Common Commands

```bash
# Start local dev server with drafts visible
hugo server -D -M --cleanDestinationDir

# Build site for production
hugo --environment production

# Validate generated search metadata, images and sitemap
python3 scripts/check_seo.py public

# Exercise metadata overrides and development indexing with isolated content
python3 scripts/test_seo.py

# Create a new post using the default archetype
hugo new content/posts/<section>/<filename>.md
```

## Deployment

The site is deployed to GitHub Pages via `.github/workflows/deploy.yml`. Deployment is triggered manually through `workflow_dispatch`, including the Deploy Site action in Pages CMS. The workflow builds with Hugo 0.152.2 extended and `--environment production --minify`, checks the generated search metadata, then deploys to `gh-pages` using `peaceiris/actions-gh-pages` when the selected branch is `master`. Pushing alone does not trigger deployment.

## Site Architecture

**Config**: Split by environment under `config/`:
- `config/_default/` — base config (`hugo.yaml`, `params.yaml`, `menus.yaml`, `related.yaml`)
- `config/production/` — production overrides (enables GA4 analytics)

**Content** (`content/posts/`): Organised into named series/sections:
- `twelve-duchies/` — solo actual-play session reports (OSE system)
- `twelve-duchies-lore/` — world-building lore posts (deities, factions, encounter tables)
- `mountaintop-isolation/` — journal series
- `streetwise/`, `rules-and-hacks/`, `the-library-between-worlds/` — other series

**Layouts** (`layouts/`): Custom templates, no external theme:
- `_partials/components/` — reusable components: `post-card.html`, `post-tags.html`, `post-title.html`, `next-previous-posts.html`, `related-posts.html`, `event.html`, `timeline.html`
- `_shortcodes/` — `event.html`, `timeline.html` shortcodes
- Top-level templates: `baseof.html`, `home.html`, `page.html`, `section.html`, `taxonomy.html`, `term.html`

## Front Matter Convention

Posts use this front matter (from `archetypes/default.md`):

```yaml
---
date: YYYY-MM-DD HH:MM:SS
draft: true
title: Post Title
summary: A brief article summary
slug: post-slug
tags: []
categories: []
---
```

- Permalinks are structured as `/:year/:month/:slug/`
- Categories map to series (e.g. `Twelve Duchies`)
- Common tags include `actual-play`, `ose`, `solo-rpg`

## Search Metadata and Indexing

- Search engine optimisation (SEO) metadata is resolved in `layouts/_partials/seo/resolve.html` and rendered by `seo/head.html`. Keep descriptions, canonical links, social previews and structured data consistent through this resolver.
- Optional front matter: `seo_title`, `description`, `seo_image`, `seo_image_alt`, `noindex`, and `lastmod`. Search titles do not change visible titles or existing slugs. Descriptions fall back to plain-text post summaries or page-specific defaults.
- Set `lastmod` only for genuine content updates. Undated pages omit modification dates; post publication dates provide the fallback for sitemap dates. Never use build time or file modification time.
- Keep category and tag archives indexable by default. Set `noindex: true` for pages that should be excluded from search. Development builds, `/error/` and the branded 404 page are always noindex, while robots.txt keeps them crawlable.
- The custom sitemap includes indexable HTML pages only. Feeds remain available but are excluded from the sitemap.
- Category and tag display titles and introductions live in `content/categories/<term>/_index.md` and `content/tags/<term>/_index.md`. Preserve directory names when changing display titles to retain existing URLs.
- Pages CMS uses `static` as its media input and `/` as the public output. Social image overrides use public paths such as `/images/home.png`, not `/static/images/home.png`.
- Local images require intrinsic width and height. Content images and archive cards are lazy-loaded; prominent homepage images remain eager.

## Callout Blocks

Posts use Obsidian-style callout syntax for game mechanics and dice rolls:

```markdown
> [!abstract]+ Introduction
> Scene metadata here

> [!roll] Questions
> Oracle questions and dice results here
```
