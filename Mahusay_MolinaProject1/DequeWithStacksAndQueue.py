from LinkedStack import LinkedStack as LinkedStack
from LinkedQueue import LinkedQueue as LinkedQueue
class DequeWithStacksAndQueue:
    def __init__(self):
        self.frontStack = LinkedStack()
        self.backStack = LinkedStack()
        self.queue = LinkedQueue()

    def _move_to_stack(self, source, destination):
        while not source.is_empty():
            destination.push(source.pop())

    def __str__(self):
        elements = []

        temp_stack = LinkedStack()
        while not self.frontStack.is_empty():
            temp_stack.push(self.frontStack.pop())
        while not temp_stack.is_empty():
            value = temp_stack.pop()
            elements.append(value)
            self.frontStack.push(value)

        temp_stack = LinkedStack()
        while not self.backStack.is_empty():
            temp_stack.push(self.backStack.pop())
        while not temp_stack.is_empty():
            value = temp_stack.pop()
            elements.append(value)
            self.backStack.push(value)

        return f"Deque with Stacks and Queue: {elements}"

    def __repr__(self):
        return self.__str__()

    def add_firstDSQ(self, value):
        # Adds an element to the front of the Deque
        self.frontStack.push(value)

    def add_lastDSQ(self, value):
        # Adds an element to the back of the Deque
        self.backStack.push(value)

    def delete_firstDSQ(self):
        # Deletes the first element
        if self.frontStack.is_empty():
            if self.backStack.is_empty():
                raise IndexError("delete_first from empty deque")
            self._move_to_stack(self.backStack, self.frontStack)
        return self.frontStack.pop()

    def delete_lastDSQ(self):
        # Deletes the last element
        if self.backStack.is_empty():
            if self.frontStack.is_empty():
                raise IndexError("delete_last from empty deque")
            self._move_to_stack(self.frontStack, self.backStack)
        return self.backStack.pop()

    def firstDSQ(self):
        # Returns the first element
        if self.frontStack.is_empty():
            if self.backStack.is_empty():
                raise IndexError("first from empty deque")
            self._move_to_stack(self.backStack, self.frontStack)
        return self.frontStack.peek()

    def lastDSQ(self):
        # Returns the last element
        if self.backStack.is_empty():
            if self.frontStack.is_empty():
                raise IndexError("last from empty deque")
            self._move_to_stack(self.frontStack, self.backStack)
        return self.backStack.peek()

    def is_emptyDSQ(self):
        # Checks if the Deque is empty
        return self.frontStack.is_empty() and self.backStack.is_empty()

    def lenDSQ(self):
        # Retuns the length of the deque
        return len(self.frontStack) + len(self.backStack)