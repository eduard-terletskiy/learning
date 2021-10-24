class LinkedList:
    def __init__(self):
        self.begin = None

    def insert(self, x):
        self.begin = [x, self.begin]

    def pop(self):
        if self.begin is None:
            return "list Empty"
        x = self.begin[0]
        self.begin = self.begin[1]
        return x

    def __repr__(self):
        return f"{self.begin}"


a = LinkedList()
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(10)
print(a.pop())
print(a.pop())
print(a.pop())
print(a)
