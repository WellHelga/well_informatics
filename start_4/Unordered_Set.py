class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return len(str(value)) % self.size

    def add(self, value):
        x = self._hash(value)
        y = self.buckets[x]
        if value not in y:
            y.append(value)

    def remove(self, value):
        x = self._hash(value)
        y = self.buckets[x]
        if value in y:
            y.remove(value)

    def contains(self, value):
        x = self._hash(value)
        y = self.buckets[x]
        return value in y

    def elements(self):
        elements2 = []
        for y in self.buckets:
            elements2.extend(y)
        return elements2

my_set = UnorderedSet()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("Elements:", my_set.elements())
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")
value_to_remove = 1
my_set.remove(value_to_remove)
print("Elements after removing 1:", my_set.elements())