from modifier import Modifier
from current_state import CurrentState

class Editor():
    def __init__(self):
        self.current_state = CurrentState('')
        self._stack = Modifier()

    def __str__(self):
        return f"{self.current_state}"

    ## PRIVATE METHODS
    def _save_latest(self):
        # push that last state on the stack
        self.__stack.push(self.current_state)

    def _get_last_state(self):
        last_state = ''
        if self.__stack.size() > 0:
            last_state = str(self.__stack.peek())
        return last_state

    def _update_current(self, s:str):
        new_content = self.__get_last_state() + s
        self.current_state = CurrentState(new_content)

    def _erase_characters(self, n:int):
        new_content = str(self.current_state)[:-n]
        self.current_state = CurrentState(new_content)

    def _roll_back(self):
        if self.__stack.size() > 0:
            self.current_state = self.__stack.pop()

    def _print_stack(self):
        print(self.__stack)

    ## PUBLIC METHODS ##
    def insert(self, s: str):
        self.__save_latest()
        self.__update_current(s)

    def delete_last(self, n: int):
        # add the most recent state to the stack
        self.__save_latest()
        # revert to a previously state
        self.__erase_characters(n)

    def print_history(self):
        self.__print_stack()

    def undo(self):
        self.__roll_back()
