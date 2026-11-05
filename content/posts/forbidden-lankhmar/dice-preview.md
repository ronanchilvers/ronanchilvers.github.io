---
date: 2026-11-04 21:00:00
draft: true
title: Forbidden Lankhmar Dice Preview
summary: A preview of the dice shortcode for Forbidden Lands dice pools.
slug: forbidden-lankhmar-dice-preview
tags:
  - testing
categories: []
---
Three base dice, two skill dice and a gear die:

{{< dice system="fl" title="Climb the wall" base="6 3 1" skill="6 1" gear="3">}}

A pool with gear and the other artifact dice:

{{< dice system="fl" title="Duel" base="4 5" skill="6 6" gear="1 6 3" d8="8" d10="7" d12="12" >}}

Artifact dice show one cross per success beneath the numeral:

{{< dice system="fl" title="d8 successes" d8="5 6 7 8" >}}

{{< dice system="fl" title="d10 successes" d10="5 6 7 8 9 10" >}}

{{< dice system="fl" title="d12 successes" d12="5 6 7 8 9 10 11 12" >}}

Standard polyhedral dice show plain results with no swords, skulls or totals:

{{< dice system="standard" title="Fireball" d6="3 5 2 6 1" d8="4" d10="9" d12="11" >}}

The system attribute can also be omitted for standard dice:

{{< dice title="Stealth check" d6="4 2" d8="6" >}}

Named base, skill and gear dice also use the aged-bone colour in the standard system:

{{< dice title="Standard pools" base="6" skill="4" gear="1" >}}

The full polyhedral set, using the values in the design reference:

{{< dice title="Polyhedral dice" d20="20" d12="12" d10="9" d100="90" d8="8" d6="6" d4="4" >}}
