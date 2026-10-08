---
title: "Was that photo made by AI? Google's free checker just opened to everyone"
date: 2026-10-09
subtitle: "SynthID Detector now takes uploads from anyone — here's how to use it, and why a clean result proves absolutely nothing."
tags: AI news, how-to, AI tools
excerpt: Google's SynthID Detector went global on 7 October, letting anyone upload an image, video or audio file to check for invisible AI watermarks from Google, OpenAI, NVIDIA and Kakao. Here's how it works, its limits, and how to read a result.
disclosure: false
sources:
- [Unite.AI](https://www.unite.ai/google-opens-synthid-detector-globally-with-partner-ai-content-checks/)
- [MacRumors](https://www.macrumors.com/2026/10/07/google-synthid-detector/)
- [SQ Magazine](https://sqmagazine.co.uk/google-synthid-detector-public-ai-media-checks/)
---

Every group chat eventually reaches the same moment. Someone drops a photo — a politician doing something absurd, a "real" video of a tornado where tornadoes don't happen — and someone else asks the only question that matters: is this even real?

Until this week, answering that properly needed either a journalist's toolkit or blind faith. [Google has quietly fixed the toolkit part](https://www.unite.ai/google-opens-synthid-detector-globally-with-partner-ai-content-checks/). On 7 October, it opened its SynthID Detector — the portal that scans files for invisible AI watermarks — to everyone, everywhere, in English. No waitlist, no press credentials. It had been sitting with a small group of journalists, media professionals and researchers since May 2025.

## How to use it

1. Go to Google's SynthID Detector (find it via the announcement on The Keyword — it's a plain web portal).
2. Sign in. There's no skipping this part; the tool requires a Google account.
3. Upload the suspicious file. It takes images (JPG, PNG, WEBP, GIF, HEIC), video (MP4, MOV, WEBM) and audio (MP3, WAV, FLAC and more).
4. Read the result. For an image, it says whether a watermark was detected. For video and audio, it's smarter than that — it flags *which segments* of the file carry the watermark, so a partially AI-edited clip can be pinned down.
5. Pace yourself. Ars Technica reports the portal caps users at roughly 10 checks a day. Google told the site the limit exists to make it harder for people to hammer the system and reverse-engineer ways to strip the watermarks. So no, you can't batch-verify your entire meme folder in one sitting.

## What it can actually detect

SynthID is an invisible watermark embedded at the moment AI content is created — hidden in the pixels, the video frames, or the audio waveform. Since launching the system in 2023, [Google says it has watermarked more than 180 billion images and videos, plus 240,000 years of audio content](https://sqmagazine.co.uk/google-synthid-detector-public-ai-media-checks/). That is not a typo. Two hundred and forty thousand *years*.

The detector covers media from Google's own generators plus partners OpenAI, NVIDIA and Kakao — and Apple support is coming later this year. The watermark is designed to survive the things people normally do to files: cropping, filters, frame-rate changes, lossy compression. The audio version survives MP3 compression and speed changes. That's deliberate — the whole point is for the signal to persist through the journey from generator to group chat.

Google already bakes this checking into Search, the Gemini app and Chrome, which it says handle more than a million verification requests a day. This portal is the standalone version anyone can use.

## What it cannot do (the important part)

The Detector's own FAQ is refreshingly blunt: *"This is not a general AI detector."* It can only spot the SynthID watermark. And that means a "no watermark found" result proves exactly nothing. Three reasons it might miss:

- The file was made by a model that doesn't use SynthID. That's a big universe — most standalone generators don't.
- The watermark degraded after heavy modification.
- The file is a photo of a photo, a screen recording, or otherwise a few steps removed from the original.

It also can't distinguish AI-*created* from AI-*edited* media, and Google notes rare false positives, recommending you upload the highest-quality file available and gather multiple points of evidence before drawing conclusions.

Two more practical notes: your uploads are processed in real time and deleted immediately after results are returned (a digital signature is kept for 24 hours purely to enforce the daily quota), and the terms of service prohibit reverse-engineering or automating queries.

## The takeaway

Think of this as one layer in a provenance toolkit, not a verdict machine. "Watermark found" is strong evidence the file came from a supported AI tool. "No watermark found" is the system politely declining to comment — treat it as *no evidence either way*, and keep checking the source, the context, and whether your uncle's forwarded video really shows a tornado in Adelaide.

But credit where it's due: this is now the largest cross-company content-provenance check available to the public for free, and the cross-company bit is what matters. A check that only catches one company's models is a curiosity; one covering Google, OpenAI, NVIDIA and Kakao — with Apple on the way — is something you might actually reach for. The next time someone drops a suspicious photo in the chat, you'll have an answer better than "looks fake to me."
