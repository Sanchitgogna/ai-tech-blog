---
title: Anthropic just told investors its AI may soon improve itself — and that it might not notice in time
date: 2026-11-05
subtitle: The scariest sentence in Anthropic's IPO filing isn't the warning. It's the admission that came just before it.
tags: AI news, AI safety, Anthropic, AI agents
excerpt: In an amended IPO filing, Anthropic said future models may "imminently" meet its own threshold for AI that dramatically accelerates AI research — and admitted it has missed such accelerations before, only spotting them afterwards.
disclosure: false
sources:
- [TechCrunch](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)
- [The Neuron](https://www.theneuron.ai/news/how-close-is-anthropic-to-ai-that-can-improve-itself/)
- [Pondero](https://pondero.ai/news/2026-11-03-anthropic-ipo-self-improvement-risk/)
---

Buried in the risk factors of Anthropic's amended IPO filing, filed with the US Securities and Exchange Commission on 2 November, sits a sentence that would sound like science fiction if it weren't written in the driest legal prose available. Anthropic's internal estimates, the filing says, indicate that its future models "may imminently meet" its own definition of "dramatically accelerated progress attributable to AI" — the point where AI starts meaningfully speeding up the research that builds the next AI. Researchers call that recursive self-improvement, or RSI.

But the warning is not the most interesting part. The admission just before it is: Anthropic says it has "in the past not identified, and may in the future not identify, a significant acceleration in our rate of development until after it has occurred." The company has built a tripwire for one of the most consequential thresholds in AI, and it is telling investors, on the record, that its tripwire has already failed to fire on time at least once.

That is the story. Not that self-improving AI has arrived — Anthropic is explicit that no current model has been designated as crossing the threshold. The story is that the world's most safety-conscious AI lab just confessed, in a document where misleading investors carries legal consequences, that it cannot reliably tell when it has crossed its own red line.

## What the threshold actually measures

Anthropic's Responsible Scaling Policy is its internal rulebook: capability thresholds that, once crossed, trigger safety obligations before a model can be deployed. The relevant one is its automated research threshold, met in two ways: AI can replace the company's entire research workforce at a competitive cost, or AI-driven progress dramatically accelerates overall AI capability.

For the acceleration route, the bar is specific. As [The Neuron](https://www.theneuron.ai/news/how-close-is-anthropic-to-ai-that-can-improve-itself/) explains, progress would need to roughly double relative to both the expected pace and the fastest sustained historical pace across at least three model generations — think two years of expected capability gains arriving in one year — with evidence that AI automation, rather than extra computing power or more researchers, was substantially responsible.

That demanding definition matters, because it stops the filing from being read as "Claude can now build itself." It cannot, by Anthropic's own account. What the filing claims is narrower and stranger: that estimates for *future* models, not current ones, point toward that bar being met soon.

## Claude is already doing the homework

The claim is plausible because Claude is already deeply embedded in building its own successors. Anthropic's research puts Claude at more than 80% of code merged into its production codebase as of May 2026, and above 90% of code contributions by September, with daily contributions per engineer more than 45 times their 2024 level.

Those numbers deserve a pinch of salt: writing more code is not doing better research, and engineers still decide which experiments are worth running. Independent evidence leans the same cautious way. In September, the evaluation organisation METR tested Claude Opus 5.5 on difficult research tasks, found improved research capability, but judged full automation of the research process unlikely. A separate preliminary METR estimate put AI-attributable acceleration at roughly 1.5 times — below Anthropic's doubling bar, and admitted to carry substantial uncertainty.

So the honest picture is a gap: Anthropic's internal estimates say "imminently," independent testing of an earlier model says "not yet." Both can be true, because they measure different models at different moments — and because nobody seems entirely sure how to measure this in real time.

## A promise that is a policy, not a lock

Anthropic did follow the warning with a commitment: it does not anticipate being able to safely use Claude to fully autonomously design and build successive generations of frontier models without meaningful human supervision, and it is considering updates to its Responsible Scaling Policy to keep humans in control.

Note the wording. "Considering updates" to a policy is not a technical safeguard. Nothing in the filing describes a mechanism that would physically stop a future model from crossing the threshold before a policy update catches up — precisely the gap the filing itself flags. A policy is a promise about what a company will do. The filing's admission is about what a company can *know*.

## Why this one matters

AI labs warn about things constantly. What makes this filing different is the venue. Anthropic usually talks about safety in blog posts and policy documents, where the standard for what can be asserted is whatever the company feels like asserting. A prospectus is different: it is read by investors deciding whether to buy stock, and its claims carry legal weight. [Pondero](https://pondero.ai/news/2026-11-03-anthropic-ipo-self-improvement-risk/) puts it well — what changes here is the evidence trail.

If both halves of that admission are right, the interesting question for the next year is not whether some lab announces RSI. It is whether anyone — the labs, independent evaluators like METR, or regulators — can build a speedometer that works while the car is still accelerating, rather than one that only tells you afterwards how fast you went. Until that measurement problem is solved, every RSI claim will have the same shape as this one: a confident forecast sitting on top of an admitted blind spot. Anthropic deserves credit for writing the blind spot down.
