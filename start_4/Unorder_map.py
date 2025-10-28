class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return len(str(key)) % self.size

    def set(self, key, value):
        x = self._hash(key)
        y = self.buckets[x]
        for pair in y:
            if pair.key == key:
                pair.value = value
                return
        y.append(KeyValuePair(key, value))

    def get(self, key, default=None):
        x = self._hash(key)
        y = self.buckets[x]
        for i in y:
            if i.key == key:
                return i.value
        return default

    def remove(self, key):
        x = self._hash(key)
        y = self.buckets[x]
        for i, j in enumerate(y):
            if j.key == key:
                del y[i]
                return

    def keys(self):
        keys2 = []
        for y in self.buckets:
            for i in y:
                keys2.append(i.key)
        return keys2

    def values(self):
        values2 = []
        for y in self.buckets:
            for i in y:
                values2.append(i.value)
        return values2

    def items(self):
        items2 = []
        for y in self.buckets:
            for i in y:
                items2.append((i.key, i.value))
        return items2

my_map = UnorderedMap()
my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")
print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))
my_map.remove("age")
print("Keys after removing 'age':", my_map.keys())