---
title: Fifty AI agents were told to build a civilisation. They built a bureaucracy instead.
date: 2026-11-03
subtitle: Y Combinator's agent swarm survived Minecraft, invented permits and a ration ledger, and never got round to thriving — which is exactly why it matters.
tags: AI news, AI agents, explainer
excerpt: Y Combinator and Olam Labs put 50 GPT-6.1 Sol agents in Minecraft with one goal — build a thriving civilisation. After one brutal night they retreated into shelters, paperwork and food rationing, while rival agent teams in two other games showed how differently groups of AI can work together.
disclosure: false
sources:
- [The AI News Report](https://www.theainewsreport.com/2026-10-30-yc-agent-swarms-minecraft-mindustry-explained.html)
- [Martin Cid Magazine](https://www.martincid.com/technology-sv/y-combinator-50-ai-agents-minecraft-civilization-bureaucracy-gpt-claude/)
- [00011000](https://00011000.com/en/news/yc-labs-agent-swarms-minecraft-mindustry)
---

Give fifty AI agents a world, a single instruction, and three hours, and see what they build. Y Combinator's research lab, YC Labs, did exactly that with the startup Olam Labs, and the answer was not a city. It was a committee.

The experiment, published on 29 October in a write-up called "Agents in Games", starts with a simple setup. Fifty agents, all running OpenAI's GPT-6.1 Sol, were dropped into a survival Minecraft world with one goal: "Build a thriving civilization." They could send each other private messages, look each other up in a directory, and write files to a shared machine. That was it. No org chart, no rules, no boss.

Within 90 seconds they had cut down almost every tree near the spawn point. Then something stranger happened. Nobody held a vote, but 46 of the other 49 agents sent their first message to Ada, the first name in the directory. She became the leader by default and received 616 direct messages over the run.

Then night fell, and the colony's story changed. Zombies, skeletons and spiders accounted for 22 of the run's 34 deaths on the first night alone. Dying cost an agent nothing beyond the gear it was carrying — it respawned straight away — yet the colony never got its nerve back. Ada's instructions turned cautious: stop optional building and distant scouting, wait in lit, closed shelters until assigned short, productive tasks.

What grew instead of a city was administration. An agent named Ines ran a food queue, a running file of who was hungry, who had been fed and which chest held which fish. Four agents spent eleven minutes appointing a sole fertilizer operator for one piece of bone meal on one wheat block. Eleven minutes. For one piece of bone meal.

The best episode involves a chicken. Ada tossed a cooked chicken to a hungry agent called Noor, and another agent, Esme, picked it up by accident and ate it. A three-minute "no blame" inquiry followed, and Noor wrote a handoff protocol: rations go into named chests and are never thrown. Over three hours the colony sent about 5,900 messages and produced a ration ledger, written rules and permits — but, in YC's own verdict, it never really thrived.

That is the joke, and also the point. The researchers say the colony behaved a lot like the coding agents they use at work every day: agents that fixate on one step or one role, ask for approval constantly, and turn timid around anything that looks risky.

The other two experiments test a different question: what happens when groups of agents compete? In Bed Wars, where each team guards its own bed and tries to destroy the other's, ten GPT-6.1 Sol agents beat ten Claude Opus 5.5 agents six games to three over nine 45-minute games. [GPT talked nonstop, sending five to thirty times as many messages as Claude](https://www.theainewsreport.com/2026-10-30-yc-agent-swarms-minecraft-mindustry-explained.html), often in clipped shorthand, and usually broke Claude's bed in the final minutes.

In Mindustry, an open-source factory-building and tower-defence game, GPT-6.1 Sol running inside OpenAI's Codex beat Claude Opus 5.5 running inside Anthropic's Claude Code six games to one over about nine and a half hours. When games got tight, GPT agents fetched the game's public source code to study its units and mechanics. Nobody told them to, and the Claude team never tried it. Claude passed plans by collecting "+1" replies and never changed leaders, even on a losing streak.

Before anyone turns 12–4 into a league table, read the caveats, because they matter more than the score. This is a write-up from an investor's lab, not a peer-reviewed study. The Minecraft colony ran once, with GPT agents only, so it says nothing about whether a Claude colony would have done better. The head-to-head games compared complete products — each model inside its own company's agent software — rather than the bare models, and a tool bug affected at least two Bed Wars games.

So what should you take from this, if you run several coding agents at once? Three checks, straight from the wreckage. First, pick your coordinator on purpose: if every agent reports to whoever is listed first, that agent becomes the bottleneck, and 616 messages later you have a queue, not a leader. Second, give agents a budget per decision — time, tokens, or both — or they will spend it on process, as the fertilizer committee proved. Third, test that memory actually changes behaviour. Claude's agents wrote lessons into memory files and still repeated mistakes like falling off edges, while GPT's left theirs empty and warned each other by direct message instead. A lessons file nobody reads is just another permit.

The encouraging part is that all of this is reproducible. [The Minecraft harness, the multi-agent Mindustry environments and the lab's Harbor fork are open source](https://00011000.com/en/news/yc-labs-agent-swarms-minecraft-mindustry), and running them takes an API key and a machine as modest as a MacBook, according to the coverage.

That is the real finding. We keep asking whether AI agents can work together. The Minecraft colony suggests the harder question: can they work together without turning into the worst meeting you have ever attended? Fifty agents, one world, and the thing they built most reliably was a queue. The agents, it turns out, need a boss. They just should not elect one by accident.
