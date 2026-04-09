---
date: 2026-04-08 18:11:00
title: Weird Science Powers
slug: weird-science-powers-system
draft: false
tags:
  - swade
  - rule-hacks
categories:
  - Rules and Tools
summary: This is a Powers hack for Savage Worlds Adventure Edition. Rather than
  selecting from a fixed list of known powers, Weird Scientists construct
  effects on the fly by combining an **Element** (what they work with) and a
  **Manipulation** (what they do with it), then declaring the mechanical
  parameters of the effect. The roll penalty is calculated from those
  parameters.
---
This is a Powers hack for Savage Worlds Adventure Edition. Rather than selecting from a fixed list of known powers, Weird Scientists
construct effects on the fly by combining an **Element** (what they work with)
and a **Manipulation** (what they do with it), then declaring the mechanical
parameters of the effect. The roll penalty is calculated from those parameters.

This system uses the **No Power Points** setting rule. There are no Power
Points to track.

## Elements

Elements define the nature of a character's science. They are **narrative
permission**, not mechanical bonuses — they tell you what a character *can*
attempt, not how well they do it.

Characters choose proficiency in **2 Elements** at creation. Additional Elements may be
gained via Advances, one new Element per Advance. Characters can only use elements which 
they have proficiency in.

| Group     | Elements                |
| --------- | ----------------------- |
| Corporeal | Body, Mind, Time, Space |
| Physical  | Fire, Earth, Water, Air |
| Esoteric  | Light, Void             |

Some Elements may only be used at higher character ranks. Element access is as follows:

| Rank     | Elements                             |
| -------- | ------------------------------------ |
| Novice   | Fire, Earth, Water, Air, Light, Void |
| Seasoned | Body, Mind                           |
| Veteran  | Space                                |
| Heroic   | Time                                 |

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

Declare your **Element + Manipulation**, then work out the cost (see Modifiers
below) and apply it as a negative modifier on the Weird Science roll. Roll **Weird Science vs. TN 4**, 
minus the total penalty from the chosen parameters.

**Success:** The effect works as declared.
**Raise:** Success with additional benefits - see Raises section.
**Failure:** The effect doesn't activate.
**Critical Failure:** Roll on the Catastrophe Table (see below).

## Base Cost

Before calculating modifiers, the GM assigns a base cost reflecting how
much the effect violates the natural order of the world. Causing a breeze to blow a piece of paper off a table into the casters hand is considerably more plausible scientifically than making the table walk across the room.

| Cost | Description | Example |
|---------|-------------|---------|
| 0 | Trivial — nudges nature | A breeze shifts a loose paper |
| 1 | Minor — bends nature | A flame burns hotter than it should |
| 2 | Significant — breaks nature | Air solidifies briefly to move an object |
| 4 | Extreme — defies reality | Time reverses locally for a few seconds |

This is a GM call, made quickly before the roll. The total roll cost = base cost + additional costs.

## Power Costs

### Range
Unit: **inches** (1″ = 2 yards). Base = Smarts die maximum value in inches / yards.

| Range    | Cost |
| -------- | ---- |
| Base     | 0    |
| Base × 2 | 1    |
| Base x 3 | 2    |
| Base x 4 | 3    |

### Duration

Effect durations are one of:

- **Instantaneous**: The effect is resolved immediately and over.
- **Sustained**: The effect remains active until dismissed, disrupted, or the caster is incapacitated. Each Sustained effect causes an additional +1 cost to all subsequent Weird Science rolls while they are active. Sustained effects can be dropped at any time.
- **Permanent**: The effect is an enduring change that does not require maintenance. This is at the GM’s discretion and will incur additional cost.

### Targets

| Number of Targets | Cost |
| ----------------- | ---- |
| 1                 | 0    |
| 2                 | 1    |
| 4                 | 2    |
| 8                 | 4    |
| 16                | 6    | 

These bands are the maximum per band. Arbitrary target counts incur a cost equal to the next band which is larger than the count. For example, 3 targets incurs a cost of 4 targets / 2.

### Damage
Unit: **Smarts die**. Base = one Smarts die, free. Each multiplier step
above ×1 costs 2.

**Note**: Damage is rolled as normal, using the appropriate number of Smarts dice.

| Damage   | Cost |
| -------- | ---- |
| Base     | 0    |
| Base x 2 | 2    |
| Base x 3 | 4    |
| Base x 4 | 6    | 

> Non-damaging effects (Perceive, Protect, etc.) treat Damage as N/A —
> no penalty, no benefit.

## Raises

On a raise, the caster can choose one of the following benefits. This is declared
after seeing the result. Multiple Raises have no additional effect.

- **Range:** Add one Smarts die to the distance achieved
- **Duration:** The effect can be Sustained without additional cost  to future casting rolls.
- **Damage:** Add a static +2 Damage
- **Target:** Double the number of targets

## Critical Failure — Catastrophe Table

A regular failure means the effect simply doesn't activate. On a **critical
failure**, roll d6 and add the total cost. Then consult the table below.

| Roll (d6 + cost) | Result                                                                                             | 
| ---------------- | -------------------------------------------------------------------------------------------------- |
| 1–2              | **Addled** — Blasted eyebrows, chattering teeth, singed coat. Dud casting, no mechanical effect.   |
| 3–4              | **Kickback** — Caster is Shaken.                                                                   |
| 5–6              | **Backlash** — Caster suffers Fatigue. All active powers end immediately.                          |
| 7–8              | **Blowback** — Effect triggers on caster or nearest ally instead of intended target.               |
| 9–10             | **Catastrophe** — Device destroyed. Caster takes damage equal to the intended effect.              |
| 11+              | **Unravelling** — Major narrative consequence, GM's call. The experiment has gone seriously wrong. |

For example, for a casting attempt with a 5 point cost, on a Critical Failure the character would roll 1d6+5 to determine the outcome.

## Edges

### Signature Method
*Requirements: Novice, Weird Science d6*
Choose one Element+Manipulation combination. Gain +2 to rolls using that combination.

### Overclock
*Requirements: Seasoned, Weird Science d8*
Once per scene, add one free parameter step to a declared effect with no additional penalty. On a critical failure, add 2 to the Effect cost when rolling for a Catastrophy.

### Jury Rig
*Requirements: Novice, Weird Science d6*
May construct one-time use devices without dedicated materials, using only found objects.
Normally this carries a GM-imposed penalty or is impossible.

### Refined Prototype
*Requirements: Veteran, Signature Method*
On a Critical Failure with your Signature Method, subtract 2 from the Effect cost when rolling for a Catastrophy.

## Example Effects

*Assume Smarts d8 throughout.*

### Bolt equivalent — Fire/Control
2 targets, standard damage, 40 yards range

| Parameter | Value               | Cost   |
| --------- | ------------------- | ------ |
| Base cost | N/A                 | 1      |
| Targets   | 2                   | 1     |
| Damage    | ×1 (d8)             | 0      |
| Range     | ×3 (24″ / 48 yards) | 2     |
| **Total** |                     | **4** |

Roll Weird Science at −4. On a Raise choose a Raise effect from the options above. On a Critical Failure roll on the Catastrophy table with a +4 modifier, ie: 1d6+4.

### Disguise equivalent — Body/Transform
Self only, 60 minutes duration

| Parameter | Value     | Cost                              |
| --------- | --------- | --------------------------------- |
| Base      | N/A       | 2                                 | 
| Targets   | 1 (self)  | 0                                 |
| Damage    | N/A       | 0                                 |
| Duration  | Sustained | 0 up front, +1 on future castings |
| **Total** |           | **2**                             |

Roll Weird Science at −2. On a raise, maintain the effect for free or choose from the Raise options above. The caster will have an additional +1 cost on any casting for the next 60 mins. On a Critical Failure roll on the Catastrophy table with a +2 modifier, ie: 1d6+2.