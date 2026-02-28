# Undo Feature for a Text Editor

Data structure: Stack

This small project implements a simple text editor that records operations on a stack so the most recent operations can be undone.

Features
- `append(text)` — append text to the end
- `delete(k)` — delete last `k` characters
- `undo()` — revert the last operation (append or delete)

Quick start

Install dev dependency and run tests:

```bash
pip install -r requirements.txt
python -m pytest -q
```

Interactive demo

```bash
python src/undo_editor.py
# then use commands: a <text>, d <n>, u (undo), q (quit)
```
