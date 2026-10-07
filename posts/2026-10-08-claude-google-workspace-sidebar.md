---
title: "Claude just moved into Google's house — and it's editing your spreadsheets"
date: 2026-10-08
subtitle: "Anthropic's assistant now sits in a sidebar inside Docs, Sheets and Slides — right where Gemini used to have the room to itself."
tags: AI news, AI tools
excerpt: Anthropic launched Claude for Google Workspace in public beta on 6 October, putting Claude in a sidebar inside Docs, Sheets and Slides — with in-place editing, an ask-before-edits approval gate, and a clear shot at Gemini's home turf.
disclosure: false
sources:
- [VentureBeat](https://venturebeat.com/technology/you-can-now-open-claude-directly-in-google-docs-sheets-and-slides-and-vice-versa-open-and-edit-the-files-in-claude)
- [AbsoluteGeeks](https://www.absolutegeeks.com/tech-news/claude-just-invaded-google-docs-and-gemini-should-be-worried/)
- [9to5Google](https://9to5google.com/2026/10/06/claude-google-docs-sheet-slides/)
---

There's a special kind of boldness in setting up shop inside your rival's house. This week, Anthropic did exactly that: [Claude now lives in a sidebar inside Google Docs, Sheets and Slides](https://venturebeat.com/technology/you-can-now-open-claude-directly-in-google-docs-sheets-and-slides-and-vice-versa-open-and-edit-the-files-in-claude), announced 6 October and available now in public beta on every paid Claude plan — Pro, Max, Team and Enterprise.

Up to now, getting Claude's help on a Google document meant the old shuffle: copy text out, paste it into the chat, copy the answer back, reformat everything you broke in transit. The new [Claude for Google Workspace add-on](https://9to5google.com/2026/10/06/claude-google-docs-sheet-slides/) kills that dance. Open a file, and Claude sits beside it, reads what's on screen, and edits the thing in place.

It works in both directions, which is the part that actually matters. You can start in the document and summon Claude from the sidebar — or start in Claude, paste in a Google file link (or ask it to create a fresh Doc, Sheet or Slides deck), and work on the file from there. Either way, access follows your existing Google sharing permissions, so Claude can't wander into files you can't.

## What it actually does in each app

Docs is the most straightforward: tighten a sentence, restyle a heading, rewrite the executive summary — Claude makes small edits directly while preserving the surrounding formatting. Bigger rewrites arrive as suggestion cards you can accept or dismiss, not as text slammed into your document. Anyone who's watched an AI enthusiastically reformat a 40-page report knows why this is the right default.

Sheets is where things get interesting. [Claude can write formulas, build pivot tables and native charts, create new tabs — and for the gnarly jobs, it runs Python behind the scenes](https://www.absolutegeeks.com/tech-news/claude-just-invaded-google-docs-and-gemini-should-be-worried/). Merging two messy tables or scrubbing a dataset with inconsistent dates is exactly the kind of job people describe to a chatbot and then rebuild by hand. Now Claude does the work and writes the results back into the sheet. If you've ever spent a Friday afternoon untangling a spreadsheet someone else broke, this is the feature you'll notice first.

Slides is narrower but thoughtful: new slides are built from your deck's existing layouts and themes rather than some generic template, and Claude checks its own output for overlapping elements, content spilling off slides and unreadable text — the classic tells of AI-generated decks.

## The approval gate is the real feature

The detail I like most isn't a capability, it's a constraint. By default, every edit needs your approval before it lands — Anthropic's "Ask before edits" mode. There's an "Accept all edits" toggle for when you're feeling brave, but the default assumes, correctly, that you might not want a language model rewriting your board report unattended.

This is a meaningful design choice in a week where AI agents are being handed ever-longer leashes. An assistant that edits your files *and* shows you each change first is an assistant you can actually trust with real work. Trust, it turns out, ships as a checkbox.

## The limits, honestly

It's a beta, and it shows. The sidebar can only see the file you have open — it can't reach other files in your Drive, and it can't interact with Docs comments, which limits its usefulness in the collaborative workflows where Docs actually lives. Charts added to Slides land as static images rather than editable objects. And yes, you need a paid Claude plan; free users are standing outside the house looking in.

## Why the timing is not a coincidence

Gemini has been sitting in Workspace side panels since June 2024 — a two-year head start on home turf. [OpenAI took a different route in August](https://www.absolutegeeks.com/tech-news/claude-just-invaded-google-docs-and-gemini-should-be-worried/), letting ChatGPT open and update Drive files, but those edits happen inside ChatGPT rather than in Google's apps. Anthropic is now covering both directions at once: in your files, and from its chat.

There's a delicious subplot too. Microsoft's agentic Office editing features run partly on Anthropic models — meaning Anthropic is competing with Microsoft at the application layer while supplying the engines behind parts of Copilot. Claude is already generally available inside Word, Excel and PowerPoint, with Outlook in beta. The Google launch completes the set: one AI work layer spanning both dominant productivity ecosystems.

## The takeaway

The AI wars spent 2024 and 2025 arguing about which chatbot was smartest. The 2026 argument is about *where the AI sits*. Benchmarks are abstract; your Monday-morning spreadsheet is not. Whoever's assistant is already inside the file you're staring at has an enormous advantage — and Google has been coasting on exactly that advantage for two years.

Now the default is contestable. If you're already paying for Claude and living in Google's apps, the install takes minutes and the first thing worth trying is the most boring one: hand it the spreadsheet you hate and ask it to clean it up. Watch the approval prompts, leave "Accept all edits" off, and see whether the AI that writes like a person also edits like a colleague. That's the test that matters — not the benchmark scores.
