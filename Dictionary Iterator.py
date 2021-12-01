from collections import deque


class dictionary_iter:
    def __init__(self, d):
        self.d = d
        self.keys = deque(self.d.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) == 0:
            raise StopIteration
        key = self.keys.popleft()
        value = self.d[key]
        return key, value


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)