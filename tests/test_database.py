"""Tests for the Todo store.

This test suite passes as-is but deliberately does NOT cover the missing-row
case in get_todo(). During the video's first live demo, Claude Code adds a
test for that exact bug: test_get_todo_missing -> expects None.
"""
import pytest

from src.database import TodoStore


def test_create_returns_task():
    store = TodoStore()
    row = store.create("Write the demo")
    assert row["task"] == "Write the demo"
    assert row["done"] is False


def test_list_returns_insertion_order():
    store = TodoStore()
    store.create("first")
    store.create("second")
    todos = store.list()
    assert [t["task"] for t in todos] == ["first", "second"]


def test_get_todo_existing_row():
    store = TodoStore()
    row = store.create("exists")
    assert store.get_todo(row["id"]) == row


def test_mark_done():
    store = TodoStore()
    row = store.create("flip me")
    updated = store.mark_done(row["id"], True)
    assert updated["done"] is True