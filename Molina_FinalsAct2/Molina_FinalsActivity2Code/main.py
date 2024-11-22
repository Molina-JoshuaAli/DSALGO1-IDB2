# Molina, Joshua Ali S.
# IDB2 DSALGO1
# Finals Activity #2

from LinkedStack import LinkedStack as Stack, into_postfix
from PositionalList import PositionalList as PositionalList


#1 Infix to Postfix
S = Stack()
print("#1")
infix_expression = input("Enter an infix expression: ")

postfix_expression = into_postfix(infix_expression)

print(f"The postfix expression is: '{postfix_expression}'")

print()

#2 Sort positional list
print("#2")
P = PositionalList()

numbers = [1, 72, 81, 25, 65, 91, 11]
for number in numbers:
    P.add_last(number)

def insertion_sort(L):
    """Sort the PositionalList in ascending order using insertion sort."""
    if len(L) > 1:  # Otherwise, no need to sort
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # Next item to place
            value = pivot.element()
            if value >= marker.element():  # Pivot is already sorted
                marker = pivot  # Pivot becomes the new marker
            else:  # Must relocate pivot
                walk = marker  # Find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)  # Remove pivot
                L.add_before(walk, value)  # Reinsert pivot

# Define the insertion sort function (descending order)
def insertion_sort_descending(L):
    """Sort the PositionalList in descending order using insertion sort."""
    if len(L) > 1:  # Otherwise, no need to sort
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # Next item to place
            value = pivot.element()
            if value <= marker.element():  # Pivot is already sorted
                marker = pivot  # Pivot becomes the new marker
            else:  # Must relocate pivot
                walk = marker  # Find the leftmost value smaller than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)  # Remove pivot
                L.add_before(walk, value)  # Reinsert pivot

def printList():
    for x in P:
        print(x, end=" ")

# Initial List
print("Initial List:")
printList()
print()

# Ascending order
insertion_sort(P)
print("Ascending order:")
printList()
print()

# Descending order
insertion_sort_descending(P)
print("Descending order:")
printList()
print()
