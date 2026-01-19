from modifier import Modifier
from current_state import CurrentState

class Editor():
    def __init__(self):
        # public variables
        self.current_state = CurrentState()
        self.last_state = ''
        # private stack
        self.__stack = Modifier()

    def __str__(self):
        info = f"{self.current_state}" #\t\t  {self.last_state}"
        return info

    def insert(self, s: str):
        # preserve the last state
        self.last_state = self.current_state
        # push onto stack
        top = self.__stack.peak() if self.__stack.size() > 0 else ''
        new = top + s
        self.__stack.push(new)
        # update current state
        self.current_state = self.__stack.peak()

    def delete_last(self, n: int):
        self.last_state = self.current_state
        older_position = -(n + 1)
        latest = self.__stack.stack[older_position]
        self.__stack.push(latest)
        # update current state
        self.current_state = self.__stack.peak()

    def undo(self):
        try:
            self.last_state = self.__stack.pop()
            self.current_state = self.__stack.peak()
        except:
            raise IndexError("No more changes to undo")
