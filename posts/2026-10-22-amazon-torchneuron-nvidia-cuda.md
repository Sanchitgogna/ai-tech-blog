---
title: Amazon says its new tool ends chip lock-in. The lock-in just moved.
date: 2026-10-22
subtitle: TorchNeuron lets PyTorch code run on Trainium chips with a one-line change. The fine print is where the real story lives.
tags: AI news, AI chips, cloud, explainer
excerpt: AWS released TorchNeuron, open-source software that moves PyTorch code to its Trainium chips with one changed line — a direct shot at NVIDIA's CUDA moat. The code moves easily. Getting the speed is the expensive part.
disclosure: false
sources:
- [PyTorch Foundation — Introducing TorchNeuron](https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/)
- [Nexairi — Amazon Says Its New Tool Ends Chip Lock-In. Here's What's Left.](https://nexairi.com/the-take/amazon-torchneuron-trainium-lock-in-claim-what-moves/)
- [Pondero — AWS ships TorchNeuron](https://pondero.ai/news/2026-10-20-aws-torchneuron-trainium-pytorch/)
---

On Monday October 19, Amazon launched its most direct attack yet on NVIDIA's empire. Not a faster chip. A piece of software.

It's called TorchNeuron, and the pitch fits in a single line of code. You take the PyTorch program you already wrote — the one that currently expects NVIDIA hardware — and you change `.to('cuda')` to `.to('neuron')`. That's the migration. AWS opened the public beta on October 20 at the PyTorch Conference in San Jose, and the whole thing ships under the Apache 2.0 open-source license, so nobody has to take Amazon's word for how it works.

## Why Amazon went after the software, not the silicon

Here's the thing everyone in AI already knows but nobody likes saying out loud: NVIDIA's moat was never really the chips. Rival chips have been competitive on raw speed for years. The moat is CUDA — the software stack that every AI developer's code is already written against. Amazon's own announcement puts a number on it: roughly 85% of AI researchers and developers write their code in PyTorch.

So Amazon did the obvious, clever thing. Instead of asking developers to learn a new toolchain, it made Trainium2 and Trainium3 chips look like a native PyTorch device. It plugs into PrivateUse1, PyTorch's official extension point for third-party hardware, which means all the tooling developers already use — the debuggers, the profilers, distributed training, `torch.compile` — works on Trainium as written. Amazon even contributed code back to the PyTorch project to remove hard-coded CUDA assumptions, which is a genuinely neighbourly thing to do while declaring war.

And it's not just a science experiment anymore. Voice-AI company Cartesia has already moved its inference pipeline to Trainium with minimal changes, per Amazon's announcement. The Lieber Institute for Brain Development is running drug-discovery and molecular-dynamics models on the chips. Deepgram says Trainium handles about 60% more audio per dollar than its GPU baselines. More than 30 early adopters are in the pipeline across robotics, voice AI, and world modelling. Wall Street noticed: Amazon shares jumped as much as 5% intraday on the announcement.

Colin Brace, the VP of software at Annapurna Labs (Amazon's chip division), told TechCrunch the thesis plainly: "The real story is removing the lock-in that kept developers from having a real choice at all."

## The one line that works, and the hundred lines it took to make it fast

Now for the part Amazon put in smaller print.

Cartesia got its code running with minimal changes. Then it did the real work: writing custom kernels — the low-level programs that actually run on the chip — in NKI, Amazon's kernel language that only runs on Trainium. That's where the performance lives. The voice synthesis layers that run thousands of times a second and set the product's response time? Hand-tuned, chip-specific kernels.

Deepgram's "60% more audio per dollar" figure came after a multi-month port done with help from AWS's own Generative AI Innovation Center. That is not a one-line migration. That is a consulting engagement.

And the first release has honest gaps: no dynamic shapes (inputs that change size require recompiling), some operations have no Trainium version at all, and FP8 and TorchAO support are still in private beta. Amazon says all of this plainly in the docs, to be fair. But it changes the shape of the offer.

## Lock-in, relocated

So where does that leave the big claim? TorchNeuron genuinely removes the first, steepest barrier: getting your code to run at all. That's real. For years the argument against trying non-NVIDIA chips was "it'll take six months just to get our pipeline compiling." That argument just died.

But the lock-in didn't die with it. It moved. Your model code is now portable; your performance is in kernels that only run on Trainium, written in a language that only Amazon's chips speak. Porting to Google's TPUs — which, in a beautiful piece of timing, got their own version of this on October 21 with [TorchTPU](https://nexairi.com/the-take/amazon-torchneuron-trainium-lock-in-claim-what-moves/) — would mean writing those kernels again.

This is how the chip wars actually play out. Nobody wins by building a better chip alone; they win by making their chip the cheapest place to run the code everyone already has, and then making the *fast* version of that code subtly unportable. Amazon just played its best hand yet. NVIDIA will notice. Google clearly already did.

The takeaway for anyone running models at scale: the one-line migration is real, and you should probably test it — Trainium pricing is aggressive for a reason. But before you sign anything, ask AWS which of your workloads need hand-tuned NKI kernels, who's writing them, and what it costs to move back. Get that number in writing, next to the cost of moving in. That's the only lock-in calculation that matters.
