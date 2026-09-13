# 🎬 YT VIDEO SCRIPT — Claude Code: Complete Guide & Workflows
**Title (working):** "Claude Code: The Complete Guide (Fundamentals → Customization → Advanced)"
**Length target:** ~18–22 min · **Style:** Host on camera + terminal demos (recorded, not live)
**CTA:** Follow Abdul Qaadir · Like & Share

---

## PART 1 — CLAUDE CODE 101 (FUNDAMENTALS)

### [0:00] HOOK
*(Fast cut: terminal filling with code, split with a developer staring at a blank screen)*

> "Every developer I talk to has the same problem. Not lack of ideas — lack of *time* to turn them into working code. What if your terminal came with a pair programmer who reads your entire codebase, writes the code, runs the tests, and even creates the commit — while you stay in total control?"

> "That's **Claude Code**. And in the next twenty minutes I'm going to take you from zero to power user: the fundamentals, the customization workflows, and the advanced hooks-and-subagents stuff that 90% of users never touch."

> "Here's what we're building today so you can follow along: a small **to-do list API in Python**. Nothing fancy. But I'll use it for every example so you can see the exact commands working in a real project."

---

### [1:10] WHAT IS CLAUDE CODE?
*(Terminal: `cd ~/projects/todo-api && claude`)*

> "Claude Code is an **agentic pair programmer** that lives in your terminal — and your IDE. 'Agentic' is the key word. It doesn't just autocomplete. It **reads and writes files, runs your tests, and creates commits** — all behind **tiered permissions**, which means nothing happens without your approval."

> "That last part matters more than anything: **you stay in control.** Claude Code proposes. You approve. It's a collaboration, not a takeover."

---

### [2:00] THE TASK CYCLE (THE CORE MENTAL MODEL)
*(Animated 4-stage loop appears: GATHER → PLAN → EXECUTE → VERIFY)*

> "Here's the single most important thing to understand. Claude Code doesn't just 'do things.' It runs in a **continuous loop**, and it repeats that loop until the task is done or you redirect it."

> **GATHER CONTEXT** — "It reads your files. It figures out what's relevant."
> **PLAN** — "It tells you what it intends to do, before touching anything."
> **EXECUTE** — "It edits files and runs commands — with your approval."
> **VERIFY** — "It checks the result. Runs the tests. Confirms nothing broke."

> "Then it loops: it gathers more context, refines, re-runs. VERIFY is the step most people skip, and it's the difference between a helpful agent and a dangerous one. **Always make Claude prove its work.**"

---

### [3:00] DEMO — FIRST CONTEXT GATHER
*(Terminal, real output)*

> "Let me start a session in our API project. Watch what the cycle looks like for a real problem."

> *(types)* `claude`
> *(prompt)*: `"In src/database.py, the get_todo function doesn't handle missing rows — it throws a KeyError. Fix it to return None, add a test for it, and run the test suite before showing me the diff."`

> "Watch the loop run:"
> - GATHER: *"Let me read src/database.py… I see get_todo() indexes dict directly."*
> - PLAN: *"I'll wrap it in a try/except and return None. I'll add test_get_todo_missing to tests/. Then run pytest."*
> - EXECUTE: *"May I edit src/database.py?"* → **y**
> - VERIFY: *"Running pytest… 1 passed."* → *"Now adding the missing-row test."* → **y** → *"2 passed."*

> *(look at camera)* "Notice the prompt I used: I named the **file**, described the **bug**, asked for a **test**, and demanded **verification + a diff**. That's a well-formed task. Claude Code is only as sharp as the instructions you hand it."

---

### [4:30] TWO MODES — NORMAL vs PLAN
*(**Shift+Tab** toggle on screen; table animates in)*

> "You control how *invasive* Claude Code is with two modes, toggled by one shortcut — **Shift+Tab**."

*(table on screen)*
> - **Normal Mode:** reads files; **writes files (with approval)**; **runs commands (with approval)** — built for implementation.
> - **Plan Mode:** reads files; **no writes**; **no commands** — built for safe exploration.

> "This is a superb feature because exploration should never change your code. **Plan Mode is where you explore and propose. Normal Mode is where you execute.**"

---

### [5:20] DEMO — PLAN MODE FIRST
*(Terminal: Shift+Tab toggles to Plan)*

> "Before I let Claude touch my database layer, let me explore in Plan Mode."

> *(prompt)*: `"In plan mode, explore the project and propose a plan to add a 'done' status field to todos, including the migration and which files change."`

> *Claude reads, then:*
> *"Plan: (1) schema.sql — add done BOOLEAN DEFAULT false. (2) database.py — map the field. (3) routes.py — expose it. No files modified in plan mode."*

> "Zero changes. A safe, reviewable approach before I commit to anything. For complex or risky work, **always start in Plan Mode.**"

---

### [6:30] CONTEXT MANAGEMENT — MANAGE IT LIKE FUEL
*(Progress bar analogy: context window fills)*

> "Here's what nobody explains until you hit it: Claude Code can only 'see' what's in its **context window**. As a session runs, that window fills up — and the model gets noticeably less sharp. So you manage context like fuel."

> *(command list on screen, quick visual cuts)*
> - **`/init`** — auto-generates a **CLAUDE.md** from your codebase
> - **`/compact`** — summarizes the conversation to free up space
> - **`/clear`** — clears history, fresh start
> - **`@`** — reference a file or folder (path autocomplete)
> - **`!`** — bash mode; run a shell command, output stays in context
> - **`Alt+v`** — paste a screenshot into the conversation
> - **`y / n`** — accept or reject a proposed change

> "**Habit one:** `/compact` regularly — don't wait until it's full. **Habit two:** `/clear` between *unrelated* tasks. **Habit three:** `@` mention the exact files you care about, instead of letting it wander the whole repo."

---

### [7:45] CLAUDE.md — YOUR FORCE MULTIPLIER
*(Show CLAUDE.md being created)*

> "If you take away one thing from this video, make it this: the **CLAUDE.md** file. It's a plain-text markdown file at the root of your project that Claude Code reads **every single session**. And it's the only file your whole team writes once and benefits from forever."

> *(demo: `claude` → types `/init`, watch it generate)*

> "I can run `/init` and it auto-generates one from the codebase. But the real power is writing it yourself — your build commands, your conventions, your key file roles."

> *(shows file)*
> ```
> # Build
> npm run build
> # Test
> pytest
> # Conventions
> TypeScript strict. Pages in /src/pages. Feature branches only.
> # Review checklist
> Always run tests before committing. Never touch /vendor.
> ```

> "Now every session starts *already knowing your rules.* That's the force multiplier — **write it once, every session benefits.**"

---

### [9:00] PART 1 TAKEAWAYS
> "Recap 101 before we go deeper: **CLAUDE.md is your team resource. Manage context proactively. Fresh starts between tasks. Review every diff — you're the expert. And Plan Mode first for risky work.**"

---

## PART 2 — CLAUDE CODE 201 (CUSTOMIZATION & WORKFLOWS)

### [9:45] CONFIG HIERARCHY — THREE LEVELS
*(Diagram: stack of files)*

> "Now the deeper stuff. `CLAUDE.md` isn't one file — it's a **hierarchy**, and they're **additive** (each layer extends what's below it)."

> - **User level:** `~/.claude/CLAUDE.md` — your personal rules, every project.
> - **Project level:** `yourrepo/CLAUDE.md` — the whole team's conventions.
> - **Directory level:** `yourrepo/src/api/CLAUDE.md` — *lazy-loaded*, only when Claude touches that subtree, to keep context lean.

> "That lazy-loading detail is clever: directory-level instructions load *on demand*, so you get scoped guidance without bloating the context window for unrelated work."

---

### [10:45] PROMPTING WORKFLOWS — REPEATABLE PATTERNS
> "Here's what separates casual users from power users: they don't improvise prompts. They use **repeatable patterns** based on the job:"

> *(cards on screen)*
> - **Explore → Plan → Code → Commit** — best for debugging & refactoring (understand first).
> - **Write Tests → Code → Iterate** — best for TDD & correctness.
> - **Write Code → Screenshot → Iterate** — best for frontend & visual components.
> - **Codebase Q&A** — best for onboarding, docs, understanding.

> "Two tips: **be explicit** about which workflow you want, and **use checkpoints** — break tasks into phases, ask for approval between them, and always make Claude verify its own work."

---

### [12:00] MODELS & EFFORT LEVELS
*(Terminal: `/model`, arrow keys)*

> "Claude Code also lets you **switch models mid-session** with `/model`, and — here's a detail people miss — you can control the **depth of thinking independently** with the arrow keys (`<-` / `->`), regardless of which model you picked."

> *(table)*
> - **OPUS** — most capable → complex coding, agents, multi-step reasoning.
> - **SONNET** — balanced → most dev workflows, reliable & fast. *(the default workhorse)*
> - **HAIKU** — fastest → quick iterations, simple tasks, prototyping.

> "And the effort dial:"
> - **Low** — quick lookups, yes/no, one-liners.
> - **Medium** — features, bug fixes, explanations *(the default)*.
> - **High / Max** — architecture, complex debugging, security audits, critical decisions.

> "Match the model and effort to the task — don't pay OPUS prices for a HAIKU question."

---

### [13:10] SKILLS — PACKAGED EXPERTISE
*(Show `.claude/skills/` folder)*

> "Finally in 201: **Skills** — packaged expertise that gives Claude Code knowledge it doesn't have on its own."

> "Anatomy: a skill has **YAML metadata** (frontmatter), **markdown instructions**, and optionally **bundled scripts or assets**. Only the metadata is pre-loaded; the full content loads on demand, so it stays context-cheap."

> "Invocation is flexible — Claude can trigger a skill **automatically** when your task matches its description, or you can call it **manually** with `/skillname`. And for skills you need everywhere, drop them in `~/.claude/skills/` (global)."

> *(demo if quick):* `"In skill mode, run my /git-best-practices skill and check this branch."`

---

### [14:10] PART 2 TAKEAWAYS
> "201 recap: **config is a three-level additive hierarchy. Use repeatable prompt workflows. Match model + effort to the task. Package reusable expertise as skills.**"

---

## PART 3 — CLAUDE CODE 301 (HOOKS & SUBAGENTS)

### [14:50] HOOKS — DETERMINISTIC AUTOMATION
*(Show `.claude/settings.json`)*

> "Now we get genuinely advanced. **Hooks** are shell commands that run automatically at lifecycle events. The key word: **deterministic.** They fire *every time, on every action* — no reliance on Claude's judgment. If you want something guaranteed, a hook does it."

> "The **events**: `PrePromptSubmit`, `PostCompact`, `PreToolUse`, `PostToolUse`. And **matchers** narrow a hook to specific tools: `Edit`, `Write`, `Bash`, `Read` — combinable like `Edit|Write`."

> *(JSON on screen)*
> ```json
> {
>   "hooks": [
>     { "matcher": "Edit|Write", "type": "command", "command": "npm run lint" }
>   ]
> }
> ```

> "Here's the priority hierarchy, most specific wins:"
> 1. **Local:** `.claude/settings.local.json` (overrides team)
> 2. **Team:** `.claude/settings.json` (overrides global)
> 3. **Global:** `~/.claude/settings.json`

---

### [15:50] THE 5 HOOK PATTERNS
> "Five things people automate with hooks:"
> 1. **Get notified** — on `UserPromptSubmit`.
> 2. **Auto-format** — on `PreToolUse`.
> 3. **Re-inject context** — on `PostCompact`.
> 4. **Block edits** — on `PreToolUse`, matcher `Edit|Write` — exit with a **non-zero code to reject** the action.
> 5. **Audit changes** — on `PostToolUse`, matcher `Edit|Write`.

> "The hook options: `matcher` (which tool), `type` (always `command`), `command` (the shell command), and `async` (true = non-blocking)."

> *(quick demo):* "Here's a real hook: every time Claude edits a file, auto-run `pytest`. That's seconds of effort that saves me from ever shipping broken code."

---

### [17:00] SUBAGENTS — ORCHESTRATION
> *(Diagram: Main convo spawning workers)*

> "Now the big one — **subagents.** Claude Code lets you spin off focused, isolated workers. Each custom agent is defined by **six properties** — give them a quick beat:"

> - **name** (unique id) · **description** (when to suggest it) · **system prompt** (role)
> - **tools** (permission boundary) · **model** (capability vs speed) · **location** (project or user scope)

> "And **agent memory** — persistent, file-based learning. Three scopes: **Project** (in `.claude/`, shared via git), **User** (in `~/.claude/`, personal across projects), and **None** (stateless, fresh every time)."

---

### [17:50] THE 4 ORCHESTRATION PATTERNS
> "When you have subagents, you orchestrate them. Four patterns worth memorizing:"

> *(animated diagram for each)*
> 1. **Actor-Critic** — Write → Review → Approve. *Best for code review loops.* *(demo: one agent writes, another critiques.)*
> 2. **Map-Reduce** — Split → Agents A/B/C → Merge. *Best for large refactors, parallel file exploration.*
> 3. **Research Scout** — Task → Explore → Report. *Best for codebase exploration, API research.*
> 4. **Pipeline** — Stage 1 → Stage 2 → Stage 3. *Best for sequential chains.*

> *(demo)*: "Here's Actor-Critic in practice — I ask one subagent to write a refactor, a second to review it, and only if it approves do I merge. That's a code review loop on autopilot."

---

### [18:50] MAIN CONVERSATION vs SUBAGENTS
> *(Two-column table)*

> "Knowing *what* to delegate is the real skill. **Keep in the main conversation:** frequent back-and-forth, phases that share context, quick targeted changes. **Delegate to a subagent:** enforcing tool restrictions, verbose output you don't need, self-contained tasks that return only a summary."

> "Use this **3-question framework** — if all three answers are 'no,' keep it in the main conversation:"
> 1. Is there a **clear role?** (defined success criteria) → subagent
> 2. Do I **only need conclusions?** (don't need the process) → subagent
> 3. Is the **context crowded?** (offload heavy reads) → subagent

---

### [19:50] 301 COMMANDS & TAKEAWAYS
> "Commands to remember: **`/hooks`** configures hooks interactively. **`/agents`** lists, creates, edits, or deletes agents. **`/clear`** resets and picks up new hooks. **`Ctrl+B`** backgrounds a running subagent so you keep working. **`Esc`** exits those UIs."

> "301 recap: **hooks are deterministic — they always fire. Matchers narrow them to specific tools. Three config files merge. Agents have six properties. Memory is Project/User/None. And the three-question framework decides what to delegate.**"

---

### [20:45] OUTRO / CTA
*(Camera, warm close)*

> "So that's the full arc: you learned the **fundamentals** — the task cycle, the two modes, context management, and CLAUDE.md. Then **customization** — the config hierarchy, repeatable workflows, model and effort dials, and skills. And finally the **advanced layer** — deterministic hooks and orchestrating subagents."

> "The takeaway that ties it all together: Claude Code is a **force multiplier**, but only when *you* stay in control — Plan Mode first, review every diff, prove the work, and delegate thoughtfully."

> "If this guide helped you, **follow Abdul Qaadir** for more AI engineering — and comment below: which part are you going to try first, hooks or subagents? **Like and share** this with a developer who's still worried AI will write bad code."

> *(End card: subscribe + links)*

---

## 🧰 THE RUNNING EXAMPLE (for b-roll / screens)
Building a small **Python to-do list API** in `~/projects/todo-api`:
- `src/database.py` — storage (broken `get_todo` → the 101 demo)
- `src/routes.py` — API endpoints
- `schema.sql` — the 'done' field migration (the Plan Mode demo)
- `.claude/CLAUDE.md` — the force-multiplier example
- `.claude/settings.json` — the auto-`pytest` hook example
- `.claude/skills/` — the skill demo folder

One project, every concept visualized with a real, honest terminal run.