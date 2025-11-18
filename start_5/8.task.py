test_cases = [
    ([(2, 10), (3, 15), (5, 30)], 5, 30),
    ([(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)], 10, 50),
    ([(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)], 7, 55)
]
def recurs(items, capacity, i=0):
    if i >= len(items) or capacity <= 0:
        return 0
    weight, value = items[i]
    x = recurs(items, capacity, i + 1)
    if weight <= capacity:
        x_items = value + recurs(items, capacity - weight, i + 1)
        return max(x, x_items)
    else:
        return x
for items, capacity2, expected in test_cases:
    res = recurs(items, capacity2)
    print(res)

if __name__ == "__main__":
    pass