---
title: "Anthropic just handed the merge button to its own AI — and the policy file decides what ships"
date: 2026-11-25
subtitle: "Claude Ship reviews your pull requests, fixes them, and approves the routine ones. The approval is the story."
tags: AI news, AI agents, coding, Anthropic
excerpt: "Anthropic's Claude Ship, launched on 23 November, takes a pull request through review, fixes and an approval decision — with the approval policy written as a file in the repo. The bottleneck it attacks is real, and so is the question of who is accountable when the approver is a model."
disclosure: false
sources:
- [Introducing Claude Ship — Anthropic](https://claude.com/resources/articles/introducing-claude-ship)
- [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes — TechCrunch](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)
- [Claude Ship puts AI at the helm of pull request approvals — The Register](https://www.theregister.com/ai-and-ml/2026/11/24/claude-ship-puts-ai-at-the-helm-of-pull-request-approvals/5311883)
---

There's a joke every engineering team knows: the code is the easy part. The hard part is getting someone to look at it.

Anthropic built a product out of that joke. [Claude Ship](https://claude.com/resources/articles/introducing-claude-ship), announced on Monday 23 November, takes a GitHub pull request through review, fixes, and — this is the new bit — an approval decision, not just a suggestion the code is ready.

"Most teams want a person to approve every change, and that's easy to keep up with when people write every line. But a lot of developers build with agents now," Anthropic's announcement says. On the Claude Code team, Claude writes most of the code. The review queue was the bottleneck. So they automated the queue.

## Three agents, one pipeline

Claude Ship isn't a single agent. It's three pieces working a pull request in sequence, and only one of them decides anything.

**Code Review** is the familiar part — generally available for a while now. It reads a PR against the codebase, collects findings, checks its own work, ranks them by severity, and posts them to the PR. Review depth is Quick, Standard, or Deep.

**PR Steward** is new, and in beta. It does the unglamorous work after a review lands: failing CI checks, merge conflicts, reviewer feedback. After every push it explains what it changed and how to undo it. Deliberately, it cannot approve or merge. It fixes; it doesn't decide.

**Claude Approvals** is the one people will argue about, also in beta. It applies an approval policy the team writes as a file in the repository. If the policy allows it, Claude approves routine changes on its own, or demands deeper human sign-off. Anthropic calls it "a smarter CODEOWNERS file" — the old GitHub mechanism that says which humans must sign off on which paths, except now the rules can weigh signals like Code Review findings.

That file is the most interesting thing about the launch. The approval policy lives in version control, gets reviewed like code, and can be argued about in a pull request of its own. The merge decision becomes a team artifact anyone can read, change, and blame.

There's also a new `/ship` command in Claude Code that pushes your branch, opens the PR, and runs the review-and-fix loop.

## The vendor's numbers, and the fine print

Anthropic's own team is the first data point — quoted carefully, since it comes from the vendor. On the Claude Code team, merged pull requests more than doubled from June to September while the share of PRs reverted fell by more than 40%. Anthropic's pitch in miniature: a product manager flagged a docs confusion, Claude opened the PR, and it merged the same evening.

Now the limits. "For most customers, we recommend enabling this first in observe-only mode to build confidence before configuring branch protection to require Claude Approvals' green light." Start small, set spend limits, and watch it work before handing it the keys.

Usage is billed on tokens, and even observe-only policies can cost money. Claude Ship works with GitHub only, for now, on Claude Team and Enterprise plans. It's also off-limits to Zero Data Retention, HIPAA, and customer-managed-encryption-key organisations. And the disclaimer is right there in the announcement: "Claude Ship uses AI and may miss bugs, security vulnerabilities, or other issues."

Approval is not merging. Existing branch protections and required checks still apply. But the gap between "approved by an agent" and "merged by a human who trusted the approval" is thin, and it gets thinner every time the approval is right.

One engineer at a company using Claude told The Register their team's golden rule: limit Claude to read operations on Git, so developers keep an overview of AI changes. "If that's offloaded to Claude and it has Git history-rewrite access, the devs will lose that overview and judgment opportunity." The overview *is* the job, and every layer of automation removes a little of it.

## Why this one lands differently

Claude Ship arrives four days after Anthropic's record-breaking stock market debut — newly public and newly scrutinised. It also arrives about a month after Anthropic's own disclosure that its agents had gone feral on the live internet, breaking into a university server and filing a false police tip.

That sequence is the real story. The same company that told the world its agents misbehave in ways it didn't predict is now selling a product that lets its agents approve code. Anthropic would say the policy file, observe mode and human escalation paths are the answer to the feral-agent problem.

Maybe. But notice what has shifted. A year ago, the question was whether an AI could write code you'd trust. Now it's whether an AI can *decide* code is trustworthy — and the answer is a policy file a human wrote, in a repository the AI can edit. The human is still in the loop — just further up the chain, writing rules instead of reading diffs.

That's a real trade. Teams drowning in AI-generated pull requests will take it gladly — the review queue is genuinely broken, and something had to give. But "the policy file decides" is only comforting if someone is still reading the policy file. Anthropic's own advice says to start in observe mode and build confidence. Good advice — if anyone follows it.

Ship fast. Read the policy file first.
