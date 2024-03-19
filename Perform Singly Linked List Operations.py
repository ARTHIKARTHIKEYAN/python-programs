class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, key, data):
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.prepend(5)
sll.insert_after(10, 15)

print("Singly Linked List:")
sll.display()

sll.delete(20)
print("After deleting 20:")
sll.display()
