class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # Streamline memory usage

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, element):
        """Add element to the top of the stack."""
        new_node = self._Node(element, self._head)
        self._head = new_node
        self._size += 1

    def top(self):
        """Return but do not remove the element at the top of the stack."""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)."""
        if self.is_empty():
            raise Exception("The stack is empty!")
        top_element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return top_element

    @staticmethod
    def evaluate_postfix(expression):
        """Evaluate a postfix expression using a linked stack."""
        stack = LinkedStack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.push(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = LinkedStack.perform_operation(operand1, operand2, token)
                stack.push(result)

        return stack.pop()

    @staticmethod
    def perform_operation(operand1, operand2, operator):
        """Perform arithmetic operations based on the operator."""
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero!")
            return operand1 / operand2  # Use float division for accuracy
        else:
            raise ValueError(f"Unknown operator: {operator}")


def precedence(operator):
    """Return precedence of operators."""
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0


def into_postfix(expression):
    """Convert an infix expression to postfix notation."""
    output = []
    operators = LinkedStack()

    # Remove spaces and tokenize input expression
    tokens = expression.replace(" ", "")

    current_number = ''

    for char in tokens:
        if char.isdigit():
            current_number += char  # Build multi-digit numbers
        else:
            if current_number:
                output.append(current_number)
                current_number = ''
            if char in '+-*/':  # Ensure using standard operators only
                while (not operators.is_empty() and
                       precedence(operators.top()) >= precedence(char)):
                    output.append(operators.pop())
                operators.push(char)
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while not operators.is_empty() and operators.top() != '(':
                    output.append(operators.pop())
                operators.pop()

    if current_number:
        output.append(current_number)

    while not operators.is_empty():
        output.append(operators.pop())

    return ' '.join(output)