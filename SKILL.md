---
name: research-skillbox
description: "Use when the user asks for end-to-end help with academic research or scholarly writing — choosing a research topic, searching and screening literature, reading or critiquing a batch of papers, writing a literature review, drafting or revising a paper section (Introduction, Methods, Results, Discussion, Conclusion), preparing a grant or research proposal, removing AI-sounding phrasing from a manuscript, turning reading into literature notes, writing official documents (notices, meeting minutes, work reports), or making a complex idea clear — understanding it first, then presenting it as text, a diagram, an interactive page, or a video. 中文触发：读论文、写文献综述、论文写作与修改、开题报告、基金申请书/课题申报、去 AI 味、文献笔记、公文写作、把复杂问题讲清楚、帮我看懂。Bundles 12 standalone research Skills and routes to the right one."
version: 1.0.0
author: Jin Hu
license: MIT
---

# Research Skillbox

A bundled collection of **12 standalone research Skills**, gathered behind one entry point.

> Ready-made paper prompts (40 workflow schemes + 30 advanced English writing
> instructions), kept verbatim for copy-and-paste use, live outside the Skills area in
> [`prompt-library/`](./prompt-library/README.md). That folder
> has no `SKILL.md`, so it is distributed with the bundle but not registered as a Skill.

## What this Skill is

This file is a **router**, not a method. It contains no writing rules of its own. Its only job is
to send the agent to the one sub-Skill that fits the request, so the agent loads a focused,
tested workflow instead of improvising.

Every sub-Skill under `skills/` is self-contained. It can also be installed and used on its own,
without this collection.

## How to use this bundle

1. Match the user's request against the routing table below.
2. Read `skills/<skill-name>/SKILL.md` **in full** before starting the task.
3. Follow that sub-Skill's workflow. Open its `references/` files only when it tells you to.
4. When two or more sub-Skills apply, chain them in order (see *Composing Skills*). Do not blend
   their instructions into a single pass.

Do not answer the user's request from this file alone. This file only picks the Skill.

## Routing table

| When the user asks to… | Load |
|---|---|
| Write or revise a paper, thesis, abstract, or one section of it | `skills/research-paper-writing/SKILL.md` |
| Write a literature review, or the review section of a proposal | `skills/research-paper-writing/SKILL.md` |
| Read a batch of papers and build a literature matrix | `skills/critical-paper-reading/SKILL.md`, then `skills/research-paper-writing/SKILL.md` |
| Strip AI traces / lower an AIGC score on a manuscript | `skills/academic-deai-writing/SKILL.md` |
| Write a grant or research proposal, section by section | `skills/grant-proposal-ai/SKILL.md` |
| Set up AI tools and workflows for research efficiency | `skills/ai-research-methodology/SKILL.md` |
| Turn books into material usable for writing | `skills/socratic-reading/SKILL.md`, then `skills/zettelkasten-notes/SKILL.md` |
| Prove a theorem, check a derivation, analyze novelty, design an algorithm experiment | `skills/research-copilot/SKILL.md` |
| Sort out graduate study, topic choice, advisor relations, or a career decision | `skills/graduate-research-career/SKILL.md` |
| Write a notice, summary, meeting minutes, report, or speech | `skills/ai-gongwen-writing/SKILL.md` |
| Explain something so the reader understands it — diagnose the blocker, then choose text, diagram, interactive page, or video | `skills/explain-clearly/SKILL.md` |
| Write an SOP, operations manual, or safety instruction; check manuscript language quality | `skills/explain-clearly/SKILL.md` (controlled language), plus `skills/research-copilot/SKILL.md` (language check scripts) |
| Reason through a complex decision or apply a thinking model | `skills/modern-thinking-toolkit/SKILL.md` |

## The 12 Skills

| Skill | What it covers |
|---|---|
| `skills/research-paper-writing/` | End-to-end paper writing and literature reviews: search and screening, critical reading, review drafting, topic and idea, section-by-section writing, pre-submission self-audit, defense |
| `skills/academic-deai-writing/` | Removing AI writing traces from papers and proposals: diagnosis, rewriting, boilerplate cleanup, word-budget reallocation, section-specific treatment |
| `skills/grant-proposal-ai/` | Grant and research proposal writing: every section, plus structured prompt templates |
| `skills/ai-research-methodology/` | Methodology and tool selection for doing research with AI: literature search, topic trends, experiment design, statistical modeling, submission and revision |
| `skills/critical-paper-reading/` | Critical reading of papers: fast triage, deep critique, multi-paper comparison, quality assessment |
| `skills/socratic-reading/` | Socratic method for reading books: four levels of reading, four core questions, reading plans and notes |
| `skills/zettelkasten-notes/` | Zettelkasten note-taking: fleeting notes, literature notes, permanent notes, linking and review |
| `skills/research-copilot/` | Rigorous research collaboration: mathematical proofs, derivations, review, literature surveys, novelty analysis, method design, numerical experiments, LaTeX, plus a controlled-language layer |
| `skills/graduate-research-career/` | Graduate study and academic career guidance distilled from 20 research guides, with 6 fillable templates |
| `skills/ai-gongwen-writing/` | Official and workplace writing in Chinese: notices, bulletins, minutes, plans, summaries, reports, speeches, and more |
| `skills/modern-thinking-toolkit/` | A toolkit of thinking models drawn from eight sources, for complex decisions and messy situations |
| `skills/explain-clearly/` | Making a reader understand: diagnose the comprehension blocker, align the facts, then pick the medium (controlled writing, diagrams, interactive HTML explainers, explainer video, discardable tools) and verify before delivery; includes the ASD-STE100 Issue 9 implementation |

## Composing Skills

Chain sub-Skills instead of running one pass that tries to do everything.

- **A pile of papers to a finished review** — `critical-paper-reading` → `zettelkasten-notes` → `research-paper-writing`
- **An idea to a grant proposal** — `research-copilot` → `grant-proposal-ai` → `academic-deai-writing`
- **A finished book to a published article** — `socratic-reading` → `zettelkasten-notes` → `research-paper-writing` or `ai-gongwen-writing`
- **A result to the right medium** — `research-paper-writing` → `explain-clearly` (controlled language, then diagram or interactive page)

## Language note

The 12 sub-Skills are written primarily in **Chinese**, and several are specific to Chinese
academic and official-document conventions. A sub-Skill's own file governs the language of its
output. `research-paper-writing`, `research-copilot`, and `explain-clearly` include
English-facing rules as well.

## License

MIT. See `LICENSE`. Third-party materials referenced inside individual Skills keep their own
terms.
