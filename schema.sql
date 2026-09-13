-- Todo table schema for the demo project.
-- The `done` column is the subject of the Plan-Mode migration demo.
-- Use sqlite:  sqlite3 todos.db < schema.sql

CREATE TABLE todos (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT    NOT NULL,
    done BOOLEAN NOT NULL DEFAULT false
);