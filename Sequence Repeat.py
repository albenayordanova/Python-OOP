class sequence_repeat:
    def __init__(self, text, count):
        self.text = text
        self.count = count
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        # result = self.text[self.idx]
        result = self.text[self.idx % len(self.text)] ###
        self.idx += 1
        self.count -= 1
        # if self.idx == len(self.text):
        #     self.idx = 0
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')