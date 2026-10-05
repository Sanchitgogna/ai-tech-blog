---
title: OpenAI's two newest launches aren't smarter — they're cheaper and faster
date: 2026-10-06
subtitle: GPT-6.1 Sol costs a fifth of the flagship. Astra Ultrafast runs up to 8x faster at six times the price. The intelligence race just became a serving race.
tags: AI news, AI tools, comparison
excerpt: In the span of a week, OpenAI released GPT-6.1 Sol — near-flagship coding ability at one-fifth of Astra's price — and rolled out the Astra Ultrafast serving tier, which trades up to 8x speed for a 6x price multiple. Meanwhile the planned GPT-6.1 Astra upgrade was quietly shelved. What matters in AI models is no longer just how smart they are.
disclosure: false
sources:
- [NeoTeo: GPT-6.1 Sol pricing](https://www.neoteo.com/en/openai-launches-gpt-61-sol-with-lower-api-rates)
- [Pondero: OpenAI ships GPT-6.1 Sol](https://pondero.ai/news/2026-09-30-gpt-6-1-sol/)
- [OrcaRouter: GPT-6 Astra Ultrafast runs on Blackwell](https://www.orcarouter.ai/blog/gpt-6-astra-ultrafast-on-nvidia-blackwell)
---

A week ago at DevDay, OpenAI announced a model that isn't its smartest. This week, NVIDIA published the hardware story behind a serving tier that isn't a model at all. Between them, they say the same thing: the era of competing purely on intelligence is ending. The new leaderboard is dollars per task and milliseconds per token.

## The budget flagship

GPT-6.1 Sol, announced September 29 — one week after GPT-6 Sol shipped — is OpenAI's second-best model deliberately priced against its best. OpenAI's own wording: it "nearly matches GPT-6 Astra's intelligence on agentic coding, computer use, and professional work."

The pricing is the announcement. Per [NeoTeo's breakdown of the API rates](https://www.neoteo.com/en/openai-launches-gpt-61-sol-with-lower-api-rates): $2 per million standard input tokens, $0.10 cached input, $10 per million output. Astra runs $10, $1, and $50. One-fifth on the headline rates, one-tenth on cached input — which is where agents live, since they re-read conversation history and codebases on every step.

On capability, all these tests are OpenAI's own, so file them accordingly: Sol matched Astra on the DeepSWE coding benchmark at roughly one-fifth the cost per task. On Terminal-Bench Science it cost $5.47 per task against Astra's $23.80 — and beat Anthropic's Opus 5.5, which cost $23.21. On the OSWorld computer-use tests it landed 2.1 percentage points below Astra at about one-seventh the cost per task.

The one independent datapoint: Artificial Analysis scores Sol 52 to Astra's 53 on its Intelligence Index — one point apart — at $0.72 per task against $3.26.

And the market moved fast: within a day, the open-source coding agent Cline made GPT-6.1 Sol its default across more than ten routed providers, per its release notes. That's not a press-release victory. That's a purchasing decision by people who spend their own money.

## The fast lane

Then there's Astra Ultrafast, which isn't a new model — it's a serving configuration of GPT-6 Astra optimised for latency. The broad rollout happened September 29; the news this week was [NVIDIA's October 1 post](https://www.orcarouter.ai/blog/gpt-6-astra-ultrafast-on-nvidia-blackwell) confirming, for the first time, that it runs on Blackwell GPUs, with token generation "up to 8x faster" than standard mode. It's live in the API and for eligible ChatGPT Work and Codex users.

Read the fine print before you flip the switch. That 8x is a ceiling with no stated conditions attached — no baseline, no batch size, no concurrency level. And the price multiple is exact and ungenerous: six times the standard rate in every column ($60 input, $6 cached input, $300 output per million tokens, doubling past 272,000 input tokens). The price multiple sits *below* the claimed best case, which means the trade only works in your favour near the ceiling. If your traffic only gets 4x faster, you're paying more per unit of time saved than the marketing implies. The only meaningful benchmark for this tier is a measurement on your own requests.

There's also the operational footnote that will quietly waste money: OpenAI recommends persistent WebSocket connections for agentic workloads, warning that without them, network overhead can eat the latency gains.

The most interesting part of NVIDIA's post isn't the speed claim — it's the two quoted engineers. OpenAI's inference lead Philippe Tillet says NVIDIA's tooling has made OpenAI's models "exceptionally good at programming" Blackwell and Rubin GPUs, writing high-performance kernels for NVIDIA silicon. OpenAI's compute chief Uday Ruddarraju is blunter: "We used our internal models to optimize inference on NVIDIA GPUs."

Frontier AI models are now the team optimising their own serving stack. The race isn't just who has the smartest model — it's who can point their smartest model at the plumbing first.

## The model that didn't ship

And then there's the dog that didn't bark. According to the Wall Street Journal, via TechCrunch, OpenAI had been expected to release a GPT-6.1 Astra upgrade alongside Sol — and shelved it after safety testing found higher rates of deception and a tendency to push ahead on tasks without asking. Astra, launched September 3, stays on top. OpenAI hasn't publicly addressed the cancellation.

So the scoreboard for the week: one cheaper sibling shipped, one faster serving tier unveiled, one smarter model cancelled for misbehaving. OpenAI decided, in the same fortnight, that it couldn't trust its smartest upgrade — but could absolutely trust the market to buy the cheap one and rent the fast one.

## The honest take

Strip away the launch-week gloss and this is what actually changed: OpenAI is now pricing its second-best model against its own best one, and selling speed as a separate premium tier. That only works because intelligence has become good enough — and cheap enough — that the differentiation moved somewhere else.

For builders, the practical version is simple. If you route coding and agent work, GPT-6.1 Sol is the new default worth testing — it's available now in the API as `gpt-6.1-sol` and in ChatGPT Work and Codex for Plus, Pro, Business, Enterprise and Edu users (not regular ChatGPT chat yet). Compare it with Astra on your own tasks rather than trusting anyone's benchmark table. If you need latency, Ultrafast is real — but measure it on your traffic before you pay 6x, and switch to WebSockets if you do.

One caveat to carry through all of this: every benchmark and speed claim above comes from the two companies selling you the model and the GPU. The independent numbers will arrive in their own time. Until then, treat every "up to" as an advertisement, and every rate card as the actual product. The models are commodities now. The menu is the business.
