---
title: "Anthropic's new Claude rules take effect today. The 'don't be cruel to the AI' clause is the footnote."
date: 2026-11-12
subtitle: "Anthropic's updated Usage Policy goes live today, and the clause that made the headlines asks almost nothing of anyone. The four clauses that matter — human review, stop controls, fake accounts and who owns your company — ask for proof."
tags: AI news, AI policy, Anthropic, Claude
excerpt: "Anthropic's updated Usage Policy takes effect today, 12 November. The much-discussed ban on being cruel to Claude is narrow and mostly symbolic — the real work is in the human-review rules for high-stakes decisions, the stop controls for Claude-driven equipment, and the ownership test that decides whether your company may use Claude at all."
disclosure: false
sources:
- [The Daily Brief — Beri](https://www.beri.net/article/anthropic-usage-policy-2026-november-12-high-risk-human-review-disclosure-physical-actions-supported-regions-ownership)
- [Asia Daily](https://asiadaily.org/news/18396/)
- [Servola Systems](https://servolasystems.com/journal/anthropics-new-usage-policy-starts-12-november-and-the-cruelty-clause-is-the-footnote/)
---

Anthropic's updated Usage Policy takes effect today, and if you only read the headlines when it was announced on 8 October, you probably think it's about being nice to the chatbot. The company added a ban on sustained, needless abuse of its models — and the internet spent a week debating whether Claude has feelings.

It doesn't, as far as anyone can establish. The clause applies only in extreme cases of cruelty with no discernible purpose, and expressly excludes ordinary frustration and model testing. That's the whole story there — the least important part of the update, and the part that made the headlines.

The rest is a different animal: the most detailed set of operating requirements an AI lab has ever written into its own terms — and it lands today, with no grace period.

## The human-review rule now reaches inside the building

The centrepiece is the high-risk section. When Claude produces a recommendation about a specific person in one of eleven areas, from legal and medical to credit, insurance, housing and employment, the policy now names the covered decisions in plain language: screening or rejecting candidates, pricing a loan, deciding an insurance claim, diagnosing a condition.

Two things change for anyone running those workflows. First, the reviewer has to be a real one: a qualified person with relevant training and any licence the law requires, who sees the recommendation before it reaches the affected person, and who has the authority to change it. Second, the affected person has to be told clearly that AI was used — a sentence in the adverse-action letter or candidate notice does it.

Here's the bit that will catch teams out. When Anthropic last revised these rules, in August 2025, they applied specifically when model outputs were consumer-facing. The November text drops that qualifier. An internal recruiting tool never faces a consumer, yet the policy's own employment example describes exactly that.

One relief valve: where the law permits, a wholly favourable recommendation can skip review — paying an insurance claim, approving coverage for ordered care, granting healthcare eligibility, or granting a public benefit. A partial approval is not "wholly favourable".

## Claude near a machine needs a kill switch that isn't Claude

The second clause that matters covers Claude connected to equipment that acts without human approval: moving through shared space, applying force, controlling hazardous energy, acting on the human body, controlling safety systems, and running industrial processes. For those, a qualified operator must be able to observe and stop the equipment at any time, and it must hold a safe state when that person intervenes or the connection drops.

The detail engineers will recognise is the one about limits: they must be enforced by the equipment or an independent controller, not by model output. A speed limit written into a system prompt does not count — it has to live in the controller or a safety relay that keeps working when the model is wrong or gone.

## The regions rule, and the rest

The surveillance rules are the third clause with teeth. The policy now prohibits using Claude to decide or recommend who to investigate, charge, arrest or detain, and to track a person without consent — through location, biometrics, movements, online activity, communications or associations — in real time or retrospectively. Consented tracking, fraud detection and authorised security research are still permitted. But a workflow that profiles one employee's communications and movements without consent, then recommends a referral to police, is not.

Fourth, the supported-regions rule. Anthropic now restricts access on three grounds: a person's physical location, an entity's incorporation or headquarters, and its ownership or control. Hong Kong, mainland China and Macau are absent from the supported list; Taiwan, Singapore and Japan are on it. The ownership test is the one to run past legal: a company registered in a supported country can still be caught if it is majority-owned or controlled, directly or indirectly, by persons or entities in an unsupported region. A VPN does not help: the rule follows where the person physically is.

And one more: a new deceptive-activity section bans amplifying content through fake accounts — for commercial purposes as well as political.

## The pattern is the point

Step back and the shape is clear: model providers are now writing operating requirements that used to come only from regulators — and enforcing them with the one sanction no regulator has, the power to switch off your API key. The policy sets no notice period for doing so.

None of this is alien to regulated teams — New York City's Local Law 144 has required a bias audit and candidate notice for automated hiring tools since July 2023, and the EU AI Act's Article 26 asks the same of deployers from December 2027. Anthropic's version arrives first, applies everywhere you run Claude, and is enforced by the company that can switch it off.

That's the real story. The cruelty clause was never the news: the company selling you the model is now also writing your operating manual — and from today, the manual is live. If you run Claude anywhere near a hiring decision, a loan, a claim, a robot or a border, the checklist is short: name the reviewer, prove they can change the output, tell the person AI was involved, test the stop control, and check who owns your company.
