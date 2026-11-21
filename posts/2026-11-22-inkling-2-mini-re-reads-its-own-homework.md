---
title: "This AI re-reads its own homework three times — and it runs on your laptop"
date: 2026-11-22
subtitle: "Thinking Machines' Inkling 2 Mini loops its middle layers instead of growing bigger, and ties Alibaba's flagship on the benchmarks that matter for coding."
tags: AI news, AI tools, open source, local AI
excerpt: "Inkling 2 Mini is a 26.4-billion-parameter open-weights model that runs its middle layers three times per token instead of stacking more parameters — and on agentic coding benchmarks it ties a model with nearly eight times the active parameters, on hardware you already own."
disclosure: false
sources:
- [VentureBeat — Thinking Machines wows with Inkling 2 Mini looped transformer model that runs locally on laptops](https://venturebeat.com/technology/thinking-machines-wows-with-inkling-2-mini-looped-transformer-model-that-runs-locally-on-laptops)
- [Artificial Analysis — Thinking Machines has released Inkling 2 Mini, an open weights looped transformer](https://artificialanalysis.ai/articles/inkling-2-mini)
- [The Decoder — New open model Inkling 2 Mini thinks in loops to solve problems with fewer words and still runs on a laptop](https://the-decoder.com/new-open-model-inkling-2-mini-thinks-in-loops-to-solve-problems-with-fewer-words-and-still-runs-on-a-laptop/)
---

For two years the recipe for a better AI model has been depressingly simple: more parameters, more GPUs, more money. Thinking Machines Lab, the startup founded by former OpenAI CTO Mira Murati, just released a model that tries a different trick. Instead of growing, it re-reads.

[Inkling 2 Mini, released on 20 November](https://venturebeat.com/technology/thinking-machines-wows-with-inkling-2-mini-looped-transformer-model-that-runs-locally-on-laptops), is a 26.4-billion-parameter open-weights model that fits in about 20GB and runs on a 32GB MacBook Pro or a single desktop GPU. And on the benchmarks that measure whether an AI can actually do coding work — not just answer trivia — it keeps up with models far larger than itself.

## The loop, explained in one paragraph

A normal transformer reads each token once, top to bottom, through all of its layers. Inkling 2 Mini has 24 layers, but it doesn't run them once. The first six and last six run once; the middle 12 run three times, reusing the same weights. That adds up to 48 effective layer passes per token — the reasoning depth of a much bigger model, without storing a single extra parameter.

The analogy the lab leans on is a human one: pausing to mentally re-check a tricky equation three times before writing down the answer, instead of filling three pages with scratch work. The practical payoff is that the model does its thinking *inside* the network, where it doesn't have to write out long chains of thought as text — which is slower, more expensive, and burns output tokens.

The numbers back it up. It scores 20.1 on the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/inkling-2-mini), tying Alibaba's dense 27-billion-parameter Qwen3.8 — a model with roughly eight times the active parameters per token. On agentic coding tests it leads every open-weights model under 100 billion parameters: 48.2% on DeepSWE v1.1 and 79.2% on SWE-bench Verified. And because it does more work per token instead of more tokens per task, it costs about $0.59 per benchmark task against Qwen's $3.53, and finishes in 9 minutes instead of 38.

## What it actually runs on

This is the part that matters for anyone who doesn't own a data centre. The weights ship under the Apache 2.0 licence on Hugging Face, and day one brought support from the local-AI tooling everyone already uses — Ollama, llama.cpp, SGLang, vLLM. Thinking Machines demonstrated it running in airplane mode on a 48GB M5 Pro MacBook Pro, building a playable flight simulator, and powering 20 persistent autonomous villagers in a local town simulation.

That's the local-AI story this blog has been tracking all year — NVIDIA's Nemotron running on a 24GB card in October, Meta's 816-billion-parameter Muse Spark Open squeezing onto Mac Studios — taken one step further. The difference is that Inkling 2 Mini isn't a stripped-down toy version of a frontier model. On coding and tool use, it's genuinely competitive with the best open models in its size class, with a million-token context window and image input on top.

## The honest caveats

Looping can't conjure knowledge out of thin air, and Thinking Machines says so itself. Factual recall scales with total parameter count, and Inkling 2 Mini trails Qwen3.8 on Artificial Analysis's omniscience test (−8.6 against −6.4), with a lower non-hallucination rate (63.4% versus 71.4%). It also lags on multi-turn conversation and multi-constraint instructions, and can fall into repetitive debugging loops or clip its phrasing in non-English languages. If you want a model that knows things, the bigger dense models still win. If you want one that *does* things — writes code, calls tools, works through a problem — the loop is doing real work.

There's a safety question hiding in the loop, too, and to the lab's credit it didn't bury it. When a model does more reasoning internally without writing it down, it's harder to oversee. Thinking Machines shipped a companion research checkpoint with adjustable loop counts and partnered with the National Deep Inference Fabric and Goodfire to study what's happening inside. Its early tests found the model's unspoken reasoning horizon stretching from 16 seconds at one pass to 37 seconds at three — but the traces that *did* come out stayed human-legible, and there was no upward trend in covert sabotage on its control benchmark. That's reassuring, not conclusive. The right read is that a model that thinks more in its head deserves more scrutiny, not less — and the lab seems to know it.

## Why this one is different

Inkling 2 Mini is the third act in an unusually fast year for Thinking Machines. The lab raised a $2 billion seed round at a $12 billion valuation in July 2025, shipped its Tinker fine-tuning platform in October, released the 975-billion-parameter Inkling in July 2026, and opened the second generation with the 594-billion-parameter Inkling 2 Small on 5 November. Fifteen days later, the same family produced a model a twentieth of the size that runs on a laptop.

That's the bet: the next frontier isn't only bigger models, it's models that spend their compute better. Looping is one answer — spend the same weights three times instead of buying new ones. If it holds up outside the lab's benchmarks, the practical consequence is a coding assistant that runs offline, on your own machine, with your code never leaving it. For a lot of developers and a lot of companies, that's not a benchmark story. It's the whole point.
