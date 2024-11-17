class Stack():
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return True if len(self.stack) == 0 else False
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return None if self.is_empty() else self.stack.pop()
    def peek(self):
        return None if self.is_empty() else self.stack[-1]
    def size(self):
        return len(self.stack)