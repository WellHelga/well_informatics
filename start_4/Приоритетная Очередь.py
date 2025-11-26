class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((item, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        priority_index = 0
        for i in range(1, len(self.elements)):
            if self.elements[i][1] < self.elements[priority_index][1]:
                highest_priority_index = i
        item, _ = self.elements.pop(priority_index)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        priority_item = self.elements[0][0]
        priority2 = self.elements[0][1]
        for item, priority in self.elements:
            if priority < priority2:
                priority2 = priority
                priority_item = item
        return priority_item

    def size(self):
        return len(self.elements)

pq = PriorityQueue()

pq.push("Задача 1", priority=2)
pq.push("Задача 2", priority=5)
pq.push("Задача 3", priority=1)

print(pq.peek())

while not pq.is_empty():
    print(pq.pop())