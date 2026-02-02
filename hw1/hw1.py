#!/usr/bin/python3

# the memento, the class that stores the state of the originator (document)
class DocumentState:
    # new attributes to documents need to added to this class as well as the Document class
    def __init__(self, content:str, font_name:str, font_size:int) -> None:
        self.content = content
        self.font_name = font_name
        self.font_size = font_size

# the caretaker, history of changes made in the document, basically a stack
class History:
    def __init__(self) -> None:
        self.stack = []

    # stack methods
    def push(self, s: str) -> None:
        self.stack.append(s)

    def pop(self) -> DocumentState:
        last = self.stack.pop()
        return last

    def peek(self) -> DocumentState:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

# the originator
class Document:
    # new attributes need to be added to __init__, _create_state, and _load_state_from_history
    # as welll as to the DocumentState class
    def __init__(self) -> None:
        self._content = ""
        self._font_name = "Times"
        self._font_size = 12
        self._history = History()

    # private methods
    def _create_state(self) -> DocumentState:
        return DocumentState(self._content, self._font_name, self._font_size)

    def _load_state_from_history(self, state: DocumentState) -> None:
        self._content = state.content
        self._font_name = state.font_name
        self._font_size = state.font_size

    def _save_history_before_change(self) -> None:
        self._history.push(self._create_state())

    # public methods
    def insert(self, text: str) -> None:
        self._save_history_before_change()
        self._content += text
    
    def set_font_type(self, f:str) -> None:
        if f not in [ 'Times', 'Arial', 'Courier', 'Wingdings' ]:
            raise ValueError(f"{f} is not an available font")
        self._save_history_before_change()
        self._font_name = f

    def set_font_size(self, n) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        self._save_history_before_change()
        self._font_size = n

    def delete_last(self, n) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        self._save_history_before_change()
        self.content = self.content[:-n] if n <= len(self._content) else ""

    def undo(self)-> None:
        print("# Undo action called!")
        if self._history.size() > 0:
            prev = self._history.pop()
            self._load_state_from_history(prev)

    def __str__(self) -> str:
        doc_details = f"[ Font: {self._font_name} | Size: {self._font_size} ]\n{self._content}\n"
        return doc_details


def main():
    new_doc = Document()
    new_doc.insert("Hello")
    print(new_doc)   
    new_doc.set_font_size(13)
    print(new_doc)   
    new_doc.set_font_size(14)
    print(new_doc)   
    new_doc.set_font_type("Arial")
    print(new_doc)   
    new_doc.set_font_type("Courier")
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.insert(" World!")
    print(new_doc)   
    new_doc.insert("!!")
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   
    new_doc.undo()
    print(new_doc)   

if __name__ == "__main__":
    main()
