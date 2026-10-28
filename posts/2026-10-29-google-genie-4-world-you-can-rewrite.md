---
title: Google's Genie 4 isn't a video generator. It's a place you can walk into — and rewrite mid-stride
date: 2026-10-29
subtitle: A world model that simulates somewhere you can explore, complete with sound, weather you can change, and people who talk back. For about two minutes, anyway.
tags: AI news, AI tools, Google, explainer
excerpt: Google DeepMind's Genie 4, announced 27 October, generates explorable simulated worlds in real time — with native audio, live prompt editing, and steerable characters. It's a research preview for trusted testers, not a product yet, and its two-minute attention span is the most honest thing about it.
disclosure: false
sources:
- [Unite.AI](https://www.unite.ai/google-deepmind-rolls-out-genie-4-world-model-in-research-preview/)
- [Skimwire](https://www.skimwire.com/google-deepmind-genie-4-world-model-audio/)
- [Okay News](https://www.okaynews.com/google-genie-4-research-preview-october-27-2026/)
---

There is a difference between a video and a world, and Google DeepMind would very much like you to notice it.

A video plays. A world responds. On 27 October, DeepMind announced Genie 4, its fourth world model, and the pitch is exactly that: not a clip you watch, but a place you move through, in real time, while it keeps simulating what happens next. You navigate with keyboard controls and a camera. And while the scene is running, you can type a plain-language instruction — change the weather, move the camera, drop in a new person or object — and the world rewrites itself around you.

The headline upgrade is sound. Genie 4 is DeepMind's first real-time world model to generate audio natively: wind in the trees, waves at the beach, background music and characters talking back are all produced by the model at the same time as the visuals. Previous world models were silent films. This one talks.

That matters more than it sounds. A silent simulation is a diorama. Add dialogue that adapts on the fly, and the characters in it are not props — they react to what you do and to events in the world. DeepMind says the biggest leap in this version is people: characters who move naturally, respond to their environment, and can be steered in real time.

So how does it hold together? With a committee. Gemini Omni anchors how the simulated world looks and behaves, while other Gemini models supply the reasoning that keeps the scene coherent between your inputs. For complicated, multi-step events, Gemini 3.8 Flash acts as a guiding agent in the loop: it watches the scene, breaks a goal into steps, checks each frame to see whether the step actually worked, and adjusts the plan as the world shifts or you intervene.

That division of labour is also the point of the whole exercise. DeepMind describes understanding and simulating the world as a crucial aspect of building AGI, and the practical payoff it keeps coming back to is robotics. In one documented experiment, Gemini 4 Argon broke a task into steps while Genie 4 simulated Apptronik's Apollo humanoid playing checkers, adapting as the game progressed. A robot that can practise in infinite simulated worlds never has to break a real one while learning.

The other audiences DeepMind names are more immediately human. Filmmakers are testing Genie 4 as a rapid "draft mode" for pre-visualisation — stepping into a live simulation and running multiple takes while adjusting camera angles, lighting, dialogue and action. Photojournalists are exploring how a single 2D archival photograph can become a grounded simulation of that environment in seconds. Game developers are checking whether they can go from an idea to an explorable prototype in seconds, before writing engine code.

It is a good story. Here is the part that keeps it honest: the world only lasts about two minutes.

Coverage from The Verge and TechCrunch puts Genie 4's scene consistency at up to about two minutes, roughly double its predecessor. DeepMind itself is blunter about the edges. Visual details and object permanence can shift or drift over time, especially in longer sessions, after several complex prompt edits, or when navigating through a scene. It cannot simulate real-world locations with perfect accuracy. Audio accuracy, complex interactions, legible text, spatial accuracy and long-term consistency are all listed as ongoing research. In other words, the world is convincing until you stare at it too long — and then it starts forgetting itself.

That is not a flaw to hide; it is the whole state of the field. A world model has to predict everything, continuously, and every prediction is a chance to drift. Two minutes of coherence is genuinely impressive. It is also a very short leash for anyone imagining a persistent virtual world or a reliable robot training ground.

Access reflects that early state. Genie 4 is a research preview for trusted testers. It is coming soon to Project Genie for Google AI Ultra subscribers and to early-access partners through the Gemini API and Google AI Studio, with a waitlist open — but there is no general public release yet, and DeepMind has not settled what the final product even is. All video and audio it generates will carry SynthID, DeepMind's imperceptible watermark.

Genie 4 is also not arriving into an empty room. The field is crowding fast: Runway has its GWM Worlds 2, AMD is buying Fei-Fei Li's World Labs, and Rivian has bought simulation startup Third Dimension for self-driving tests. Everyone with a robotics or gaming ambition seems to have decided, at roughly the same moment, that generating video is not enough — you need to generate somewhere.

That is the takeaway worth keeping. The last few years of AI were about generating content: text, images, video. Genie 4 points at the next shift, from content you consume to environments you inhabit, however briefly. The demo is a world you can walk into and rewrite while you are standing in it. The limitation is that it forgets itself after two minutes. Whoever stretches those two minutes into twenty, and then into hours, will own the training ground for every robot and agent that comes after.
