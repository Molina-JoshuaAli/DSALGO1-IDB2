class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "THE QUEUE IS EMPTY!!!!"
        return self.queue.pop(0)

    def first(self):
        if self.is_empty():
            return "THE QUEUE IS EMPTY!!!! "
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def display(self):
        return str(self.queue)

# Simulation
q = Queue()
q.enqueue(5)
print("The queue contains: " + q.display())
q.enqueue(3)
print("The queue contains: " + q.display())
print("The length of the queue is: " + str(len(q)))
print("Dequeued item: " + str(q.dequeue()))
print("Is the queue empty? " + str(q.is_empty()))
print("Dequeued item: " + str(q.dequeue()))
print("Is the queue empty? " + str(q.is_empty()))
print(str(q.dequeue()))
q.enqueue(7)
print("The queue contains: " + q.display())
q.enqueue(9)
print("The queue contains: " + q.display())
print("The first item in the queue is: " + str(q.first()))
q.enqueue(9)
print("The queue contains: " + q.display())
print("The length of the queue is: " + str(len(q)))
print("Dequeued item: " + str(q.dequeue()))
print("The final queue is: " + q.display())


print()
print("=========================================")
print()

# Resets the queue
q.dequeue()
q.dequeue()


# Print returned values
q.enqueue(5)
q.enqueue(3)
print("Returned value: " + str(q.dequeue()))
q.enqueue(2)
q.enqueue(8)
print("Returned value: " + str(q.dequeue()))
print("Returned value: " + str(q.dequeue()))
q.enqueue(9)
q.enqueue(1)
print("Returned value: " + str(q.dequeue()))
q.enqueue(7)
q.enqueue(6)
print("Returned value: " + str(q.dequeue()))
print("Returned value: " + str(q.dequeue()))
q.enqueue(4)
print("Returned value: " + str(q.dequeue()))
print("Returned value: " + str(q.dequeue()))
