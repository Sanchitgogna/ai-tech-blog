---
title: OpenAI is cutting Cursor off on Thursday. The real story is who owns your editor now.
date: 2026-11-08
subtitle: The cutoff affects about 5% of Cursor's traffic. The precedent affects every developer tool that rents its brain from someone else.
tags: AI news, AI tools, coding, OpenAI
excerpt: OpenAI says it will stop supplying models to Cursor on 12 November, after SpaceX bought the editor for $60 billion. Only about 5% of Cursor's traffic runs on OpenAI models — but the change-of-control clause behind the decision is now the most important line in any AI tool's contract.
disclosure: false
sources:
- [OpenAI](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)
- [Evermx](https://evermx.com/case/openai-cursor-model-cutoff)
- [Sift It](https://blog.ainetix.com/posts/cursor-spacex-60-billion-openai-model-cutoff-november-12-inkling2-thinking-machines)
---

On Thursday, 12 November, OpenAI's models are scheduled to stop working inside Cursor. The date was set in August, and this week it comes due — and whether or not it actually happens, the story it tells about who controls the tools developers use every day has already changed.

The facts are not in dispute, because OpenAI published them itself. On 28 August, two weeks after SpaceX closed its roughly $60 billion all-stock acquisition of Anysphere, the company behind Cursor, OpenAI [announced](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) it intended to wind down the contract supplying its models to the editor. The proposed shutoff is 12 November, which OpenAI says is the maximum notice its contract allows. Cursor will also not receive future models — including Astra, OpenAI's next flagship.

## The reason is a sentence, not a spreadsheet

OpenAI did not blame performance, cost, or capacity. It blamed trust. "We cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts."

That is a remarkable thing for a company to put in writing about a partner. OpenAI backs it up with two specifics: after Musk acquired Twitter — now part of SpaceX — the company broke the terms of its contract, and earlier this year Musk admitted under oath that xAI, also now part of SpaceX, had violated OpenAI's terms of service.

Behind the rhetoric sits a piece of contract law that will matter far beyond this feud. OpenAI's custom agreement with Cursor gave it a limited window to cancel after a change of control. Cursor changed owners, the window opened, OpenAI used it — and timed the cancellation to the latest date it could while still cutting off future models. The change-of-control clause, once a boring paragraph in a supply agreement, is now a weapon. Every AI tool that rents its intelligence from a frontier lab just learned that its owner can become its problem overnight.

## Five percent, and why it still matters

Cursor's chief executive, Michael Truell, replied the same night OpenAI posted. OpenAI's models account for about 5% of Cursor's user traffic, he said, and the two companies were talking to try to resolve the dispute. He also made the point that stings most: Cursor was one of OpenAI's very first users, and the team had "trusted their platform to be neutral infrastructure for our business."

He is right about the numbers. Ninety-five percent of Cursor's usage runs on other models — Anthropic's Claude above all, plus Google's Gemini and SpaceX's own Grok. Anthropic co-founder Tom Brown said the same night that Cursor "has been a trusted partner of Anthropic since Sonnet 3.5" and that Anthropic would keep increasing the compute behind Claude models in Cursor. But the 5% figure is the least interesting number here, because the cutoff was never about the 5%. It is about Truell's phrase: *neutral infrastructure*. For four years Cursor sold itself as the editor that let you pick any model. The acquisition ended that neutrality in August, whether or not the models actually disappear on Thursday. Cursor is now a SpaceXAI product that happens to resell Anthropic and Google models — and Anthropic and Google can read a change-of-control clause as well as OpenAI can.

Nor is OpenAI's move without precedent on the other side. In June 2025, Anthropic limited Windsurf's direct access to Claude models after that editor was itself the subject of acquisition drama. The labs have now all done this to each other at least once. The pattern is the point: when the tool and the model belong to rival companies, the model supply is a leash, and the leash gets pulled.

## The same week, the same direction

If the Cursor cutoff looks like a one-off billionaire feud, look at what else happened this week. Meta confirmed it had acquired Conductor, a startup that runs several AI coding agents in parallel, and scheduled Conductor's cloud service to shut down on 20 November. A different layer of the same workflow, but the same direction of travel. The companies competing at the frontier-model layer are buying up the tools developers touch, and each purchase turns a neutral marketplace into a distribution channel for one lab's models.

Three weeks ago this blog ranked the [coding assistants](https://sanchitgogna.github.io/ai-tech-blog/posts/2026-10-20-everyones-ranking-ai-coding-assistants/) on benchmarks and prices, as if the choice were about which model writes the best code. The Cursor cutoff says the choice is increasingly about something else: whose company owns the window your code passes through, and what happens to your workflow when that owner falls out with the company supplying the brain.

## What to do before Thursday

One caveat, and it matters: 12 November is a *proposed* date, and both sides say talks are ongoing. Truell said they were speaking to resolve it, and OpenAI framed the shutoff as an intention, not a done deal. It is entirely possible the deadline moves, or a revised arrangement appears. Treat it as probable, not certain.

Still, if your team runs workflows on OpenAI models inside Cursor, switch to Claude, Gemini, or Grok before Thursday rather than discovering the failure mid-task. And the longer question is worth asking now, while it is cheap: when you chose your coding tools, did you evaluate them as neutral developer tools, or as products of companies that compete with each other? If it was the former, August already changed your answer. Thursday just makes it visible.
