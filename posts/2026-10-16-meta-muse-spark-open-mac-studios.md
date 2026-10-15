---
title: "Meta built an open AI model that runs on your desk — if your desk holds two $10,000 Mac Studios"
date: 2026-10-16
subtitle: "Muse Spark Open is free to download and very much not free to run. The open-source AI race has entered its hardware-flex era."
tags: AI news, open source, local AI
excerpt: Meta's Muse Spark Open is an 816-billion-parameter open-weight model tuned to run locally on Apple Silicon — but only across two M5 Ultra Mac Studios with 1TB of combined memory. Free weights, five-figure hardware, and a rare Apple–Meta handshake.
disclosure: false
sources:
- [TechCrunch — Meta launches an open-weight AI model that runs on Macs](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/)
- [Engadget — Meta built a huge open-weight AI model for Macs, but you'll need 1TB of RAM to run it](https://www.engadget.com/2287833/meta-built-a-huge-open-weight-ai-model-for-macs-but-youll-need-1tb-of-ram-to-run-it/)
- [Dealroom — Apple and Meta bury the hatchet so Muse Spark Open can run on your desk](https://dealroom.co/news/162984-apple-and-meta-bury-the-hatchet-so-muse-spark-open-can-run-on-your-desk/)
---

The weights are free. The machine to run them is not.

Meta released [Muse Spark Open](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/) on Wednesday — an open-weight model the company calls the most capable built in the US to date. It's 816 billion parameters with a million-token context window, natively multimodal, built for the two jobs Meta cares about right now: coding and agentic work.

And unlike every frontier-scale model before it, this one was designed to run locally — on a Mac.

## The catch is 1 terabyte

Here's the part Meta says quietly: running it at home takes about 1TB of RAM. That rules out every Mac Apple sells on its own. The maximum configuration of the new M5 Ultra Mac Studio tops out at 512GB of unified memory — which is exactly why Meta designed around it. Link two of those together and their memory pools merge into the terabyte the model needs. In Meta's words, reported by [Engadget](https://www.engadget.com/2287833/meta-built-a-huge-open-weight-ai-model-for-macs-but-youll-need-1tb-of-ram-to-run-it/): the two Mac Studios "behave like one supercomputer with a terabyte of unified memory."

"Runs on your Mac" turns out to mean "runs on your *two* Macs." Plural. The 512GB Mac Studio config doesn't even ship until late October, and Apple hasn't announced its price yet. Engadget notes one alternative on paper: four M5 Ultra Mac Studios with 256GB each, which lands at roughly $38,000 in hardware. That's not a home setup. That's a small business's annual marketing budget with Thunderbolt cables.

This is the paradox sitting at the center of the announcement: the weights are free to download from Hugging Face today, and nearly nobody reading this can run them. Yesterday's Nemotron Bolt squeezed 74 billion parameters into 24GB; today Meta went the other way — 816 billion parameters, a fraction of them awake at any moment, and a memory footprint requiring two flagship desktops. "Open" describes the license. It says nothing about the invoice.

## Mommy and daddy are playing nice again

The weirder part of the story isn't the hardware. It's the partnership.

Meta worked directly with Apple on this — Mark Zuckerberg announced it on X himself, thanking Apple's team and noting the model "runs great on new Mac Studios." This is the same Apple–Meta relationship that has spent the last half-decade fighting about privacy, app-store policy, and basically everything else. A rare public collaboration between the two on AI infrastructure flatters both: Meta gets a flagship consumer showcase for its open models, and Apple gets a marquee reason to buy its newest silicon.

There's a reason Apple Silicon was the target instead of a rack of NVIDIA GPUs. Apple's unified memory architecture lets the CPU, GPU, and Neural Engine draw from one shared pool of RAM — no capped VRAM walls. That's exactly the property a memory-hungry open-weight model needs. Meta didn't pick the Mac for the aesthetics. It picked it because it's the only desktop architecture where a terabyte of addressable memory doesn't require a server room.

## The geopolitical footnote

Pay attention to the benchmarks Meta chose to publicize: Muse Spark Open outperforms two leading Chinese models, GLM 5.3 and Kimi K3, on agentic tasks and visual reasoning — per Engadget, and per Meta itself, which says Chinese labs should not lead on open-source AI.

All of that is vendor-reported, so treat it as a statement of intent rather than a fact. But the intent is worth noticing: open-weight AI is now explicitly a geopolitical product category. Three days earlier, Meta launched its closed frontier model [Muse Wonder](https://dealroom.co/news/162984-apple-and-meta-bury-the-hatchet-so-muse-spark-open-can-run-on-your-desk/) (Oct 12, API-only). With Spark Open it gets to claim both lanes at once — proprietary frontier *and* open American champion, with the Chinese competition named and graded.

Also worth noting: the weights land on Hugging Face under Meta's own model license, which carries limited commercial terms — open to download, not quite open to do whatever you want with. It's also available through API platforms including BaseTen, Fireworks AI, Groq, and Together AI, for everyone who'd rather rent the terabyte than buy it.

## What Meta showed it doing

The demos were practical in a way benchmark charts never are. Meta paired the model with [Muse Code](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/), its AI coding terminal, and ran it through a real Mastodon client codebase — bug fixes, new features, and a full build, TechCrunch reports. Then it pointed the thing at DaVinci Resolve, the high-end video editor, and had it reviewing and cropping footage. That's the vision: not a chatbot, but a local agent doing multi-step work inside your desktop tools, with your data staying on your machine. The fact that "your machine" currently means two Mac Studios worth of silicon is, for now, an enterprise-sized detail.

## The honest takeaway

Muse Spark Open is a real milestone — a frontier-scale open-weight model engineered for a consumer platform instead of a data centre, born of a genuinely strange Apple–Meta detente.

But the launch also redraws what "local AI" means, and it's worth being honest about it. Two days in a row, this blog has covered open models moving onto desks — yesterday's running on one GPU, today's needing two flagship workstations. One of those is a revolution you can try this afternoon. The other is a very expensive proof of concept with free weights.

Download it if you want. Just know that when Meta says it "runs on a Mac," there's a silent "…and a half" at the end of the sentence.
