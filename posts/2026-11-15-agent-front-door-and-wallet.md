---
title: "Your AI agent just got a front door and a wallet on the same day. The shops aren't ready."
date: 2026-11-15
subtitle: "Poppy 1.0 and ChatGPT Wallet landed on the same Friday — the plumbing for agents that shop and pay. The catch: the shops, the banks, and the customers haven't agreed to any of it yet."
tags: AI news, AI agents, AI tools, shopping
excerpt: "On Friday 13 November, Sierra shipped Poppy 1.0 — the protocol that lets your AI agent walk into a business and introduce itself — and OpenAI shipped ChatGPT Wallet, which lets its dots agents pay. Shopify switched Poppy on for every store, but Amazon blocks agent purchases, United Airlines is stopping agent bookings, and Visa found AI shoppers fail 42.8% of the time."
disclosure: false
sources:
- [Sierra — Releasing Personal Agent Protocol 1.0](https://sierra.ai/blog/releasing-poppy)
- [The Outpost — OpenAI launches ChatGPT Wallet for agent shopping](https://theoutpost.ai/news-story/openai-s-agents-can-now-buy-things-for-you-if-anyone-lets-them-33501/)
- [Unite.AI — Sierra Releases Poppy 1.0 With Shopify and Meta Muse Support](https://www.unite.ai/sierra-releases-poppy-1-0-with-shopify-and-meta-muse-support/)
---

Friday was the day the agent economy got its two missing pieces, within hours of each other. One tells a shop who your agent is. The other lets it pay. Neither works yet in the way its makers hope — and the gap between the two launches is the whole story.

Sierra [released version 1.0 of the Personal Agent Protocol](https://sierra.ai/blog/releasing-poppy) — Poppy — on 13 November, five weeks after the draft we covered here in October. Poppy is the handshake: your personal agent turns up at a business, says who it is and who it represents, and finds out what it's allowed to do, instead of pretending to be you with your password. The big move is distribution. Shopify has switched Poppy on automatically for every merchant on its platform, across more than 175 countries, with no work required from the shop. Meta's Muse agent now looks for Poppy first on every site it visits. Sixty new companies joined as design partners, taking the total past 100 — Cisco, Delta Air Lines, Intuit, Salesforce, Twilio and Zoom among them. Mercury, Synchrony and Turkish Airlines are already live with it.

The same day, OpenAI [launched ChatGPT Wallet](https://theoutpost.ai/news-story/openai-s-agents-can-now-buy-things-for-you-if-anyone-lets-them-33501/), built with American Express, Mastercard and Visa. It lets OpenAI's dots agents complete purchases on your behalf. You save a card once; the agent assembles the purchase, you review the items and the total, and you approve with Face ID or a fingerprint before anything is charged. The card number never travels — the payment network issues a token, a stand-in number, so neither the agent nor the merchant ever sees your real details. OpenAI takes no cut of transactions at launch, and it published a Commerce Partner Playbook to persuade retailers to let agents through their firewalls.

## Two halves of one checkout

Put them together and the picture is clear: Poppy is the front door, the Wallet is the till. Poppy handles the moment an agent arrives and identifies itself; Shopify's Universal Commerce Protocol handles the cart and checkout; the Wallet handles the money. Sierra and Shopify co-authored a commerce extension linking Poppy to UCP, so an agent can shop as a guest or signed in to your account, and talk directly to the store's own agent.

It is a genuinely elegant stack. It is also, for now, a stack with almost nothing on top of it. The wallet is limited to a small group of US ChatGPT Pro subscribers aged 18 and over, with a US billing address and an eligible US-issued card. Every purchase still needs your biometric approval — full autonomy, with spending caps, categories and time limits set in advance, is promised for later, with no timeline. And Poppy's own specification is still labelled draft 1.0, with breaking changes explicitly possible. Version 1.0, it turns out, is a draft.

## The web is saying no

The bigger problem is on the other side of the counter. Plenty of the internet will simply refuse your agent. Amazon blocks agent purchases on its marketplace. United Airlines said this week it will stop agents booking tickets, and Delta bans them too. JPMorgan and Schwab don't let agents move customer money. OpenAI itself warns that some sites may block its agents by accident and that fraud systems may flag legitimate agent purchases, producing declines or cancellations.

Then there's the demand question, which is awkward. Uber reported four agent rides and 500 Uber Eats orders in the final week of October, against roughly 320 million rides and deliveries. DoorDash's chief executive put agent orders at several hundred in total. Airbnb described its agent bookings as "very non-material". An American Bankers Association survey last month found 77% of respondents concerned about giving an agent permission to pay, and 61% unlikely to let one manage bank balances within a year. Visa tested 22 AI models as shoppers this month and they failed 42.8% of the time.

The counter-argument is scale. Meta's Muse agent has more than 10 million users, and shopping has become a top activity on the app. ChatGPT has over 1.2 billion weekly users, giving the wallet reach no smaller agent product has. The dots agents only arrived in late September, so the wallet is a fast follow-on about six weeks later — OpenAI is building the checkout before anyone has asked for it, betting that the asking comes once the checkout exists.

## The takeaway

There is a pattern here worth naming. The agent economy keeps arriving as infrastructure first and demand second: a protocol before the partners, a wallet before the shoppers, a checkout before the trust. That is not necessarily wrong — the web itself was built that way — but it means the next year of agent commerce will be decided less by the companies shipping the plumbing and more by the ones refusing to connect to it. Amazon, United, the banks and the fraud systems are not laggards here; they are the market, telling the labs what it actually wants.

The honest test is simple. Watch whether the merchants who said no start saying yes, and whether the shoppers who said they're worried start letting an agent hold the card. Until then, your agent has a front door and a wallet — and a lot of closed shops to walk past.
