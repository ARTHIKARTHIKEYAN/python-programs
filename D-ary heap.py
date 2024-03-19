class DaryHeap:
    def __init__(self, d):
        self.heap = []
        self.d = d

    def parent(self, i):
        return (i - 1) // self.d

    def child(self, i, j):
        return self.d * i + j + 1

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def delete_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.heapify_down(0)
        return min_val

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            parent_index = self.parent(i)
            self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
            i = parent_index

    def heapify_down(self, i):
        while True:
            min_child = self.min_child(i)
            if min_child is None:
                break
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break

    def min_child(self, i):
        min_child_index = None
        start = self.child(i, 0)
        end = min(start + self.d, len(self.heap))
        for j in range(start, end):
            if min_child_index is None or self.heap[j] < self.heap[min_child_index]:
                min_child_index = j
        return min_child_index

    def print_heap(self):
        print(self.heap)

# Example usage:
d = 3
heap = DaryHeap(d)
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(40)
heap.insert(50)
heap.insert(100)
heap.insert(25)

print("Initial heap:")
heap.print_heap()

print("Deleting min value:", heap.delete_min())
print("Heap after deletion:")
heap.print_heap()
