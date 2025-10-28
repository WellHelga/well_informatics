class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            raise IndexError()
        root = self.heap[0]
        last_element = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_element
            self._heapify_down(0)
        return root

    def peek(self):
        if self.is_empty():
            raise IndexError()
        return self.heap[0]

    def _heapify_up(self, index):
        index2 = (index - 1) // 2
        if self.max_heap:
            should_swap = self.heap[index] > self.heap[index2]
        else:
            should_swap = self.heap[index] < self.heap[index2]
        if index > 0 and should_swap:
            self.heap[index], self.heap[index2] = self.heap[index2], self.heap[index]
            self._heapify_up(index2)

    def _heapify_down(self, index):
        lt_child = 2 * index + 1
        rt_child = 2 * index + 2
        x = index
        if self.max_heap:
            if lt_child < self.size() and self.heap[lt_child] > self.heap[x]:
                x = lt_child
            if rt_child < self.size() and self.heap[rt_child] > self.heap[x]:
                x = rt_child
        else:
            if lt_child < self.size() and self.heap[lt_child] < self.heap[x]:
                x = lt_child
            if rt_child < self.size() and self.heap[rt_child] < self.heap[x]:
                x = rt_child
        if x != index:
            self.heap[index], self.heap[x] = self.heap[x], self.heap[index]
            self._heapify_down(x)

h = Heap(max_heap=True)
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)
print("Корень кучи:", h.peek())
while not h.is_empty():
    print("Извлеченный элемент:", h.extract())