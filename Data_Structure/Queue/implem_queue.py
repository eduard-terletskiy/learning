
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue == []:
            return "queue is empty"
        return self.queue.pop(0)

    def __str__(self):
        return (f'{self.queue}')


q = Queue()
print(q)
print(q.pop())
q.push(8)
print(q)
q.push(9)
print(q)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q)
print(q.pop())
print(q)
print(q.pop())
print(q)

que = Queue()
print(que)
print(que.pop())
que.push(134123412)
print(que)
print(q)
