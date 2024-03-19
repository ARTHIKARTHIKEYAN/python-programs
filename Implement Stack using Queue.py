class StackUsingQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if not self.queue1:
            print("Stack is empty")
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped_item = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item

    def is_empty(self):
        return not self.queue1

    def size(self):
        return len(self.queue1)

    def top(self):
        if not self.queue1:
            print("Stack is empty")
            return None
        return self.queue1[-1]

# Example usage:
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element:", stack.top())

print("Popping:", stack.pop())
print("Stack size:", stack.size())
