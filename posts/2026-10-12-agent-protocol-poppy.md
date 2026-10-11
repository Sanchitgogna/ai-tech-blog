---
title: "Your AI agent just got its own front door — meet Poppy, the handshake between bots and businesses"
date: 2026-10-12
subtitle: "Meta and Sierra's Personal Agent Protocol wants to end the era of AI agents pretending to be humans clicking buttons"
tags: AI news, AI agents, explainer
excerpt: "On 6 October, Meta and Sierra announced the Personal Agent Protocol — an OAuth-based open standard for how your AI agent signs in to businesses and gets things done. Three days later, a draft nicknamed Poppy went public. Here's how it works, who's in, and why the standards war underneath it matters."
disclosure: false
sources:
- [CellCog — Personal Agent Protocol (Poppy): Draft Spec and Partners](https://cellcog.ai/blog/personal-agent-protocol/)
- [Prompt & Power — Personal Agent Protocol Explained: Meta, Sierra and Shopify](https://promptandpower.com/personal-agent-protocol-meta-sierra-shopify-explained/)
- [Sunporch AI — AI's Biggest Week Yet: Math Breakthroughs and Agent Standards](https://sunporchai.com/blog/ai-s-biggest-week-yet-math-breakthroughs-and-agent-standards-2026-10-10)
---

Right now, when you ask your AI agent to book a hotel, rebook a flight, or process a return, it does something a little absurd: it logs into the company's website and clicks through every step exactly like a human would.

Pages loaded. Forms filled. Buttons pressed. One slow, fragile pantomime at a time.

Companies don't love it either. Their options are to block AI agents outright — Amazon has reportedly done exactly that to Meta's agents — or accept that bots will cosplay as customers on their websites, and try to tell the legitimate ones apart from the scrapers. As Sierra co-founder Bret Taylor [put it to CNBC](https://cellcog.ai/blog/personal-agent-protocol/): "It is kind of chaos until such a standard exists."

Well, someone has now proposed the standard.

## The handshake, announced

On 6 October 2026, at Sierra Summit in San Francisco, Sierra (the enterprise AI company co-founded by ex-Salesforce co-CEO Bret Taylor and ex-Google AR lead Clay Bavor) announced the **Personal Agent Protocol** — PAP for short — developed together with Meta. The pitch is simple: a universal, open "handshake" for how a personal AI agent signs in to a business and gets a task done on your behalf.

The founding partner list reads like a coalition that actually wants this thing to exist: **Shopify, Stripe, Walmart, Genesys, Instinct, and Rocket**, with contact-centre vendors NiCE and Decagon named on Meta's version of the list.

Here's how a session works under the proposal:

1. **Discovery.** Your agent visits the company's website and reads what it offers and how to reach it.
2. **Guest start.** The agent opens a session as a guest — enough to check stock or read a returns policy.
3. **Sign-in.** For account tasks, you sign in on the company's page, the familiar OAuth flow you already know.
4. **Access.** You decide whether your agent gets read-only or write access.
5. **The task.** The company chooses the route: its regular website set up to be readable by agents, its APIs (built on standards like MCP or OpenAPI), or its *own* agent taking over the conversation for things like warranty claims.

And here's the neat bit: one session carries across channels. A question asked before sign-in and an order change made after it count as a single visit, because it's all one OAuth session.

## Poppy is already real — as a draft

This is where the story got interesting fast. Three days after the announcement, on 9 October, Sierra published an actual draft of the protocol, nicknamed **Poppy**, at personalagentprotocol.org. Companies publish a single file at `/.well-known/poppy.json` that tells agents how to connect, how customers authenticate, and what's allowed.

The draft's five building blocks — discovery, sessions, sign-in, one session across channels, getting the job done — are all published and readable today. Design workshops and a reference implementation are promised over the following month.

Even more telling than the draft: the same day, Sierra named **35 design partners** joining the process. Payments and banking dominate the list — Bank of America, Mastercard, Visa, PayPal, Wells Fargo, Adyen, Chime — alongside retailers (Target, Gap, Nordstrom), airlines (United), insurers, and software companies (Notion, Cloudflare, 1Password, Zendesk, ElevenLabs).

And — plot twist — **OpenAI is on the design-partner list**, three days after CNBC reported it wasn't participating. (Taylor, who is also OpenAI's chairman, said he'd be disappointed if competitors didn't join.) **Anthropic is still absent.** Google and Amazon are not named either. So this is a real coalition with real momentum, and a real holdout list that will decide whether it becomes *the* standard or just *a* standard.

## It's not the only protocol at the table

This is the part that makes the whole thing genuinely fascinating. PAP doesn't arrive alone — it joins a crowded, half-built layer of agent-commerce standards, and they don't all do the same job:

- **UCP** (Google + Shopify, January 2026) handles discovery, carts, and checkout.
- **ACP** (OpenAI + Stripe, September 2025) handles checkout *inside* the agent.
- **TAP** (Visa + Cloudflare, October 2025) passes merchants a cryptographic signature declaring the agent's intent, optionally with payment details.

PAP is the layer *beneath* all of them. It answers "who is this agent, who sent it, and what may it do here?" and leaves "how does the money move?" to someone else. Sierra's own announcement lists payments as a possible future extension, not part of the first version.

That layering is why the same names keep appearing on several lists — Stripe is in PAP and ACP, Shopify in PAP and UCP. Shopify's VP of product told Sierra that PAP "helps establish how agents and merchants can work together." Translation: merchants can't negotiate with every agent-maker individually, so they want a seat wherever the rules get written.

## Why this actually matters to you

Meta's David Singleton compared the protocol to email — shared plumbing that everyone runs over. And the pressure for it is coming from real usage: Meta's personal agent Muse launched in September and, per Singleton, already has millions of US users doing travel bookings, form-filling, and purchases.

If PAP gains traction, the boring, fragile way agents use the web today — pretending to be you, clicking your buttons — gives way to something cleaner. Businesses get to see exactly which agent is acting for whom. You decide whether it can read or write. And the agent-to-agent channels start to matter as much as the websites you visit yourself — an AI creator's work might one day be discovered, licensed, or transacted through these channels, not just browsed by humans.

The caveats are real, though. It's a draft, not a finished standard. The reference implementation doesn't exist yet. Anthropic — whose agents are arguably the most capable at this kind of work — isn't at the table. And the payments question, the thing that makes this whole exercise actually *useful*, is still "a possible extension" with no date.

But here's the thing about standards: they tend to look irrelevant right up until they're invisible. Nobody thinks about OAuth when they sign in with Google. In two years, you may never think about the handshake your agent uses to talk to a hotel website either.

The draft is at personalagentprotocol.org. The workshops are coming within the month. Watch who shows up next — the holdout list is the whole story.
