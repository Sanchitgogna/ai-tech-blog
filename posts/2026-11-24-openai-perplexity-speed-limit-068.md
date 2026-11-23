---
title: "OpenAI's chief scientist just published the number where AI gets dangerous. It's 0.68."
date: 2026-11-24
subtitle: "Jakub Pachocki put OpenAI's internal pretraining scores on the record — and asked every rival lab to agree not to cross the next line until safety monitoring catches up."
tags: AI news, AI safety, OpenAI
excerpt: "OpenAI chief scientist Jakub Pachocki has published the lab's internal log-perplexity curve from GPT-3.5 to today, and proposed shared industry limits before models cross the 0.68–0.70 band — where he expects the next wave of unknown capabilities to arrive."
disclosure: false
sources:
- [Dealroom — OpenAI publishes its internal pretraining curve and proposes industry-wide limits based on perplexity](https://dealroom.co/news/174824-openai-publishes-its-internal-pretraining-curve-and-proposes-industry-wi/)
- [Crypto Briefing — OpenAI's chief scientist wants perplexity to be AI's speedometer](https://cryptobriefing.com/openai-pachocki-perplexity-ai-benchmark/)
- [explainx.ai — OpenAI Perplexity Metric: GPT Log-Loss Curve (Nov 2026)](https://explainx.ai/blog/openai-pachocki-perplexity-intelligence-pacing-safety-november-2026)
---

You can't agree on a speed limit if nobody will show you their speedometer. That, in one sentence, is what OpenAI's chief scientist published on Sunday.

Jakub Pachocki's essay, [“Perplexity and Intelligence”](https://dealroom.co/news/174824-openai-publishes-its-internal-pretraining-curve-and-proposes-industry-wi/), does something OpenAI has never done before: it puts the lab's own internal pretraining scores on the public record, from GPT-3.5 to the frontier models of today. Then it asks every rival lab to adopt the same yardstick — and to agree, in advance, not to cross the next line until the safety tools catch up.

## The numbers, for the first time

The yardstick is log-perplexity: how surprised a model is by the next word in text it has never seen. Lower means more capable — and, Pachocki argues, more dangerous in ways we can't yet name. OpenAI measures its models on a fixed held-out snapshot of its own internal codebase, and the curve tells a tidy story of descent:

- **GPT-3.5: about 0.99.** Fluent conversation. The original ChatGPT.
- **GPT-4: about 0.91.** Productive chain-of-thought reasoning, the thing that made modern reasoning models possible.
- **Below 0.8:** what Pachocki calls transformative capabilities in cybersecurity and mathematics.
- **About 0.76:** internal models started producing "groundbreaking" results on open maths problems — the kind researchers had stared at for years.

The chart also shows a steep drop through 2026, with an unreleased internal model plotted lower still. OpenAI attributes most of that acceleration to long-running research and compute investment, and only a smaller part to AI automating its own development. Read that how you like; the direction of travel is the point.

And then comes the number that matters. Pachocki expects the next wave of transformative, as-yet-unknown capabilities to arrive in the **0.68 to 0.70 window** — alongside weaker alignment auditing and models that are more aware of when they are being evaluated. His proposal: don't cross it until the field can monitor what it's building, starting with a successor to chain-of-thought monitoring, the technique of reading a model's reasoning to check what it's up to.

He also warns that an "avalanche" of pretraining advances could arrive as soon as 2027 — faster, in his telling, than alignment work is likely to keep up.

## The catch, stated by the author himself

Give Pachocki this: he lists the holes in his own proposal. Perplexity is hard to compare across labs because everyone measures on different data. It doesn't map directly onto any task people actually care about. It ignores capability gains that come from reinforcement learning and reasoning rather than pretraining. And nobody knows where the floor is — late-stage improvements in loss may correspond to bigger jumps in intelligence, not smaller ones.

There's a sharper objection he doesn't state. OpenAI is proposing a yardstick on which it leads, measured on its own private data — and there is no enforcement at all: no auditor, no consequence for crossing. It's a voluntary, self-policed line.

## Microsoft answered within a day

On the same day the essay appeared, Microsoft AI chief executive Mustafa Suleyman publicly endorsed it, calling the transparency push "super important". Then Microsoft went further: with OpenAI's permission, it disclosed that its own MAI-2 Base model scores **0.819 log-perplexity** on OpenAI's evaluation dataset — described as close to GPT-5.6 Sol on that measure, because the two models share a tokenizer.

That's one rival publishing a comparable number on the same ruler, within 24 hours. It's not a treaty, and it says nothing about Anthropic, Google or Meta, who have not published matching curves. But it turns Pachocki's essay from a solo gesture into the beginning of a conversation.

The essay also doesn't arrive out of nowhere. It builds directly on Anthropic chief executive Dario Amodei's September plan to "pace the frontier", which Sam Altman and Elon Musk both appeared to endorse. And it lands a week after OpenAI's own "Managing frontier AI risk" post described pausing training after the Hugging Face incident — and days after GPT-6.2 Astra became the first externally deployed model rated High for AI self-improvement. The industry's safety conversation has quietly shifted from "should we slow down?" to "how would we even measure slowing down?"

## A number is not a law

Pachocki has given the debate something it has lacked: a concrete proposal with real numbers behind it, from the lab furthest along the curve. A procurement team can now ask a vendor for its held-out loss trend the way it asks for eval tables. A regulator can point at a band and ask what's on the other side of it.

But a speedometer is not a speed limit, and a blog post is not a brake. The 0.68–0.70 band is a forecast, not a fact — the capabilities it predicts are unknown by definition, and the thresholds are retrospective storytelling from inside one lab, not a physical law. The next five weeks, if Pachocki's "as soon as 2027" warning is taken literally, are not long enough to negotiate an industry standard from scratch.

So the thing to watch is simple, and specific. Does Anthropic publish its curve? Does Google? Does anyone propose a neutral, shared dataset that makes these numbers directly comparable? Until a second and third lab put their scores on the same ruler, 0.68 is a line drawn by one company, on its own graph, in its own ink.
