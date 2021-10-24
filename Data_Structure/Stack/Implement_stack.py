
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def __str__(self):
        return f'{self.stack}'


stack = Stack()
stack_1 = Stack()
stack.push('1')
stack_1.push('2')
stack.push('3')
stack_1.push('4')
stack.push('5')
stack_1.push('6')

print('''stack: {}, 
stack_1: {}'''.format(stack, stack_1))


stack.pop()
stack_1.pop()
stack.pop()
stack_1.pop()
print('''stack: {}, 
stack_1: {}'''.format(stack, stack_1))
