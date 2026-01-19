- Build a small text editor that supports multiple changes and multi-level undo [without exposing internal state]

- Class Editor Should support:
    - insert(text: str)
    - delete_last(n: int)
    - undo()
        - Undo is multi-level (undo repeatedly returns step-by-step)
        - If there is nothing to undo, do nothing or raise a clear exception (your choice)
    - __str__() to print current content

- Hint: save a “snapshot” of the editor before each modifying operation, and store snapshots in a stack-like history
