class DequeWithStacks:
    def __init__(self):
        self.frontStack = []
        self.backStack = []

    def __str__(self):

        combined = self.frontStack[::-1] + self.backStack
        return f"Deque with 2 Stacks: {combined}"

    def __repr__(self):
        return self.__str__()
    def _move_to_stack(self, source, destination):
        while source:
            destination.append(source.pop())

    def add_firstDS(self, value):
        # adds an element to the front of the Deque
        self.frontStack.append(value)

    def add_lastDS(self, value):
        # Adds an element to the back of the deque
        self.backStack.append(value)

    def delete_firstDS(self):
        # deletes the first element
        if not self.frontStack:
            if not self.backStack:
                raise IndexError("pop_front from empty deque")
            self._move_to_stack(self.backStack, self.frontStack)
        return self.frontStack.pop()

    def delete_lastDS(self):
        # deletes the last element
        if not self.backStack:
            if not self.frontStack:  # If both stacks are empty
                raise IndexError("pop_back from empty deque")
            self._move_to_stack(self.frontStack, self.backStack)
        return self.backStack.pop()

    def firstDS(self):
        # returns the first element
        if not self.frontStack:
            if not self.backStack:
                raise IndexError("peek_front from empty deque")
            self._move_to_stack(self.backStack, self.frontStack)
        return self.frontStack[-1]

    def lastDS(self):
        # returns the last element
        if not self.backStack:
            if not self.frontStack:
                raise IndexError("peek_back from empty deque")
            self._move_to_stack(self.frontStack, self.backStack)
        return self.backStack[-1]

    def is_emptyDS(self):
        # checks if the deque is empty
        return not self.frontStack and not self.backStack

    def lenDS(self):
        # returns the length of the deque
        return len(self.frontStack) + len(self.backStack)