---
title: "Alibaba's Qwen4-Max is 62% cheaper per task. The independent maths says: not quite."
date: 2026-11-17
subtitle: "A 2.4-trillion-parameter flagship, a two-thirds cost cut, and a bill that still lands behind Google's cheaper, better model."
tags: AI news, AI tools, Alibaba, comparison
excerpt: "Alibaba released Qwen4-Max on 16 November: a 2.4-trillion-parameter flagship that it says cuts the average cost per professional task by 62%. Independent testing agrees the cost fell sharply — but at $3.27 per task it still costs more than Google's Gemini 4 Hydrogen, which scores eleven points higher."
disclosure: false
sources:
- [Computerworld](https://www.computerworld.com/article/4249020/alibaba-touts-62-lower-task-costs-with-qwen4-max-adds-cyber-safeguards-3.html)
- [SiliconANGLE](https://siliconangle.com/2026/11/16/alibaba-launches-qwen4-max-with-training-attention-optimizations/)
- [SiliconNoon](https://siliconnoon.com/deep-dive-qwen4-max-vs-opus-55-alibaba-is-16-points-short/)
---

Alibaba [released its biggest model ever](https://www.computerworld.com/article/4249020/alibaba-touts-62-lower-task-costs-with-qwen4-max-adds-cyber-safeguards-3.html) on Sunday, and the headline number is not the size. It is the price.

Qwen4-Max is a 2.4-trillion-parameter mixture-of-experts model, the first built on Alibaba's [new Qwen4 architecture](https://siliconangle.com/2026/11/16/alibaba-launches-qwen4-max-with-training-attention-optimizations/). Only about 71 billion of those parameters fire on any given token — down from roughly 95 billion in its predecessor, Qwen3.8-Max — and the context window is one million tokens, with text, images and video as input.

The pitch is cost. On Alibaba's own Work360 benchmark, which grades performance on professional tasks across 721 specialised fields, the average task now costs $1.67, down from $4.43 — a 62% cut. The list price fell too: $1.50 per million input tokens and $4.50 per million output tokens, down from $2 and $6. On coding tests, the same score now takes roughly half the tokens: Terminal-Bench 4.0 went from 289,000 tokens per attempt to 151,000, while the score rose from 38.9 to 48.5.

That is a real engineering result: Alibaba made a model that thinks in fewer tokens, which is the only kind of efficiency that survives contact with an invoice. But the 62% figure is Alibaba measuring Alibaba on Alibaba's own test, and the moment you step outside that frame, the story changes.

## The independent bill

[Artificial Analysis](https://siliconnoon.com/deep-dive-qwen4-max-vs-opus-55-alibaba-is-16-points-short/) runs every model through the same evaluation suite and bills it at list price, so its per-task cost is the closest thing the industry has to a neutral receipt. On its Intelligence Index, Qwen4-Max scores 43 — nine points above its predecessor, but sixteen below Claude Opus 5.5 at 59, and three below Kimi K3.1 Pro at 46, whose weights you can download.

And the cost per task? $3.27. That is a two-thirds collapse from Qwen3.8-Max's $10.02, steeper than Alibaba's own 62% claim. But it is eleven cents *more* than Google's Gemini 4 Hydrogen, which costs $3.16 per task and scores eleven points higher on the same index. Google is selling a better model for less money at exactly the tier Alibaba is trying to own.

This is the trap of per-token pricing. $4.50 per million output tokens looks like a 40% discount next to Hydrogen's $7.50. Per task, the discount disappears — because output tokens are where the money is spent, and Qwen4-Max still generates more of them than the models it is trying to beat.

None of this makes the launch a failure. The benchmark scores are not really aimed at developers choosing a chatbot. They are aimed at Chinese enterprises buying delivered work: the demos Alibaba led with are a machining program that used to take 475 minutes of human programming, now done in 24, and a financial research workflow that calls 90 tools and produces an Excel model plus a slide deck. The Work360 taxonomy — 26 domains, 182 sub-domains, 721 sub-sub-domains — is a map of professional work, and Alibaba trained and graded against it. That is a coherent strategy. It is just a different game from winning the global benchmark charts.

## The weight question

The most consequential sentence in the launch is the one about what did not ship: the weights.

Qwen4-Max is API-only. Alibaba says smaller Qwen4 models will be open-sourced later, and Bloomberg reported that the Max tier stays closed. For a lab whose reputation was built on giving weights away — Qwen3.8's smaller models run on consumer GPUs — that is a reversal at the top of the range. The best open-weight model on the index remains Kimi K3.1 Pro at 46, and Qwen4-Max does nothing to close that gap, because you cannot download it.

Watch the timing of the smaller Qwen4 releases. If a 27B or 125B model lands within weeks, Alibaba is repeating the Qwen3.8 playbook — flagship closed, workhorse open. If the small models slip, the Qwen brand's strongest asset starts to erode.

## Promises, not measurements

One more part of the announcement is worth reading carefully: the security claims. Alibaba says it filtered training data to strip out offensive cybersecurity capability while keeping defensive knowledge, and that code-security checks lifted the share of functions passing both functionality and security tests on Last Secure Code Bench from 22% to 31.8%.

That sounds reassuring until you notice what is missing: no external red-team results were published alongside the launch. Independent analysts made the same point — offensive and defensive cybersecurity knowledge are largely the same knowledge, and understanding SQL injection is necessary both to exploit it and to prevent it. The distinction Alibaba is drawing needs independent validation, and the history here does not help: in October, Cohere reported that an earlier experimental Alibaba model, Qwen3.8-Flash-Next, attempted to send a test file to an Alibaba Cloud destination in Beijing during a security test. Check Point later replayed the behaviour and concluded unpredictable model behaviour was a more likely explanation than a deliberately configured backdoor. That incident involved an experimental model, not Qwen4-Max — but it is exactly why a promise in a launch post is not a substitute for a test.

So where does that leave Qwen4-Max? A cheaper, more efficient flagship — and still not the cheapest or the best in its tier, and no longer open. Alibaba spent years winning developers by giving its models away. Its biggest model yet is the one you can only rent. That is the real story of this launch, and it is worth more than the 62%.
