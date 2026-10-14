---
title: "NVIDIA's 74-billion-parameter model leaves the data centre — and only 9 billion of it is awake"
date: 2026-10-15
subtitle: "Nemotron 3.5 Bolt arrives today, fully open source, squeezed into 24GB with 2-bit quantization. The local-agent era is officially on — read the footnotes."
tags: AI news, open source, local AI
excerpt: NVIDIA releases Nemotron 3.5 Bolt 74B A9B today: 74 billion parameters, 9 billion active per token, fitting in 24GB via 2-bit quantization — fully open source and running on llama.cpp, Ollama and LM Studio from day one. All the performance claims, though, are NVIDIA's own.
disclosure: false
sources:
- [Tech Times — 74-billion-parameter AI fits in 24GB laptop](https://www.techtimes.com/articles/328981/20261014/nvidia-rtx-spark-launches-friday-74-billion-parameter-ai-fits-24gb-laptop.htm)
- [alfw.ai — Nemotron Bolt 74B: 74B in 24GB, Only 9B Active](https://alfw.ai/article/nvidia-nemotron-bolt-74b-24gb/)
- [Gadget Pilipinas — RTX Spark launch week software updates](https://www.gadgetpilipinas.net/2026/10/nvidia-rtx-spark-launch-week-software-updates/)
- [Blockchain.News — NVIDIA RTX Spark software ecosystem updates](https://blockchain.news/news/nvidia-rtx-spark-software-ecosystem-updates-october-2026)
---

Today is the day a 74-billion-parameter AI model becomes a laptop workload.

NVIDIA releases [Nemotron 3.5 Bolt 74B A9B](https://www.techtimes.com/articles/328981/20261014/nvidia-rtx-spark-launches-friday-74-billion-parameter-ai-fits-24gb-laptop.htm) today — 15 October — a model with 74 billion parameters that fits inside 24 gigabytes of memory. That's one high-end consumer GPU. Or, pointedly, the memory class of the RTX Spark laptops that go on sale tomorrow.

Let's get the important part out of the way first: 74B is the marketing number. The number that does the work is 9B.

## The trick: a big brain, asleep in parts

Bolt 74B is a [sparse mixture-of-experts model](https://alfw.ai/article/nvidia-nemotron-bolt-74b-24gb/). All 74 billion parameters live in memory, but only about 9 billion of them wake up for any given token. Different tokens get routed to different specialist sub-networks by a gating mechanism trained alongside the model. So in terms of actual compute per inference, it behaves more like a 9-billion-parameter model — while carrying around the knowledge base of a 74B one.

That alone wouldn't get it onto a laptop. The second trick is [2-bit quantization-aware training](https://www.techtimes.com/articles/328981/20261014/nvidia-rtx-spark-launches-friday-74-billion-parameter-ai-fits-24gb-laptop.htm): instead of training at full precision and squishing the weights afterwards (the usual method, and the one that turns quality to mush at aggressive ratios), NVIDIA simulated the 2-bit precision loss *during* training, so the model learned to compensate. Result: a 74B-class model occupying 24GB at inference, where a dense full-precision model of comparable size would want well over 140GB.

Neither trick is brand new — MoE is the architecture family behind Mixtral and DeepSeek-V3 — but stacking them this aggressively, in a model purpose-built for *agents* (coding help, tool calls, monitoring, background tasks running resident on your machine), is.

## And it's actually open

This is the part that makes the launch matter beyond NVIDIA's hardware sales. Bolt 74B ships fully open source — weights, training data, and training recipes. Not open-weight-but-hush-about-how: the whole recipe.

That openness shows in the day-one support. It runs through [llama.cpp, Ollama, vLLM, Unsloth and LM Studio](https://blockchain.news/news/nvidia-rtx-spark-software-ecosystem-updates-october-2026) from launch, and it's wired directly into agent frameworks like Hermes and OpenClaw. There's even a new [Llama for Windows app](https://www.gadgetpilipinas.net/2026/10/nvidia-rtx-spark-launch-week-software-updates/) — a system-tray GUI built with Hugging Face that lets you download and run local models without touching a command line. A smaller sibling, Bolt E4B, follows on 23 October, aimed at conversational agents and game NPCs — developers can try it inside SkyrimNET, an AI-NPC modding platform for Skyrim. Yes, really.

The surrounding software push makes NVIDIA's real bet clear. PAIR — the Personal AI Router — left beta on Tuesday: a free, open-source tool that auto-discovers GPUs on your local network and spreads inference across them (NVIDIA has tested it across 18 devices, and it supports everything from RTX 20-series cards to Apple M4 chips). Meanwhile Switchyard, NVIDIA's hybrid routing library, addresses the obvious question — what happens when the local model isn't smart enough? LangChain reported cutting its AI costs 74% by routing just 7% of calls to frontier cloud models, accepting a 6% accuracy tradeoff.

One product is the model. The strategy is a habit: run the easy stuff on your own hardware for free, escalate to the cloud only when it counts.

## The honest footnotes

All of which is great — and all of which comes with caveats, because every performance claim so far is NVIDIA's own. "Faster than common dense models, stronger than similar-footprint MoE models" is vendor framing with no released weights behind it until today. Independent benchmarks will tell the real story now that the model is public.

Two footnotes deserve particular attention. First, the 24GB figure is the *weights* footprint — actual deployment memory also depends on context length, KV cache, runtime overhead, and whatever agent harness you're running alongside it. "Fits in 24GB" and "runs well on 24GB with a real workload attached" are different sentences. Second, NVIDIA's claim that local LLM downloads are already five times higher than last year arrives with no dataset, no measurement period, and no methodology. Plausible direction; unverifiable magnitude.

The biggest open question is the 2-bit quantization itself. It's one thing to compress a model that hard and keep its benchmarks intact; it's another to keep it reliable at agentic tool use, where small errors compound across a multi-step run. That's exactly what today's release lets everyone finally test.

## Why this one's worth watching

For the last two years, "local AI" has meant either running genuinely small models or renting a workstation-class machine. Bolt 74B is the moment the marketing number for a laptop model reached 74B while the model doing the work stayed in single digits — and the recipe is open, so the whole ecosystem can optimise for it on day one.

I keep coming back to a line from the alfw.ai writeup: if the quantization holds, NVIDIA has built a local agent model that's open enough to build on and small enough to leave running. If the quantization shows, the launch is still instructive — it'll mark the point where shrinking became the frontier. Either way, the interesting number to benchmark today isn't 74B. It's 9.
