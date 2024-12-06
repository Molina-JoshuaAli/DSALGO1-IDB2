# Mahusay, Divine Mars
# Molina, Joshua Ali S.
# Team Project #1 Finals
# 11/29/2024

from DequeWithStacks import DequeWithStacks as DequeStacks
from DequeWithStacksAndQueue import DequeWithStacksAndQueue as DequeStacksQueue

# In this code, DS stands for Deque with stacks
# DSQ stands for Deque with Stacks and Queues

# Deque with 2 Stack implementations
print("Deque with 2 Stack implementations")
DS = DequeStacks()

DS.add_firstDS(1)
DS.add_firstDS(2)
DS.add_lastDS(4)
DS.add_firstDS(10)
print("Delete element", DS.delete_lastDS())
print("The length is: ", DS.lenDS())
print(DS.is_emptyDS())
DS.add_firstDS(9)
DS.add_lastDS(5)

print(DS)

print()


# Deque with Stack and Queue implementations
print("Deque with Stack and Queue implementations")
DSQ = DequeStacksQueue()

DSQ.add_firstDSQ(4)
print("The length is: ", DSQ.lenDSQ())
print("Delete element", DSQ.delete_lastDSQ())
DSQ.add_lastDSQ(1)
DSQ.add_firstDSQ(9)
print("The length is: ", DSQ.lenDSQ())
DSQ.add_firstDSQ(3)
DSQ.add_firstDSQ(434)
DSQ.add_lastDSQ(2)

print(DSQ)

