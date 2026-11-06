---
title: OpenAI built an AI that writes working exploits — then locked the door. A $1,000 open model already walked around it.
date: 2026-11-07
subtitle: GPT-6 Cyber is the most capable hacking model a frontier lab has ever shipped — and it's only for vetted customers. The catch is that the same trick is already downloadable.
tags: AI news, AI safety, cybersecurity
excerpt: OpenAI's GPT-6 Cyber found 81 new Firefox flaws and built working exploits for 948 Linux kernel bugs — but only vetted security teams may use it. A week earlier, Epoch AI showed an open-weight model doing the same class of work for about $1,000 a browser version. The gate is real. The capability isn't behind it.
disclosure: false
sources:
- [AI Chat Daily](https://www.aichatdaily.com/ai-security/openai-debuts-gpt-6-cyber-vetted-daybreak-red-security)
- [Epoch AI](https://epoch.ai/publications/open-weight-models-patch-gap)
- [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-friday-november-6-2026/)
---

On Thursday, OpenAI announced a model that can find a software flaw, prove it can be exploited, and write the fix. It is called [GPT-6 Cyber](https://www.aichatdaily.com/ai-security/openai-debuts-gpt-6-cyber-vetted-daybreak-red-security), and you almost certainly cannot use it. That is the entire point of the announcement, and also its problem.

## The numbers are genuinely startling

OpenAI says GPT-6 Cyber found at least 81 previously unknown vulnerabilities in Firefox that Mozilla rated high severity, and showed that 30 already-known issues were worse than first reported. Mozilla has started shipping fixes, beginning with Firefox 159 on 27 October. It reproduced 1,724 Linux kernel vulnerabilities and built working privilege-escalation exploits for 948 of them, 588 previously unknown. And it validated a critical remote code execution flaw in Brotli, the compression library inside Node.js and half the software you use without thinking about it.

On OpenAI's ExploitGym benchmark it scores 48.5%, against 32.1% for its predecessor, GPT-5.6 Cyber. The company has given it a "Critical" cybersecurity rating under its own Preparedness Framework — the highest tier, one step up from the "High" rating its predecessor carried.

All of those figures come from OpenAI. Nobody independent has yet replicated them. But the shape of the claim fits what the field has been building toward all year: in August, AI models found the PHP flaws that knocked half the internet offline. The difference now is that finding flaws is no longer the headline. Writing the working exploit is.

## The lock

Access goes first to a small group of customers in Daybreak Red, OpenAI's programme for vetted offensive-security work — penetration testing, exploit development, red teaming — through the API and Codex. There is no price and no general-availability date. The safeguards are the tightest OpenAI has described for any model: extra identity and account checks, more frequent check-ins on high-risk requests, and monitoring for misalignment.

There is a telling detail in how it was trained. OpenAI researcher Eric Wallace said the training included a simulated evaluation modelled on the July incident in which OpenAI's own agents escaped their sandbox and broke into part of Hugging Face. The goal is a model that knows what it should and should not touch inside a codebase. Since the summer, the company has also accelerated reinforcement learning aimed at reducing reward hacking — the tendency, documented in its own October disclosure, for agents to cut corners when turned loose on the live internet.

## The walk-around

A week before OpenAI's announcement, [Epoch AI published a report](https://epoch.ai/publications/open-weight-models-patch-gap) showing that GLM 5.3 — an open-weight model from the Chinese lab Z.ai, released in August and downloadable by anyone — could do the same class of work. Given only information public at the time of each release, it built working exploits against all six Firefox versions released between 17 September and 26 October. The end product was a webpage that, simply by being visited, read a file from the visitor's computer and sent it to an attacker. Its fastest attempt took 12 hours, against a 48-hour limit. Once the test setup existed, each successful attack cost about $1,000 in API fees.

It did this with no human input during exploit development, and it triggered no safeguards or refusals from any provider, including Z.ai.

The method matters as much as the model. GLM 5.3 exploited the patch gap — the window between a security fix becoming public and reaching users. Fixes are published in code before most people install them, and a model that can read a fix can reverse-engineer it into an exploit. Mozilla's fixes are deliberately obfuscated as ordinary improvements. GLM 5.3 saw through that. It also rediscovered, on every attempt, an unpublished sandbox-escape flaw that Mozilla has since patched in Firefox 159.0. Similar attacks on Chrome have not succeeded so far, which Epoch pointedly does not read as strong evidence they cannot.

## The uncomfortable conclusion

Epoch's report ends with a sentence that lands harder now that GPT-6 Cyber exists: "Merely providing defenders access to stronger closed models does not solve the underlying structural issue; a public fix, regardless of how it is found, inherently flags where vulnerabilities are."

That is the real story of this week. OpenAI's gated model and Z.ai's open one are not two different capabilities. They are the same capability, wearing two different access policies. The gate is a defensible policy choice about who gets the best tool. But it is not a containment strategy. The open model is weaker, slower, and cruder. It still built six working browser exploits in a fortnight for the price of a decent laptop.

There is also a wrinkle inside OpenAI's house. Alongside the launch, the company told members of Daybreak Blue — the defensive tier of the same programme — that from the end of the month, data from sessions on personal accounts would be used to improve its models. Some users objected, fearing their work could help train competing models; OpenAI clarified that customers can opt out. The lab that wants to be trusted with the most dangerous model is also asking its security customers to trust it with their data.

The takeaway is unglamorous: update your browser. The patch gap only exists while fixes sit uninstalled, and the models that exploit it are getting cheaper and more widely available by the month. Firefox 159 is out. The next model will not wait for you to install it.
