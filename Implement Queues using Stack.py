class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                print("Queue is empty")
                return None
            else:
                while self.enqueue_stack:
                    self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack

    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def peek(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                print("Queue is empty")
                return None
            else:
                while self.enqueue_stack:
                    self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Front element:", queue.peek())

print("Dequeuing:", queue.dequeue())
print("Dequeuing:", queue.dequeue())
print("Queue size:", queue.size())
