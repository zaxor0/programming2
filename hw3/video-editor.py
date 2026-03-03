#!/usr/bin/python3
from abc import ABC, abstractmethod

## ANSWERS
"""
1. What is the key idea of your chosen pattern?
- I like the command pattern because the commands or actions are extensible. Specifically, we could add logging for each exection. We could also add a queue mechanism, something like at timestamp X add text "title screen."
- Compared to memento from HW1, it creates a system for commands that could be applied to other targets, like a document or photo. This overall is just moreusable.

2. Why is it a better fit here than the other pattern?
- In memento, the originator was a complicated object with many methods, Command Pattern lets us simplify that object. 
- 


3. What is the main tradeoff of your choice?

"""


## INTERFACE 
class Cmd(ABC):
    @abstractmethod
    def execute(self) -> None:
        """execute the command"""
        pass

# I find "undoable" is somewhat ambiguous as it could mean something that is able to be "undone" but it can also mean not possible to do
# Instead I am using revertable, because you can revert the change; by removing the "un" prefix it removes the "negative" implication of undo.
class RevertableCmd(Cmd):
    @abstractmethod
    def unexecute(self) -> None:
        """Undo the effect of execute()."""
        pass

## RECIEVER 
class VideoEditor:
    def __init__(self) -> None:
        self._contrast = 0.5
        self._text = ""

    def set_text(self, text: str) -> None:
        self._text = text

    def remove_text(self) -> None:
        self._text = ""

    def get_contrast(self) -> float:
        return self._contrast

    def set_contrast(self, contrast: float) -> None:
        self._contrast = contrast

    def __str__(self) -> str:
        return f"VideoEditor(contrast={self._contrast}, text={self._text!r})"

## HISTORY STACK 
class History:
    def __init__(self) -> None:
        self._commands: list[RevertableCmd] = []

    def push(self, cmd: RevertableCmd) -> None:
        self._commands.append(cmd)

    def pop(self) -> RevertableCmd:
        return self._commands.pop()

    def __len__(self) -> int:
        return len(self._commands)


## CONCRETE COMMANDS 

class SetTextCmd(RevertableCmd):
    def __init__(self, editor: VideoEditor, history: History, new_text: str) -> None:
        self._editor = editor
        self._history = history
        self._payload = new_text
        self._prev_text = ""

    def execute(self) -> None:
        self._prev_text = self._editor._text
        self._editor.set_text(self._payload)
        self._history.push(self)
 
    def unexecute(self) -> None:
        self._editor._text = self._prev_text
        
class SetContrastCmd(RevertableCmd):
    def __init__(self, editor: VideoEditor, history: History, new_contrast: float) -> None:
        self._editor = editor
        self._history = history
        self._payload = new_contrast
        self._prev_contrast = None 

    def execute(self) -> None:
        self._prev_contrast = self._editor._contrast
        self._editor.set_contrast(self._payload)
        self._history.push(self)
 
    def unexecute(self) -> None:
        self._editor._contrast = self._prev_contrast

class RemoveTextCmd(RevertableCmd):
    def __init__(self, editor: VideoEditor, history: History) -> None:
        self._editor = editor
        self._history = history
        self._prev_text = ""

    def execute(self) -> None:
        self._prev_text = self._editor._text
        self._editor.remove_text()
        self._history.push(self)
 
    def unexecute(self) -> None:
        self._editor._text = self._prev_text

# you dont want to undo the undo, so its not a revertable command
class UndoCmd(Cmd):
    def __init__(self, history: History) -> None:
        self._history = history

    def execute(self) -> None:
        if len(self._history) > 0:
            self._history.pop().unexecute()


## CLIENT CODE 
def main():
    editor = VideoEditor()
    history = History()
    print(f"Intital State:\n{editor}\n")

    # user actions
    set_text = SetTextCmd(editor, history, "Intro")
    set_text.execute()
    print(editor)

    set_contrast = SetContrastCmd(editor, history, 0.8)
    set_contrast.execute()
    print(editor)

    remove_text = RemoveTextCmd(editor, history)
    remove_text.execute()
    print(editor)

    undo = UndoCmd(history)
    undo.execute()
    print(editor)

    undo.execute()
    print(editor)

    undo.execute()
    print(editor)

    undo.execute()
    print(editor)



if __name__ == "__main__":
    main()
