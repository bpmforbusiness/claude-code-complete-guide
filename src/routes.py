"""API routes for the Todo service (minimal FastAPI-style layer).

This file is intentionally lightweight — it exists so the repo feels real
and gives Claude Code a few files to read during the demo. The interesting
logic lives in src/database.py.
"""
from typing import Optional

from src.database import TodoStore


class TodoAPI:
    def __init__(self) -> None:
        self.store = TodoStore()

    def create(self, body: dict) -> dict:
        task = body.get("task")
        if not task:
            raise ValueError("task is required")
        return self.store.create(task)

    def list(self) -> list[dict]:
        return self.store.list()

    def get(self, todo_id: int) -> Optional[dict]:
        return self.store.get_todo(todo_id)

    def set_done(self, todo_id: int, done: bool = True) -> Optional[dict]:
        return self.store.mark_done(todo_id, done)