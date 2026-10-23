---
title: "An AI found the flaw that knocked half the internet offline. Now comes the hard part."
date: 2026-10-24
subtitle: "PHP2Shell is the first internet-scale bug found by frontier AI — and the same models that found it can help attackers exploit it."
tags: AI news, AI safety
excerpt: "Two critical PHP flaws dubbed php2shell, found with AI help, forced governments to take their websites offline this week. OpenAI calls it the start of a new phase in cybersecurity — one where the audit cycle is about to get dramatically shorter."
disclosure: false
sources:
- [TechCity Authority](https://www.techcityauthority.com/2026/10/openai-php-critical-flaws-patch-the-planet.html)
- [Zotpaper](https://zot.news/article/emergency-php-patches-issued-critical-remote-code-execution-qt2lx)
- [TrendInTech](https://trendintech.com/php2shell-ai-vulnerability-70-percent-websites-2026/)
- [Artiverse](https://www.artiverse.ca/gpt-56-sol-uncovers-php-flaws-threatening-70-of-the-web/)
---

On Wednesday, government IT teams did something they almost never do voluntarily: they switched their websites off.

Finland's state IT centre took public web services offline as a precaution. The Netherlands' national cybersecurity agency did the same — it pulled its *own* site. France followed. So did pages for the BBC and Edinburgh Council, and the Wikimedia Foundation preemptively shut down systems while it worked through the patch. It wasn't a hack. It was the response to one — or rather, to the possibility of millions of them.

The culprit was hiding in PHP, the workhorse server language that quietly runs WordPress, Drupal, Joomla, and a huge chunk of everything else you touch online. Two bugs in the PHP engine itself — [CVE-2026-109618 and CVE-2026-109619](https://www.techcityauthority.com/2026/10/openai-php-critical-flaws-patch-the-planet.html), collectively dubbed **php2shell** — let an attacker run their own code on a server without logging in first. They score 9.2 out of 10 on the CVSS severity scale. OpenAI estimates PHP runs about 70% of websites; however you slice that figure, it's a lot of websites sharing one very bad day.

Here's the part that matters for this blog: **an AI found them.**

Security firm Calif spotted the first flaw on August 1 using OpenAI's GPT-5.6 Sol model, as part of OpenAI's "Patch the Planet" initiative — a programme pairing frontier models with human security researchers for exactly this kind of hunt. Cloud security company Wiz, now part of Google Cloud, independently found both flaws on August 19 using its own tooling plus outside models including Gemini 4 Argon. Two separate AI-assisted teams, two weeks apart, converged on the same critical holes.

And here's the unsettling detail: this bug class isn't new. Calif's CEO told the Wall Street Journal that researchers had [identified this kind of flaw decades earlier but considered exploiting it too difficult](https://trendintech.com/php2shell-ai-vulnerability-70-percent-websites-2026/). Humans found the lock but couldn't pick it. The AI picked it in a few dozen requests. That's not a faster researcher — that's a capability step. Wiz put it bluntly: "frontier models were critical to making this process practical, enabling us to develop and adapt working exploits across multiple applications in hours."

What followed was a two-month coordinated disclosure — PHP's volunteer maintainers rewriting deep engine code, Cloudflare building mitigations, government agencies brought in quietly. Then the plan sprang a leak: details surfaced on social media the day before the announcement, forcing the PHP Foundation to [rush the patches out early](https://www.techcityauthority.com/2026/10/openai-php-critical-flaws-patch-the-planet.html). Cloudflare's CTO reported seeing early attacks within hours of the leak. The fixes shipped Wednesday: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35.

OpenAI is framing all this as a win, and honestly, they're entitled to some credit. The company calls it a **"Defender's Window"** — frontier AI found the vulnerability ahead of attackers, giving the good guys time to prepare. It says it committed $1 billion in subsidised access to its security tools for under-resourced groups protecting essential services, and published a draft playbook for handling future AI-found bugs.

But read the fine print of OpenAI's own announcement and the victory lap gets wobbly. The same post that celebrates the Defender's Window admits the capabilities that found php2shell "can also help attackers rapidly develop offensive tools and exploits." OpenAI expects findings like this to rise sharply in the coming months. The window only holds while defenders have better tools than attackers — and both sides are shopping at the same AI vendors.

And the patching reality is grim. Censys data puts about 1.5 million of 2.6 million PHP-reporting hosts on a version with no official fix. PHP 7 and 5 still run on a big share of PHP sites and are long out of support. PHP quietly powers shared hosting platforms, control panels, and software that doesn't even advertise it runs PHP under the hood — the long tail of the internet is going to be patching this for months, and some of it will never be patched.

**What should you do?** If you run a server: update PHP to one of the patched versions now, or install your Linux distribution's backported fix. If you're on managed or WordPress hosting: ask your provider whether they've patched — don't assume. If you're just someone who visits websites: nothing. The scramble is happening on the other side of the screen, which is why half of it went dark.

The takeaway is bigger than one bug. AI doesn't just write our code anymore — it audits the foundations the code stands on. For decades, a serious bug sat in one of the most-used languages on Earth because humans couldn't figure out how to exploit it. A model did it in August, and we found out in October because someone leaked. Next time the model won't need a leak, the disclosure window will be shorter, and there will be more bugs in the queue.

OpenAI's researchers say they already have "several significant vulnerabilities" lined up and expect similar findings to increase sharply. The web's immune system — volunteer maintainers, patched hosts, emergency maintenance windows — is about to learn what it feels like to be audited continuously, by machines that never sleep.

This week, the auditors gave the defenders a two-month head start. Enjoy the memory. Next time, the clock might be measured in days.
