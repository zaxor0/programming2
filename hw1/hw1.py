#!/usr/bin/python3

# the memento, the class that stores the state of the originator (document)
class DocumentState:
    def __init__(self, content:str, font_name:str, font_size:int) -> None:
        self.content = content
        self.font_name = font_name
        self.font_size = font_size

# the caretaker, history of changes made in the document, basically a stack
class History:
    def __init__(self):
        self.stack = []

    # debugging method
    def __str__(self):
        history = ''
        for text in self.stack:
            history += str(text) + ' | '
        return history

    def push(self, s: str):
        self.stack.append(s)

    def pop(self):
        last = self.stack.pop()
        return last

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# the originator
class Document:
    def __init__(self) -> None:
        self._content = ""
        self._font_name = "default font"
        self._font_size = 12
        self._history = History()

    # private methods
    def _create_state(self) -> DocumentState:
        return DocumentState(self._content, self.font_name, self.font_size)

    def _load_state_from_history(self, state: DocumentState) -> None:
        self._content = state.content
        self._font_name = state.font_name
        self._font_size = state.font_size

    def _save_history_before_change(self) -> None:
        self.history.push(self._create_state())

    # public methods
    def insert(self, text: str) -> None:
        self._save_history_before_change()
        self.content += text

    def delete_last(self, n) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        self._save_history_before_change()
        self.content = self.content[:-n] if n <= len(self._content) else ""

    def undo(self)-> None:
        prev = self._history.pop()
        if prev is None:
            return
        self._set_content_from_history(prev)

    def __str__(self) -> str:
        return self._content


def main():
    print("Welcome")

if __name__ == "__main__":
    main()
