---
title: "Meta launched a 10-cent model and Anthropic launched an $8 one on the same day. The gap is the story."
date: 2026-11-10
subtitle: "Muse Ember does the boring work for almost nothing; Claude Fable 5.2 does the spectacular work for a fortune. The AI market has quietly split in two."
tags: AI news, comparison, AI agents, AI tools
excerpt: "On 9 November, Meta shipped Muse Ember at $0.10 per million input tokens while Anthropic shipped Claude Fable 5.2 at $8. The 80x price gap isn't a pricing war — it's the industry admitting that 'an AI model' is now two very different products."
disclosure: false
sources:
- [Meta Research](https://research.meta.ai/blog/muse-ember)
- [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/meta-and-anthropic-push-ai-models-into-more-complex-work/)
- [Sulat AI & Tech News](https://news.sulat.com/2026/11/10/claude-fable-5-2-mythos-devin-early-access-builds/)
---

Two frontier labs launched new models on the same day, Monday 9 November. One costs ten cents per million input tokens. The other costs eight dollars. That is not a rounding error, and it is not really a price war either. It is the AI market quietly splitting into two products that happen to share the name "model".

Meta's entry is Muse Ember, the smallest and cheapest model in its Muse family. It is built for the work AI agents repeat all day: calling tools, running coding subtasks, routing requests, pulling facts out of long documents. It costs $0.10 per million input tokens and $0.50 per million output tokens, with cached input at $0.004, a 1-million-token context window and up to 512,000 output tokens. [Meta's own pitch](https://research.meta.ai/blog/muse-ember) is that Ember matches Claude Haiku 5.5's best score on the Artificial Analysis Intelligence Index — 36 — at about a third of the cost per task: $0.14 against Haiku's $0.41.

Anthropic's entry is Claude Fable 5.2, alongside Claude Mythos 5.2 — the same underlying model with different locks. Fable is the one anyone can use; Mythos, with fewer safeguards for cybersecurity and life-sciences work, goes only to organisations vetted through Anthropic's verification programmes. Fable costs $8 per million input tokens and $40 per million output, down from $10 and $50 for the 5.1 versions, and Anthropic says it generates output up to 30 per cent faster. It is aimed at the most demanding technical work: coordinating more than 1,000 agents at once, advanced software engineering, hardware design, even controlling robots.

## The cheap one is the honest one

Here is the part worth sitting with. Ember's headline prices are identical to Haiku 5.5's and OpenAI's GPT-6 Luna — $0.10 and $0.50. Meta has not cut the price of a token. What it claims is that Ember does more work per token: fewer tokens burned per finished job, cheaper cached input, shorter outputs. That is a narrower claim than "we made intelligence cheaper", and a more believable one. [Meta says](https://research.meta.ai/blog/muse-ember) Ember is the first model trained using Muse Wonder Full, its biggest model, and it positions the family as a division of labour: Wonder plans, Spark handles coding and agentic workflows, Ember does the volume.

That division of labour is the real announcement. Agents spend most of their tokens on small structured steps — read a file, run a test, call an API, check a result. Sending every one of those steps to a frontier model is like hiring a barrister to open your post. Ember exists because the economics of agents only work if the boring steps are nearly free. Meta's framing is blunt about it: a cost "low enough to run in every product, for everyone".

## The expensive one is the showpiece

Fable 5.2's launch was a parade of spectacles, and the honest thing to do is report them as Anthropic's claims, because most of them are not independently verified. A team of 1,000 Fable agents formalised the proof of Fermat's Last Theorem in the Lean language in 30 hours; the same setup running Opus 5.5 managed 26 per cent of it in 18 hours. Two preprints claim new results in black-hole physics — preprints, not peer-reviewed papers. One tester built a browser spreadsheet over 50 hours at an estimated US$11,700 of tokens. Another built a playable shooter in Unreal Engine over three days at roughly US$15,000.

The early testers were candid about the bill, at least. Every's chief executive Dan Shipper said the projects his staff built were "slow and burns through tokens" and that their early access was free — "these projects would have been expensive at API rates". Wharton professor Ethan Mollick, who had pre-release access, reported that the agents building his endless-worlds project set up a review process whose rule book grew to 204 sections and 87,500 words, and output slowed from hundreds of worlds a day to about a dozen. "Most critically, the AI did not notice these problems itself," he wrote.

## Two tiers, one bill

Put the two launches together and the shape of the market becomes clear. At the bottom, a race to make the routine step nearly free — Ember at $0.14 a benchmark task, Haiku and Luna at the same per-token price. At the top, a race to make the spectacular step possible at any price — Fable coordinating a thousand agents to formalise a theorem, with a fast mode that doubles the price for up to 2.5 times the speed. The gap between the tiers is now 80 times on input tokens.

That split is good news and bad news at once. The good news is that the boring tier is where most real work lives, and it is getting cheap fast — cheap enough that agents stop being a demo and start being infrastructure. The bad news is that the top tier's demos are priced like moonshots: a spreadsheet for $11,700, a game for $15,000. For most people, Fable 5.2 is a thing to read about, not a thing to run.

So the question to ask about any agent product from here on is not "which model does it use?" but "which tier does it live in, and who is paying for the other one?" Meta and Anthropic answered on the same day. One is building the engine room. The other is building the penthouse. The price tags say it louder than the press releases.
