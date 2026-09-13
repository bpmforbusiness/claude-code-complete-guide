# 🎥 SHOOT KIT — How to Make the Claude Code Video
**This is your instructions file. Follow it in order. Everything below = exactly what to do while recording.**

---

## STEP 0 — PREP (do this before you hit record)

### 0.1 Build the demo project (one time, ~20 min)
Create `~/projects/todo-api` with these files so every terminal demo is real:
- `src/database.py` — a small dict-backed todo store, but make `get_todo()` throw a `KeyError` when the row is missing (this becomes the 101 bug demo — do NOT fix it yet).
- `src/routes.py` — 2–3 read endpoints (not strictly used but makes the repo feel real).
- `schema.sql` — a `todos` table with `id`, `task`, `done BOOLEAN DEFAULT false` (this is the Plan Mode migration demo).
- `tests/test_database.py` — a passing test that does NOT cover the missing-row case (so you can add it in the demo).

Commit this as a clean starting point.

### 0.2 Install / verify Claude Code
```bash
claude --version      # newest version
```
Have the `claude` CLI working in that repo before recording.

### 0.3 Test the three live demos ONCE (off-camera)
These MUST work exactly as scripted before you film:
1. **Get context demo** — the missing-row fix (GATHER→PLAN→EXECUTE→VERIFY).
2. **Plan Mode demo** — the `done` field migration, showing zero file changes.
3. **Hooks demo** — the auto-`pytest` on `Edit|Write`.

> If any demo is slow or flaky, pre-warm the model with a trivial prompt first, or rebuild it off-screen. **Never film a demo you haven't rehearsed.**

---

## STEP 1 — SETUP (the shots)
1. Open the repo: `cd ~/projects/todo-api`
2. Terminal theme: **dark**, large font, high contrast. Make the prompt and any `claude` output clearly readable.
3. Camera: you + a mid/wide shot showing the terminal beside you (or full-screen terminal with a small inset camera — pick one, stay consistent).
4. Record the **HOOK b-roll first**: terminal filling with output + you looking at a "blank page." Film at 2× your footage need (it's the cold open).
5. Keep a **teleprompter** of the narration only (the `<SHOOT KIT>` blocks below). The `<TERMINAL>` blocks are screen actions, not things to say.

---

## STEP 2 — FILM ORDER (batches; the script timestamps are your guide)

### BATCH A — PART 1 (FUNDAMENTALS) · ~9 min
| # | Filming note | Terminal action |
|---|---|---|
| A1 | Camera, cold-open hook (vs. script [0:00]) | b-roll only |
| A2 | Camera + terminal: intro Claude Code, start session | `cd ~/projects/todo-api && claude` |
| A3 | Voice-over over the animated **task-cycle loop** graphic | none (graphic on screen) |
| A4 | **LIVE DEMO 1** — the missing-row fix (vs. script [3:00]) | paste the prompt, type `y`, show test pass |
| A5 | Shift+Tab demo — Normal vs Plan (vs. [4:30]) | press Shift+Tab on camera |
| A6 | **LIVE DEMO 2** — Plan Mode migration (vs. [5:20]) | paste the plan prompt, show "no files modified" |
| A7 | Context commands on screen (vs. [6:30]) | overlay list |
| A8 | **LIVE DEMO 3** — `/init` generating CLAUDE.md (vs. [7:45]) | run `/init`; then `cat CLAUDE.md` |

**Checkpoint:** replay A4, A6, A8 — they must show REAL, honest output (green test, "no files modified," a real generated CLAUDE.md). No faked wins.

### BATCH B — PART 2 (CUSTOMIZATION) · ~5 min
| # | Filming note | Terminal / graphic |
|---|---|---|
| B1 | Camera: config hierarchy (vs. [9:45]) | 3-level diagram graphic |
| B2 | **LIVE DEMO 4** — View your project CLAUDE.md | `cat CLAUDE.md` / open in editor |
| B3 | Camera: prompt workflows (vs. [10:45]) | 4-pattern cards graphic |
| B4 | Terminal: `/model` + arrow keys (vs. [12:00]) | run `/model`, press `<-` / `->` |
| B5 | Camera: models/effort table (vs. [12:00]) | table graphic |
| B6 | Terminal: show `.claude/skills/` (vs. [13:10]) | `ls .claude/skills/` + open one skill's frontmatter |

### BATCH C — PART 3 (HOOKS & SUBAGENTS) · ~6 min
| # | Filming note | Terminal / graphic |
|---|---|---|
| C1 | Terminal: show settings.json hook (vs. [14:50]) | open `.claude/settings.json` with the pytest hook |
| C2 | **LIVE DEMO 5** — the auto-pytest hook (vs. [15:50]) | make a fake edit → show it auto-runs pytest |
| C3 | Camera: 5 hook patterns (vs. [15:50]) | 5-card graphic |
| C4 | Camera: subagent anatomy + memory (vs. [17:00]) | 6-property diagram |
| C5 | **LIVE DEMO 6 (if time)** — Actor-Critic: writer agent → reviewer agent | `/agents` or subagent orchestration |
| C6 | Camera: 3-question framework (vs. [18:50]) | framework graphic |

### BATCH D — OUTRO · ~1 min
| # | Filming note |
|---|---|
| D1 | Camera, warm close, recap + CTA (vs. [20:45]) |

---

## STEP 3 — POST-PRODUCTION
1. **Edits:** cut long terminal waits (trim pauses inside the loop; keep beats visible). Add the animated **GATHER→PLAN→EXECUTE→VERIFY** loop as your recurring transition between every part — it's your visual signature.
2. **Captions:** on for every prompt you type and every tool output. This is a tutorial; captions are non-negotiable.
3. **Zoom:** punch-in on the terminal whenever you type a command or show an approve prompt (`y`/`n`).
4. **B-roll pack:** the 4-PATTERN diagrams, the 3-LEVEL config stack, the 5-HOOK cards, the models/effort table — pre-render these as clean slides and drop them in at the marked timestamps.
5. **Color/audio:** consistent levels; clean up breaths; one mix.

---

## STEP 4 — PUBLISH KIT (draft this after editing)
- **Title options:**
  1. "Claude Code Complete Guide: Fundamentals → Hooks → Subagents"
  2. "Claude Code Power User in 20 Minutes (with real examples)"
- **Description:** hook line + timestamp chapters (from the script timestamps) + your follow/like/share CTA + links.
- **Thumbnail concept:** split — you on one side, a terminal with GATHER→PLAN→EXECUTE→VERIFY loop, big text "COMPLETE GUIDE."
- **Tags:** Claude Code, AI coding, Anthropic, AI agent, pair programming, terminal AI.

---

## ✅ FINAL CHECKLIST (before upload)
- [ ] Live demos are real + honest (green tests, real output, no fakes)
- [ ] The running to-do-API example is used in EVERY part
- [ ] Captions on every prompt + output
- [ ] Loop-animation repeated as a transition (visual signature)
- [ ] CTA + links in the last 30 seconds
- [ ] Title/desc/thumbnail/tags from STEP 4