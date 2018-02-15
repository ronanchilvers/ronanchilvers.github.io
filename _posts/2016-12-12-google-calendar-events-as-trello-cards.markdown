---
title: Google Calendar events as Trello cards
date: 2016-12-12 17:04:22
tags:
- trello
- google
- php
description: A simple way of generating Trello cards from Google Calendar events using
  PHP
image: "/assets/posts/google-calendar-events-as-trello-cards/calendar-event-as-a-trello-card.png"
---

So far in my Trello task list adventures ([here]({% post_url 2016-09-07-how-i-use-trello %}) and [here]({% post_url 2016-11-29-trello-two-months-on %})), one of the niggling little shortcomings has been not having google calendar events in my Today list. We use [Harvest] at work and the [Harvest Chrome extension] handly integrates with Trello, giving you a 'Track Time' button when you open a card.

![Harvest time tracking in Trello][harvest-for-trello]

This works great for most things but with meetings, calls, etc, I was having to manually create a card just to track time against them. Annoying and clunky.

But ... I'm a developer for goodness sake! I know about APIs. I should be up to the challenge!!

# APIs - gotta love 'em!

![The Trello API][trello-api]

Trello has a comprehensive and simple API that lets you manipulate pretty much every part of the system. Similarly Google has a huge sprawling mass of an API suite that lets you (probably) control the entire world if you can work out how to talk to it. Fortunately the Google Calendar API is straightforward once you've got the authentication sorted out.

My little scipt needed to do two things:

- For a given date, read a list of calendar events out of Google Calendar
- Add a card for each event into a Trello list preserving the event title, description, date/time and attendees.

There are a couple of other bells and whistles (and some quirks! Hey - its alpha!) but that's pretty much it. A simple, schmimple bit of hacking. The result is [google-calendar-to-trello], a little CLI tool written in PHP that does exactly the above.

![A calendar event as a Trello card][calendar-event-in-trello]

And that's the result - a calendar event imported in from Google Calendar complete with attendees, date and everything. Yay me!

[Harvest]: https://www.getharvest.com/
[Harvest Chrome extension]: https://chrome.google.com/webstore/detail/harvest-time-tracker/fbpiglieekigmkeebmeohkelfpjjlaia?hl=en
[google-calendar-to-trello]: https://github.com/ronanchilvers/google-calendar-to-trello
[harvest-for-trello]: /assets/posts/google-calendar-events-as-trello-cards/harvest-time-tracking-in-trello.png
[calendar-event-in-trello]: /assets/posts/google-calendar-events-as-trello-cards/calendar-event-as-a-trello-card.png
[trello-api]: /assets/posts/google-calendar-events-as-trello-cards/trello-api.png
