class Stack:
    def __init__(self):
        self.stack = list()

    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            return
        return self.stack.pop()
    def top(self):
        if self.isEmpty():
            return
        return self.stack[-1]
