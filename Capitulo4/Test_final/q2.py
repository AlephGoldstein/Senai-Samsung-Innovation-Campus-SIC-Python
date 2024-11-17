from stacks import Stack
stack = Stack()
items = [10 * i for i in range(1, 10)]
for item in items:
    stack.push(item)
    if (item // 10) % 2 == 0:
        stack.pop()
print(stack.stack)