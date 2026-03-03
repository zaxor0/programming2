#!/usr/bin/python3

from abc import ABC, abstractmethod

## INTERFACE 
class Cmd(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# undoable is too ambiguous it could mean something that is able to be "undone" but it can mean not possible to do
# instead I am using revertable, because you can revert the change, and this gets rid of the "un" which often implis opposite or not.
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

    print(editor)
    # user actions
    set_text = SetTextCmd(editor, history, "Intro")
    set_text.execute()

    print(editor)

    # user actions
    set_contrast = SetContrastCmd(editor, history, 0.8)
    set_contrast.execute()

    print(editor)

    # user actions
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
