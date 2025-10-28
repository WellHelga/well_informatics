class SimpleMap:
    def __init__(self):
        self._data = []

    def set(self, key, value):
        for i in range(len(self._data)):
            if self._data[i][0] == key:
                self._data[i] = (key, value)
                return
        self._data.append((key, value))

    def get(self, key, default=None):
        for k, v in self._data:
            if k == key:
                return v
        return default

    def remove(self, key):
        for i in range(len(self._data)):
            if self._data[i][0] == key:
                del self._data[i]
                return

    def keys(self):
        return [pair[0] for pair in self._data]

    def values(self):
        return [pair[1] for pair in self._data]

    def items(self):
        return [(k, v) for k, v in self._data]

my_map = SimpleMap()
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