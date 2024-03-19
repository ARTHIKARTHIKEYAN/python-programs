class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = last
            last.next = new_node
            self.head = new_node

    def insert_after(self, key, data):
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                next_node = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next = next_node
                next_node.prev = new_node
                break
            current = current.next
            if current == self.head:
                break

    def delete(self, key):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == key:
                if current.next == self.head:
                    if current.prev == current:
                        self.head = None
                    else:
                        last = current.prev
                        last.next = self.head
                        self.head.prev = last
                        self.head = self.head.next
                else:
                    prev_node = current.prev
                    next_node = current.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                break
            current = current.next
            if current == self.head:
                break

    def display(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage:
cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.prepend(5)
cdll.insert_after(10, 15)

print("Circular Doubly Linked List:")
cdll.display()

cdll.delete(20)
print("After deleting 20:")
cdll.display()
