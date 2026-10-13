# Research & Academic Skills Collection

**English | [中文](./README.cn.md)**

> A set of AI Agent Skills built around three pillars: **the full research workflow**, **academic career development**, and **general-purpose thinking**.
> It covers a complete loop — **read papers → think through problems → do research → write papers → apply for funding → build a knowledge base** —
> plus official-document writing and a general thinking toolkit.

This repository contains **12 Skills**, primarily written in Chinese, following the common
`SKILL.md + references/` layout. In principle they work on any Agent platform that supports
this convention (WorkBuddy, Claude Code, Codex, and others).

Beyond the Skills, [`prompt-library/`](./prompt-library/README.md) holds a set of
ready-made paper prompts (40 workflow schemes + 30 advanced English writing
instructions) kept verbatim, for copy-and-paste use. They cover the whole paper lifecycle from
topic selection to submission. That folder carries no `SKILL.md`, so it
ships with the repository but is not registered as a Skill.

The root also carries a `SKILL.md`. It is a **collection router**: it holds no writing rules of
its own and exists only to send the agent to the right sub-Skill under `skills/`. You can use
the repository as one bundle, or take a single Skill out of it.

---

## Table of contents

- [What these Skills are](#what-these-skills-are)
- [Skill overview](#skill-overview)
- [Choose a Skill by scenario](#choose-a-skill-by-scenario)
- [Quick start](#quick-start)
- [Repository structure](#repository-structure)
- [Composing Skills](#composing-skills)
- [Sources and copyright notice](#sources-and-copyright-notice)
- [License](#license)

---

## What these Skills are

A Skill is essentially **a reusable professional workflow written for an AI**: it consists of a
`SKILL.md` (which declares *when to trigger* and *what process to follow*) and a number of
`references/` files (which hold the detailed knowledge, templates, and checklists). When you
raise a relevant request in conversation, the Agent automatically loads the matching Skill and
executes it according to an established method — turning "improvise on the spot" into
"follow an expert's process."

These Skills share three characteristics:

1. **Traceable provenance** — most domain knowledge is distilled from classic books, authoritative
   guides, or public papers, not invented on the fly.
2. **Actionable, not vague** — they provide decision criteria, checklists, writing formulas, and
   prompt templates rather than generic advice.
3. **Clear boundaries** — each states explicitly when to use it and *when not to*, avoiding
   over-triggering and misuse.

---

## Skill overview

### A. Research writing and output

| Skill | One-line positioning | Core content |
|---|---|---|
| [research-paper-writing](./skills/research-paper-writing/README.md) | The **end-to-end** workhorse for paper writing and literature reviews | Search & screening → critical reading → review drafting → topic & idea → section-by-section writing (Intro/Abstract/Method/Experiments/Related Work/Conclusion) → pre-submission self-audit → defense; includes a real-example library and a manuscript check script |
| [academic-deai-writing](./skills/academic-deai-writing/README.md) | Remove **AI traces / AIGC markers** from papers and grant proposals | Root-cause diagnosis, general rewriting, boilerplate cleanup, re-allocating word budget, plus section-specific treatment (Introduction/Results/Discussion/novelty) and English-specific rewriting |
| [grant-proposal-ai](./skills/grant-proposal-ai/README.md) | A writing guide for **grant / research proposals** | Writing techniques for every section (rationale, research content, technical route, novelty, feasibility, budget) + 40 structured prompt templates |
| [ai-research-methodology](./skills/ai-research-methodology/README.md) | **Methodology and tool selection** for doing research with AI | Literature search, topic trends, data processing, experiment design and novelty mining, statistical modeling, figure generation, submission and revision; separate golden prompt sets for STEM and humanities |

### B. Literature reading and knowledge management

| Skill | One-line positioning | Core content |
|---|---|---|
| [critical-paper-reading](./skills/critical-paper-reading/README.md) | **Critical close reading** of one or many papers | Keshav's three-pass method + structured element extraction + a critical-thinking engine (question checklists, argument evaluation, research-gap identification); outputs a structured reading report |
| [socratic-reading](./skills/socratic-reading/README.md) | Read a book using the **Socratic questioning method** | Adler's four levels of reading (elementary/inspectional/analytical/syntopical) + a four-question chain + book selection and speed-reading output methods |
| [zettelkasten-notes](./skills/zettelkasten-notes/README.md) | The **Zettelkasten note-taking method** | Fleeting → literature → permanent notes + linking + index + review; solves "I take lots of notes but never write anything" |

### C. Research collaboration and career development

| Skill | One-line positioning | Core content |
|---|---|---|
| [research-copilot](./skills/research-copilot/README.md) | A rigorous **research collaboration** entry point | Mathematical proofs and derivations, paper writing and review, literature surveys, novelty analysis, topic selection and method design, algorithms and numerical experiments, LaTeX; v2 adds a controlled-language layer (ASD-STE100 research-adapted edition + Chinese/English manuscript check scripts) |
| [graduate-research-career](./skills/graduate-research-career/README.md) | Guidance for **graduate study and academic careers** | Distilled from 20 research guides: onboarding, topic selection, reading literature, research habits, writing and publishing, advisor relations, research integrity, career choices; includes 6 fillable templates |

### D. Workplace writing and general thinking

| Skill | One-line positioning | Core content |
|---|---|---|
| [ai-gongwen-writing](./skills/ai-gongwen-writing/README.md) | A **Chinese official-document and workplace writing** library | 20+ official document types (notices, bulletins, meeting minutes, requests for instructions, summaries, research reports, leadership speeches…) and workplace genres (weekly reports, retrospectives, applications, public remarks, annual reviews); each with a writing formula + step-by-step prompts + final-draft self-check |
| [modern-thinking-toolkit](./skills/modern-thinking-toolkit/README.md) | A **modern thinking toolkit** (~320 models) | Decision algorithms, game theory, probability and Bayes, critical thinking, systems thinking, role-based mindsets, cognitive growth; automatically picks 1 primary and up to 3 supporting/counter tools and outputs conclusions, mechanisms, trade-offs, and actions |
| [explain-clearly](./skills/explain-clearly/README.md) | **Make a reader understand** — diagnose the blocker, then pick the medium that costs the reader the least effort | Five rungs (controlled writing → diagrams → interactive HTML explainer → explainer video → discardable tool) + escalation/de-escalation criteria; a comprehension-first layer (preserve facts, boundaries, and source; report "not yet verified" honestly); and a complete implementation of ASD-STE100 Simplified Technical English Issue 9 (53 rules + controlled dictionary + check scripts) |

---

## Choose a Skill by scenario

| What I want to do… | Which Skill |
|---|---|
| Write a paper or thesis, or I'm stuck on a section | `research-paper-writing` |
| Write a literature review or the review section of a proposal | `research-paper-writing` |
| Read through a batch of papers and build a literature matrix | `critical-paper-reading` + `research-paper-writing` |
| A reviewer says my writing sounds AI-generated; my AIGC score is too high | `academic-deai-writing` |
| I just want a ready-made set of paper-writing prompts | [`prompt-library/`](./prompt-library/README.md) (not a Skill — reference material) |
| Write a grant or research proposal | `grant-proposal-ai` |
| Learn how to use AI to boost research efficiency (tools, workflows) | `ai-research-methodology` |
| Turn books I've read into material I can actually write with | `socratic-reading` → `zettelkasten-notes` |
| Mathematical proofs, derivations, novelty analysis, algorithm experiments | `research-copilot` |
| I'm a grad student feeling lost: topics, advisor relations, whether to do a PhD | `graduate-research-career` |
| Write a notice, summary, meeting minutes, or work report | `ai-gongwen-writing` |
| Understand something myself, or explain it clearly to others: diagrams, an interactive webpage, an explainer video | `explain-clearly` |
| Write an operations manual / SOP / safety instructions, or check manuscript language quality | `explain-clearly` (controlled language) + `research-copilot` (language check scripts) |
| Make a complex decision, analyze a messy situation, find a mental model | `modern-thinking-toolkit` |

---

## Quick start

Every Skill is a self-contained directory — just copy it in.

**Option 1: Install the whole bundle (all 12 Skills at once)**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cp -r <repo-name> ~/.workbuddy/skills/research-skillbox
```

The root `SKILL.md` is the collection router; `skills/` holds the 12 sub-Skills. The platform
loads the router first, then descends into `skills/` and registers all 12 sub-Skills.

**Option 2: Install a single Skill (global; available to all projects)**

```bash
git clone https://github.com/<your-username>/<repo-name>.git

# Copy the Skills you need into your user-level skills directory
cp -r <repo-name>/skills/research-paper-writing ~/.workbuddy/skills/
cp -r <repo-name>/skills/critical-paper-reading  ~/.workbuddy/skills/
# …copy as needed
```

**Option 3: Project-level install (active in one project only; easier to share with a team)**

```bash
mkdir -p <your-project>/.workbuddy/skills
cp -r <repo-name>/skills/research-paper-writing <your-project>/.workbuddy/skills/
```

After installing, restart the Agent or reload Skills. They will then trigger automatically in
conversation, or you can invoke them by name (e.g. "use research-paper-writing to help me draft
a literature review").

> Layout convention: `SKILL.md` is the entry point, `references/` holds knowledge fragments,
> `assets/` holds templates, and `scripts/` holds scripts. **When installing the bundle, the
> sub-Skills must sit under `skills/`**: most platforms descend only into that directory once a
> `SKILL.md` is present at the parent level, so sub-Skills placed anywhere else will not be
> registered automatically. If your platform requires specific frontmatter fields, add them per
> its documentation — the body needs no changes.

---

## Repository structure

```text
.
├── SKILL.md                      # Collection router: routes a task to a sub-Skill under skills/
├── README.md                     # English README (default, this file)
├── README.cn.md                  # Chinese README
├── LICENSE                       # MIT License
├── prompt-library/               # Not a Skill (no SKILL.md) — distributed reference material
│   ├── README.md                 #   Index, source notes, and usage rules
│   └── *.md                      #   40 prompt schemes + 30 English writing instructions (verbatim)
└── skills/                       # Each directory below = one standalone Skill
    ├── research-paper-writing/
    │   ├── SKILL.md              #   Entry point: trigger conditions + workflow
    │   ├── README.md             #   Skill detail page
    │   ├── references/           #   Knowledge fragments (section guides, checklists, examples)
    │   └── scripts/              #   Executable scripts (e.g. manuscript self-check)
    ├── academic-deai-writing/
    ├── grant-proposal-ai/
    ├── ai-research-methodology/
    ├── critical-paper-reading/
    ├── socratic-reading/
    ├── zettelkasten-notes/
    ├── research-copilot/
    ├── graduate-research-career/
    ├── ai-gongwen-writing/
    ├── modern-thinking-toolkit/
    └── explain-clearly/
```

---

## Composing Skills

Each works well alone, but chaining them is far more powerful. A few typical chains:

- **From a pile of papers to a finished review**
  `critical-paper-reading` (read each paper, extract elements, raise critiques)
  → `zettelkasten-notes` (distill into literature cards and build links)
  → `research-paper-writing` (structure, write, and self-audit the review)

- **From an idea to a grant proposal**
  `research-copilot` (argue the scientific question and method feasibility)
  → `grant-proposal-ai` (write section by section, apply the prompt templates)
  → `academic-deai-writing` (strip boilerplate and AI traces)

- **From finishing a book to publishing an article**
  `socratic-reading` (four levels of reading, four core questions)
  → `zettelkasten-notes` (permanent notes)
  → `research-paper-writing` / `ai-gongwen-writing` (produce the final text)

---

## Sources and copyright notice

Some Skills in this repository **distill methodology and material from publicly published books,
courses, white papers, or public lectures** (e.g. paper-writing guides, literature-review
methodologies, mental-model courses, official-document writing handbooks). They were
**restructured, rewritten, and reorganized** by the author for personal learning and research
efficiency.

### Content falls into three categories — please treat them differently

| Category | Description | Examples |
|---|---|---|
| **① Distilled / rewritten** (the bulk) | Restatement and structural reorganization of key methods, not verbatim copying | The flows, rules, and checklists of each Skill; the functional distillation of ASD-STE100 controlled English in `explain-clearly` / `research-copilot` |
| **② Verbatim quotations** (all sources cited) | Original sentences, prompt templates, or phrase banks kept for authenticity or functionality | The "金句 (Lecture N)" quotes in `modern-thinking-toolkit`; the verbatim prompt sets in `prompt-library/`; the academic phrase bank in `research-paper-writing` |
| **③ Third-party material under known copyright constraints** | Material whose owners explicitly restrict redistribution; such files carry prominent notices | *Academic Phrasebank* cited in `research-paper-writing` (University of Manchester — personal use only, electronic redistribution prohibited) |

### Citation conventions

- **Every verbatim quotation is set in quotation marks and attributed** (lecture number, chapter,
  author, or source file).
- **Wherever a method can be stated in our own words, we do so** — verbatim quotations are kept
  only where the original wording is irreplaceable or where functionality requires it (e.g. prompts
  meant to be copied and used as-is).
- **Every Skill directory's `README.md` includes a "References / Sources" list**, itemizing the
  source, author, origin, and what was borrowed — for traceability and credit.
- Third-party material under copyright constraints carries a prominent **usage and redistribution
  notice** in the relevant file.

### Rights and contact

- The MIT License of this repository **covers only the author's own contributions** and **does not
  alter** the ownership of any third-party material.
- If you hold rights to any original material and believe the content organized here infringes
  your rights, please contact us via an Issue and we will **remove or adjust the relevant content
  immediately**.

> Users are advised to follow their institution's academic integrity rules when citing output
> produced by these Skills. AI output must be human-verified; this repository assumes no academic
> liability arising from such use.

---

## License

This repository is released under the **MIT License** — see [LICENSE](./LICENSE).
You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of
the content, provided the copyright notice and permission notice are retained.

**Important caveat:** the MIT License covers the **author's own contribution** (code,
documentation, and the organization of the methodology). It does **not** grant any rights in
third-party source material that some Skills distill from — those rights remain with their
respective owners. See [Sources and copyright notice](#sources-and-copyright-notice) above.

> Final reference: the `LICENSE` file in the repository root.

---

## Contributing

Issues and PRs are welcome: adding new Skills, fixing knowledge errors, improving workflows, and
completing source attributions.

When submitting a PR, please keep each Skill directory self-contained and describe the trigger
scenarios and sources in its README.
