---
title: The four biggest AI labs just agreed on something. It's two lines in a text file.
date: 2026-10-31
subtitle: One robots.txt token now lets a website opt out of AI training across OpenAI, Google, Microsoft and Anthropic — with a long list of caveats attached.
tags: AI news, AI policy, AI tools
excerpt: On 30 October, OpenAI, Google, Microsoft and Anthropic all backed a shared robots.txt token, __usage_ai-training, that lets a site opt out of AI training across every participating company at once. It is real progress — and it does not do nearly as much as the headlines suggest.
disclosure: false
sources:
- [Unite.AI](https://www.unite.ai/openai-to-honor-shared-robots-txt-signal-for-ai-training-preferences/)
- [Search Engine Land](https://searchengineland.com/google-also-gives-publishers-more-control-over-how-ai-uses-their-content-499971)
- [Skimwire](https://www.skimwire.com/ai-training-opt-out-robots-txt-openai-google-microsoft-anthropic/)
- [AI Weekly](https://aiweekly.co/alerts/openai-google-microsoft-anthropic-back-one-ai-opt-out-token)
---

For once, the four biggest AI labs agree on something. Given the last few weeks — duelling letters to California's governor about kill switches, a price war fought with 90 percent discounts, an IPO filing that reads like a confession — that alone is worth pausing over. This time, though, the agreement is not about a model, a market, or a law. It is about two lines in a text file.

On 30 October, OpenAI, Google, Microsoft and Anthropic all said they will honour a single shared signal in robots.txt — the humble file websites have used for decades to tell crawlers what they may and may not touch. The signal is a policy token called `__usage_ai-training`. A site that wants out of AI training writes this:

```
User-Agent: __usage_ai-training
Disallow: /
```

And that, in theory, is it. One entry, every participating company. Want to opt out of everything except your press kit? Add `Allow: /press-kit/` underneath. No new directives, no new grammar — the draft behind it deliberately leaves the robots.txt standard, RFC 9309, untouched, so existing parsers just ignore the token the way they ignore any user agent they do not recognise.

Until now, opting out meant keeping a list: GPTBot, Google-Extended, ClaudeBot, plus a growing tail of smaller crawlers. Every new lab meant a new line, and every missed line meant a loophole.

The paperwork behind the announcement deserves the same care as the announcement itself. The token comes from an Internet-Draft titled "Machine-Readable Training Preference Signal," written by Kevin Kelley of Anthropic and dated 30 October, under the Internet Engineering Task Force's AI Preferences working group. It is an individual draft, not a formal standard — the IETF's own datatracker notes it "is not endorsed by the IETF and has no formal standing in the IETF standards process" — and it expires on 3 May 2027 unless updated. This is a promise dressed as a draft, not a law dressed as a standard.

Then there is the timeline, best described as staggered. Anthropic says it has already begun implementing support. OpenAI says it aims to implement the signal "in the coming months." Microsoft targets 1 February 2027. Google says 2027, with no month attached. Add those two lines to your robots.txt today and nothing changes today. The opt-out is published; the honouring of it is still arriving, company by company.

And even when it arrives, it will not do what many people will assume it does. This is the part that matters most, so let us be precise.

First, the token governs training, not fetching. The draft says so explicitly: it "is not a directive for crawling behavior." Bots may still pull the page. It does not block search indexing, and it does not stop a page from being quoted in AI-written search answers — which, for publishers watching their traffic drain into chatbots, is arguably the use that hurts most. Opting out of training and opting out of being answered-from are two different doors, and this token only closes one of them.

Second, it is voluntary, and it only binds the companies that choose to follow it. OpenAI frames the mechanism as "a coordination mechanism rather than a security control," a polite way of saying a scraper that ignores robots.txt will keep ignoring it. Nothing here reaches the bad actors, the data brokers, or the labs that never signed up.

Third, it is not retroactive. Updating robots.txt does not remove material already collected into datasets or baked into trained models. The token speaks to the future, not the past — and the past is where most of the training data already lives.

Microsoft went furthest on the practical details: a page-level training setting, a separate "AI Grounding" setting for Bing, Copilot and Microsoft 365 answers, and a `DisallowExtended` option for grounding in its own products only. These replace Bing's old NoArchive and NoCache tags, and sites relying on those have until 1 March 2027 to switch. Microsoft is also blunt: "Neither choice guarantees inclusion, traffic, or payment."

So is this a win? Yes, but a narrow one, and the narrowness is the story. For years the debate over AI training and publishers' rights has been stuck between two unworkable positions: individual opt-outs nobody can maintain, and lawsuits that take years and settle nothing for the small site in the middle. A single shared token is the first mechanism actually usable by a blogger, a local newspaper, or a photographer with a portfolio site — which, not coincidentally, is most of the web. It turns a chore into a choice.

But a choice is all it is. It does not pay publishers, it does not restore traffic, it does not undo training that already happened, and it does not bind anyone who declines to be bound. The labs have agreed on the easy part — a common vocabulary for saying no — while the hard parts, payment and attribution and answers, remain exactly where they were.

Still, do not underestimate the boringness of this news. Robots.txt itself was never a law; it was a convention that worked because everyone agreed to pretend it mattered, until it did. If this token follows the same path, 30 October will look like the day publishers finally got a door they could close. Just check which rooms it locks, and which ones it leaves wide open.
