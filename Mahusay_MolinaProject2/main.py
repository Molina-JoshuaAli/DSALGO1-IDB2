# Mahusay, Divine Mars
# Molina, Joshua Ali S.
# DSALGO1 Project 2
# IDB2
from LinkedBinaryTree import LinkedBinaryTree as Tree


# Function to perform inorder traversal
def inorder(tree, position):
    if position is not None:
        if tree.left(position) is not None:
            inorder(tree, tree.left(position))
        print(position.element(), end=" ")
        if tree.right(position) is not None:
            inorder(tree, tree.right(position))


# Function to display traversals
def display_traversals(tree):
    print("Preorder traversal:", end=" ")
    for pos in tree.preorder():
        print(pos.element(), end=" ")
    print()

    print("Postorder traversal:", end=" ")
    for pos in tree.postorder():
        print(pos.element(), end=" ")
    print()

    print("Inorder traversal:", end=" ")
    inorder(tree, tree.root())
    print()


# Function to print the tree structure
def print_tree(tree, position, level=0):
    if position is not None:
        print_tree(tree, tree.right(position), level + 1)
        print("    " * level + str(position.element()))
        print_tree(tree, tree.left(position), level + 1)

print("Team project #2 Part A")
# Equation 1: (3 * 5) - ((4 * 5) + (6 - 7))
print("Equation 1:")
tree = Tree()
root = tree._add_root("-")
left_mul = tree._add_left(root, "*")
tree._add_left(left_mul, 3)
tree._add_right(left_mul, 5)

right_add = tree._add_right(root, "+")
right_mul = tree._add_left(right_add, "*")
tree._add_left(right_mul, 4)
tree._add_right(right_mul, 5)

right_sub = tree._add_right(right_add, "-")
tree._add_left(right_sub, 6)
tree._add_right(right_sub, 7)

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print()
# Equation 2: ((a + b) * c) - (d - e)
print("Equation 2:")
tree = Tree()
root = tree._add_root("-")
left_mul = tree._add_left(root, "*")

left_add = tree._add_left(left_mul, "+")
tree._add_left(left_add, "a")
tree._add_right(left_add, "b")

tree._add_right(left_mul, "c")

right_sub = tree._add_right(root, "-")
tree._add_left(right_sub, "d")
tree._add_right(right_sub, "e")

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print()
# Equation 3: ((a ^ b) + (c + d)) + ((e * f) / (g + h))
print("Equation 3:")
tree = Tree()
root = tree._add_root("+")
left_add = tree._add_left(root, "+")
left_exp = tree._add_left(left_add, "^")
tree._add_left(left_exp, "a")
tree._add_right(left_exp, "b")

right_add = tree._add_right(left_add, "+")
tree._add_left(right_add, "c")
tree._add_right(right_add, "d")

right_div = tree._add_right(root, "/")
right_mul = tree._add_left(right_div, "*")
tree._add_left(right_mul, "e")
tree._add_right(right_mul, "f")

right_add2 = tree._add_right(right_div, "+")
tree._add_left(right_add2, "g")
tree._add_right(right_add2, "h")

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print()
# Equation 4: (a + b) / (c * (d - (e ^ f)))
print("Equation 4:")
tree = Tree()
root = tree._add_root("/")
left_add = tree._add_left(root, "+")
tree._add_left(left_add, "a")
tree._add_right(left_add, "b")

right_mul = tree._add_right(root, "*")
tree._add_left(right_mul, "c")

right_sub = tree._add_right(right_mul, "-")
tree._add_left(right_sub, "d")

right_exp = tree._add_right(right_sub, "^")
tree._add_left(right_exp, "e")
tree._add_right(right_exp, "f")

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print()
# Equation 5: ((a - b) + c) * ((d + e) * (f / g))
print("Equation 5:")
tree = Tree()
root = tree._add_root("*")

left_add = tree._add_left(root, "+")
left_sub = tree._add_left(left_add, "-")
tree._add_left(left_sub, "a")
tree._add_right(left_sub, "b")
tree._add_right(left_add, "c")

right_mul = tree._add_right(root, "*")
right_add = tree._add_left(right_mul, "+")
tree._add_left(right_add, "d")
tree._add_right(right_add, "e")

right_div = tree._add_right(right_mul, "/")
tree._add_left(right_div, "f")
tree._add_right(right_div, "g")

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print()
# Equation 6: (((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1))) * 8
print("Equation 6:")
tree = Tree()
root = tree._add_root("*")

# Left subtree: (((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1)))
left_div = tree._add_left(root, "/")
left_mul = tree._add_left(left_div, "*")

left_add = tree._add_left(left_mul, "+")
tree._add_left(left_add, 5)
tree._add_right(left_add, 2)

left_sub = tree._add_right(left_mul, "-")
tree._add_left(left_sub, 2)
tree._add_right(left_sub, 1)

right_add1 = tree._add_right(left_div, "+")
right_add2 = tree._add_left(right_add1, "+")
tree._add_left(right_add2, 2)
tree._add_right(right_add2, 9)

right_sub = tree._add_right(right_add1, "-")
left_sub2 = tree._add_left(right_sub, "-")
tree._add_left(left_sub2, 7)
tree._add_right(left_sub2, 2)
tree._add_right(right_sub, 1)

# Right subtree: *8
tree._add_right(root, 8)

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print("Team project #2 Part B")
print("Matrix 1:")
tree = Tree()
root = tree._add_root("r")
a = tree._add_left(root, "a")

b = tree._add_left(a, "b")
tree._add_right(b, "d")

c = tree._add_right(a, "c")
f = tree._add_right(c, "f")

e = tree._add_left(c, "e")
g = tree._add_right(e, "g")
h = tree._add_right(g, "h")
display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()


print("Matrix 2:")
tree = Tree()
root = tree._add_root("r")
a = tree._add_left(root, "a")
b = tree._add_right(root, "b")
tree._add_left(a, "c")
tree._add_right(a, "d")

e = tree._add_right(b, "e")
f = tree._add_right(e, "f")
g = tree._add_right(f, "g")
display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print("Matrix 3:")
tree = Tree()
root = tree._add_root("r")
a = tree._add_left(root, "a")
b = tree._add_right(root, "b")

c = tree._add_right(a, "c")

f = tree._add_left(c, "f")

d = tree._add_left(b, "d")
e = tree._add_right(b, "e")

display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()

print("Matrix 4:")
tree = Tree()
root = tree._add_root("r")
a = tree._add_left(root, "a")
b = tree._add_right(root, "b")

c = tree._add_left(a, "c")
d = tree._add_right(a, "d")
g= tree._add_left(c, "g")
h= tree._add_right(c, "h")

e = tree._add_left(b, "e")
f = tree._add_right(b, "f")
i = tree._add_left(e, "i")
display_traversals(tree)
print("Tree structure:")
print_tree(tree, tree.root())
print()
