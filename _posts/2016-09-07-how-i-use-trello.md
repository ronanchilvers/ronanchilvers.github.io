---
title:  "How I use Trello"
description: A workflow using trello, github, JIRA and IFTTT
## date: add a date when publishing
---

I recently decided that I needed to get a better handle on my daily tasks at work. We use github pull requests and JIRA (migrating from Basecamp) for project management and code storage, both of which generate a steady flow of tasks. There's also the day to day maintenance that needs to happen in any modest network and of course the sundry flow of ad-hoc stuff that crops up. Since my memory is marginally worse at retaining information than a sieve, I decided I needed some help!

# Finding the tools

There are a [million task management tools out there][google task management] that will help you organise your tasks in a multitude of different ways. After far too much reading about GTD, Pomodoro, Now Habits, people with seven habits and a whole load of other approaches I eventually distilled it down to these requirements.

- Don't forget anything
- What do I need to do soon
- What do I need to do today
- What did I do yesterday

With these key points in mind I worked out a set of lists, [kanban stylee][kanban], that would help me address them.

# The toolkit

I've ended up using two main tools. [Trello] gives me the task management. [IFTTT] allows me to automatically create cards from Github issues and pull requests, Basecamp assignment emails and recurring cards. [Zapier] creates tickets for me from Jira tickets. Jeremy Seitz's [Jira Tracker for Trello] syncs Jira ticket information onto Trello cards automatically. Finally [Trello's Github power up][trello github] lets me attach pull request data to cards.

Read on for the low-down.

## Trello

In creating my Trello board, the four requirements above were the main focus. I have six standard lists.

![Example ToDo Board][image-board-thumbnail]

- **Inbox** - this is my "don't forget anything" list. All new tasks get thrown in here. I also use Trello's [email to card / comment] and feature to create cards from incoming emails if required.
- **This Week** - these are the curated tasks, moved out of the Inbox list, that I need to get done soon
- **Today** - these are the tasks, moved out of the 'This Week' list, that I need to do today
- **Pull Requests** - this is really a sub-section of the Today list and is just for Github pull requests. I use a separate list so that my Today list doesn't get to noisy.
- **On Hold** - these tasks are on hold for some reason. Maybe I'm waiting on someone else, the task might be blocked by another one, etc, etc
- **Done** - Each day I create a new 'Done' list, specific to that day and archive the old one. This allows me to see exactly what got done on what date. Useful for standups!

## IFTTT / Zapier

![IFTTT screenshot][image-ifttt-thumbnail]

I have several recipes / zaps setup that keep my board populated from the various sources that we use at work.

- **Github Pull Requests / Issues** - IFTTT does this for me. I have a recipe for each repository I need to watch that adds a card to the 'Pull Requests' list for any new pull requests. I have another recipe that adds a card for any issues assigned to me.
- **JIRA tickets** - Zapier handles these. I have a zap that watches for any new tasks assigned to me and creates cards in my 'This Week' list for them.
- **Basecamp tickets** - Another IFTTT one. I have a recipe that watches my emails for any new tickets assigned to me and adds a card to my 'This Week' list.

## Jira Tracker for Trello

This handy utility by [Jeremy Seitz][Jira Tracker for Trello] allows me to sync specific cards with Jira. That way I have visibility of where my Jira tasks are in my Trello workflow while maintaining the data for those tasks in Jira. It runs from a cron job and uses a simple syntax in the Trello card comments to control sync behaviour. Its one way (Jira to Trello only) but that's fine for me.

At the moment, initialising the sync is a manual task. However if I stump up the cash for a paid Zapier account I would be able to automate it by using a second step in my Jira zap to add the required comment to the new cards.

## Trello's Github Power-Up

![Trello's Github Power-Up][image-trello-github-thumbnail]

This little power up just gives me the 'quick glance' information that's handy on Github PRs. Has it been merged? Is it passing CI tests?

[google task management]: https://www.google.co.uk/?q=task%20management%20tool
[kanban]: https://www.google.co.uk/?q=kanban
[trello]: https://trello.com/
[ifttt]: https://ifttt.com
[trello github]: http://blog.trello.com/github-and-trello-integrate-your-commits/
[zapier]: https://zapier.com
[Jira Tracker for Trello]: https://github.com/somebox/jira-tracker-for-trello
[email to card / comment]: http://help.trello.com/article/809-creating-cards-by-email
[image-board-thumbnail]: /assets/posts/how-i-use-trello/example-board-thumbnail.png
[image-board]: /assets/posts/how-i-use-trello/example-board.png
[image-ifttt-thumbnail]: /assets/posts/how-i-use-trello/ifttt-thumbnail.png
[image-trello-github-thumbnail]: /assets/posts/how-i-use-trello/trello-github-thumbnail.png