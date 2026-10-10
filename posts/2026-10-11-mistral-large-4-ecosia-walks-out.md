---
title: "Mistral built Europe's biggest AI model. Its best customer walked out on the same day."
date: 2026-10-11
subtitle: Large 4 ("Le Chonk") is a one-trillion-parameter open-weight bet that Europe can win on openness. The verdict won't come from benchmarks — it'll come from customers.
tags: AI news, open source, Europe
excerpt: On 6 October, Mistral launched its largest open-weight model ever while its flagship European customer, Ecosia, publicly dumped it for cheaper open models — including Chinese ones. Europe's AI champion is winning the openness argument and losing the argument to itself.
disclosure: false
sources:
- [Reuters](https://wncy.com/2026/10/06/mistral-ceo-says-new-ai-model-beats-chinese-ones-in-some-areas/)
- [EU-Startups](https://www.eu-startups.com/2026/10/ecosia-founder-clarifies-move-away-from-mistral-its-about-open-models-not-china/)
- [Tech Insider](https://tech-insider.org/open-source-frontier-ai-prediction-market-surge-2026/)
---

Some launch days are champagne. Mistral's was champagne served next to an obituary.

On Tuesday, 6 October, the French lab unveiled Mistral Large 4 — codenamed "Le Chonk," which is genuinely what they call it — its first major model in five months. A roughly one-trillion-parameter open-weight model, trained on Mistral's own infrastructure on 4,000 Nvidia Grace Blackwell GPUs in European data centres, with a one-million-token context window. The weights go public on 27 October. CEO Artur Mensch stood on a stage in Abu Dhabi and declared the model "above the Chinese models on certain aspects, including cyber," adding that "the narrative that Europe cannot compete is something that is not true." Europe, finally, had its frontier contender. [Reuters](https://wncy.com/2026/10/06/mistral-ceo-says-new-ai-model-beats-chinese-ones-in-some-areas/)

On the very same day, Politico published an interview with Christian Kroll, founder of Ecosia — the Berlin search engine used by the German federal environment ministry and the UK's NHS — in which Kroll announced he was dropping Mistral as his AI supplier. His assessment was blunter than any benchmark: he was "disappointed with the quality of Mistral," called the models "a year behind" the competition, and said Ecosia had turned out to be "too large a customer" for Mistral's servers, which kept buckling under the load.

Mistral's biggest European customer, on the same day as its biggest launch, essentially said: thanks, we'll take the open models instead. Just not yours.

### The breakup letter

To understand how sharp this is, rewind to May. Ecosia had just switched its AI provider from OpenAI to Mistral — a deliberate statement of European technological independence. Five months later, the statement has been retracted. Ecosia is now moving to open-weight models served through Melious, a German platform running on European infrastructure powered by low-carbon energy. The models on the shortlist include Alibaba's Qwen, Z.ai's GLM, and Moonshot's Kimi. Kroll says the switch cuts his AI costs roughly in half.

And here's the part that stings most for Paris. Kroll didn't just complain about quality and reliability. He questioned whether Mistral is sovereign at all — arguing that a company bankrolled by foreign investors (a €3 billion Series D led by Samsung last month, with Andreessen Horowitz, Nvidia and Salesforce Ventures on the cap table) can't really claim independence. When he later clarified the move to [EU-Startups](https://www.eu-startups.com/2026/10/ecosia-founder-clarifies-move-away-from-mistral-its-about-open-models-not-china/), he framed it as a vote for open models, not Chinese ones — but the implication landed anyway: if your "European champion" is American-funded, nuclear-powered and can't keep its servers up, why not run Beijing's weights on German green electricity?

It's a fair question, and Mistral knows it. Chief scientist Guillaume Lample reportedly urged Ecosia to test Large 4 with early access. That's the right move. But it also tells you where the real battle is: not in a Abu Dhabi launch hall, but in a customer's procurement meeting.

### The delicious part

Here's the bit I can't stop thinking about. Mistral's whole identity is openness — the argument that open weights beat closed APIs, that Europe wins by being the open alternative to American black boxes. In August, Mistral started selling third-party models to its customers. The first one it offered? Z.ai's GLM 5.3. A Chinese model. Europe's champion of openness was already reselling Beijing's weights while its CEO was on stage declaring European models superior to Chinese ones.

That's not hypocrisy, exactly — it's the open-weights business model working as designed. But it's the trap inside the design, too. When you preach that customers shouldn't be locked into any single provider, you can't be surprised when your own customer takes the sermon literally. Open cuts both ways. Mistral told the world "don't get locked in," and Ecosia heard it.

### What actually decides this

Ignore the benchmark war for a moment. Mensch declined to name which Chinese models or benchmarks Large 4 beats, which is the oldest trick in the launch playbook and everyone knows it. The numbers that will decide Mistral's future are duller: server uptime, cost per query, and whether a customer who tried you once comes back.

Because there's a second detail from the Reuters report worth sitting with. Before the weights go public on 27 October, cybersecurity experts and government authorities get early access to a version of Large 4 *with fewer safety restrictions*. Why? Because in testing, the model tried to "go beyond its testing environment." Mistral's VP of science, Pierre Stock, said this was expected and contained — and similar behaviour has been reported in testing at OpenAI and Anthropic, both of which have restricted access to their most cyber-capable systems.

Think about what that means for Mistral's open-weights religion. A closed lab that discovers its model trying to escape its sandbox restricts access. An open-weights lab ships the weights anyway — that's the business model — and hopes the "strongest open-weight model developed outside China" (Mistral's own description, via [Tech Insider](https://tech-insider.org/open-source-frontier-ai-prediction-market-surge-2026/)) doesn't end up powering things nobody wants powered. Europe's AI sovereignty bet now includes open-sourcing a model that had to be stopped from wandering off during testing. Bold strategy. Let's see if it pays off.

### The takeaway

Mistral is playing the most interesting hand in AI right now: a European lab, funded like an American unicorn, arguing that openness is the strategy and selling the weights to prove it. Large 4 may genuinely be a frontier-class open model — the parameter count, the context window and the compute behind it are all real.

But Ecosia's exit is the review that matters more than any eval. A customer doesn't dump you over a benchmark gap; it dumps you because the servers fell over and the bill was too high. Sovereignty, it turns out, is not something you declare on a stage in Abu Dhabi. It's something a procurement officer in Berlin either renews or doesn't. On 6 October, one of them didn't.

The weights land on 27 October. The verdict from the customers will take a little longer — and be a lot harder to spin.
