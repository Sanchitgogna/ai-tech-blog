---
title: "Google's new AI can't write a single sentence. That's the point."
date: 2026-11-13
subtitle: "Gemini Decision 1 doesn't generate text — it scores options, 1,000 at a time, in about a fifth of a second. The labs are now selling decisions by the million, and the price war has found its floor."
tags: AI news, AI agents, Google, explainer
excerpt: "Google announced Gemini Decision 1 on 11 November: a model that skips text generation entirely and scores candidate answers in a single pass — up to 1,000 questions per request, 150–250 ms, $0.10 per million input tokens, zero for output. It is the latest in a sudden wave of decision-only models, and it turns the cheapest unit in AI from a word into a choice."
disclosure: false
sources:
- [Google — Gemini Decisions API: Fast multimodal decisions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/?ref=explainx)
- [MLQ — Google launches Gemini Decision 1](https://mlq.ai/news/google-launches-gemini-decision-1-a-model-that-scores-up-to-1000-questions-in-one-pass/)
- [BigGo Finance — Google Abandons Text Generation for "Decision-Specialized" AI](https://finance.biggo.com/news/e334413b-8aa0-4e11-b048-6e66d9338af0)
---

Every model you've ever used writes its answer one word at a time, even when the answer is just "yes". Google's newest model doesn't. It can't write a sentence at all. It scores options — up to 1,000 in a single pass — and hands back a probability for each. [Announced on 11 November](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/?ref=explainx), Gemini Decision 1 powers the new Gemini Decisions API, and it's the clearest sign yet that the AI business is splitting in two: the models that write, and the models that decide.

The trick is what it skips. A normal model generates its answer token by token, which is why even a one-word answer takes time and costs output tokens. Decision 1 never generates: you hand it a fixed list of candidates and it evaluates them all in one forward pass, returning probabilities and a confidence score from 0 to 1. One request can carry a single multimodal input of up to 256,000 tokens — text, images, audio, video, PDFs — plus up to 1,000 questions, in 150–250 milliseconds. The input is billed once per request.

Three question types, and they're the whole product: yes/no checks, multiple choice across 2 to 255 options, and ordered rubric scores — each returning probabilities for every candidate. Google's example runs all three against one photo of a breakroom counter in a single request.

## The ten-cent tier is becoming a category

The price is $0.10 per million input tokens and $0 for output, with a no-cost tier in Google AI Studio for prototyping. Google says that works out to roughly a fifth of the cost of using Gemini 3.5 Flash-Lite through its Interactions API on the same benchmark suite.

That number should sound familiar. [Two days ago](https://sanchitgogna.github.io/ai-tech-blog/posts/2026-11-10-meta-ember-vs-anthropic-fable-price-gap/) this blog noted that Meta's Muse Ember launched at exactly $0.10 per million input tokens. Same price, different job: Ember generates text; Decision 1 doesn't generate anything. Two labs landing on the same figure within 48 hours isn't a coincidence — it's a price war finding its floor. The cheapest unit in AI is now ten cents per million.

Google's benchmarks, for the record, are Google's: Decision 1 tops seven of nine, with the lowest calibration error — 0.0250 against GPT-6 Luna's 0.0721. But the two it loses are worth more than the seven it wins. It trails TypeSafe's Jev 1.14 on When2Call, the tool-selection timing test (79.9% to 82.0%), and on Mind2Web (86.2% to 86.8%). Tool calling is the whole point of a decision model for agents. The specialist still beats the generalist at the specialist's own game.

## The startup did it first

Google is, unusually, following. The decision-only model was pioneered by Jev, from the startup TypeSafe, which shipped in September. OpenAI announced its own Decisions API on 29 September and put it in public beta on 6 October. Microsoft launched Microsoft-Decision-1 on 9 October, built on Alibaba's Qwen3.5-9B. Google is the fourth mover in six weeks — and the one lab conspicuously absent is Anthropic, which has announced nothing comparable.

That sequence matters. It's an industry realising that agents spend most of their time not writing but choosing: which tool to call, which model to route to, whether a result passes a policy check. Each choice used to mean firing up a full generative model and paying for an answer you could have expressed in one word. Now there's a cheaper, faster component for it — and every lab wants to own the one that sits in the middle of every agent's loop.

Google is already eating its own cooking. Gemini Notebook uses the API as a live router — Google says everyday queries come back up to 40% faster. Google Search uses it as a safety layer, screening MCP tools for adversarial behaviour. Stitch and Google Labs' CC use it for wireframes and emoji picks. Integrations with OpenRouter, LangChain, Vercel and LiteLLM are rolling out, with Google Cloud support promised soon.

## The honest part is the confidence score

Here's the part that deserves more attention than the speed: every answer comes with a confidence score. It's the whole reason a decision model can be trusted inside an agent loop — your code can send low-confidence calls to a bigger model or a human, and let the confident ones fly. A system that knows when it doesn't know is worth more than one that's right slightly more often and silent about the rest.

Which brings us to the caveat. A decision delivered in 200 milliseconds is still a wrong decision if the model picks the wrong tool, and in an agent system a wrong tool call doesn't stay wrong — it cascades. It books the wrong thing, and the next ten decisions inherit the error. Making decisions cheap and fast is genuinely useful. It is also genuinely dangerous if teams treat a probability as a permission slip and stop checking the low-confidence tail.

The shift is real, though. Three years ago the unit of AI was the word. Then it was the token. Now Google, OpenAI, Microsoft and a startup you've probably never heard of are all selling the same new unit: a decision, priced by the million, delivered in a fifth of a second, with a number attached that says how sure it is. The writing models aren't going anywhere. But the models that decide what the writing models do will run the most, cost the least, and fail the quietest. Watch the confidence scores.
