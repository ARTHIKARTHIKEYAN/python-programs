class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        deleted_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return deleted_value

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] < self.heap[smallest]):
            smallest = left_child_index
        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] < self.heap[smallest]):
            smallest = right_child_index
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

# Example usage:
heap = BinaryHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(5)
heap.insert(4)

print("Heap elements:", heap.heap)

print("Deleting the minimum element:", heap.delete())
print("Heap elements after deletion:", heap.heap)

print("Peek at the minimum element:", heap.peek())
