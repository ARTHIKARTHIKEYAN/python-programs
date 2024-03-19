class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, key, data):
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                next_node = current.next
                current.next = new_node
                new_node.next = next_node
                break
            current = current.next
            if current == self.head:
                break

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev_node = None
            while current.next != self.head:
                if current.data == key:
                    prev_node.next = current.next
                    break
                prev_node = current
                current = current.next
            if current.data == key:
                prev_node.next = current.next

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
csll = CircularSinglyLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.prepend(5)
csll.insert_after(10, 15)

print("Circular Singly Linked List:")
csll.display()

csll.delete(20)
print("After deleting 20:")
csll.display()
