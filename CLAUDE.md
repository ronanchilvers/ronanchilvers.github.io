# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Hugo static site — "By Lantern Light" — a personal blog focused on tabletop RPGs. It uses Hugo v0.152.2+ (extended).

## Common Commands

```bash
# Start local dev server with drafts visible
hugo server -D -M --cleanDestinationDir

# Build site for production
hugo --environment production

# Create a new post using the default archetype
hugo new content/posts/<section>/<filename>.md
```

## Deployment

The site is deployed to GitHub Pages via `.github/workflows/deploy.yml`. Pushing to `master` triggers an automatic build (Hugo 0.147.2 extended, with `--minify`) and deploy to the `gh-pages` branch using `peaceiris/actions-gh-pages`.

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

## Callout Blocks

Posts use Obsidian-style callout syntax for game mechanics and dice rolls:

```markdown
> [!abstract]+ Introduction
> Scene metadata here

> [!roll] Questions
> Oracle questions and dice results here
```
