class Stack(list):
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        # return str(list(reversed(self.data)))
        return f'[{", ".join(self.data[::-1])}]'

s = Stack()
print(s.is_empty())
s.push('a')
s.push('b')
s.push('c')
print(s.is_empty())
print(s.top())
print(s)