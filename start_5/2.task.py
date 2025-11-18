flowers_set = [
    {"rose", "jasmine", "lily"},
    {"orchid", "tulip", "violet", "daisy"},
    {"lavender", "sunflower"}
]
for i, flowers in enumerate(flowers_set, 1):
    n = len(flowers)
    print(2 ** n - 1)