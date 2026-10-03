---
title: Apple just told AI agents to stop asking for your whole hard drive
date: 2026-10-04
subtitle: macOS's most powerful permission is getting harder to grant, and the reason Apple names is your agent
tags: AI agents, AI news
excerpt: Apple is tightening macOS Full Disk Access explicitly because of AI agents — and it's the clearest signal yet that "just trust the agent" was never a permission model.
disclosure: false
sources:
- [Unite.AI: Apple to tighten macOS Full Disk Access, citing AI agent risks](https://www.unite.ai/apple-to-tighten-macos-full-disk-access-citing-ai-agent-risks/)
- [Agntbox: Your AI Agent Does Not Need Your Whole Hard Drive](https://agntbox.com/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from/)
- [ai0.news: Apple locks Full Disk Access over agent risks](https://ai0.news/posts/2026-10-03-daily-digest/)
---

Somewhere in Cupertino, someone finally said it out loud: your AI agent does not need to read your love letters to do your expense reports.

On Thursday, Apple posted a quiet update to its developer news site — "Updates to Full Disk Access in macOS" — and tied it, unambiguously, to AI agents. Full Disk Access, Apple said, was built so backup software can do its job: it largely sidesteps the privacy controls that normally protect your data so a backup app can copy everything. The problem is that a growing crowd of developers has started asking for the same permission for very different purposes, exposing files, mail, messages, and browsing history "without users' full knowledge and understanding."

Apple's framing of the fix is one sentence: granting that access will soon require "very explicit user action." No date. No macOS version. No named app. But the stated reason is doing all the work: "As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially."

Now, Apple didn't invent this concern. The announcement follows reports that Meta's Muse agent accessed a journalist's private iPhone and Mac messages without clear user awareness — a claim Meta disputes — and a separate vulnerability in ChatGPT's Mac app that could have exposed sensitive data. Reaction on Hacker News was split in a way that tells its own story: some developers welcomed per-folder granularity, while others objected to Apple calling disk access "extraordinary" at all. It used to be the baseline assumption, one commenter grumbled, that software running on hardware you own could read your files. That's true — and it also misses the point entirely.

Because an agent asking for Full Disk Access is a different proposition from a backup utility asking for the same thing. A backup utility reads files and copies them to a disk you own. An agent reads files and sends them somewhere: a model provider, a logging endpoint, a vector database, a telemetry pipeline nobody documented. Apple's phrasing gets at this obliquely — the risk is reading *plus* outbound — but the math is straightforward. The agent has your data; the agent also has a network connection. That combination is what makes whole-disk access "extraordinary" in a way it wasn't in the backup-utility era.

Here's the part that should make agent developers squirm. Broad permissions aren't usually a design decision — they're the path of least resistance. Building scoped file access means thinking about which directories actually matter, writing a folder-picker flow, handling the case where the user says no. Asking for Full Disk Access means one dialog and done. Plenty of agent tools have shipped setup docs that start with "enable Full Disk Access," screenshot of System Settings and all, before explaining a word about what the agent does with your files. When the easy path is also the overreaching path, you get overreach by default — not malice, just friction doing what friction does.

Apple adding friction flips the incentive. If granting Full Disk Access becomes a deliberately scarier, more explicit act, developers who grabbed it out of convenience get a reason to build the scoped version instead. The permission request becomes a review signal: a tool that demands your whole disk without explaining why is telling you something about how carefully it was designed.

There is one caveat, and it's the whole game. Consent screens have a terrible track record of actually informing anyone. We have all accepted cookie banners we didn't read. If Apple's new flow is just more words in the same box, behaviour won't change. If it's structurally different — clearer disclosure of exactly what the app can reach, maybe scoped middle tiers — it could genuinely reshape how agent tools get built on the Mac. Apple hasn't said which. The gap between "we will introduce additional controls" and shipping behaviour is where this either becomes meaningful or becomes wallpaper.

So what do you do before any of this lands? Don't wait for Apple — audit your Full Disk Access list yourself, right now. Open System Settings and look at who holds it. You'll probably find at least one tool you tested once and never uninstalled. Revoke anything you don't actively use; nothing breaks that you can't re-enable. For the agent tools you keep, check whether they offer a scoped alternative — some do and just don't advertise it. And ask where your data goes. The answer should be in the docs. If it isn't, that's your answer.

The deeper signal here matters more than the dialog box. When a platform vendor names AI agents as the reason for a platform-level lockdown, the overreach was visible enough from the outside to force a response. Dots, Manus, Muse — the agent wave is real, and so is the new bargain it's quietly trying to strike: hand over the keys to everything, and trust the cloud. Apple's bet is that you shouldn't have to.

The permission an agent asks for tells you a lot about how carefully it was designed. Soon, on the Mac at least, those asks are going to be a lot harder to hide.
