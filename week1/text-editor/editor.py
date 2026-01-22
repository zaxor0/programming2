from modifier import Modifier
from current_state import CurrentState

class Editor():
    def __init__(self):
        # public variables
        self.current_state = CurrentState('')
        # private variables
        self.__stack = Modifier()

    def __str__(self):
        return f"{self.current_state}"

    ## PRIVATE METHODS
    def __save_latest(self):
        # push that last state on the stack
        self.__stack.push(self.current_state)

    def __get_last_state(self):
        last_state = ''
        if self.__stack.size() > 0:
            last_state = str(self.__stack.peek())
        return last_state

    def __update_current(self, s:str):
        # create a string for the new object
        new_content = self.__get_last_state() + s
        # create a new object for the stack
        self.current_state = CurrentState(new_content)

    def __erase_characters(self, n:int):
        # create a string based on a subset of characters from the current state
        new_content = str(self.current_state)[:-n]
        # update current state
        self.current_state = CurrentState(new_content)

    def __roll_back(self):
        if self.__stack.size() > 0:
            self.current_state = self.__stack.pop()

    def __print_stack(self):
        print(self.__stack)

    ## PUBLIC METHODS ##
    def insert(self, s: str):
        # add the most recent state to the stack
        self.__save_latest()
        # update the current state with user entered string
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
