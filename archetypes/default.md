---
date: {{ now.Format "2006-01-02 15:04:05" }}
draft: true
title: {{ replace .File.ContentBaseName "-" " " | title }}
summary: A brief article summary
slug: {{ replace .File.ContentBaseName " " "-" | strings.ToLower }}
tags: []
categories: []
---
