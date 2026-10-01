---
date: {{ now.Format "2006-01-02 15:04:05" }}
draft: true
featured: false
title: {{ replace .File.ContentBaseName "-" " " | title }}
summary: A brief article summary
seo_title: ""
description: ""
seo_image: ""
seo_image_alt: ""
noindex: false
# Set lastmod only when updating published content: YYYY-MM-DD HH:MM:SS
slug: {{ replace .File.ContentBaseName " " "-" | strings.ToLower }}
tags: []
categories: []
---
