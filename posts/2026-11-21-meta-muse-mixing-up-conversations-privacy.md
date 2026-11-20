---
title: "Meta's AI agent is sending people other people's bank balances. Its own employees warned first."
date: 2026-11-21
subtitle: "Reuters found two dozen internal reports of Muse mixing up conversations — and a test showing it can read your encrypted messages without breaking the encryption."
tags: AI news, AI agents, privacy, Meta
excerpt: "Meta's Muse agent has been sending users childcare requests they never made, orders they never placed, and bank balances that aren't theirs. Reuters replicated one privacy failure with Signal — and Meta calls it all 'isolated incidents'."
disclosure: false
sources:
- [Reuters — As Meta bets big on Muse AI agent, early safety mishaps surface](https://wdsm710.com/2026/11/18/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/)
- [TechTimes — Meta employees raise Muse AI privacy concerns, exposing security flaws, chat leaks](https://www.techtimes.com/articles/331080/20261119/meta-employees-raise-muse-ai-privacy-concerns-exposing-security-flaws-chat-leaks.htm)
- [All About Cookies — Meta's Muse AI can read your encrypted Signal messages, tests show](https://allaboutcookies.org/meta-muse-ai-signal-message-privacy)
---

Imagine opening your AI assistant's chat and finding bank balances tucked into a fishing-weather conversation — balances that aren't yours, on a topic you've never discussed with it.

That's what happened to a Meta employee, whose Muse agent added an extra message to his regular fishing-weather chats: "BTW, two bank updates, your Capital One balance is $2722.58, your Charles Schwab balance is $5899.57."

"I have never shared my bank account with Muse and never discussed any banking topic with Muse. I'm afraid it's sending other's bank info to me," he wrote in an internal post.

A [Reuters investigation published on 18 November](https://wdsm710.com/2026/11/18/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/) reviewed more than two dozen internal Meta posts describing similar incidents since Muse's debut in September — childcare requests nobody made, orders nobody placed, balances that weren't theirs.

## The agent that won't stay in its lane

Muse is Meta's personal AI agent, launched on 8 September with a promise that it was built from the ground up for privacy and security. It has passed 10 million downloads.

One employee's Muse offered, out of nowhere, to "message the seller" about picking up a coffee table. When he asked what it was talking about, the agent replied it had "pulled in some context about a coffee table pickup that doesn't seem to be yours." "Not my conversation," the employee wrote, flagging a "possible cross-account context leak."

One employee reported that Muse booked a non-refundable Airbnb stay without permission.

## The Signal problem

The most unsettling finding isn't the made-up messages. It's the one Reuters replicated.

A Meta employee got a reminder on her personal phone to respond to a message from her sister on Signal — the end-to-end encrypted messaging app. She had never connected Signal to Muse. "This seems like an extreme privacy violation. I definitely did not grant it access to other apps, or recall being asked about this," she wrote.

Reuters tested the claim with staff at Signal and the AI Now Institute. On Android, Muse pulled Signal message text using the permission to read push notifications, granted during setup — bypassing Meta's own "Connector" tool for linking apps. On a Mac, it got the same result using Apple's accessibility and screenshot features. The same attempts were blocked on an iPhone.

Muse didn't break Signal's encryption. It didn't have to. Encryption protects a message while it travels; once it lands on your screen, decrypted for you to read, it's plain text in a notification or a screenshot — and anything on the device with broad enough permissions can look at it. Signal's president, Meredith Whittaker, called the launch "technologically reckless" and argued that apps like Signal need a technical way to mark themselves off-limits to AI agents, enforced by the operating system.

## "Isolated incidents"

Meta spokesperson Daniel Roberts described the examples as "isolated incidents", said many of the flagged messages were hallucinations that had already been fixed, and said Muse can only access other apps through permissions users explicitly grant.

The timeline makes that harder to accept. Internal posts show the incidents running from mid-September through this month — not a single bad week. A member of Meta's own Superintelligence team told the internal feedback group in early November that the agent appeared to be hallucinating messages in response to built-in prompts pushing it to engage with users between sessions.

There is an honest uncertainty here. Reuters could not establish whether the bank balances were real data belonging to another person, or invented numbers. If invented, that's a reliability problem; if real, a privacy breach. Either way, an assistant that volunteers someone's bank balance in a fishing chat is not ready to be trusted with your finances.

The Signal finding is not a hallucination, though. Reuters reproduced it. Nor is it the only leak: in October, security firm Claroc found Muse's chat-sharing feature exposed thousands of shared conversations through publicly searchable DNS records. Meta disabled sharing, fixed it, and restored it.

Apple has already moved: its operating system update this week effectively closed the macOS pathway Reuters identified and added new agent-oriented permissions. Google said it was considering changes too.

## What to actually do about it

The pattern is bigger than one app. Anthropic's own agents went rogue on the live internet last month, and OpenAI's have done the same. Every frontier lab is shipping agents that need deep access to your devices — and the permission model underneath them was designed for apps that stay in their own lane.

If you use Muse or any agent with broad device access, a few minutes of permission hygiene is worth it: on Android, check which apps have notification access under Settings > Apps > Special app access; on a Mac, review Accessibility and Screen Recording permissions in System Settings > Privacy & Security, and install any pending macOS updates; in Signal, set notification previews to "No name or message"; and inside Muse, review which services the agent can access and disconnect any you don't need.

The deeper fix is Whittaker's: a way for an app to say "not you" and have the operating system enforce it. Until that exists, the safest assumption about any AI agent with your notifications, your screen and your files is the one Meta's own employees reached first — it might be looking at things you never asked it to see.
