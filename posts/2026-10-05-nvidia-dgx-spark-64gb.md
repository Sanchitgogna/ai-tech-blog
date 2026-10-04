---
title: NVIDIA's $5,000 AI box is the "cheap" one — and that's the whole story
date: 2026-10-05
subtitle: The new 64GB DGX Spark costs a thousand dollars more than the original 128GB model did. Blame the chips' chips.
tags: AI news, gear
excerpt: NVIDIA launched a cheaper DGX Spark for local AI at $4,999 — more than the 128GB original's $3,999 debut. The pricing tells you everything about where AI hardware stands in late 2026: memory is the bottleneck, and local AI has a price tag to prove it.
disclosure: false
sources:
- [NeoTeo: 64GB DGX Spark — NVIDIA's $4,999 starting price](https://www.neoteo.com/en/nvidia-announced-a-64gb-dgx-spark-with-a-4999-starting-price)
- [AI Weekly: Nvidia launches 64GB DGX Spark at $4,999 as 128GB hits $6,950](https://aiweekly.co/alerts/nvidia-launches-64gb-dgx-spark-at-4999-as-128gb-hits-6950)
---

NVIDIA announced a new computer last week that you have never been closer to being able to afford — and that's not entirely a joke.

On October 2, NVIDIA introduced a 64GB version of the [DGX Spark](https://www.neoteo.com/en/nvidia-announced-a-64gb-dgx-spark-with-a-4999-starting-price), its compact AI computer for running models locally. Same GB10 Grace Blackwell Superchip, same DGX OS, same software stack — but half the unified memory of the original 128GB model, starting at $4,999. It goes on sale October 23 through Acer, ASUS, Dell, Gigabyte, HP and MSI.

And here is the part that makes you do a double take: the original 128GB DGX Spark debuted at $3,999. NVIDIA's new "cheaper" box costs a grand more than the old one ever did at launch. Something has gone sideways in the memory market, and NVIDIA isn't even pretending otherwise.

## The arithmetic is a comedy

NVIDIA says one 64GB Spark can run models with up to 100 billion parameters entirely on the device. Two linked together — a direct QSFP cable between their ConnectX-7 ports, configured by NVIDIA's Sync Cluster Assistant — pool their memory to 128GB and reach models up to 200 billion parameters. In NVIDIA's own test, a clustered pair beat a single 128GB box by up to 1.7x on the Qwen3.8 27B model. (Worth noting, as [NeoTeo](https://www.neoteo.com/en/nvidia-announced-a-64gb-dgx-spark-with-a-4999-starting-price) points out, that this is one test on one model, not a general guarantee.)

Two 64GB boxes at $4,999 each: roughly $10,000 for 128GB of pooled memory. One 128GB Spark: $6,950. You pay forty percent more for the same memory pool — though you do get double the compute and bandwidth for your trouble. It's the kind of pricing spreadsheet that only makes sense if you stop thinking of it as buying computers and start thinking of it as buying memory with a computer attached. That's exactly what it is.

Meanwhile the 128GB model itself has been on its own adventure: $3,999 at debut, up 18% to $4,699 back in February, and now listed at $6,950. NVIDIA cites memory supply constraints. Micron has warned DRAM supply stays tight through 2028. If you were waiting for local AI hardware to get cheaper with time, the 2026 memory market has other plans.

## Why people want this box anyway

Prices aside, the DGX Spark exists because of a real shift: developers and researchers increasingly want to run serious models on their own hardware instead of renting GPU time from a cloud provider. The pitch is straightforward — privacy (your data never leaves your desk), no per-token API bills, and availability that doesn't depend on anyone's datacenter queue. A 64GB unified pool, shared between CPU and GPU, handles inference, fine-tuning and agentic workflows locally, and it ships with NVIDIA's Agent Toolkit, CUDA-X libraries, open Nemotron models, and runtimes like Ollama, vLLM and PyTorch ready to go. [AI Weekly](https://aiweekly.co/alerts/nvidia-launches-64gb-dgx-spark-at-4999-as-128gb-hits-6950) even notes Blender is among the first major creator apps to support the platform.

This is local AI maturing past the hobbyist phase. The DGX Spark isn't a science project with a soldering iron — it's a turnkey machine with a software stack designed so a developer can be running an agent on their desk by the afternoon. NVIDIA describes the expected uses plainly: round-the-clock coding or research agents, offloading inference from everyday laptops, and scaling to a second unit when the workload outgrows one box. (That last one is doing a lot of work in NVIDIA's revenue model, but let's not be cynical before lunch.)

## The honest take

So should you buy one? The honest answer is that the DGX Spark 64GB makes sense for exactly one person: a developer who is already spending enough on cloud GPU bills or API usage that five grand pencils out as the cheaper path — and who needs their models to run behind their own firewall. For everyone else, this is still enthusiast territory, and enthusiast territory has never been more expensive. A "budget" AI workstation now costs more than a well-spec'd MacBook Pro, and the memory shortage keeping it that way is not a blip.

But zoom out and the signal is encouraging. Three years ago, running a 100-billion-parameter model outside a datacenter was a curiosity. Now NVIDIA ships a small box that does it, sells it through Dell and HP, and worries the main constraint is DRAM supply, not software readiness. Local AI isn't a fringe hobby anymore. It's a product category with a price list — and a price list that currently reads like a hostage note from the memory market.

If the DRAM supply situation normalizes, prices follow. If it doesn't, the cloud providers keep charging rent and the locals keep building. Either way, the real product this week isn't the 64GB Spark. It's the confirmation that the race to own your own AI stack is fully on — and everyone in it is now bidding against Micron.
