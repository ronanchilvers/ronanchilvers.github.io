---
date: 2026-04-08 21:11:00
title: Weird Science Powers System
slug: weird-science-powers-system
draft: true
tags:
  - swade
categories:
  - Rules and Hacks
---
# Overview

Rather than selecting from a fixed list of known powers, Weird Scientists
construct effects on the fly by combining an **Element** (what they work with)
and a **Manipulation** (what they do with it), then declaring the mechanical
parameters of the effect. The roll penalty is calculated from those parameters.

This system uses the **No Power Points** setting rule. There are no Power
Points to track.

---

## Elements

Elements define the nature of a character's science. They are **narrative
permission**, not mechanical bonuses — they tell you what a character *can*
attempt, not how well they do it.

Characters choose **2 Elements** at creation. Additional Elements may be
gained via Advances.

| Group | Elements |
|-------|----------|
| Corporeal | Body, Mind, Time, Space |
| Physical | Fire, Earth, Water, Air |
| Esoteric | Light, Void |

Attempting an effect **outside your known Elements** carries an additional
**−2 penalty**.

## Manipulations

Manipulations define what a character does with their Element. All Manipulations are
available to all characters — they are not learned or gated.

| Manipulation | Description |
|--------|-------------|
| **Create** | Produce, generate, summon |
| **Destroy** | Damage, dissolve, break down |
| **Transform** | Alter form or properties |
| **Perceive** | Sense, detect, analyse |
| **Control** | Direct, compel, bind |
| **Protect** | Shield, absorb, negate |

## Activation

Declare your **Element + Manipulation**, then set your parameters (see Modifiers
below). Roll **Weird Science vs. TN 4**, minus the total penalty from your
chosen parameters.

**Success:** The effect works as declared.
**Raise:** Add one free Smarts die step to any single parameter (range,
duration, or damage) or add an additional target after seeing the result.
**Failure:** The effect doesn't activate.
**Critical Failure:** Roll on the Catastrophe Table (see below).

## Base Penalty

Before calculating modifiers, the GM assigns a base penalty reflecting how
much the effect violates the natural order of the world. Causing a breeze to blow a piece of paper off a table into the casters hand is considerably more plausible scientifically than making the table walk across the room!

| Penalty | Description | Example |
|---------|-------------|---------|
| 0 | Trivial — nudges nature | A breeze shifts a loose paper |
| −1 | Minor — bends nature | A flame burns hotter than it should |
| −2 | Significant — breaks nature | Air solidifies briefly to move an object |
| −4 | Extreme — defies reality | Time reverses locally for a few seconds |

This is a GM call, made quickly before the roll. The total roll penalty =
base penalty + modifier penalties.

## Modifiers

All parameters use the same scale: **Smarts die × multiplier**. The base
value (×1, i.e. your Smarts die maximum value in the relevant unit) is always free. Each
multiplier step above ×1 costs **−1 per step** (round down). 

> **Formula:** Penalty = multiplier − 1

So Sm×1 = 0, Sm×2 = −1, Sm×3 = −2, Sm×4 = −3, and so on.

### Range
Unit: **inches** (1″ = 2 yards). Base = Smarts die maximum value in inches / yards.

| Range | Multiplier | Penalty |
|-------|-----------|---------|
| Base | ×1 | 0 |
| Base × 2 | ×2 | −1 |
| Base x 3 | ×3 | −2 |
| Base x 4 | ×4 | −3 |

### Duration
Unit: **minutes**. Base = Smarts die in minutes.

| Duration | Multiplier | Penalty |
|----------|-----------|---------|
| Base mins | ×1 | 0 |
| Base x 2 mins | ×2 | −1 |
| Base x 3 mins | ×3 | −2 |
| ... | ... | ... |

> **Alternative:** A caster may re-cast every Smarts minutes instead of
> paying a higher duration penalty, accepting a fresh roll each time.

### Targets / Area
Base = single target. Each additional target above 1 costs −1
(round down for groups).

| Targets | Penalty |
|---------|---------|
| Base | 0 |
| Base x 2 | −1 |
| Base x 3 | −2 |
| Base x 4 | −3 |

### Damage
Unit: **Smarts die**. Base = one Smarts die, free. Each multiplier step
above ×1 costs −1.

**Note**: Damage is rolled as normal with the appropriate number of dice used.

| Damage | Multiplier | Penalty |
|--------|-----------|---------|
| Base | ×1 | 0 |
| Base x 2 | ×2 | −1 |
| Base x 3 | ×3 | −2 |
| Base x 4 | ×4 | −3 |

> Non-damaging effects (Perceive, Protect, etc.) treat Damage as N/A -
> no penalty, no benefit.

## Raises

On a raise, the caster gains **one free Smarts die step** to spend on any
single parameter after the roll or an additional target. This is declared after seeing the result.

- **Range:** Add one Smarts die to the distance achieved
- **Duration:** Add one Smarts die of minutes to the duration achieved
- **Damage:** Add one Smarts die to the damage roll
- **Target/Area:** Add an extra target to the effect

## Critical Failure — Catastrophe Table

A regular failure means the effect simply doesn't activate. On a **critical
failure**, roll d6 and add the total penalty attempted. Consult the table below.

| Roll (d6 + penalty) | Result |
|---------------------|--------|
| 1–2 | **Addled** — Blasted eyebrows, chattering teeth, singed coat. Dud casting, no mechanical effect. |
| 3–4 | **Kickback** — Caster is Shaken. |
| 5–6 | **Backlash** — Caster suffers Fatigue. All active powers end immediately. |
| 7–8 | **Blowback** — Effect triggers on caster or nearest ally instead of intended target. |
| 9–10 | **Catastrophe** — Device destroyed. Caster takes damage equal to the intended effect. |
| 11+ | **Unravelling** — Major narrative consequence, GM's call. The experiment has gone seriously wrong. |

## Maintenance

Each power currently being maintained imposes **−1 to all further Weird
Science rolls** (cumulative). A caster maintaining two effects rolls at −2
for the next activation, and so on.

## Edges

### Signature Method
*Requirements: Novice, Weird Science d6*
Choose one Element+Manipulation combination. Gain +2 to rolls using that combination.

### Overclock
*Requirements: Seasoned, Weird Science d8*
Once per scene, add one free parameter step to a declared effect with no
additional penalty. On a critical failure, Backlash triggers at a minimum.

### Jury Rig
*Requirements: Novice, Weird Science d6*
May construct one-time use devices without dedicated materials, using only found objects.
Normally this carries a GM-imposed penalty or is impossible.

### Refined Prototype
*Requirements: Veteran, Signature Method*
Your Signature Method combination never causes worse than Backlash on a critical failure.

## Example Effects

*Assume Smarts d8 throughout.*

### Bolt equivalent — Fire/Control
2 targets, standard damage, 40 yards range

| Parameter | Value | Penalty |
|-----------|-------|---------|
| Targets | 2 | −1 |
| Damage | ×1 (d8) | 0 |
| Range | ×3 (24″ / 48 yards) | −2 |
| **Total** | | **−3** |

Roll Weird Science at −3. On a raise, add a free d8 to damage, range,
or an extra target.

### Disguise equivalent — Body/Transform
Self only, 60 minutes duration

| Parameter | Value | Penalty |
|-----------|-------|---------|
| Targets | 1 (self) | 0 |
| Damage | N/A | 0 |
| Duration | ×8 (64 mins) | −7 |
| **Total** | | **−7** |

Roll Weird Science at −7. On a raise, add a free d8 of minutes to the
duration.

Alternatively, the caster might decide to re-cast every 8 minutes at −0 penalty (Sm×1 duration) and risk a failure.