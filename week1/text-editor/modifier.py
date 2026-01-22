class Modifier():
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
