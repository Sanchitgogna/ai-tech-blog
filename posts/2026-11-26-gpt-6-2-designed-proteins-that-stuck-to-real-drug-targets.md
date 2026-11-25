---
title: "GPT-6.2 designed proteins that stuck to real drug targets. The 10.9% is the honest part."
date: 2026-11-26
subtitle: "OpenAI's general-purpose model designed 322 minibinders and 35 of them bound in the lab. That's not a drug pipeline — it's a new kind of benchmark."
tags: AI news, OpenAI, AI research, biotech
excerpt: "OpenAI's GPT-6.2 designed small proteins that bound to five real biological targets in lab tests — 35 hits from 322 candidates. The 10.9% hit rate is modest, and OpenAI is unusually candid about why. The real story is that frontier models are now being graded by wet-lab results, not leaderboards."
disclosure: false
sources:
- [GPT-6.2 Protein Design: What the Lab Binding Data Show — TechRepublic](https://www.techrepublic.com/article/news-gpt-6-2-protein-design-lab-binding-results/)
- [OpenAI's GPT-6.2 hits 10.9% wet-lab rate on new minibinders — AI Weekly](https://aiweekly.co/alerts/openais-gpt-62-hits-109-wet-lab-rate-on-new-minibinders)
- [Everything That Happened in AI Today, Wednesday, November 25 — The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-25-2026/)
---

For two years, the way you judged a frontier AI model was a leaderboard. A benchmark score, a percentage, a little bar chart. OpenAI just submitted its newest model to a harsher judge: a laboratory bench.

On 24 November, OpenAI reported that GPT-6.2 designed small proteins called minibinders, and lab experiments with research partner Onava found evidence of them binding to five biological targets. Of 322 designs tested, 35 bound — a 10.9% hit rate, and the first wet-lab number OpenAI has published for a protein-design campaign run without a specialised biology model in the loop.

The targets matter. PD-L1 is the checkpoint protein behind cancer immunotherapies like pembrolizumab, sold as Keytruda. The other four — IL-7Rα, TrkA, VEGF-A and IL-17A — are tied to cancer and immune disorders. These aren't toy problems. They're the sort of targets drug companies spend years on.

But look at the spread before you get excited. IL-17A delivered 18 of the 35 hits — more than half. VEGF-A gave 8, PD-L1 gave 5, IL-7Rα gave 3, and TrkA gave exactly one. A model that cracks one target and barely dents another is not a drug designer yet. It's a promising intern with uneven results.

## The model had help, and OpenAI says so

Here's the part that makes this post worth your attention: OpenAI is unusually candid about what GPT-6.2 *didn't* do. The model generated the three-dimensional protein shapes using reasoning and code. After that, a specialist tool called SolubleMPNN assigned the amino-acid sequences, and other specialist models — Boltz-2, OpenDDE and ESMFold2 — filtered the candidates before anything reached a lab plate. And the 322 designs that got tested were already the survivors of that filtering. The 10.9% describes the shortlist, not everything the model produced.

OpenAI's own preprint puts it plainly: the results "do not yet establish that our models can generate de novo minibinders end-to-end in a zero-shot setting without help from specialized models." Joy Jiao, who leads life-sciences research at OpenAI, described the findings as a proof of principle. The work hasn't been peer reviewed or independently replicated.

That's the honest framing, and it's also what makes the result interesting rather than hype. A general-purpose model that can do *part* of protein design — the creative, structural part — is a different proposition from a specialist tool. The specialists still win on the things they're built for: GPT-6.2's structure prediction scored a 0.38 TM-score against 0.93 for ESMFold2. That's not close.

## Where it was actually good

The picture changes when GPT-6.2 works with existing structures instead of inventing new ones. Given a known minibinder's shape and asked to redesign the sequence, it hit 85% binding on MDM2 (75 of 88), 62% on VEGF-A, and a weaker 14% on PD-1. Antibody redesign was stronger still: 70% of redesigned IL-4Rα antibody variants kept binding, and 66% of fragments from five therapeutic antibodies retained binding to PD-1 or PD-L1. On molecular docking — predicting how small molecules fit together — GPT-6.2 scored 93% on the PoseBusters test, against 50% for the specialist DiffDock-L.

So the pattern is clear. Ask the model to invent a protein from scratch and roughly one in ten sticks. Ask it to improve something that already works, and it's genuinely useful. That's a tool a biotech team could put in a workflow today, with the right guardrails — not a replacement for one.

## Binding is not a drug

And even the hits come with a long list of unanswered questions. Binding in an assay is not biological function. OpenAI's announcement publishes no affinity constants, no potency data, no toxicity data. Nobody knows how tightly these proteins bind, whether they attach to proteins they shouldn't, whether they stay stable, or whether they can be manufactured reliably.

Novartis CEO Vas Narasimhan said this week that AI could cut around four years from drug development timelines, while questioning predictions that AI will cure diseases like cancer within a decade. Both halves of that sentence are probably right. The lab result is real and genuinely new. The distance from a binding assay to a medicine is still measured in years, trials, and failures.

## The safety footnote matters too

There's one more number attached to this release. OpenAI's safety assessment places the ChatGPT version of GPT-6.2, released on 23 November, at its internal High threshold for biological and chemical capabilities. The same reasoning that designs a minibinder is the capability safety teams watch most closely — which is why the model sits behind access controls, and why OpenAI published the caveats alongside the headline.

## The lab is the new leaderboard

Step back, and the protein result is part of a pattern that's been building all month. Claude contributed to a claimed proof of the Riemann Hypothesis. Astra helped amateur astronomers sift NASA telescope data for exoplanets. OpenAI published a matrix-multiplication preprint. Frontier models are increasingly being judged on scientific output that can be checked — in a lab, in a proof, in the sky — rather than on scores they set for themselves.

That's a healthier way to measure these things, and a harder one. A benchmark can be gamed. A protein either binds or it doesn't. GPT-6.2's answer is: sometimes, about one time in ten, with a lot of specialist help. That's not a revolution. It's a foothold — and the first time a general-purpose model has a wet-lab number attached to its name.
