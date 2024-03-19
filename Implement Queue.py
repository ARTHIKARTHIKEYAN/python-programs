class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())
print("Front element:", q.peek())

print("Dequeuing:", q.dequeue())
print("Queue size:", q.size())
