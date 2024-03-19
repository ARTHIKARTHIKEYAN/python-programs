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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def convert_to_circular_linked_list(sll):
    if not sll.head:
        print("Empty singly linked list")
        return
    current = sll.head
    while current.next:
        current = current.next
    current.next = sll.head

# Example usage:
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)

print("Singly Linked List:")
sll.display()

convert_to_circular_linked_list(sll)

print("Circular Linked List:")
current = sll.head
while current:
    print(current.data, end=" ")
    current = current.next
    if current == sll.head:
        break
print()
