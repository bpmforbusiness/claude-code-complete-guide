# CLAUDE.md — Todo API (demo/sample for the Claude Code video)

This file is an EXAMPLE of the "force multiplier" concept shown in the tutorial.
In your real projects, keep this honest and project-specific.

## Build & Run
- Install: `pip install -e .` (or `uv sync`)
- Start API: `uvicorn src.routes:app --reload`

## Test
- Run tests: `pytest`
- Run a single file: `pytest tests/test_database.py`

## Conventions
- Python 3.11+, type annotations on all public functions.
- No external DB for the in-memory store — keep it dict-backed.
- `get_todo()` returns `None` for a missing id (see #1 — currently BUGGY).
- Never modify `schema.sql` without a migration plan.

## Key Files & Roles
- `src/database.py` — storage layer (the bug lives here)
- `src/routes.py` — API endpoints
- `tests/test_database.py` — test suite
- `schema.sql` — singe-table schema (additive migrations only)

## Review Checklist (always run before committing)
- [ ] `pytest` passes
- [ ] Diff reviewed for scope creep
- [ ] No debug prints left behind