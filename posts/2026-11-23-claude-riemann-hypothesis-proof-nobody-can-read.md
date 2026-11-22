---
title: "Claude just proved the Riemann Hypothesis. No human can read the proof."
date: 2026-11-23
subtitle: "An Anthropic mathematician and Claude cracked maths' most famous problem in six weeks. The machines have certified it correct — and the humans are still catching up."
tags: AI news, AI research, Anthropic, Claude
excerpt: "Levent Alpöge says he and Claude proved the Riemann Hypothesis, maths' most famous open problem. The Lean and Mathlib communities have certified the 17-million-line proof as correct — but nobody, including Alpöge, has read it yet."
disclosure: false
sources:
- [Phys.org (AFP) — Anthropic researcher says he and Claude proved the Riemann hypothesis, first posed in 1859](https://phys.org/news/2026-11-anthropic-claude-math-greatest-riddle.html)
- [The Decoder — Hours after Anthropic claims a Claude proof of the Riemann hypothesis, Stanford releases an all-human competing draft](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/)
- [Andrew Sutherland (MIT) — Verification files for the Lean proof of the Riemann Hypothesis](https://math.mit.edu/~drew/grh/)
- [Tbreak — Claude-assisted Riemann hypothesis proof passes Lean checks](https://tbreak.com/riemann-hypothesis-proof-claude-anthropic/)
---

On Friday, an Anthropic mathematician said he and Claude had done what mathematics couldn't do in 167 years. Then he admitted something stranger: he can't fully explain how.

"I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis," [Levent Alpöge wrote in a four-page note](https://phys.org/news/2026-11-anthropic-claude-math-greatest-riddle.html) posted to his personal website on 20 November. The hypothesis, proposed by Bernhard Riemann in 1859, predicts a precise hidden pattern in how prime numbers are distributed. It is one of the Clay Mathematics Institute's seven Millennium Prize Problems, each carrying a $1 million prize. Alpöge says his method also resolves the broader Generalized Riemann Hypothesis.

Brian Conrey, a leading specialist on the problem, called it "the biggest thing I think that's ever happened in mathematics" — before adding he hadn't seen a manuscript, only the remarks posted online.

## The proof is 17 million lines long

Alpöge and Claude worked on the problem for about six weeks, from 6 October to 16 November. He set the direction; Claude did the technical work. The result exists only as computer code: roughly 17 million lines of Lean, a language that checks mathematical arguments step by step, split across 14 archives. Printed out, Alpöge says the argument would run to more than 250,000 pages, and he calls it unreadable.

The core idea is, at least in outline, human-sized. The pair extended an approach pioneered by the mathematician Stepanov, chaining special transformations together to mimic the effect of a derivative on whole numbers — a trick that normally fails, because individual values can't be differentiated like a continuous line. The key insight, supplied by the model, was that for a number sequence of length X, you need to chain exactly as many transformations as the square root of X.

Then the scale exploded: Claude spelled out even the most basic steps, until no person could ever sit down and read it.

## The machines checked it in a day

So the checking was outsourced to machines, too. On 21 November, the communities behind Lean and its main maths library, Mathlib, published a joint statement saying they have "full confidence" that Alpöge's proof is correct and certifying both the statement and the proof. Dozens of people independently compiled the codebase without errors.

MIT's Andrew Sutherland logged the checks: all 175,187 modules compile with zero errors, the five headline theorems rest only on the three standard axioms of mathematics, and independent proof checkers written in different languages — nanoda, con-leche, lean4lean — all accept the exported proof.

What remains is understanding it. Alpöge openly says he hasn't mastered parts of the mathematics himself, particularly where Claude raced ahead of him, and he plans to write a human-readable account over the coming months.

## Stanford rushed out a rival proof hours later

Within hours, the story got stranger. Stanford mathematician Ravi Vakil posted a draft proof of the Generalized Riemann Hypothesis by Alessandro Masullo — pointedly "all human, with no AI." Brian Conrad had reviewed it for months, and the plan was a year of refining. Anthropic's announcement forced their hand.

About eight hours later, Vakil updated his post: several people had reported problems in the draft, identified with the assistance of different AI models. The symmetry is hard to miss — the AI-assisted proof was certified by machines in a day, while the all-human proof was debugged, in part, by AI within hours.

## The timing, and the year that led here

The announcement landed the day after Anthropic's record-breaking stock market debut — a point Alpöge raised himself. He says he texted CEO Dario Amodei about the result late on a Sunday, waited until after the IPO on 19 November, and calls the timing "extremely unfortunate" while rejecting any suggestion of a PR stunt.

The result caps a year in which AI kept creeping up on this problem. In August, Anthropic said a research version of Claude had raised the proven share of the zeta function's zeros from 41.6% to 67.2% — while explicitly warning the techniques wouldn't lead to a proof. Three months later, they did.

Forecasters had expected the proof by May 2035; Terence Tao said last month he expected it around 2050. Both were wrong by a decade or more.

## What counts as a proof now?

The $1 million prize, for now, stays unclaimed. The Clay Institute still lists the problem as unsolved: a solution needs a peer-reviewed publication, two years of scrutiny, and general acceptance among mathematicians. Alpöge has published only on his own website.

Hundreds of published papers assume the Riemann Hypothesis is true; if the certification holds, they all become established theorems overnight. For centuries, a proof was a human argument that other humans could follow. This one is a machine argument that other machines have verified — and the humans, including its own author, are now doing the homework of understanding what was proved.

At a Harvard workshop in October 2024, MIT number theorist Andrew Sutherland summed up the stakes: "An AI that can prove the Riemann hypothesis is not one I'd want to meet. If that happens, mathematicians having jobs will be the least of our problems." Two years later, they solved it. The jobs question is still open. The understanding question is now the job.
