class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        return len(str(key)) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        hash = hash_value
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
                return
            hash_value = (hash_value + 1) % self.size
            if hash_value == hash:
                raise RuntimeError("Hash table is full")
        self.slots[hash_value] = key
        self.data[hash_value] = value

    def get(self, key, default=None):
        hash_value = self._hash(key)
        hash = hash_value
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            hash_value = (hash_value + 1) % self.size
            if hash_value == hash:
                break
        return default

    def remove(self, key):
        hash_value = self._hash(key)
        hash = hash_value
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                self.slots[hash_value] = None
                self.data[hash_value] = None
                return
            hash_value = (hash_value + 1) % self.size
            if hash_value == hash:
                break

    def keys(self):
        return [key for key in self.slots if key is not None]

    def values(self):
        return [value for value in self.data if value is not None]

    def items(self):
        return [(self.slots[i], self.data[i])
                for i in range(self.size)
                if self.slots[i] is not None]

my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")
print("Keys:", my_hashmap.keys())
print("Values:", my_hashmap.values())
print("Items:", my_hashmap.items())
print("Name:", my_hashmap.get("name"))
print("Gender:", my_hashmap.get("gender", "Not specified"))
my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())