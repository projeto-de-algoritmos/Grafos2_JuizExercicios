class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._shift_up()

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)

        return min_value

    def _shift_up(self):
        index = len(self.heap) - 1

        while index > 0:
            element = self.heap[index]
            parent_index = (index - 1) // 2
            parent = self.heap[parent_index]

            if element < parent:
                self.heap[index] = parent
                self.heap[parent_index] = element
                index = parent_index
            else:
                break

    def _heapify(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] < self.heap[smallest_index]):
            smallest_index = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] < self.heap[smallest_index]):
            smallest_index = right_child_index

        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._heapify(smallest_index)

# Exemplo de uso:
heap = MinHeap()
heap.push(4)
heap.push(1)
heap.push(7)
heap.push(9)
heap.push(2)
print(heap.pop())  # 1
print(heap.pop())  # 2
print(heap.pop())  # 4
print(heap.pop())  # 7
print(heap.pop())  # 9
