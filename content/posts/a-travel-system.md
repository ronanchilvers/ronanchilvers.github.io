---
publishDate:
date: 2025-05-16T13:52:39+01:00
draft: true
title: A Travel System
tags: ["travel", "shadowdark"]
summary: A simple travel system for use with OSR games such as Shadowdark.
---
When a journey is undertaken the following steps are followed:

1. **Plan The Route**
The party selects a route they want to take to their destination, determining how long it will take and what waypoints, if any, they will aim for. If they are at the Kaer, the Guild may be able to help them with maps and historical knowledge of the area.

2. **Prepare To Start**
The party assigns the journey roles - Guide, Scout, Quartermaster, Wrangler - and gather equipment, rations, etc. They must decide if they are going to use horses or not - if so, the Guild can supply hardy ponies.

3. **Make The Journey**
Each leg of the journey is handled by the various roles using ability checks to determine if anything untoward happens. Encounters are resolved as they happen.

## How far can you go?
We assume that given favourable conditions, an average party can travel *10 miles per day on foot* and *15 miles per day on horseback*.

## Plan the Route
> [!note] GM Actons
> 1. Describe the potential routes

- The party needs to choose their route as best they can, based on what they know of the area
    - The Seers may be able to help with weather predictions
    - Adepts should consider the moon phases
- Determine waypoints on the journey
    - A longer journey can be split up into waypoints if the party wishes
    - Each waypoint should be treated as a distinct journey or "leg" of the overall journey

## Prepare to Set Out
> [!note] GM Actions
> 1. Create the **travel clock** with the **Guide**
> 2. Create the **rations clock** with the **Quartermaster**

- The Guild can supply the party with the basics for safe travel. Along with equipment (basic bedroll and travelling clothes) they can provide:
    - A pony per party member. The ponies are a small, tough breed, well suited to hard journeys but not very fast.
    - Enough rations to keep the party going for 10 days (see the ration clock below).
- Choose roles
    - **Guide** - Intelligence - Characters taking on this role help ensure the group stays on track and heads in the right direction. They reference maps and physical distinguishing features to ensure the characters don't lose their way. The Guide is responsible for the **travel clock**.
	 - **Scout** - Wisdom - Characters taking on this role keep an eye out for nasty creatures and signs of recent activity (or activities yet to come). They're watching out for trouble.
	 - **Quartermaster** - Intelligence - The quartermaster ensures the health and well-being of the party. They make sure food stays unspoiled, enough water stays on hand, everyone's staying well-fed and well-hydrated, and everyone's socks are clean. The Quartermaster is responsible for the **rations clock**.
	 - **Wrangler** - Wisdom - (Optional) The stablehand is responsible for looking after the ponies, making sure they are fed, checking their hobbles and sorting out any issues like stones in their hooves, etc.
 - Supporting a role
     - A character can lend their support to one of the assigned roles if they wish to
     - The supporting character must make a travel check using the stat of the role they intend to support
         - If the role succeeds the supported character may make their next travel check with **Advantage**
     - If the supporting character holds an assigned role, they must make their next travel check with **Disadvantage**

## Make the Journey
> [!note] GM Actions
> Each day:
> 1. Determine the [[The Moons|dominant moon]]
> 2. Determine [[GM Binder Weather Effects|the weather conditions]]
> 3. Determine the safety of the terrain and area
> 4. Calculate the Journey DC

For each day spent travelling, determine the following:
- The **Guide** makes a travel check to determine whether they stay on course and updates the travel clock accordingly
- The **Scout** makes a travel check to determine the safety of the waypoint they reach
- The **Quartermaster** makes a travel check to see whether they use their rations effectively and updates the rations clock accordingly
- *[Optional, if using horses]* The **Wrangler** makes a travel check to determine if all is well with the horses

The GM then rolls for encounters using the normal Shadowdark rules. If Cinder is dominant, an encounter happens on a 1 *or 2* when rolling the encounter die (`dice: 1d6`) . For convenience here are the roll frequencies, assuming the characters are travelling for 8 hours.

| dice: 1d6 | Danger Level | Base DC | Frequency     | Daily             |
| --------- | ------------ | ------- | ------------- | ----------------- |
| 1-2       | Unsafe       | 9       | Every 3 hours | 3d6 (`dice: 3d6`) |
| 3-4       | Risky        | 12      | Every 2 hours | 4d6 (`dice: 4d6`) |
| 5-6       | Deadly       | 15      | Every hour    | 8d6 (`dice: 8d6`) |

## Journey Difficulty
The journey DC is based on a number of factors including
- [[GM Binder Weather Effects|the weather]]
- The terrain the party is travelling over

The base journey DC is 9. Add applicable modifiers for the conditions that apply to the route. Conditions are cumulative but the overall DC *cannot fall below 9 or rise above 18*.

| Condition           | Modifier |
| ------------------- | -------- |
| Poor weather        | +1       |
| Bad weather         | +2       |
| Extreme weather     | +4       |
| Party is in a hurry | +2       |

## Clocks

### Travel Clock
- The **Guide** is responsible for maintaining the travel clock
- The travel clock determines a party's progress towards their next intended destination.
- The clock has a number of segments equal to the number of days of travel to the intended destination
- Each clock segment is treated as a separate section of the trip
- A successful travel check by the **Guide** allows a single segment to be filled
- Two consecutive failed travel checks or a critical fumble by the **Guide** requires an additional segment to be added to the clock
- Once all segments are filled, the section of the journey is complete

### Ration Clock
- The **Quartermaster** is responsible for maintaining the ration clock.
- The clock has a number of segments equal to the number of days of rations the party has when they set out.
- Rations are tracked per party, not per character.
- Each day the **Quartermaster** fills in one ration segment and makes a travel check
- A failed travel check by the **Quartermaster** requires an additional segment to be filled
- A failed travel check with a critical fumble requires *two* additional segments to be filled
- The **Quartermaster** may make a travel check to forage for food and if successful, they may add an additional ration segment to the clock

## Encounter Types
`dice: 1d12`

| dice: 1d12 | Encounter          | Relevant Role |
| ---------- | ------------------ | ------------- |
| 1          | A chance meeting   | Guide         |
| 2          | Hidden reserves    | Quartermaster |
| 3          | A bump in the road | Scout         |
| 4          | Needing assistance | Guide         |
| 5          | Danger afoot       | Scout         |
| 6          | Natural wonders    | Guide         |
| 7          | Monster hunt       | Scout         |
| 8          | A place to rest    | Quartermaster |
| 9          | Old memories       | Guide         |
| 10         | A dark place       | Scout         |
| 11         | Deadly fight       | Scout         |
| 12         | Fateful encounter  | Scout         |

## Wrangler Mishaps
`dice: 1d12`

| dice: 1d12 | Mishap                             |
| ---------- | ---------------------------------- |
| 1          | Thrown a shoe                      |
| 2          | Broken saddle strap                |
| 3          | Panicked by unknown threat         |
| 4          | Injured by environment             |
| 5          | Bitten by snake or reptile         |
| 6          | Lost footing on treacherous ground |
| 7          | Wanders off when hobble breaks     |
| 8          | Kicked by another horse            |
| 9          | Blown                              |
| 10         | Lame                               |
| 11         | Poisoned by eating something       |
| 12         | Blinded by grit or dust            |

## Quartermaster Mishaps
`dice: 1d12`

1. Weevil infestation
2. Spoiled by damp
3. Leaking water skin
4. Torn backpack
5. Misjudged rations
6. Scavenged by rats
7. Cooking pot breaks and food is lost to the fire
8. Trodden on by accident
9. Swarmed by wasps
10. Spoiled by windblown grit or debris
11. Animal pees on a bag
12. Lost a bag

## Minor problems
`dice: 1d12`

1. A snake strikes!
2. A branch of blood thorn stabs into a leg
3. A tangler vine slips a creeper around an ankle
4. Scorpion in a sleeping bag!
5. Leeches / giant ticks in a boot
6. Twisted ankle caused by a rabbit hole
7. A hidden dip in the ground causes an unexpected tumble
8. A burrowing wasp stings an exposed arm
9. Food raided by a large and dangerous animal
10. Persistent gnats disrupt rest
11. Clothing catches in some vegetation causing delay
12. Sharp silver sedge cuts exposed flesh
