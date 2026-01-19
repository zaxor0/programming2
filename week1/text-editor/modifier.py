class Modifier():
    def __init__(self):
        self.stack = []

    def push(self, s: str):
        self.stack.append(s)

    def pop(self):
        last = self.stack.pop()
        return last

    def peak(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
