# Claude Code — Complete Guide (Video Kit)

Everything you need to film, edit, and publish the **"Claude Code Complete Guide: Fundamentals → Hooks → Subagents"** YouTube video.

Built by **Abdul Qaadir** (@TechWorldWithAbdul) · 30 Labs, 30 Days series.

---

## 📁 What's in this repo

| Path | What it is |
|---|---|
| `todo-api/` playground | The **demo project** used in every on-screen example (Python to-do API) |
| `docs/video-script/SCRIPT.md` | Full **narration script** (~21 min), parts 101 / 201 / 301 |
| `docs/shoot-kit/SHOOT_KIT.md` | **Instructions file** — prep, filming batches A–D, post-production, checklist |
| `docs/slides/` | 7 clean **diagram slides** (SVG + PNG): task-cycle loop, config hierarchy, 5 hook patterns, models/effort, prompt workflows, subagent anatomy, 3-question framework |
| `docs/publish-kit/PUBLISH_KIT.md` | Title, description + chapters, thumbnail concept, tags, broadcast CTA |
| `schema.sql`, `pyproject.toml` | Demo app scaffolding |

## 🎓 The 6 live demos
1. **Missing-row bug fix** → shows GATHER→PLAN→EXECUTE→VERIFY (the `get_todo` bug is left unfixed on purpose)
2. **Plan Mode migration** → zero file changes in explore mode
3. **`/init`** → auto-generates `CLAUDE.md`
4. **`/model` + arrow-key effort dial**
5. **Auto-`pytest` hook** on `Edit|Write`
6. **Actor-Critic subagent** orchestration (if time)

## 📐 Concepts covered
- **101:** task cycle · Normal vs Plan mode · context commands · `CLAUDE.md`
- **201:** config hierarchy · 4 prompt workflows · models + effort · skills
- **301:** hooks (5 patterns, deterministic) · subagents (6 properties, memory, 4 orchestration patterns) · 3-question delegation framework

---

## 🚀 Quickstart (film it)
1. Read `docs/shoot-kit/SHOOT_KIT.md` first.
2. `cd todo-api && python -m venv .venv && .venv/bin/pip install pytest && .venv/bin/python -m pytest` → expect **4 passed** (missing-row case uncovered = ready to film).
3. Follow filming batches A → D. Use `docs/slides/` for your b-roll graphics.
4. Publish with `docs/publish-kit/PUBLISH_KIT.md`.

> The known `get_todo()` bug stays in `src/database.py` on purpose — it's the hook for the first live demo. Do not fix it before filming.