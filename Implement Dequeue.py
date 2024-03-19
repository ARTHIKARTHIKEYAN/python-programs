class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Deque is empty")
            return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Deque is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Deque is empty")
            return None

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Deque is empty")
            return None

# Example usage:
deque = Deque()
deque.add_front(1)
deque.add_front(2)
deque.add_rear(3)
deque.add_rear(4)

print("Deque size:", deque.size())
print("Front element:", deque.peek_front())
print("Rear element:", deque.peek_rear())

print("Removing front:", deque.remove_front())
print("Removing rear:", deque.remove_rear())
print("Deque size:", deque.size())
