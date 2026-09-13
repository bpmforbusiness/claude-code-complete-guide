"""Todo storage layer for the Claude Code demo project.

NOTE: `get_todo()` deliberately throws a KeyError when the row is missing.
This is the intentional bug used in the video's first live demo (the
GATHER -> PLAN -> EXECUTE -> VERIFY cycle). Do NOT fix it before filming.
"""
from typing import Optional


class TodoStore:
    """A minimal dict-backed in-memory todo store."""

    def __init__(self) -> None:
        # id -> {"id": int, "task": str, "done": bool}
        self._todos: dict[int, dict] = {}
        self._next_id = 1

    def create(self, task: str) -> dict:
        """Create a new todo and return it."""
        row = {"id": self._next_id, "task": task, "done": False}
        self._todos[self._next_id] = row
        self._next_id += 1
        return row

    def list(self) -> list[dict]:
        """Return all todos in insertion order."""
        return list(self._todos.values())

    def get_todo(self, todo_id: int) -> Optional[dict]:
        """Return a single todo by id, or None if it does not exist.

        BUG (intentional, for the video demo): indexes the dict directly,
        so a missing id raises KeyError instead of returning None.
        """
        return self._todos[todo_id]

    def mark_done(self, todo_id: int, done: bool = True) -> Optional[dict]:
        row = self.get_todo(todo_id)
        if row is None:
            return None
        row["done"] = done
        return row