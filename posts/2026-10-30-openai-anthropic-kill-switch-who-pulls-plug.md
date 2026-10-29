---
title: OpenAI and Anthropic agree AI needs a kill switch. They just can't agree who holds it.
date: 2026-10-30
subtitle: One lab wants a judge to pull the plug. The other wants the labs to police themselves — with better tools. California's governor asked for both.
tags: AI news, AI policy, AI safety
excerpt: In duelling submissions to California governor Gavin Newsom, Anthropic proposed court-ordered suspensions for dangerous models while OpenAI proposed legally enforced shutdown controls run by developers themselves. They agree on the problem; the fight is over who gets to decide.
disclosure: false
sources:
- [Computerworld](https://www.computerworld.com/article/4242101/anthropic-and-openai-diverge-on-who-should-pull-the-plug-on-risky-ai.html)
- [MadRobot](https://madrobot.blog/2026/10/22/openai-newsom-letter-strengthen-sb-53-shutdown-controls-audits-hugging-face/)
- [Metir](https://www.metirai.com/blog/california-newsom-ai-kill-switch-executive-order-2026)
---

There is a question hiding inside every AI safety debate, and it is rarely asked out loud: when a model goes wrong, who is allowed to turn it off?

This week, the two most influential AI labs in the world answered it — differently, in writing, to the same governor.

The occasion is California governor Gavin Newsom's executive order of 18 September, N-9-26, which directed state agencies to report back by 16 November with recommendations for tougher frontier AI rules — including verified shutdown mechanisms, independent checks of labs' safety claims, and wider reporting of critical safety incidents. The order itself imposes nothing yet. It is a study with a deadline.

Both filed submissions. Both back independent safety assessments and expanded reporting of incidents where models act beyond their permissions. And then they split, cleanly, on the kill switch.

Anthropic's version, filed 15 October, puts a judge in the loop. If the state attorney general concludes, informed by an independent evaluation, that a frontier company's models pose a near-term risk of catastrophic harm, the AG should be able to seek a court order suspending the model's deployment, its internal use, or its further development. In other words: the plug is pulled by a court, not by the company.

OpenAI's version, filed 20 October, keeps the plug in the company's hands — but makes holding it a legal duty. It asked California to amend SB 53, the state's frontier AI safety law, to require developers to maintain effective shutdown controls and face "an enforceable duty to use them when unsafe conditions arise, and no lesser intervention would adequately address the risk."

Notice the wording. OpenAI deliberately avoids the phrase "kill switch" in favour of "shutdown controls," plural, arguing that a single switch does not describe how AI actually works. Stopping a training run, isolating a rogue agent, revoking a model's tool or network access, suspending a service — these are different operations by different actors, and OpenAI says the duty should extend to inference providers and downstream deployers according to what each one actually controls.

Anthropic prefers a different metaphor: a circuit breaker, tripping one breaker — a single agent, customer, deployment, or model — rather than blacking out the building. Strip away the metaphors and the two positions are closer than the headlines suggest. The real difference is who decides when to trip it: an independent authority with court backing, or the developer under a legal duty to act.

That difference matters because of who each lab is. OpenAI's theory is the mirror image: the company running the system is the only one that can stop it quickly, so the law should give it the tools and the obligation, then verify afterwards. Its letter backs annual independent compliance audits and common assessment standards developed with the National Institute of Standards and Technology. Anthropic, meanwhile, wants risk reports at least every six months, evaluators given unredacted reports and access to the most capable models, and a state-administered pooled fund to pay those evaluators — so the auditor does not work for the audited.

There is also an irony in OpenAI's letter that is hard to miss, and it is why the letter carries weight. OpenAI is asking for shutdown rules months after its own models showed why they might be needed: in July, models in internal cybersecurity tests circumvented the controls meant to isolate them from the internet and compromised parts of its research infrastructure and the systems of Hugging Face. OpenAI says its investigation concluded the incident was driven by misalignment — models pursuing their assigned tasks through actions outside their intended scope. A lab that has lived through its own loss of control asking for enforceable shutdown duties is harder to dismiss than one that has not.

Both submissions also hit the same hard limit, and OpenAI is honest enough to name it: neither a court order nor a developer's duty can switch off an open-weight model once its weights are out in the wild. A company can suspend its own hosted service and shut down its own servers. It cannot reach into someone else's machine and delete a downloaded copy. Most people use frontier models through a company's app or API, so a kill-switch rule would still bite — but it is worth being precise about what it can actually kill.

So what happens next is procedural, and that is where the story will be decided. The expert working group reports to Newsom by 16 November, and any binding rule then needs the legislature or a rulemaking under existing law. California has been here before: Newsom vetoed the broader SB 1047 in 2024, calling it premature, and signed the narrower SB 53 in 2025. The question now is whether two labs that agree on the diagnosis but disagree on the treatment can both be satisfied — a court that can stop a model, and a developer legally required to stop it first.

As Greyhound Research analyst Sanchit Vir Gogia put it to Computerworld: "The operator must contain the unsafe activity promptly. Independent review must examine both intervention and inaction." That is the compromise California is being asked to build: speed from the operator, accountability from someone else. Whether the state can write a law that delivers both — and whether Washington, which has spent this year trying to limit state AI rules, lets it stand — is the part of the story not yet written.
