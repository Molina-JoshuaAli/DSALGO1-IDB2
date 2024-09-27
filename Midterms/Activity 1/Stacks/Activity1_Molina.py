class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)  # Fixed: Changed self-stack to self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "The stack is empty"

    def current_items(self):
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "The stack is empty"


stack = Stack()

#Table code
stack.push(5)
print("Current stack: " + str(stack.current_items()))
stack.push(3)
print("Current stack: " + str(stack.current_items()))
print(f"Current size: {stack.size()}")
print(f"Popped value: {stack.pop()}")
print(f"Is stack empty? {stack.is_empty()}")
print(f"Popped value: {stack.pop()}")
print(f"Is stack empty? {stack.is_empty()}")
print(f"Popped value: {stack.pop()}")
stack.push(7)
print("Current stack: " + str(stack.current_items()))
stack.push(9)
print("Current stack: " + str(stack.current_items()))
print(f"Top value: {stack.top()}")
stack.push(4)
print("Current stack: " + str(stack.current_items()))
print(f"Current size: {stack.size()}")
print(f"Popped value: {stack.pop()}")
stack.push(6)
print("Current stack: " + str(stack.current_items()))
stack.push(8)
print("Current stack: " + str(stack.current_items()))
print(f"Popped value: {stack.pop()}")
print("Current stack: " + str(stack.current_items()))

stack.pop()
stack.pop()
stack.pop()
print()

#Returned Values code
stack.push(5)
stack.push(3)

print(f"Popped value: {stack.pop()}")

stack.push(2)
stack.push(8)

print(f"Popped value: {stack.pop()}")
print(f"Popped value: {stack.pop()}")

stack.push(9)
stack.push(1)

print(f"Popped value: {stack.pop()}")

stack.push(7)
stack.push(6)

print(f"Popped value: {stack.pop()}")
print(f"Popped value: {stack.pop()}")

stack.push(4)

print(f"Popped value: {stack.pop()}")
print(f"Popped value: {stack.pop()}")
