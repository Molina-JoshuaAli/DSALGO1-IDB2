#Molina, Joshua Ali S.
#DSALGO1
#IDB2
#11/15/2024

#Activity1Finals

from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList


CircQ = CircularQueue()

P = PositionalList()
'''
#Adding elements to the stack
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

#Removing elements from the stack
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())

#Adding elements to the Queue
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)

#Removing elements from the Queue
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
'''
'''
#adding elements to the Circular Queue
CircQ.enqueue(1)
CircQ.enqueue(2)
CircQ.enqueue(3)
#printing elements from the Circular Queue
CircQ.rotate()
print(CircQ.dequeue())
print(CircQ.dequeue())
print(CircQ.dequeue())
'''
'''
#adding elements to the Deque
D.insert_first(1)
D.insert_first(2)
D.insert_first(3)
#removing elements from the Deque
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
'''
Q = Queue()
D = Deque()
S = Stack()

# Initialize the deque with the starting elements
D.insert_first(8)
D.insert_first(7)
D.insert_first(6)
D.insert_first(5)
D.insert_first(4)
D.insert_first(3)
D.insert_first(2)
D.insert_first(1)

print("#1 Starting elements:")
print("D =", D)
print("Q =", Q)

Q.enqueue(D.delete_last())

Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())

Q.enqueue(D.delete_last())

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())

D.insert_last(Q.dequeue())

Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())

D.insert_first(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())

Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())

print("Final state:")
print("D =", D)
print("Q =", Q)

D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.insert_first(8)
D.insert_first(7)
D.insert_first(6)
D.insert_first(5)
D.insert_first(4)
D.insert_first(3)
D.insert_first(2)
D.insert_first(1)

print("")

print("#2 Starting elements: ")
print("D= ",D)
print("S= ", S)

S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())

D.insert_first(D.delete_last())
D.insert_first(D.delete_last())
S.push(D.delete_first())
S.push(D.delete_first())

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())

S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())

print("Final state:")
print("D =", D)
print("S =", S)
