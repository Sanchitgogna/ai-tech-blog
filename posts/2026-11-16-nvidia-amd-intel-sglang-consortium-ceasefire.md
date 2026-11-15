---
title: "NVIDIA, AMD and Intel just joined the same club. The chip war has a ceasefire — in software."
date: 2026-11-16
subtitle: "The fiercest rivals in AI hardware are now co-owners of the same open-source serving stack. The fight moved from who makes the chip to who runs it cheapest."
tags: AI news, open source, AI chips, AI infrastructure
excerpt: "LMSYS Org launched the SGLang Consortium on 12 November, with NVIDIA, AMD, Intel, Google, Meta, Cloudflare, Modal and RadixArk as founding members. The rivals will jointly steer the open-source engine that serves AI models — because inference, not training, is now where the money goes."
disclosure: false
sources:
- [LMSYS Org](https://www.lmsys.org/blog/2026-11-12-sglang-consortium)
- [Bitcoin Versus](https://bitcoinversus.tech/2026/11/15/sglang-consortium-nvidia-amd-intel-google-open-ai-inference-november-2026/)
- [Business Wire](https://www.businesswire.com/news/home/20261112052367/en/LMSYS-Org-Launches-SGLang-Consortium-with-NVIDIA-AMD-Intel-Google-Meta-Cloudflare-Modal-and-RadixArk-to-Advance-Open-Source-AI-Inference)
---

NVIDIA, AMD and Intel spent the last three years trying to bury each other. Last Thursday, they joined the same club.

LMSYS Org [launched the SGLang Consortium](https://www.lmsys.org/blog/2026-11-12-sglang-consortium) on 12 November, in the opening keynote of the first SGLang Summit in San Francisco. The founding members are NVIDIA, AMD, Intel, Google, Meta, Cloudflare, Modal and RadixArk — eight companies that, between them, cover almost every chip, cloud and deployment platform AI runs on. Their job: jointly steer the roadmap of SGLang, the open-source engine that serves AI models to users.

This is not a charity project. It's a ceasefire with a business case.

## Inference is where the money went

Training gets the headlines. Inference pays the bills. Deloitte estimates inference will account for roughly two-thirds of all AI compute in 2026, up from about half in 2025. Every chatbot reply, every agent action, every AI-generated image is an inference job — and the software that runs those jobs decides how fast they come back and what they cost.

SGLang is that software, or at least one of the main contenders for the job. It's a full-stack inference engine, part of the PyTorch ecosystem, and LMSYS says it runs on hundreds of thousands of GPUs, powering production deployments at Meta, Microsoft, Google, Amazon, Thinking Machines Lab, Cloudflare, Reflection and Modal. Its signature trick is RadixAttention, a caching technique that reuses work from earlier requests instead of recomputing it — the kind of unglamorous optimisation that shows up directly in a cloud bill.

That's why the member list matters more than the press release. When the companies that buy the most inference capacity all agree to build on the same serving stack, the stack becomes infrastructure. And infrastructure, once shared, is very hard to take private again.

## What the consortium actually does

The governance is deliberately boring, which is the point. Each founding member names a technical representative and joins two roadmap meetings a year, contributing engineering, deployment feedback, testing resources or joint development. Working groups can collaborate between meetings, with public updates on direction and progress. LMSYS's maintainers keep final say over technical decisions and code acceptance — membership buys a seat at the table, not a veto.

The five focus areas are frontier model support, reasoning and multimodal workloads, distributed inference, and hardware optimisation. Translation: making sure the newest models run well everywhere, not just on one vendor's silicon.

There were concrete signs on day one. Intel and RadixArk announced they'll optimise SGLang for Intel CPUs, GPUs and accelerators, including support for Intel's Advanced Matrix Extensions, and upstream the work rather than keeping a vendor-only fork. And SGLang-Neuron v0.1.0, co-developed by RadixArk and AWS Annapurna Labs, entered public preview the same day, bringing the serving stack to AWS Trainium hardware through a native PyTorch plugin. The SGLang team also marked a version 1.0 milestone, citing more than 330 adopting organisations and day-zero support for 217 models.

## Why rivals would share the plumbing

Every chipmaker has the same problem: their hardware is only as good as the software that runs on it. NVIDIA learned this a decade ago with CUDA. AMD's MI450X, announced the same week Jensen Huang resigned, is a serious chip — but a serious chip with thin software support is a paperweight. Intel has been living that lesson for years.

So the logic inverts. Instead of each vendor maintaining its own serving stack and hoping developers bother, they all pour engineering into one open stack that runs well on everything. NVIDIA's Ian Buck put it plainly in the announcement: better software helps developers get more performance from NVIDIA compute, and lower inference costs make AI more accessible. AMD's Ramine Roane made the same argument from the other side: SGLang runs across hardware, including AMD Instinct GPUs.

It's the same playbook as the Linux Foundation, or the early days of Kubernetes: compete on the product, cooperate on the layer underneath. The difference is the stakes. The serving layer decides which hardware is cheap to run, and cheap-to-run hardware gets bought.

## The caveats, because there are always caveats

A consortium is a governance announcement, not a shipped feature. No new capability arrived with it. The funding each member contributes, and the engineering headcount behind the promises, hasn't been spelled out publicly. Intel's performance language is aspiration, not a benchmark — the release names no test configuration, no tokens-per-second figure, no date for a finished optimised build. And the SGLang-Neuron plugin is in public preview, not general availability.

There's also the question this blog has raised before. When Amazon launched TorchNeuron in October, the pitch was the same — one migration line, run anywhere — and the catch was that the real speed came from chip-specific kernels. Open serving stacks reduce lock-in; they don't abolish it. A model that runs everywhere still runs *best* somewhere, and that somewhere is usually whoever wrote the most optimised code for their own silicon.

Still, the direction of travel is unmistakable. The last month has seen open-weight models, open serving stacks and shared governance pile up faster than any single vendor's walled garden. The chip war isn't over. It just moved one layer up the stack — from who fabricates the silicon to who writes the software that makes it worth buying.

And on that layer, for once, everyone is on the same side.
